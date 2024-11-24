<script lang="ts">
    import { InternStatus } from "$lib";
    import type { InternFilter } from "$lib";
    import { slide } from "svelte/transition";

    let {filter = $bindable()}: {filter: InternFilter} = $props();

    let isShowing: boolean = $state(false);

    function toggle() {
        isShowing = !isShowing;
    }

</script>

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" />

<button class="material-symbols-outlined toggle" onclick={toggle}>
    filter_alt
</button>
{#if isShowing}
    <div class="parent" in:slide out:slide>
        <p>Filter Search</p>
        <input type="text" bind:value={filter.name_contains} placeholder="Name Contains">  <br>
        <label for="applied_after">Applied After</label>
        <input name="applied_after" type="date" bind:value={filter.applied_after}>  <br>

        <label for="applied_before">Applied Before</label>
        <input name="applied_before" type="date" bind:value={filter.applied_before}> <br>

        <label for="status">Status</label>
        <select name="status" bind:value={filter.status}>
            <option value="">All</option>
            {#each Object.values(InternStatus) as status}
                <option value={status}>{status}</option>
            {/each}
        </select>
    </div>
{/if}

<style>
    button.toggle {
        text-align: left;
        background-color: #eee;
        color: black;
        padding: 5px;
        border-radius: 10px;
        border: none;
        display: inline;
        margin: 5px;
    }

    div.parent {
        text-align: left;
        width: 30em;
        background-color: #eee;
        color: black;
        padding: 16px;
        border-radius: 0.5em;
        display: block;
        margin: 1em;
    }
</style>