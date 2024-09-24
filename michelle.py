from dash import Dash, html, dcc, Input, Output, State

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(children=[
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
    html.Div(id='general-section', style={'display': 'none'}),  # Initially hidden

    html.Button(
        'Notes',
        id='notes-button',
        n_clicks=0,
        style={
            'outline': 'none', 'border': 'none', 'background-color': 'white',
            'color': 'black', 'padding': '10px 20px', 'font-size': '25px', 'cursor': 'pointer',
            'z-index': 2, 'text-decoration': 'underline'
        }
    ),
    html.Div(id='notes-section', style={'display': 'none'}),  # Initially hidden

    html.Button('Clear', id='clear-button', style={'margin-top': '20px'}),
])


@app.callback(
    Output('general-section', 'style'),
    Input('general-button', 'n_clicks'),
    State('general-section', 'style')
)
def toggle_general_section(n_clicks, style):
    if n_clicks % 2 == 1:
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    Output('notes-section', 'style'),
    Input('notes-button', 'n_clicks'),
    State('notes-section', 'style')
)
def toggle_notes_section(n_clicks, style):
    if n_clicks % 2 == 1:
        return {'display': 'block'}
    return {'display': 'none'}


@app.callback(
    [Output('general-section', 'children'),
     Output('notes-section', 'children')],
    [Input('general-button', 'n_clicks'),
     Input('notes-button', 'n_clicks')],
)

def update_sections(general_clicks, notes_clicks):
    general_content = html.Div([
        html.Div('Session Number', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
        dcc.Input(placeholder='Session Number', type='number', value='', id='session', style={'width': '100%'}),
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
    ])

    notes_content = html.Div([
        html.Div('Driver Notes', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
        dcc.Textarea(placeholder='Driver Notes', value='', style={'width': '100%'}, id='driver-notes'),
        html.Div('Faults', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
        dcc.Textarea(placeholder='Faults', value='', style={'width': '100%'}, id='faults'),
        html.Div('Improvements', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
        dcc.Textarea(placeholder='Improvements', value='', style={'width': '100%'}, id='improvements'),
        html.Div('Misc.', style={'grid-column': '1 / 3', 'font-weight': 'bold'}),
        dcc.Textarea(placeholder='Misc. Notes', value='', style={'width': '100%'}, id='misc-notes'),
    ])

    return general_content if general_clicks else None, notes_content if notes_clicks else None


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
