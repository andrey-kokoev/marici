import * as THREE from "three"
import { OrbitControls } from "three/addons/controls/OrbitControls.js"

const N = 7
const host = document.querySelector("#scene")
const detail = document.querySelector("#detail")
const input = document.querySelector("#coordinates")
const tooltip = document.querySelector("#tooltip")
const buildTime = document.querySelector("#build-time")
fetch("./__build-info", { cache: "no-store" })
  .then(response => response.ok ? response.json() : Promise.reject(new Error("build info unavailable")))
  .then(info => { buildTime.textContent = `last build: ${new Date(info.lastBuild).toLocaleString()}` })
  .catch(() => { buildTime.textContent = `last build: ${document.lastModified}` })

const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100)
camera.position.set(8.4, 6.5, 9.2)
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
renderer.setPixelRatio(Math.min(devicePixelRatio, 2))
host.append(renderer.domElement)
const controls = new OrbitControls(camera, renderer.domElement)
controls.enableDamping = true
controls.target.set(0, 0.15, 0)
scene.add(new THREE.HemisphereLight(0xc8efff, 0x101b24, 2.4))
const light = new THREE.DirectionalLight(0xffffff, 2.8)
light.position.set(5, 9, 7)
scene.add(light)

const root = new THREE.Group()
scene.add(root)
const highlightGroup = new THREE.Group()
scene.add(highlightGroup)

const corners = [
  new THREE.Vector3(-3.45, -2.35, 2.45),
  new THREE.Vector3(3.45, -2.35, 2.45),
  new THREE.Vector3(0, -2.35, -3.55),
  new THREE.Vector3(0, 3.65, 0.2),
]
const nodeGeometry = new THREE.SphereGeometry(0.085, 16, 12)
const normalMaterial = new THREE.MeshStandardMaterial({ color: 0xdcebf1, emissive: 0x10242d, roughness: 0.42 })
const selectedMaterial = new THREE.MeshStandardMaterial({ color: 0xffcb68, emissive: 0x6b3c08, roughness: 0.32 })
const nodes = []
const nodeByKey = new Map()

function key(c) { return c.join(",") }
function text(c) { return `(${c.join(",")})` }
function position(c) {
  const p = new THREE.Vector3()
  for (let i = 0; i < 4; i++) p.addScaledVector(corners[i], c[i] / N)
  return p
}
const cornerLabels = []
function makeLabel(label, p) {
  const el = document.createElement("div")
  el.className = "corner"
  el.textContent = label
  host.append(el)
  cornerLabels.push({ el, position: p.clone() })
}
function positionLabels() {
  const width = host.clientWidth
  const height = host.clientHeight
  for (const label of cornerLabels) {
    const projected = label.position.clone().project(camera)
    label.el.style.left = `${(projected.x * 0.5 + 0.5) * width}px`
    label.el.style.top = `${(-projected.y * 0.5 + 0.5) * height}px`
    label.el.style.display = projected.z > -1 && projected.z < 1 ? "block" : "none"
  }
}
function cylinder(a, b, material, radius = 0.012) {
  const d = new THREE.Vector3().subVectors(b, a)
  const mid = new THREE.Vector3().addVectors(a, b).multiplyScalar(0.5)
  const mesh = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, d.length(), 8), material)
  mesh.position.copy(mid)
  mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.clone().normalize())
  return mesh
}

for (let a = 0; a <= N; a++) {
  for (let b = 0; b <= N - a; b++) {
    for (let c = 0; c <= N - a - b; c++) {
      const coord = [a, b, c, N - a - b - c]
      const mesh = new THREE.Mesh(nodeGeometry, normalMaterial)
      mesh.position.copy(position(coord))
      mesh.userData.coord = coord
      root.add(mesh)
      nodes.push(mesh)
      nodeByKey.set(key(coord), mesh)
    }
  }
}

const edgeMaterial = new THREE.MeshBasicMaterial({ color: 0x315a6b, transparent: true, opacity: 0.38 })
for (const node of nodes) {
  const c = node.userData.coord
  for (let i = 0; i < 4; i++) {
    if (c[i] === 0) continue
    for (let j = i + 1; j < 4; j++) {
      const next = [...c]
      next[i]--
      next[j]++
      const other = nodeByKey.get(key(next))
      if (other) root.add(cylinder(node.position, other.position, edgeMaterial))
    }
  }
}

makeLabel("V₁  (7,0,0,0)", corners[0])
makeLabel("V₂  (0,7,0,0)", corners[1])
makeLabel("V₃  (0,0,7,0)", corners[2])
makeLabel("V₄  (0,0,0,7)", corners[3])

