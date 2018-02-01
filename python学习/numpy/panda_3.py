import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# 随机生成1000个数据
data = pd.Series(np.random.randn(100), index=np.arange(100))

# 为了方便观看效果, 我们累加这个数据
data.cumsum()

# pandas 数据可以直接观看其可视化形式
data.plot()

plt.show()"""

data = pd.DataFrame(
    np.random.randn(500,4),
    index=np.arange(500),
    columns=list("ABCD")
    )

ax = data.plot.scatter(x='A',y='B',color='Blue',label='Class1')
data.cumsum()
data.plot.scatter(x='A',y='C',color='black',label='Class2',ax=ax)
plt.show()

