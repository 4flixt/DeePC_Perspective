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
- scipy
- CasADi

**To investigate the code**, we recommend to either locally install Python (and the toolboxes) and then clone the repo **or** you you can use the Binder links listed below. Binder clones the repo on their servers and installs all packages automatically. This way you can get started immediately! 

## Presented Results

To get started, we recommend first having a look at our notebook ``./ECC2020/res_01_woNoise.ipynb``. The content of this notebook is used to create **Figure 2 in the paper** and explains our methods, tools and the investigated system model in great detail. It covers the **case of deterministic DeePC vs. our proposed method**.


In **Figure 3** in the Paper we are comparing open-loop control of DeePC vs. MPC based on the multi-step prediction model. We present the code to reproduce these results in our notebook ``./ECC2020/res_02_open-loop_control.ipynb``.

Finally, the results presented in Table 1 can be reproduced with the code in ``./ECC2020/res_03_Noise_closed_loop.ipynb``. Note that you will likely obtain different computation times for the variants of DeePC and our proposed method. We expect that the general trend is going to be reproducable, however. 


You can find the links to binder (interactive) and the rendered Jupyter Notebook on Github (not-interactive) in the table below:

| Content        | Element in Paper           | Binder Link  | Github Link |
| ------------- |:-------------:| -----:| -----:|
| Closed-loop deterministic     | Figure 2 | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_01_woNoise.ipynb) | [Link](./ECC2021/res_01_woNoise.ipynb) |
| Open-loop non-deterministic  | Figure 3      |   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_02_open-loop_control.ipynb)| [Link](./ECC2021/res_02_open-loop_control.ipynb) |
| Closed-loop non-dterministic | Table 1    |    [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_03_Noise_closed_loop.ipynb) | [Link](./ECC2021/res_03_Noise_closed_loop.ipynb) |


