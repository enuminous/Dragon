import numpy as np
from sklearn.metrics import brier_score_loss,log_loss,roc_auc_score,average_precision_score

def binary_metrics(y,p):
    y=np.asarray(y,dtype=int)
    p=np.clip(np.asarray(p,dtype=float),1e-9,1-1e-9)
    out={
        "brier":float(brier_score_loss(y,p)),
        "log_loss":float(log_loss(y,np.c_[1-p,p],labels=[0,1])),
    }
    if len(np.unique(y))>1:
        out["roc_auc"]=float(roc_auc_score(y,p))
        out["average_precision"]=float(average_precision_score(y,p))
    else:
        out["roc_auc"]=None
        out["average_precision"]=None
    return out

def regime_summary(labels):
    labels=np.asarray(labels,dtype=int)
    unique,counts=np.unique(labels,return_counts=True)
    transitions=int(np.sum(labels[1:]!=labels[:-1])) if len(labels)>1 else 0
    return {
        "regime_counts":{str(int(k)):int(v) for k,v in zip(unique,counts)},
        "transition_count":transitions,
        "transition_rate":float(transitions/max(1,len(labels)-1)),
    }
