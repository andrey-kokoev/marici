#!/usr/bin/env node

import { spawn } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// Uses the sibling ../stacks-project checkout by default; override it with
// STACKS_PROJECT_ROOT (and STACKS_PYTHON when a specific Python is needed).
const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const mariciRoot = resolve(scriptDirectory, "..");
const configuredRoot = process.env.STACKS_PROJECT_ROOT;
const stacksRoot = configuredRoot
  ? resolve(mariciRoot, configuredRoot)
  : resolve(mariciRoot, "..", "stacks-project");
const searchScript = resolve(stacksRoot, "scripts", "search.py");
const python = process.env.STACKS_PYTHON || (process.platform === "win32" ? "python" : "python3");
const forwardedArgs = process.argv[2] === "--" ? process.argv.slice(3) : process.argv.slice(2);

const child = spawn(python, [searchScript, ...forwardedArgs], {
  cwd: stacksRoot,
  stdio: "inherit",
  windowsHide: true,
});

let spawnFailed = false;

child.once("error", (error) => {
  spawnFailed = true;
  console.error(`stacks:search: unable to run ${python} from ${stacksRoot}: ${error.message}`);
});

child.once("close", (code, signal) => {
  process.exitCode = spawnFailed || signal ? 1 : code ?? 1;
});
