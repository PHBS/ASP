# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 13:17:25 2018

@author: jaehyuk
"""

import numpy as np
from option_models import basket

spot = np.ones(4) * 100
vol = np.ones(4) * 0.4
weights = np.ones(4) * 0.25
divr = np.zeros(4)
intr = 0
cor_m = 0.5*np.identity(4) + 0.5
texp = 5
strike = 100
price_basket = basket.basket_price_mc(strike, spot, vol*spot, weights, texp, cor_m, bsm=False)

print(price_basket)