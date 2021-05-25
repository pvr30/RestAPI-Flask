from flask import Flask, views
from flask_restful import Api, Resource, abort, marshal_with, reqparse, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#SQLALCHEMY_TRACK_MODIFICATIONS = False

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

#db.create_all()

#For Create
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name Of The Video Is Required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes Of The Video Is Required", required=True)
video_put_args.add_argument("views", type=int, help="Views On The Video Is Required", required=True)

# For Update 
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name Of The Video Is Required")
video_update_args.add_argument("likes", type=int, help="Likes Of The Video Is Required")
video_update_args.add_argument("views", type=int, help="Views On The Video Is Required")

resource_field = {
    'id':fields.Integer,
    'name':fields.String,
    'likes':fields.Integer,
    'views':fields.Integer,
}

class Video(Resource):
    @marshal_with(resource_field)  # Serialize the object
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could Not Find Video With that Id')
        return result
        
    @marshal_with(resource_field)  
    def put(self,video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(404, message="Video Already Taken.....")
        video = VideoModel(id=video_id, name=args['name'], likes=args['likes'], views=args['views'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_field)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Video does\'t exists, cannot update')

        if args['name']:
            result.name = args['name']
        if args['likes']:
            result.name = args['likes']
        if args['views']:
            result.name = args['views']

        db.session.commit()

        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            db.session.delete(result)
            db.session.commit()
        return 'Deleted Successfully', 204

api.add_resource(Video, '/video/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)