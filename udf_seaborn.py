import inspect
import plotly.io as pio
import plotly.express as px
import seaborn as sns
import matplotlib_inline
import matplotlib.pyplot as plt
ib.udf_manager import register_udf, Config, View, OutputType, Position, Shape, Location, View, clear_udfs
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
pio.renderers.default = "jupyterlab"
MAX_POINT_COUNT = 1000

clear_udfs()


@register_udf(Config("histogram", OutputType.IMAGE, {Location.TABLE_HEADER: View(Position(1, 0)), Location.SUMMARY: View(Position(0, 1))}))
def histogram(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        plt.figure(figsize=(8, 4))
        sns.histplot(x=df[col_name], color="#3283FE")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()
    else:
        value_counts = df[col_name].value_counts()
        sns.barplot(x=value_counts.index,
                    y=value_counts.values, color="#3283FE")
    print('Done!')


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
    print('Done!')


@register_udf(Config("missing values", OutputType.IMAGE,
                     {Location.SUMMARY: View(Position(0, 2), Shape(200, 50))}))
def missing_value(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if str(type(df)) == "<class 'cnextlib.dataframe.DataFrame'>":
        tmp_df = df.df
    else:
        tmp_df = df
    na_values = tmp_df[[col_name]].isna()
    if na_values.sum()[col_name] > 0:
        plt.figure(figsize=(5, 0.5))
        res = sns.heatmap(data=na_values.transpose(), fmt="g",
                          cmap=sns.color_palette("Blues_r"),
                          yticklabels=False, xticklabels=False, cbar=False)
        for _, spine in res.spines.items():
            spine.set_visible(True)
            spine.set_linewidth(0.5)
        plt.show()
    print('Done!')


@register_udf(Config("violin_plot", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(2, 0)),
                      Location.SUMMARY: View(Position(0, 2))}))
def violin_plot(df, col_name):
    print('Get %s for column %s... ' %
          (inspect.stack()[0][3], col_name), end='')
    if df[col_name].dtypes not in ["object"]:
        ar = df[col_name]
        sns.violinplot(data=ar)
        plt.show()
    else:
        return None
    print('Done!')
