    # -*- coding: utf-8 -*-
"""
Created on Tue Oct 10

@author: jaehyuk
"""

import numpy as np
import scipy.stats as ss
import scipy.optimize as sopt
from . import normal
from . import bsm

import pyfeng as pf

'''
MC model class for Beta=1
'''

class ModelBsmMC:
    beta = 1.0   # fixed (not used)
    vov, rho = 0.0, 0.0
    sigma, intr, divr = None, None, None
    bsm_model = None
    '''
    You may define more members for MC: time step, etc
    '''
    
    def __init__(self, sigma, vov=0, rho=0.0, beta=1.0, intr=0, divr=0):
        self.sigma = sigma
        self.vov = vov
        self.rho = rho
        self.intr = intr
        self.divr = divr
        self.bsm_model = pf.Bsm(sigma, intr=intr, divr=divr)
        
    def bsm_vol(self, strike, spot, cp=1, texp=None, sigma=None):
        ''''
        From the price from self.price() compute the implied vol
        this is the opposite of bsm_vol in ModelHagan class
        use bsm_model
        '''
        bsm_model = bsm.Model(texp=texp,vol=self.sigma,intr=self.intr,divr=self.divr)
        price_in = self.price(strike, spot, texp, sigma)
        impvol_m = []
        for i in range(len(price_in)):
            impvol_m.append(bsm_model.impvol(price_in[i], strike[i], spot, texp, cp))
        
        return impvol_m
    
    def price(self, strike, spot, texp=None, sigma=None, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol and price first. Then get prices (vector) for all strikes
        You may fix the random number seed
        '''
        np.random.seed(12345)
        
        npath = 10000
        nstep = 365
        dt = texp / nstep
        cor_m = np.array([[1,self.rho],[self.rho,1]])
        cov_m = cor_m 
        chol_m = np.linalg.cholesky(cov_m)
        
        vov = self.vov
        sigma = self.sigma

        St = spot * np.ones((nstep+1, npath))
        vol = sigma * np.ones((nstep+1, npath))
        strike_m = strike[:,None] * np.ones((strike.size, npath))
        
        
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=[2, npath]) # 生成二维独立随机变量
            znorm_correlated = chol_m @ znorm_m # 生成二维相关随机变量

            St[k + 1, :] = St[k, :] * np.exp( vol[k,:] * np.sqrt(dt) * znorm_correlated[0,:]- 1/2 * dt * vol[k,:]**2 )
            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_correlated[1,:]-1/2 * (self.vov**2)*dt)
        
        opt_price = np.mean( np.fmax(cp*(St[-1,:] - strike_m), 0),axis=1 )
        
        return opt_price
    
    def variance(self, strike, spot, texp=None, sigma=None, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol and price first. Then get prices (vector) for all strikes
        You should not use the random number seed
        '''
        
        npath = 10000
        nstep = 365
        dt = texp / nstep
        cor_m = np.array([[1,self.rho],[self.rho,1]])
        cov_m = cor_m 
        chol_m = np.linalg.cholesky(cov_m)
        
        vov = self.vov
        sigma = self.sigma

        St = spot * np.ones((nstep+1, npath))
        vol = sigma * np.ones((nstep+1, npath))
        strike_m = strike[:,None] * np.ones((strike.size, npath))
        
        
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=[2, npath]) # 生成二维独立随机变量
            znorm_correlated = chol_m @ znorm_m # 生成二维相关随机变量

            St[k + 1, :] = St[k, :] * np.exp( vol[k,:] * np.sqrt(dt) * znorm_correlated[0,:]- 1/2 * dt * vol[k,:]**2 )
            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_correlated[1,:]-1/2 * (self.vov**2)*dt)
        
        opt_npath = np.fmax(cp*(St[-1,:] - strike_m), 0)
        var_mc = np.var(opt_npath, axis = 1)
        
        return var_mc

