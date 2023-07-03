<script>
  import { SearchIcon } from 'lucide-svelte';
  	import RecipePreview from './recipePreview.svelte';
    let recipe = {
    name: 'Delicious  Recipe',
    image: 'https://img.chefkoch-cdn.de/rezepte/1320901236931593/bilder/967323/crop-960x540/raffaello-creme.jpg',
    categories: ['Breakfast', 'Dessert'],
  };
</script>

<div class="flex justify-center my-10">
  <div class="relative">
    <button class="absolute left-1 top-1/2 transform -translate-y-1/2">
          <SearchIcon class=" text-gray-500" />
    </button>
    <input class="border rounded-xl px-1 py-1 pl-10" type="text" placeholder="recipe" />
  </div>
</div>
<div class=" grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-2">
  {#each {length: 100} as _, i}
    <RecipePreview {recipe}/>
  {/each}
</div>
