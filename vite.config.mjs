import { defineConfig } from "vite";


export default defineConfig({
    base: "./",
    build: {
        outDir: "bobtail_admin/static/admin",
        lib: {
            entry: "src/js/admin.js",
            formats: ["es"],
            fileName: () => "admin.js",
            cssFileName: "admin",
        },
    },
});