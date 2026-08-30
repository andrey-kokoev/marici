import * as THREE from "three"
import { OrbitControls } from "three/addons/controls/OrbitControls.js"

const host = document.querySelector("#scene")
const detail = document.querySelector("#detail")
const status = document.querySelector("#validation")
const controlsHost = document.querySelector(".controls")
const text = await fetch("./coherence-lattice.toml", { cache: "no-cache" }).then(r => {
  if (!r.ok) throw new Error(`TOML fetch ${r.status}`)
  return r.text()
})

function value(raw) {
  const s = raw.trim()
  if (s.startsWith("[")) return JSON.parse(s.replace(/,\s*]$/, "]"))
  if (s.startsWith('"')) return JSON.parse(s)
  if (s === "true" || s === "false") return s === "true"
  if (/^[-+]?\d+$/.test(s)) return Number(s)
  return s
}

function parseToml(source) {
  const root = Object.create(null)
  const arrays = Object.create(null)
  const lines = source.split(/\r?\n/)
  const clean = line => line.replace(/(^|\s+)#.*$/, "").trim()
  let target = root
  for (let i = 0; i < lines.length; i++) {
    const line = clean(lines[i])
    if (!line) continue
    let match
    if ((match = line.match(/^\[\[([^\]]+)\]\]$/))) {
      const key = match[1]
      arrays[key] ??= []
      target = Object.create(null)
      arrays[key].push(target)
      root[key] = arrays[key]
      continue
    }
    if ((match = line.match(/^\[([^\]]+)\]$/))) {
      const key = match[1]
      if (!Object.hasOwn(root, key)) root[key] = Object.create(null)
      target = root[key]
      continue
    }
    const at = line.indexOf("=")
    if (at < 1) throw new Error(`Unsupported TOML line: ${line}`)
    const key = line.slice(0, at).trim()
    let raw = line.slice(at + 1).trim()
    if (raw.startsWith("[") && !raw.endsWith("]")) {
      while (++i < lines.length) {
        const next = clean(lines[i])
        if (next) raw += next
        if (next.endsWith("]")) break
      }
      if (!raw.endsWith("]")) throw new Error(`Unterminated TOML array: ${key}`)
    }
    target[key] = value(raw)
  }
  return root
}

const model = parseToml(text)
const n = model.lattice.object_count
const rungs = [...model.rung].sort((a, b) => a.index - b.index)
const reconcilers = new Map((model.reconciler ?? []).map(x => [x.id, x]))
const transportLaws = new Map((model.transport_law ?? []).map(x => [x.id, x]))
const coherenceCells = new Map((model.coherence_cell ?? []).map(x => [x.id, x]))
const thetaTate = new Map((model.theta_tate_cell ?? []).map(x => [x.id, x]))
const lenses = model.coefficient_lens ?? []

const errors = []
if (n !== 8) errors.push("this pyramid realization requires order 8")
if (rungs.length !== n) errors.push("rung count mismatch")
if (reconcilers.size !== n - 1) errors.push("transport count mismatch")
if (transportLaws.size !== n - 1) errors.push("transport-law count mismatch")
if (coherenceCells.size !== (n - 1) * (n - 2) / 2) errors.push("Layer-0 higher-cell count mismatch")
if (errors.length) throw new Error(errors.join("\n"))

const idOf = (layer, column, index) => `L${layer}_C${column}_${index}`
const layerOrder = layer => n - layer
const layerCellCount = order => order * (order + 1) / 2
const cells = []

function layerZeroData(column, index) {
  const sourceId = `C${column}_${index}`
  const sector = thetaTate.get(sourceId)
  if (column === 0) return {
    label: rungs[index].label,
    status: "pinned",
    authority: "pinned tower vocabulary",
    sector,
    kind: "presentation",
  }
  if (column === 1) return {
    label: reconcilers.get(sourceId).label,
    status: "partial",
    authority: reconcilers.get(sourceId).authority,
    sector,
    kind: "transport",
    transportLaw: transportLaws.get(sourceId),
  }
  return {
    label: sector.label,
    status: coherenceCells.get(sourceId).status,
    authority: sector.authority,
    sector,
    kind: "coherencer",
    coherenceCell: coherenceCells.get(sourceId),
  }
}

