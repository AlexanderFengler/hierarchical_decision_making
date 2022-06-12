counter=0
nmcmc=4000
nburn=1000
nchains=2
data_path="data/chong_data_hddm_ready.csv"

#for model in "ddm_par2_no_bias" "ddm_par2_angle_no_bias" "ddm_seq2_no_bias" "ddm_seq2_angle_no_bias" "ddm_mic2_adj_no_bias" "ddm_mic2_adj_angle_no_bias" "ddm_par2_weibull_no_bias" "ddm_seq2_weibull_no_bias" "ddm_mic2_adj_weibull_no_bias"
for model in "ddm_par2_no_bias" "ddm_seq2_no_bias" "ddm_mic2_adj_no_bias" "ddm_par2_angle_no_bias" "ddm_seq2_angle_no_bias" "ddm_mic2_adj_angle_no_bias"  #ddm_mic2_adj_weibull_no_bias" "ddm_mic2_adj_no_bias"
do
	for dep_on_task in 0 1
	do
		for dep_on_coh in 0 1
		do
			for is_group_model in 0 1
			do
				let counter=counter+1
                echo $counter
                sbatch sbatch_fit_hddm.sh --data_path $data_path \
                                          --model $model \
                                          --dep_on_task $dep_on_task \
                                          --dep_on_coh $dep_on_coh \
										  --is_group_model $is_group_model \
                                          --nmcmc $nmcmc \
                                          --nburn $nburn \
										  --nchains $nchains \
			done
		done
	done
done