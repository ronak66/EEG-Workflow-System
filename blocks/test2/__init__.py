from .AddSub.Addition import Addition
from .AddSub.Subraction import Subraction
from .Constant.Constant import Constant

string_classobject_mapping = {
    Addition.name: Addition(),
    Subraction.name: Subraction(),
    Constant.name: Constant()
}