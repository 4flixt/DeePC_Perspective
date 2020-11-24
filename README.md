# A new perspective on data-enabled predictive control
Accompanying  repository for our work "A new perspective on data-enabled predictive control" submitted to ECC 2021.

## Abstract
Data-enabled predictive control (DeePC) is a recently proposed approach that combines system identification, estimation and control in a single optimization problem, for which only recorded input/output data of the examined system is required.
In this work we present a simple method to identify a multi-step prediction model from the same data required for DeePC. We prove that model predictive control based on this model is equivalent to DeePC in the deterministic case and that its solution has the same structure in the stochastic case. 
We investigate the advantages and shortcomings of DeePC as opposed to the sequential system identification and control approach for linear models with and without measurement noise. We find that DeePC adds significant complexity to the optimization problem and can also lead to deterioration in control performance for the non-deterministic case, as we illustrate with a simulation example.

## About this Repository

Dear visitor, 

thank you for checking our the supplementary materials for our work. 
If you have questions, remarks, technical issues etc. feel free to **use the issues page of this repository.**
We are looking forward to your feedback and the discussion. 

The purpose of this repository is to provide all the materials needed to recreate our results and to allow to experiment yourself with the code. 
Most importantly, we are providing here the investigated system model.
All of our results are created using Python code (using Jupyter Notebooks) and the toolboxes:

- numpy
- matplotlib
- CasADi

**To investigate the code**, we recommend to either locally install Python (and the toolboxes) and then clone the repo **or** you you can use the Binder links listed below. Binder clones the repo on their servers and installs all packages automatically. This way you can get started immediately! 

## Presented Results

To get started, we recommend first having a look at our notebook ``./ECC2020/res_01_woNoise.ipynb``. The content of this notebook is used to create **Figure 2 in the paper** and explains our methods, tools and the investigated system model in great detail. It covers the **case of deterministic DeePC vs. our proposed method**.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_01_woNoise.ipynb)



