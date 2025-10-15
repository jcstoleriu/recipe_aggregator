from index import app
import time
from flask import request, redirect, url_for
from datetime import datetime

import sqlite3 as sql
from models import db, Recipe

@app.route('/api/time')
def get_time():
    return {'time': time.time()}


@app.route('/api/recipes')
def get_recipes():
    recipes = Recipe.query.all()
    return [r.as_dict() for r in recipes]


@app.route('/api/recipe/<int:recipe_id>')
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        return recipe.as_dict()
    else:
        #TODO 404 react page
        return {"msg": "404"}


@app.route('/api/recipe/create', methods=['GET', 'POST'])
def make_recipe():
    if request.method == 'POST':
        recipe = Recipe(
            title=request.form["Title"],
            ingredients=request.form["Ingredients"],
            instructions=request.form["Instructions"],
            source=request.form["Sourcce"],
            addedAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(f"api/recipe/{recipe.id}")

    #TODO react 404
    return {"msg": "404"}


@app.route("/api/recipe/<int:recipe_id>/delete", methods=['GET', 'DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe:
        if request.method == 'DELETE':
            db.session.delete(recipe)
            db.session.commit()
            #TODO react deleted page
            return {"msg": "deleted"}
    else:
        #TODO react 404
        return {"msg": "404"}