
from anvil.util import WrappedObject, WrappedList
from anvil.server import serializable_type


@serializable_type
class Concentrationscales(WrappedObject):
    _name = "Concentrationscales"
    _module = "plotly.graph_objs.sankey.link"

@serializable_type
class Hoverlabel(WrappedObject):
    _name = "Hoverlabel"
    _module = "plotly.graph_objs.sankey.link"

@serializable_type
class Line(WrappedObject):
    _name = "Line"
    _module = "plotly.graph_objs.sankey.link"


__all__ = [
    'Concentrationscales',
    'Hoverlabel',
    'Line',
    'hoverlabel',
]

from plotly.graph_objs.sankey.link import hoverlabel
