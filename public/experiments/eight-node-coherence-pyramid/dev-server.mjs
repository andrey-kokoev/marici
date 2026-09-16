import { createServer } from "node:http"
import { readFile, stat } from "node:fs/promises"
import { dirname, extname, join, normalize } from "node:path"
import { fileURLToPath } from "node:url"

const host = "127.0.0.1"
const port = Number(process.env.PORT ?? 8766)
const publicRoot = normalize(join(dirname(fileURLToPath(import.meta.url)), "../.."))
const types = new Map([
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".mjs", "text/javascript; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".png", "image/png"],
])

createServer(async (request, response) => {
  try {
    const url = new URL(request.url, `http://${request.headers.host ?? host}`)
    if (url.pathname === "/experiments/eight-node-coherence-pyramid/__build-info") {
      const pageRoot = dirname(fileURLToPath(import.meta.url))
      const files = await Promise.all(["index.html", "app.js"].map(name => stat(join(pageRoot, name))))
      const lastBuild = new Date(Math.max(...files.map(file => file.mtimeMs))).toISOString()
      response.writeHead(200, { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" })
      response.end(JSON.stringify({ lastBuild }))
      return
    }
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
}).listen(port, host, () => {
  console.log(`eight-node coherence pyramid: http://${host}:${port}/experiments/eight-node-coherence-pyramid/`)
})
