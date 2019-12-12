from flask import Flask, render_template, request
from google.cloud import storage
import json
import datetime

with open('config.json') as f:
    config = json.load(f)

app = Flask(__name__)

def generate_PUT_url(blob_name, mimetype):
    """Generates a v4 signed URL for uploading a blob using HTTP PUT.

    Note that this method requires a service account key file. You can not use
    this if you are using Application Default Credentials from Google Compute
    Engine or from the Google Cloud SDK.
    """
    storage_client = storage.Client.from_service_account_json('service-account.json')
    bucket = storage_client.get_bucket(config['BUCKET'])
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version='v4',
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=15),
        # Allow GET requests using this URL.
        method='PUT',
        content_type=mimetype)
    return url


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-signed-url', methods=['POST'])
def get_signed_url():
    fname = request.json['fname']
    mimetype = request.json['mimetype']

    return {
        'url': generate_PUT_url(fname, mimetype)
    }, 200

if __name__ == '__main__':
    app.run(debug=True)
