<script>
	export let links = [
		{ url: './mock', text: 'subpage1' },
	];;
  import { ChefHat } from 'lucide-svelte';
</script>

<nav class="bg-black text-white mb-2">
	<div class="container mx-auto px-4 py-2 flex justify-between items-center">
		<div class="flex items-center">
			<ChefHat class="h-8 w-8 mr-2"/>
			<span class="font-bold text-lg">Recipes</span>
		</div>
		<!-- Nav Links -->
		<div class="space-x-4">
			{#each links as link}
				<a href={link.url} class="text-white hover:text-gray-300">{link.text}</a>
			{/each}
		</div>
	</div>
</nav>
