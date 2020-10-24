# from app import db
#
# from datetime import datetime


# # flask-socketio generates a uuid4 for its sid in hex form, and according
# # to python docs that uses 32 characters
# SID_LENGTH = 32
#
# GAME_CODE_LENGTH = 4
#
# # Arbitrary number. TODO Align with Marc
# PLAYER_NAME_LENGTH = 20
#
#
# class Game(db.Model):
#
#     id = db.Column(db.Integer, primary_key=True)
#     code = db.Column(db.String(GAME_CODE_LENGTH), unique=True, nullable=False)
#     host_sid = db.Column(db.String(SID_LENGTH), nullable=True)
#     last_activity = db.Column(
#         db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
#     )
#
#     @staticmethod
#     def create():
#         game = Game(code=Game.random_code())
#         db.session.add(game)
#         db.session.commit()
#
#         return game
#
#     @staticmethod
#     def get(unsanitized_code):
#         return Game(code=unsanitized_code)
#
#     @staticmethod
#     def random_code():
#         """
#         Generate a random code for the game.
#         Currenty 62^4 = 14.7 Milion different combinations
#         """
#
#         alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#
#         return "".join(map(lambda x: random.choice(alphabet), range(GAME_CODE_LENGTH)))
#
#     def is_valid(self):
#         return self.host_sid is not None
#
#     def to_dict(self):
#         return {
#             "code": self.code,
#             "players": [player.to_dict() for player in self.players],
#         }
#
#
# class Player(db.Model):
#
#     id = db.Column(db.Integer, primary_key=True)
#     sid = db.Column(db.String(SID_LENGTH), unique=True, nullable=False)
#     name = db.Column(db.String(PLAYER_NAME_LENGTH), nullable=False)
#     last_activity = db.Column(
#         db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
#     )
#
#     game_id = db.Column(db.Integer, db.ForeignKey("game.id"), nullable=False)
#
#     game = db.relationship(
#         "Game",
#         lazy="joined",
#         backref=db.backref("players", lazy="select", cascade="all, delete-orphan"),
#     )
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#         }
#
#
# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.Text)
#
#     @staticmethod
#     def get_random():
#         # import ipdb; ipdb.set_trace()
#         # Horrible inefficient method, TODO: fix it eventualy
#         index = random.randrange(0, Question.query.count()) + 1
#         return Question.query.get(index)
#
#
# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     answer = db.Column(db.Text, nullable=True)
#
#     game_id = db.Column(db.Integer, db.ForeignKey("game.id"), nullable=False)
#     game = db.relationship(
#         "Game",
#         lazy="joined",
#         backref=db.backref("answers", lazy="select", cascade="all, delete-orphan"),
#     )
#
#     player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
#     player = db.relationship(
#         "Player",
#         lazy="joined",
#         backref=db.backref("answers", lazy="select", cascade="all, delete-orphan"),
#     )
#
#     question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
#     question = db.relationship(
#         "Question",
#         lazy="joined",
#         backref=db.backref("answers", lazy="select", cascade="all, delete-orphan"),
#     )
#
#     def is_answered(self):
#         return self.answer != ""
#
