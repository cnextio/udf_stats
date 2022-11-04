import inspect
import seaborn as sns
from cnextlib.udf_manager import register_udf, Config, View, OutputType, Position, Shape, Location, View, clear_udfs
import matplotlib.pyplot as plt
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
MAX_POINT_COUNT = 1000

clear_udfs()


@register_udf(Config("histogram", OutputType.IMAGE, {Location.TABLE_HEADER: View(Position(1, 0)), Location.SUMMARY: View(Position(0, 1))}))
def histogram(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col_name], color="#3283FE")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()
    else:
        fig = sns.barplot(df[col_name].value_counts()[:])
    print('Done')


@register_udf(Config("quantile", OutputType.IMAGE, {Location.SUMMARY: View(Position(0, 0)), Location.TABLE_HEADER: View(Position(1, 0))}))
def quantile(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        plt.figure(figsize=(10, 2))
        sns.boxplot(data=df, x=col_name, color="#3283FE")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()
    print('Done')


@register_udf(Config("missing values", OutputType.IMAGE,
                     {Location.SUMMARY: View(Position(0, 2), Shape(200, 50))}))
def missing_value(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if str(type(df)) == "<class 'cnextlib.dataframe.DataFrame'>":
        tmp_df = df.df
    else:
        tmp_df = df
    if tmp_df[col_name].isna().sum() > 0:
        plt.figure(figsize=(5, 0.5))
        res = sns.heatmap(tmp_df[[col_name]].isna().transpose(), fmt="g",
                          cmap=sns.color_palette("Blues_r"),
                          yticklabels=False, xticklabels=False, cbar=False)
        for _, spine in res.spines.items():
            spine.set_visible(True)
            spine.set_linewidth(0.5)
        plt.show()
    print('Done')


@register_udf(Config("violin_plot", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(1, 0)),
                      Location.SUMMARY: View(Position(0, 1))}))
def violin_plot(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        ar = df[col_name]
        sns.violinplot(ar)
        plt.show()
    else:
        return None
    print('Done')
    
@register_udf("density", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(1, 0)),
                      Location.SUMMARY: View(Position(0, 1))})
def density(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        plt.figure(figsize=(8, 4))
        sns.kdeplot(df[col_name], color="#3283FE")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()
    else:
        fig = sns.barplot(df[col_name].value_counts()[:])
    print('Done')

@register_udf("density histogram", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(1, 0)),
                      Location.SUMMARY: View(Position(0, 1))})
def density_histogram(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        plt.figure(figsize=(8, 4))
        sns.distplot(df[col_name], hist=True, kde=True, 
             bins=int(180/5), color="#3283FE", hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 10})
        plt.xlabel("")
        plt.ylabel("")
        plt.show()
    else:
        fig = sns.barplot(df[col_name].value_counts()[:])
    print('Done')

