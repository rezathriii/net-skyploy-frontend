import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

main_style = {
    "textAlign": "center",
    "margin": "0 auto",
    "padding": "20px",
    "maxWidth": "1200px",
    "fontFamily": "Arial, sans-serif"
}

header_style = {
    "backgroundColor": "#007BFF",
    "color": "white",
    "padding": "20px",
    "fontSize": "2.5em",
    "fontWeight": "bold"
}

section_style = {
    "padding": "40px 0",
    "fontSize": "1.2em"
}

slider_style = {
    "width": "80%",
    "margin": "0 auto"
}

footer_style = {
    "backgroundColor": "#343A40",
    "color": "white",
    "padding": "20px",
    "marginTop": "40px"
}

carousel_items = [
    {"key": "1", "src": "/assets/images/slider-1.png", "header": "Satellite Analysis",
     "caption": "Analyze satellite visibility."},
    {"key": "2", "src": "/assets/images/slider-2.png", "header": "Skyplot Visualization",
     "caption": "Graphical Skyplot."},
    {"key": "3", "src": "/assets/images/slider-3.png", "header": "DOP Values",
     "caption": "View detailed DOP value graphs."}
]

# Layout of the landing page
app.layout = html.Div(style=main_style, children=[
    # Header
    html.Div("NET-SKYPLOT", style=header_style),

    # Image Carousel (replacing the slider)
    html.Div(style=slider_style, children=[
        dbc.Carousel(
            items=[
                {"key": item["key"], "src": item["src"], "header": item["header"], "caption": item["caption"]}
                for item in carousel_items
            ],
            controls=True,
            indicators=True,
            interval=3000,
            ride="carousel",
        )
    ]),

    # Project Introduction
    html.Div(style=section_style, children=[
        html.H2("Project Introduction"),
        html.P(
            "NET-SKYPLOT is a tool designed for GNSS survey planning. By incorporating digital elevation models (DTM or DSM), "
            "it offers an advanced analysis of satellite visibility, skyplots, and satellite configurations, which enhances accuracy in planning."
        )
    ]),

    # Features
    html.Div(style=section_style, children=[
        html.H2("Features"),
        html.Ul(children=[
            html.Li("Satellite Visibility Analysis"),
            html.Li("Digital Elevation Model Integration"),
            html.Li("Graphical Visualization of DOP Values"),
            html.Li("Open Source with custom integration options"),
        ])
    ]),

    # Team Members
    html.Div(style=section_style, children=[
        html.H2("Team Members"),
        html.P("Saeed Amiri - Team Member"),
        html.P("Mohammadreza Taheri - Team Member"),
        html.P("Lena Kazemahvazi - Team Member"),
        html.P("Elahe Fallahi - Team Member"),
        html.P("Arezou Shadkam - Team Member"),
        html.P("Keyvan Abbas Majidi - Team Member")
    ]),

    # Open Source Information
    html.Div(style=section_style, children=[
        html.H2("Open Source"),
        html.P("This project is open-source and can be found on GitHub:"),
        html.A("Visit GitHub Repository", href="https://github.com/rezathriii/net-skyploy-frontend", target="_blank")
    ]),

    # Footer
    html.Footer(style=footer_style, children=[
        html.P("© 2024 NET-SKYPLOT Project"),
        html.P("Contact us at: info@netskyplot.com")
    ])
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=80, debug=True)
