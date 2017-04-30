
import ipywidgets as widgets

from traitlets import Unicode, Instance

from .maps import Map
from .toolbar import Toolbar


class Figure(widgets.DOMWidget):
    _view_name = Unicode("FigureView").tag(sync=True)
    _view_module = Unicode("jupyter-gmaps").tag(sync=True)
    _model_name = Unicode("FigureModel").tag(sync=True)
    _model_module = Unicode("jupyter-gmaps").tag(sync=True)
    _toolbar = Instance(Toolbar, allow_none=True, default=None).tag(
        sync=True, **widgets.widget_serialization)
    _map = Instance(Map).tag(sync=True, **widgets.widget_serialization)

    def add_layer(self, layer):
        self._map.add_layer(layer)


def figure(show_toolbar=True):
    _map = Map()
    _toolbar = Toolbar() if show_toolbar else None
    return Figure(_map=_map, _toolbar=_toolbar)
