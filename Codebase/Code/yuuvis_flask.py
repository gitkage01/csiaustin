import flask
from flask import request,Flask, render_template, redirect, url_for, send_from_directory, request
import os
import werkzeug
import werkzeug.utils

from flask import Flask
app = Flask(__name__)

app.add_url_rule(rule="/upload", endpoint="upload", view_func=upload_image, methods=["POST"])
app.add_url_rule(rule="/", endpoint="homepage", view_func=redirect_upload)

def redirect_upload():
    """
    A viewer function that redirects the Web application from the root to a HTML page for uploading an image to get classified.
    The HTML page is located under the /templates directory of the application.
    :return: HTML page used for uploading an image. It is 'upload_image.html' in this exmaple.
    """
    return flask.render_template(template_name_or_list="upload_image.html")


def upload_image():
    """
    Viewer function that is called in response to getting to the 'http://localhost:7777/upload' URL.
    It uploads the selected image to the server.
    :return: redirects the application to a new page for predicting the class of the image.
    """
    #Global variable to hold the name of the image file for reuse later in prediction by the 'CNN_predict' viewer functions.
    global secure_filename
    if flask.request.method == "POST":#Checking of the HTTP method initiating the request is POST.
        img_file = flask.request.files["image_file"]#Getting the file name to get uploaded.
        print(img_file)
        secure_filename = werkzeug.utils.secure_filename(img_file.filename)#Getting a secure file name. It is a good practice to use it.
        img_path = os.path.join(app.root_path, secure_filename)#Preparing the full path under which the image will get saved.
        img_file.save(img_path)#Saving the image in the specified path.

        #Push the file to cloud
        print("Image uploaded successfully.")
        #return flask.redirect(flask.url_for(endpoint="predict"))
        return "File Upload Success!"
    return "Image upload failed."

if __name__ == "__main__":
    app.run()