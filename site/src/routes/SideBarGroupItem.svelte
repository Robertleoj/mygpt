<script>
    import { ChevronRightIcon, SquareIcon } from 'svelte-feather-icons'
    import SideBarFileItem from './SideBarFileItem.svelte';

    let isDropdownOpen = false;

    const toggleDropdown = () => {
        isDropdownOpen = !isDropdownOpen;
    }

    const onCheckBoxClick = () => {
        // Your checkbox click logic here
    }

</script>

<div class="p-2 cursor-pointer" style="position: relative;">
    <div class="flex">
        <span class:rotate180={isDropdownOpen}>
            <div on:click={toggleDropdown} on:keydown={() => {}}>
                <ChevronRightIcon class="text-black {isDropdownOpen ? "rotate-90" : ""}" size="20" />
            </div>
        </span>
        <span class="text-black" style="margin-right: auto;">Spanish</span>
        <input type="checkbox" id="fileCheckbox" on:click={onCheckBoxClick}>
    </div>
    {#if isDropdownOpen}
        <SideBarFileItem/>
        <SideBarFileItem/>
        <SideBarFileItem/>
    {/if}
</div>
