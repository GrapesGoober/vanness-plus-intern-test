<script lang="ts">
    // format of yyyy-mm-dd
    let date: string = $props(
        (new Date(Date.now()))
            .toISOString()
            .split('T')[0]
    );
</script>

<input type="date" name="" id="" bind:value={date}>