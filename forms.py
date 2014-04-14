from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField, TextAreaField
 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  ref=TextField("Ref")
  message = TextAreaField("Message")
  submit = SubmitField("Send")