from app import db
from sqlalchemy.sql import func

class Code(db.Model):
    uid = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    ip = db.Column(db.String(40), nullable=False)
    code = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    expire_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"<Code {self.uid}>"
