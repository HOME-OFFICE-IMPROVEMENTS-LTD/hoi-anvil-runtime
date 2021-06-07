
from anvil.util import WrappedObject, WrappedList
from anvil.server import serializable_type


@serializable_type
class ErrorX(WrappedObject):
    _name = "ErrorX"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class ErrorY(WrappedObject):
    _name = "ErrorY"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Hoverlabel(WrappedObject):
    _name = "Hoverlabel"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Line(WrappedObject):
    _name = "Line"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Marker(WrappedObject):
    _name = "Marker"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Selected(WrappedObject):
    _name = "Selected"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Stream(WrappedObject):
    _name = "Stream"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Textfont(WrappedObject):
    _name = "Textfont"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Transform(WrappedObject):
    _name = "Transform"
    _module = "plotly.graph_objs.scatter"

@serializable_type
class Unselected(WrappedObject):
    _name = "Unselected"
    _module = "plotly.graph_objs.scatter"


__all__ = [
    'ErrorX',
    'ErrorY',
    'Hoverlabel',
    'Line',
    'Marker',
    'Selected',
    'Stream',
    'Textfont',
    'Transform',
    'Unselected',
    'hoverlabel',
    'marker',
    'selected',
    'unselected',
]

from plotly.graph_objs.scatter import hoverlabel
from plotly.graph_objs.scatter import marker
from plotly.graph_objs.scatter import selected
from plotly.graph_objs.scatter import unselected
