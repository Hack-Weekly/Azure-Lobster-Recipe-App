<script>
	import { SearchIcon, RotateCw } from 'lucide-svelte';
	import RecipePreview from '$lib/components/recipePreview.svelte';
	import { onMount } from 'svelte';

	let recipes = [];
	let isLoading = false;

	function loadMoreRecipes() {
		isLoading = true;

		// dummy api call (just a timeout for now)
		setTimeout(() => {
			// Generate some dummy recipes
			const newRecipes = Array.from({ length: 10 }, (_, i) => ({
				name: `Recipe ${recipes.length + i + 1}`,
				categories: ['Breakfast', 'Dessert', 'Food', 'Vegan'],
				image: 'example.png'
			}));

			recipes = [...recipes, ...newRecipes];
			isLoading = false;
		}, 5000);
	}

	onMount(() => {
		// Initial load of recipes
		loadMoreRecipes();
	});

	function handleScroll() {
		const { scrollTop, clientHeight, scrollHeight } = document.documentElement;

		if (scrollTop + clientHeight >= scrollHeight - 100 && !isLoading) {
			loadMoreRecipes();
		}
	}

	window.addEventListener('scroll', handleScroll);
</script>

<div class="flex justify-center my-10">
	<div class="relative">
		<button class="absolute left-1 top-1/2 transform -translate-y-1/2">
			<SearchIcon class="text-gray-500" />
		</button>
		<input class="border rounded-xl px-1 py-1 pl-10" type="text" placeholder="recipe" />
	</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-2">
	{#each recipes as recipe}
		<RecipePreview {recipe} />
	{/each}
</div>
{#if isLoading}
	<div class="flex justify-center my-4 flex-row">
		<span class="">Loading...</span><RotateCw class="animate-spin" />
	</div>
{/if}
