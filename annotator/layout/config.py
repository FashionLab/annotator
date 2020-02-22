import os
import os.path
import dash_html_components as html
import dash_core_components as dcc

ClassUploadStyle = {
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
            }

FolderSelectStyle = {
                'width': '100%',
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


ConfigLayout = html.Div([
        html.H3('Class List'),
        dcc.Upload(
            id='class-upload',
            children=ClassUploadChildren,
            style=ClassUploadStyle,
            multiple=False,
        ),
        html.H3('Data Folder'),
        dcc.Input(
            id='folder-select',
            type='text',
            placeholder='Select folder...',
            value=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'corpus')),
            style=FolderSelectStyle
        ),
        html.Button('Go',
                    id='go-button',
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
    id='config-content'
)
