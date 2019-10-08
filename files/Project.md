# ASP Course Project

## Do do
* Please report me (by email) if you already formed a group.

## Project List [[link](https://github.com/PHBS/pyfedev_ASP2019/projects)]

## Topics
* Among the topics and HWs covered in the class, choose an in-depth research on one topic. You are also welcome to do the project on your own original idea. Otherwise, pick one from my suggestions which are basically understanding and implementing literatures. Topics includes 
  * BSM (lognormal) vs Bachelier (normal) model
  * Spread/Basket/Asian option pricing
  * SABR model and other stochastic volatility models

## Repository:
* https://github.com/PHBS/pyfedev_ASP2019

## File requirements
* Core implementation (.py): python class and functions
  * Make sure to comment in detail.
  * __Integrate into the `pyfe` folder.__ Do not mix with testing/manual notebook files.
* Documentation/Manual (__.ipynb__): one Jupyter notebook file briefly describing the method (base theory, equations, SDE, strength/weakness, etc), the function prototype and arguments (manual style) and the usage examples
  * The best examples are from numpy documentation: [example](https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.polynomials.hermite.html)
* Validation/Test (__.py__): one python file briefly test the code/model.
  * Think creatively how to avoid possible errors. For example,
  * BSM/Normal model: make sure to include the analytic-vs-numerical risk test.
  * SV (SABR/Heston): make sure that the price converge to BSM/Normal if alpha(vov parameter) goes to 0
  * Spread/Basket: make sure that the price is same as single asset BSM if the weigit is 1 for only one asset and zero otherwise.

## Other guidelines
* Make sure to show the contribution via github desktop commits (not online upload).
* The presentation next week doesn't have to be complete. Show your plan and understanding so far, e.g. function prototypes & arguments, etc and the tests to put on.

