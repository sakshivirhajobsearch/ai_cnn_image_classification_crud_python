from flask import Flask, render_template, request, redirect, url_for
import os
import database
import model

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

database.init_db()
cnn_model = model.load_model()

@app.route('/')
def index():
    images = database.get_all_images()
    return render_template("index.html", images=images)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            label = model.predict_image(cnn_model, filepath)
            database.add_image(file.filename, label)
            return redirect(url_for('index'))
    return render_template("upload.html")

@app.route('/update/<int:image_id>', methods=['GET', 'POST'])
def update(image_id):
    img_data = database.get_image(image_id)
    if request.method == 'POST':
        new_label = request.form['label']
        database.update_image(image_id, new_label)
        return redirect(url_for('index'))
    return render_template("update.html", image=img_data)

@app.route('/delete/<int:image_id>')
def delete(image_id):
    database.delete_image(image_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
