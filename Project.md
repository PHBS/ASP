# ASP Course Project

## [Repository](https://github.com/pyfe/pyfeng) and [Project List](https://github.com/pyfe/pyfeng/projects)

## List of Projects
* Simulation of the GARCH Diffusion model
  * [@Harveydentsun](https://github.com/Harveydentsun) and [@yogaball](https://github.com/yogaball)
* Simulation of Rough Volatility Model 
  * [@polarbluebear](https://github.com/polarbluebear) and [@Baiwisher](https://github.com/Baiwisher)
  * Ma J, Wu H (2021) A fast algorithm for simulation of rough volatility models. Quantitative Finance 0:1–16. https://doi.org/10.1080/14697688.2021.1970213
* Lifted Heston Model
  * [@jyyccc](https://github.com/jyyccc) and [@Cecilia525](https://github.com/Cecilia525)
  * Jaber EA (2019) Lifting the Heston model. Quantitative Finance 19:1995–2013. https://doi.org/10.1080/14697688.2019.1615113
* Almost Exact Simulation of the 3/2 Volatility Model
  * [@AHrmnd](https://github.com/AHrmnd) and [@FLXE-Feidou](https://github.com/FLXE-Feidou)
* Solving Risk Parity Weights
  * [@lililiyf](https://github.com/lililiyf) and [@TinaWang39](https://github.com/TinaWang39)
  * Bai X, Scheinberg K, Tutuncu R (2016) Least-squares approach to risk parity in portfolio selection. Quantitative Finance 16:357–376. https://doi.org/10.1080/14697688.2015.1031815
* Approximate Stochastic Volatility Model Option Pricing
  * [@zwc00098](https://github.com/zwc00098)
  * Ball CA, Roma A (1994) Stochastic Volatility Option Pricing. Journal of Financial and Quantitative Analysis 29:589–607. https://doi.org/10.2307/2331111

## Presentation and Deadline
* Presentation: 4.22 (Friday) 10 minutes by each group.
* Pull request deadline: 4.30 (Saturday)

## File requirements
* `PyFENG` repository:
  * Core implementation (.py): python class and functions
  * Make sure to add docstring in detail. Example: [bsm.py](https://github.com/PYFE/pyfeng/blob/master/pyfeng/bsm.py)
  * The best examples of docstring are from numpy documentation: [example](https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.polynomials.hermite.html)
  * __Integrate into the `PyFENG` repository__ by making pull-requests (pr).
  * __Do not__ place any `.ipynb` file.
* Your repository (`PHBS_ASP_2021` or any name is OK)
  * Test (__.ipynb__): one Jupyter notebook file briefly describing the method (base theory, equations, SDE, strength/weakness, etc).
  * Include some test examples (e.g., the same parameter sets from the paper)
* See past years' proejct:
  * [2020-21](https://github.com/PHBS/ASP/blob/master/past-years/2020-21-M1/Project.md)
  * [2019-20](https://github.com/PHBS/ASP/blob/master/past-years/2019-20-M1/Project.md)
  * [2018-19](https://github.com/PHBS/ASP/blob/master/past-years/2018-19-M1/Project.md)
  * [2017-18](https://github.com/PHBS/ASP/blob/master/past-years/2017-18-M1/Project.md)

# Project Topics

## Topics
* Among the topics and HWs covered in the class, choose an in-depth research on one topic. You are also welcome to do the project on your own original idea. Otherwise, pick one from my suggestions which are basically understanding and implementing literatures. Topics includes 
  * Spread/Basket/Asian option pricing
  * SV models (SABR, Heston, etc)
  * Rough volatility
  * Copula

### * Rough Volatility
* Ma J, Wu H (2021) A fast algorithm for simulation of rough volatility models. Quantitative Finance 0:1–16. https://doi.org/10.1080/14697688.2021.1970213
* Jaber EA (2019) Lifting the Heston model. Quantitative Finance 19:1995–2013. https://doi.org/10.1080/14697688.2019.1615113
* Horvath B, Jacquier A, Muguruza A (2019) Functional central limit theorems for rough volatility. arXiv:171103078 [math, q-fin] http://arxiv.org/abs/1711.03078
* McCrickerd R, Pakkanen MS (2018) Turbocharging Monte Carlo pricing for the rough Bergomi model. Quantitative Finance 18:1877–1886. https://doi.org/10.1080/14697688.2018.1459812
* Bennedsen, M., Lunde, A., Pakkanen, M.S., 2017. Hybrid scheme for Brownian semistationary processes. Finance Stoch 21, 931–965. https://doi.org/10.1007/s00780-017-0335-5
* J. Gatheral's [python code](https://tpq.io/p/rough_volatility_with_python.html)

### * Spread/Basket/Asian Option
* [[Partially](https://github.com/PyFE/pyfedev/blob/master/pyfe/bsm_multi_choi2018.py) implemented] Choi J (2018) Sum of all Black-Scholes-Merton models: An efficient pricing method for spread, basket, and Asian options. Journal of Futures Markets 38:627–644. https://doi.org/10.1002/fut.21909
  * R implementation: https://github.com/PyFE/SumBSM-R
* [Most methods implemented] Krekel M, de Kock J, Korn R, Man T-K (2004) An analysis of pricing methods for basket options. Wilmott Magazine 2004:82–89

### Option pricing with Fourier Transform
* Lord R, Kahl C (2010) Complex Logarithms in Heston-Like Models. Mathematical Finance 20:671–694. https://doi.org/10.1111/j.1467-9965.2010.00416.x
* Kahl C, Jäckel P (2005) Not-so-complex Logarithms in the Heston Model. Wilmott 19
* [Implemented but not perfect] __OUSV:__ Schöbel R, Zhu J (1999) Stochastic Volatility With an Ornstein–Uhlenbeck Process: An Extension. Rev Financ 3:23–46. https://doi.org/10.1023/A:1009803506170

### * GARCH-diffusion model
* [Implemented] Barone-Adesi G, Rasmussen H, Ravanelli C (2005) An option pricing formula for the GARCH diffusion model. Computational Statistics & Data Analysis 49:287–310. https://doi.org/10.1016/j.csda.2004.05.014
* Tubikanec I, Tamborrino M, Lansky P, Buckwar E (2021) Qualitative properties of numerical methods for the inhomogeneous geometric Brownian motion. arXiv:200310193 [cs, math] http://arxiv.org/abs/2003.10193
* [Implemented] Euler/Milstein/Log scheme (in class)
* [????] Capriotti L, Jiang Y, Shaimerdenova G (2018) Approximation methods for inhomogeneous geometric brownian motion. Int J Theor Appl Finan 22:1850055. https://doi.org/10.1142/S0219024918500553
* __IGBM:__ Zhao B (2009) Inhomogeneous Geometric Brownian Motion. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.1429449
* [Consider] PhD Thesis of Ravanelli, C., University of Lugano, Switzerland, https://doc.rero.ch/record/4229/files/1_2003ECO001.pdf
* [No method] Papadopoulos, Y.A., Lewis, A.L., 2018. A First Option Calibration of the GARCH Diffusion Model by a PDE Method. arXiv:1801.06141 [q-fin].

### * SABR model
* [Implemented but not verified] Cai N, Song Y, Chen N (2017) Exact Simulation of the SABR Model. Oper Res 65:931–951. https://doi.org/10.1287/opre.2017.1617
* [Implemented but not verified] Leitao Á, Grzelak LA, Oosterlee CW (2017) On a one time-step Monte Carlo simulation approach of the SABR model: Application to European options. Applied Mathematics and Computation 293:461–479. https://doi.org/10.1016/j.amc.2016.08.030

### * [Heston Model](https://en.wikipedia.org/wiki/Heston_model) (SV)
* [No need] Broadie M, Kaya Ö (2006) Exact Simulation of Stochastic Volatility and Other Affine Jump Diffusion Processes. Operations Research 54:217–231. https://doi.org/10.1287/opre.1050.0247
* [Implemented] Glasserman P, Kim K-K (2011) Gamma expansion of the Heston stochastic volatility model. Finance Stoch 15:267–296. https://doi.org/10.1007/s00780-009-0115-y
* [Implemented]  Andersen, L., 2008. Simple and efficient simulation of the Heston stochastic volatility model. The Journal of Computational Finance 11, 1–42. https://doi.org/10.21314/JCF.2008.189
* [Implemented / 2022 Thesis] Almost exact simulation

### * OUSV Model
* [Implemented] Euler/Milstein
* [Implemented] Li C, Wu L (2019) Exact simulation of the Ornstein–Uhlenbeck driven stochastic volatility model. European Journal of Operational Research 275:768–779. https://doi.org/10.1016/j.ejor.2018.11.057
* [2021 Thesis] Almost exact simulation

### * 3/2 SV model
* [Implemented but not verified] Baldeaux, J., 2012. Exact simulation of the 3/2 model. Int. J. Theor. Appl. Finan. 15, 1250032. https://doi.org/10.1142/S021902491250032X
* [Implemented but not verified] Almost exact simulation

### * Other Simulation-related Papers
* [Implemented but not verified] __General SDE__: Beskos, A., Roberts, G.O., 2005. Exact simulation of diffusions. Ann. Appl. Probab. 15, 2422–2444. https://doi.org/10.1214/105051605000000485
* [Implemented] __Computing Moments from Laplace Transform__: Choudhury, G.L., Lucantoni, D.M., 1996. Numerical Computation of the Moments of a Probability Distribution from its Transform. Operations Research 44, 368–381. https://doi.org/10.1287/opre.44.2.368
