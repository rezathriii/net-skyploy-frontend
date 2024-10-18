import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
from src.templates.LandingPage import generate_landing_page
from src.templates.PlanningPage import generate_planning_page, register_callbacks

app = dash.Dash(__name__, title="NET-SKYPLOT", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(id='page-content', children=[generate_landing_page()])

# Register callbacks
register_callbacks(app)


@app.callback(
    Output('page-content', 'children'),
    Input('start-planning-button', 'n_clicks'),
)
def navigate_to_planning(n_clicks):
    if n_clicks:
        return generate_planning_page()  # Redirect to Planning Page
    return generate_landing_page()  # Return to Landing Page


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=80)
