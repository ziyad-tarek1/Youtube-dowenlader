from flask import Flask, render_template, request, redirect, url_for, flash
import os
from yt_dlp import YoutubeDL

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

DOWNLOAD_DIR = 'downloads'

def download_video(url, download_dir):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Download completed successfully for: {url}"
    except Exception as e:
        return f"An error occurred while downloading {url}: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        choice = request.form['choice']
        if choice not in ['1', '2']:
            flash('Invalid choice. Please select 1 or 2.')
            return redirect(url_for('index'))

        result = download_video(url, DOWNLOAD_DIR)
        flash(result)
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    app.run(host='0.0.0.0', port=5000, debug=True)
