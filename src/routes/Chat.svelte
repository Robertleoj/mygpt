
<script>    
    import { onMount } from 'svelte';
	import { currentChat } from '$lib/stores/currentChat.js';
    import MessageInput from "./MessageInput.svelte";
    import UserChatMessage from './UserChatMessage.svelte';

	let messages = [];

    let scrollableDiv;
    onMount(() => {
        scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
    });

    const handleSendMessage = (event) => {

        const message = event.detail;
        
        if (!message.isValidMessage()) {
            return;
        }

        console.log(message);

		messages = [...messages, message];
        
        if($currentChat === null){
            currentChat.set('new chat id'); // Update this as per your requirements
        }

        // wait for the browser to render the new message before scrolling
        setTimeout(() => {
            scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
        }, 0);
        
    }

</script>


<div class="relative h-full">
    <div class="relative h-full overflow-scroll px-6" bind:this={scrollableDiv}>
        {#each messages as msg, i}
            <UserChatMessage message={msg}/>
        {/each}
    </div>
    <div class="absolute bg-white bottom-6 w-3/5 inset-x-0 mx-auto flex items-center border-black border-2">
        <MessageInput on:messageSent={handleSendMessage}/>
    </div>
    
</div>