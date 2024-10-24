from dash import Dash, html, dcc, Output, Input

app = Dash(__name__)

# Define common styles
button_style = {'outline': 'none', 'border': 'none', 'background-color': 'white', 'color': 'black',
                'padding': '10px 20px',
                'font-size': '25px', 'cursor': 'pointer', 'z-index': 2, 'text-decoration': 'underline'}
label_style = {'grid-column': '1 / 3', 'font-weight': 'bold'}
input_style = {'width': '100%'}

app.layout = html.Div(children=[
    html.Img(src='/assets/logo.png', alt='Revealed Image'),  # FORMULA PICCCC

    html.Div('Session Number', style=label_style),
    dcc.Input(placeholder='Session Number', type='number', value='', id='session', style=input_style),

    # General Section
    html.Div(children=[
        html.Button('General', id='general-button', n_clicks=0, style=button_style),
        html.Div(id='general-inputs', children=[
            html.Div('Date', style=label_style),
            dcc.DatePickerSingle(id='date-picker'),
            html.Div('Venue', style=label_style),
            dcc.Dropdown(['Purdue GP', 'Venue 2', 'Venue 3'], placeholder='Venue', id='venue'),
            html.Div('Event', style=label_style),
            dcc.Dropdown(['Skid', 'Brake', 'Autox'], placeholder='Event', id='event'),
            html.Div('Driver', style=label_style),
            dcc.Dropdown(['Iancarlo', 'Simon', 'Troy', 'Matt'], placeholder='Driver', id='driver'),
            html.Div('Weight', style=label_style),
            dcc.Input(placeholder='Weight', type='number', value='', id='weight', style=input_style),
        ], style={'display': 'none'}),
    ], style={'margin-bottom': '20px'}),

    # Tires Section
    html.Div(children=[
        html.Button('Tires', id='tires-button', n_clicks=0, style=button_style),
        html.Div(id='tires-inputs', children=[
            html.Img(
                src='/assets/car.png', alt='Revealed Image',
                style={
                    'position': 'relative',  # Keep within the flow
                    'margin': '0 auto', 'display': 'block',  # Center image horizontally
                    'max-width': '70%', 'height': 'relative', 'margin-top': '100px'  # Responsive width and height
                }
            ),
            html.Div(
                children=[
                    # Top-Left Box
                    html.Div(
                        children=[
                            html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-pressure-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-pressure-after'),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-oTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-mTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-iTemp-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-oTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-mTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-iTemp-after'),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fl-spring')
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
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-pressure-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-pressure-after'),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-oTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-mTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-iTemp-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-oTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-mTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-iTemp-after'),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='fr-spring')
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
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-pressure-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-pressure-after'),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-oTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-mTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-iTemp-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-oTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-mTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-iTemp-after'),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rl-spring')
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
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-pressure-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-pressure-after'),
                            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                            html.Div('Before', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-oTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-mTemp-before'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-iTemp-before'),
                            html.Div('After', style={'grid-column': '1 / 2'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-oTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-mTemp-after'),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-iTemp-after'),
                            html.Div('Spring Rate', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                            dcc.Input(type='number', placeholder='', style={'width': '100%'}, id='rr-spring')
                        ],
                        style={
                            'position': 'absolute', 'bottom': '25%', 'right': '5%', 'margin-right': '300px',
                            'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                            'width': '15%', 'border': '2px solid black', 'padding': '10px',
                            'background-color': 'white'
                        }
                    ),
                ], style={'position': 'relative', 'top': '-300px'}
            ),
            html.Div(
                children=[html.Div('Tire Compound', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                          dcc.Input(type='text', placeholder='', style={'width': '10%'}, id='tire-compound'),
                          ],
                style={'position': 'relative', 'margin-left': '1050px'})
        ], style={'display': 'none'}),
    ], style={'margin-bottom': '20px'}),

    # Notes Section
    html.Div(children=[
        html.Button('Notes', id='notes-button', n_clicks=0, style=button_style),
        html.Div(id='notes-inputs', children=[
            html.Div('Driver Notes', style=label_style),
            dcc.Textarea(placeholder='Driver Notes', value='', style=input_style, id='driver-notes'),
            html.Div('Faults', style=label_style),
            dcc.Textarea(placeholder='Faults', value='', style=input_style, id='faults'),
            html.Div('Improvements', style=label_style),
            dcc.Textarea(placeholder='Improvements', value='', style=input_style, id='improvements'),
            html.Div('Misc.', style=label_style),
            dcc.Textarea(placeholder='Misc. Notes', value='', style=input_style, id='misc-notes'),
        ], style={'display': 'none'}),
    ], style={'margin-bottom': '20px'}),

    # Clear Button
    html.Button('Clear', id='clear-button',
                style={'margin-top': '20px', 'margin-left': '20px', 'width': '8%', 'height': '40px',
                       'font-size': '20px', 'padding': '10px', }
                ),
])


