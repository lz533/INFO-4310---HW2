from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app,
                          root='public_site/',
                          prefix='',
                          index_file="index.htm",
                          autorefresh=True)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
