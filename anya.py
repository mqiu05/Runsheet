from dash import Dash, html, dcc, Output, Input

app = Dash(__name__)
#test
# Initial layout with the button and image container
app.layout = html.Div(children=[
    html.Div(id='output-image'),
    html.Button(
        'Tires',
        id='reveal-button',
        n_clicks=0,
        style={
            'outline': 'none', 'border': 'none', 'background-color': 'white',
            'color': 'black', 'padding': '10px 20px', 'font-size': '25px', 'cursor': 'pointer',
            'z-index': 2, 'text-decoration': 'underline'
        }
    ),
    html.Div(id='output-content', style={'position': 'relative'})  # Container for the image and grid
])


# Callback to update the output-content div with an image and grid on button click
@app.callback(
    Output('output-content', 'children'),
    Input('reveal-button', 'n_clicks')
)
def reveal_image(n_clicks):
    if n_clicks > 0:
        return html.Div([
            html.Img(
                src='/assets/car.png', alt='Revealed Image',
                style={
                    'position': 'relative',  # Keep within the flow
                    'margin': '0 auto', 'display': 'block',  # Center image horizontally
                    'max-width': '70%', 'height': 'relative', 'margin-top':'100px'  # Responsive width and height
                }
            ),
            # Add the four boxes to the corners of the screen
            html.Div(
                children=[
                    # Top-Left Box
                    html.Div(
                        children=[
                            html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'})
                        ],
                        style={
                            'position': 'absolute', 'margin-top': '40px','margin-left':'300px', 'left': '5%',
                            'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                            'width': '15%', 'border': '2px solid black', 'padding': '10px',
                            'background-color': 'white'
                        }
                    ),
                    # Top-Right Box
                    html.Div(
                        children=[
                            html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'})
                        ],
                        style={
                            'position': 'absolute', 'margin-top': '40px','margin-right':'300px', 'right': '5%',
                            'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                            'width': '15%', 'border': '2px solid black', 'padding': '10px',
                            'background-color': 'white'
                        }
                    ),
                    # Bottom-Left Box
                    html.Div(
                        children=[
                            html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'})
                        ],
                        style={
                              'position': 'absolute', 'bottom': '25%', 'left': '5%','margin-left':'300px',
                            'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                            'width': '15%', 'border': '2px solid black', 'padding': '10px',
                            'background-color': 'white'
                        }
                    ),
                    # Bottom-Right Box
                    html.Div(
                        children=[
                            html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='text', placeholder='', style={'width': '100%'})
                        ],
                        style={
                            'position': 'absolute', 'bottom': '25%', 'right': '5%','margin-right':'300px',
                            'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                            'width': '15%', 'border': '2px solid black', 'padding': '10px',
                            'background-color': 'white'
                        }
                    ),

                ],

                style={'position': 'relative', 'top': '-300px'}  # Relative positioning for the containing div
            ),
            html.Div(
                children=[html.Div('Tire Compound', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                          dcc.Input(type='text', placeholder='', style={'width': '100%'}),
                          ],
                style={'position': 'absolute', 'margin-top': '3000px}', 'margin-left': '1050px'})
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
