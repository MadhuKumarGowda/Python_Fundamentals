# pip freeze > requirements.txt
# To install packages from requirements.txt : pip install -r requirements.txt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Instance to get API requests
api = Api(app)

# Defining data model  and schema for API to perform validation and save into database
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User (name = {self.username}, email= {self.email})>'

# Method to validate the request parameters
user_args  = reqparse.RequestParser()
user_args.add_argument("username", type=str, help="Name of the user can not be blank", required=True)
user_args.add_argument("email", type=str, help="Email of the user can not be blank", required=True)

userFields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}

# Defining routes for API
class Users(Resource):
    @marshal_with(userFields)
# Get method to get all users
    def get(self):
        users = UserModel.query.all() # line to get all users data from table
        return users, 200
    @marshal_with(userFields)
# Post method to add new user
    def post(self):
        args = user_args.parse_args()
        user = UserModel(username=args['username'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201


class User(Resource):
    # Get user by id
    @marshal_with(userFields)
    def get(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        return user, 200
    
    #Patch/Update the user data by ID    
    @marshal_with(userFields)
    def patch(self,id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        user.username = args['username']
        user.email = args['email']
        db.session.commit()
        return user, 200
    
    # Delete user by ID
    @marshal_with(userFields)
    def delete(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 200
# Assigning route for API    
api.add_resource(Users, '/api/users') 
api.add_resource(User, '/api/user/<int:id>') 
    

@app.route('/')
def home():
    return '<h1>Welcome to Flask REST API</h1>'

if __name__ == '__main__':
    app.run(debug=True)

