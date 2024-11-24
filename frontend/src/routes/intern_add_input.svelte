<script lang='ts'>
    import { InternStatus, API } from "$lib";
    import type { InternInfo } from "$lib";

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

<input type="text" bind:value={internInfo.name} placeholder="Name-Surname">
<input type="role" bind:value={internInfo.role} placeholder="Role">
<input type="date" bind:value={internInfo.applied_date}>

<select bind:value={internInfo.status}>
    {#each Object.values(InternStatus) as s}
        <option value={s}>{s}</option>
    {/each}
</select>

<input type="button" value="Add" onclick={AddIntern}>

