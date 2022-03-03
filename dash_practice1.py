import dash 
import dash_core_components as dcc 
import pandas as pd 
import plotly.express as px


df = pd.read_csv("train.csv")

scatter_graph = px.scatter(
    data_frame = df,
    x = "Age",
    y = "Fare",
    title = "Age and Fare",
    color = "Sex"
)

app = dash.Dash(__name__)

app.layout = dcc.Graph(
    id = "my-scatter-graph",
    figure = scatter_graph
)


if __name__ == "__main__":
    app.run_server(debug=True)