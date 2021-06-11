from app import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'
