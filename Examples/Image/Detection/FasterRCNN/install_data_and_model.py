# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

from __future__ import print_function
import zipfile
import os, sys

base_folder = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(base_folder, "..", "..", "DataSets", "Grocery"))
from install_grocery import download_grocery_data
download_grocery_data()

sys.path.append(os.path.join(base_folder, "..", "..", "Detection", "utils", "annotations"))
from map_file_helper import create_class_dict, create_map_files
print("Creating mapping files for Grocery data set..")
abs_path = os.path.dirname(os.path.abspath(__file__))
data_set_path = os.path.join(abs_path, r"..\..\DataSets\Grocery")
class_dict = create_class_dict(data_set_path)
create_map_files(data_set_path, class_dict, training_set=True)
create_map_files(data_set_path, class_dict, training_set=False)

sys.path.append(os.path.join(base_folder, "..", "..", "PretrainedModels"))
from models_util import download_model_by_name
download_model_by_name("AlexNet")