for (let layer = 0; layer < n; layer++) {
  const order = layerOrder(layer)
  for (let column = 0; column < order; column++) {
    for (let index = 0; index < order - column; index++) {
      const id = idOf(layer, column, index)
      const lowerSource = layer > 0 ? idOf(layer - 1, column + 1, index) : null
      const data = layer === 0 ? layerZeroData(column, index) : {
        label: `coherence lift of ${lowerSource}`,
        status: "required",
        authority: "unconstructed higher coherencer",
        sector: { label: `higher coherence over ${lowerSource}`, authority: "required" },
        kind: column === 0 ? "lifted conservation object" : "higher coherencer",
      }
      cells.push({
        ...data,
        id, layer, column, index, order, lowerSource,
        leftFace: column > 0 ? idOf(layer, column - 1, index) : null,
        rightFace: column > 0 ? idOf(layer, column - 1, index + 1) : null,
        sharedFace: column > 1 ? idOf(layer, column - 2, index + 1) : null,
      })
    }
  }
}

const expectedTotal = Array.from({ length: n }, (_, layer) => layerCellCount(layerOrder(layer))).reduce((a, b) => a + b, 0)
if (cells.length !== expectedTotal || expectedTotal !== 120) throw new Error("pyramid cell count mismatch")
status.textContent = `valid TOML · 8 triangular layers · 120 standard cells · 36,28,21,15,10,6,3,1`

function routesFor(cell) {
  if (cell.layer === 0 && cell.coherenceCell) return {
    routeA: cell.coherenceCell.route_a,
    routeB: cell.coherenceCell.route_b,
    content: cell.coherenceCell.transported_content,
    context: cell.coherenceCell.comparison_context,
  }
  if (cell.column > 1) return {
    routeA: `R_${cell.layer}_${cell.column - 1}_${cell.index} ∘ L_${cell.layer}_${cell.column}_${cell.index}`,
    routeB: `L_${cell.layer}_${cell.column - 1}_${cell.index + 1} ∘ R_${cell.layer}_${cell.column}_${cell.index}`,
    content: cell.lowerSource ? `coherence content lifted from ${cell.lowerSource}` : "Layer-0 transported constructor content",
    context: cell.sharedFace,
  }
  return null
}

function instantiatedLenses(routes) {
  return routes ? lenses.map(lens => ({
    id: lens.id,
    formula: lens.formula.replaceAll("R∘L", `(${routes.routeA})`).replaceAll("L∘R", `(${routes.routeB})`),
    identity: lens.flat_identity,
  })) : []
}

function describe(cell) {
  const base = `<strong>${cell.id} · ${cell.label}</strong><span>pyramid layer: ${cell.layer} · triangular order: ${cell.order}</span><span>column: ${cell.column} · index: ${cell.index}</span><span>kind: ${cell.kind}</span><span>status: ${cell.status}</span><span>authority: ${cell.authority}</span>`
  if (cell.layer === 0 && cell.transportLaw) {
    const law = cell.transportLaw
    detail.innerHTML = `${base}<hr><span>${law.transport}: ${law.source} → ${law.target}</span><span>${law.interpretation}</span><span class="formula"><b>conservation</b>: ${law.formula} = ${law.flat_identity}</span>`
    return
  }
  const routes = routesFor(cell)
  const vertical = cell.lowerSource ? `<span>lower-layer source: ${cell.lowerSource}</span>` : ""
  if (!routes) {
    detail.innerHTML = `${base}<hr>${vertical}<span>${cell.layer === 0 ? "Layer-0 presentation object" : "Conservation object lifted from the preceding triangular layer"}.</span>`
    return
  }
  detail.innerHTML = `${base}<hr>${vertical}<span>left face: ${cell.leftFace}</span><span>right face: ${cell.rightFace}</span><span>shared face: ${cell.sharedFace}</span><span>route A: ${routes.routeA}</span><span>route B: ${routes.routeB}</span><span>transported content: ${routes.content}</span><span>comparison context: ${routes.context}</span>${instantiatedLenses(routes).map(l => `<span class="formula"><b>${l.id}</b>: ${l.formula} = ${l.identity}</span>`).join("")}`
}

const scene = new THREE.Scene()
scene.background = new THREE.Color(0x071117)
const camera = new THREE.PerspectiveCamera(43, 1, 50, 12000)
const initialCameraPosition = new THREE.Vector3(2800, -800, 4200)
const initialOrbitTarget = new THREE.Vector3(800, 0, 1000)
camera.position.copy(initialCameraPosition)
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" })
renderer.domElement.className = "webgl-root"
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5))
renderer.outputColorSpace = THREE.SRGBColorSpace
host.replaceChildren(renderer.domElement)
const orbit = new OrbitControls(camera, renderer.domElement)
orbit.enableDamping = true
orbit.target.copy(initialOrbitTarget)
orbit.minDistance = 1200
orbit.maxDistance = 10000

const dimensions = { width: 270, height: 112, depth: 82 }
const spacing = { column: 360, row: 165, layer: 390 }
const colors = ["#63b3ff", "#f3b35d", "#50d890", "#b68cff", "#e96b78", "#d68cff", "#8cd9d0", "#ffffff"]
const centers = new Map()
const components = new Map()
const edgeDefinitions = []
const labels = []
const enabledLayers = new Set(Array.from({ length: n }, (_, i) => i))

