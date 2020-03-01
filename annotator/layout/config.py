import os
import os.path
import dash_html_components as html
import dash_core_components as dcc

SelectStyle = {
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'borderColor': 'black',
                'textAlign': 'center',
            }

ClassUploadChildren = [html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ])]

CONFIG_CONTENT = 'config-content'
CLASS_UPLOAD = 'class-upload'
FOLDER_SELECT = 'folder-select'
DATA_OUTPUT = 'data-output'
GO_BUTTON = 'go-button'

ConfigLayout = html.Div([
        html.H3('Class List'),
        dcc.Upload(
            id=CLASS_UPLOAD,
            children=ClassUploadChildren,
            style=SelectStyle,
            multiple=False,
        ),
        html.H3('Data Folder'),
        dcc.Input(
            id=FOLDER_SELECT,
            type='text',
            placeholder='Select folder...',
            value=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'corpus')),
            style=SelectStyle
        ),
        html.H3('Data Output File'),
        dcc.Input(
            id=DATA_OUTPUT,
            type='text',
            placeholder='Select output...',
            value=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'corpus', 'data.csv')),
            style=SelectStyle
        ),
        html.Button('Go',
                    id=GO_BUTTON,
                    style={
                        'marginTop': '1.5rem',
                        'marginLeft': 'auto',
                        'marginRight': 'auto',
                    }
        ),
    ],
    style={
    'display': 'flex',
    'flexDirection': 'column',
    'margin': '10px'
    },
    id=CONFIG_CONTENT
)
