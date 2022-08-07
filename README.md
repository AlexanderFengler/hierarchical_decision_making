# hierarchical_decision_making
This is the repo for utilizing HDDMnn to fit models of hierarchical decision-making to reaction-time data.

The purpose of this repo is to provide a pipeline for generating data and plots for models of behavior on hierarchical decision-making tasks. Using HDDM, we can fit drift-diffusion models to reaction-time data. Since we are specifically concerned with models of hierarchical decision-making, we use HDDMnn to approximate the likelihood function of hierarchical decision-making models for model-fitting.

As of 8/6/2022, HDDMnn only supports 3 models of hierarchical decision-making. These are "ddm_seq2_no_bias", "ddm_par2_no_bias", and "ddm_mic2_adj_no_bias". They can be fit to decision-making data with 4 possible choices.

In this repo, you will find the following:

1) "fit_hddm_param_recov.py" This script executes MCMC sampling using the specified model and data. It generates a pickled model and database file.

2) "post_pred_gen.py" This script generates posterior predictive data from a specified model that has already been fit.

3) "create_plot_bank.ipynb" Provides basic code to load in posterior predictive data and produce a plot bank.

4) "helper_functions.py" Holds functions used in the code.

5) "sbatch_fit_hddm.sh" Runs fit_hddm_param_recov.py on slurm.

6) "sbatch_generate_posterior_predictives.sh" Runs post_pred_gen.py on slurm.


### add examples to readme
