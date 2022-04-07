from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)  
# Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'hello'  # Return the string 'Hello World!' as a response


@app.route('/john')          # The "@" decorator associates this route with the function immediately following
def john():
    return 'hi im john'  # Return the string 'Hello World!' as a response

@app.route('/erik')          # The "@" decorator associates this route with the function immediately following
def erik():
    return 'hi im erik'







if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

