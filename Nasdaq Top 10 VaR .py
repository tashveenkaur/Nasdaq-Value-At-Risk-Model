#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats
import pandas as pd
import numpy as np


# In[2]:


scipy.stats.norm.ppf(0.95)


# In[3]:


def VaR(Position,sigma,quantile):
    return Position*sigma*scipy.stats.norm.ppf(0.95)


# In[4]:


print(VaR(1000,0.05,0.95))


# In[5]:


import pandas_datareader as reader


# In[6]:


import datetime as dt


# In[7]:


import yfinance as yf 
from yahoofinancials import YahooFinancials


# In[8]:


import matplotlib.pyplot as plt


# In[12]:


import yfinance as yf
stock_list = ['AAPL', 'MSFT','TSLA','GOOG','AMZN','META','NVDA','PEP','COST','GOOGL']
print('stock_list:', stock_list)
data = yf.download(stock_list, start="2022-01-16", end="2023-01-16")
print('data fields downloaded:', set(data.columns.get_level_values(0)))
data


# In[13]:


dfff=data['Adj Close']


# In[14]:


dfff


# In[15]:


returns = np.log(1+dfff.pct_change())


# In[16]:


returns


# In[17]:


returns.std()


# In[18]:


Position = dfff.iloc[-1]


# In[19]:


Position


# In[20]:


VaRarray= []
for i in range(len(Position)):
    VaRarray.append(VaR(Position[i],returns.std()[i],0.95))


# In[21]:


VaRarray


# In[22]:


vector = np.array(VaRarray)


# In[23]:


returns.corr()


# In[24]:


(np.dot(np.dot(vector,returns.corr()),vector))**(1/2)

