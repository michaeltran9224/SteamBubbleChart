import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {
    proxy: { "/steam":   {
        target: "http://backend:5000/",
        changeOrigin: true,
        secure: false,
      }
    },
    port: 3000,
    strictPort: true,
   },
   server: {
    proxy: { "/steam":   {
        target: "http://backend:5000/",
        changeOrigin: true,
        secure: false,
      }
    },
    port: 3000,
    strictPort: true,
    host: true,
   },
})