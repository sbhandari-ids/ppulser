from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, StringField
from wtforms.validators import DataRequired


class EventForm(FlaskForm) :
    event_name = StringField('Event_Name : ', validators=[DataRequired()])
    description = StringField('Description: ', validators=[DataRequired()])
    event_date = StringField('Event_Date: ', validators=[DataRequired()])
    venue = StringField('Venue: ', validators=[DataRequired()])
    start_time = StringField('Start_Time: ', validators=[DataRequired()])
    end_time = StringField('End_Time: ', validators=[DataRequired()])
    event_type = StringField('Event_Type: ', validators=[DataRequired()])
    music_type = StringField('Music_Type: ', validators=[DataRequired()])
    organizer = StringField('Organizer: ', validators=[DataRequired()])
    entry_fees =StringField('Entry_Fees: ', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')
