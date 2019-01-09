from flask import Flask, request, abort, Blueprint
from flask import current_app
from flask import jsonify


app_bp = Blueprint('', __name__)

###################################
########### APP ROUTES ############
###################################

@app_bp.route('/')
def heartbeat():
    """Return a friendly HTTP greeting."""
    return 'hi!'

@app_bp.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=4000, debug=True)

# [END app]