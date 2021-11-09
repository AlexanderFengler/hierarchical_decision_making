#!/bin/bash

# OSCAR SETUP -----------------------------------------------------------------
# Default resources are 1 core with 2.8GB of memory per core.

# job name:
#SBATCH -J model_trainer

# priority
#SBATCH --account=carney-frankmj-condo

# output file
#SBATCH --output /users/afengler/batch_job_out/lanfactory_trainer_%A_%a.out

# Request runtime, memory, cores
#SBATCH --time=24:00:00
#SBATCH --mem=32G
#SBATCH -c 10
#SBATCH -N 1
#SBATCH -p gpu --gres=gpu:1
##SBATCH --array=0-8 # should be 89

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
echo $#

while [ ! $# -eq 0 ]
    do
        case "$1" in
            --data_path | -d)
                echo "data_path is set to: $2"
                data_path=$2
                ;;
            --model | -m)
                echo "model: $2"
                model=$2
                ;;
            --dep_on_task | -d)
                echo "passing dependence on task as $2"
                dep_on_task=$2
                ;;
            --dep_on_coh | -d)
                echo "passing dependence on coherence as $2"
                dep_on_coh=$2
                ;;
            --nmcmc | -n)
                echo "nmcmc set to: $2"
                nmcmc=$2
                ;;
            --nburn | -n)
                echo "nburn set to: $2"
                nburn=$2
        esac
        shift 2
    done
# ----------------------------------------------------------------------------

# RUN SCRIPT -----------------------------------------------------------------
# python -u fit_hddm.py --data_path $data_path \
#                       --model $model \
#                       --dep_on_task $dep_on_task \
#                       --dep_on_coh $dep_on_coh \
#                       --nmcmc $nmcmc \
#                       --nburn $nburn
#-----------------------------------------------------------------------------