function parseCoordinates(value) {
  const groups = [...value.matchAll(/\(?\s*(\d+)\s*[, ]\s*(\d+)\s*[, ]\s*(\d+)\s*[, ]\s*(\d+)\s*\)?/g)]
  return groups.map(m => m.slice(1, 5).map(Number))
}
function valid(c) { return c.length === 4 && c.every(Number.isInteger) && c.every(x => x >= 0) && c.reduce((a, b) => a + b, 0) === N }
function adjacent(a, b) { return a.reduce((sum, x, i) => sum + Math.abs(x - b[i]), 0) === 2 }
function clearHighlight() {
  highlightGroup.clear()
  for (const node of nodes) node.material = normalMaterial
}
function showSelection(coords) {
  clearHighlight()
  if (coords.length < 1 || coords.length > 4) throw new Error("Enter between one and four coordinates.")
  if (coords.some(c => !valid(c))) throw new Error("Each coordinate must contain four nonnegative integers summing to 7.")
  if (new Set(coords.map(key)).size !== coords.length) throw new Error("Coordinates in one cell must be distinct.")
  const meshes = coords.map(c => nodeByKey.get(key(c)))
  for (const mesh of meshes) mesh.material = selectedMaterial
  const p = meshes.map(m => m.position)
  const gold = new THREE.MeshBasicMaterial({ color: 0xffcb68, transparent: true, opacity: 0.98, depthTest: false })
  const fill = new THREE.MeshBasicMaterial({ color: 0xffcb68, transparent: true, opacity: 0.16, side: THREE.DoubleSide, depthWrite: false })
  for (let i = 0; i < p.length; i++) for (let j = i + 1; j < p.length; j++) highlightGroup.add(cylinder(p[i], p[j], gold, 0.034))
  if (p.length === 3) {
    const geometry = new THREE.BufferGeometry().setFromPoints(p)
    geometry.setIndex([0, 1, 2])
    geometry.computeVertexNormals()
    highlightGroup.add(new THREE.Mesh(geometry, fill))
  }
  if (p.length === 4) {
    const geometry = new THREE.BufferGeometry().setFromPoints(p)
    geometry.setIndex([0,1,2, 0,3,1, 0,2,3, 1,3,2])
    geometry.computeVertexNormals()
    highlightGroup.add(new THREE.Mesh(geometry, fill))
  }
  const names = ["node", "edge", "face", "tetrahedron"]
  const elementary = coords.every((a, i) => coords.slice(i + 1).every(b => adjacent(a, b)))
  detail.innerHTML = `<strong>${names[coords.length - 1]} selected</strong>${coords.map(text).join("<br>")}<hr>${coords.length === 1 ? "lattice vertex" : elementary ? "elementary lattice cell" : "non-elementary coordinate span"}`
}

const ray = new THREE.Raycaster()
const pointer = new THREE.Vector2()
function pointFromEvent(event) {
  const rect = renderer.domElement.getBoundingClientRect()
  pointer.set((event.clientX - rect.left) / rect.width * 2 - 1, -(event.clientY - rect.top) / rect.height * 2 + 1)
  ray.setFromCamera(pointer, camera)
  return ray.intersectObjects(nodes, false)[0]
}
renderer.domElement.addEventListener("pointermove", event => {
  const hit = pointFromEvent(event)
  if (!hit) { tooltip.style.display = "none"; return }
  tooltip.textContent = text(hit.object.userData.coord)
  tooltip.style.left = `${event.clientX - host.getBoundingClientRect().left}px`
  tooltip.style.top = `${event.clientY - host.getBoundingClientRect().top}px`
  tooltip.style.display = "block"
})
renderer.domElement.addEventListener("pointerleave", () => { tooltip.style.display = "none" })
renderer.domElement.addEventListener("pointerdown", event => {
  const hit = pointFromEvent(event)
  if (!hit) return
  input.value = text(hit.object.userData.coord)
  showSelection([hit.object.userData.coord])
})

document.querySelector("#highlight").onclick = () => {
  try { showSelection(parseCoordinates(input.value)) }
  catch (error) { detail.innerHTML = `<strong>Invalid selection</strong>${error.message}` }
}
document.querySelector("#example").onclick = () => {
  input.value = "(0,0,3,4); (0,0,2,5); (1,0,2,4); (0,1,2,4)"
  showSelection(parseCoordinates(input.value))
}
document.querySelector("#clear").onclick = () => {
  input.value = ""
  clearHighlight()
  detail.innerHTML = "<strong>Coordinate selection</strong>Every coordinate must contain four nonnegative integers summing to 7."
}
document.querySelector("#reset").onclick = () => {
  camera.position.set(8.4, 6.5, 9.2)
  controls.target.set(0, 0.15, 0)
  controls.update()
}
input.addEventListener("keydown", event => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") document.querySelector("#highlight").click()
})

function resize() {
  const width = host.clientWidth
  const height = host.clientHeight
  camera.aspect = width / height
  camera.updateProjectionMatrix()
  renderer.setSize(width, height, false)
  positionLabels()
}
new ResizeObserver(resize).observe(host)
resize()
function frame() {
  controls.update()
  renderer.render(scene, camera)
  positionLabels()
  requestAnimationFrame(frame)
}
frame()
