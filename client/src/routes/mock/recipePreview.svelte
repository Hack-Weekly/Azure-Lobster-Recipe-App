<script>
	export let recipe = {
		name: 'Delicious Recipe',
		image: 'https://img.chefkoch-cdn.de/rezepte/1320901236931593/bilder/967323/crop-960x540/raffaello-creme.jpg',
		categories: ['Breakfast', 'Dessert']
	};
	import { ImageOff } from 'lucide-svelte';
</script>

<div class="max-w-xs mx-auto bg-white rounded overflow-hidden shadow-lg">
	<div class="aspect-video">
		<img
			class="object-cover object-center w-full h-full"
			src={recipe.image}
			alt="Recipe"
			onerror="this.style.display='none'"
		/>
		<div class="flex justify-center items-center w-full h-full bg-stone-300">
			<ImageOff />
		</div>
	</div>
	<div class="px-6 py-4">
		<div class="font-bold text-xl mb-2">{recipe.name}</div>
		<div class="flex flex-wrap">
			{#each recipe.categories as category}
				<button
					class="mr-2 mb-2 p-1 hover:border-sky-500 border-2 border-gray-200 bg-gray-200 text-gray-700 text-sm rounded"
					>{category}</button
				>
			{/each}
		</div>
	</div>
</div>
