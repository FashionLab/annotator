from dash.dependencies import Input, Output
from ..layout import (
    ITEM_VALID,
    ITEM_AD_TYPE,
    ITEM_VIEW,
    ITEM_SEX,
    ITEM_COLOR,
    ITEM_CLASS,
    ITEM_NOTES,
)
from ..utils import load_image
from ..app import app, appConfigure


@app.callback(
    [
        Output("table", "style_data_conditional"),
        Output("preview", "src"),
        Output(ITEM_VALID, "value"),
        Output(ITEM_CLASS, "value"),
        Output(ITEM_AD_TYPE, "value"),
        Output(ITEM_VIEW, "value"),
        Output(ITEM_SEX, "value"),
        Output(ITEM_COLOR, "value"),
        Output(ITEM_NOTES, "value"),
    ],
    [
        Input("next", "n_clicks"),
        Input("prev", "n_clicks"),
        Input("table", "derived_viewport_row_ids"),
    ],
)
def update_next(next, prev, page):
    if page != appConfigure._current_page:
        appConfigure._selected = 0
        appConfigure._current_page = page

    if next and next > appConfigure._next_clicks:
        appConfigure._next_clicks = next
        appConfigure._selected = min(
            appConfigure._selected + 1, len(appConfigure._current_page) - 1
        )

    if prev and prev > appConfigure._prev_clicks:
        appConfigure._prev_clicks = prev
        appConfigure._selected = max(appConfigure._selected - 1, 0)

    selected = (appConfigure._current_page or [0])[appConfigure._selected]

    return (
        [
            {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"},
            {
                "if": {"row_index": appConfigure._selected},
                "backgroundColor": "rgb(255, 0, 0)",
            },
        ],
        load_image(appConfigure.files(selected)["path"])
        if appConfigure.files()
        else "",
        appConfigure.loadRecord("valid"),
        appConfigure.loadRecord("class"),
        appConfigure.loadRecord("ad"),
        appConfigure.loadRecord("view"),
        appConfigure.loadRecord("sex"),
        appConfigure.loadRecord("color"),
        appConfigure.loadRecord("notes"),
    )


@app.callback(
    [Output("hidden-div1", "value")],
    [
        Input(ITEM_VALID, "value"),
        Input(ITEM_CLASS, "value"),
        Input(ITEM_AD_TYPE, "value"),
        Input(ITEM_VIEW, "value"),
        Input(ITEM_SEX, "value"),
        Input(ITEM_COLOR, "value"),
        Input(ITEM_NOTES, "value"),
    ],
)
def update_data(
    item_valid, item_class, item_ad_type, item_view, item_sex, item_color, item_notes
):
    if item_valid is not None:
        appConfigure.storeRecord("valid", item_valid)

    if item_class is not None:
        appConfigure.storeRecord("class", item_class)

    if item_ad_type is not None:
        appConfigure.storeRecord("ad", item_ad_type)

    if item_view is not None:
        appConfigure.storeRecord("view", item_view)

    if item_sex is not None:
        appConfigure.storeRecord("sex", item_sex)

    if item_color is not None:
        appConfigure.storeRecord("color", item_color)

    if item_notes is not None:
        appConfigure.storeRecord("notes", item_notes)

    return [""]
