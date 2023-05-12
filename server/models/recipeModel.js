import mongoose from "mongoose";

const mealTagSchema = mongoose.Schema({
    tagName: {
        type: String,
        enum: ['breakfast', 'lunch', 'dinner', 'dessert', 'snack'],
        default: 'lunch'
    }
});
const MealTag = mongoose.model("MealTag", mealTagSchema);

const recipeCardSchema = mongoose.Schema({
    recipeCardId: Number,
    title: String,
    mealTag: mealTagSchema,
    tags: [String]
});
const RecipeCard = mongoose.model("RecipeCard", recipeCardSchema);

const recipeSchema = mongoose.Schema({
    coreInfo: recipeCardSchema,
    recipeId: Number,
    ingredients: [{
        quantity: Number,
        ingredient: String
    }],
    instructions: String,
    source: String,
    addedAt: {
        type: Date,
        default: new Date()
    }
});
const Recipe = mongoose.model("Recipe", recipeSchema);

module.exports = {
    RecipeCard: RecipeCard,
    Recipe: Recipe,
    MealTag: MealTag
}