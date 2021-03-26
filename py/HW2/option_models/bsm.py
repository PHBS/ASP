    # -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:56:58 2017

@author: jaehyuk
"""

import numpy as np
import scipy.stats as ss
import scipy.optimize as sopt

def bsm_formula(strike, spot, vol, texp, intr=0.0, divr=0.0, cp=1):
    div_fac = np.exp(-texp*divr)
    disc_fac = np.exp(-texp*intr)
    forward = spot / disc_fac * div_fac

    if( texp<0 or vol*np.sqrt(texp)<1e-8 ):
        return disc_fac * np.fmax( cp*(forward-strike), 0 )
    
    vol_std = vol*np.sqrt(texp)
    d1 = np.log(forward/strike)/vol_std + 0.5*vol_std
    d2 = d1 - vol_std

    price = cp * disc_fac \
        * ( forward * ss.norm.cdf(cp*d1) - strike * ss.norm.cdf(cp*d2) )
    return price

class BsmModel:
    vol, intr, divr = None, None, None
    
    def __init__(self, vol, intr=0, divr=0):
        self.vol = vol
        self.intr = intr
        self.divr = divr
    
    def price(self, strike, spot, texp, cp=1):
        return bsm_formula(strike, spot, self.vol, texp, intr=self.intr, divr=self.divr, cp=cp)
    
    def delta(self, strike, spot, texp, cp=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0

    def vega(self, strike, spot, vol, texp, cp=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0

    def gamma(self, strike, spot, vol, texp, cp=1):
        ''' 
        <-- PUT your implementation here
        '''
        return 0

    def impvol(self, price, strike, spot, texp, cp=1):
        iv_func = lambda _vol: \
            bsm_formula(strike, spot, _vol, texp, self.intr, self.divr, cp) - price
        vol = sopt.brentq(iv_func, 0, 10)
        return vol
