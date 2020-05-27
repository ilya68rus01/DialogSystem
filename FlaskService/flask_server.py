#!/usr/bin/env python
# -*- coding: utf-8 -*-
from FlaskService import app
from FlaskService.QAForm import QAForm
from flask import jsonify, request, render_template, flash
#from DialogService.DeepPavlovWrapper import DeepPavlovWrapper


@app.route('/', methods=['GET', 'POST'])
def index():
    form = QAForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.question.data))
        return "form.question.data = form.password"
    return render_template('index.html', title='Home', form=form)


def start():
    app.run(debug=True, host='0.0.0.0', port=8080)

