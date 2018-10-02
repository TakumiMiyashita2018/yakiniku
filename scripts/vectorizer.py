from sklearn.feature_extraction import FeatureHasher
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
import pandas as pd


def vec_general(gen):
    list = []
    list.append(gen["file_size"])
    list.append(gen["vsize"])
    list.append(gen["has_debug"])
    list.append(gen["exports"])
    list.append(gen["imports"])
    list.append(gen["has_relocations"])
    list.append(gen["has_resources"])
    list.append(gen["has_signature"])
    list.append(gen["has_tls"])
    list.append(gen["symbols"])
    return list

def vec_header(head):
    list = []
    list.append(head["timestamp"])
#   machine
#   characteristics
#   subsystem
#   dll_characteristics
#   magic
    list.append(head["major_image_version"])
    list.append(head["minor_image_version"])
    list.append(head["major_linker_version"])
    list.append(head["minor_linker_version"])
    list.append(head["major_operating_system_version"])
    list.append(head["minor_operating_system_version"])
    list.append(head["major_subsystem_version"])
    list.append(head["minor_subsystem_version"])
    list.append(head["sizeof_code"])
    list.append(head["sizeof_headers"])
    list.append(head["sizeof_heap_commit"])
    return list

# def vec_imports(imports):

# def vec_exports(exports):

# def vec_section(sec):
