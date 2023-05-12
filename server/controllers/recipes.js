import {Recipe, RecipeCard} from '../models/recipeModel.js';

export const getRecipes = async (req, res) => {
    try {
        const getRecipeCards = await RecipeCard.find();
        console.log(getRecipeCards);

        res.status(200).json(getRecipeCards);
    } catch (error) {
        res.status(404).json({message: error.message});
    }
}

export const createRecipe = async (req, res) => {
    const body = req.body;
    const newRecipe = new RecipeCard(body);
    try {
        await newRecipe.save();

        res.status(201).json(newRecipe);
    } catch (error) {
        res.status(400).json({message: error.message})
    }
}