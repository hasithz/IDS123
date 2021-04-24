from flask import Flask
from flask import render_template, url_for

import tensorflow as tf 
import numpy as np

new_model = tf.keras.models.load_model('save_model')


#input sample data to check prediction
sample = {
    "duration"           : 10,
    "protocol_type"      : 'icmp', 
    "service"            : 'ecr_i', 
    "src_bytes"          : 'SF', 
    "dst_bytes"          : 1, 
    "flag"               : 0, 
    "land"               : 0, 
    'wrong_fragment'     : 0,
    'urgent'             : 0,
    'hot'                : 0,
    'num_failed_logins'  : 0,
    'logged_in'          : 0,
    'num_compromised'    : 0,
    'root_shell'         : 0,
    'su_attempted'       : 0,    
    'num_root'           : 0,
    'num_file_creations' : 1,
    'num_shells'         : 0,
    'num_access_files'   : 0,
    'num_outbound_cmds'  : 0,
    'is_hot_login'       : 0,
    'is_guest_login'     : 0,
    'count'              : 1,
    'serror_rate'        : 0,
    'rerror_rate'        : 0,
    'same_srv_rate'      : 0,
    'diff_srv_rate'      : 0,
    'srv_count'          : 0,
    'srv_serror_rate'    : 0,
    'srv_rerror_rate'    : 0,
    'srv_diff_host_rate' : 1,
    'unknown_data1'      : 0,
    'unknown_data2'      : 0,
    'unknown_data3'      : 0,
    'unknown_data4'      : 0,
    'unknown_data5'      : 0,
    'unknown_data6'      : 0,
    'unknown_data7'      : 0,
    'unknown_data8'      : 0,
    'unknown_data9'      : 0,
    'unknown_data10'     : 0,
#     'results'            : 0,
}


#predicted output
def pre():
  # convertig the sample into tensors
  input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
  # calling the predicrt function to predict the data and pass to the array array size 1
  predictions = new_model.predict(input_dict)
  print(predictions)

  return str(predictions)

# %timeit pre()

asd = pre()

app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello, hello hellooooooo World!"
    # return render_template('index.html')
    return asd

if __name__ == "__main__":
  app.run(debug=True)
