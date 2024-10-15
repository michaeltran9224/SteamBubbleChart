import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {
    proxy: { "/steam":   {
        target: "http://127.0.0.1:5000/",
        changeOrigin: true,
        secure: false,
        ws: true,
      }
    },
    port: 3000,
    strictPort: true,
   },
   server: {
    proxy: { "/steam":   {
        target: "http://localhost:5000/",
        changeOrigin: true,
        secure: false,
        ws: true,
      }
    },
    port: 3000,
    strictPort: true,
    host: true,
   },
})