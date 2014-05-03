from app import app
from flask import Flask, render_template, send_from_directory, request, flash,redirect,url_for
from forms import ContactForm
# from app import mail
from emails import send_email
# from emails import follower_notification

app.secret_key = 'development key'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            flash_errors(form)
            return redirect(url_for('index'))
        else:
            subject=form.subject.data
            message=form.name.data+' said '+form.message.data+" form "+form.email.data
            send_email(subject,'doesitmatter',['chetstar@gmail.com'],message)
            flash('Thank you for your message')
            flash_errors(form)
            return redirect(url_for('index'))
    elif request.method == 'GET':
       return render_template('index.html', form=form)


# @app.route("/contact", methods=['GET', 'POST'])
# def contact():
#     form = ContactForm()
#     if request.method == 'POST':
#         if form.validate() == False:
#             flash('All fields are required.')
#             return redirect(url_for('index'))
#         else:
#             return 'Form posted.'
#     elif request.method == 'GET':
#        return render_template('index.html', form=form)
# from emails import follower_notification

# @app.route('/follow/<nickname>')
# @login_required
# def follow(nickname):
#     user = User.query.filter_by(nickname = nickname).first()
#     # ...
#     follower_notification(user, g.user)
#     return redirect(url_for('user', nickname = nickname))