## Suggested Topics and Papers 
### * Simulations of Heston model
* [Heston Model](https://en.wikipedia.org/wiki/Heston_model)
* Broadie, M., Kaya, Ö., 2006. Exact Simulation of Stochastic Volatility and Other Affine Jump Diffusion Processes. Operations Research 54, 217–231. https://doi.org/10.1287/opre.1050.0247 | Glasserman, P., Kim, K.-K., 2011. Gamma expansion of the Heston stochastic volatility model. Finance Stoch 15, 267–296. https://doi.org/10.1007/s00780-009-0115-y
* Kahl, C., Jäckel, P., 2006. Fast strong approximation Monte Carlo schemes for stochastic volatility models. Quantitative Finance 6, 513–536. https://doi.org/10.1080/14697680600841108
* Andersen, L., 2008. Simple and efficient simulation of the Heston stochastic volatility model. The Journal of Computational Finance 11, 1–42. https://doi.org/10.21314/JCF.2008.189
* Lord, R., Koekkoek, R., Dijk, D.V., 2010. A comparison of biased simulation schemes for stochastic volatility models. Quantitative Finance 10, 177–194. https://doi.org/10.1080/14697680802392496

### * GARCH-diffusion model
* Papadopoulos, Y.A., Lewis, A.L., 2018. A First Option Calibration of the GARCH Diffusion Model by a PDE Method. arXiv:1801.06141 [q-fin].
* Barone-Adesi, G., Rasmussen, H., Ravanelli, C., 2005. An option pricing formula for the GARCH diffusion model. Computational Statistics & Data Analysis, 2nd CSDA Special Issue on Computational Econometrics 49, 287–310. https://doi.org/10.1016/j.csda.2004.05.014

### * Exact Simulation Scheme
* __General SDE__: Beskos, A., Roberts, G.O., 2005. Exact simulation of diffusions. Ann. Appl. Probab. 15, 2422–2444. https://doi.org/10.1214/105051605000000485
* __OU SV Model__: Li, C., Wu, L., 2019. Exact simulation of the Ornstein–Uhlenbeck driven stochastic volatility model. European Journal of Operational Research 275, 768–779. https://doi.org/10.1016/j.ejor.2018.11.057
* __Heston Model__: Broadie, M., Kaya, Ö., 2006. Exact Simulation of Stochastic Volatility and Other Affine Jump Diffusion Processes. Operations Research 54, 217–231. https://doi.org/10.1287/opre.1050.0247 | Glasserman, P., Kim, K.-K., 2011. Gamma expansion of the Heston stochastic volatility model. Finance Stoch 15, 267–296. https://doi.org/10.1007/s00780-009-0115-y
* __3/2 SV Model__: Baldeaux, J., 2012. Exact simulation of the 3/2 model. Int. J. Theor. Appl. Finan. 15, 1250032. https://doi.org/10.1142/S021902491250032X
* __SABR Model__: Cai, N., Song, Y., Chen, N., 2017. Exact Simulation of the SABR Model. Operations Research 65, 931–951. https://doi.org/10.1287/opre.2017.1617
* __Computing Moments from Laplace Transform__: Choudhury, G.L., Lucantoni, D.M., 1996. Numerical Computation of the Moments of a Probability Distribution from its Transform. Operations Research 44, 368–381. https://doi.org/10.1287/opre.44.2.368

### * Rough Volatility
* McCrickerd, R., Pakkanen, M.S., 2018. Turbocharging Monte Carlo pricing for the rough Bergomi model. Quantitative Finance 18, 1877–1886. https://doi.org/10.1080/14697688.2018.1459812
* Bennedsen, M., Lunde, A., Pakkanen, M.S., 2017. Hybrid scheme for Brownian semistationary processes. Finance Stoch 21, 931–965. https://doi.org/10.1007/s00780-017-0335-5

### * Unfinished Projects
* [BSM Implied Volatility] Analytic approximation of BSM implied volatility ([Jackel 2016](jaeckel.16mb.com/LetsBeRational.pdf)): implement the method, include it to BSM class and write a thorough test code. In python notebook, summarize the method, write a quick help and report strength and weakness.

## Completed Papers
* ~[Normal Implied Volatility]~ Analytic approximation of normal implied volatility ([Choi et al 2007](http://jaehyukchoi.com/research/normvol/index.html)): (Contact me if you want to take this project) implement the method, include it to Normal class and write a thorough test code. In python notebook, summarize the method, write a quick help and report strength and weakness.
* ~[Normal Implied Volatility]~ Analytic approximation of normal implied volatility ([Le Floc'h 2016](https://ssrn.com/abstract=2420757), [some discussion](https://www.clarusft.com/analytic-implied-basis-point-volatility/)): implement the method, include it to Normal class and write a thorough test code. In python notebook, summarize the method, write a quick help and report strength and weakness.
* ~[Spread option]~ Very accurate analytic approximation for spread options by [Li et al, 2006](https://ssrn.com/abstract_id=952747). 
Also implement Kirk's approximation covered in class and [(Bjersund, Stensland 2014)](http://ssrn.com/abstract_id=1145206). Implement each method in a new class. In python notebook, summarize the method, write a quick help and report strength and weakness. Compare the three methods.
* ~[Basket+Asian option]~ Pick one method in the following 3 methods in survey of basket option pricing (Krekel at al, 2004, Wilmott magazine, July, 82-89): Implement the method in a new class. In python notebook, summarize the method, write a quick help and report strength and weakness.
  * a) Beisser's conditional expectation 
  * c) Levy's log-normal moment matching
  * d) Ju's Taylor expansion
* ~[Basket/Spread/Asian Option]~ A unified numerical method for both spread and basket options: [Choi (2017)](http://papers.ssrn.com/abstract_id=2913048): Contact me
* ~[CEV Model]~ Option pricing under Constant Elasticity of Variance (CEV) model (formula available many on-line sources):
implement the method, include it to Normal class and write a thorough test code. In python notebook, summarize the method, write a quick help and report strength and weakness.
* ~[SABR Option Pricing]~ Arbitrage-free pricing method by [Kennedy et al, 2011](http://www.tandfonline.com/doi/abs/10.1080/1350486X.2011.646523) ([Download](http://ssrn.com/abstract_id=2043504)): simpler approach introduced in class is enough. Implement the method, create a new class ModelKennedy in sabr.py, and write a thorough test code. In python notebook, summarize the method, write a quick help and report strength and weakness. 
* ~[SABR Calibration]~ Efficient first guess for SABR calibrations to 3 option prices by [Le Floc’h and Kennedy, 2014](https://ssrn.com/abstract_id=2467231) (see also [here](https://www.clarusft.com/sabr-calibration-a-simple-explicit-initial-guess/)): Implement the method, add to sabr.py, and write a code comparing the efficient against the dumb initial guess. In python notebook, summarize the method, write a quick help and report strength and weakness. 
* ~[Vanna-Volga method]~ a smile interpolation method ([Wiki](https://en.wikipedia.org/wiki/Vanna-Volga_pricing), [BSM](https://arxiv.org/abs/0904.1074), [Normal](https://arxiv.org/abs/1810.07457))
* ~[SABR Simulation]~ [Efficient SABR simulation by Leitao et al](http://dx.doi.org/10.1016/j.amc.2016.08.030)
* ~[SABR approximations]~ Various improvement to Hagan's original paper: [Paulot](https://arxiv.org/abs/0906.0658), [Obloj](https://arxiv.org/abs/0708.0998), [Balland](http://janroman.dhis.org/finance/OIS/Artiklar%20%C3%B6vrigt/SABR%20goes%20Normal.pdf) 
, etc. Contact me for more information.
* ~[SABR Simulation/Interpolation]~ SABR simulation by stochastic collocation Monte Carlo method ( [paper 1](https://ssrn.com/abstract=2529691), [paper 2](https://ssrn.com/abstract=2529684) )

