<script lang='ts'>
    let name: string = $state("");
    let position: string = $state("");

    // date default to today, format of yyyy-mm-dd
    let applied_date: string = $state(
        (new Date(Date.now()))
            .toISOString()
            .split('T')[0]
    );

    // allowable status
    const STATUS: Array<string> = [
        "New", "WIP", "Wait", "Pass", "Fail", "Hire"
    ];

    let status: string = $state(STATUS[0]);

</script>

<input type="text" name="" id="" placeholder="Name-Surname">
<input type="role" name="" id="" placeholder="Role">
<input type="date" name="" id="" bind:value={applied_date}>

<select id="cars" name="cars" bind:value={status}>
    {#each STATUS as s}
        <option value={s}>{s}</option>
    {/each}
</select>
