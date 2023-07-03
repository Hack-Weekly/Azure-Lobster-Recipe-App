<script>
  export let recipe = {
    name: 'Delicious Recipe',
    image: 'https://img.chefkoch-cdn.de/rezepte/1320901236931593/bilder/967323/crop-960x540/raffaello-creme.jpg',
    categories: ['Breakfast', 'Dessert'],
  };
</script>

<div class="max-w-xs mx-auto bg-white rounded overflow-hidden shadow-lg">
  <img class="w-full" src="{recipe.image}" alt="Recipe">
  <div class="px-6 py-4">
    <div class="font-bold text-xl mb-2">{recipe.name}</div>
    <div class="flex flex-wrap">
      {#each recipe.categories as category}
        <span class="mr-2 mb-2 p-1 bg-gray-200 text-gray-700 text-sm rounded">{category}</span>
      {/each}
    </div>
  </div>
</div>