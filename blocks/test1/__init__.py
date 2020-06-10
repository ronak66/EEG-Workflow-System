from blocks.test1.AddSub.Addition import Addition
from blocks.test1.AddSub.Subraction import Subraction
from blocks.test1.Constant.Constant import Constant

string_classobject_mapping = {
    Addition.name: Addition(),
    Subraction.name: Subraction(),
    Constant.name: Constant()
}