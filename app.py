from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    return send_from_directory(directory=os.path.join(app.root_path, 'static', 'downloads'),
                               path='AetheriumLauncher.exe',
                               as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
