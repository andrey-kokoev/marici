import { createServer } from "node:http"
import { readFile, stat } from "node:fs/promises"
import { dirname, extname, join, normalize } from "node:path"
import { fileURLToPath } from "node:url"

const host = "127.0.0.1"
const port = 8765
const publicRoot = normalize(join(dirname(fileURLToPath(import.meta.url)), "../.."))
const types = new Map([
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".mjs", "text/javascript; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".toml", "text/plain; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".png", "image/png"],
])

createServer(async (request, response) => {
  try {
    const url = new URL(request.url, `http://${request.headers.host ?? host}`)
    const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "")
    let path = normalize(join(publicRoot, relative))
    if (!path.startsWith(publicRoot)) throw new Error("path outside public root")
    const metadata = await stat(path).catch(() => null)
    if (metadata?.isDirectory()) path = join(path, "index.html")
    const body = await readFile(path)
    response.writeHead(200, {
      "Content-Type": types.get(extname(path)) ?? "application/octet-stream",
      "Cache-Control": "no-store, max-age=0",
      "Pragma": "no-cache",
    })
    response.end(body)
  } catch {
    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8", "Cache-Control": "no-store" })
    response.end("Not found")
  }
}).listen(port, host, () => console.log(`typed reconciler: http://${host}:${port}/experiments/typed-reconciler-cube/`))
