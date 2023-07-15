<script>
    import SideBarFileItem from "./SideBarFileItem.svelte";
    import SideBarGroupItem from "./SideBarGroupItem.svelte";
    import AddButton from "./AddButton.svelte";
</script>

<div class="flex flex-col">
    <AddButton/>
    <h1 class="pt-5 text-black">Files</h1>
    <div>
        <SideBarFileItem />
    </div>
</div>
