import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";
import { spawn, type ChildProcessWithoutNullStreams } from "node:child_process";
import { readFile, readdir, stat, writeFile } from "node:fs/promises";
import { basename, join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

interface Diagnostic {
  range?: { start?: { line?: number; character?: number }; end?: { line?: number; character?: number } };
  severity?: number;
  message?: string;
  source?: string;
}

interface Pending {
  resolve: (value: unknown) => void;
  reject: (error: Error) => void;
  timer: NodeJS.Timeout;
}

class RzkLspClient {
  private child?: ChildProcessWithoutNullStreams;
  private buffer = Buffer.alloc(0);
  private nextId = 1;
  private pending = new Map<number, Pending>();
  private diagnostics = new Map<string, Diagnostic[]>();
  private waiters = new Map<string, Array<(items: Diagnostic[]) => void>>();
  private versions = new Map<string, number>();
  private documentText = new Map<string, string>();
  private stderrTail = "";
  projectRoot?: string;

  async start(projectRoot: string): Promise<void> {
    if (this.child && this.projectRoot === projectRoot) return;
    await this.stop();
    this.projectRoot = projectRoot;
    const configPath = join(projectRoot, "rzk.yaml");
    const config = await readFile(configPath, "utf8");
    const focusedConfig = config.replace("src/marici/**/*.rzk.md", "src/marici-target/**/*.rzk.md");
    if (focusedConfig !== config) await writeFile(configPath, focusedConfig, "utf8");
    const child = spawn("rzk", ["lsp"], { cwd: projectRoot, stdio: "pipe", windowsHide: true });
    this.child = child;
    child.stdout.on("data", (chunk: Buffer) => this.receive(chunk));
    child.stderr.on("data", (chunk: Buffer) => {
      this.stderrTail = (this.stderrTail + chunk.toString("utf8")).slice(-8000);
    });
    child.on("exit", (code, signal) => {
      const error = new Error(`rzk lsp exited: code=${code} signal=${signal}\n${this.stderrTail}`);
      for (const pending of this.pending.values()) {
        clearTimeout(pending.timer);
        pending.reject(error);
      }
      this.pending.clear();
      this.child = undefined;
    });
    await new Promise<void>((resolveReady, reject) => {
      child.once("spawn", resolveReady);
      child.once("error", reject);
    });
    await this.request("initialize", {
      processId: process.pid,
      rootUri: pathToFileURL(projectRoot).href,
      capabilities: { textDocument: { publishDiagnostics: { relatedInformation: true } } },
      workspaceFolders: [{ uri: pathToFileURL(projectRoot).href, name: "marici-rzk" }],
    }, 30000);
    this.notify("initialized", {});
  }

  async stop(): Promise<void> {
    const child = this.child;
    if (child) {
      try { await this.request("shutdown", null, 2000); } catch {}
      try { this.notify("exit", null); } catch {}
      child.kill();
      this.child = undefined;
    }
    this.buffer = Buffer.alloc(0);
    this.diagnostics.clear();
    this.versions.clear();
    this.documentText.clear();
  }

  status() {
    return { running: Boolean(this.child), pid: this.child?.pid, projectRoot: this.projectRoot, stderrTail: this.stderrTail };
  }

  async check(livePath: string, timeoutMs: number): Promise<{ uri: string; diagnostics: Diagnostic[] }> {
    if (!this.child || !this.projectRoot) throw new Error("Rzk LSP is not started");
    const text = await readFile(livePath, "utf8");
    const shadowPath = join(this.projectRoot, "src", "marici-target", basename(livePath));
    await writeFile(shadowPath, text, "utf8");
    const uri = pathToFileURL(shadowPath).href;
    const cached = this.diagnostics.get(uri);
    if (this.documentText.get(uri) === text && cached) return { uri, diagnostics: cached };
    this.documentText.set(uri, text);
    const version = (this.versions.get(uri) ?? 0) + 1;
    this.versions.set(uri, version);
    this.diagnostics.delete(uri);
    if (version === 1) {
      this.notify("textDocument/didOpen", { textDocument: { uri, languageId: "rzk", version, text } });
    } else {
      this.notify("textDocument/didChange", { textDocument: { uri, version }, contentChanges: [{ text }] });
    }
    const items = await new Promise<Diagnostic[]>((resolveDiagnostics, reject) => {
      const timer = setTimeout(() => {
        const waiters = this.waiters.get(uri) ?? [];
        this.waiters.set(uri, waiters.filter((waiter) => waiter !== done));
        reject(new Error(`Timed out after ${timeoutMs}ms waiting for Rzk diagnostics`));
      }, timeoutMs);
      const done = (diagnostics: Diagnostic[]) => { clearTimeout(timer); resolveDiagnostics(diagnostics); };
      this.waiters.set(uri, [...(this.waiters.get(uri) ?? []), done]);
    });
    return { uri, diagnostics: items };
  }

  private send(message: unknown): void {
    if (!this.child) throw new Error("Rzk LSP is not running");
    const body = Buffer.from(JSON.stringify(message), "utf8");
    this.child.stdin.write(`Content-Length: ${body.length}\r\n\r\n`);
    this.child.stdin.write(body);
  }

  private notify(method: string, params: unknown): void { this.send({ jsonrpc: "2.0", method, params }); }

  private request(method: string, params: unknown, timeoutMs: number): Promise<unknown> {
    const id = this.nextId++;
    this.send({ jsonrpc: "2.0", id, method, params });
    return new Promise((resolveRequest, reject) => {
      const timer = setTimeout(() => { this.pending.delete(id); reject(new Error(`${method} timed out`)); }, timeoutMs);
      this.pending.set(id, { resolve: resolveRequest, reject, timer });
    });
  }

  private receive(chunk: Buffer): void {
    this.buffer = Buffer.concat([this.buffer, chunk]);
    while (true) {
      const headerEnd = this.buffer.indexOf("\r\n\r\n");
      if (headerEnd < 0) return;
      const header = this.buffer.subarray(0, headerEnd).toString("ascii");
      const match = /Content-Length:\s*(\d+)/i.exec(header);
      if (!match) { this.buffer = this.buffer.subarray(headerEnd + 4); continue; }
      const length = Number(match[1]);
      const bodyStart = headerEnd + 4;
      if (this.buffer.length < bodyStart + length) return;
      const body = this.buffer.subarray(bodyStart, bodyStart + length).toString("utf8");
      this.buffer = this.buffer.subarray(bodyStart + length);
      try { this.handle(JSON.parse(body)); } catch {}
    }
  }

  private handle(message: any): void {
    if (typeof message?.id === "number" && ("result" in message || "error" in message)) {
      const pending = this.pending.get(message.id);
      if (!pending) return;
      this.pending.delete(message.id);
      clearTimeout(pending.timer);
      if (message.error) pending.reject(new Error(JSON.stringify(message.error)));
      else pending.resolve(message.result);
      return;
    }
    if (message?.method === "textDocument/publishDiagnostics") {
      const uri = String(message.params?.uri ?? "");
      const items = Array.isArray(message.params?.diagnostics) ? message.params.diagnostics : [];
      this.diagnostics.set(uri, items);
      const waiters = this.waiters.get(uri) ?? [];
      this.waiters.delete(uri);
      for (const waiter of waiters) waiter(items);
    }
  }
}

async function discoverProjectRoot(cwd: string): Promise<string> {
  const configured = process.env.MARICI_RZK_PROJECT_ROOT;
  if (configured) return resolve(configured);
  const base = join(cwd, "research", "grothendieck", "rzk");
  const candidates: Array<{ path: string; mtimeMs: number }> = [];
  for (const tempName of await readdir(base)) {
    if (!tempName.startsWith(".check-tmp-")) continue;
    const temp = join(base, tempName);
    for (const checkName of await readdir(temp)) {
      const source = join(temp, checkName, "source");
      try {
        for (const projectName of await readdir(source)) {
          if (!projectName.startsWith("sHoTT-")) continue;
          const project = join(source, projectName);
          candidates.push({ path: project, mtimeMs: (await stat(project)).mtimeMs });
        }
      } catch {}
    }
  }
  candidates.sort((a, b) => b.mtimeMs - a.mtimeMs);
  if (!candidates[0]) throw new Error("No staged sHoTT project found; run the Rzk checker first or set MARICI_RZK_PROJECT_ROOT");
  return candidates[0].path;
}

function formatDiagnostics(items: Diagnostic[]): string {
  if (items.length === 0) return "Rzk LSP reported no diagnostics.";
  return items.slice(0, 100).map((item) => {
    const start = item.range?.start;
    const location = start ? `${(start.line ?? 0) + 1}:${(start.character ?? 0) + 1}` : "?:?";
    const message = item.message ?? "";
    const bounded = message.length > 2000 ? `${message.slice(0, 2000)}\n[diagnostic truncated]` : message;
    return `${location} severity=${item.severity ?? "?"} ${bounded}`;
  }).join("\n");
}

export default function (pi: ExtensionAPI) {
  const client = new RzkLspClient();
  pi.registerTool({
    name: "rzk_lsp_diagnostics",
    label: "Rzk LSP Diagnostics",
    description: "Keep rzk lsp alive and return bounded diagnostics for one live Rzk Markdown source file.",
    promptSnippet: "Get incremental diagnostics from the persistent Rzk language server",
    promptGuidelines: ["Use rzk_lsp_diagnostics for rapid Rzk feedback; retain fresh headless closure checks as verification."],
    parameters: Type.Object({ path: Type.String(), projectRoot: Type.Optional(Type.String()), timeoutMs: Type.Optional(Type.Integer({ minimum: 1000, maximum: 300000 })) }),
    async execute(_id, params, signal, onUpdate, ctx) {
      signal?.throwIfAborted();
      const projectRoot = params.projectRoot ? resolve(ctx.cwd, params.projectRoot) : await discoverProjectRoot(ctx.cwd);
      onUpdate?.({ content: [{ type: "text", text: `Starting/reusing rzk lsp in ${projectRoot}` }] });
      await client.start(projectRoot);
      const result = await client.check(resolve(ctx.cwd, params.path.replace(/^@/, "")), params.timeoutMs ?? 120000);
      return { content: [{ type: "text", text: formatDiagnostics(result.diagnostics) }], details: { ...result, projectRoot } };
    },
  });
  pi.registerCommand("rzk-lsp-status", { description: "Show persistent Rzk LSP status", handler: async (_args, ctx) => ctx.ui.notify(JSON.stringify(client.status()), "info") });
  pi.registerCommand("rzk-lsp-check", {
    description: "Request Rzk LSP diagnostics for one repository-relative file",
    handler: async (args, ctx) => {
      if (!args.trim()) { ctx.ui.notify("Usage: /rzk-lsp-check <path>", "error"); return; }
      const projectRoot = await discoverProjectRoot(ctx.cwd);
      await client.start(projectRoot);
      const result = await client.check(resolve(ctx.cwd, args.trim().replace(/^@/, "")), 120000);
      ctx.ui.notify(formatDiagnostics(result.diagnostics), result.diagnostics.length === 0 ? "info" : "warning");
    },
  });
  pi.registerCommand("rzk-lsp-restart", { description: "Restart the persistent Rzk LSP", handler: async (_args, ctx) => { await client.stop(); await client.start(await discoverProjectRoot(ctx.cwd)); ctx.ui.notify("Rzk LSP restarted", "info"); } });
  pi.on("session_shutdown", async () => { await client.stop(); });
}
