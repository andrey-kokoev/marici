import { spawn } from "node:child_process";
import { performance } from "node:perf_hooks";

const cli = "C:/Users/andrey/AppData/Local/fnm_multishells/26768_1788200249140/node_modules/@earendil-works/pi-coding-agent/dist/bundle/cli.js";
const extension = ".pi/extensions/rzk-lsp.ts";
const valid = "research/grothendieck/rzk/src/99zzzzzzs99999999998-marici-raw-translated-addition-cancellation.rzk.md";
const invalid = "research/grothendieck/rzk/fixtures/lsp-deliberate-failure.rzk.md";
const steps = [
  { id: "valid-cold", path: valid, expectsDiagnostics: false },
  { id: "valid-warm", path: valid, expectsDiagnostics: false },
  { id: "invalid-warm", path: invalid, expectsDiagnostics: true },
];
const child = spawn(process.execPath, [cli, "--mode", "rpc", "--no-session", "-e", extension], {
  cwd: process.cwd(), stdio: ["pipe", "pipe", "pipe"], windowsHide: true,
});
let stdout = "";
let stderr = "";
let index = 0;
let started = 0;
let diagnosticMessage;
let finished = false;
const timings = {};
const timer = setTimeout(() => finish(new Error(`timeout\nstdout=${stdout.slice(-8000)}\nstderr=${stderr.slice(-8000)}`)), 240000);

function sendStep() {
  const step = steps[index];
  diagnosticMessage = undefined;
  started = performance.now();
  child.stdin.write(JSON.stringify({ id: step.id, type: "prompt", message: `/rzk-lsp-check ${step.path}` }) + "\n");
}

function finish(error) {
  if (finished) return;
  finished = true;
  clearTimeout(timer);
  child.stdin.end();
  setTimeout(() => { if (!child.killed) child.kill(); }, 3000).unref();
  if (error) { console.error(error.message); process.exitCode = 1; }
  else {
    console.log(`RZK_LSP_TIMINGS_MS ${JSON.stringify(timings)}`);
    console.log("PI_RZK_LSP_SMOKE_OK");
  }
}

child.stderr.on("data", chunk => { stderr = (stderr + chunk).slice(-16000); });
child.stdout.on("data", chunk => {
  stdout += chunk.toString("utf8");
  while (true) {
    const newline = stdout.indexOf("\n");
    if (newline < 0) break;
    const line = stdout.slice(0, newline).replace(/\r$/, "");
    stdout = stdout.slice(newline + 1);
    if (!line) continue;
    let event;
    try { event = JSON.parse(line); } catch { continue; }
    if (event.type === "extension_error") return finish(new Error(JSON.stringify(event)));
    if (event.type === "extension_ui_request" && event.method === "notify" && !String(event.message).startsWith("Narada MCP")) {
      diagnosticMessage = String(event.message);
      console.log(`RZK_NOTIFY ${event.notifyType}: ${diagnosticMessage.slice(0, 1000)}`);
    }
    const step = steps[index];
    if (event.type === "response" && event.id === step.id) {
      if (!event.success) return finish(new Error(JSON.stringify(event)));
      timings[step.id] = Math.round(performance.now() - started);
      if (diagnosticMessage === undefined) return finish(new Error(`${step.id}: no diagnostics notification`));
      const empty = diagnosticMessage === "Rzk LSP reported no diagnostics.";
      if (step.expectsDiagnostics === empty) return finish(new Error(`${step.id}: unexpected diagnostic result: ${diagnosticMessage}`));
      index += 1;
      if (index === steps.length) return finish();
      sendStep();
    }
  }
});
child.on("error", finish);
child.on("exit", code => { if (!finished) finish(new Error(`Pi RPC exited ${code}: ${stderr}`)); });
sendStep();
