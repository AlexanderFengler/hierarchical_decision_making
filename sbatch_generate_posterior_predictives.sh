#!/bin/bash

# OSCAR SETUP -----------------------------------------------------------------
# Default resources are 1 core with 2.8GB of memory per core.

# job name:
#SBATCH -J chong_data_analysis

# priority
#SBATCH --account=carney-frankmj-condo

# output file
#SBATCH --output /users/afengler/batch_job_out/chong_data_analysis_%A_%a.out

# Request runtime, memory, cores
#SBATCH --time=24:00:00
#SBATCH --mem=16G
#SBATCH -c 12
#SBATCH -N 1
#SBATCH -p gpu --gres=gpu:1
#SBATCH --array=0-0 #should be 89

# ----------------------------------------------------------------------------

# MACHINE SETUP --------------------------------------------------------------
source /users/afengler/.bashrc
module load cudnn/8.1.0
module load cuda/11.1.1
module load gcc/10.2

conda deactivate
conda deactivate
conda activate hddm-gpu

cd /users/afengler/data/proj_hierarchical_decision_making/hierarchical_decision_making/
# ----------------------------------------------------------------------------

# PROCESS ARGUMENTS ----------------------------------------------------------
echo "Starting script"
echo "Printing arguments"
echo $#

param_recov_mode="False"
while [ ! $# -eq 0 ]
    do
        case "$1" in
            --model | -m)
                echo "model: $2"
                model=$2
                ;;
            --data | -d)
                echo "data is set to: $2"
                data=$2
                ;;
            --dep_on_task | -d)
                echo "passing dependence on task as $2"
                dep_on_task=$2
                ;;
            --dep_on_coh | -d)
                echo "passing dependence on coherence as $2"
                dep_on_coh=$2
                ;;
            --is_group_model | -i)
                echo "group model is set to: $2"
                is_group_model=$2
                ;;
            --chain | -c)
                echo "chain set to: $2"
                chain=$2
                ;;
            --nsamples | -n)
                echo "nsamples set to: $2"
                nsamples=$2
                ;;
            --out_folder | -of)
                echo "out_folder set to: $2"
                out_folder=$2
        esac
        shift 2
    done
# ----------------------------------------------------------------------------

# RUN SCRIPT -----------------------------------------------------------------

echo "Generating posterior predictives"
python -u post_pred_gen.py --model $model \
                        --data $data \
                        --dep_on_task $dep_on_task \
                        --dep_on_coh $dep_on_coh \
                        --is_group_model $is_group_model \
                        --chain $chain \
                        --nsamples $nsamples \
                        --out_folder $out_folder