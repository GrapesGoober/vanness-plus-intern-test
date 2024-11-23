<script lang="ts">
    import InternFilterInput from "./intern_filter_input.svelte";
    import InternList from "./intern_list.svelte";
    import type { InternFilter } from "$lib"; 
    import { InternStatus } from "$lib"; 

    let appliedBeforeDefault: string = "2020-01-01";
    let dateNow: string = 
        (new Date(Date.now()))
            .toISOString()
            .split('T')[0];

    let filter: InternFilter = {
        name_contains: "",
        applied_after: appliedBeforeDefault,
        applied_before: dateNow, 
        status: InternStatus.HIRE
    };
</script>

<div>
    <h1>Welcome to Intern Tracking App</h1>
    <p>This app is made by Nachat K, as intern trial for Vanness Plus Consulting Co., Ltd</p>
    <InternFilterInput bind:filter={filter}></InternFilterInput>
    <InternList bind:filter={filter}></InternList>
</div>