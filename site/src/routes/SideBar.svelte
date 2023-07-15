<script>
    import AddButton from "./AddButton.svelte";
    import SideBarFileItem from "./SideBarFileItem.svelte";

    let mFiles = []; // type: File
  
    function handleFileChange(event) {
      const newFiles = Array.from(event.detail);
      mFiles = [...mFiles, ...newFiles];
    }
  </script>
  
  <!--Button for the user to upload files-->
  <AddButton on:filesSelected={handleFileChange}/>
  
  {#each mFiles as file}
    <SideBarFileItem fileName={file.name}/>
  {/each}
  