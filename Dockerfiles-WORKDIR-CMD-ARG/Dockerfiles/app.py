from flask import Flask, render_template
import os
app = Flask(__name__)


# get the environment variable APP_ENVIRONMENT ( defualt to 'dev')
app_environment = os.environ.get('APP_ENVIRONMENT', 'dev')

@app.route('/')
def home():
    # serve different templates based on the environment
    if app_environment == 'dev':
        return render_template('dev.html')
    elif app_environment == 'qa':
        return render_template('qa.html')
    else:
        return "<h1>Unknown environment</h1>"
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
