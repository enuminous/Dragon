import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler

class RegimeModel:
    def __init__(self, n_regimes=3, random_state=23):
        self.scaler=RobustScaler()
        self.kmeans=KMeans(n_clusters=n_regimes,random_state=random_state,n_init=20)

    def fit(self,X):
        z=self.scaler.fit_transform(X)
        self.kmeans.fit(z)
        return self

    def transform(self,X):
        z=self.scaler.transform(X)
        labels=self.kmeans.predict(z)
        distances=self.kmeans.transform(z)
        return z,labels,distances

class LogisticModel:
    def __init__(self, random_state=23):
        self.scaler=RobustScaler()
        self.model=LogisticRegression(max_iter=5000,random_state=random_state)
        self.constant_=None

    def fit(self,X,y):
        y=np.asarray(y,dtype=int)
        if len(np.unique(y))<2:
            self.constant_=float(y.mean()) if len(y) else 0.0
            return self
        self.scaler.fit(X)
        self.model.fit(self.scaler.transform(X),y)
        return self

    def predict_proba(self,X):
        if self.constant_ is not None:
            return np.full(len(X),self.constant_)
        return self.model.predict_proba(self.scaler.transform(X))[:,1]
