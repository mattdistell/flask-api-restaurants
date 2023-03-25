from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse



app = Flask(__name__)
api = Api(app)



location_put_args = reqparse.RequestParser()
location_put_args.add_argument("city", type=str, help="Name of city is required", required=True)
location_put_args.add_argument("restaurant", type=str, help="Restaurant of city", required=True)
location_put_args.add_argument("rating", type=int, help="Rating of city", required=True)

restaurants = {}

# names = {"Matt": {"age": 21, "gender": "male"},
#         "Bill" : {"age": 70, "gender": "male"}}

def abort_if_restaurant_id_not_exist(restaurant_id):
    if restaurant_id not in restaurants:
        abort("restaurant_id is not valid. . .")


class Travel(Resource):
    def get(self, restaurant_id):
        return restaurants[restaurant_id]

    def put(self, restaurant_id):
        args = location_put_args.parse_args()
        restaurants[restaurant_id] = args
        return restaurants[restaurant_id], 201


api.add_resource(Travel, "/travel/<int:restaurant_id>")



if __name__ == "__main__":
    app.run(debug=True)