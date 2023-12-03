from app.bcrypt_extension import bcrypt
from app.models import User
from app.database import db

def get_user(email):
	user = User.query.filter_by(email = email).first()
	return user

def create_user(email, user_password):
	user = User.query.filter_by(email = email).first()
	if(user):
		return 409
	password = bcrypt.generate_password_hash(user_password).decode('utf-8')
	new_user = User(email = email, password = password)
	db.session.add(new_user)
	db.session.commit()
	return 200

def load_user(user_id):
	user = User.query.filter_by(id = int(user_id)).first()
	return user
