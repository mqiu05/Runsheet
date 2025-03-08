from dash import Dash, html, dcc, dash_table, Output, Input, State, no_update
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import os

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Helper function for creating form fields
def create_input(label, input_id, input_type='text', placeholder='', options=None):
    if options:
        return dbc.Row([
            dbc.Label(label, width=1),
            dbc.Col(dcc.Dropdown(options, id=input_id, placeholder=placeholder, style={'width': '100%'}), width=9)
        ], className='mb-2')
    else:
        return dbc.Row([
            dbc.Label(label, width=1),
            dbc.Col(dcc.Input(type=input_type, id=input_id, placeholder=placeholder, style={'width': '100%'}), width=9)
        ], className='mb-2')


def create_tire_box(tire_label, tire_id_prefix, top, left):
    return html.Div(
        children=[
            html.Div(f'{tire_label} Tire',
                     style={'grid-column': '1 / 5', 'font-weight': 'bold', 'text-align': 'center'}),

            # Pressure
            html.Div('Pressure', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
            html.Div('Before', style={'grid-column': '1 / 2'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-pressure-before', style={'width': '100%'}),
            html.Div('After', style={'grid-column': '1 / 2'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-pressure-after', style={'width': '100%'}),

            # Temperature
            html.Div('Temp', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),

            # Temps Before
            html.Div('Before', style={'grid-column': '1 / 2'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-oTemp-before', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-mTemp-before', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-iTemp-before', style={'width': '100%'}),

            # Temps After
            html.Div('After', style={'grid-column': '1 / 2'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-oTemp-after', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-mTemp-after', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-iTemp-after', style={'width': '100%'}),
    # Tire wear
            html.Div('Wear', style={'grid-column': '1 / 2', 'font-weight': 'bold'}),
            html.Div('O', style={'text-align': 'center', 'font-weight': 'bold'}),
            html.Div('M', style={'text-align': 'center', 'font-weight': 'bold'}),
            html.Div('I', style={'text-align': 'center', 'font-weight': 'bold'}),

            # Temps Before
            html.Div('Before', style={'grid-column': '1 / 2'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-oWear-before', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-mWear-before', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-iWear-before', style={'width': '100%'}),

            # Temps After
            html.Div('After', style={'grid-column': '1 / 2'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-oWear-after', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-mWear-after', style={'width': '100%'}),
            dcc.Input(type='number', id=f'{tire_id_prefix}-iWear-after', style={'width': '100%'}),
        ],
        style={
            'position': 'absolute',
            'top': top,
            'left': left,
            'display': 'grid',
            'grid-template-columns': 'repeat(4, 1fr)',
            'gap': '5px',
            'width': '230px',
            'border': '2px solid black',
            'padding': '10px',
            'background-color': 'white'
        }
    )


app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.Img(src='/assets/logo.png', className='img-fluid', style={'max-width': '400px'}), width=12,
                className='text-center my-3')
    ),

    dbc.Tabs([
        dbc.Tab(label='Input Data', children=[
            dbc.Card([
                dbc.CardHeader(html.H4("Session Details")),
                dbc.CardBody([
                    create_input('Session Number', 'session', 'number', 'Enter session number'),
                ])
            ], className='mb-3'),

            dbc.Accordion([
                dbc.AccordionItem([
                    dbc.Row([
                        dbc.Label("Date", width=1),
                        dbc.Col(
                            dcc.DatePickerSingle(id='date-picker', style={'width': '100%'}),
                            width=9
                        )
                    ], className='mb-2'),

                    create_input('Venue', 'venue', options=['Purdue GP', 'Frankfort HS']),
                    create_input('Event', 'event',
                                 options=['Acceleration', 'Autocross', 'Brake', 'Endurance', 'Skid Pad']),
                    create_input('Driver', 'driver', options=['Matt', 'Simon', 'Troy']),
                    create_input('Weight (kg)', 'weight', 'number'),
                ], title='General'),
                dbc.AccordionItem([
                    create_input('Front Wing', 'front-wing', options=['Yes', 'No']),
                    create_input('Under tray', 'under-tray', options=['Yes', 'No']),
                    create_input('Rear Wing', 'rear-wing', options=['Yes', 'No']),
                ], title='Aero'),
                dbc.AccordionItem([
                    html.Label("Tire Pressure"),

                    html.Div(
                        [
                            html.Img(
                                src='/assets/car.png',
                                style={
                                    'width': '55%',
                                    'height': 'auto',
                                    'display': 'block',
                                    'margin': '0 auto'
                                }
                            ),
                            # Front Left Tire Box
                            create_tire_box('Front Left', 'fl', '5%', '-10%'),

                            # Front Right Tire Box
                            create_tire_box('Front Right', 'fr', '5%', '77%'),

                            # Rear Left Tire Box
                            create_tire_box('Rear Left', 'rl', '60%', '-10%'),

                            # Rear Right Tire Box
                            create_tire_box('Rear Right', 'rr', '60%', '77%'),
                        ],
                        style={
                            'position': 'relative',
                            'width': '700px',
                            'margin': '0 auto',
                            'border': '1px solid #ccc',
                            'boxSizing': 'border-box'
                        }
                    ),

                    dbc.Row([
                        dbc.Label("Tire Compound", width=1),
                        dbc.Col(dcc.Input(id='tire-compound', type='text', placeholder='', style={'width': '100%'}),
                                width=9)
                    ], className='mb-2'),

                    dbc.Row([
                        dbc.Label("Tire Set", width=1),
                        dbc.Col(dcc.Input(id='tire-set', type='text', placeholder='', style={'width': '100%'}), width=9)
                    ], className='mb-2'),

                    create_input('Front Spring Rate', 'front-spring-rate', options=['300', '350', '400', '450']),
                    create_input('Rear Spring Rate', 'rear-spring-rate', options=['300', '350', '400', '450']),
                    create_input('Right ARB', 'right-arb', options=['1', '2', '3', '4', '5', '6']),
                    create_input('Left ARB', 'left-arb', options=['1', '2', '3', '4', '5', '6']),
                ], title='Suspension'),

                dbc.AccordionItem([
                    create_input('Faults', 'faults'),
                    create_input('Improvements', 'improvements'),
                    create_input('Misc.', 'misc'),
                ], title='Notes'),

                dbc.Row([
                    dbc.Col(dbc.Button('Clear', id='clear-button', color='danger', className='w-100'), width=6),
                    dbc.Col(dbc.Button('Save', id='save-button', color='success', className='w-100'), width=6),
                ], className='mb-3')
            ]),
            dcc.ConfirmDialog(
                id='session-error',
                message='Session value cannot be empty.'
            )
        ]),
        dbc.Tab(label='View Data', children=[
            html.H4('General'),
            dash_table.DataTable(id='general-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}),
            html.H4('Tires Data'),
            dash_table.DataTable(id='tire-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}),
            html.H4('Aero Data'),
            dash_table.DataTable(id='aero-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}),
            html.H4('Suspension Data'),
            dash_table.DataTable(id='suspension-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}),
            html.H4('Notes'),
            dash_table.DataTable(id='notes-table', columns=[], data=[], editable=True,
                                 style_table={'overflowX': 'scroll'}),
            dbc.Button('Export', id='export-button', color='primary', className='mt-3'),
            dcc.Download(id='download-button')
        ]),
    ])
], fluid=True)  # Correct placement of fluid=True


@app.callback(
    [
        Output('session', 'value'),
        Output('date-picker', 'date'),
        Output('venue', 'value'),
        Output('event', 'value'),
        Output('driver', 'value'),
        Output('weight', 'value'),
        Output('front-wing', 'value'),
        Output('under-tray', 'value'),
        Output('rear-wing', 'value'),

        # FL Tire
        Output('fl-pressure-before', 'value'),
        Output('fl-pressure-after', 'value'),
        Output('fl-oTemp-before', 'value'),
        Output('fl-mTemp-before', 'value'),
        Output('fl-iTemp-before', 'value'),
        Output('fl-oTemp-after', 'value'),
        Output('fl-mTemp-after', 'value'),
        Output('fl-iTemp-after', 'value'),
        Output('fl-oWear-before', 'value'),
        Output('fl-mWear-before', 'value'),
        Output('fl-iWear-before', 'value'),
        Output('fl-oWear-after', 'value'),
        Output('fl-mWear-after', 'value'),
        Output('fl-iWear-after', 'value'),

        # FR Tire
        Output('fr-pressure-before', 'value'),
        Output('fr-pressure-after', 'value'),
        Output('fr-oTemp-before', 'value'),
        Output('fr-mTemp-before', 'value'),
        Output('fr-iTemp-before', 'value'),
        Output('fr-oTemp-after', 'value'),
        Output('fr-mTemp-after', 'value'),
        Output('fr-iTemp-after', 'value'),
        Output('fr-oWear-before', 'value'),
        Output('fr-mWear-before', 'value'),
        Output('fr-iWear-before', 'value'),
        Output('fr-oWear-after', 'value'),
        Output('fr-mWear-after', 'value'),
        Output('fr-iWear-after', 'value'),

        # RL Tire
        Output('rl-pressure-before', 'value'),
        Output('rl-pressure-after', 'value'),
        Output('rl-oTemp-before', 'value'),
        Output('rl-mTemp-before', 'value'),
        Output('rl-iTemp-before', 'value'),
        Output('rl-oTemp-after', 'value'),
        Output('rl-mTemp-after', 'value'),
        Output('rl-iTemp-after', 'value'),
        Output('rl-oWear-before', 'value'),
        Output('rl-mWear-before', 'value'),
        Output('rl-iWear-before', 'value'),
        Output('rl-oWear-after', 'value'),
        Output('rl-mWear-after', 'value'),
        Output('rl-iWear-after', 'value'),

        # RR Tire
        Output('rr-pressure-before', 'value'),
        Output('rr-pressure-after', 'value'),
        Output('rr-oTemp-before', 'value'),
        Output('rr-mTemp-before', 'value'),
        Output('rr-iTemp-before', 'value'),
        Output('rr-oTemp-after', 'value'),
        Output('rr-mTemp-after', 'value'),
        Output('rr-iTemp-after', 'value'),
        Output('rr-oWear-before', 'value'),
        Output('rr-mWear-before', 'value'),
        Output('rr-iWear-before', 'value'),
        Output('rr-oWear-after', 'value'),
        Output('rr-mWear-after', 'value'),
        Output('rr-iWear-after', 'value'),

        # Other Fields
        Output('tire-compound', 'value'),
        Output('tire-set', 'value'),
        Output('front-spring-rate', 'value'),
        Output('rear-spring-rate', 'value'),
        Output('right-arb', 'value'),
        Output('left-arb', 'value'),
        Output('faults', 'value'),
        Output('improvements', 'value'),
        Output('misc', 'value'),
    ],
    Input('clear-button', 'n_clicks'),
    prevent_initial_call=True
)
def clear_inputs(n_clicks):
    return (
        '',  # Session Number
        None, None, None, None, None,  # General
        None, None, None,  # Aero

        # FL Tire
        '', '', '', '', '', '', '', '', '', '', '', '', '', '',

        # FR Tire
        '', '', '', '', '', '', '', '', '', '', '', '', '', '',

        # RL Tire
        '', '', '', '', '', '', '', '', '', '', '', '', '', '',

        # RR Tire
        '', '', '', '', '', '', '', '', '', '', '', '', '', '',

        # Suspension and Notes
        '', '', None, None, None, None, '', '', ''
    )


@app.callback(
    [
        Output('general-table', 'columns'),
        Output('general-table', 'data'),
        Output('tire-table', 'columns'),
        Output('tire-table', 'data'),
        Output('aero-table', 'columns'),
        Output('aero-table', 'data'),
        Output('suspension-table', 'columns'),
        Output('suspension-table', 'data'),
        Output('notes-table', 'columns'),
        Output('notes-table', 'data'),
        Output('session-error', 'displayed'),
    ],
    Input('save-button', 'n_clicks'),
    [
        State('session', 'value'),
        State('date-picker', 'date'),
        State('venue', 'value'),
        State('event', 'value'),
        State('driver', 'value'),
        State('weight', 'value'),

        # FL Tire
        State('fl-pressure-before', 'value'),
        State('fl-pressure-after', 'value'),
        State('fl-oTemp-before', 'value'),
        State('fl-mTemp-before', 'value'),
        State('fl-iTemp-before', 'value'),
        State('fl-oTemp-after', 'value'),
        State('fl-mTemp-after', 'value'),
        State('fl-iTemp-after', 'value'),
        State('fl-oWear-before', 'value'),
        State('fl-mWear-before', 'value'),
        State('fl-iWear-before', 'value'),
        State('fl-oWear-after', 'value'),
        State('fl-mWear-after', 'value'),
        State('fl-iWear-after', 'value'),

        # FR Tire
        State('fr-pressure-before', 'value'),
        State('fr-pressure-after', 'value'),
        State('fr-oTemp-before', 'value'),
        State('fr-mTemp-before', 'value'),
        State('fr-iTemp-before', 'value'),
        State('fr-oTemp-after', 'value'),
        State('fr-mTemp-after', 'value'),
        State('fr-iTemp-after', 'value'),
        State('fr-oWear-before', 'value'),
        State('fr-mWear-before', 'value'),
        State('fr-iWear-before', 'value'),
        State('fr-oWear-after', 'value'),
        State('fr-mWear-after', 'value'),
        State('fr-iWear-after', 'value'),

        # RL Tire
        State('rl-pressure-before', 'value'),
        State('rl-pressure-after', 'value'),
        State('rl-oTemp-before', 'value'),
        State('rl-mTemp-before', 'value'),
        State('rl-iTemp-before', 'value'),
        State('rl-oTemp-after', 'value'),
        State('rl-mTemp-after', 'value'),
        State('rl-iTemp-after', 'value'),
        State('rl-oWear-before', 'value'),
        State('rl-mWear-before', 'value'),
        State('rl-iWear-before', 'value'),
        State('rl-oWear-after', 'value'),
        State('rl-mWear-after', 'value'),
        State('rl-iWear-after', 'value'),

        # RR Tire
        State('rr-pressure-before', 'value'),
        State('rr-pressure-after', 'value'),
        State('rr-oTemp-before', 'value'),
        State('rr-mTemp-before', 'value'),
        State('rr-iTemp-before', 'value'),
        State('rr-oTemp-after', 'value'),
        State('rr-mTemp-after', 'value'),
        State('rr-iTemp-after', 'value'),
        State('rr-oWear-before', 'value'),
        State('rr-mWear-before', 'value'),
        State('rr-iWear-before', 'value'),
        State('rr-oWear-after', 'value'),
        State('rr-mWear-after', 'value'),
        State('rr-iWear-after', 'value'),

        # Other Fields
        State('tire-compound', 'value'),
        State('tire-set', 'value'),
        State('front-wing', 'value'),
        State('under-tray', 'value'),
        State('rear-wing', 'value'),
        State('front-spring-rate', 'value'),
        State('rear-spring-rate', 'value'),
        State('right-arb', 'value'),
        State('left-arb', 'value'),
        State('faults', 'value'),
        State('improvements', 'value'),
        State('misc', 'value'),

        # Existing Data
        State('general-table', 'columns'),
        State('general-table', 'data'),
        State('tire-table', 'columns'),
        State('tire-table', 'data'),
        State('aero-table', 'columns'),
        State('aero-table', 'data'),
        State('suspension-table', 'columns'),
        State('suspension-table', 'data'),
        State('notes-table', 'columns'),
        State('notes-table', 'data'),
    ],
    prevent_initial_call=True
)

def save_data(n_clicks, session, date, venue, event, driver, weight,
              fl_pressure_before, fl_pressure_after, fl_oTemp_before, fl_mTemp_before, fl_iTemp_before,
              fl_oTemp_after, fl_mTemp_after, fl_iTemp_after, fl_oWear_before, fl_mWear_before, fl_iWear_before,
              fl_oWear_after, fl_mWear_after, fl_iWear_after,

              fr_pressure_before, fr_pressure_after, fr_oTemp_before, fr_mTemp_before, fr_iTemp_before,
              fr_oTemp_after, fr_mTemp_after, fr_iTemp_after, fr_oWear_before, fr_mWear_before, fr_iWear_before,
              fr_oWear_after, fr_mWear_after, fr_iWear_after,

              rl_pressure_before, rl_pressure_after, rl_oTemp_before, rl_mTemp_before, rl_iTemp_before,
              rl_oTemp_after, rl_mTemp_after, rl_iTemp_after, rl_oWear_before, rl_mWear_before, rl_iWear_before,
              rl_oWear_after, rl_mWear_after, rl_iWear_after,

              rr_pressure_before, rr_pressure_after, rr_oTemp_before, rr_mTemp_before, rr_iTemp_before,
              rr_oTemp_after, rr_mTemp_after, rr_iTemp_after, rr_oWear_before, rr_mWear_before, rr_iWear_before,
              rr_oWear_after, rr_mWear_after, rr_iWear_after,

              tire_compound, tire_set,
              front_wing, under_tray, rear_wing,
              front_spring, rear_spring, right_arb, left_arb,
              faults, improvements, misc,
              general_cols, general_data,
              tire_cols, tire_data,
              aero_cols, aero_data,
              susp_cols, susp_data,
              notes_cols, notes_data):
    if not n_clicks:
        raise PreventUpdate

    # Session is mandatory: if empty, display error dialog instead of saving
    if not session:
        return (
            no_update, no_update,  # general table
            no_update, no_update,  # tire table
            no_update, no_update,  # aero table
            no_update, no_update,  # suspension table
            no_update, no_update,  # notes table
            True  # session-error => displayed
        )

    # For every other field, autofill with '' if None
    date = date or ''
    venue = venue or ''
    event = event or ''
    driver = driver or ''
    weight = weight or ''

    fl_pressure_before = fl_pressure_before or ''
    fl_pressure_after = fl_pressure_after or ''
    fl_oTemp_before = fl_oTemp_before or ''
    fl_mTemp_before = fl_mTemp_before or ''
    fl_iTemp_before = fl_iTemp_before or ''
    fl_oTemp_after = fl_oTemp_after or ''
    fl_mTemp_after = fl_mTemp_after or ''
    fl_iTemp_after = fl_iTemp_after or ''
    fl_oWear_before = fl_oWear_before or ''
    fl_mWear_before = fl_mWear_before or ''
    fl_iWear_before = fl_iWear_before or ''
    fl_oWear_after = fl_oWear_after or ''
    fl_mWear_after = fl_mWear_after or ''
    fl_iWear_after = fl_iWear_after or ''

    fr_pressure_before = fr_pressure_before or ''
    fr_pressure_after = fr_pressure_after or ''
    fr_oTemp_before = fr_oTemp_before or ''
    fr_mTemp_before = fr_mTemp_before or ''
    fr_iTemp_before = fr_iTemp_before or ''
    fr_oTemp_after = fr_oTemp_after or ''
    fr_mTemp_after = fr_mTemp_after or ''
    fr_iTemp_after = fr_iTemp_after or ''
    fr_oWear_before = fr_oWear_before or ''
    fr_mWear_before = fr_mWear_before or ''
    fr_iWear_before = fr_iWear_before or ''
    fr_oWear_after = fr_oWear_after or ''
    fr_mWear_after = fr_mWear_after or ''
    fr_iWear_after = fr_iWear_after or ''

    rl_pressure_before = rl_pressure_before or ''
    rl_pressure_after = rl_pressure_after or ''
    rl_oTemp_before = rl_oTemp_before or ''
    rl_mTemp_before = rl_mTemp_before or ''
    rl_iTemp_before = rl_iTemp_before or ''
    rl_oTemp_after = rl_oTemp_after or ''
    rl_mTemp_after = rl_mTemp_after or ''
    rl_iTemp_after = rl_iTemp_after or ''
    rl_oWear_before = rl_oWear_before or ''
    rl_mWear_before = rl_mWear_before or ''
    rl_iWear_before = rl_iWear_before or ''
    rl_oWear_after = rl_oWear_after or ''
    rl_mWear_after = rl_mWear_after or ''
    rl_iWear_after = rl_iWear_after or ''

    rr_pressure_before = rr_pressure_before or ''
    rr_pressure_after = rr_pressure_after or ''
    rr_oTemp_before = rr_oTemp_before or ''
    rr_mTemp_before = rr_mTemp_before or ''
    rr_iTemp_before = rr_iTemp_before or ''
    rr_oTemp_after = rr_oTemp_after or ''
    rr_mTemp_after = rr_mTemp_after or ''
    rr_iTemp_after = rr_iTemp_after or ''
    rr_oWear_before = rr_oWear_before or ''
    rr_mWear_before = rr_mWear_before or ''
    rr_iWear_before = rr_iWear_before or ''
    rr_oWear_after = rr_oWear_after or ''
    rr_mWear_after = rr_mWear_after or ''
    rr_iWear_after = rr_iWear_after or ''

    tire_compound = tire_compound or ''
    tire_set = tire_set or ''
    front_wing = front_wing or ''
    under_tray = under_tray or ''
    rear_wing = rear_wing or ''
    front_spring = front_spring or ''
    rear_spring = rear_spring or ''
    right_arb = right_arb or ''
    left_arb = left_arb or ''
    faults = faults or ''
    improvements = improvements or ''
    misc = misc or ''

    # Build the new rows for each category
    new_general_row = {
        'Session': session,
        'Date': date,
        'Venue': venue,
        'Event': event,
        'Driver': driver,
        'Weight': weight,
    }

    # GENERAL TABLE
    if not general_data:
        general_df = pd.DataFrame([new_general_row])
    else:
        general_df = pd.DataFrame(general_data)
    general_df = pd.concat([general_df, pd.DataFrame([new_general_row])], ignore_index=True)
    general_cols = [{'name': c, 'id': c, 'editable': True} for c in general_df.columns]
    general_data = general_df.to_dict('records')

    # TIRE TABLE
    new_tire_row = {
        # Front Left Tire
        'FL Pressure Before': fl_pressure_before,
        'FL Pressure After': fl_pressure_after,
        'FL Outer Temp Before': fl_oTemp_before,
        'FL Middle Temp Before': fl_mTemp_before,
        'FL Inner Temp Before': fl_iTemp_before,
        'FL Outer Temp After': fl_oTemp_after,
        'FL Middle Temp After': fl_mTemp_after,
        'FL Inner Temp After': fl_iTemp_after,
        'FL Outer Wear Before': fl_oWear_before,
        'FL Middle Wear Before': fl_mWear_before,
        'FL Inner Wear Before': fl_iWear_before,
        'FL Outer Wear After': fl_oWear_after,
        'FL Middle Wear After': fl_mWear_after,
        'FL Inner Wear After': fl_iWear_after,

        # Front Right Tire
        'FR Pressure Before': fr_pressure_before,
        'FR Pressure After': fr_pressure_after,
        'FR Outer Temp Before': fr_oTemp_before,
        'FR Middle Temp Before': fr_mTemp_before,
        'FR Inner Temp Before': fr_iTemp_before,
        'FR Outer Temp After': fr_oTemp_after,
        'FR Middle Temp After': fr_mTemp_after,
        'FR Inner Temp After': fr_iTemp_after,
        'FR Outer Wear Before': fr_oWear_before,
        'FR Middle Wear Before': fr_mWear_before,
        'FR Inner Wear Before': fr_iWear_before,
        'FR Outer Wear After': fr_oWear_after,
        'FR Middle Wear After': fr_mWear_after,
        'FR Inner Wear After': fr_iWear_after,

        # Rear Left Tire
        'RL Pressure Before': rl_pressure_before,
        'RL Pressure After': rl_pressure_after,
        'RL Outer Temp Before': rl_oTemp_before,
        'RL Middle Temp Before': rl_mTemp_before,
        'RL Inner Temp Before': rl_iTemp_before,
        'RL Outer Temp After': rl_oTemp_after,
        'RL Middle Temp After': rl_mTemp_after,
        'RL Inner Temp After': rl_iTemp_after,
        'RL Outer Wear Before': rl_oWear_before,
        'RL Middle Wear Before': rl_mWear_before,
        'RL Inner Wear Before': rl_iWear_before,
        'RL Outer Wear After': rl_oWear_after,
        'RL Middle Wear After': rl_mWear_after,
        'RL Inner Wear After': rl_iWear_after,

        # Rear Right Tire
        'RR Pressure Before': rr_pressure_before,
        'RR Pressure After': rr_pressure_after,
        'RR Outer Temp Before': rr_oTemp_before,
        'RR Middle Temp Before': rr_mTemp_before,
        'RR Inner Temp Before': rr_iTemp_before,
        'RR Outer Temp After': rr_oTemp_after,
        'RR Middle Temp After': rr_mTemp_after,
        'RR Inner Temp After': rr_iTemp_after,
        'RR Outer Wear Before': rr_oWear_before,
        'RR Middle Wear Before': rr_mWear_before,
        'RR Inner Wear Before': rr_iWear_before,
        'RR Outer Wear After': rr_oWear_after,
        'RR Middle Wear After': rr_mWear_after,
        'RR Inner Wear After': rr_iWear_after,

        # Tire Compound & Set
        'Tire Compound': tire_compound,
        'Tire Set': tire_set,
    }

    if not tire_data:
        tire_df = pd.DataFrame([new_tire_row])
    else:
        tire_df = pd.DataFrame(tire_data)
    tire_df = pd.concat([tire_df, pd.DataFrame([new_tire_row])], ignore_index=True)
    tire_cols = [{'name': c, 'id': c, 'editable': True} for c in tire_df.columns]
    tire_data = tire_df.to_dict('records')

    # AERO TABLE
    new_aero_row = {
        'Front Wing': front_wing,
        'Under Tray': under_tray,
        'Rear Wing': rear_wing,
    }
    if not aero_data:
        aero_df = pd.DataFrame([new_aero_row])
    else:
        aero_df = pd.DataFrame(aero_data)
    aero_df = pd.concat([aero_df, pd.DataFrame([new_aero_row])], ignore_index=True)
    aero_cols = [{'name': c, 'id': c, 'editable': True} for c in aero_df.columns]
    aero_data = aero_df.to_dict('records')

    # SUSPENSION TABLE
    new_susp_row = {
        'Front Spring Rate': front_spring,
        'Rear Spring Rate': rear_spring,
        'Right ARB': right_arb,
        'Left ARB': left_arb,
    }
    if not susp_data:
        susp_df = pd.DataFrame([new_susp_row])
    else:
        susp_df = pd.DataFrame(susp_data)
    susp_df = pd.concat([susp_df, pd.DataFrame([new_susp_row])], ignore_index=True)
    susp_cols = [{'name': c, 'id': c, 'editable': True} for c in susp_df.columns]
    susp_data = susp_df.to_dict('records')

    # NOTES TABLE
    new_notes_row = {
        'Faults': faults,
        'Improvements': improvements,
        'Misc': misc,
    }
    if not notes_data:
        notes_df = pd.DataFrame([new_notes_row])
    else:
        notes_df = pd.DataFrame(notes_data)
    notes_df = pd.concat([notes_df, pd.DataFrame([new_notes_row])], ignore_index=True)
    notes_cols = [{'name': c, 'id': c, 'editable': True} for c in notes_df.columns]
    notes_data = notes_df.to_dict('records')

    return (
        general_cols, general_data,
        tire_cols, tire_data,
        aero_cols, aero_data,
        susp_cols, susp_data,
        notes_cols, notes_data,
        False  # Hide the session-error dialog
    )


@app.callback(
    Output('download-button', 'data'),
    Input('export-button', 'n_clicks'),
    [
        State('general-table', 'data'),
        State('tire-table', 'data'),
        State('aero-table', 'data'),
        State('suspension-table', 'data'),
        State('notes-table', 'data'),
    ],
    prevent_initial_call=True
)
def export_data(n_clicks, general_data, tire_data, aero_data, susp_data, notes_data):
    if not n_clicks:
        raise PreventUpdate

    downloads_path = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_path, "Runsheet.xlsx")

    general_df = pd.DataFrame(general_data)
    tire_df = pd.DataFrame(tire_data)
    aero_df = pd.DataFrame(aero_data)
    susp_df = pd.DataFrame(susp_data)
    notes_df = pd.DataFrame(notes_data)

    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for df, sheet_name in zip(
                [general_df, tire_df, aero_df, susp_df, notes_df],
                ['General', 'Tires', 'Aero', 'Suspension', 'Notes']
        ):
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # 🔥 Auto-adjust column widths
            worksheet = writer.sheets[sheet_name]
            for col_idx, col in enumerate(df.columns):
                max_length = max(df[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.column_dimensions[worksheet.cell(1, col_idx + 1).column_letter].width = max_length

    return dcc.send_file(file_path)


if __name__ == '__main__':
    app.run_server(debug=True)
