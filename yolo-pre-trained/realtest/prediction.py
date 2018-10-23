import os
from prediction_evaluate import *

result_dir = "/home/sakulaki/code/yolo-pre-trained/darknet/results"
classes = ["ASCUS", "LSIL", "ASCH", "HSIL", "SCC"]

dict_pic_info = get_predictions_result(result_dir, classes)

