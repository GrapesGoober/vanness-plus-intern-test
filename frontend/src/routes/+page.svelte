<script lang="ts">
    import InternFilterInput from "./intern_filter_input.svelte";
    import InternList from "./intern_list.svelte";
    import type { InternFilter } from "$lib"; 
    import { GetDefaultInternFilter } from "$lib"; 
    import InternAddInput from "./intern_add_input.svelte";

    let filter: InternFilter = $state(GetDefaultInternFilter());
</script>

<div>
    <h1>Welcome to Intern Tracking App</h1>
    <p>This app is made by Nachat K, as intern trial for Vanness Plus Consulting Co., Ltd</p>
    <InternFilterInput bind:filter={filter}></InternFilterInput>
    <InternList bind:filter={filter}></InternList>
    <InternAddInput></InternAddInput>
</div>