<script lang="ts">
    import { InternStatus } from "$lib";
    import type { InternFilter } from "$lib";

    let {filter = $bindable()}: {filter: InternFilter} = $props();

</script>

<input type="text" bind:value={filter.name_contains} placeholder="Name">
<label for="applied_after">Applied After</label>
<input name="applied_after" type="date" bind:value={filter.applied_after}>
<label for="applied_before">Applied Before</label>
<input name="applied_before" type="date" bind:value={filter.applied_before}>
<select bind:value={filter.status}>
    <option value="">All</option>
    {#each Object.values(InternStatus) as status}
        <option value={status}>{status}</option>
    {/each}
</select>