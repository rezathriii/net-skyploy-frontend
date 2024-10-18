from dash import html, dcc
import dash_leaflet as dl
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


def create_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="#home", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("Introduction", href="#introduction", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("Features", href="#features", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("Team", href="#team", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("Open Source", href="#opensource", style={"color": "white"})),
        ],
        brand="NET-SKYPLOT",
        brand_href="#home",
        color="primary",
        dark=True,
        style={"paddingLeft": "40px", "paddingRight": "40px"}
    )


def generate_planning_page():
    return html.Div([
        create_navbar(),  # Include navbar
        html.H2("Select a Location on the Map", style={"textAlign": "center"}),
        dl.Map(id="map", center=[20, 0], zoom=2, style={'width': '100%', 'height': '500px'},
               children=[
                   dl.TileLayer(),
                   dl.Marker(position=[20, 0], id='marker')  # Initial marker position
               ]),
        html.Div(id="coordinates-output", style={"textAlign": "center", "marginTop": "20px"}),
        dcc.Input(id="latitude", type="text", placeholder="Latitude", readOnly=True, style={"margin": "10px"}),
        dcc.Input(id="longitude", type="text", placeholder="Longitude", readOnly=True, style={"margin": "10px"}),
        html.Button("Submit", id="submit-button", n_clicks=0, style={"marginTop": "10px"})
    ])


def register_callbacks(app):
    @app.callback(
        Output('marker', 'position'),
        Output('latitude', 'value'),
        Output('longitude', 'value'),
        Input('map', 'click_lat_lng')
    )
    def update_marker_position(click_lat_lng):
        if click_lat_lng is None:
            return [20, 0], "", ""  # Default position if no click
        else:
            lat, lng = click_lat_lng
            return [lat, lng], str(lat), str(lng)
