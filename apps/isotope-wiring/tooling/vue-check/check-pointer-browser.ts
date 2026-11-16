import ts from "typescript";
import { z } from "zod";
import { spawn } from "node:child_process";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createServer } from "vite";

// Native browser input, not dispatchEvent mocks. Protocol decoding uses the pinned JSON parser.
function expression(text: string): ts.Expression {
  const source = ts.parseJsonText("browser-protocol.json", text),
    statement = source.statements[0];
  if (statement === undefined || !ts.isExpressionStatement(statement))
    throw new Error("Invalid browser protocol JSON");
  return statement.expression;
}
function field(node: ts.Expression | undefined, key: string): ts.Expression | undefined {
  if (node === undefined || !ts.isObjectLiteralExpression(node)) return undefined;
  const item = node.properties.find(
    (item) =>
      ts.isPropertyAssignment(item) && ts.isStringLiteral(item.name) && item.name.text === key,
  );
  return item !== undefined && ts.isPropertyAssignment(item) ? item.initializer : undefined;
}
function text(node: ts.Expression | undefined): string {
  if (node === undefined || !ts.isStringLiteral(node)) throw new Error("Expected protocol string");
  return node.text;
}
function number(node: ts.Expression | undefined): number {
  if (node === undefined || !ts.isNumericLiteral(node)) throw new Error("Expected protocol number");
  return Number(node.text);
}
const MouseType = z.enum(["mousePressed", "mouseMoved", "mouseReleased"]);
const Command = z.discriminatedUnion("method", [
  z.strictObject({ method: z.literal("Page.enable"), params: z.strictObject({}) }),
  z.strictObject({ method: z.literal("Runtime.enable"), params: z.strictObject({}) }),
  z.strictObject({
    method: z.literal("Emulation.setDeviceMetricsOverride"),
    params: z.strictObject({
      width: z.int(),
      height: z.int(),
      deviceScaleFactor: z.number(),
      mobile: z.boolean(),
    }),
  }),
  z.strictObject({
    method: z.literal("Emulation.clearDeviceMetricsOverride"),
    params: z.strictObject({}),
  }),
  z.strictObject({
    method: z.literal("Input.insertText"),
    params: z.strictObject({ text: z.string() }),
  }),
  z.strictObject({
    method: z.literal("Page.handleJavaScriptDialog"),
    params: z.strictObject({ accept: z.boolean() }),
  }),
  z.strictObject({
    method: z.literal("Page.navigate"),
    params: z.strictObject({ url: z.string() }),
  }),
  z.strictObject({
    method: z.literal("Runtime.evaluate"),
    params: z.strictObject({
      expression: z.string(),
      awaitPromise: z.boolean(),
      returnByValue: z.boolean(),
    }),
  }),
  z.strictObject({
    method: z.literal("Input.dispatchMouseEvent"),
    params: z.strictObject({
      type: MouseType,
      x: z.number(),
      y: z.number(),
      button: z.literal("left"),
      buttons: z.int(),
      clickCount: z.int(),
    }),
  }),
  z.strictObject({
    method: z.literal("Input.dispatchKeyEvent"),
    params: z.strictObject({
      type: z.enum(["keyDown", "keyUp"]),
      key: z.string(),
      code: z.string(),
      windowsVirtualKeyCode: z.int(),
    }),
  }),
  z.strictObject({
    method: z.literal("Emulation.setTouchEmulationEnabled"),
    params: z.strictObject({ enabled: z.boolean() }),
  }),
  z.strictObject({
    method: z.literal("Input.dispatchTouchEvent"),
    params: z.strictObject({
      type: z.enum(["touchStart", "touchMove", "touchEnd", "touchCancel"]),
      touchPoints: z.array(z.strictObject({ x: z.number(), y: z.number(), id: z.int() })),
    }),
  }),
]);
const Point = z.strictObject({ x: z.number(), y: z.number() });
const executable = process.env["ISOTOPE_BROWSER"];
if (executable === undefined) throw new Error("Set ISOTOPE_BROWSER");
const server = await createServer({
  cacheDir: ".verification/vite-pointer-cache",
  server: { host: "127.0.0.1", port: 0, strictPort: true },
});
await server.listen();
const address = server.httpServer?.address();
if (address === undefined || address === null || typeof address === "string")
  throw new Error("Missing server address");
