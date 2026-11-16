import { spawn } from "node:child_process";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createServer } from "vite";

// No browser automation dependency: a local installed Chromium/Edge runs the checked module.
const executable = process.env["ISOTOPE_BROWSER"];
if (executable === undefined)
  throw new Error("Set ISOTOPE_BROWSER to an installed Chromium/Edge executable");
const server = await createServer({
  cacheDir: ".verification/vite-browser-cache",
  server: { host: "127.0.0.1", port: 0, strictPort: true },
  plugins: [
    {
      name: "local-browser-check",
      transformIndexHtml: (_html, context) => [
        {
          tag: "output",
          attrs: { id: "browser-result", "data-status": "running" },
          children: "RUNNING",
          injectTo: "body",
        },
        {
          tag: "script",
          attrs: {
            type: "module",
            src: context.originalUrl?.includes("versions-check=1")
              ? "/scripts/browser-named-versions.ts"
              : context.originalUrl?.includes("edit-check=1")
                ? "/scripts/browser-edge-edits.ts"
                : "/scripts/browser-scenario.ts",
          },
          injectTo: "body",
        },
      ],
    },
  ],
});
try {
  await server.listen();
  const address = server.httpServer?.address();
  if (address === undefined || address === null || typeof address === "string")
    throw new Error("Missing local server address");
  for (const scale of [1, 2]) {
    for (const mode of ["smoke", "edits", "versions"]) {
      console.log(`Browser ${mode}: device scale ${scale}`);
      const profile = await mkdtemp(join(tmpdir(), "isotope-browser-check-"));
      try {
        // Separate browser launches with the same profile prove persistence, not
        // merely retention in Vue or a single document's JavaScript heap.
        for (const stage of mode === "versions"
          ? ["save", "reload", "delete-reload", "active-reload", "ux", "ux-reload"]
          : mode === "edits"
            ? ["edit", "reload", "invalid", "approved", "approved-reload"]
            : ["smoke"]) {
          const output = await new Promise<string>((resolve, reject) => {
            const child = spawn(
              executable,
              [
                "--headless=new",
                "--disable-gpu",
                `--force-device-scale-factor=${scale}`,
                scale === 1 ? "--window-size=1000,800" : "--window-size=480,640",
                "--no-first-run",
                "--no-default-browser-check",
                `--user-data-dir=${profile}`,
                "--dump-dom",
                "--virtual-time-budget=20000",
                `http://127.0.0.1:${address.port}/?scale=${scale}${mode === "versions" ? `&versions-check=1&stage=${stage}` : mode === "edits" ? `&edit-check=1&stage=${stage}` : ""}`,
              ],
              { stdio: ["ignore", "pipe", "pipe"], timeout: 60000 },
            );
            let text = "";
            let errors = "";
            child.stdout.setEncoding("utf8");
            child.stderr.setEncoding("utf8");
            child.stdout.on("data", (chunk: string) => {
              text += chunk;
            });
            child.stderr.on("data", (chunk: string) => {
              errors = (errors + chunk).slice(-4000);
            });
            child.once("error", reject);
            child.once("close", (code) => {
              if (code === 0) resolve(text);
              else reject(new Error(`Browser exited ${code}: ${errors}`));
            });
          });
          if (!output.includes('data-status="pass"'))
            throw new Error(
              `Browser workflow did not pass: ${output.match(/<output[^>]*id="browser-result"[^>]*>[\s\S]*?<\/output>/)?.[0] ?? output.slice(0, 2000)}`,
            );
        }
      } finally {
        await rm(profile, { recursive: true, force: true, maxRetries: 10, retryDelay: 200 });
      }
    }
  }
  console.log(
    "PASS: persistent edge edits and two viewport/device-scale configurations; catalog filters/navigation, docking, reference pins, edge selection, labels and animated routing; removed UI absent",
  );
} finally {
  await server.close();
}
