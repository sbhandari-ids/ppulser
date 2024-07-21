@app.route('/events', methods = ['GET','POST'])
def events():
       form = EventForm()
       if request.method == 'POST': 
         event_name = form.event_name.data
         description = form.description.data
         event_date = form.event_date.data
         venue = form.venue.data
         start_time = form.start_time.data
         end_time = form.end_time.data
         event_type = form.event_type.data
         music_type = form.music_type.data
         organizer = form.organizer.data
         entry_fees = form.entry_fees.data

         new_event=Event(event_name, description, event_date, venue, start_time, end_time, event_type, music_type, organizer, entry_fees)

         new_event.save()
         

         flash("Successfully created new event")
         return redirect(url_for('/events'))
       else: 
         return render_template('enterEvents.html', form=form)


@app.route('/efeed')
def efeed():
   events = events.query.all()
   return render_template('efeed.html', events=events)


@app.route('/edit_event/<event_id>', methods =['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get(event_id)
    form = EventForm()
    if request.method == 'POST' and form.validate_on_submit():
         event.event_name = form.event_name.data
         event.description = form.description.data
         event.event_date = form.event_date.data
         event.venue = form.venue.data
         event.start_time = form.start_time.data
         event.end_time = form.end_time.data
         event.event_type = form.event_type.data
         event.music_type = form.music_type.data
         event.organizer = form.organizer.data
         event.entry_fees = form.entry_fees.data

         event.save()

         flash('Event is Updated !')
        
         return redirect(url_for('app.efeed'))
    else :
        return render_template('edit_event.html', form=form, event=event)


    
@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    event = Event.query.get(event_id)
    
    
    db.session.delete(event)
    db.session.commit()
    flash(f'Event {event_id} Successfully Deleted', 'warning')
        
    return redirect(url_for('app.efeed'))
   