const profile = await mkdtemp(join(tmpdir(), "isotope-pointer-"));
const child = spawn(
  executable,
  [
    "--headless=new",
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    "--window-size=1000,800",
    "--remote-debugging-port=0",
    `--user-data-dir=${profile}`,
    "about:blank",
  ],
  { stdio: "ignore" },
);
const closed = new Promise<void>((resolve) => child.once("close", () => resolve()));
let socket: WebSocket | null = null;
const deadline = setTimeout(() => child.kill(), 45000);
const pending = new Map<number, (result: ts.Expression | undefined, error: Error | null) => void>();
try {
  let port = "";
  for (let attempt = 0; attempt < 100; attempt++) {
    try {
      port = (await readFile(join(profile, "DevToolsActivePort"), "utf8")).split("\n")[0] ?? "";
      if (port) break;
    } catch {}
    if (child.exitCode !== null) throw new Error("Browser exited before debugging was ready");
    await new Promise<void>((resolve) => setTimeout(resolve, 50));
  }
  if (!/^\d+$/.test(port)) throw new Error("Missing debugging port");
  const targets = expression(await (await fetch(`http://127.0.0.1:${port}/json/list`)).text());
  if (!ts.isArrayLiteralExpression(targets)) throw new Error("Invalid debugging targets");
  const target = targets.elements.find((item) => {
    const kind = field(item, "type");
    return kind !== undefined && ts.isStringLiteral(kind) && kind.text === "page";
  });
  const connection = new WebSocket(text(field(target, "webSocketDebuggerUrl")));
  socket = connection;
  connection.binaryType = "arraybuffer";
  await new Promise<void>((resolve, reject) => {
    connection.addEventListener("open", () => resolve(), { once: true });
    connection.addEventListener("error", () => reject(new Error("Debug connection failed")), {
      once: true,
    });
  });
  let onLoad: (() => void) | null = null;
  let onDialog: (() => void) | null = null;
  connection.addEventListener("message", (event: MessageEvent<string | ArrayBuffer>) => {
    if (typeof event.data !== "string") return;
    const root = expression(event.data),
      id = field(root, "id");
    const method = field(root, "method");
    if (method !== undefined && ts.isStringLiteral(method) && method.text === "Page.loadEventFired")
      onLoad?.();
    if (
      method !== undefined &&
      ts.isStringLiteral(method) &&
      method.text === "Page.javascriptDialogOpening"
    )
      onDialog?.();
    if (
      method !== undefined &&
      ts.isStringLiteral(method) &&
      method.text === "Runtime.exceptionThrown"
    )
      console.error(event.data.slice(0, 4000));
    if (id === undefined) return;
    const key = number(id),
      callback = pending.get(key);
    pending.delete(key);
    callback?.(
      field(root, "result"),
      field(root, "error") === undefined &&
        field(field(root, "result"), "exceptionDetails") === undefined
        ? null
        : new Error(event.data.slice(0, 4000)),
    );
  });
  connection.addEventListener("close", () => {
    for (const callback of pending.values())
      callback(undefined, new Error("Debug connection closed"));
    pending.clear();
  });
  let serial = 0;
  function send(command: z.infer<typeof Command>): Promise<ts.Expression | undefined> {
    const checked = Command.parse(command),
      id = ++serial;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        pending.delete(id);
        reject(new Error(`Timed out: ${checked.method}`));
      }, 10000);
      pending.set(id, (result, error) => {
        clearTimeout(timer);
        if (error !== null) reject(error);
        else resolve(result);
      });
      connection.send(JSON.stringify({ id, ...checked }));
    });
  }
  async function evaluate(
    name:
      | "ready"
      | "prepare"
      | "captured"
      | "released"
      | "moved"
      | "disableMove"
      | "removeDiagram"
      | "removed",
  ): Promise<ts.Expression | undefined> {
    // The invoked scenario module is checked TypeScript; no inline application implementation.
    const result = await send({
      method: "Runtime.evaluate",
      params: {
        expression: `import('/scripts/pointer-scenario.ts').then(m => m.${name}())`,
        awaitPromise: true,
        returnByValue: true,
      },
    });
    return field(field(result, "result"), "value");
  }
  async function prepare(): Promise<z.infer<typeof Point>> {
    const value = await evaluate("prepare");
    return Point.parse({ x: number(field(value, "x")), y: number(field(value, "y")) });
  }
  async function mouse(type: z.infer<typeof MouseType>, x: number, y: number): Promise<void> {
    await send({
      method: "Input.dispatchMouseEvent",
      params: {
        type,
        x,
        y,
        button: "left",
        buttons: type === "mouseReleased" ? 0 : 1,
        clickCount: 1,
      },
    });
  }
  await send({ method: "Page.enable", params: {} });
  await send({ method: "Runtime.enable", params: {} });
  const loaded = new Promise<void>((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error("Page did not load")), 10000);
    onLoad = () => {
      clearTimeout(timer);
      resolve();
    };
  });
  await send({
    method: "Page.navigate",
    params: { url: process.env["ISOTOPE_POINTER_URL"] ?? `http://127.0.0.1:${address.port}/` },
  });
  await loaded;
  onLoad = null;
  for (let attempt = 0; attempt < 300; attempt++) {
    if ((await evaluate("ready"))?.kind === ts.SyntaxKind.TrueKeyword) break;
    await new Promise<void>((resolve) => setTimeout(resolve, 50));
  }
  if ((await evaluate("ready"))?.kind !== ts.SyntaxKind.TrueKeyword)
    throw new Error("Application did not become ready");
  async function versionAction(
    name:
      | "summary"
      | "name"
      | "save"
      | "saved"
      | "load"
      | "loaded"
      | "remove"
      | "removed"
      | "outside"
      | "outsideClosed"
      | "closed"
      | "compact"
      | "compactEmpty"
      | "morseOpen"
      | "morseCheck"
      | "morseClose"
      | "morseClosed",
  ): Promise<ts.Expression | undefined> {
    const result = await send({
      method: "Runtime.evaluate",
      params: {
        expression: `import('/scripts/native-versions-scenario.ts').then(m => m.${name}())`,
        awaitPromise: true,
        returnByValue: true,
      },
    });
    return field(field(result, "result"), "value");
  }
  async function versionClick(
    name: "summary" | "name" | "save" | "load" | "remove" | "outside" | "morseOpen" | "morseClose",
    confirm = false,
  ): Promise<void> {
    const value = await versionAction(name);
    const p = Point.parse({ x: number(field(value, "x")), y: number(field(value, "y")) });
    const confirmed = confirm
      ? new Promise<void>((resolve, reject) => {
          const timer = setTimeout(
            () => reject(new Error("Native version confirmation did not appear: " + name)),
            5000,
          );
          onDialog = () => {
            send({ method: "Page.handleJavaScriptDialog", params: { accept: true } }).then(() => {
              clearTimeout(timer);
              resolve();
            }, reject);
          };
        })
      : Promise.resolve();
    await mouse("mousePressed", p.x, p.y);
    await mouse("mouseReleased", p.x, p.y);
    await confirmed;
    onDialog = null;
  }
  await versionClick("summary");
  await versionAction("name"); // Assert autofocus; do not click the input.
  await send({ method: "Input.insertText", params: { text: "Native baseline" } });
  await versionClick("save");
  await versionAction("saved");
  await send({
    method: "Emulation.setDeviceMetricsOverride",
    params: { width: 320, height: 360, deviceScaleFactor: 2, mobile: false },
  });
  await versionAction("compact");
  await send({ method: "Emulation.clearDeviceMetricsOverride", params: {} });
  await versionClick("load", true);
  await versionAction("loaded");
  await versionClick("summary");
  await versionClick("remove", true);
  await versionAction("removed");
  await send({
    method: "Input.dispatchKeyEvent",
    params: { type: "keyDown", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 },
  });
  await send({
    method: "Input.dispatchKeyEvent",
    params: { type: "keyUp", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 },
  });
  await versionAction("closed");
  await versionClick("summary");
  await versionClick("outside");
  await versionAction("outsideClosed");
  await send({
    method: "Emulation.setDeviceMetricsOverride",
    params: { width: 320, height: 360, deviceScaleFactor: 2, mobile: false },
  });
  await versionClick("summary");
  await versionAction("compactEmpty");
  await send({
    method: "Input.dispatchKeyEvent",
    params: { type: "keyDown", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 },
  });
  await send({
    method: "Input.dispatchKeyEvent",
    params: { type: "keyUp", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 },
  });
  await versionAction("closed");
  await send({ method: "Emulation.clearDeviceMetricsOverride", params: {} });
  console.log(
    "PASS: native save/load/delete focus, Escape and outside dismissal without graph edits",
  );
  await versionClick("morseOpen");
  await versionAction("morseCheck");
  await versionClick("morseClose");
  await versionAction("morseClosed");
  console.log("PASS: live Morse surface invariants and read-only dialog");
  let point = await prepare();
  await mouse("mousePressed", point.x, point.y);
  await mouse("mouseMoved", point.x + 40, point.y + 20);
  await evaluate("captured");
  await mouse("mouseReleased", point.x + 40, point.y + 20);
  await evaluate("moved");
  point = await prepare();
  await mouse("mousePressed", point.x, point.y);
  await mouse("mouseMoved", point.x + 20, point.y);
  await evaluate("captured");
  await evaluate("disableMove");
  await evaluate("released");
  await mouse("mouseReleased", point.x + 20, point.y);
  point = await prepare();
  await mouse("mousePressed", point.x, point.y);
  await mouse("mouseMoved", point.x + 20, point.y);
  await evaluate("captured");
  await send({
    method: "Input.dispatchKeyEvent",
    params: { type: "keyDown", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 },
  });
  await evaluate("released");
  await send({
    method: "Input.dispatchKeyEvent",
    params: { type: "keyUp", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 },
  });
  await mouse("mouseReleased", point.x + 20, point.y);
  await send({ method: "Emulation.setTouchEmulationEnabled", params: { enabled: true } });
  point = await prepare();
  await send({
    method: "Input.dispatchTouchEvent",
    params: { type: "touchStart", touchPoints: [{ ...point, id: 1 }] },
  });
  await send({
    method: "Input.dispatchTouchEvent",
    params: { type: "touchMove", touchPoints: [{ x: point.x + 40, y: point.y + 20, id: 1 }] },
  });
  await evaluate("captured");
  await send({
    method: "Input.dispatchTouchEvent",
    params: { type: "touchCancel", touchPoints: [] },
  });
  await evaluate("moved");
  await send({ method: "Emulation.setTouchEmulationEnabled", params: { enabled: false } });
  point = await prepare();
  await mouse("mousePressed", point.x, point.y);
  await mouse("mouseMoved", point.x + 20, point.y);
  await evaluate("captured");
  await evaluate("removeDiagram");
  await evaluate("removed");
  await mouse("mouseReleased", point.x + 20, point.y);
  console.log(
    "PASS: native mouse drag, capture release on mode exit/Escape, touch cancellation and diagram removal",
  );
} finally {
  clearTimeout(deadline);
  socket?.close();
  child.kill();
  await closed;
  await rm(profile, { recursive: true, force: true, maxRetries: 10, retryDelay: 200 });
  await server.close();
}
