<script lang="ts">
    import { API } from "$lib";
    import type { InternFilter, InternInfoWithId,  } from "$lib";
    import { onMount } from "svelte";
    import InternItem from "./intern_item.svelte";

    let {
        filter = $bindable(),
        interns = $bindable(),
    }: {
        filter: InternFilter,
        interns: Array<InternInfoWithId>,
    } = $props();

    async function UpdateInternsArray() {
        interns = await API.GetInterns(filter);
    }
    
    onMount(() => {
        UpdateInternsArray();
        setInterval(UpdateInternsArray, 5000);
    });
    
</script>

{#each interns as _, index }
    <InternItem bind:internInfo={interns[index]}></InternItem>
{/each}