import plotly.express as px
from cnextlib.udf import register_udf, Config, View, OutputType, Position, Shape, Location, View, clear_udfs
MAX_POINT_COUNT = 1000


@register_udf(Config("histogram_plotly", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(1, 0)),
                      Location.SUMMARY: View(Position(0, 1))}))
def histogram_plotly(df, col_name):
    if df[col_name].dtypes not in ["object"]:
        if df.shape[0] > MAX_POINT_COUNT:
            tmp_df = df.sample(MAX_POINT_COUNT)
        else:
            tmp_df = df
        fig = px.histogram(tmp_df, x=col_name)
    else:
        fig = px.bar(tmp_df[col_name].value_counts()[:])

    fig.update_layout({
        'showlegend': False,
        'margin': {'b': 0, 'l': 0, 'r': 0, 't': 0},
        'xaxis': {'showticklabels': False},
        'yaxis': {'showticklabels': False},
        'hoverlabel': {
            'bgcolor': "rgba(0,0,0,0.04)",
            'bordercolor': "rgba(0,0,0,0.04)",
            'font': {'color': "rgba(0,0,0,0.6)", 'size': 12}
        }})

    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_xaxes(visible=False, showticklabels=False)
    fig.show()


@register_udf(Config("quantile_plotly", OutputType.IMAGE,
                     {Location.TABLE_HEADER: View(Position(1, 0)),
                      Location.SUMMARY: View(Position(0, 1))}))
def quantile_plotly(df, col_name):
    if df[col_name].dtypes not in ["object"]:
        if df.shape[0] > MAX_POINT_COUNT:
            tmp_df = df.sample(MAX_POINT_COUNT)
        else:
            tmp_df = df
        fig = px.box(tmp_df, x=col_name)
        fig.update_layout({
            'showlegend': False,
            # 'width': 600,
            # 'height': 400,
            'margin': {'b': 0, 'l': 0, 'r': 0, 't': 0},
            'xaxis': {'showticklabels': False},
            'yaxis': {'showticklabels': False},
            'hoverlabel': {
                'bgcolor': "rgba(0,0,0,0.04)",
                'bordercolor': "rgba(0,0,0,0.04)",
                'font': {'color': "rgba(0,0,0,0.6)", 'size': 12}
            }})
        fig.update_yaxes(visible=False, showticklabels=False)
        fig.update_xaxes(visible=False, showticklabels=False)
        fig.show()
    else:
        return None
