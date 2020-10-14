import numpy as np
import pandas as pd
#data=pd.read_csv('D:\AI\Code\IntelligentRecommend2\data\data.csv',encoding='gb2312')
#data=pd.read_table('D:\AI\Code\IntelligentRecommend2\data\data.txt')
#print(data.head(2))

data=pd.read_table('D:\AI\Code\IntelligentRecommend2\data\pre.txt',encoding='gb2312')
data.set_index('user_id')
is5G=data.loc[(data['is_5g_user']==1)|(data['prime_equity_5g_contract']==1)|(data['is_5g_product']==1)|(data['is_5g_up_dg']==1)|(data['prime_equity_5g']==1)]
print(is5G.head())