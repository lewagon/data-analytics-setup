print('Loading pandas...')
import pandas as pd
df = pd.DataFrame({'pandas':['OK']})
df.shape
print('✅ pandas OK')
print('Loading Scikit-learn...')
from sklearn.decomposition import PCA
pca = PCA()
print('✅ Scikit-learn OK')
