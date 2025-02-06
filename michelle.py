from dash import Dash, html, dcc, Output, Input, State, dash_table, no_update
from dash.exceptions import PreventUpdate
import pandas as pd
import os

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
                    # Add Aero inputs if needed here.
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Chassis Section
            html.Div(children=[
                html.Button('Chassis', id='chassis-button', n_clicks=0, style=button_style),
                html.Div(id='chassis-inputs', children=[
                    # Add Chassis inputs if needed here.
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Powertrain Section
            html.Div(children=[
                html.Button('Powertrain', id='powertrain-button', n_clicks=0, style=button_style),
                html.Div(id='powertrain-inputs', children=[
                    # Add Powertrain inputs if needed here.
                ], style={'display': 'none'}),
            ], style={'margin-bottom': '20px'}),

            # Suspension Section
            html.Div(children=[
                html.Button('Suspension', id='suspension-button', n_clicks=0, style=button_style),
                html.Div(id='suspension-inputs', children=[
                    html.Div('Tire Compound', style=label_style),
                    dcc.Input(placeholder='Tire Compound', value='', style={'width': '10%', 'height': '20px'},
                              id='tire-compound'),
                    html.Div('Tire Set', style=label_style),
                    dcc.Input(placeholder='Tire Set', value='', style={'width': '10%', 'height': '20px'},
                              id='tire-set'),
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

            # Save Button
            html.Button('Save', id='save-button',
                        style={'margin-top': '20px', 'margin-left': '20px', 'width': '8%', 'height': '40px',
                               'font-size': '20px', 'padding': '10px'}
                        ),
        ]),

        dcc.Tab(label='View Data', children=[

            html.H1('General'),
            dash_table.DataTable(id='general-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.H1('Tire'),
            dash_table.DataTable(id='fl-tire-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),
            dash_table.DataTable(id='fr-tire-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),
            dash_table.DataTable(id='rl-tire-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),
            dash_table.DataTable(id='rr-tire-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.H1('Aero'),
            dash_table.DataTable(id='aero-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.H1('Chassis'),
            dash_table.DataTable(id='chassis-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.H1('Powertrain'),
            dash_table.DataTable(id='powertrain-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.H1('Suspension'),
            dash_table.DataTable(id='suspension-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.H1('Notes'),
            dash_table.DataTable(id='notes-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}, style_cell={'textAlign': 'left'}),

            html.Button('Export', id='export-button',
                        style={'margin-top': '20px', 'margin-left': '20px', 'width': '8%', 'height': '40px',
                               'font-size': '20px', 'padding': '10px'}
                        ),
            dcc.Download(id='download-button'),

            # Confirmation and Error Dialogs
            dcc.ConfirmDialog(id='save-confirm', message='Data saved to DataFrame.'),
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
        Output('tire-set', 'value'),
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
            '', '', '', '', '', '')  # Notes

# Callback for saving data to DataFrame and displaying it in an editable table
@app.callback(
    [
        Output('general-table', 'columns'),
        Output('general-table', 'data'),
        Output('fl-tire-table', 'columns'),
        Output('fl-tire-table', 'data'),
        Output('fr-tire-table', 'columns'),
        Output('fr-tire-table', 'data'),
        Output('rl-tire-table', 'columns'),
        Output('rl-tire-table', 'data'),
        Output('rr-tire-table', 'columns'),
        Output('rr-tire-table', 'data'),
        Output('aero-table', 'columns'),
        Output('aero-table', 'data'),
        Output('chassis-table', 'columns'),
        Output('chassis-table', 'data'),
        Output('powertrain-table', 'columns'),
        Output('powertrain-table', 'data'),
        Output('suspension-table', 'columns'),
        Output('suspension-table', 'data'),
        Output('notes-table', 'columns'),
        Output('notes-table', 'data'),
        Output('save-confirm', 'displayed'),
        Output('session-error', 'displayed')
    ],
    Input('save-button', 'n_clicks'),
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
        State('tire-set', 'value'),
        State('front-spring-rate', 'value'),
        State('rear-spring-rate', 'value'),
        State('left-arb', 'value'),
        State('right-arb', 'value'),
        State('faults', 'value'),
        State('improvements', 'value'),
        State('misc-notes', 'value'),
        State('general-table', 'columns'),
        State('general-table', 'data'),
        State('fl-tire-table', 'columns'),
        State('fl-tire-table', 'data'),
        State('fr-tire-table', 'columns'),
        State('fr-tire-table', 'data'),
        State('rl-tire-table', 'columns'),
        State('rl-tire-table', 'data'),
        State('rr-tire-table', 'columns'),
        State('rr-tire-table', 'data'),
        State('aero-table', 'columns'),
        State('aero-table', 'data'),
        State('chassis-table', 'columns'),
        State('chassis-table', 'data'),
        State('powertrain-table', 'columns'),
        State('powertrain-table', 'data'),
        State('suspension-table', 'columns'),
        State('suspension-table', 'data'),
        State('notes-table', 'columns'),
        State('notes-table', 'data')
    ],
    prevent_initial_call=True
)
def save_data(n_clicks, session, date, venue, event, driver, weight, driver_notes,
              fl_pressure_before, fl_pressure_after, fl_oTemp_before, fl_mTemp_before, fl_iTemp_before,
              fl_oTemp_after, fl_mTemp_after, fl_iTemp_after,
              fr_pressure_before, fr_pressure_after, fr_oTemp_before, fr_mTemp_before, fr_iTemp_before,
              fr_oTemp_after, fr_mTemp_after, fr_iTemp_after,
              rl_pressure_before, rl_pressure_after, rl_oTemp_before, rl_mTemp_before, rl_iTemp_before,
              rl_oTemp_after, rl_mTemp_after, rl_iTemp_after,
              rr_pressure_before, rr_pressure_after, rr_oTemp_before, rr_mTemp_before, rr_iTemp_before,
              rr_oTemp_after, rr_mTemp_after, rr_iTemp_after,
              tire_compound, tire_set, front_spring_rate, rear_spring_rate, left_arb, right_arb,
              faults, improvements, misc_notes,
              general_columns, general_data,
              fl_tire_columns, fl_tire_data,
              fr_tire_columns, fr_tire_data,
              rl_tire_columns, rl_tire_data,
              rr_tire_columns, rr_tire_data,
              aero_columns, aero_data,
              chassis_columns, chassis_data,
              powertrain_columns, powertrain_data,
              suspension_columns, suspension_data,
              notes_columns, notes_data):
    if not n_clicks:
        raise PreventUpdate

    # Check for a valid session value
    if not session:
        # Show session error dialog
        return (no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update,
                no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update,
                False, True)

    # General Data
    general_data_new = {
        'Session': session,
        'Date': date,
        'Venue': venue,
        'Event': event,
        'Driver': driver,
        'Weight': weight,
        'Driver Notes': driver_notes
    }
    if general_data is None or general_data == []:
        general_df = pd.DataFrame([general_data_new])
    else:
        general_df = pd.DataFrame(general_data)
        general_df = pd.concat([general_df, pd.DataFrame([general_data_new])], ignore_index=True)
    general_columns = [{'name': col, 'id': col, 'editable': True} for col in general_df.columns]
    general_data_records = general_df.to_dict('records')

    # FL Tire Data
    fl_tire_data_new = {
        'FL Pressure Before': fl_pressure_before,
        'FL Pressure After': fl_pressure_after,
        'FL Outer Temp Before': fl_oTemp_before,
        'FL Middle Temp Before': fl_mTemp_before,
        'FL Inner Temp Before': fl_iTemp_before,
        'FL Outer Temp After': fl_oTemp_after,
        'FL Middle Temp After': fl_mTemp_after,
        'FL Inner Temp After': fl_iTemp_after,
    }
    if fl_tire_data is None or fl_tire_data == []:
        fl_tire_df = pd.DataFrame([fl_tire_data_new])
    else:
        fl_tire_df = pd.DataFrame(fl_tire_data)
        fl_tire_df = pd.concat([fl_tire_df, pd.DataFrame([fl_tire_data_new])], ignore_index=True)
    fl_tire_columns = [{'name': col, 'id': col, 'editable': True} for col in fl_tire_df.columns]
    fl_tire_data_records = fl_tire_df.to_dict('records')

    # FR Tire Data
    fr_tire_data_new = {
        'FR Pressure Before': fr_pressure_before,
        'FR Pressure After': fr_pressure_after,
        'FR Outer Temp Before': fr_oTemp_before,
        'FR Middle Temp Before': fr_mTemp_before,
        'FR Inner Temp Before': fr_iTemp_before,
        'FR Outer Temp After': fr_oTemp_after,
        'FR Middle Temp After': fr_mTemp_after,
        'FR Inner Temp After': fr_iTemp_after,
    }
    if fr_tire_data is None or fr_tire_data == []:
        fr_tire_df = pd.DataFrame([fr_tire_data_new])
    else:
        fr_tire_df = pd.DataFrame(fr_tire_data)
        fr_tire_df = pd.concat([fr_tire_df, pd.DataFrame([fr_tire_data_new])], ignore_index=True)
    fr_tire_columns = [{'name': col, 'id': col, 'editable': True} for col in fr_tire_df.columns]
    fr_tire_data_records = fr_tire_df.to_dict('records')

    # RL Tire Data
    rl_tire_data_new = {
        'RL Pressure Before': rl_pressure_before,
        'RL Pressure After': rl_pressure_after,
        'RL Outer Temp Before': rl_oTemp_before,
        'RL Middle Temp Before': rl_mTemp_before,
        'RL Inner Temp Before': rl_iTemp_before,
        'RL Outer Temp After': rl_oTemp_after,
        'RL Middle Temp After': rl_mTemp_after,
        'RL Inner Temp After': rl_iTemp_after,
    }
    if rl_tire_data is None or rl_tire_data == []:
        rl_tire_df = pd.DataFrame([rl_tire_data_new])
    else:
        rl_tire_df = pd.DataFrame(rl_tire_data)
        rl_tire_df = pd.concat([rl_tire_df, pd.DataFrame([rl_tire_data_new])], ignore_index=True)
    rl_tire_columns = [{'name': col, 'id': col, 'editable': True} for col in rl_tire_df.columns]
    rl_tire_data_records = rl_tire_df.to_dict('records')

    # RR Tire Data
    rr_tire_data_new = {
        'RR Pressure Before': rr_pressure_before,
        'RR Pressure After': rr_pressure_after,
        'RR Outer Temp Before': rr_oTemp_before,
        'RR Middle Temp Before': rr_mTemp_before,
        'RR Inner Temp Before': rr_iTemp_before,
        'RR Outer Temp After': rr_oTemp_after,
        'RR Middle Temp After': rr_mTemp_after,
        'RR Inner Temp After': rr_iTemp_after,
    }
    if rr_tire_data is None or rr_tire_data == []:
        rr_tire_df = pd.DataFrame([rr_tire_data_new])
    else:
        rr_tire_df = pd.DataFrame(rr_tire_data)
        rr_tire_df = pd.concat([rr_tire_df, pd.DataFrame([rr_tire_data_new])], ignore_index=True)
    rr_tire_columns = [{'name': col, 'id': col, 'editable': True} for col in rr_tire_df.columns]
    rr_tire_data_records = rr_tire_df.to_dict('records')

    # Aero Data
    aero_data_new = {}
    if aero_data is None or aero_data == []:
        aero_df = pd.DataFrame([aero_data_new])
    else:
        aero_df = pd.DataFrame(aero_data)
        aero_df = pd.concat([aero_df, pd.DataFrame([aero_data_new])], ignore_index=True)
    aero_columns = [{'name': col, 'id': col, 'editable': True} for col in aero_df.columns]
    aero_data_records = aero_df.to_dict('records')

    # Chassis Data
    chassis_data_new = {}
    if chassis_data is None or chassis_data == []:
        chassis_df = pd.DataFrame([chassis_data_new])
    else:
        chassis_df = pd.DataFrame(chassis_data)
        chassis_df = pd.concat([chassis_df, pd.DataFrame([chassis_data_new])], ignore_index=True)
    chassis_columns = [{'name': col, 'id': col, 'editable': True} for col in chassis_df.columns]
    chassis_data_records = chassis_df.to_dict('records')

    # Powertrain Data
    powertrain_data_new = {}
    if powertrain_data is None or powertrain_data == []:
        powertrain_df = pd.DataFrame([powertrain_data_new])
    else:
        powertrain_df = pd.DataFrame(powertrain_data)
        powertrain_df = pd.concat([powertrain_df, pd.DataFrame([powertrain_data_new])], ignore_index=True)
    powertrain_columns = [{'name': col, 'id': col, 'editable': True} for col in powertrain_df.columns]
    powertrain_data_records = powertrain_df.to_dict('records')

    # Suspension Data
    suspension_data_new = {
        'Tire Compound': tire_compound,
        'Tire Set': tire_set,
        'Front Spring Rate': front_spring_rate,
        'Rear Spring Rate': rear_spring_rate,
        'Left ARB': left_arb,
        'Right ARB': right_arb,
    }
    if suspension_data is None or suspension_data == []:
        suspension_df = pd.DataFrame([suspension_data_new])
    else:
        suspension_df = pd.DataFrame(suspension_data)
        suspension_df = pd.concat([suspension_df, pd.DataFrame([suspension_data_new])], ignore_index=True)
    suspension_columns = [{'name': col, 'id': col, 'editable': True} for col in suspension_df.columns]
    suspension_data_records = suspension_df.to_dict('records')

    # Notes Data
    notes_data_new = {
        'Faults': faults,
        'Improvements': improvements,
        'Misc Notes': misc_notes
    }
    if notes_data is None or notes_data == []:
        notes_df = pd.DataFrame([notes_data_new])
    else:
        notes_df = pd.DataFrame(notes_data)
        notes_df = pd.concat([notes_df, pd.DataFrame([notes_data_new])], ignore_index=True)
    notes_columns = [{'name': col, 'id': col, 'editable': True} for col in notes_df.columns]
    notes_data_records = notes_df.to_dict('records')

    return (general_columns, general_data_records,
            fl_tire_columns, fl_tire_data_records,
            fr_tire_columns, fr_tire_data_records,
            rl_tire_columns, rl_tire_data_records,
            rr_tire_columns, rr_tire_data_records,
            aero_columns, aero_data_records,
            chassis_columns, chassis_data_records,
            powertrain_columns, powertrain_data_records,
            suspension_columns, suspension_data_records,
            notes_columns, notes_data_records,
            True, False)

@app.callback(
    Output('download-button', 'data'),
    Input('export-button', 'n_clicks'),
    [
        State('general-table', 'data'),
        State('fl-tire-table', 'data'),
        State('fr-tire-table', 'data'),
        State('rl-tire-table', 'data'),
        State('rr-tire-table', 'data'),
        State('suspension-table', 'data'),
        State('notes-table', 'data')
    ],
    prevent_initial_call=True
)
def export_data(n_clicks, general_data, fl_tire_data, fr_tire_data, rl_tire_data, rr_tire_data, suspension_data, notes_data):
    if not n_clicks:
        raise PreventUpdate

    general_df = pd.DataFrame(general_data)
    fl_tire_df = pd.DataFrame(fl_tire_data)
    fr_tire_df = pd.DataFrame(fr_tire_data)
    rl_tire_df = pd.DataFrame(rl_tire_data)
    rr_tire_df = pd.DataFrame(rr_tire_data)
    suspension_df = pd.DataFrame(suspension_data)
    notes_df = pd.DataFrame(notes_data)

    downloads_path = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_path, "Runsheet.xlsx")

    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        general_df.to_excel(writer, sheet_name='General', index=False)
        fl_tire_df.to_excel(writer, sheet_name='FL Tire', index=False)
        fr_tire_df.to_excel(writer, sheet_name='FR Tire', index=False)
        rl_tire_df.to_excel(writer, sheet_name='RL Tire', index=False)
        rr_tire_df.to_excel(writer, sheet_name='RR Tire', index=False)
        suspension_df.to_excel(writer, sheet_name='Suspension', index=False)
        notes_df.to_excel(writer, sheet_name='Notes', index=False)

    return dcc.send_file(file_path)


if __name__ == '__main__':
    app.run_server(debug=True)
