<script lang="ts">
    import { API, InternStatus } from "$lib";
    import type { InternInfoWithId } from "$lib";

    let {
        internInfo = $bindable(),
    }: {
        internInfo: InternInfoWithId,
    } = $props();

    const InternStatusColors = {
        [InternStatus.NEW]: '#5ac475',
        [InternStatus.WIP]: '#edbc28',
        [InternStatus.WAIT]: '#eabbf2',
        [InternStatus.PASS]: '#6aa7ba',
        [InternStatus.FAIL]: '#b8b8b8',
        [InternStatus.HIRE]: '#ed6ded'
    };

    let isFocused: boolean = $state(false);
    let isEditing: boolean = $state(false);
    let internEditInfo: InternInfoWithId = $state({...internInfo});

    function StartFocus() {
        isFocused = true;
    }

    function CancelFocus() {
        isFocused = false;
    }

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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" />

<div class="parent" onfocusin={StartFocus} onfocusout={CancelFocus}>
{#if !isEditing}
    <div class="status-icon" 
    style="background-color: {InternStatusColors[internInfo.status]};">
        {internInfo.status}
    </div>
    {internInfo.name} <br>
    {internInfo.applied_date}
    {internInfo.role}
    <button class="material-symbols-outlined icon" onclick={StartEdit}>
        edit_square
    </button>
{:else}
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
{/if}
</div>  

<style>
    div.parent {
        text-align: left;
        width: 30em;
        background-color: #eee;
        color: black;
        padding: 16px;
        border-radius: 0.5em;
        display: block;
        margin: 1em;
        border: #eee solid 1px;
    }
    div.parent:hover {
        border: #aaa solid 1px;
    }
    div.status-icon {
        display: inline-block;
        color: white;
        padding: 0.2em 0.4em;
        border-radius: 0.3em;
    }
    button.icon {
        border: none;
        background-color: transparent;
        float: right;
        opacity: 0.2;
    }
    button.icon:hover {
        border: none;
        background-color: transparent;
        float: right;
        position: relative;
        right: 0.1em;
        top: -0.1em;
        opacity: 1;
    }
</style>
    