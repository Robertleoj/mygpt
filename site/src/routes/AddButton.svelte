<script>
    import { createEventDispatcher } from 'svelte';
    import {PlusIcon} from 'svelte-feather-icons'
  
    const dispatch = createEventDispatcher();

    let allowedFileExtensions = ".txt"
  
    const onPress = () => {
      const input = document.createElement('input');
      input.type = 'file';
      input.multiple = true;
      input.accept = allowedFileExtensions; // Specify the text-based file types here
      input.addEventListener('change', handleFileChange);
      input.click();
    };
  
    function handleFileChange(event) {
      const newFiles = Array.from(event.target.files);
      dispatch('filesSelected', newFiles);
    }
  </script>

<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-5 rounded w-full flex items-center justify-center" on:click={onPress}>
  <PlusIcon class="mr-1" />
  Add files
</button>