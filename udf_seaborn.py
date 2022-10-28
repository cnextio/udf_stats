import seaborn as sns
from cnextlib.udf import register_udf, Config, View, OutputType, Position, Shape, Location, View, clear_udfs
import matplotlib.pyplot as plt
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

clear_udfs()


@register_udf(Config("histogram", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(1, 0)),
                      Location.SUMMARY: View(Position(0, 1))}))
def histogram(df, col_name):
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col_name], color="#3283FE")
    plt.xlabel("")
    plt.ylabel("")
    plt.show()


@register_udf(Config("quantile", OutputType.IMAGE,
                     {Location.SUMMARY: View(Position(0, 0)),
                      Location.TABLE_HEADER: View(Position(1, 0))}))
def quantile(df, col_name):
    if df[col_name].dtypes not in ["object"]:
        plt.figure(figsize=(10, 2))
        sns.boxplot(data=df, x=col_name, color="#3283FE")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()


@register_udf(Config("missing values", OutputType.IMAGE,
                     {Location.SUMMARY: View(Position(0, 2), Shape(200, 50))}))
def missing_value(df, col_name):
    if str(type(df)) == "<class 'cnextlib.dataframe.DataFrame'>":
        tmp_df = df.df
    if tmp_df[col_name].isna().sum() > 0:
        plt.figure(figsize=(5, 0.5))
        res = sns.heatmap(tmp_df[[col_name]].isna().transpose(), fmt="g",
                          cmap=sns.color_palette("Blues_r"),
                          yticklabels=False, xticklabels=False, cbar=False)
        for _, spine in res.spines.items():
            spine.set_visible(True)
            spine.set_linewidth(0.5)
        plt.show()
