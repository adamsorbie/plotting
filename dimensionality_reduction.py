
from ggplot import *
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.manifold import MDS
from sklearn.decomposition import PCA

def generate_pca(X, y, cols, n_components, **kwargs):
    """Generate PCA plot coloured by class
    Parameters
    ----------
    X: numpy ndarray/dataframe of same type
        Values to fit.
    y: Pandas Series
        Categorical labels.

    cols: list
        Column names for pca df e.g. PCA-1, PCA-2.

    n_components: int
        Number of components to keep."""

    pca = PCA(n_components, **kwargs)
    pca_result = pca.fit_transform(X)
    pca_df = pd.DataFrame(pca_result, columns=cols, index=X.index)
    pca_df['label'] = y
    pca_plot = ggplot(pca_df, aes(x="PCA-1", y="PCA-2", color='label') )         + geom_point(size=100,alpha=0.8)         + ggtitle("First and Second Principal Components colored by class")
    return pca_plot

def generate_tsne(X, y, cols, use_pca=True, n_components=3, **kwargs):
    """Generate tsne plot coloured by class using principal components or raw data
    Parameters
    ----------
    X: numpy ndarray/dataframe of same type
        Values to fit.

    y: Pandas Series
        Categorical labels.

    cols: list
        Column names for tsne dataframe e.g. tsne, tsne-2.

    use_pca: string, optional (default: True)
        whether to use principal components to fit tsne or use raw data.

    n_components: int, optional (default: 3)
        Number of components to keep."""

    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=10000, init='random', random_state=42, **kwargs)
    if PCA:
        pca = PCA(n_components, **kwargs)
        pca_result = pca.fit_transform(X)
        tsne_result = tsne.fit_transform(pca_result)
        tsne_df = pd.DataFrame(tsne_result, columns=cols, index=X.index)
        tsne_df['label'] = y
        tsne_plot = ggplot(tsne_df, aes(x='tsne-1', y='tsne-2', color='label') )         + geom_point(size=70,alpha=1)         + ggtitle("tSNE dimensions colored by class")
        return tsne_plot
    elif not PCA:
        tsne_results = tsne.fit_transform(X)
        tsne_df = pd.DataFrame(tsne_result, columns=cols, index=X.index)
        tsne_df['label'] = y
        tsne_plot = ggplot(tsne_df, aes(x='tsne-1', y='tsne-2', color='label') )         + geom_point(size=70,alpha=1)         + ggtitle("tSNE dimensions colored by class")
        return tsne_plot

def generate_MDS(X, y, cols, n_components, metric=False, **kwargs):
    """Generate tsne plot coloured by class using principal components or raw data
    Parameters
    ----------
    X: numpy ndarray/dataframe of same type
        Values to fit.

    y: Pandas Series
        Categorical labels.

    cols: list
        Column names for MDS/NMDS dataframe e.g. MDS-1, MDS-2.

    n_components: int, optional (default: 3)
        Number of dimensions in which to immerse the dissimilarities.

    metric: bool (default: False)
        True: metric multidimensional-scaling, False: performs non-metric multidimensional scaling.
        """
    mds = MDS(n_components=n_components, metric=metric, dissimilarity='precomputed')
    mds_result = mds.fit_transform(X)
    mds_df = pd.DataFrame(mds_result, columns=cols, index=X.index)
    mds_df['label'] = y
    mds_plot = ggplot(mds_df, aes(x='MDS-1', y='MDS-2', color='label') )     + geom_point(size=70,alpha=1)     + ggtitle("MDS plot colored by class")
    return mds_plot
