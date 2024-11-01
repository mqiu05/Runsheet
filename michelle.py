from dash import Dash, html, dcc, Output, Input, State, dash_table, no_update
from dash.exceptions import PreventUpdate
import pandas as pd

app = Dash(__name__)

# Define common styles
button_style = {
    'outline': 'none', 'border': 'none', 'background-color': 'white', 'color': 'black',
    'padding': '10px 20px', 'font-size': '25px', 'cursor': 'pointer',
    'z-index': 2, 'text-decoration': 'underline'
}
label_style = {'grid-column': '1 / 3', 'font-weight': 'bold'}
input_style = {'width': '100%'}

app.layout = html.Div(children=[
    html.Img(src='/assets/logo.png', alt='Revealed Image'),  # FORMULA PIC

    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Input Data', children=[
            html.Div('Session Number', style=label_style),
            dcc.Input(placeholder='Session Number', type='number', value='', id='session', style=input_style),

            # General Section
            html.Div(children=[
                html.Button('General', id='general-button', n_clicks=0, style=button_style),
                html.Div(id='general-inputs', children=[
                    html.Div('Date', style=label_style),
                    dcc.DatePickerSingle(id='date-picker'),
                    html.Div('Venue', style=label_style),
                    dcc.Dropdown(['Purdue GP', 'Frankfort HS'], placeholder='Venue', id='venue'),
                    html.Div('Event', style=label_style),
                    dcc.Dropdown(['Acceleration', 'Autocross', 'Brake', 'Endurance', 'Skid Pad'], placeholder='Event', id='event'),
                    html.Div('Driver', style=label_style),
                    dcc.Dropdown(['Iancarlo', 'Matt', 'Simon', 'Troy'], placeholder='Driver', id='driver'),
                    html.Div('Weight', style=label_style),
                    dcc.Input(placeholder='Weight', type='number', value='', id='weight', style=input_style),
                    html.Div('Driver Notes', style=label_style),
                    dcc.Textarea(placeholder='Driver Notes', value='', style=input_style, id='driver-notes'),
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Tires Section
            html.Div(children=[
                html.Button('Tires', id='tires-button', n_clicks=0, style=button_style),
                html.Div(id='tires-inputs', children=[
                    html.Img(
                        src='/assets/car.png', alt='Revealed Image',
                        style={
                            'position': 'relative', 'margin': '0 auto', 'display': 'block',
                            'max-width': '70%', 'height': 'relative', 'margin-top': '100px'
                        }
                    ),
                    html.Div(
                        children=[
                            # Top-Left Box (Front Left Tire)
                            html.Div(
                                children=[
                                    html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-pressure-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-pressure-after'),
                                    html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                                    html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-oTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-mTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-iTemp-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-oTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-mTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fl-iTemp-after'),

                                ],
                                style={
                                    'position': 'absolute', 'margin-top': '40px', 'margin-left': '300px', 'left': '5%',
                                    'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                                    'width': '15%', 'border': '2px solid black', 'padding': '10px',
                                    'background-color': 'white'
                                }
                            ),
                            # Top-Right Box (Front Right Tire)
                            html.Div(
                                children=[
                                    html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-pressure-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-pressure-after'),
                                    html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                                    html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-oTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-mTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-iTemp-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-oTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-mTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='fr-iTemp-after'),

                                ],
                                style={
                                    'position': 'absolute', 'margin-top': '40px', 'margin-right': '300px',
                                    'right': '5%',
                                    'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                                    'width': '15%', 'border': '2px solid black', 'padding': '10px',
                                    'background-color': 'white'
                                }
                            ),
                            # Bottom-Left Box (Rear Left Tire)
                            html.Div(
                                children=[
                                    html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-pressure-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-pressure-after'),
                                    html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                                    html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-oTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-mTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-iTemp-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-oTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-mTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rl-iTemp-after'),

                                ],
                                style={
                                    'position': 'absolute', 'bottom': '25%', 'left': '5%', 'margin-left': '300px',
                                    'display': 'grid', 'grid-template-columns': 'repeat(4, 1fr)', 'gap': '10px',
                                    'width': '15%', 'border': '2px solid black', 'padding': '10px',
                                    'background-color': 'white'
                                }
                            ),
                            # Bottom-Right Box (Rear Right Tire)
                            html.Div(
                                children=[
                                    html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-pressure-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-pressure-after'),
                                    html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
                                    html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),
                                    html.Div('Before', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-oTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-mTemp-before'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-iTemp-before'),
                                    html.Div('After', style={'grid-column': '1 / 2'}),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-oTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-mTemp-after'),
                                    dcc.Input(type='number', placeholder='', style={'width': '100%'},
                                              id='rr-iTemp-after'),

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

                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Aero Section
            html.Div(children=[
                html.Button('Aero', id='aero-button', n_clicks=0, style=button_style),
                html.Div(id='aero-inputs', children=[
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Chassis Section
            html.Div(children=[
                html.Button('Chassis', id='chassis-button', n_clicks=0, style=button_style),
                html.Div(id='chassis-inputs', children=[
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Powertrain Section
            html.Div(children=[
                html.Button('Powertrain', id='powertrain-button', n_clicks=0, style=button_style),
                html.Div(id='powertrain-inputs', children=[
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Suspension Section
            html.Div(children=[
                html.Button('Suspension', id='suspension-button', n_clicks=0, style=button_style),
                html.Div(id='suspension-inputs', children=[
                    html.Div('Tire Compound', style=label_style),
                    dcc.Input(placeholder='Tire Compound', value='', style={'width': '10%', 'height': '20px'},
                                 id='tire-compound'),
                    html.Div('Front Spring Rate', style=label_style),
                    dcc.Dropdown(['300', '350', '400', '450'], placeholder='Front Spring Rate', id='front-spring-rate'),
                    html.Div('Rear Spring Rate', style=label_style),
                    dcc.Dropdown(['300', '350', '400', '450'], placeholder='Rear Spring Rate', id='rear-spring-rate'),
                    html.Div('Left ARB', style=label_style),
                    dcc.Dropdown(['1', '2', '3', '4', '5', '6'], placeholder='Left ARB', id='left-arb'),
                    html.Div('Right ARB', style=label_style),
                    dcc.Dropdown(['1', '2', '3', '4', '5', '6'], placeholder='Right ARB', id='right-arb'),
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Notes Section
            html.Div(children=[
                html.Button('Notes', id='notes-button', n_clicks=0, style=button_style),
                html.Div(id='notes-inputs', children=[
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
                               'font-size': '20px', 'padding': '10px'}
                        ),

            # Export Button
            html.Button('Export', id='export-button',
                        style={'margin-top': '20px', 'margin-left': '20px', 'width': '8%', 'height': '40px',
                               'font-size': '20px', 'padding': '10px'}
                        ),
        ]),

        dcc.Tab(label='View Data', children=[
            # DataTable
            dash_table.DataTable(id='editable-table', columns=[], data=[], editable=True,  # Enable editing
                                style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}
            ),

            # Confirmation and Error Dialogs
            dcc.ConfirmDialog(id='export-confirm', message='Data exported to DataFrame.'),
            dcc.ConfirmDialog(id='session-error', message='Session value cannot be empty.')
        ]),
    ]),

    # Hidden Div or Store to hold the session data (optional, if needed)
    # dcc.Store(id='session-data-store', data=[])
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

# Callback to toggle Aero section visibility
@app.callback(
    Output('aero-inputs', 'style'),
    Input('aero-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_aero_section(n_clicks):
    return {'display': 'block'} if n_clicks % 2 == 1 else {'display': 'none'}

# Callback to toggle Chassis section visibility
@app.callback(
    Output('chassis-inputs', 'style'),
    Input('chassis-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_chassis_section(n_clicks):
    return {'display': 'block'} if n_clicks % 2 == 1 else {'display': 'none'}

# Callback to toggle Powertrain section visibility
@app.callback(
    Output('powertrain-inputs', 'style'),
    Input('powertrain-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_powertrain_section(n_clicks):
    return {'display': 'block'} if n_clicks % 2 == 1 else {'display': 'none'}

# Callback to toggle Suspension section visibility
@app.callback(
    Output('suspension-inputs', 'style'),
    Input('suspension-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_suspension_section(n_clicks):
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
    [
        Output('session', 'value'),
        Output('date-picker', 'date'),
        Output('venue', 'value'),
        Output('event', 'value'),
        Output('driver', 'value'),
        Output('weight', 'value'),
        Output('driver-notes', 'value'),
        Output('fl-pressure-before', 'value'),
        Output('fl-pressure-after', 'value'),
        Output('fl-oTemp-before', 'value'),
        Output('fl-mTemp-before', 'value'),
        Output('fl-iTemp-before', 'value'),
        Output('fl-oTemp-after', 'value'),
        Output('fl-mTemp-after', 'value'),
        Output('fl-iTemp-after', 'value'),
        Output('fr-pressure-before', 'value'),
        Output('fr-pressure-after', 'value'),
        Output('fr-oTemp-before', 'value'),
        Output('fr-mTemp-before', 'value'),
        Output('fr-iTemp-before', 'value'),
        Output('fr-oTemp-after', 'value'),
        Output('fr-mTemp-after', 'value'),
        Output('fr-iTemp-after', 'value'),
        Output('rl-pressure-before', 'value'),
        Output('rl-pressure-after', 'value'),
        Output('rl-oTemp-before', 'value'),
        Output('rl-mTemp-before', 'value'),
        Output('rl-iTemp-before', 'value'),
        Output('rl-oTemp-after', 'value'),
        Output('rl-mTemp-after', 'value'),
        Output('rl-iTemp-after', 'value'),
        Output('rr-pressure-before', 'value'),
        Output('rr-pressure-after', 'value'),
        Output('rr-oTemp-before', 'value'),
        Output('rr-mTemp-before', 'value'),
        Output('rr-iTemp-before', 'value'),
        Output('rr-oTemp-after', 'value'),
        Output('rr-mTemp-after', 'value'),
        Output('rr-iTemp-after', 'value'),
        Output('tire-compound', 'value'),
        Output('front-spring-rate', 'value'),
        Output('rear-spring-rate', 'value'),
        Output('left-arb', 'value'),
        Output('right-arb', 'value'),
        Output('faults', 'value'),
        Output('improvements', 'value'),
        Output('misc-notes', 'value')
    ],
    Input('clear-button', 'n_clicks'),
    prevent_initial_call=True
)
def clear_inputs(n_clicks):
    return ('', None, '', '', '', '',  # General
            '', '', '', '', '', '', '', '', '',  # FL Tire
            '', '', '', '', '', '', '', '', '',  # FR Tire
            '', '', '', '', '', '', '', '', '',  # RL Tire
            '', '', '', '', '', '', '', '', '',  # RR Tire
            '', '', '', '', '')  # Notes


# Callback for exporting data to DataFrame and displaying it in an editable table
@app.callback(
    [
        Output('editable-table', 'columns'),
        Output('editable-table', 'data'),
        Output('export-confirm', 'displayed'),
        Output('session-error', 'displayed')
    ],
    Input('export-button', 'n_clicks'),
    [
        State('session', 'value'),
        State('date-picker', 'date'),
        State('venue', 'value'),
        State('event', 'value'),
        State('driver', 'value'),
        State('weight', 'value'),
        State('driver-notes', 'value'),
        State('fl-pressure-before', 'value'),
        State('fl-pressure-after', 'value'),
        State('fl-oTemp-before', 'value'),
        State('fl-mTemp-before', 'value'),
        State('fl-iTemp-before', 'value'),
        State('fl-oTemp-after', 'value'),
        State('fl-mTemp-after', 'value'),
        State('fl-iTemp-after', 'value'),
        State('fr-pressure-before', 'value'),
        State('fr-pressure-after', 'value'),
        State('fr-oTemp-before', 'value'),
        State('fr-mTemp-before', 'value'),
        State('fr-iTemp-before', 'value'),
        State('fr-oTemp-after', 'value'),
        State('fr-mTemp-after', 'value'),
        State('fr-iTemp-after', 'value'),
        State('rl-pressure-before', 'value'),
        State('rl-pressure-after', 'value'),
        State('rl-oTemp-before', 'value'),
        State('rl-mTemp-before', 'value'),
        State('rl-iTemp-before', 'value'),
        State('rl-oTemp-after', 'value'),
        State('rl-mTemp-after', 'value'),
        State('rl-iTemp-after', 'value'),
        State('rr-pressure-before', 'value'),
        State('rr-pressure-after', 'value'),
        State('rr-oTemp-before', 'value'),
        State('rr-mTemp-before', 'value'),
        State('rr-iTemp-before', 'value'),
        State('rr-oTemp-after', 'value'),
        State('rr-mTemp-after', 'value'),
        State('rr-iTemp-after', 'value'),
        State('tire-compound', 'value'),
        State('front-spring-rate', 'value'),
        State('rear-spring-rate', 'value'),
        State('left-arb', 'value'),
        State('right-arb', 'value'),
        State('faults', 'value'),
        State('improvements', 'value'),
        State('misc-notes', 'value'),
        State('editable-table', 'columns'),
        State('editable-table', 'data')
    ],
    prevent_initial_call=True
)
def export_data(n_clicks, session, date, venue, event, driver, weight, driver_notes,
                fl_pressure_before, fl_pressure_after, fl_oTemp_before, fl_mTemp_before, fl_iTemp_before,
                fl_oTemp_after, fl_mTemp_after, fl_iTemp_after,
                fr_pressure_before, fr_pressure_after, fr_oTemp_before, fr_mTemp_before, fr_iTemp_before,
                fr_oTemp_after, fr_mTemp_after, fr_iTemp_after,
                rl_pressure_before, rl_pressure_after, rl_oTemp_before, rl_mTemp_before, rl_iTemp_before,
                rl_oTemp_after, rl_mTemp_after, rl_iTemp_after,
                rr_pressure_before, rr_pressure_after, rr_oTemp_before, rr_mTemp_before, rr_iTemp_before,
                rr_oTemp_after, rr_mTemp_after, rr_iTemp_after,
                tire_compound, front_spring_rate, rear_spring_rate, left_arb, right_arb,
                faults, improvements, misc_notes,
                existing_columns, existing_data):
    if not n_clicks:
        raise PreventUpdate

    # Check for a valid session value
    if not session:
        return no_update, no_update, False, True  # Show session error dialog

    # Collect data from inputs
    data = {
        'Session': session,
        'Date': date,
        'Venue': venue,
        'Event': event,
        'Driver': driver,
        'Weight': weight,
        'Driver Notes': driver_notes,
        # FL Tire Data
        'FL Pressure Before': fl_pressure_before,
        'FL Pressure After': fl_pressure_after,
        'FL O Temp Before': fl_oTemp_before,
        'FL M Temp Before': fl_mTemp_before,
        'FL I Temp Before': fl_iTemp_before,
        'FL O Temp After': fl_oTemp_after,
        'FL M Temp After': fl_mTemp_after,
        'FL I Temp After': fl_iTemp_after,
        # FR Tire Data
        'FR Pressure Before': fr_pressure_before,
        'FR Pressure After': fr_pressure_after,
        'FR O Temp Before': fr_oTemp_before,
        'FR M Temp Before': fr_mTemp_before,
        'FR I Temp Before': fr_iTemp_before,
        'FR O Temp After': fr_oTemp_after,
        'FR M Temp After': fr_mTemp_after,
        'FR I Temp After': fr_iTemp_after,
        # RL Tire Data
        'RL Pressure Before': rl_pressure_before,
        'RL Pressure After': rl_pressure_after,
        'RL O Temp Before': rl_oTemp_before,
        'RL M Temp Before': rl_mTemp_before,
        'RL I Temp Before': rl_iTemp_before,
        'RL O Temp After': rl_oTemp_after,
        'RL M Temp After': rl_mTemp_after,
        'RL I Temp After': rl_iTemp_after,
        # RR Tire Data
        'RR Pressure Before': rr_pressure_before,
        'RR Pressure After': rr_pressure_after,
        'RR O Temp Before': rr_oTemp_before,
        'RR M Temp Before': rr_mTemp_before,
        'RR I Temp Before': rr_iTemp_before,
        'RR O Temp After': rr_oTemp_after,
        'RR M Temp After': rr_mTemp_after,
        'RR I Temp After': rr_iTemp_after,
        # Suspension
        'Tire Compound': tire_compound,
        'Front Spring Rate': front_spring_rate,
        'Rear Spring Rate': rear_spring_rate,
        'Left ARB': left_arb,
        'Right ARB': right_arb,
        # Notes
        'Faults': faults,
        'Improvements': improvements,
        'Misc Notes': misc_notes
    }

    # Append new data to the DataFrame
    if existing_data is None or existing_data == []:
        session_data = pd.DataFrame([data])
    else:
        session_data = pd.DataFrame(existing_data)
        session_data = session_data.append(data, ignore_index=True)

    # Prepare columns if not set
    if not existing_columns:
        columns = [{'name': col, 'id': col, 'editable': True} for col in session_data.columns]
    else:
        columns = existing_columns

    data_records = session_data.to_dict('records')

    return columns, data_records, True, False  # Update table and confirm export


if __name__ == '__main__':
    app.run_server(debug=True)
