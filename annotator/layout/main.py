import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from ..app import appConfigure
from ..utils import load_image

BRAND_FILTER = 'brand-filter'
ORDER_DROPDOWN = 'order-dropdown'
ITEM_VALID = 'item-valid'
ITEM_AD_TYPE = 'item-ad-type'
ITEM_VIEW = 'item-view'
ITEM_SEX = 'item-sex'
ITEM_COLOR = 'item-color'
ITEM_CLASS = 'item-class'
ITEM_NOTES = 'item_notes'
MAIN_CONTENT = 'main-content'


MainLayoutEmpty = [dcc.Dropdown(id=BRAND_FILTER, options=[]),
                   dcc.Dropdown(id=ORDER_DROPDOWN, options=[])]

MainLayout = html.Div(MainLayoutEmpty,
                      id=MAIN_CONTENT,
                      style={
                          'display': 'flex',
                          'flexDirection': 'columns',
                          'height': '100%'
                      })

MainContent = lambda: html.Div([
        html.Div([
            html.Label('Brand'),
            dcc.Dropdown(
                id=BRAND_FILTER,
                options=appConfigure.files_by_brand(),
                value=appConfigure.brand_filter(),
            ),
            html.Label('Order'),
            dcc.Dropdown(
                id=ORDER_DROPDOWN,
                options=[{'label': x, 'value': x} for x in ('random', 'sorted', 'unlabeled')],
                style={'marginBottom': '10px'},
                value=appConfigure.order(),
            ),
            dash_table.DataTable(id='table',
                                 columns=[{'name': i, 'id': i} for i in appConfigure.files()[0].keys() if i != 'path'],
                                 data=appConfigure.files(),
                                 page_action="native",
                                 page_current=0,
                                 page_size=appConfigure._max_per_page,
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
        ], style={
            'height': '100%',
            'display': 'flex',
            'flexDirection': 'column',
            'width': '50%',
            'margin': '5px',
        }),
        html.Div([
            html.Label('Preview'),
            html.Img(id='preview',
                     src=load_image(appConfigure.files()[0]['path']),
                     style={'maxHeight': '325px',
                            'height': '325px'}),
            dcc.Dropdown(
                id=ITEM_VALID,
                options=[
                    {'label': 'Valid', 'value': 'valid'},
                    {'label': 'Invalid', 'value': 'invalid'},
                ]            ),
            html.Label('Class'),
            dcc.Dropdown(
                id=ITEM_CLASS,
                options=appConfigure.classes(),
                placeholder='Class...',
                style={'width': '100%'}
            ),
            html.Label('Ad Type'),
            dcc.Dropdown(
                id=ITEM_AD_TYPE,
                options=[
                    {'label': 'Single Item', 'value': 'single'},
                    {'label': 'Multi Item', 'value': 'multi'},
                    {'label': 'Ad', 'value': 'ad'},
                ]
            ),
            html.Label('View'),
            dcc.Dropdown(
                id=ITEM_VIEW,
                options=[
                    {'label': 'Top', 'value': 'top'},
                    {'label': 'Front', 'value': 'front'},
                    {'label': 'Back', 'value': 'back'},
                    {'label': 'Side', 'value': 'side'},
                    {'label': 'Bottom', 'value': 'bottom'},
                    {'label': 'Other', 'value': 'other'},
                ]
            ),
            html.Label('M/F'),
            dcc.Dropdown(
                id=ITEM_SEX,
                options=[
                    {'label': 'Male', 'value': 'male'},
                    {'label': 'Female', 'value': 'female'},
                    {'label': 'Either', 'value': 'either'},
                ],
            ),
            html.Label('Color'),
            dcc.Dropdown(
                id=ITEM_COLOR,
                options=[
                    {'label': 'Monochromatic', 'value': 'mono'},
                    {'label': 'Colorful', 'value': 'colorful'},
                    {'label': 'Neutral', 'value': 'neutral'},
                ],
            ),
            html.Label('Notes'),
            dcc.Textarea(id=ITEM_NOTES,
                         value='',
                         style={'width': '100%',
                                'marginBottom': '10px'}),
            html.Div(id='hidden-div1', style={'display':'none'}),
            html.Div([
                html.Button('Previous',
                            id='prev',
                            style={'width': '50%',
                                   'marginBottom': '10px'}),
                html.Button('Next',
                            id='next',
                            style={'width': '50%',
                                   'marginBottom': '10px'}),
            ], style={
                'width': '100%',
                'margin': 'auto',
            }),
        ], style={      
            'height': '100%',
            'width': '50%',
            'margin': '5px',
        })
    ], style={
        'display': 'flex',
        'flexDirection': 'row',
        'height': '100%',
        'width': '100%'
    })
