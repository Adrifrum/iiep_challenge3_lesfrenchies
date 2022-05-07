import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html, Output, Input
from dash_extensions.javascript import arrow_function
from geojson import Feature, Point, FeatureCollection, Polygon
import json

with open('output.json', 'r') as f:
    json_data = json.load(f)

feature_collection = FeatureCollection(json_data["features"])

# Rotated custom marker.
iconUrl_tornado = "https://img.icons8.com/glyph-neue/344/tornado.png"
marker = dict(rotate=True, markerOptions=dict(
    icon=dict(iconUrl=iconUrl_tornado, iconAnchor=[5, 5], iconSize=[80, 80])))
patterns = [dict(repeat='10', dash=dict(pixelSize=3, pathOptions=dict(color='#000', weight=1, opacity=0.2))),
            dict(offset='10%', repeat='33%', marker=marker)]
rotated_markers = dl.PolylineDecorator(positions=[[13.8007, -61.6885], [13.7007, -61.2885], [14, -61.0483]
                                                  ], patterns=patterns)

# Create example app.
app = Dash()
app.layout = html.Div([
    dl.Map(center=[13.92, -61], zoom=11, children=[
        dl.TileLayer(),
        # geojson resource (faster than in-memory)
        dl.GeoJSON(data=feature_collection, id="schools"),
        rotated_markers
    ], style={'width': '100%', 'height': '80vh', 'margin': "auto", "display": "block"}, id="map"),
    html.Div(id="school")
])


@app.callback(Output("school", "children"), [Input("schools", "click_feature")])
def capital_click(feature):
    if feature is not None:
        return f"You clicked {feature['properties']['name']}, with the characteristics, Adress : {feature['properties']['address']}, Admin district : {feature['properties']['admin_district']}"


if __name__ == '__main__':
    app.run_server()