'''
MC model class for Beta=0
'''
class ModelNormalMC:
    beta = 0.0   # fixed (not used)
    vov, rho = 0.0, 0.0
    sigma, intr, divr = None, None, None
    normal_model = None
    
    def __init__(self, sigma, vov=0, rho=0.0, beta=0.0, intr=0, divr=0):
        self.sigma = sigma
        self.vov = vov
        self.rho = rho
        self.intr = intr
        self.divr = divr
        self.normal_model = pf.Norm(sigma, intr=intr, divr=divr)
        
    def norm_vol(self, strike, spot, texp=None, sigma=None):
        ''''
        From the price from self.price() compute the implied vol
        this is the opposite of normal_vol in ModelNormalHagan class
        use normal_model 
        '''
        normal_model = normal.Model(texp=texp,vol=self.sigma,intr=self.intr,divr=self.divr)
        price_in = self.price(strike, spot, texp, sigma)
        impvol_m = []
        for i in range(len(price_in)):
            impvol_m.append(normal_model.impvol(price_in[i], strike[i], spot, texp))
        
        return impvol_m
        
    def price(self, strike, spot, texp=None, sigma=None, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol and price first. Then get prices (vector) for all strikes
        You may fix the random number seed
        '''
        np.random.seed(12345)
        
        npath = 10000
        nstep = 365
        dt = texp / nstep
        cor_m = np.array([[1,self.rho],[self.rho,1]])
        cov_m = cor_m 
        chol_m = np.linalg.cholesky(cov_m)
        
        vov = self.vov
        sigma = self.sigma

        St = spot * np.ones((nstep+1, npath))
        vol = sigma * np.ones((nstep+1, npath))
        strike_m = strike[:,None] * np.ones((strike.size, npath))
        
        
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=[2, npath]) # 生成二维独立随机变量
            znorm_correlated = chol_m @ znorm_m # 生成二维相关随机变量

            St[k + 1, :] = St[k, :] + vol[k,:] * np.sqrt(dt) * znorm_correlated[0,:]
            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_correlated[1,:]-1/2 * (self.vov**2)*dt)
        
        
        opt_price = np.mean( np.fmax(cp*(St[-1,:] - strike_m), 0),axis=1 )
        
        return opt_price
    
    def variance(self, strike, spot, texp=None, sigma=None, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol and price first. Then get prices (vector) for all strikes
        You should not use the random number seed
        '''
        
        npath = 10000
        nstep = 365
        dt = texp / nstep
        cor_m = np.array([[1,self.rho],[self.rho,1]])
        cov_m = cor_m 
        chol_m = np.linalg.cholesky(cov_m)
        
        vov = self.vov
        sigma = self.sigma

        St = spot * np.ones((nstep+1, npath))
        vol = sigma * np.ones((nstep+1, npath))
        strike_m = strike[:,None] * np.ones((strike.size, npath))
        
        
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=[2, npath]) # 生成二维独立随机变量
            znorm_correlated = chol_m @ znorm_m # 生成二维相关随机变量

            St[k + 1, :] = St[k, :] + vol[k,:] * np.sqrt(dt) * znorm_correlated[0,:]
            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_correlated[1,:]-1/2 * (self.vov**2)*dt)
        
        opt_npath = np.fmax(cp*(St[-1,:] - strike_m), 0)
        var_mc = np.var(opt_npath, axis = 1)
        
        return var_mc

'''
Conditional MC model class for Beta=1
'''
class ModelBsmCondMC:
    beta = 1.0   # fixed (not used)
    vov, rho = 0.0, 0.0
    sigma, intr, divr = None, None, None
    bsm_model = None
    '''
    You may define more members for MC: time step, etc
    '''
    
    def __init__(self, sigma, vov=0, rho=0.0, beta=1.0, intr=0, divr=0):
        self.sigma = sigma
        self.vov = vov
        self.rho = rho
        self.intr = intr
        self.divr = divr
        self.bsm_model = pf.Bsm(sigma, intr=intr, divr=divr)
        
    def bsm_vol(self, strike, spot, texp=None):
        ''''
        From the price from self.price() compute the implied vol
        this is the opposite of bsm_vol in ModelHagan class
        use bsm_model
        should be same as bsm_vol method in ModelBsmMC (just copy & paste)
        '''
        return 0
    
    def price(self, strike, spot, texp=None, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol only. Then compute integrated variance and BSM price.
        Then get prices (vector) for all strikes
        You may fix the random number seed
        '''
        np.random.seed(12345)
        
        npath = 10000
        nstep = 365 * texp
        dt = texp / nstep
       
        
        vov = self.vov
        sigma = self.sigma

        
        vol = sigma * np.ones((nstep+1, npath))
        strike_m = strike[:,None] * np.ones((strike.size, npath))
        
        
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=(npath)) 

            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_m-1/2 * (vov**2)*dt)
            
        opt_price = []
        N = vol.shape[0]-1
        weight = 4*np.ones(N+1)
        weight[::2] = 2
        weight[0] = 1
        weight[-1] = 1
        IT = (weight @ (vol**2))/ (3*N)
        spot_new = spot * np.exp(self.rho/vov *(vol[-1,:]-vol[0,:])-(self.rho*sigma)**2 * texp *IT/2)
        sigma_new = sigma * np.sqrt((1-self.rho**2)*IT)

        for s in strike:
            opt_npath = bsm.price(s, spot_new, texp = texp, vol = sigma_new, intr = self.intr, divr = self.divr, cp_sign = cp)
            opt_price.append( np.mean( opt_npath ) )
        
        return opt_price
    
    def variance(self, strike, spot, texp=None, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol only. Then compute integrated variance and BSM price.
        Then get prices (vector) for all strikes
        You should not use the random number seed
        '''
        
        npath = 10000
        nstep = 365 * texp
        dt = texp / nstep
       
        
        vov = self.vov
        sigma = self.sigma

        
        vol = sigma * np.ones((nstep+1, npath))
        strike_m = strike[:,None] * np.ones((strike.size, npath))
        
        
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=(npath)) 

            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_m-1/2 * (vov**2)*dt)
            
        var_mc = []
        N = vol.shape[0]-1
        weight = 4*np.ones(N+1)
        weight[::2] = 2
        weight[0] = 1
        weight[-1] = 1
        IT = (weight @ (vol**2))/ (3*N)
        spot_new = spot * np.exp(self.rho/vov *(vol[-1,:]-vol[0,:])-(self.rho*sigma)**2 * texp *IT/2)
        sigma_new = sigma * np.sqrt((1-self.rho**2)*IT)

        for s in strike:
            opt_npath = bsm.price(s, spot_new, texp = texp, vol = sigma_new, intr = self.intr, divr = self.divr, cp_sign = cp)
            var_mc.append( np.var( opt_npath ) )
        
        return var_mc

    
