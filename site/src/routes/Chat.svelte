
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

    const handleSendMessage = async (event) => {

        const message = event.detail;
        
        if (!message.isValidMessage()) {
            return;
        }

        console.log(message);

		messages = [...messages, {
            role: 'user',
            content: message
        }];
        
        if ($currentChat === null){
            currentChat.set('new chat id'); // Update this as per your requirements
        }

        // wait for the browser to render the new message before scrolling
        setTimeout(() => {
            scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
        }, 0);

        /** Post message to server */

        const response = await fetch('/api/brain/response', {
            method: 'POST',
			body: JSON.stringify({
                messages
            })
		})

        let aiMessage = await response.json();
        aiMessage = aiMessage.response;
        console.log("ai Message");
        console.log(aiMessage);


        messages = [...messages, aiMessage];

    }

</script>


<div class="relative h-full flex flex-col">
    <div class="relative h-full overflow-y-scroll px-6 pb-3 flex-grow" bind:this={scrollableDiv}>
        {#each messages as msg, i}
            <UserChatMessage message={msg.content}/>
        {/each}
    </div>
    <div class="bg-white bottom-6 w-3/5 inset-x-0 mx-auto mt-2 flex items-center border-black border-2">
        <MessageInput on:messageSent={handleSendMessage}/>
    </div>
    
</div>