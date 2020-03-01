from copy import deepcopy
from dash import no_update
from dash.dependencies import Input, Output, State
import dash_html_components as html
from ..layout import ConfigLayout, \
                     MainLayout, \
                     MainLayoutEmpty, \
                     TITLE, \
                     SelectStyle, \
                     ClassUploadChildren, \
                     MainContent, \
                     CONFIG_CONTENT, \
                     MAIN_CONTENT, \
                     CLASS_UPLOAD, \
                     FOLDER_SELECT, \
                     DATA_OUTPUT, \
                     GO_BUTTON, \
                     BRAND_FILTER, \
                     ORDER_DROPDOWN
from ..app import app, appConfigure


@app.callback([Output(CONFIG_CONTENT, 'style'),
               Output(MAIN_CONTENT, 'style'),
               Output(MAIN_CONTENT, 'children'),
               Output(CLASS_UPLOAD, 'style'),
               Output(FOLDER_SELECT, 'style'),
               Output(DATA_OUTPUT, 'style'),
               Output(CLASS_UPLOAD, 'children')],
              [Input(CLASS_UPLOAD, 'contents'),
               Input(FOLDER_SELECT, 'value'),
               Input(GO_BUTTON, 'n_clicks'),
               Input(DATA_OUTPUT, 'value'),
               Input(BRAND_FILTER, 'value'),
               Input(ORDER_DROPDOWN, 'value')],
              [State(CLASS_UPLOAD, 'filename')])
def update_output(classes, data_folder, go_button, data_file_filename, brand_filter, order_dropdown, classes_filename):
    if classes is not None:
        appConfigure.setClasses(classes)
        ClassUploadChildren[0] = html.Span(classes_filename)

    if data_folder is not None:
        appConfigure.setDataFolder(data_folder)

    if data_file_filename is not None:
        appConfigure.setDataFile(data_file_filename)

    if go_button and go_button > appConfigure.count():
        # check if ready
        if appConfigure.classes() and appConfigure.dataFolder():
            if not appConfigure.loaded() or brand_filter != appConfigure.brand_filter() or order_dropdown != appConfigure.order():
                if brand_filter is not None:
                    appConfigure.setBrandFilter(brand_filter)
                if order_dropdown is not None:
                    appConfigure.setOrder(order_dropdown)

                ConfigLayout.style['display'] = 'none'
                appConfigure.load()
                return {'display': 'none'}, \
                    {'display': 'flex', 'flexDirection': 'column'}, \
                    MainContent(), \
                    deepcopy(SelectStyle), \
                    deepcopy(SelectStyle), \
                    deepcopy(SelectStyle), \
                    ClassUploadChildren[0]
            return no_update, no_update, no_update, no_update, no_update, no_update, no_update


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
           MainLayoutEmpty, \
           class_style, \
           data_folder_style, \
           data_file_style, \
           ClassUploadChildren[0]