'''
Conditional MC model class for Beta=0
'''
class ModelNormalCondMC:
    beta = 0.0   # fixed (not used)
    vov, rho = 0.0, 0.0
    sigma, intr, divr = None, None, None
    normal_model = None
    
    def __init__(self, sigma, vov=0, rho=0.0, beta=0.0, intr=0, divr=0):
        self.sigma = sigma
        self.vov = vov
        self.rho = rho
        self.intr = intr
        self.divr = divr
        self.normal_model = pf.Norm(sigma, intr=intr, divr=divr)
        
    def norm_vol(self, strike, spot, texp=None):
        ''''
        From the price from self.price() compute the implied vol
        this is the opposite of normal_vol in ModelNormalHagan class
        use normal_model
        should be same as norm_vol method in ModelNormalMC (just copy & paste)
        '''
        return 0
        
    def price(self, strike, spot, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol only. Then compute integrated variance and normal price.
        You may fix the random number seed
        '''
        np.random.seed(12345)
        
        npath = 10000
        nstep = 365 * texp
        dt = texp / nstep
          
        vov = self.vov
        sigma = self.sigma
        vol = sigma * np.ones((nstep+1, npath))
         
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=(npath)) 
            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_m-1/2 * (vov**2)*dt)
            
        opt_price = []
        N = vol.shape[0]-1
        weight = 2*np.ones(N+1)
        weight[0] = 1
        weight[-1] = 1
        IT = (weight @ (vol**2))/ (2*N)
        spot_new = spot + self.rho/vov *(vol[-1,:]-vol[0,:])
        sigma_new = sigma * np.sqrt((1-self.rho**2)*IT)

        for s in strike:
            opt_npath = normal.price(strike=s, spot=spot_new, texp = texp, vol = sigma_new, intr = self.intr, divr = self.divr, cp_sign = cp)
            opt_price.append( np.mean( opt_npath ) )
        
        
        return opt_price
    
    def variance(self, strike, spot, cp=1):
        '''
        Your MC routine goes here
        Generate paths for vol only. Then compute integrated variance and normal price.
        You should not use the random number seed
        '''
        
        npath = 10000
        nstep = 365 * texp
        dt = texp / nstep
          
        vov = self.vov
        sigma = self.sigma
        vol = sigma * np.ones((nstep+1, npath))
         
        for k in range(0, nstep):
            znorm_m = np.random.normal(loc=0,scale=1,size=(npath)) 
            vol[k+1, :] = vol[k, :] * np.exp(vov * np.sqrt(dt) * znorm_m-1/2 * (vov**2)*dt)
            
        var_mc = []
        N = vol.shape[0]-1
        weight = 2*np.ones(N+1)
        weight[0] = 1
        weight[-1] = 1
        IT = (weight @ (vol**2))/ (2*N)
        spot_new = spot + self.rho/vov *(vol[-1,:]-vol[0,:])
        sigma_new = sigma * np.sqrt((1-self.rho**2)*IT)

        for s in strike:
            opt_npath = normal.price(strike=s, spot=spot_new, texp = texp, vol = sigma_new, intr = self.intr, divr = self.divr, cp_sign = cp)
            var_mc.append( np.var( opt_npath ) )
        
        
        return var_mc

