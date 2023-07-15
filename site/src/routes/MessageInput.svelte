<script>
    import { ArrowUpIcon } from "svelte-feather-icons";
    import { createEventDispatcher } from "svelte";
  
    let message = "";
    const dispatch = createEventDispatcher();
  
    const sendMessage = () => {
      dispatch("messageSent", message);
      message = "";
    };
  
    const onKeyDown = (e) => {
      if (e.key === "Enter") sendMessage();
    };
  </script>
  
  <input
    on:keydown={onKeyDown}
    bind:value={message}
    class="flex-grow p-3"
    type="text"
    placeholder="Type your question here"
  />
  
  <button on:click={sendMessage} class="mx-2">
    <ArrowUpIcon class="h-6 w-6" />
  </button>
  