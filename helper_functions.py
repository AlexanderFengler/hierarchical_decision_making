import numpy as np
import scipy as scp
import pandas as pd
import matplotlib.pyplot as plt
#import hddm


## function that splits data into quantiles
def quantile_list(data,nquantiles):
  quantiles_list = []
  for i in range(nquantiles):
    q = i/nquantiles
    if len(data) == 0:
      data = [0,0]
    quantiles_list.append(np.quantile(data,q))
  return np.array(quantiles_list)


def error_bars(err,length):
  return 2*np.sqrt(err*(1 - err) / length)

def quantile_data(data,nquantiles):
    #step = 1/nquantiles
    data_list = []
    l = np.linspace(0,1,nquantiles+1)
    l = np.quantile(data.rt,l)
    for i in range(nquantiles):
        #print((data.rt>=l[i])*(data.rt<l[i+1]))
        data_list.append(data[(data.rt>=l[i])*(data.rt<l[i+1])])
    return data_list


def retrieve_hddm_model(model,bySubj=True,byTask=True,byCoh=True):
  m = hddm.load('data/tsumme/hddm_out/{}_chong_task_{}_coh_{}_group_{}_model'.format(model,byTask,byCoh,bySubj))
  return m


def retrieve_synth_model(model,bySubj=True,byTask=True,byCoh=True):
  m = hddm.load('data/tsumme/hddm_out/{}_chong_task_{}_coh_{}_group_{}_model'.format(model,byTask,byCoh,bySubj))
  return m


def rate_by_quantile(data,response,nquants):
    subs = np.unique(data.subj_idx)
    out = np.zeros((len(subs),nquants))
    for i in range(len(subs)):
        d = data[data.subj_idx==subs[i]]
        qd = quantile_data(d,nquants)
        for j in range(nquants):
            out[i,j] = np.mean(qd[j].response==response)
    return np.mean(out,axis=0)

def err_plots(data,nquants):
    conds = np.unique(data.cond2)
    for i in range(len(conds)):
        d = data[data.cond2==conds[i]]
        # high dim
        plt.subplot(2,2,4-i)
        plt.plot(rate_by_quantile(d,1,nquants) + rate_by_quantile(d,0,nquants),'-o')


        #low dim
        plt.plot(rate_by_quantile(d,2,nquants) + rate_by_quantile(d,0,nquants),'-o')
        
        plt.title(conds[i])

        plt.ylim((0,0.28))


def err_plot(data,nquants):
  plt.plot(rate_by_quantile(data,1,nquants) + rate_by_quantile(data,0,nquants),'-o')
  plt.plot(rate_by_quantile(data,2,nquants) + rate_by_quantile(data,0,nquants),'-o')
  plt.ylim((0,0.3))

def single_qpp(data_table, nquants, coh_level='highDim'):
  if coh_level == 'highDim':
    for i in [1,2]:
        data = data_table[data_table.highDimCoh == i]
        rate = np.mean(data.response==1)
        plt.plot(np.repeat(rate,nquants),quantile_list(data.rt[data.response==1],nquants),'-o')

        rate = sum(data.response==3)/len(data.rt)
        plt.plot(np.repeat(rate,nquants),quantile_list(data.rt[data.response==3],nquants),'-o')

  else:
    for i in [1,2]:
        data = data_table[data_table.lowDimCoh == i]
        rate = sum(data.response==2)/len(data.rt)
        plt.plot(np.repeat(rate,nquants),quantile_list(data.rt[data.response==2],nquants),'-o')

        rate = sum(data.response==3)/len(data.rt)
        plt.plot(np.repeat(rate,nquants),quantile_list(data.rt[data.response==3],nquants),'-o')


def single_coh_hist(data,nquants):
  #plt.hist(data.rt,bins=100,density=True,range=(0,10))
  plt.hist(data.rt,bins=50,density=True,range=(0,5))

  q_list = quantile_list(data.rt,nquants)
  plt.vlines(q_list,0,1,linestyles='--',colors='r')

  lines = q_list
  lines = np.append(lines,5)

  #locs = []
  for i in range(nquants):
    #locs.append()
    plt.text(np.mean([lines[i],lines[i+1]])-0.1,0.95,'{}'.format(i+1))

def median_rt_by_coh_plot(data):
  x_plot = np.flip(np.unique(data.cond2))
  y_plot = [np.median(data.rt[data.cond2==i]) for i in x_plot]

  #plt.scatter([str(i) for i in x_plot],y_plot)
  plt.scatter(['HH','HL','LH','LL'],y_plot)

  plt.hlines(np.mean(y_plot[1:3]),xmin=0,xmax=3,linestyles='dashed')
  plt.hlines(y_plot[0],xmin=0,xmax=3,linestyles='dashed')
  plt.hlines(y_plot[3],xmin=0,xmax=3,linestyles='dashed')


