<script lang="ts">
    import { API, InternStatus } from "$lib";
    import type { InternFilter, InternInfoWithId,  } from "$lib";
    import { onMount } from "svelte";

    let interns: Array<InternInfoWithId> = $state([]);
    let {filter = $bindable()}: {filter: InternFilter} = $props();

    async function UpdateInternsArray() {
        interns = await API.GetInterns(filter);
    }
    
    onMount(() => {
        UpdateInternsArray();
        setInterval(UpdateInternsArray, 5000);
    });
    
</script>

{#each interns as i}
<div>
    {i.status}
    {i.name}
    {i.applied_date}
    {i.role}
</div>    
{/each}