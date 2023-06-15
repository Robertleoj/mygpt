<script>
	import Chat from "./Chat.svelte";
	import SideBar from "./SideBar.svelte";
</script>

<div class="flex min-h-screen max-h-screen">
    <aside class="w-64 bg-gray-800 text-white p-4">
		<SideBar/>
    </aside>

    <main class="flex-1 bg-gray-200 p-2">
		<Chat/>
    </main>
</div>
