#!/usr/bin/env python
# -*- coding: utf-8 -*-
from FlaskService import app
from FlaskService.QAForm import QAForm
from flask import jsonify, request, render_template, flash
from DialogService.DeepPavlovWrapper import DeepPavlovWrapper

class Server:
    def __init__(self):
        self.wrapper = DeepPavlovWrapper()

    @app.route('/', methods=['GET', 'POST'])
    def index(self):
        form = QAForm()
        if form.validate_on_submit():
            flash('Login requested for user {}'.format(
                form.question.data))
            question = form.question.data
            answer = self.wrapper.get_answer_on_question(question)
            return answer
        return render_template('index.html', title='Home', form=form)

    def start(self):
        app.run(debug=True, host='0.0.0.0', port=8080)

