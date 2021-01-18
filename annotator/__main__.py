# -*- coding: utf-8 -*-
import sys
from .app import app
from .layout import MAIN, TITLE, CONTENT, ConfigLayout, MainLayout
from .callbacks import *  # noqa: F401

if __name__ == "__main__":
    app.layout = MAIN
    CONTENT[:] = [TITLE, ConfigLayout, MainLayout]
    app.run_server(debug="prod" not in sys.argv)