# Callback to toggle General section visibility
@app.callback(
    Output('general-inputs', 'style'),
    Input('general-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_general_section(n_clicks):
    return {'display': 'block'} if n_clicks % 2 == 1 else {'display': 'none'}


# Callback to toggle Tires section visibility
@app.callback(
    Output('tires-inputs', 'style'),
    Input('tires-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_tires_section(n_clicks):
    return {'display': 'block'} if n_clicks % 2 == 1 else {'display': 'none'}


# Callback to toggle Notes section visibility
@app.callback(
    Output('notes-inputs', 'style'),
    Input('notes-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_notes_section(n_clicks):
    return {'display': 'block'} if n_clicks % 2 == 1 else {'display': 'none'}


# Callback to clear all inputs
@app.callback(
    [Output('session', 'value'),
     Output('date-picker', 'date'),
     Output('venue', 'value'),
     Output('event', 'value'),
     Output('driver', 'value'),
     Output('weight', 'value'),
     Output('fl-pressure-before', 'value'),
     Output('fl-pressure-after', 'value'),
     Output('fl-oTemp-before', 'value'),
     Output('fl-mTemp-before', 'value'),
     Output('fl-iTemp-before', 'value'),
     Output('fl-oTemp-after', 'value'),
     Output('fl-mTemp-after', 'value'),
     Output('fl-iTemp-after', 'value'),
     Output('fl-spring', 'value'),
     Output('fr-pressure-before', 'value'),
     Output('fr-pressure-after', 'value'),
     Output('fr-oTemp-before', 'value'),
     Output('fr-mTemp-before', 'value'),
     Output('fr-iTemp-before', 'value'),
     Output('fr-oTemp-after', 'value'),
     Output('fr-mTemp-after', 'value'),
     Output('fr-iTemp-after', 'value'),
     Output('fr-spring', 'value'),
     Output('rl-pressure-before', 'value'),
     Output('rl-pressure-after', 'value'),
     Output('rl-oTemp-before', 'value'),
     Output('rl-mTemp-before', 'value'),
     Output('rl-iTemp-before', 'value'),
     Output('rl-oTemp-after', 'value'),
     Output('rl-mTemp-after', 'value'),
     Output('rl-iTemp-after', 'value'),
     Output('rl-spring', 'value'),
     Output('rr-pressure-before', 'value'),
     Output('rr-pressure-after', 'value'),
     Output('rr-oTemp-before', 'value'),
     Output('rr-mTemp-before', 'value'),
     Output('rr-iTemp-before', 'value'),
     Output('rr-oTemp-after', 'value'),
     Output('rr-mTemp-after', 'value'),
     Output('rr-iTemp-after', 'value'),
     Output('rr-spring', 'value'),
     Output('tire-compound', 'value'),
     Output('driver-notes', 'value'),
     Output('faults', 'value'),
     Output('improvements', 'value'),
     Output('misc-notes', 'value')],
    Input('clear-button', 'n_clicks'),
    prevent_initial_call=True
)
def clear_inputs(n_clicks):
    return '', None, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''


if __name__ == '__main__':
    app.run_server(debug=True)
