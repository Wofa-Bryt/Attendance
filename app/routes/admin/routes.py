from app.routes.admin import admin
from app.models import teacher, student
from app import db
from flask import render_template, redirect, url_for, flash, request
    

@admin.route('/')
def dashboard():
    try:
        total_lecturers = teacher.query.count()
        total_students = student.query.count()
        return render_template('admin_dashboard.html', total_lecturers=total_lecturers, total_students=total_students)
    except Exception as e:
        flash(f'Error loading dashboard: {e}', 'danger')
        return redirect(url_for('admin.dashboard'))



@admin.route('/lecturers', methods=['GET', 'POST'])
def view_lecturers():
    try:
        users = teacher.query.all()
        return render_template('lectures_view.html', users=users)
    except Exception as e:
        flash(f'Error loading lecturers: {e}', 'danger')
        return redirect(url_for('admin.dashboard'))

@admin.route('/delete_lecturer/<int:id>', methods=['POST'])
def delete_lecturer(id):
    try:
        lecturer = teacher.query.get(id)
        if lecturer:
            db.session.delete(lecturer)
            db.session.commit()
            flash('Lecturer deleted successfully!', 'success')
        else:
            flash('Lecturer not found!', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {e}', 'danger')
    
    return redirect(url_for('admin.view_lecturers'))


@admin.route('/students', methods=['GET', 'POST'])
def students_view():
    try:
        users = student.query.all()
        return render_template('students_view.html', users=users)
    except Exception as e:
        flash(f'Error loading students: {e}', 'danger')
        return redirect(url_for('admin.dashboard'))


@admin.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    try:
        students = student.query.get(id) 
        if student:
            db.session.delete(students)
            db.session.commit()
            flash('Student deleted successfully!', 'success')
        else:
            flash('Student not found!', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {e}', 'danger')
    
    return redirect(url_for('admin.students_view'))  

