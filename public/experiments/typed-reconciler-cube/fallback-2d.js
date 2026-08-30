import { CELL_KINDS, typedCube } from "./scene-data.js?v=3"

const host = document.querySelector("#scene")
const detail = document.querySelector("#detail")
const canvas = document.createElement("canvas")
canvas.setAttribute("aria-label", "Canvas 2D isometric view of the typed coherence cube")
host.appendChild(canvas)
const context = canvas.getContext("2d")
const byId = new Map(typedCube.cells.map((cell) => [cell.id, cell]))
const colors = {
  process: "#63b3ff", reconciliation: "#f3b35d", transport: "#b68cff",
  interchanger: "#50d890", processPreservation: "#63b3ff",
  reconciliationPreservation: "#f3b35d", volumeCoherencer: "#e96b78",
}
const routes = {
  processThenReconcile: ["v0", "v1", "v3"],
  reconcileThenProcess: ["v0", "v2", "v3"],
}
let maxDimension = 3
let activeRoute = null
let projected = new Map()

function show(cell) {
  const contract = CELL_KINDS[cell.kind]
  detail.innerHTML = `<strong>${cell.label}</strong><span>${cell.kind} · dimension ${contract.dimension}</span><span>status: ${cell.status}</span><span>authority: ${cell.authority}</span><span>boundary: ${cell.boundaryRefs.join(", ") || "none"}</span>`
}
show(byId.get("omega"))

function iso(position, width, height) {
  const [x, y, z] = position
  const scale = Math.min(width * 0.22, height * 0.19)
  return [width * 0.5 + (x - z) * scale, height * 0.53 + (x + z) * scale * 0.48 - y * scale]
}

function path(points, fill, stroke, alpha = 1) {
  context.beginPath()
  points.forEach(([x, y], index) => index ? context.lineTo(x, y) : context.moveTo(x, y))
  context.closePath()
  context.globalAlpha = alpha
  if (fill) { context.fillStyle = fill; context.fill() }
  if (stroke) { context.strokeStyle = stroke; context.lineWidth = 1.5; context.stroke() }
  context.globalAlpha = 1
}

const faces = [[0,1,3,2],[4,5,7,6],[0,1,5,4],[2,3,7,6],[0,2,6,4],[1,3,7,5]]
function draw(time = performance.now()) {
  const ratio = Math.min(devicePixelRatio, 2)
  const width = canvas.width = Math.max(1, Math.floor(host.clientWidth * ratio))
  const height = canvas.height = Math.max(1, Math.floor(host.clientHeight * ratio))
  context.clearRect(0, 0, width, height)
  context.fillStyle = "#071117"; context.fillRect(0, 0, width, height)
  projected = new Map([...byId].filter(([, c]) => CELL_KINDS[c.kind].dimension === 0).map(([id, c]) => [id, iso(c.position, width, height)]))

  if (maxDimension >= 3) path(faces[1].map((id) => projected.get(`v${id}`)), colors.volumeCoherencer, null, 0.08)
  if (maxDimension >= 2) faces.forEach((face, index) => path(face.map((id) => projected.get(`v${id}`)), colors[typedCube.cells.filter((c) => CELL_KINDS[c.kind].dimension === 2)[index].kind], null, 0.09))
  if (maxDimension >= 1) for (const cell of typedCube.cells.filter((c) => CELL_KINDS[c.kind].dimension === 1)) {
    const [a, b] = cell.boundaryRefs.map((id) => projected.get(id))
    context.beginPath(); context.moveTo(...a); context.lineTo(...b)
    context.strokeStyle = colors[cell.kind]; context.globalAlpha = cell.status === "inaccessible" ? 0.28 : 0.9
    context.lineWidth = 2.5 * ratio; context.stroke(); context.globalAlpha = 1
  }
  if (maxDimension >= 0) for (const [id, point] of projected) {
    context.beginPath(); context.arc(...point, 6 * ratio, 0, Math.PI * 2)
    context.fillStyle = "#f4f8fb"; context.fill()
    context.fillStyle = "#9db0b9"; context.font = `${10 * ratio}px ui-monospace`; context.fillText(id, point[0] + 8 * ratio, point[1] - 7 * ratio)
  }
  if (activeRoute) {
    const t = Math.min(1, (time - activeRoute.started) / 2200)
    const n = t * 2, segment = Math.min(1, Math.floor(n)), u = n - segment
    const a = projected.get(activeRoute.ids[segment]), b = projected.get(activeRoute.ids[segment + 1])
    const marker = [a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u]
    context.beginPath(); context.arc(...marker, 9 * ratio, 0, Math.PI * 2); context.fillStyle = "#ffffff"; context.fill()
    if (t === 1) activeRoute = null
  }
  if (activeRoute) requestAnimationFrame(draw)
}

for (const button of document.querySelectorAll("[data-layer]")) button.addEventListener("click", () => {
  maxDimension = Number(button.dataset.layer)
  document.querySelectorAll("[data-layer]").forEach((item) => item.classList.toggle("active", item === button))
  draw()
})
for (const button of document.querySelectorAll("[data-route]")) button.addEventListener("click", () => {
  activeRoute = { ids: routes[button.dataset.route], started: performance.now() }
  show(byId.get("fa")); requestAnimationFrame(draw)
})
canvas.addEventListener("pointerdown", (event) => {
  const rect = canvas.getBoundingClientRect(), sx = canvas.width / rect.width, sy = canvas.height / rect.height
  const p = [(event.clientX - rect.left) * sx, (event.clientY - rect.top) * sy]
  const nearest = [...projected].map(([id, q]) => [id, Math.hypot(p[0] - q[0], p[1] - q[1])]).sort((a,b) => a[1] - b[1])[0]
  if (nearest?.[1] < 28 * Math.min(devicePixelRatio, 2)) show(byId.get(nearest[0]))
})
new ResizeObserver(() => draw()).observe(host)
draw()