function positionFor(cell) {
  const order = cell.order
  const x = cell.column * spacing.column - (order - 1) * spacing.column / 2
  const y = (cell.index + cell.column / 2 - (order - 1) / 2) * spacing.row
  const z = cell.layer * spacing.layer
  return new THREE.Vector3(x, y, z)
}

function wrapCanvasText(context, content, maxWidth, maxLines = 2) {
  const words = content.split(/\s+/)
  const lines = []
  let line = ""
  for (const word of words) {
    const candidate = line ? `${line} ${word}` : word
    if (context.measureText(candidate).width <= maxWidth) line = candidate
    else {
      if (line) lines.push(line)
      line = word
      if (lines.length === maxLines - 1) break
    }
  }
  if (line && lines.length < maxLines) lines.push(line)
  if (words.join(" ") !== lines.join(" ")) lines[lines.length - 1] = `${lines.at(-1).replace(/…$/, "").slice(0, -1)}…`
  return lines
}

function makeLabelSprite(cell) {
  const canvas = document.createElement("canvas")
  canvas.width = 384
  canvas.height = 144
  const context = canvas.getContext("2d")
  context.fillStyle = "#08141b"
  context.fillRect(0, 0, canvas.width, canvas.height)
  context.strokeStyle = colors[cell.layer]
  context.lineWidth = cell.status === "required" ? 5 : 3
  context.strokeRect(3, 3, canvas.width - 6, canvas.height - 6)
  context.textAlign = "center"
  context.textBaseline = "middle"
  context.fillStyle = "#eaf4f7"
  context.font = "600 25px ui-monospace, monospace"
  context.fillText(cell.id, canvas.width / 2, 29)
  context.font = "18px ui-monospace, monospace"
  context.fillStyle = "#b5c9d1"
  wrapCanvasText(context, cell.label, canvas.width - 34).forEach((line, i) => context.fillText(line, canvas.width / 2, 67 + i * 22))
  context.font = "16px ui-monospace, monospace"
  context.fillStyle = colors[cell.layer]
  context.fillText(`L${cell.layer} · C${cell.column}`, canvas.width / 2, 126)
  const texture = new THREE.CanvasTexture(canvas)
  texture.colorSpace = THREE.SRGBColorSpace
  texture.minFilter = THREE.LinearFilter
  texture.magFilter = THREE.LinearFilter
  const material = new THREE.SpriteMaterial({ map: texture, transparent: false, depthTest: true, depthWrite: false })
  const sprite = new THREE.Sprite(material)
  sprite.scale.set(246, 92, 1)
  return sprite
}

const boxGeometry = new THREE.BoxGeometry(dimensions.width, dimensions.height, dimensions.depth)
const boxMaterial = new THREE.MeshBasicMaterial({ vertexColors: true })
const boxInstances = new THREE.InstancedMesh(boxGeometry, boxMaterial, cells.length)
boxInstances.instanceMatrix.setUsage(THREE.DynamicDrawUsage)
scene.add(boxInstances)
const matrix = new THREE.Matrix4()
const scaleVisible = new THREE.Vector3(1, 1, 1)
const scaleHidden = new THREE.Vector3(0, 0, 0)

for (let instance = 0; instance < cells.length; instance++) {
  const cell = cells[instance]
  const center = positionFor(cell)
  centers.set(cell.id, center)
  boxInstances.setColorAt(instance, new THREE.Color(colors[cell.layer]))
  const sprite = makeLabelSprite(cell)
  scene.add(sprite)
  labels.push({ sprite, center, cell })
  components.set(cell.id, { cell, instance, sprite })
}
boxInstances.instanceColor.needsUpdate = true

function addCenterEdge(from, to, kind) {
  if (!centers.has(from) || !centers.has(to)) throw new Error(`edge endpoint missing: ${from} → ${to}`)
  edgeDefinitions.push({ from, to, kind })
}
for (const cell of cells) {
  if (cell.leftFace) addCenterEdge(cell.id, cell.leftFace, "L")
  if (cell.rightFace) addCenterEdge(cell.id, cell.rightFace, "R")
  if (cell.lowerSource) addCenterEdge(cell.id, cell.lowerSource, "Z")
}

