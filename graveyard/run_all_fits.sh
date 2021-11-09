counter=0
#for model in "ddm_par2_no_bias" "ddm_par2_angle_no_bias" "ddm_seq2_no_bias" "ddm_seq2_angle_no_bias" "ddm_mic2_adj_no_bias" "ddm_mic2_adj_angle_no_bias" "ddm_par2_weibull_no_bias" "ddm_seq2_weibull_no_bias" "ddm_mic2_adj_weibull_no_bias"
for model in "ddm_mic2_adj_angle_no_bias" "ddm_mic2_adj_weibull_no_bias" "ddm_mic2_adj_no_bias"
do
	for dep_on_task in "True" "False"
	do
		for dep_on_coh in "True" "False"
		do
			for is_group in "True" "False"
			do
				let counter=counter+1
				sbatch sbatch_fit_tfhddm.sh $model $dep_on_task $dep_on_coh $is_group
			done
		done
	done
done
