<script lang="ts">
    let dateStr: string = $state(
        (new Date(Date.now()))
            .toISOString()
            .split('T')[0]
    );
    let date: Date = $derived(new Date(dateStr))
</script>

<input type="date" name="" id="" bind:value={dateStr}>