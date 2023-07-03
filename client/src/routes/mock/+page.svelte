<script>
  import { SearchIcon } from 'lucide-svelte';
</script>

<div class="flex justify-center">
  <div class="relative">
    <button class="absolute left-1 top-1/2 transform -translate-y-1/2">
          <SearchIcon class=" text-gray-500" />
    </button>
    <input class="border rounded-xl px-1 py-1 pl-10" type="text" placeholder="recipe" />
  </div>
</div>
