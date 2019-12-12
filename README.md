# Google Cloud Storage Upload Example

1. On your GCP account, create a storage bucket. Put its ID into config.json
2. On your GCP account, create a service account and download its credentials into a file called service-account.json
3. Install a Python 3.7 virtual environment and install requirements.txt.
4. Activate the environment

## Localhost
1. Run `python app.py`
2. Go to 0.0.0.0:5000 and test. After the "File uploaded" alert comes up, check your bucket the file should be there.

## Deployment
1. Update cors file (cors.json) to have correct origins
2. Set CORS policy: `gsutil cors set cors.json gs://<bucket-id>`
3. Deploy GCP project.
