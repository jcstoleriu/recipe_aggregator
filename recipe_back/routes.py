from index import app
import time

@app.route('/api/time')
def get_recipes():
    return {'time': time.time()}