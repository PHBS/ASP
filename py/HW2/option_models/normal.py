# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:56:58 2017

@author: jaehyuk
"""
import numpy as np
import scipy.stats as ss
import scipy.optimize as sopt

def normal_formula(strike, spot, vol, texp, intr=0.0, divr=0.0, cp=1):
    div_fac = np.exp(-texp*divr)
    disc_fac = np.exp(-texp*intr)
    forward = spot / disc_fac * div_fac

    if( texp<0 or vol*np.sqrt(texp)<1e-8 ):
        return disc_fac * np.fmax( cp*(forward-strike), 0 )

    vol_std = np.fmax(vol * np.sqrt(texp), 1.0e-16)
    d = (forward - strike) / vol_std

    price = disc_fac * (cp * (forward - strike) * ss.norm.cdf(cp * d) + vol_std * ss.norm.pdf(d))
    return price

class NormalModel:
    
    vol, intr, divr = None, None, None
    
    def __init__(self, vol, intr=0, divr=0):
        self.vol = vol
        self.intr = intr
        self.divr = divr
    
    def price(self, strike, spot, texp, cp=1):
        return normal_formula(strike, spot, self.vol, texp, intr=self.intr, divr=self.divr, cp=cp)
    
    def delta(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp=1):
        div_fac = np.exp(-texp*divr)
        disc_fac = np.exp(-texp*intr)
        forward = spot / disc_fac * div_fac
        vol_std = np.fmax(vol * np.sqrt(texp), 1.0e-16)
        d = (forward - strike) / vol_std
        self.delta = disc_fac * ss.norm.cdf(cp * d)
        return self.delta

    def vega(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp=1):
        div_fac = np.exp(-texp*divr)
        disc_fac = np.exp(-texp*intr)
        forward = spot / disc_fac * div_fac
        vol_std = np.fmax(vol * np.sqrt(texp), 1.0e-16)
        d = (forward - strike) / vol_std
        self.vega = disc_fac * np.sqrt(texp) * ss.norm.pdf(cp * d)
        return self.vega

    def gamma(self, strike, spot, vol, texp, intr=0.0, divr=0.0, cp=1):
        div_fac = np.exp(-texp*divr)
        disc_fac = np.exp(-texp*intr)
        forward = spot / disc_fac * div_fac
        vol_std = np.fmax(vol * np.sqrt(texp), 1.0e-16)
        d = (forward - strike) / vol_std
        self.gamma =  disc_fac * ss.norm.pdf(cp * d) / vol_std
        return self.gamma

    def impvol(self, price, strike, spot, texp, cp=1):
        iv_func = lambda _vol: \
            normal_formula(strike, spot, _vol, texp, self.intr, self.divr, cp) - price
        vol = sopt.brentq(iv_func, 0, 10)
        return 0