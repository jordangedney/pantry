#!flask/bin/python
# Keep .pyc files from being generated
import sys
sys.dont_write_bytecode = True

from app import app
app.run(debug = True, host='0.0.0.0', port=80)
#app.run(debug = True, host = '0.0.0.0', port = 80)

