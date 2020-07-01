from .AddSub.Addition import Addition
from .AddSub.Subraction import Subraction
from .Constant.Constant import Constant
from .MultiDiv.Multiplication import Multiplication
from .MultiDiv.Division import Division

string_classobject_mapping = {
    Addition.name: Addition(),
    Subraction.name: Subraction(),
    Multiplication.name: Multiplication(),
    Division.name: Division(),
    Constant.name: Constant()
}