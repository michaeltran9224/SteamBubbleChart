import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path"

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
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