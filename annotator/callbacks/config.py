from dash.dependencies import Input, Output, State
import dash_html_components as html
from ..layout import ConfigLayout, MainLayout, TITLE, ClassUploadStyle, FolderSelectStyle, ClassUploadChildren
from ..app import app, appConfigure


@app.callback([Output('config-content', 'style'),
               Output('main-content', 'style'),
               Output('class-upload', 'style'),
               Output('folder-select', 'style'),
               Output('class-upload', 'children')],
              [Input('class-upload', 'contents'),
               Input('folder-select', 'value'),
               Input('go-button', 'n_clicks')],
              [State('class-upload', 'filename')])
def update_output(classes, data_folder, go_button, classes_filename):
    if classes is not None:
        appConfigure.setClasses(classes)
        ClassUploadChildren[0] = html.Span(classes_filename)

    if data_folder is not None:
        appConfigure.setDataFolder(data_folder)

    if go_button and go_button > appConfigure.count():
        # check if ready
        if appConfigure.classes() and appConfigure.dataFolder():
            ConfigLayout.style['display'] = 'none'
            print('here!!!!')
            return {'display': 'none'}, \
                   {'display': 'flex', 'flexDirection': 'column'}, \
                   ClassUploadStyle, \
                   FolderSelectStyle, \
                   ClassUploadChildren[0]

        if not appConfigure.classes():
            ConfigLayout.children[1].style['borderColor'] = 'red'
        else:
            ConfigLayout.children[1].style['borderColor'] = 'black'

        if not appConfigure.dataFolder():
            ConfigLayout.children[3].style['borderColor'] = 'red'
        else:
            ConfigLayout.children[3].style['borderColor'] = 'black'

    appConfigure.incGoButton(go_button)
    return {'display': 'flex', 'flexDirection': 'column'}, \
           {'display': 'none'}, \
           ClassUploadStyle, \
           FolderSelectStyle, \
           ClassUploadChildren[0]
