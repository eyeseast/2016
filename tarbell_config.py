# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""
import requests
from flask import Blueprint, g

blueprint = Blueprint('election', __name__)

# Google spreadsheet key
#SPREADSHEET_KEY = "None"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

POLLS = {
    'GOP': 'http://elections.huffingtonpost.com/pollster/api/charts/2016-national-gop-primary',
    'DEM': 'http://elections.huffingtonpost.com/pollster/api/charts/2016-national-democratic-primary'
}

@blueprint.app_context_processor
def get_polls():
    """
    Add polls to context
    """
    context = {}
    for party, url in POLLS.items():
        r = requests.get(url)
        context[party] = r.json()

    return context

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    
    #"production": "",
    #"staging": "",
}

# Default template variables
DEFAULT_CONTEXT = {
    'POLLS': POLLS,
    'title': '2016'
}