let edgeMesh = null
const edgeColor = { L: new THREE.Color("#63b3ff"), R: new THREE.Color("#f3b35d"), Z: new THREE.Color("#b68cff") }
function rebuildEdges() {
  if (edgeMesh) {
    scene.remove(edgeMesh)
    edgeMesh.geometry.dispose()
  }
  const positions = []
  const edgeColors = []
  for (const edge of edgeDefinitions) {
    const fromLayer = components.get(edge.from).cell.layer
    const toLayer = components.get(edge.to).cell.layer
    if (!enabledLayers.has(fromLayer) || !enabledLayers.has(toLayer)) continue
    const a = centers.get(edge.from)
    const b = centers.get(edge.to)
    positions.push(a.x, a.y, a.z, b.x, b.y, b.z)
    const c = edgeColor[edge.kind]
    edgeColors.push(c.r, c.g, c.b, c.r, c.g, c.b)
  }
  const geometry = new THREE.BufferGeometry()
  geometry.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3))
  geometry.setAttribute("color", new THREE.Float32BufferAttribute(edgeColors, 3))
  edgeMesh = new THREE.LineSegments(geometry, new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity: 0.72 }))
  scene.add(edgeMesh)
}

function updateInstances() {
  for (const { cell, instance } of components.values()) {
    const scale = enabledLayers.has(cell.layer) ? scaleVisible : scaleHidden
    matrix.compose(centers.get(cell.id), camera.quaternion, scale)
    boxInstances.setMatrixAt(instance, matrix)
  }
  boxInstances.instanceMatrix.needsUpdate = true
}

controlsHost.replaceChildren()
function applyLayerVisibility() {
  for (const { cell, sprite } of components.values()) sprite.visible = enabledLayers.has(cell.layer)
  updateInstances()
  rebuildEdges()
  const master = controlsHost.querySelector('input[data-all-layers]')
  if (master) {
    master.checked = enabledLayers.size === n
    master.indeterminate = enabledLayers.size > 0 && enabledLayers.size < n
  }
}
function layerToggle(label, input) {
  const wrapper = document.createElement("label")
  wrapper.className = "layer-toggle"
  wrapper.append(input, document.createTextNode(label))
  return wrapper
}
const allInput = document.createElement("input")
allInput.type = "checkbox"
allInput.checked = true
allInput.dataset.allLayers = ""
allInput.addEventListener("change", () => {
  enabledLayers.clear()
  if (allInput.checked) for (let layer = 0; layer < n; layer++) enabledLayers.add(layer)
  controlsHost.querySelectorAll("input[data-layer]").forEach(input => { input.checked = allInput.checked })
  applyLayerVisibility()
})
controlsHost.append(layerToggle("all", allInput))
for (let layer = 0; layer < n; layer++) {
  const input = document.createElement("input")
  input.type = "checkbox"
  input.checked = true
  input.dataset.layer = String(layer)
  input.addEventListener("change", () => {
    if (input.checked) enabledLayers.add(layer)
    else enabledLayers.delete(layer)
    applyLayerVisibility()
  })
  controlsHost.append(layerToggle(`L${layer}`, input))
}
const resetView = document.createElement("button")
resetView.type = "button"
resetView.className = "reset-view"
resetView.textContent = "reset view"
resetView.addEventListener("click", () => {
  camera.position.copy(initialCameraPosition)
  camera.up.set(0, 1, 0)
  orbit.target.copy(initialOrbitTarget)
  orbit.update()
})
controlsHost.append(resetView)
applyLayerVisibility()
describe(cells.at(-1))

const raycaster = new THREE.Raycaster()
const pointer = new THREE.Vector2()
let pointerDown = null
renderer.domElement.addEventListener("pointerdown", event => { pointerDown = { x: event.clientX, y: event.clientY } })
renderer.domElement.addEventListener("pointerup", event => {
  if (!pointerDown || Math.hypot(event.clientX - pointerDown.x, event.clientY - pointerDown.y) > 5) return
  const rect = renderer.domElement.getBoundingClientRect()
  pointer.set((event.clientX - rect.left) / rect.width * 2 - 1, -(event.clientY - rect.top) / rect.height * 2 + 1)
  raycaster.setFromCamera(pointer, camera)
  const hit = raycaster.intersectObject(boxInstances, false)[0]
  if (hit?.instanceId !== undefined) {
    const cell = cells[hit.instanceId]
    if (enabledLayers.has(cell.layer)) describe(cell)
  }
})

function resize() {
  const width = Math.max(1, host.clientWidth)
  const height = Math.max(1, host.clientHeight)
  renderer.setSize(width, height, false)
  camera.aspect = width / height
  camera.updateProjectionMatrix()
}
new ResizeObserver(resize).observe(host)
resize()

const outward = new THREE.Vector3()
function animate() {
  requestAnimationFrame(animate)
  orbit.update()
  updateInstances()
  for (const { sprite, center } of labels) {
    outward.subVectors(camera.position, center).normalize()
    sprite.position.copy(center).addScaledVector(outward, dimensions.depth / 2 + 14)
  }
  renderer.render(scene, camera)
}
animate()
