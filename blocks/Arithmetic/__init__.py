from .AddSub.Addition import Addition
from .AddSub.Subtraction import Subtraction
from .Constant.Constant import Constant
from .MultiDiv.Multiplication import Multiplication
from .MultiDiv.Division import Division
from .Graph.Plot import Plot

string_classobject_mapping = {
    Addition.name: Addition(),
    Subtraction.name: Subtraction(),
    Multiplication.name: Multiplication(),
    Division.name: Division(),
    Constant.name: Constant(),
    Plot.name: Plot()
}