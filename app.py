#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from DialogService.app import Test

app = Flask(__name__)


@app.route('/')
def hello_world():
    test = Test("Hello, фцрвамиашфцвим")
    return test.get_text()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
