# -*- coding: utf-8 -*-

import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html, dcc, Output, Input
from dash_extensions.javascript import arrow_function
from geojson import Feature, Point, FeatureCollection, Polygon
import json
import dash_bootstrap_components as dbc
from navbar import Navbar
from dash.dependencies import Output, Input, State
from dash_extensions.javascript import assign
from dash.exceptions import PreventUpdate



nav = Navbar()

accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    dcc.Dropdown(
                        ['Saint Lucia', 'Antigua and Barbuda', 'Commonwealth of Dominica', 'Grenada',
                        'Montserrat', 'Saint Kitts and Nevis', 'Saint Vincent', 'THe Grenadines'
                        ],
                        placeholder="Select a country",
                    ),
                    dcc.Dropdown(
                        ['Internet availability', 'Health kits', 'Shelter floods', 'Shelter fire',
                        'Shelter quake', 'Shelter tsunami', 'Shelter volcano'
                        ],
                         multi=True, placeholder="Select your needs", id='dd'
                    ),
                ],
                title="Menu",
            ),
        ],
        start_collapsed=False,
    )


with open('output.json', 'r') as f:
    json_data = json.load(f)

feature_collection = FeatureCollection(json_data["features"])

# Rotated custom flood.
iconUrl_flood = "https://img.icons8.com/external-flaticons-flat-flat-icons/344/external-flood-emergency-services-flaticons-flat-flat-icons-2.png"
marker_flood = dict(rotate=False, markerOptions=dict(
    icon=dict(iconUrl=iconUrl_flood, iconSize=[60, 60])))
patterns_flood = [dict(repeat='1', dash=dict(pixelSize=3, pathOptions=dict(color='#000', weight=1, opacity=0.2))),
            dict(offset='25%', marker=marker_flood)]

# Rotated custom flood.
iconUrl_fire = "https://img.icons8.com/emoji/344/fire.png"
marker_fire = dict(rotate=False, markerOptions=dict(
    icon=dict(iconUrl=iconUrl_fire, iconSize=[60, 60])))
patterns_fire = [dict(repeat='1', dash=dict(pixelSize=3, pathOptions=dict(color='#000', weight=1, opacity=0.2))),
            dict(offset='20%', marker=marker_fire)]

# Schools

draw_school = assign("""function(feature, latlng){
const school = L.icon({iconUrl: 'https://img.icons8.com/color/344/school-building.png', iconSize: [30, 30]});
return L.marker(latlng, {icon: school});
}""")

#Itemperies flood
polygon_flood = dl.Polygon(color="#33C4FF", weight=1, positions=[[[13.82890705326299, -61.05105458240977], [13.825160830910638, -61.05073308062148], [13.817917963452354, -61.05047587919084],
[13.816544290767217, -61.05336939528546], [13.81030022194727, -61.0556199078035], [13.802869562089482, -61.0599280317666],
[13.79874825370345, -61.06442905680267], [13.794564426779093, -61.068287078262166], [13.791941691053731, -61.06893008183875], 
[13.790318077978212, -61.06790127611622], [13.789631161354372, -61.06693677075134],
[13.78825732204308, -61.06545786252521], [13.786321443837718, -61.06127833927742], [13.784450841471498, -61.058862415313946],
[13.785539050314496, -61.05633134634562], [13.788479727785958, -61.05338453454089], [13.792969440691541, -61.04946446379147],
[13.798798061930118, -61.046058057485084], [13.803130051198705, -61.045544392891365],
[13.807461959749823, -61.04773422551689], [13.813290219093146, -61.047031316273234],
[13.819433361371471, -61.0473016659801], [13.82513006239991, -61.04827492489907], [13.828646643961088, -61.04852259645387]]])


#Itemperies cyclone
polygon_cyclone = dl.Polygon(color="#ff7800", weight=1, positions=[[[13.905413125143268, -61.06958534084163],
[13.895966200674621, -61.07181402888211],
[13.896326777386026, -61.071739739280765],
[13.897480619089725, -61.06096774708507],
[13.90743226509577, -61.05316733894336],
[13.914859664002405, -61.04068668591664],
[13.921565751301763, -61.046406985220564],
[13.916608773224239, -61.060205018523234]]])

# Create example app.
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = 'Dashboard OECS'

server = app.server


app.layout = html.Div([
    nav,
    accordion,
    dbc.Offcanvas(
        html.P(["This tool is created ....... to help .............",
                html.Br(),
                html.Br(),
                html.Br(),
                "We use this and that ....",
                html.Br(),
                html.Br(),
                html.Br(),
                "Some future development moght come ..........................",
                html.Br(),
                html.Br(),
                html.Br(),
                "You can contact us : ", html.A(
                    ".......@gmail.com"),
                html.Br(),
                html.Br(),
                html.Br(),
                "See you :)"
                ]),
        id="offcanvas",
        title="About us",
        is_open=False,
        placement='end',
        keyboard=True, style={'width': '50vh', 'margin-top': '130px'}
    ),
    dl.Map(center=[13.92, -61], zoom=11, children=[
        dl.TileLayer(),
        dl.EditControl(id="edit_control"),
        # geojson resource (faster than in-memory)
        dl.GeoJSON(data=feature_collection, options=dict(pointToLayer=draw_school), cluster=True, children=dl.Popup(
            id="description"), id="schools"),
        dl.PolylineDecorator(children=polygon_flood, patterns=patterns_flood, id="area_flood"),
        dl.PolylineDecorator(children=polygon_fire, patterns=patterns_fire, id="area_fire")
    ], style={'width': '100%', 'height': '72vh', 'margin': "auto", "display": "block"}, id="map"),
    dbc.Row(
        [
            dbc.Col(dbc.Button("Advice Section", color="success",
                               id="advice", n_clicks=0, href='https://webbot.me/ec2dc16d38cab7c79cdf1dd44c1607e3b303aeca68e53575120eec15963b1f0f', target="_blank"), className="me-1", width={"size": 2, "offset": 5}),
            dbc.Col(dbc.Button("SOS", color="danger", id="sos",
                               n_clicks=0, href='https://imagizer.imageshack.com/img922/7628/QmeElj.gif', target="_blank"), className="me-1", width={"size": 2, "offset": 14})
        ],
        align="center", style={"margin-bottom": "0px", "margin-top": "10px","margin-bottom": "-15px", "margin-right": "auto"},
    ),
])

@ app.callback(Output("description", "children"), [Input("schools", "click_feature")])
def school_click(feature):
    return (html.P(["{}".format(feature['properties']['name']), html.Br(), html.B("Resistance of shelters : "), html.Br(), html.B("Shelter Floods : "), "{}".format(feature['properties']['Shelter_floods']),
            html.Br(), html.B("Shelter Fire : "), "{}".format(feature['properties']['Shelter_fire']), html.Br(), html.B("Shelter quake : "), "{}".format(feature['properties']['Shelter_quake']), html.Br(),
            html.B("Shelter tsunami : "), "{}".format(feature['properties']['Shelter_tsunami']), html.Br(), html.B("Shelter volcano : "), "{}".format(feature['properties']['Shelter_volcano'])
                    ]))

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)
