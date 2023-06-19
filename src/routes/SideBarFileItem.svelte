<script>
    import {FileIcon, SquareIcon} from 'svelte-feather-icons'

    const onCheckBoxClick = () => {
        // Handle
    }

</script>

<div class="flex p-2 cursor-pointer" style="justify-content: space-between;">
    <FileIcon class="text-black" size="20"/>
    <span class="text-black mr-auto">Physics</span>
    <input type="checkbox" id="fileCheckbox" on:click={onCheckBoxClick}>
</div>