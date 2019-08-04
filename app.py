# Author Rahul A Thawal
# Importing JSON and Falcon Library
import json

import falcon


# Defining Class
class souledStoreApi:
  # Get Method with Request and Response Parameter
    def on_get(self, req, resp):
        # Using only for Testing Purposes maked by *
        # In Production Code the * will be replaced by the site name
        resp.set_header('Access-Control-Allow-Origin', '*')

        # Artists Data i.e. Artists --> Products
        artists = {
            "Massimo Almond": ["Water & Stain Resistant: Solids Green", "Batman: Classic Logo (Black)"],
            "Cohen Goodman": ["Batman: Logo", "Batman: Classic Logo (Grey)"],
            "Steven Oneil": ["GOT: House Stark (Grey)", "GOT: House Stark (Blue)"]
        }
        # Products Data i.e. Products ---> Categories
        products = [
            {
                "id": "water-resistant-solids-green-tshirt",
                "url": "https://cdn.pixabay.com/photo/2012/04/14/13/51/tee-34004_960_720.png",
                "name": "Water & Stain Resistant: Solids Green",
                "type": "T-shirt",
                "color": "green",
                "price": 10,
                "memprice": 5,
            },
            {
                "id": "batman-classic-logo-black-polo",
                "url": "https://cdn.pixabay.com/photo/2012/04/14/13/51/tee-34001_960_720.png",
                "name": "Batman: Classic Logo (Black)",
                "type": "Polos",
                "color": "black",
                "price": 20,
                "memprice": 10,
            },
            {
                "id": "batman-logo",
                "url": "https://cdn.pixabay.com/photo/2014/04/02/10/23/t-shirt-303669_960_720.png",
                "name": "Batman: Logo",
                "type": "Full sleeves",
                "color": "red",
                "price": 43,
                "memprice": 20,
            },
            {
                "id": "batman-classic-logo-grey-polos",
                "url": "https://cdn.pixabay.com/photo/2012/04/14/13/51/t-shirt-34005_960_720.png",
                "name": "Batman: Classic Logo (Grey)",
                "type": "Polos",
                "color": "grey",
                "price": 22,
                "memprice": 11,
            },
            {
                "id": "got-house-stark-polos",
                "url": "https://cdn.pixabay.com/photo/2012/04/14/13/51/t-shirt-34005_960_720.png",
                "name": "GOT: House Stark (Grey)",
                "type": "Polos",
                "color": "grey",
                "price": 50,
                "memprice": 25,
            },
            {
                "id": "got-house-stack",
                "url": "https://cdn.pixabay.com/photo/2012/04/14/13/51/tee-34002_960_720.png",
                "name": "GOT: House Stark (Blue)",
                "type": "Polos",
                "color": "blue",
                "price": 25,
                "memprice": 15,
            }
        ]

        route_path = str(req.path)
        if route_path.startswith("/fake-api/v1/souledStore/artists"):
            # Logic for /fake-api/v1/souledStore/artists
            # The Response Status 200
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(artists)

        elif route_path.startswith("/fake-api/v1/souledStore/products"):
            # Logic for /fake-api/v1/souledStore/products
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(products)


api = falcon.API()
# End Point at /fake-api/v1/souledStore/artists
api.add_route('/fake-api/v1/souledStore/artists', souledStoreApi())
# End Point at /fake-api/v1/souledStore/products
api.add_route('/fake-api/v1/souledStore/products', souledStoreApi())
