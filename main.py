#!/usr/bin/env python
from webapp import app
from config import Config

if __name__ == '__main__':
    app.run(port=8000, host=Config.HOST)
