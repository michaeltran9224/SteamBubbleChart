import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {
    port: 3000,
    strictPort: true,
   },
   server: {
    port: 3000,
    strictPort: true,
    host: true,
    // origin: "http://0.0.0.0:3000", for some reason, this causes images to not load because of [[Failed to load resource: net::ERR_ADDRESS_INVALID]]
   },
})