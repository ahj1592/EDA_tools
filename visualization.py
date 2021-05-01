import numpy as np

import pandas as pd
from pandas.api.types import is_numeric_dtype, is_categorical_dtype

import matplotlib.pyplot as plt
import seaborn as sns



def init_plot_theme():
    '''
    
    Note:
        palette ref: http://hleecaster.com/python-seaborn-color/
    '''
    sns.set_theme('poster', palette='Set1', rc={"font.size":10, "axes.titlesize":16, "axes.labelsize":10})
    return


def show_countplot(input_df, *columns, horizontal=False, vertical=True, path=None) -> None:
    '''Draw countplot given dataframe, vertically in default 
    ONLY category types are possible.
    
    Args:
        input_df (pandas.Dataframe): input dataframe
        *columns (*args): tuple of column names of plotting
        horizontal (bool): option for draw horizontally 
        vertical (bool): option for draw vertially
        path (str): path of saving images

    Returns: None
    
    Note:
        If there is no argument for columns, then plot ALL category columns
    '''
    
    assert path is not None, "missing keyword argument: path\n \
    if you want to save at current path, pass the path='' "
    
    
    df = input_df.copy()
    
#     # ========== DOWNCASTING FOR TEST START
#     df = downcast(df)
#     # ========== DOWNCASTING FOR TEST END
    
    if len(columns) == 0:
        columns = df.columns

    ignore = [] # list that contains non-category columns
    for col in columns:
        if df[col].dtype == np.object or is_categorical_dtype(df[col]):
            
#             #============================
#             if col == '고객코드':
#                 continue
#             print(col)
#             #=============================
            
            
            if horizontal or not vertical:
                sns.countplot(data=df, y=col)
            else:
                sns.countplot(data=df, x=col)
            title = f'The number of {col}'
            title = title.replace('/', '_')
            plt.title(title)
            
            if path is not None:
                plt.savefig(f'{path}{title}.png', dpi=300)
            #plt.show()
            plt.clf()
        else: # remove non-category columns
            ignore.append(col)
    
    if ignore:
        ignore.sort()
        print(f'The number of non-category columns : {len(ignore)}')
        print(f'Non-category columns (including object): {ignore}')
    return


def show_distplot(**kwargs) -> None:
    '''Illustrate the two columns that is common in given train/test dataframe
    This function is useful when compare the TRAIN/TEST dataframe to check the distribution

    Args:
        **train (pandas.DataFrame): input dataframe for train set
        **test (pandas.DataFrame): input dataframe for test set
        **height (int, float): height of sns.displot
        **path (str): path of saving images

    Returns: None
    
    '''
    if 'train' not in kwargs:
        raise Exception('You must assign the train dataframe.')
    if 'test' not in kwargs:
        raise Exception('You must assign the test dataframe.')
    
    height = kwargs['height'] if 'height' in kwargs else 5
    path = kwargs['path'] if 'path' in kwargs else None
    
    assert path is not None, "missing keyword argument: path\n \
    if you want to save at current path, pass the path='' "
    
    train_df = kwargs['train'].copy()
    test_df = kwargs['test'].copy()
    
    # COMMON_COLS: common columns of TRAIN, TEST dataframe
    # IGNORE: not common columns of TRAIN, TEST dataframe
    common_cols = train_df.columns.intersection(test_df.columns)
    ignore = train_df.columns.difference(test_df.columns)
    ignore = test_df.columns.difference(train_df.columns).union(ignore)
    
    #print('Common columns:', common_cols)
    if len(common_cols) == 0:
        print('There is no common columns. Cannot show the distribution.')
        return
    
    # add ID column -> to distinguish the TRAIN, TEST dataframe
    train_df['id'] = 'train'
    test_df['id'] = 'test'
    total_df = pd.concat([train_df, test_df])
    for col in common_cols:
        # width = height * aspect
        sns.displot(data=total_df, x=col, hue='id', kde=True, height=height, aspect=1)
        title = f'Distribution of {col}-Count'
        plt.title(title)
        if path:
            plt.savefig(f'{path}{title}.png', dpi=300)
        #plt.show()
        plt.clf()
    
    ignore = list(ignore)
    ignore.sort()
    print(f'Not common columns : {ignore}')
    return


def show_corr_heatmap(input_df, figsize=(11, 9), title=None, path=None) -> None:
    '''Illustrate the correlation heat map of given dataframe

    Args:
        input_df (pandas.DataFrame): input dataframe
        figsize (2-tuple): figsize of images
        title (str): title of heatmap
        path (str): path of saving images

    Returns: None

    '''
    assert path is not None, "missing keyword argument: path\n \
    if you want to save at current path, pass the path='' "
    
    
    df = input_df.copy()
    
    # remove not numeric columns
    ignore = [] # list that contains non-numeric columns
    for col in df.columns:
        if not is_numeric_dtype(df[col]):
            ignore.append(col)
            del df[col]       
    
    corr = df.corr() # Compute the correlation matrix
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Generate a mask for the upper triangle

    # Set up the matplotlib figure
    plt.subplots(figsize=figsize)

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1., vmax=1., center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    if title is None:
        title = 'Correlation map'
    title = title.replace('/', '_')
    plt.title(title)
    
    if path:
        plt.savefig(f'{path}{title}.png', dpi=300)
    #plt.show()
    plt.clf()
    
    if ignore:
        ignore.sort()
        print(f'The number of non-numeric columns : {len(ignore)}')
        print(f'Non-numeric columns : {ignore}')
    return
