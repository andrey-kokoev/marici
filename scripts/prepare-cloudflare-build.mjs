import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const naradaRoot = resolve(repositoryRoot, "..", "narada");
const uiPackage = resolve(naradaRoot, "packages", "ui", "package.json");
const naradaRemote = "https://github.com/narada-core/narada.git";
const naradaRef = (process.env.NARADA_UI_REF || "main").trim();

function runGit(args, cwd) {
  execFileSync("git", args, { cwd, stdio: "inherit" });
}

if (existsSync(uiPackage)) {
  console.log("[cloudflare-build] Using existing Narada checkout at " + naradaRoot + ".");
  process.exit(0);
}

if (existsSync(naradaRoot)) {
  throw new Error(
    "The expected Narada checkout already exists but is missing packages/ui: " + naradaRoot,
  );
}

mkdirSync(dirname(naradaRoot), { recursive: true });
console.log("[cloudflare-build] Fetching Narada ref " + naradaRef + ".");
runGit(["init", naradaRoot], repositoryRoot);
runGit(["remote", "add", "origin", naradaRemote], naradaRoot);
runGit(["fetch", "--depth=1", "origin", naradaRef], naradaRoot);
runGit(["checkout", "--detach", "FETCH_HEAD"], naradaRoot);

if (!existsSync(uiPackage)) {
  throw new Error("Narada checkout did not contain packages/ui: " + naradaRoot);
}

console.log("[cloudflare-build] Narada UI is available at " + naradaRoot + ".");
