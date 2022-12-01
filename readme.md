## Propose

The propose of this repository is to catorgorize M&M's from photos. I started by training a model in an juypter notebook. Then I used that model in a flask server. The server allows upload of 100x100 images to identify as M&M's.

## To Run

Start by training the model. Everything should work but you will have to update the location of you data since its probably on a different location on you computer.

Then once you have ran the entire notebook you will have a history.pkl file. This is the file that the flask server will run:
```
export FLASK_ENV=development
export FLASK_APP=server.py
flask run
```

Then go to localhost on the port displayed and upload some images from the test directory.