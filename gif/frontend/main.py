from check_status import check_server_status
from flask import Flask, send_from_directory, jsonify, session
from flask import render_template, request, redirect, url_for
import requests
import os


GIF_FOLDER = os.getcwd()
GIF_FOLDER = os.path.split(GIF_FOLDER)[0]
GIF_FOLDER = os.path.join(GIF_FOLDER, 'backend')
GIF_FOLDER = os.path.join(GIF_FOLDER, 'gif_save')

FORMAT_FILES = ['png', 'jpeg', 'jpg', 'tiff']

app = Flask(__name__)
app.secret_key = 'giff'


def clear():
    directory = os.path.join(os.getcwd(), 'temp')
    if os.listdir(directory):
        for i in os.listdir(directory):
            os.remove(os.path.join(directory, i))


@app.route('/')
@app.route('/main')
def home():
    clear()
    gif_name = session.get('gif_name')
    error = session.get('errormessage')

    #clear gif_name, errormessage after reload.
    session['gif_name'] = ''
    session['errormessage'] = ''

    return render_template('main.html', gif_name=gif_name, errormessage=error)


@app.route('/uploadFiles', methods=['GET', 'POST'])
def gif_creator_func():
    global image_list
    if request.method == 'POST':
        image_list = []
        for i in request.files.getlist('photo'):
            if not i.filename or check_server_status()[0]=='offline':
                session['gif_name'] = ''
                session['errormessage'] = 'No files or server offline'
                return redirect(url_for('home'))

            if i.filename.rsplit('.', 1)[-1] not in FORMAT_FILES:
                session['errormessage'] = 'Unreadable file extension'
                return redirect(url_for('home'))

            directory = f'temp/{i.filename}'
            i.save(directory)
            image_list.append(directory)


        files = [("files", open(file_path, "rb")) for file_path in image_list]

        response = requests.post('http://127.0.0.1:8000/uploadfiles/', files=files)

        session['gif_name'] = response.json()

        return redirect(url_for('home'))

    return redirect('/main')


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename=''):
    if not filename:
        return
    return send_from_directory(GIF_FOLDER, filename)


@app.route('/check')
def check():
    return jsonify({'key': check_server_status()[0]})


# launch server
if __name__ == '__main__':
    app.run()