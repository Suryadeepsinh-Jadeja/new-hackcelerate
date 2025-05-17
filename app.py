from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from werkzeug.utils import secure_filename
from name import detect_top_celebrity_name
from urls import (get_google_image_urls, get_youtube_video_urls, 
                get_vimeo_video_urls, get_dailymotion_video_urls)

app = Flask(__name__)
app.secret_key = 'celebrity_search_app'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Detect celebrity name from uploaded image
            celebrity_name = detect_top_celebrity_name(filepath)
            
            # Get URLs
            num_images = 10
            num_videos = 5
            
            image_urls = get_google_image_urls(celebrity_name, total_num=num_images)
            youtube_urls = get_youtube_video_urls(celebrity_name, max_results=num_videos)
            vimeo_urls = get_vimeo_video_urls(celebrity_name, max_results=num_videos)
            dailymotion_urls = get_dailymotion_video_urls(celebrity_name, max_results=num_videos)
            
            # Store results in session
            session['celebrity_name'] = celebrity_name
            session['image_urls'] = image_urls
            session['youtube_urls'] = youtube_urls
            session['vimeo_urls'] = vimeo_urls
            session['dailymotion_urls'] = dailymotion_urls
            
            return redirect(url_for('results'))
        
        except Exception as e:
            flash(f'Error processing image: {str(e)}')
            return redirect(url_for('index'))

@app.route('/results')
def results():
    # Get results from session
    celebrity_name = session.get('celebrity_name', 'Unknown')
    image_urls = session.get('image_urls', [])
    youtube_urls = session.get('youtube_urls', [])
    vimeo_urls = session.get('vimeo_urls', [])
    dailymotion_urls = session.get('dailymotion_urls', [])
    
    return render_template('results.html', 
                           celebrity_name=celebrity_name,
                           image_urls=image_urls,
                           youtube_urls=youtube_urls,
                           vimeo_urls=vimeo_urls,
                           dailymotion_urls=dailymotion_urls)

if __name__ == '__main__':
    app.run(debug=True) 