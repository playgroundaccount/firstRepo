from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get the color from the environment variable, with a default value if not set
    banner_color = os.getenv('BANNER_COLOR', 'blue')
    
    # Render a simple HTML template with a dynamic banner color
    html_template = f'''
    <h1 style="background-color:{banner_color}; padding: 20px; color: white;">
        Hello, Welcome to Your Flask App!
    </h1>
    '''
    
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
