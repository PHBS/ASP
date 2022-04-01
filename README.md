# Applied Stochastic Processes 2021-22 Module 3 (Spring 2022)

## Announcements
* Email is the preferred method of communication. Class mailing list will be created as PHBS.ASP@allmail.net.

## Course Slides and Other Resources
* Prelims: [Probability Statistics Review](files/Prob_Stat_Review.pdf) 
* Past Midterm Exams: [All Exams](files/ASP_Problems.pdf) ([2017-18](files/ASP2017_Midterm.pdf), [2018-19](files/ASP2018_Midterm.pdf), [2019-20](files/ASP2019_Midterm.pdf), [2020-21](files/ASP2020_Midterm.pdf))
* `PyFeng` package ([PyPI](https://pypi.org/project/pyfeng/) \| [Github](https://github.com/PyFE/PyFENG) \| [Documentation](https://pyfeng.readthedocs.io/))
* Scientific computing, MC method, RN generation ([Slides](files/MCmethod.pdf) | [Py demo](py/MC_Demo.ipynb))
* Black-Scholes model ([Py demo](py/BlackScholes_ImpliedVol.ipynb), [MC demo](py/BlackScholes_MC.ipynb)): Also see Ch. 10 of [StoFin Course Notes](https://github.com/PHBS/StoFin/blob/master/files/SCFA_Notes.pdf)
* Normal (Bachelier) model ([Slides](files/Normal_Model.pdf)) from **Stochastic Finance** class
* Implied volatility ([Slides](files/ImpVol.pdf) | [Py demo](py/BlackScholes_ImpliedVol.ipynb))
* Spread/Basket options ([Slides](files/SpreadBasketOption.pdf))
* SABR model ([Slides](files/SABRmodel.pdf)) | NSVh model ([Slides](files/NSVh_Slides.pdf))
* Copula ([Slides](files/Copula.pdf), [Py demo](py/Demo_Copula.ipynb))

## Lectures
No | Date | Contents
--- | :---: | ---
__01__ | 2.22 Tue | Course overview, Scientific computing, MC method, RN generation ([Slides](files/MCmethod.pdf) \| [Py demo](py/MC_Demo.ipynb))
__02__ | 2.25 Fri | Continued ([Slides](files/MCmethod.pdf) \| [Py demo](py/MC_Demo.ipynb))
__03__ | 3.01 Tue | Python crash course ([Py Demo](py/PythonCrashCourse_Derek_Banas.ipynb)). More [cheatsheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html) also available in [MLF CMS](http://cms.phbs.pku.edu.cn/claroline/document/document.php?cidReset=true&cidReq=FN570).  Numpy crach course ([Py Demo](py/PythonCrashCourse_Numpy.ipynb)). 
__04__ | 3.04 Fri |Black-Scholes implementation ([Py Demo](py/BlackScholes_FunctionVsClass.ipynb)). Implied volatility ([Slides](files/ImpVol.pdf) \| [Py demo](py/BlackScholes_ImpliedVol.ipynb)). 
__05__ | 3.08 Tue | Bachelier model ([Slides](files/Normal_Model.pdf)). Black-Scholes-Merton and Bachelier option pricing with MC ([Py Demo](py/BlackScholes_MC.ipynb)). Spread/Basket options ([Slides](files/SpreadBasketOption.pdf)). Correlated Normal RNs ([Slides](files/MCmethod.pdf) \| [Py Demo](py/CorrelatedNormals_Demo.ipynb))
__06__ | 3.11 Fri | Spread/Basket options continued, [HW2: [Spread/Basket option implementation](py/HW2/TestCode_BasketSpread.ipynb), Due next Friday]
__07__ | 3.15 Tue | SABR model ([Slides](files/SABRmodel.pdf): Volatility smile), Suggested [project topics](files/Project.md)
__08__ | 3.18 Fri | SABR model continued ([Slides](files/SABRmodel.pdf): Local volatility model, Model intro), Introduction to [PyFENG](https://github.com/PyFE/PyFENG) package
__09__ | 3.22 Tue | SABR model continued ([Slides](files/SABRmodel.pdf): Euler/Milstein method, Conditional MC), Github pull-request (PR), Py Demo ([SABR](py/SabrModel_Demo.ipynb), [BsmNdMc](BsmNdMc_Demo.ipynb)), HW3: [MC method for SABR](py/HW3/TestCode_SABR.ipynb)
__10__ | 3.25 Fri | Python Import ([Py Demo](py/HW3/Demo_Advanced_Import.ipynb)), SV Model Simulation for Project ([Slides](files/SV_Simulation.pdf))
__11__ | 3.29 Tue | SV Model Simulation for Project ([Slides](files/SV_Simulation.pdf)), [Past Exams](files/ASP_Problems.pdf) Review
__12__ | 4.01 Fri | [Past Exams](files/ASP_Problems.pdf) Review
__13__ | 4.06 __Wed__ | Midterm Exam ([Solution](files/ASP2020_Midterm.pdf))
__14__ | 4.88 Fri | Copula ([Slides](files/Copula.pdf), [Py demo](py/Demo_Copula.ipynb))
__15__ | 4.12 Tue | Copula ([Slides](files/Copula.pdf), [Py demo](py/Demo_Copula.ipynb))
__16__ | 4.15 Wed | Research Presentation: NSVh model and Normal SABR ([Slides](files/NSVh_Slides.pdf))
__17__ | 4.19 Tue | Course project presentation
__18__ | 4.22 Fri | Course project presentation

<!-- , Research Presentation: NSVh model and Normal SABR ([Slides](files/NSVh_Slides.pdf)) -->

## Homeworks:
* ### __Set 0__: (Due by 2.24 Fri)
  * Register on Github.com and send your ID and student number to Prof. Choi via email (jaehyuk@phbs.pku.edu.cn). Use your __full name__ in your profile. Accept invitation to the [PHBS organization](https://github.com/orgs/PHBS/people) from TA. Install [Github Desktop](https://desktop.github.com/). 
  * Install [Anaconda](https://www.anaconda.com/download/) Python distribution (__3.X version__, not 2.X version). Anaconda distribution is core Python + useful scientific computation libraries (e.g., numpy, scipy, pandas) + package management system (pip or conda)
  * Send the screenshot of Github desktop and Anaconda installed to TA. (Example: [Github Desktop](files/Choi_Jaehyuk_Github.png), [Anaconda Spyder](files/Choi_Jaehyuk_Python.png))  
* ### __Set 1__ [Due by XXX] Simple corporate (default) bond pricing by MC simulation. [Starter Code](py/HW1/HW1.ipynb)
* ### __Set 2__ [Due by XXX] Pricing basket and spread option using MC. [Starter Code](py/HW2/TestCode_BasketSpread.ipynb)
* ### __Set 3__ [Due by XXX] Simulating SABR model. [Starter Code](py/HW3/TestCode_SABR.ipynb)

## Course Project: [Project Description](files/Project.md) (Previous year: [2017](past-years/2017-18-M1/Project.md) | [2018](past-years/2018-19-M1/Project.md) | [2019](past-years/2019-20-M1/Project.md))

## Classes: 
* Lectures: Tues & Fri 1:30 – 3:20 PM
* Venue: PHBS Building, Room 229

## Instructor: [Jaehyuk Choi](http://www.jaehyukchoi.net/phbs_en)
* Office: PHBS Building, Room 755
* Phone: 86-755-2603-0568
* Email: jaehyuk@phbs.pku.edu.cn
* Office Hour: __TBA__

## Teaching Assistance: NING Lei (宁磊)
* Email: leining@stu.pku.edu.cn
* TA Office Hour: __TBA__ (Room 213/214)

## Course overview: 
Applied Stochastic Processes (ASP) is intended for the students who are
seeking advanced knowledge in stochastic calculus and are eventually interested in the jobs in
financial engineering. As the name indicates, the course will emphasis on applications such as
numerical calculation and programming. On completion of this course, the students will learn
how financial observations (e.g. stock prices and FX rate) are modelled with stochastic
processes and how they can be computed using analytics or computer simulations.

## Prerequisites: 
[Stochastic Finance](https://github.com/PHBS/StoFin) (FIN 519), a year 1 required course for quantitative finance program, is a prerequisite for the ASP since it provides theoretical background. Undergraduate-level knowledge in probability, statistics, linear algebra and programming skill (Python) are also highly recommended. 

##  Extra Reading Materials
* Monte Carlo Methods in Finance by Peter Jaeckel
* Option Valuation Under Stochastic Volatility by Alan Lewis
* [Stochastic Calculus and Financial Applications](http://www-stat.wharton.upenn.edu/~steele/StochasticCalculus.html) by J. Michael Steele
([Stochastic finance course notes](https://github.com/PHBS/2018.M3.StoFin/blob/master/files/SCFA_Notes.pdf))

## Assessment/Grading Details
Attendance 20%, Mid-term Exam 30%, Assignments 20%, Course Project 30%
* __Midterm exam__: 4.06 __Wed__. Open-book exam without computer/phone/calculator use. No final exam.
* __Course project__: Presentation (Last week). Group up to X people.
* __Attendance__: Randomly checked. The score is calculated as 20 – 2`x`(#of absence). Leave request should be made 24 hours before with supporting documents, except for emergency. Job interview/internship cannot be a valid reason for leave
* __Grade__ in letters (e.g., A+, A-, ... ,D+, D, F). __A- or above < 30% and B- or below > 10%__.
