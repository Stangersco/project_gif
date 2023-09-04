from check_status import check_server_status
from flask import Flask, send_from_directory, jsonify
from flask import render_template, request, redirect, url_for
import requests
import os

GIF_FOLDER = os.getcwd()
GIF_FOLDER = os.path.split(GIF_FOLDER)[0]
GIF_FOLDER = os.path.join(GIF_FOLDER, 'backend')
GIF_FOLDER = os.path.join(GIF_FOLDER, 'gif_save')


app = Flask(__name__)


def clear():
    directory = os.path.join(os.getcwd(), 'temp')
    if os.listdir(directory):
        for i in os.listdir(directory):
            os.remove(os.path.join(directory, i))


@app.route('/')
@app.route('/home')
@app.route('/home/<gif_name>')
def home(gif_name=''):
    clear()
    return render_template('main.html', gif_name=gif_name)


@app.route('/uploadFiles', methods=['GET', 'POST'])
def gif_creator_func():
    if request.method == 'POST':
        image_list = []
        for i in request.files.getlist('photo'):
            if not i.filename:
                return redirect(url_for('home'))

            directory = f'temp/{i.filename}'
            i.save(directory)
            image_list.append(directory)


        files = [("files", open(file_path, "rb")) for file_path in image_list]

        response = requests.post('http://127.0.0.1:8000/uploadfiles/', files=files)

        return redirect(url_for('home', gif_name=response.json()))

    return redirect('/home')




@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename=''):
    if not filename:
        return
    return send_from_directory(GIF_FOLDER, filename)


@app.route('/check')
def check():
    return jsonify({'key': check_server_status()[0]})
