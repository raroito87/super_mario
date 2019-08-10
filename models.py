from app import db


class Moves(db.Model):
    __tablename__ = "moves"

    id = db.Column(db.DateTime, primary_key=True)
    moves = db.Column(db.String)
    time = db.Column(db.Float)

    def __repr__(self):
        return "<Moves: {}>".format(self.moves)
