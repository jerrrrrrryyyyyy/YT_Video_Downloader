from flask import Flask, render_template,redirect,url_for,request
from yt_dlp import YoutubeDL
from pathlib import Path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def download_video():
    video_url = request.form.get('video_url')
    download_options = {
        'format': 'bestvideo[height=1080]+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output folder and filename
    }

    if video_url and request.method == 'POST':
        downloads_path = str(Path.home() / "Downloads")
        try:
            with YoutubeDL(download_options) as video:
                video.download([video_url])
            return redirect(url_for('download_video'))
        except Exception as e:
            print(f"Error downloading video: {e}")
            return render_template('vid.html', error=str(e))

    return render_template('vid.html')

if __name__ == '__main__':
    app.run(debug=True)

