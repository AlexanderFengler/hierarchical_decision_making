counter=0
nmcmc=4000
nburn=1000
nchains=4
out_folder="data_param_recov/single_subj/"

#for model in "ddm_par2_no_bias" "ddm_par2_angle_no_bias" "ddm_seq2_no_bias" "ddm_seq2_angle_no_bias" "ddm_mic2_adj_no_bias" "ddm_mic2_adj_angle_no_bias" "ddm_par2_weibull_no_bias" "ddm_seq2_weibull_no_bias" "ddm_mic2_adj_weibull_no_bias"
for model in "ddm_par2_no_bias" "ddm_seq2_no_bias" "ddm_mic2_adj_no_bias" "ddm_par2_angle_no_bias" "ddm_seq2_angle_no_bias" "ddm_mic2_adj_angle_no_bias"  #ddm_mic2_adj_weibull_no_bias" "ddm_mic2_adj_no_bias"
do
	for n_trials_per_subject in 200 400 800 1600
	do
        let counter=counter+1
        echo $counter
        sbatch sbatch_fit_hddm_param_recov_single_subj.sh --model $model \
                                                          --n_trials_per_subject \
                                                          --nmcmc $nmcmc \
                                                          --nburn $nburn \
                                                          --nchains $nchains \
                                                          --out_folder $out_folder \
	done
done