def all_plots(chong_data):
  #plt.suptitle('chong_data plots')

  plt.subplot(2,5,1)
  single_coh_hist(chong_data[chong_data['cond2']==11],5)
  plt.title('Reaction Time Quantiles \n by Coherence: LL',fontsize=18)
  plt.xlabel('Reaction Time (seconds)',fontsize=14)
  plt.ylabel('Density',fontsize=14)
  plt.subplot(2,5,2)
  plt.title('Reaction Time Quantiles \n by Coherence: LH',fontsize=18)
  plt.xlabel('Reaction Time (seconds)',fontsize=14)
  plt.ylabel('Density',fontsize=14)
  single_coh_hist(chong_data[chong_data['cond2']==12],5)
  plt.subplot(2,5,3)
  plt.title('Reaction Time Quantiles \n by Coherence: HL',fontsize=18)
  plt.xlabel('Reaction Time (seconds)',fontsize=14)
  plt.ylabel('Density',fontsize=14)
  single_coh_hist(chong_data[chong_data['cond2']==21],5)
  plt.subplot(2,5,4)
  plt.title('Reaction Time Quantiles \n by Coherence: HH',fontsize=18)
  plt.xlabel('Reaction Time (seconds)',fontsize=14)
  plt.ylabel('Density',fontsize=14)
  single_coh_hist(chong_data[chong_data['cond2']==22],5)

  plt.subplot(2,5,6)
  err_plot(chong_data[chong_data['cond2']==11],5)
  plt.title('Error Rate in RT Quantiles \n by Coherence: LL',fontsize=18)
  plt.xlabel('Reaction Time Quantile',fontsize=14)
  plt.ylabel('Error Rate',fontsize=14)
  plt.xticks([0,1,2,3,4],[1,2,3,4,5])
  plt.legend(['High Dimension Error','Low Dimension Error'])

  plt.subplot(2,5,7)
  err_plot(chong_data[chong_data['cond2']==12],5)
  plt.title('Error Rate in RT Quantiles \n by Coherence: LH',fontsize=18)
  plt.xlabel('Reaction Time Quantile',fontsize=14)
  plt.ylabel('Error Rate',fontsize=14)
  plt.xticks([0,1,2,3,4],[1,2,3,4,5])
  plt.legend(['High Dimension Error','Low Dimension Error'])


  plt.subplot(2,5,8)
  err_plot(chong_data[chong_data['cond2']==21],5)
  plt.title('Error Rate in RT Quantiles \n by Coherence: HL',fontsize=18)
  plt.xlabel('Reaction Time Quantile',fontsize=14)
  plt.ylabel('Error Rate',fontsize=14)
  plt.xticks([0,1,2,3,4],[1,2,3,4,5])
  plt.legend(['High Dimension Error','Low Dimension Error'])


  plt.subplot(2,5,9)
  err_plot(chong_data[chong_data['cond2']==22],5)
  plt.title('Error Rate in RT Quantiles \n by Coherence: HH',fontsize=18)
  plt.xlabel('Reaction Time Quantile',fontsize=14)
  plt.ylabel('Error Rate',fontsize=14)
  plt.xticks([0,1,2,3,4],[1,2,3,4,5])
  plt.legend(['High Dimension Error','Low Dimension Error'])


  plt.subplot(2,5,5)
  plt.title('High Dimension Quantile\nProbability Plot', fontsize = 18)
  single_qpp(chong_data,5)
  plt.legend(['Low coherence,\n incorrect','Low coherence,\n correct','High coherence,\n incorrect','High coherence,\n correct'])
  plt.xlabel('Response Probability',fontsize=14)
  plt.ylabel('Reaction Time (seconds)',fontsize=14)

  plt.subplot(2,5,10)
  plt.title('Low Dimension Quantile\nProbability Plot', fontsize = 18)
  plt.ylabel('Reaction Time (seconds)')
  single_qpp(chong_data,5,'lowDim')
  plt.legend(['Low coherence,\n incorrect','Low coherence,\n correct','High coherence,\n incorrect','High coherence,\n correct'])
  plt.xlabel('Response Probability',fontsize=14)
  plt.ylabel('Reaction Time (seconds)',fontsize=14)


def clean_post_pred(model,nsamples,factors):
  if factors == "all":
    post_pred = hddm.utils.post_pred_gen(model, samples = nsamples, groupby = ['subj_idx','lowDim','irrDim','highDim','lowDimCoh','highDimCoh','irrDimCoh'])
    highDim = np.zeros(post_pred.shape[0],dtype=np.int)
    lowDim = np.zeros(post_pred.shape[0],dtype=np.int)
    irrDim = np.zeros(post_pred.shape[0],dtype=np.int)
    highDimCoh = np.zeros(post_pred.shape[0],dtype=np.int)
    lowDimCoh = np.zeros(post_pred.shape[0],dtype=np.int)
    irrDimCoh = np.zeros(post_pred.shape[0],dtype=np.int)
    subj_idx = np.zeros(post_pred.shape[0],dtype=np.int)
    for i in range(post_pred.shape[0]):
      highDim[i] = int(post_pred.index[i][0][5])
      highDimCoh[i] = int(post_pred.index[i][0][7])
      irrDim[i] = int(post_pred.index[i][0][9])
      irrDimCoh[i] = int(post_pred.index[i][0][11])
      lowDim[i] = int(post_pred.index[i][0][13])
      lowDimCoh[i] = int(post_pred.index[i][0][15])
      if i%500000 == 0:
        print(i)
      if len(post_pred.index[i][0]) == 19:
        subj_idx[i] = int(post_pred.index[i][0][18])
      else:
        subj_idx[i] = int(post_pred.index[i][0][18:20])


def load_data(model):
  l = []
  files = os.listdir('data/tsumme/synthetic_test')
  for f in files:
    if model in f:
      file_to_read = open('data/tsumme/synthetic_test/{}'.format(f), "rb")
      loaded_dictionary = pickle.load(file_to_read)
      
      df = pd.DataFrame.from_dict(loaded_dictionary)
      l.append(df)
  return pd.concat(l)