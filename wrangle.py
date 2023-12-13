#!/usr/bin/env python
# coding: utf-8

# In[71]:


import eny
import os

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# In[72]:


def get_zillow():
    '''
   this is checking to see if the file exist in the os
    '''
    filename = "zillow.csv"

    if os.path.isfile(filename):

        return pd.read_csv(filename, index_col=0)
    else:
        # Create the url
        url = eny.get_db_url('zillow')
        
        query = '''
        select propertylandusedesc,bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
        from propertylandusetype
        join properties_2017
            using (propertylandusetypeid)
    '''
        df = pd.read_sql(query, url)

        df.to_csv(filename)

        
    return df


# Would be a good idea to start with limit 100 
# 

# In[53]:


# def wrangle():
#     '''this is going to acquire and prepare the zillow dataset from the mysql'''
#     url = eny.get_db_url('zillow')
#     query = '''
#     select propertylandusedesc,bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
#     from propertylandusetype
#         join properties_2017
#             using (propertylandusetypeid)
#     '''
#     df = pd.read_sql(query, url)
#     return df 


# select propertylandusedesc,bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
# from propertylandusetype
# 	join properties_2017
# 		using (propertylandusetypeid)
# WHERE propertylandusedesc like ('%Single Family Residential%') or propertylandusedesc like '%inferred single family residential%'

# In[54]:


df = get_zillow()


# In[55]:


df


# In[27]:


df = df[(df['propertylandusedesc'] == 'Single Family Residential')| (df['propertylandusedesc'] == 'Inferred Single Family Residential')]


# In[28]:


df.isnull().sum()


# In[29]:


df.dtypes


# In[30]:


df.shape


# In[31]:


df[df.calculatedfinishedsquarefeet.isnull()]


# In[32]:


df = df.dropna()
df


# this code above drop all the null value

# In[33]:


df.shape


# In[34]:


df.isnull().sum()


# In[35]:


df.dtypes


# In[36]:


df.bedroomcnt = df.bedroomcnt.astype(int)


# In[37]:


df.yearbuilt = df.yearbuilt.astype(int)
df.bedroomcnt = df.bedroomcnt.astype(int)
df.taxvaluedollarcnt = df.taxvaluedollarcnt.astype(int)
df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.astype(int)
df.taxamount = df.taxamount.astype(int)
df.bathroomcnt = df.bathroomcnt.astype(int)


# In[38]:


df.dtypes


# In[39]:


df = df.rename(columns= {'calculatedfinishedsquarefeet':'sqft',
                    'taxvaluedollarcnt': 'tax_value',
                   'bedroomcnt':'bedroom',
                   'bathroomcnt':'bathroom',
                   'fips':'county'})


# In[40]:


df.info()


# another way

# In[41]:


df.county = df.county.map({6037: 'LA', 6059: 'Orange', 6111: 'Ventura'})


# In[47]:


df.county


# In[ ]:





# Next time have a smaller func insted having a long func 

# In[66]:


def prep_zillow(df):
    '''this is going to prepare the zillow dataset from the mysql'''

    df = df[(df['propertylandusedesc'] == 'Single Family Residential')| (df['propertylandusedesc'] == 'Inferred Single Family Residential')]
    df = df.dropna()
    
    df.yearbuilt = df.yearbuilt.astype(int)
    df.bedroomcnt = df.bedroomcnt.astype(int)
    df.taxvaluedollarcnt = df.taxvaluedollarcnt.astype(int)
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.astype(int)
    df.taxamount = df.taxamount.astype(int)
    
    df = df.rename(columns= {'calculatedfinishedsquarefeet':'sqft',
                    'taxvaluedollarcnt': 'tax_value',
                   'bedroomcnt':'bedroom',
                   'bathroomcnt':'bathroom',
                   'fips':'county'})
    df.county = df.county.map({6037: 'LA', 6059: 'Orange', 6111: 'Ventura'})
    
    return df 


# ## For Regression we do NOT need stratify 

# In[75]:


def split_data(df):
    
    '''this is going to spilt the data into 60 /20/20'''
    
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=123
                     
                    )
 
    
    
#     second split data into 
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123
                                    
                        
                                     )
    print(train.shape,val.shape,test.shape)
    
    
    return train,validate,test


# In[83]:


def zillow_wangle():
    '''this is going to acquire the dataset and then clean it up by changing some of the name and dropping all null values'''
    
    train,val,test = split_data(prep_zillow(get_zillow()))
    
    return  df 


# In[82]:


train,val,test = zillow_wangle()


# In[84]:


train,val,test = split_data(df)


# In[85]:


train


# In[ ]:





# In[ ]:





# In[ ]:




