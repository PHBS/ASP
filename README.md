# Applied Stochastic Processes (FIN 514, 2019-20 Module 1)

## Announcements
* Email is the preferred method of communication. Class mailing list will be created as PHBS.ASP@allmail.net.

## Course Slides and Other Resources
* Prelims: [Probability Statistics Review](files/Prob_Stat_Review.pdf) 
* Past Exam: [2017-18 Midterm](files/ASP2017_Midterm.pdf), [2018-19 Midterm](files/ASP2018_Midterm.pdf)
* Scientific computing, MC method, RN generation ([Slides](files/MCmethod.pdf) | [Py demo](py/MC_Demo.ipynb))
* Black-Scholes model ([Py demo](py/BlackScholes_ImpliedVol.ipynb), [MC demo](py/BlackScholes_MC.ipynb)): Also see Ch. 10 of [StoFin Course Notes](https://github.com/PHBS/2018.M3.StoFin/blob/master/files/SCFA_Notes.pdf)
* Normal (Bachelier) model ([Slides](files/Normal_Model.pdf)) from **Stochastic Finance** class
* Implied volatility ([Slides](files/ImpVol.pdf) | [Py demo](py/BlackScholes_ImpliedVol.ipynb))
* Spread/Basket options ([Slides](files/SpreadBasketOption.pdf))
* SABR model ([Slides](files/SABRmodel.pdf)) | NSVh model ([Slides](files/NSVh_Slides.pdf))
* Copula ([Slides](files/Copula.pdf), [Py demo](py/Demo_Copula.ipynb))

## Lectures
No | Date | Contents
--- | :---: | ---
__01__ | 9.03 Tue | Course overview, Scientific computing, MC method, RN generation ([Slides](files/MCmethod.pdf) \| [Py demo](py/MC_Demo.ipynb))
__02__ | 9.06 Fri | Continued ([Slides](files/MCmethod.pdf) \| [Py demo](py/MC_Demo.ipynb))
__03__ | 9.10 Tue | Black-Scholes-Merton and Normal option pricing with MC ([Py Demo](py/BlackScholes_MC.ipynb)), Normal model ([Slides](files/Normal_Model.pdf)), Black-Scholes implementation ([Py Demo](py/BlackScholes_FunctionVsClass.ipynb)), Implied volatility ([Slides](files/ImpVol.pdf), [Py demo](py/BlackScholes_ImpliedVol.ipynb))
__04__ | 9.11 Wed | Python crash course ([Basic](py/PythonCrashCourse_Derek_Banas.ipynb) \| [Numpy](py/PythonCrashCourse_Numpy.ipynb)).  More [cheatsheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html) also available in [MLF CMS](http://cms.phbs.pku.edu.cn/claroline/document/document.php?cidReset=true&cidReq=FN570). HW1
__05__ | 9.17 Tue | Spread/Basket options ([Slides](files/SpreadBasketOption.pdf)), Correlated Normal RNs ([Slides](files/MCmethod.pdf) \| [Py Demo](py/CorrelatedNormals_Demo.ipynb))
__06__ | 9.20 Fri | Spread/Basket options continued, HW2: [Spread/Basket option implementation](py/HW2/TestCode_BasketSpread.ipynb)
__07__ | 9.24 Tue | SABR model ([Slides](files/SABRmodel.pdf): Volatility smile, Local volatility model)
__08__  | 9.27 Fri | SABR model continued ([Slides](files/SABRmodel.pdf): Model intro, Euler/Milstein method).
 x | x | __No Class: National Day Week__
__09__ | 10.08 Tue | SABR model continued ([Slides](files/SABRmodel.pdf): Conditional MC method), Python Import ([Py Demo](py/HW3/Demo_Advanced_Import.ipynb)), Suggested [project topics](files/Project.md). HW3: [MC method for SABR](py/HW3/TestCode_SABR.ipynb)
__10__ | 10.11 Fri | SV Model Simulation for Project ([Slides](files/SV_Simulation.pdf))
__11__ | 10.15 Tue | Research Presentation: NSVh model and Normal SABR ([Slides](files/NSVh_Slides.pdf)), Introduction to PyFE, Github Pull-request
__12__ | 10.18 Fri | Review for midterm exam
__13__ | 10.22 Tue | Midterm exam
__14__ | 10.25 Fri | Copula ([Slides](files/Copula.pdf), [Py demo](py/Demo_Copula.ipynb))
__15__ | 10.29 Tue | Copula ([Slides](files/Copula.pdf), [Py demo](py/Demo_Copula.ipynb))
__16__ | 11.01 Fri | Research Presentation: (Sum of BSM models) and HW3 review
__17__ | 11.05 Tue | Course project presentation
__18__ | 11.08 Fri | Course project presentation

## Homeworks:
* ### __Set 0__: (Due by 9.6 Fri)
  * Register on Github.com and send your ID and student number to Prof. Choi via email (jaehyuk@phbs.pku.edu.cn). Use your __full name__ in your profile. Accept invitation to the [PHBS organization](https://github.com/orgs/PHBS/people) from TA. Install [Github Desktop](https://desktop.github.com/). 
  * Install [Anaconda](https://www.anaconda.com/download/) Python distribution (__3.X version__, not 2.X version). Anaconda distribution is core Python + useful scientific computation libraries (e.g., numpy, scipy, pandas) + package management system (pip or conda)
  * Send the screenshot of Github desktop and Anaconda installed to TA. (Example: [Github Desktop](files/Choi_Jaehyuk_Github.png), [Anaconda Spyder](files/Choi_Jaehyuk_Python.png))  
* ### __Set 1__ [Due by 9.19 Fri] Simple corporate (default) bond pricing by MC simulation. [Starter Code](py/HW1/HW1.ipynb)
* ### __Set 2__ [Due by 9.27 Fri] Pricing basket and spread option using MC. [Starter Code](py/HW2/TestCode_BasketSpread.ipynb)
* ### __Set 3__ [Due by 10.17 Fri] Simulating SABR model. [Starter Code](py/HW3/TestCode_SABR.ipynb)
* ### __Set 4__ 

## Course Project: [Project Description](files/Project.md) (Previous year: [2018](https://github.com/PHBS/2018.M1.ASP/blob/master/files/Project.md))

## Classes: 
* Lectures: Tues & Fri 1:30 – 3:20 PM
* Venue: PHBS Building, Room 209

## Instructor: [Jaehyuk Choi](http://www.jaehyukchoi.net/phbs_en)
* Office: PHBS Building, Room 755
* Phone: 86-755-2603-0568
* Email: jaehyuk@phbs.pku.edu.cn
* Office Hour: Tues 11:30AM-12:30PM & Fri 3:30-4:30 PM

## Teaching Assistance: TBA
* Email: xxxx@pku.edu.cn
* TA Office Hour: TBA (Room 213/214)

## Course overview: 
Applied Stochastic Processes (ASP) is intended for the students who are
seeking advanced knowledge in stochastic calculus and are eventually interested in the jobs in
financial engineering. As the name indicates, the course will emphasis on applications such as
numerical calculation and programming. On completion of this course, the students will learn
how financial observations (e.g. stock prices and FX rate) are modelled with stochastic
processes and how they can be computed using analytics or computer simulations.

## Prerequisites: 
[Stochastic Finance](https://github.com/PHBS/2018.M3.StoFin) (FIN 519), a year 1 required course for quantitative finance program, is a prerequisite for the ASP since it provides theoretical background. Undergraduate-level knowledge in probability, statistics, linear algebra and programming skill (Python) are also highly recommended. 

##  Extra Reading Materials
* Monte Carlo Methods in Finance by Peter Jaeckel
* Option Valuation Under Stochastic Volatility by Alan Lewis
* [Stochastic Calculus and Financial Applications](http://www-stat.wharton.upenn.edu/~steele/StochasticCalculus.html) by J. Michael Steele
([Stochastic finance course notes](https://github.com/PHBS/2018.M3.StoFin/blob/master/files/SCFA_Notes.pdf))

## Assessment/Grading Details
Attendance 20%, Mid-term Exam 30%, Assignments 20%, Course Project 30%
* __Midterm exam__: 10.22 Tues. Open-book exam without computer/phone/calculator use. No final exam.
* __Course project__: Presentation (Last week). Group up to X people.
* __Attendance__: Randomly checked. The score is calculated as 20 – 2`x`(#of absence). Leave request should be made 24 hours before with supporting documents, except for emergency. Job interview/internship cannot be a valid reason for leave
* __Grade__ in letters (e.g., A+, A-, ... ,D+, D, F). __A- or above < 30% and B- or below > 10%__.
