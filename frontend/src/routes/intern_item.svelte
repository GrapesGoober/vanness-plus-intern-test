<script lang="ts">
    import { API, InternStatus } from "$lib";
    import type { InternInfoWithId,  } from "$lib";

    let {
        internInfo = $bindable(),
    }: {
        internInfo: InternInfoWithId,
    } = $props();

    let isEditing: boolean = $state(false);
    let internEditInfo: InternInfoWithId = $state({...internInfo});

    function StartEdit() {
        isEditing = true;
        internEditInfo = {...internInfo};
    }

    function ConfirmEdit() {
        API.EditIntern(internEditInfo);
        isEditing = false;
    }

    function CancelEdit() {
        internEditInfo = {...internInfo};
        isEditing = false;
    }
    
</script>

{#if !isEditing}
<div>
    {internInfo.status}
    {internInfo.name}
    {internInfo.applied_date}
    {internInfo.role}
    <input type="button" value="Edit" onclick={StartEdit}>
</div>    

{:else}
<div>
    <select bind:value={internEditInfo.status}>
        {#each Object.values(InternStatus) as status}
            <option value={status}>{status}</option>
        {/each}
    </select>
    <input type="text" bind:value={internEditInfo.name}>
    <input type="date" bind:value={internEditInfo.applied_date}>
    <input type="text" bind:value={internEditInfo.role}>
    <input type="button" value="Confirm" onclick={ConfirmEdit}>
    <input type="button" value="Cancel" onclick={CancelEdit}>
</div>  
{/if}
    