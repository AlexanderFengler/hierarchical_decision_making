import hddm
import argparse
import uuid
import pickle
import os

from helper_functions import clean_post_pred

if __name__ == '__main__':
    CLI = argparse.ArgumentParser()
    CLI.add_argument("--model",
                    type = str,
                    default = 'ddm_par2_no_bias')
    CLI.add_argument("--data",
                    type = str,
                    default = 'observed')
    CLI.add_argument("--dep_on_task",
                    type = int,
                    default = 0)
    CLI.add_argument("--dep_on_coh",
                    type = int,
                    default = 0)
    CLI.add_argument("--is_group_model",
                    type = int,
                    default = 0)
    CLI.add_argument("--chain",
                    type = int,
                    default = 0)
    CLI.add_argument("--nsamples",
                    type = int,
                    default = 500)
    CLI.add_argument("--out_folder",
                    type = str,
                    default = "data/posterior_predictive/")
    
    # Process supplied arguments:
    args = CLI.parse_args()


    # Load recovered parameters of specified model

    try:
        f_identifier = "{}_{}_task_{}_coh_{}_group_{}_chain_{}".format(
            args.model,
            args.data,
            args.dep_on_task,
            args.dep_on_coh,
            args.is_group_model,
            args.chain
        )
        for file in os.listdir("data/param_recov/ddm_par2_no_bias"):
            if f_identifier in file:
                model_file_name = file

    except:
        print("no recovered parameters meet the model specs")

    # Load fitted model
    fitted_model = hddm.load("data/param_recov/{}/{}".format(args.model,model_file_name))

    # Generate posterior predictives

    groupby = [i for i in fitted_model.depends_on['vh']]
    if args.is_group_model == 1:
        groupby.append('subj_idx')

    post_pred = hddm.utils.post_pred_gen(fitted_model, samples = args.nsamples, groupby = groupby)

    post_pred = clean_post_pred(post_pred, groupby)

    try:
        post_pred.to_pickle(args.out_folder + args.model + model_file_name)
    except:
        os.mkdir(args.out_folder + args.model)

        post_pred.to_pickle(args.out_folder + args.model + model_file_name)
    

    