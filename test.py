import plotly.graph_objects as go
import numpy as np

# Example satellite data for two satellites at different time snapshots
satellite_data = {
    "satellite_1": {
        "azimuth": [10, 60, 90, 120, 150],  # in degrees
        "elevation": [70, 60, 50, 40, 30],  # in degrees
        "time": ['10:00', '10:10', '10:20', '10:30', '10:40']
    },
    "satellite_2": {
        "azimuth": [200, 220, 240, 260, 280],
        "elevation": [80, 70, 60, 50, 40],
        "time": ['10:00', '10:10', '10:20', '10:30', '10:40']
    }
}


# Convert elevation degrees to polar coordinates (90 degrees - elevation)
def polar_elevation(elevation_deg):
    return 90 - np.array(elevation_deg)


# Create traces for each satellite
fig = go.Figure()

for satellite, data in satellite_data.items():
    fig.add_trace(go.Scatterpolar(
        r=polar_elevation(data["elevation"]),  # Radial coordinate (elevation)
        theta=data["azimuth"],  # Angular coordinate (azimuth)
        mode='lines+markers',  # Plot as lines with markers
        name=satellite,  # Satellite name
        text=data["time"],  # Time snapshots (shown on hover)
        hoverinfo="text",  # Display time on hover
    ))

fig.update_layout(
    polar=dict(
        angularaxis=dict(
            # Remove the 'title' property here
            showline=True,
            linewidth=2,
            linecolor="black",
            gridcolor="grey",
        ),
        radialaxis=dict(
            showline=True,
            linewidth=2,
            linecolor="black",
            gridcolor="grey",
        )
    ),
    title="Skyplot of Satellite Paths"  # Add the title here
)

# Show the plot
fig.show()
