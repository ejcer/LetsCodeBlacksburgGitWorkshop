import os
import re
from bottle import route, run

@route('/:path')
def catchall(path=''):
    if re.match(r'^[0-9]+$', path):
      return "Path is numeric" 
    elif re.match(r'^[a-zA-Z]+$', path):
      return "Path is non numeric."
    else:
      return "other"


@route('/')
def index():
    return "Hello World!" 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
