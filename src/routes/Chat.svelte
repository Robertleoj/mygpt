
<script>
    import { onMount } from 'svelte';
	import { currentChat } from '$lib/stores/currentChat.js';
	let message = '';
	let messages = [];
    // for(let i = 0; i < 50; i++){
    //     messages.push('Message ' + i);
    // }

    let scrollableDiv;
    onMount(() => {
        scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
    });

	function sendMessage() {
		if (message.trim() !== '') {
			messages = [...messages, message];
			message = '';
			if($currentChat === null){
				currentChat.set('new chat id'); // Update this as per your requirements
			}

            // wait for the browser to render the new message before scrolling
            setTimeout(() => {
                scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
            }, 0);
		}
	}
</script>

<div class="flex flex-col h-full m-auto p-0">
	<div class="overflow-y-auto px-4 py-0 w-full h-full flex-grow flex items-center flex-col" bind:this={scrollableDiv}>
        <div class="max-w-xl w-full">
            {#if $currentChat === null && messages.length === 0}
                <div class="h-full flex">
                    <div class="text-center text-gray-500 italic m-auto">New Chat</div>
                </div>
            {/if}
            {#each messages as msg, i}
                <div class="bg-green-200 p-2 my-2 rounded-md">
                    {msg}
                </div>
            {/each}
        </div>
	</div>

	<div class="p-4 bg-gray-100  w-full">
		<div class="flex gap-2">
			<input type="text" bind:value={message} class="flex-grow rounded-md border-2" placeholder="Type your message here..." on:keydown={(e) => e.key === 'Enter' && sendMessage()}>

			<button on:click={sendMessage} class="bg-blue-500 text-white rounded-md px-2 py-1">Send</button>
		</div>
	</div>
</div>
