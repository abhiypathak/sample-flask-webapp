from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Tasks
from app import app, db
from datetime import datetime
import forms


@app.route('/')
@app.route('/index')
def index():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Tasks(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash(message="Task added successfully")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Tasks.query.get(task_id)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash(message="Task updated successfully")
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Tasks.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash(message="Task deleted successfully")
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash(message="Task not found")
    return redirect(url_for('index'))
