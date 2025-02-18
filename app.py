from dash import Dash, html, dcc, dash_table, Output, Input, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import os

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Helper function for creating form fields
def create_input(label, input_id, input_type='text', placeholder='', options=None):
    if options:
        return dbc.Row([
            dbc.Label(label, width=3),
            dbc.Col(dcc.Dropdown(options, id=input_id, placeholder=placeholder, style={'width': '100%'}), width=9)
        ], className='mb-2')
    else:
        return dbc.Row([
            dbc.Label(label, width=3),
            dbc.Col(dcc.Input(type=input_type, id=input_id, placeholder=placeholder, style={'width': '100%'}), width=9)
        ], className='mb-2')


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
                    dcc.DatePickerSingle(id='date-picker'),
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
                    create_input('Tire Compound', 'tire-compound'),
                    create_input('Tire Set', 'tire-set'),
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
        '', '', None, None, None, None,  # Suspension
        '', '', ''  # Notes
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
            PreventUpdate, PreventUpdate,  # general table
            PreventUpdate, PreventUpdate,  # tire table
            PreventUpdate, PreventUpdate,  # aero table
            PreventUpdate, PreventUpdate,  # suspension table
            PreventUpdate, PreventUpdate,  # notes table
            True                   # session-error => displayed
        )

    # For every other field, autofill with '' if None
    date = date or ''
    venue = venue or ''
    event = event or ''
    driver = driver or ''
    weight = weight or ''       # If blank or None, store as ''
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
        False   # Hide the session-error dialog
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
        general_df.to_excel(writer, sheet_name='General', index=False)
        tire_df.to_excel(writer, sheet_name='Tires', index=False)
        aero_df.to_excel(writer, sheet_name='Aero', index=False)
        susp_df.to_excel(writer, sheet_name='Suspension', index=False)
        notes_df.to_excel(writer, sheet_name='Notes', index=False)

    return dcc.send_file(file_path)


if __name__ == '__main__':
    app.run_server(debug=True)
