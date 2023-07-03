<script>
	import Navbar from './navbar.svelte';
	const links = [
		{ url: './mock', text: 'subpage1' },
		{ url: './mock', text: 'subpage2' },
		{ url: './mock', text: 'subpage3' }
	];
</script>

<Navbar {links} />
<main class="px-2 md:px-24">
	<slot />
</main>
