from flask import Flask  # Flask for web application
import os  # os for accessing environment variables
import socket  # socket for getting the machine's hostname

app = Flask(__name__)  # Create the Flask app instance

@app.route("/")  # Define the root route
def hello():
    html = """Hello {name}!
    Hostname: {hostname}"""
    # Format the HTML with the 'NAME' environment variable and machine hostname
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":  # Run the app if the script is executed directly
    app.run(host='0.0.0.0', port=80)  # Make the app accessible on all network interfaces

