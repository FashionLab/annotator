import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from ..app import appConfigure
from ..utils import load_image




MainLayout = html.Div([], id='main-content')

MainContent = lambda: html.Div([
        html.Div([
            html.Label('Brand'),
            dcc.Dropdown(
                id='brand_filter',
                options=appConfigure.files_by_brand()
            ),
            html.Label('Order'),
            dcc.Dropdown(
                id='order',
                options=[{'label': x, 'value': x} for x in ('random', 'sorted', 'unlabeled')],
                style={'marginBottom': '10px'}
            ),
            dash_table.DataTable(id='table',
                                 columns=[{'name': i, 'id': i} for i in appConfigure.files()[0].keys() if i != 'path'] if len(appConfigure.files() or []) > 0 else [],
                                 data=appConfigure.files(),
                                 page_action="native",
                                 page_current=0,
                                 page_size=18,
                                 row_selectable=False,
                                 style_table={'maxHeight': '600px',
                                              'overflowY': 'scroll'},
                                 style_cell_conditional=[{'if': {'column_id': c},
                                                          'textAlign': 'center'} for c in ['name', 'folder']],
                                 style_data_conditional=[{'if': {'row_index': 'odd'},
                                                          'backgroundColor': 'rgb(248, 248, 248)'},
                                                         {'if': {'row_index': appConfigure.selected()},
                                                          'backgroundColor': 'rgb(255, 0, 0)'}],
                                 style_header={'backgroundColor': 'rgb(230, 230, 230)',
                                               'fontWeight': 'bold',
                                               'textAlign': 'center'}),
        ], style={'columnCount': 1, 'height': '100%'}),
        html.Div([
            html.Label('Preview'),
            html.Img(id='preview',
                     src=load_image(appConfigure.files()[0]['path']) if len(appConfigure.files() or []) else '',
                     style={'maxHeight': '325px',
                            'height': '325px'}),
            dcc.RadioItems(
                options=[
                    {'label': 'Valid', 'value': 'valid'},
                    {'label': 'Invalid', 'value': 'invalid'},
                ],
                labelStyle={'display': 'inline-block'},
                value='valid'
            ),
            html.Label('M/F'),
            dcc.RadioItems(
                options=[
                    {'label': 'Male', 'value': 'male'},
                    {'label': 'Female', 'value': 'female'},
                    {'label': 'Either', 'value': 'either'},
                ],
                labelStyle={'display': 'inline-block'},
                value='either'
            ),
            html.Label('Class'),
            dcc.Dropdown(
                id='class',
                options=appConfigure.classes() or [],
                placeholder='Class...',
                style={'width': '100%'}
            ),
            html.Label('Notes'),
            dcc.Input(value='',
                      type='text',
                      style={'width': '100%',
                             'marginBottom': '10px'}),
            html.Div([
                html.Button('Previous',
                            id='prev',
                            style={'width': '50%',
                                   'marginBottom': '10px'}),
                html.Button('Next',
                            id='next',
                            style={'width': '50%',
                                   'marginBottom': '10px'}),
            ]),
            html.Button('Save',
                        id='save',
                        style={'width': '50%',
                               'marginLeft': '25%'}),
        ], style={'columnCount': 1,
                  'height': '100%',
                  'width': '100%'})
    ], style={'columnCount': 2,
              'height': '100%',
              'width': '100%'})
