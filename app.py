from flask import Flask, request, render_template, jsonify
import base64
from io import BytesIO
from PIL import Image
app = Flask(__name__)

def convert_and_save(b64_string):
    with open("imageToSave.jpg", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        file = request.form['file']
        starter = file.find(',')
        image_data = file[starter+1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        im.save('static/captured/'+request.form['image_name']+'.jpg')
        return jsonify(request.form['image_name'], request.form['file'])

    return render_template('capture.html')

if __name__ == '__main__':
    app.run(debug=True)
