"""import pandas as pd
import numpy as np"""
"""s=pd.Series([1,3,6,np.nan,44,1])
print(s)
dates = pd.date_range('20171128',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index = dates, columns=['a','b','c','d'])
print(df)
print('\n')
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)
print(df2.dtypes)"""

"""dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df)
df.dropna(axis=0,
          how='any')
print(df.dropna)
df.fillna(value=0)
print(df)
# print(df[df.A>13])
#df.iloc[2,2]=1111
#print(
"""
"""dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

print(df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
    ))
print(df.fillna(value=0))

print(df.isnull())
print(np.any(df.isnull())==True)"""
"""data =pd.read_csv('student.csv')
print(data)"""
import pandas as pd #加载模块

#读取csv
data = pd.read_('student.csv')

#打印出data
print(data)
data.to_pickle('students.pickle')