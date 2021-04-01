# On the relationship between data-enabled predictive control and subspace predictive control
Accompanying  repository for our work "On the relationship between data-enabled predictive control and subspace predictive control" accepted at ECC 2021.

## Abstract
Data-enabled predictive control (DeePC) is a recently proposed approach that combines system identification, estimation and control in a single optimization problem, for which only recorded input/output data of the examined system is required. The same premise holds for the subspace predictive control (SPC) method in which a multi-step prediction model is identified from the same data as required for DeePC. This model is then used to formulate a similar optimal control problem. In this work we investigate the relationship between DeePC and SPC. Our primary contribution is to show that SPC is equivalent to DeePC in the deterministic case. We also show the equivalence of both methods in a special case for the non- deterministic formulation. We investigate the advantages and shortcomings of DeePC as opposed to SPC with and without measurement noise and illustrate them with a simulation example.

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

To get started, we recommend first having a look at our notebook ``./ECC2020/res_01_woNoise.ipynb``. The content of this notebook is used to create **Figure 2 in the paper** and explains our methods, tools and the investigated system model in great detail. It covers the **case of deterministic DeePC vs. SPC**.


In **Figure 3** in the Paper we are comparing open-loop control of DeePC vs. SPC. We present the code to reproduce these results in our notebook ``./ECC2020/res_02_open-loop_control.ipynb``.

Finally, the results presented in Table 1 can be reproduced with the code in ``./ECC2020/res_03_Noise_closed_loop.ipynb``. Note that you will likely obtain different computation times for the variants of DeePC and our proposed method. We expect that the general trend is going to be reproducable, however. 


You can find the links to binder (interactive) and the rendered Jupyter Notebook on Github (not-interactive) in the table below:

| Content        | Element in Paper           | Binder Link  | Github Link |
| ------------- |:-------------:| -----:| -----:|
| Closed-loop deterministic     | Figure 2 | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_01_woNoise.ipynb) | [Link](./ECC2021/res_01_woNoise.ipynb) |
| Open-loop non-deterministic  | Figure 3      |   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_02_open-loop_control.ipynb)| [Link](./ECC2021/res_02_open-loop_control.ipynb) |
| Closed-loop non-dterministic | Table 1    |    [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4flixt/DeePC_Perspective/main?filepath=.%2FECC2021%2Fres_03_Noise_closed_loop.ipynb) | [Link](./ECC2021/res_03_Noise_closed_loop.ipynb) |


