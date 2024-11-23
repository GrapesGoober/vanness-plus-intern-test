<script lang="ts">
    import { API, InternStatus } from "$lib";
    import type { InternFilter, InternInfoWithId,  } from "$lib";
    import { onMount } from "svelte";

    let interns: Array<InternInfoWithId> = [];
    let filter: InternFilter = {
        name_contains: "",
        applied_after: "2020-01-01",
        applied_before: "2026-01-01",
        status: InternStatus.HIRE
    };

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