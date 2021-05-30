from flask import Flask
from flask import make_response
import numpy as np
app = Flask(__name__)
@app.route("/")
def corelation():
    # 1 2 3 8 9 7 3 12 65 45 26 33
     firstArray = np.loadtxt("firstfile.txt")
    # 43 32 23 45 65 99 77 11 20 32 65 11 12
     secondArray = np.loadtxt("secondfile.txt")
     corr = np.correlate(firstArray,secondArray, 'full')  
     result = print (corr)  
     # [1.2000e+01 3.5000e+01 1.2300e+02 2.9100e+02 4.7500e+02 8.5000e+02
     # 1.2000e+01 3.5000e+01 1.2300e+02 2.9100e+02 4.7500e+02 8.5000e+02
     # 1.2000e+01 3.5000e+01 1.2300e+02 2.9100e+02 4.7500e+02 8.5000e+02
     # 1.2000e+01 3.5000e+01 1.2300e+02 2.9100e+02 4.7500e+02 8.5000e+02]
     response = make_response(str(corr), 200)
     response.mimetype = 'text/plain'
     return response
if __name__ == "__main__":
    app.run(debug = True)