<script lang='ts'>
    import { InternStatus, API } from "$lib";
    import type { InternInfo } from "$lib";
    import { slide } from "svelte/transition";

    let isShowing: boolean = $state(false);

    function toggle() {
        isShowing = !isShowing;
    }

    // date default to today, format of yyyy-mm-dd
    let default_date: string = $state(
        (new Date(Date.now()))
            .toISOString()
            .split('T')[0]
    );

    let internInfo: InternInfo = $state({
        name: "",
        applied_date: default_date,
        role: "",
        status: InternStatus.NEW
    });

    function AddIntern() {
        API.AddIntern(internInfo);
        internInfo = {
            name: "",
            applied_date: default_date,
            role: "",
            status: InternStatus.NEW
        };
    }

</script>
<button class="material-symbols-outlined toggle" onclick={toggle}>
    add
</button>
{#if isShowing}
    <div class="parent" in:slide out:slide>
        <p>Insert New Intern</p>
        <input type="text" bind:value={internInfo.name} placeholder="Name-Surname">
        <input type="role" bind:value={internInfo.role} placeholder="Role">
        <input type="date" bind:value={internInfo.applied_date}>

        <select bind:value={internInfo.status}>
            {#each Object.values(InternStatus) as s}
                <option value={s}>{s}</option>
            {/each}
        </select>

        <input type="button" value="Add" onclick={AddIntern}>
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

