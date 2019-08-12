from app import db


class MarioMoves(db.Model):
    __tablename__ = "mario_moves"

    id = db.Column(db.DateTime, primary_key=True)
    grid = db.Column(db.String)
    moves = db.Column(db.String)
    time = db.Column(db.Float)

    def __repr__(self):
        return "<Moves: {}>".format(self.mario_moves)
