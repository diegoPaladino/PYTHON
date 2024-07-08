from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Reservation {self.name} for {self.date} at {self.time}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        
        if not name or not email or not date or not time:
            flash('Please fill out all fields')
            return redirect(url_for('reserve'))
        
        reservation_date = datetime.strptime(date, '%Y-%m-%d')
        new_reservation = Reservation(name=name, email=email, date=reservation_date, time=time)
        
        try:
            db.session.add(new_reservation)
            db.session.commit()
            flash('Reservation successful')
            return redirect(url_for('index'))
        except:
            flash('Error in reservation process')
            return redirect(url_for('reserve'))
    
    return render_template('reserve.html')

@app.route('/reservations')
def reservations():
    all_reservations = Reservation.query.order_by(Reservation.date).all()
    return render_template('reservations.html', reservations=all_reservations)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
