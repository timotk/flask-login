#!env/bin/python
from app import app
import config

app.debug = config.DEBUG
app.run(host=config.IP, port=config.PORT)