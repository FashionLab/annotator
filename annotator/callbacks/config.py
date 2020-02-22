from copy import deepcopy
from dash.dependencies import Input, Output, State
import dash_html_components as html
from ..layout import ConfigLayout, \
                     MainLayout, \
                     TITLE, \
                     SelectStyle, \
                     ClassUploadChildren, \
                     DataFileChildren, \
                     MainContent, \
                     CONFIG_CONTENT, \
                     MAIN_CONTENT, \
                     CLASS_UPLOAD, \
                     FOLDER_SELECT, \
                     DATA_OUTPUT, \
                     GO_BUTTON
from ..app import app, appConfigure


@app.callback([Output(CONFIG_CONTENT, 'style'),
               Output(MAIN_CONTENT, 'style'),
               Output(MAIN_CONTENT, 'children'),
               Output(CLASS_UPLOAD, 'style'),
               Output(FOLDER_SELECT, 'style'),
               Output(DATA_OUTPUT, 'style'),
               Output(CLASS_UPLOAD, 'children'),
               Output(DATA_OUTPUT, 'children')],
              [Input(CLASS_UPLOAD, 'contents'),
               Input(FOLDER_SELECT, 'value'),
               Input(GO_BUTTON, 'n_clicks'),
               Input(DATA_OUTPUT, 'contents')],
              [State(CLASS_UPLOAD, 'filename'),
               State(DATA_OUTPUT, 'filename')])
def update_output(classes, data_folder, go_button, data_file, classes_filename, data_file_filename):
    if classes is not None:
        appConfigure.setClasses(classes)
        ClassUploadChildren[0] = html.Span(classes_filename)

    if data_folder is not None:
        appConfigure.setDataFolder(data_folder)

    if data_file is not None:
        appConfigure.setDataFile(data_file_filename)
        DataFileChildren[0] = html.Span(data_file_filename)

    if go_button and go_button > appConfigure.count():
        # check if ready
        if appConfigure.classes() and appConfigure.dataFolder():
            ConfigLayout.style['display'] = 'none'
            appConfigure.load()
            return {'display': 'none'}, \
                   {'display': 'flex', 'flexDirection': 'column'}, \
                   MainContent(), \
                   deepcopy(SelectStyle), \
                   deepcopy(SelectStyle), \
                   deepcopy(SelectStyle), \
                   ClassUploadChildren[0], \
                   DataFileChildren[0]

        class_style = deepcopy(SelectStyle)
        if not appConfigure.classes():
            class_style['borderColor'] = 'red'
        else:
            class_style['borderColor'] = 'black'

        data_folder_style = deepcopy(SelectStyle)
        if not appConfigure.dataFolder():
            data_folder_style['borderColor'] = 'red'
        else:
            data_folder_style['borderColor'] = 'black'

        data_file_style = deepcopy(SelectStyle)
        if not appConfigure.dataFile():
            data_file_style['borderColor'] = 'red'
        else:
            data_file_style['borderColor'] = 'black'

    else:
        class_style = deepcopy(SelectStyle)
        data_folder_style = deepcopy(SelectStyle)
        data_file_style = deepcopy(SelectStyle)

    appConfigure.incGoButton(go_button)
    return {'display': 'flex', 'flexDirection': 'column'}, \
           {'display': 'none'}, \
           [], \
           class_style, \
           data_folder_style, \
           data_file_style, \
           ClassUploadChildren[0], \
           DataFileChildren[0]
