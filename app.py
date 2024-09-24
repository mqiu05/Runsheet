import os
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd

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
    html.Div(id='output-content', style={'position': 'relative'}),  # Container for the image and grid

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
    html.Button('Save', id='save-button', style={'margin-top': '20px', 'margin-left': '10px'}),
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
