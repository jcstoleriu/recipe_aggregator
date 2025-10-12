from index import app

@app.route('/')
@app.route('/recipes')
def get_recipes():
    pass