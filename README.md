# Celebrity Media Finder

This web application allows you to upload an image of a celebrity and automatically find related media content including images and videos from various platforms.

## Features

- Upload an image containing a celebrity
- Automatic celebrity recognition using Google Cloud Vision API
- Retrieves related content from:
  - Google Images
  - YouTube
  - Vimeo
  - Dailymotion

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Google Cloud Vision API credentials
- API keys for Google Custom Search, YouTube, and Vimeo

### Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set up Google Cloud Vision API:
   - Create a project in Google Cloud Console
   - Enable the Vision API
   - Create and download service account credentials
   - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to your JSON credentials file:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-credentials.json"
```

### Running the Application

1. Start the Flask web server:

```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

3. Upload an image containing a celebrity and view the results!

## Project Structure

- `app.py` - Main Flask application
- `name.py` - Celebrity detection using Google Cloud Vision
- `urls.py` - Functions to retrieve media from various platforms
- `templates/` - HTML templates for the web interface
- `uploads/` - Directory for uploaded images (created automatically)

## Notes

- The application uses API keys embedded in the code for demonstration purposes only
- For production use, you should store API keys as environment variables or in a secure configuration
- The Google Vision API has usage limits and may incur charges 