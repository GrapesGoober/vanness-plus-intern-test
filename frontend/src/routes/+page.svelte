<script lang="ts">
    import InternFilterInput from "./intern_filter_input.svelte";
    import InternList from "./intern_list.svelte";
    import type { InternFilter, InternInfoWithId } from "$lib"; 
    import { GetDefaultInternFilter } from "$lib"; 
    import InternAddInput from "./intern_add_input.svelte";

    let interns: Array<InternInfoWithId> = $state([]);
    let filter: InternFilter = $state(GetDefaultInternFilter());
</script>

<div>
    <h1>Welcome to Intern Tracking App</h1>
    <p>This app is made by Nachat K, as intern trial for Vanness Plus Consulting Co., Ltd</p>
    <InternFilterInput bind:filter={filter}></InternFilterInput>
    <InternAddInput></InternAddInput>
    <InternList bind:interns={interns} bind:filter={filter}></InternList>
</div>

<style>
    * {
        font-family: 'Verdana', 'Trebuchet MS', 'Tahoma', 'Arial ';
    }
</style>