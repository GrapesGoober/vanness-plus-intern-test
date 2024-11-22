import { sveltekit } from '@sveltejs/kit/vite';
import {defineConfig} from "vite";

export default defineConfig({
    plugins: [sveltekit()],
    server: {
        watch: {
            usePolling: true,
        },
        host: true, // needed for the DC port mapping to work
        strictPort: true,
        port: 5173,
        proxy: {
			'/api/': {
				target: 'http://fastapi-app:8000'
			}
		}
    }
});