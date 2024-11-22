<script lang="ts">
    import { API, InternStatus } from "$lib";
    import type { InternFilter, InternInfoWithId,  } from "$lib";
    import { onMount } from "svelte";

    onMount(() => {
        let filter: InternFilter = {
            name_contains: "N",
            applied_after: "2020-01-01",
            applied_before: "2026-01-01",
            status: InternStatus.HIRE
        }
        API.GetInterns(filter)
        .then((interns) => {
            interns.forEach((i) => {
                console.log(i)
            })
        });
    })
</script>