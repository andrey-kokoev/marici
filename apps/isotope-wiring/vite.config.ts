import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    host: "127.0.0.1",
    // Editors/formatters may briefly truncate a module before writing its contents.
    // Do not transform and cache that transient empty file during hot reload.
    watch: { awaitWriteFinish: { stabilityThreshold: 200, pollInterval: 25 } },
  },
  preview: { host: "127.0.0.1" },
});
