from dash import Dash, html, dcc, Output, Input

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(children=[
    # General button and content
    html.Div(children=[
        html.Img(
                src='/assets/logo.png', alt='Revealed Image',
            ),
        html.Div('Session Number', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
        dcc.Input(placeholder='Session Number', type='number', value='', id='session', style={'width': '100%'}),

        html.Button(
            'General',
            id='general-button',
            n_clicks=0,
            style={
                'outline': 'none', 'border': 'none', 'background-color': 'white',
                'color': 'black', 'padding': '10px 20px', 'font-size': '25px', 'cursor': 'pointer',
                'z-index': 2, 'text-decoration': 'underline'
            }
        ),
        html.Div(id='general-section', style={'display': 'none'}),  # Div that will be toggled

        # Input elements for General section, initially hidden
        html.Div(id='session-inputs', children=[
            html.Div('Date', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.DatePickerSingle(id='date-picker'),
            html.Div('Venue', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Dropdown(['Purdue GP', 'Venue 2', 'Venue 3'], placeholder='Venue', id='venue'),
            html.Div('Event', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Dropdown(['Skid', 'Brake', 'Autox'], placeholder='Event', id='event'),
            html.Div('Driver', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Dropdown(['Iancarlo', 'Simon', 'Troy'], placeholder='Driver', id='driver'),
            html.Div('Weight', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Input(placeholder='Weight', type='number', value='', id='weight', style={'width': '100%'}),
        ], style={'display': 'none'}),  # Initially hidden
    ], style={'margin-bottom': '20px'}),  # Ensure vertical space between sections

    # Tires button and content
    html.Div(children=[
        html.Button(
            'Tires',
            id='tire-button',
            n_clicks=0,
            style={
                'outline': 'none', 'border': 'none', 'background-color': 'white',
                'color': 'black', 'padding': '10px 20px', 'font-size': '25px', 'cursor': 'pointer',
                'z-index': 2, 'text-decoration': 'underline'
            }
        ),
        html.Div(id='output-tires', style={'position': 'relative'}),
    ], style={'margin-bottom': '20px'}),  # Ensure vertical space

    # Notes button and content
    html.Div(children=[
        html.Button('Notes', id='notes-button', n_clicks=0,
                    style={'outline': 'none', 'border': 'none', 'background-color': 'white',
                           'color': 'black', 'padding': '10px 20px', 'font-size': '25px', 'cursor': 'pointer',
                           'z-index': 2,
                           'text-decoration': 'underline'}
                    ),
        html.Div(id='notes-inputs', children=[
            html.Div('Driver Notes', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Textarea(placeholder='Driver Notes', value='', style={'width': '100%'}, id='driver-notes'),
            html.Div('Faults', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Textarea(placeholder='Faults', value='', style={'width': '100%'}, id='faults'),
            html.Div('Improvements', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Textarea(placeholder='Improvements', value='', style={'width': '100%'}, id='improvements'),
            html.Div('Misc.', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            dcc.Textarea(placeholder='Misc. Notes', value='', style={'width': '100%'}, id='misc-notes'),
        ], style={'display': 'none'}),
    ], style={'margin-bottom': '20px'}),  # Ensure vertical space

    # Clear button
    html.Button('Clear', id='clear-button', style={'margin-top': '20px', 'margin-left': '20px', 'width':'8%',  'height': '40px','font-size': '20px','padding': '10px',}),
])


@app.callback(
    Output('general-section', 'children'),
    Output('session-inputs', 'style'),
    Input('general-button', 'n_clicks')
)
def reveal_general(n_clicks):
    if n_clicks % 2 == 1:
        return 'General Section Revealed', {'display': 'block'}
    else:
        return '', {'display': 'none'}


@app.callback(
    Output('output-tires', 'children'),
    Input('tire-button', 'n_clicks')
)
def reveal_tire(n_clicks):
    if n_clicks % 2 == 1:
        return html.Div([
            html.Img(
                src='/assets/car.png', alt='Revealed Image',
                style={
                    'position': 'relative',  # Keep within the flow
                    'margin': '0 auto', 'display': 'block',  # Center image horizontally
                    'max-width': '70%', 'height': 'relative', 'margin-top': '100px'  # Responsive width and height
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
                            'position': 'absolute', 'margin-top': '40px', 'margin-left': '300px', 'left': '5%',
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
                            'position': 'absolute', 'margin-top': '40px', 'margin-right': '300px', 'right': '5%',
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
                            'position': 'absolute', 'bottom': '25%', 'left': '5%', 'margin-left': '300px',
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
                            'position': 'absolute', 'bottom': '25%', 'right': '5%', 'margin-right': '300px',
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
                          dcc.Input(type='text', placeholder='', style={'width': '10%'}),
                          ],
                style={'position': 'relative', 'margin-left': '1050px'})
        ])


@app.callback(
    Output('notes-inputs', 'style'),
    Input('notes-button', 'n_clicks')
)
def reveal_notes(n_clicks):
    if n_clicks % 2 == 1:
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@app.callback(
    [Output('session', 'value'),
     Output('date-picker', 'date'),
     Output('venue', 'value'),
     Output('event', 'value'),
     Output('driver', 'value'),
     Output('weight', 'value'),
     Output('driver-notes', 'value'),
     Output('faults', 'value'),
     Output('improvements', 'value'),
     Output('misc-notes', 'value')],
     Input('clear-button', 'n_clicks')
)
def clear_inputs(n_clicks):
    if n_clicks:
        return '', None, '', '', '', '', '', '', '', ''


if __name__ == '__main__':
    app.run_server(debug=True)