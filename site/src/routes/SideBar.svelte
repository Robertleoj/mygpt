<script>
    import SideBarFileItem from "./SideBarFileItem.svelte";
    import SideBarGroupItem from "./SideBarGroupItem.svelte";
</script>

<div class="flex flex-col">
    <h1 class="pt-5 text-black">Groups</h1>
    <div>
        <SideBarGroupItem />
    </div>
    <h1 class="pt-5 text-black">Files</h1>
    <div>
        <SideBarFileItem />
    </div>
</div>
