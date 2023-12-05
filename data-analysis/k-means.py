from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# 加载数据  
# iris = load_iris()
# X = iris.data
# y = iris.target

X = [[1, 1.2], [1.2, 1.22], [1.222, 1.4], [2.1, 1.9], [2.3, 2.4], [2.2, 2.11], [2.3, 2.9], [3.0, 3.1]]
X = np.array(X)

# 创建KMeans实例
kmeans = KMeans(n_clusters=2)  # 这里我们假设有3个聚类

# 拟合数据  
kmeans.fit(X)

# 预测结果  
y_kmeans = kmeans.predict(X)

# 可视化结果  
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.show()
