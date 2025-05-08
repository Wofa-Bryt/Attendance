from app.models import teacher, student
from app.forms import Teacher, Choice, Student
from app.routes.main import main
from app import db
from flask import render_template, redirect, url_for, flash

@main.route('/', methods=['GET', 'POST'])
def home():
    form = Choice()
    form.choice.choices = [('', 'Select your role'), ('Student', 'Student'), ('Lecturer', 'Lecturer')]
    if form.validate_on_submit():
        selected_role = form.choice.data
        if selected_role == 'Student':
            return redirect(url_for('main.student_page'))
        elif selected_role == 'Lecturer':
            return redirect(url_for('main.teacher_page'))
    return render_template('index.html', form=form)

@main.route('/teacher', methods=['GET', 'POST'])
def teacher_page():
    form = Teacher()
    if form.validate_on_submit():
        try:
            phone_number = form.phone.data
            if len(phone_number) != 10 or not phone_number.isdigit():
                flash('Phone number must be exactly 10 digits.', 'warning')
                return render_template('Lecturer.html', form=form)

            existing_teacher = teacher.query.filter_by(phone=phone_number).first()
            if existing_teacher:
                existing_teacher.attend = True
                existing_teacher.times_present += 1
                db.session.commit()
                flash('Attendance updated successfully for Lecturer!', 'success')
            else:
                user = teacher(
                    name=form.name.data,
                    phone=phone_number,
                    course_code=form.course_code.data,
                    attend=True,
                    times_present=1
                )
                db.session.add(user)
                db.session.commit()
                flash('Attendance successfully taken for Lecturer!', 'success')
            return redirect(url_for('main.home'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error occurred: {e}', 'danger')

    return render_template('Lecturer.html', form=form)

@main.route('/student', methods=['GET', 'POST'])
def student_page():
    form = Student()
    if form.validate_on_submit():
        try:
            phone_number = form.phone.data
            index_number = form.index_num.data

            if len(phone_number) != 10 or not phone_number.isdigit():
                flash('Phone number must be exactly 10 digits.', 'warning')
                return render_template('Student.html', form=form)

            if len(index_number) != 13:
                flash('Index number must be exactly 13 characters.', 'warning')
                return render_template('Student.html', form=form)

            existing_student = student.query.filter_by(phone=phone_number).first()
            if existing_student:
                existing_student.attend = True
                existing_student.times_present += 1
                db.session.commit()
                flash('Attendance updated successfully for Student!', 'success')
            else:
                user = student(
                    name=form.name.data,
                    phone=phone_number,
                    faculty_class=form.faculty_class.data,
                    index_num=index_number,
                    attend=True,
                    times_present=1
                )
                db.session.add(user)
                db.session.commit()
                flash('Attendance successfully taken for Student!', 'success')

            return redirect(url_for('main.home'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error occurred: {e}', 'danger')

    return render_template('Student.html', form=form)







