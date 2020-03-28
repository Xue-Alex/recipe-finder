from app import app
from flask import render_template
from app.forms import SearchForm
from app.find_recipes import find_matching_recipes, get_one_recipe

@app.route('/info')
def info():
    return render_template('index.html', title = "Home")

@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.add_entry.data:
        form.ingredients.append_entry()
        return render_template('search.html', form=form)
    if form.remove_entry.data:
        form.ingredients.pop_entry()
        return render_template('search.html', form=form)
    if form.validate_on_submit():
        recipes= find_matching_recipes(form.ingredients.data)
        return render_template('recipe_display.html', recipes=recipes)
    return render_template('search.html', form=form)


@app.route("/recipe/<title>")
def recipe_title(title):
    recipe = get_one_recipe(title)
    return render_template('recipe_detail.html',recipe=recipe)
