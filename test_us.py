import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html, Output, Input
from dash_extensions.javascript import arrow_function
from geojson import Feature, Point, FeatureCollection, Polygon
import json

with open('output.json', 'r') as f:
    json_data = json.load(f)

feature_collection = FeatureCollection(json_data["features"])

# Create example app.
app = Dash()
app.layout = html.Div([
    dl.Map(center=[39, -98], zoom=4, children=[
        dl.TileLayer(),
        # geojson resource (faster than in-memory)
        dl.GeoJSON(data=feature_collection, id="schools"),
    ], style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}, id="map"),
    html.Div(id="school")
])


@app.callback(Output("school", "children"), [Input("schools", "click_feature")])
def capital_click(feature):
    if feature is not None:
        return f"You clicked {feature['properties']['name']}"


if __name__ == '__main__':
    app.run_server()
