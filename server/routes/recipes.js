import express from 'express';

import { getRecipes, createRecipe } from '../controllers/recipes';

const router = express.Router();

router.get('/', getRecipes);
router.post('/', createRecipe);

export default router;