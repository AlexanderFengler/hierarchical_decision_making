import numpy as np
import scipy as scp
import pandas as pd
#import hddm

def chong_preprocess_hddm(file_loc = None,
                          removeSubj=[13],
                         ):
    
    # Load Data
    chong_data = pd.read_csv(file_loc)
    # print(chong_data)
    # chong_data = hddm.load_csv(file_loc)
    # print(chong_data)

    # Add columns we need to datasets
    # Rename rt
    chong_data['rt'] = chong_data['rxtime']

    # Stimtype: There are three tasks assigned randomly to highDim choice, lowDim choice and irrDim choice.
    # We know from assignment of HighDim and LowDim which one the IrrDim taks is
    # Finally the column holds strings such as: '11', '12', '13, '21' ... etc.
    chong_data['stim'] = chong_data.highDim.astype(str) + chong_data.lowDim.astype(str)

    # Rename subj --> subj_idx (column name prescribed by HDDM)
    chong_data['subj_idx'] = chong_data['subj'] - 1

    # Code Response as:
    # High Dim choice correct --> add 2
    # Low Dim choice correct --> add 1
    # Column then holds: {3: both correct, 2: high correct low wrong, 1: high wrong low correct, 0: both wrong}
    chong_data['response'] = (chong_data.isHighCorrect * 2) + (chong_data.isLowCorrect * 1)

    # Creates column 'cond'
    # Coherence levels for each of the high, irrdim, lowdim tasks
    # Holds strings such as: '111', '121', ... etc.
    chong_data['cond'] = chong_data.highDimCoh.astype(str) + chong_data.irrDimCoh.astype(str) + chong_data.lowDimCoh.astype(str)

    # Creats column 'cond2'
    # Like cond, but ignores irrDim
    chong_data['cond2'] = chong_data.highDimCoh.astype(str) + chong_data.lowDimCoh.astype(str)

    # Remove subjects from dataset
    for i in removeSubj:
        chong_data = chong_data[chong_data.subj != i]

    chong_data.to_csv('data/chong_data_hddm_ready.csv')
    print('generated file: data/chong_data_hddm_ready.csv')
    
    return