from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Download route
@app.route('/download')
def download():
    downloads_dir = os.path.join(app.root_path, 'static', 'downloads')
    
    # Get the first file in the downloads directory
    files = os.listdir(downloads_dir)
    if not files:
        return "No file available for download.", 404

    latest_file = files[0]  # or pick the first file
    return send_from_directory(directory=downloads_dir, path=latest_file, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)