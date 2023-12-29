from flask import Flask

import config
import init

app = Flask(__name__, template_folder=config.TEMPLATE_FOLDER_PATH)