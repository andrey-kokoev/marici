export const CELL_KINDS = Object.freeze({
  state: { dimension: 0 },
  process: { dimension: 1, axis: "process" },
  reconciliation: { dimension: 1, axis: "reconciliation" },
  transport: { dimension: 1, axis: "system-transport" },
  interchanger: { dimension: 2, plane: "process-reconciliation" },
  processPreservation: { dimension: 2, plane: "process-transport" },
  reconciliationPreservation: { dimension: 2, plane: "reconciliation-transport" },
  volumeCoherencer: { dimension: 3 },
})

export const STATUS = Object.freeze(["strict", "witnessed", "obstructed", "untyped", "inaccessible"])

const vertices = [
  [-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1],
  [-1, -1, 1], [1, -1, 1], [-1, 1, 1], [1, 1, 1],
]

const vertexCells = vertices.map((position, index) => ({
  id: `v${index}`,
  label: `state ${index}`,
  kind: "state",
  position,
  boundaryRefs: [],
  constructorRefs: ["source:typed-cube-fixture"],
  authority: "model",
  status: "strict",
}))

const edge = (id, label, kind, a, b) => ({
  id, label, kind, boundaryRefs: [`v${a}`, `v${b}`],
  constructorRefs: ["source:typed-cube-fixture"], authority: "model", status: "witnessed",
})

const face = (id, label, kind, boundaryRefs, status = "witnessed") => ({
  id, label, kind, boundaryRefs,
  constructorRefs: ["source:typed-cube-fixture"], authority: "conjectured", status,
})

export const typedCube = {
  kind: "marici-typed-cell-scene",
  schemaVersion: 1,
  id: "kitaev:typed-reconciler-cube:v1",
  title: "Two reconciliation dimensions plus transport coherencer",
  axes: {
    x: { kind: "process", label: "process / history" },
    y: { kind: "reconciliation", label: "reconciliation" },
    z: { kind: "system-transport", label: "system transport" },
  },
  evidence: [{
    id: "source:typed-cube-fixture",
    label: "Kitaev typed reconciliation-cube fixture",
    claimClass: "conjectured-model",
    locator: "research/kitaev",
  }],
  cells: [
    ...vertexCells,
    edge("px0", "process A0", "process", 0, 1), edge("px1", "process A1", "process", 2, 3),
    edge("px2", "process B0", "process", 4, 5), edge("px3", "process B1", "process", 6, 7),
    edge("ry0", "reconcile A0", "reconciliation", 0, 2), edge("ry1", "reconcile A1", "reconciliation", 1, 3),
    edge("ry2", "reconcile B0", "reconciliation", 4, 6), edge("ry3", "reconcile B1", "reconciliation", 5, 7),
    edge("tz0", "transport 0", "transport", 0, 4), edge("tz1", "transport 1", "transport", 1, 5),
    edge("tz2", "transport 2", "transport", 2, 6), edge("tz3", "transport 3", "transport", 3, 7),
    face("fa", "interchanger A", "interchanger", ["px0", "ry1", "px1", "ry0"]),
    face("fb", "interchanger B", "interchanger", ["px2", "ry3", "px3", "ry2"]),
    face("fp0", "process transport 0", "processPreservation", ["px0", "tz1", "px2", "tz0"]),
    face("fp1", "process transport 1", "processPreservation", ["px1", "tz3", "px3", "tz2"]),
    face("fr0", "reconciliation transport 0", "reconciliationPreservation", ["ry0", "tz2", "ry2", "tz0"]),
    face("fr1", "reconciliation transport 1", "reconciliationPreservation", ["ry1", "tz3", "ry3", "tz1"], "inaccessible"),
    {
      id: "omega", label: "volume coherencer", kind: "volumeCoherencer",
      boundaryRefs: ["fa", "fb", "fp0", "fp1", "fr0", "fr1"],
      constructorRefs: ["source:typed-cube-fixture"], authority: "conjectured", status: "obstructed",
    },
  ],
}

export function validateTypedScene(scene) {
  const errors = []
  if (scene.kind !== "marici-typed-cell-scene" || scene.schemaVersion !== 1) errors.push("schema mismatch")
  const evidence = new Set(scene.evidence.map(({ id }) => id))
  const ids = new Set()
  for (const cell of scene.cells) {
    if (ids.has(cell.id)) errors.push(`duplicate cell ${cell.id}`)
    ids.add(cell.id)
    const contract = CELL_KINDS[cell.kind]
    if (!contract) errors.push(`unknown kind ${cell.kind}`)
    if (!STATUS.includes(cell.status)) errors.push(`unknown status ${cell.status}`)
    if (!cell.constructorRefs.length) errors.push(`${cell.id}: missing constructor authority`)
    for (const ref of cell.constructorRefs) if (!evidence.has(ref)) errors.push(`${cell.id}: unknown source ${ref}`)
  }
  for (const cell of scene.cells) {
    const dimension = CELL_KINDS[cell.kind]?.dimension ?? -1
    for (const ref of cell.boundaryRefs) {
      const target = scene.cells.find((candidate) => candidate.id === ref)
      if (!target) errors.push(`${cell.id}: unknown boundary ${ref}`)
      else if ((CELL_KINDS[target.kind]?.dimension ?? 99) >= dimension) errors.push(`${cell.id}: boundary ${ref} is not lower-dimensional`)
    }
  }
  return { status: errors.length ? "invalid" : "valid", errors }
}
