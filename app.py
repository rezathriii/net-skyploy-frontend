import dash
from dash import html
import dash_bootstrap_components as dbc
from assets.styles import (
    main_container_style,
    header_style,
    menu_style,
    section_style,
    slider_style,
    carousel_item_style,
    footer_style,
    carousel_items
)

app = dash.Dash(__name__, title="NET-SKYPLOT", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    # Header and Navbar
    html.Div(style=header_style, children=[
        dbc.NavbarSimple(
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
    ]),

    html.Div(style=main_container_style, children=[
        html.Div(style={"paddingTop": "80px"}),

        html.Div(id="home", style=slider_style, children=[
            dbc.Carousel(
                items=[
                    {
                        "key": item["key"],
                        "src": item["src"],
                        "header": item["header"],
                        "caption": item["caption"],
                        "img_style": carousel_item_style
                    }
                    for item in carousel_items
                ],
                controls=True,
                indicators=True,
                interval=4000,
                ride="carousel",
                style={"height": "100%"}
            )
        ]),

        # Project Introduction
        html.Div(id="introduction", style=section_style, className="mt-5", children=[
            html.H2("Project Introduction", style={"fontSize": "2em", "marginBottom": "20px"}),
            html.P(
                "NET-SKYPLOT is a cutting-edge tool designed for GNSS survey planning. By integrating digital elevation models (DTM or DSM), "
                "it enables detailed analysis of satellite visibility, skyplots, and satellite configurations, improving the precision of your surveys."
            ),
            dbc.Button("Start Planning", href="#", color="primary", size="lg", className="mt-4",
                       style={"fontWeight": "bold"})  # Start Planning Button
        ]),

        # Features
        html.Div(id="features", style=section_style, className="mt-5", children=[
            html.H2("Features", style={"fontSize": "2em", "marginBottom": "20px"}),
            html.Ul(children=[
                html.Li("Satellite Visibility Analysis", style={"marginBottom": "10px"}),
                html.Li("Digital Elevation Model Integration", style={"marginBottom": "10px"}),
                html.Li("Graphical Visualization of DOP Values", style={"marginBottom": "10px"}),
                html.Li("Open Source with custom integration options", style={"marginBottom": "10px"}),
            ], style={"listStyleType": "none", "paddingLeft": "0"})
        ]),

        # Team Members
        html.Div(id="team", style=section_style, className="mt-5", children=[
            html.H2("Team Members", style={"fontSize": "2em", "marginBottom": "20px"}),
            html.Ul(children=[
                html.Li("Saeed Amiri - Team Member"),
                html.Li("Mohammadreza Taheri - Team Member"),
                html.Li("Lena Kazemahvazi - Team Member"),
                html.Li("Elahe Fallahi - Team Member"),
                html.Li("Arezou Shadkam - Team Member"),
                html.Li("Keyvan Abbas Majidi - Team Member")
            ], style={"listStyleType": "none", "paddingLeft": "0"})
        ]),

        # Open Source Information
        html.Div(id="opensource", style=section_style, className="mt-5", children=[
            html.H2("Open Source", style={"fontSize": "2em", "marginBottom": "20px"}),
            html.P("This project is open-source and can be found on GitHub:"),
            html.A("Visit GitHub Repository", href="https://github.com/rezathriii/net-skyploy-frontend",
                   target="_blank",
                   style={"color": "#0056b3", "fontWeight": "bold"})
        ]),

        # Footer
        html.Footer(style=footer_style, children=[
            html.P("© 2024 NET-SKYPLOT Project", style={"marginBottom": "5px"}),
            html.P("Contact us at: info@netskyplot.com")
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=80)
