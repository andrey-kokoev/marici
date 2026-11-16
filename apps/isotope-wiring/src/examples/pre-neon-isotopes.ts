import { type DiagramDocument } from "../schemas/document.js";
import { AuthoredDrawingSchema, authoredIsotope } from "./authored-isotope.js";

// Explicit ports and incidence, manually authored against DRAWING_RECIPES and
// the Li6 named drawing. Reuse here follows those named recipes, not Z/N counts.
const li6 = AuthoredDrawingSchema.parse({
  key: "li6",
  name: "Lithium-6",
  symbol: "Li",
  protons: 3,
  neutrons: 3,
  vertices: [
    ["top", 0, 34],
    ["left", -50, 84],
    ["right", 50, 84],
    ["center", 0, 134],
    ["lower-left", -50, 184],
    ["lower-right", 50, 184],
  ],
  edges: [
    [1, "top", "left", "red", []],
    [2, "right", "top", "blue", []],
    [3, "right", "center", "red", []],
    [4, "center", "left", "blue", []],
    [5, "left", "right", "green", []],
    [6, "center", "lower-right", "red", []],
    [7, "lower-left", "center", "blue", []],
    [8, "lower-left", "lower-right", "green", []],
  ],
  undirectedEdges: [5, 8],
  viewBox: [-86, 14, 172, 200],
});
const li7 = AuthoredDrawingSchema.parse({
  ...li6,
  key: "li7",
  name: "Lithium-7",
  neutrons: 4,
  edges: [
    ...li6.edges,
    [9, "left", "lower-left", "green", []],
    [10, "right", "lower-right", "green", []],
  ],
  undirectedEdges: [5, 8, 9, 10],
});
const be9 = AuthoredDrawingSchema.parse({
  ...li7,
  key: "be9",
  name: "Beryllium-9",
  symbol: "Be",
  protons: 4,
  neutrons: 5,
  vertices: [...li7.vertices, ["bottom", 0, 234]],
  edges: [
    ...li7.edges,
    [11, "bottom", "lower-right", "red", []],
    [12, "lower-left", "bottom", "blue", []],
  ],
  viewBox: [-86, 14, 172, 250],
});
// B10 reflects the Li6 base only; the added upper diamond is not reflected.
// The reflected incidence and arrow endpoints are written explicitly below.
const b10 = AuthoredDrawingSchema.parse({
  key: "b10",
  name: "Boron-10",
  symbol: "B",
  protons: 5,
  neutrons: 5,
  vertices: [
    ...li6.vertices,
    ["upper-tip", 0, -66],
    ["upper-left", -50, -16],
    ["upper-right", 50, -16],
  ],
  edges: [
    [1, "top", "right", "red", []],
    [2, "left", "top", "blue", []],
    [3, "left", "center", "red", []],
    [4, "center", "right", "blue", []],
    [5, "left", "right", "green", []],
    [6, "center", "lower-left", "red", []],
    [7, "lower-right", "center", "blue", []],
    [8, "lower-left", "lower-right", "green", []],
    [9, "upper-tip", "upper-left", "red", []],
    [10, "upper-right", "upper-tip", "blue", []],
    [11, "upper-right", "top", "red", []],
    [12, "top", "upper-left", "blue", []],
    [13, "upper-left", "upper-right", "green", []],
  ],
  undirectedEdges: [5, 8, 13],
  viewBox: [-86, -86, 172, 300],
});
const b11 = AuthoredDrawingSchema.parse({
  ...b10,
  key: "b11",
  name: "Boron-11",
  neutrons: 6,
  edges: [
    ...b10.edges,
    [14, "upper-left", "lower-left", "green", []],
    [15, "upper-right", "lower-right", "green", []],
  ],
  undirectedEdges: [5, 8, 13, 14, 15],
});
const c12 = AuthoredDrawingSchema.parse({
  ...b10,
  key: "c12",
  name: "Carbon-12",
  symbol: "C",
  protons: 6,
  neutrons: 6,
  vertices: [...b10.vertices, ["bottom", 0, 234]],
  edges: [
    ...b10.edges,
    [14, "lower-right", "bottom", "red", []],
    [15, "bottom", "lower-left", "blue", []],
  ],
  viewBox: [-86, -86, 172, 350],
});
const c13 = AuthoredDrawingSchema.parse({
  ...c12,
  key: "c13",
  name: "Carbon-13",
  neutrons: 7,
  edges: [
    ...c12.edges,
    [16, "upper-left", "lower-left", "green", []],
    [17, "upper-right", "lower-right", "green", []],
  ],
  undirectedEdges: [5, 8, 13, 16, 17],
});
const n14 = AuthoredDrawingSchema.parse({
  ...c12,
  key: "n14",
  name: "Nitrogen-14",
  symbol: "N",
  protons: 7,
  neutrons: 7,
  vertices: [...c12.vertices, ["nitrogen-left", -50, 284], ["nitrogen-right", 50, 284]],
  edges: [
    ...c12.edges,
    [16, "bottom", "nitrogen-right", "red", []],
    [17, "nitrogen-left", "bottom", "blue", []],
    [18, "nitrogen-right", "nitrogen-left", "green", []],
  ],
  undirectedEdges: [5, 8, 13, 18],
  viewBox: [-86, -86, 172, 400],
});
const n15 = AuthoredDrawingSchema.parse({
  ...n14,
  key: "n15",
  name: "Nitrogen-15",
  neutrons: 8,
  edges: [
    ...n14.edges,
    [19, "upper-left", "nitrogen-left", "green", []],
    [20, "upper-right", "nitrogen-right", "green", []],
  ],
  undirectedEdges: [5, 8, 13, 18, 19, 20],
});
const o16 = AuthoredDrawingSchema.parse({
  ...n14,
  key: "o16",
  name: "Oxygen-16",
  symbol: "O",
  protons: 8,
  neutrons: 8,
  vertices: [...n14.vertices, ["oxygen-bottom", 0, 334]],
  edges: [
    ...n14.edges,
    [19, "oxygen-bottom", "nitrogen-right", "red", []],
    [20, "nitrogen-left", "oxygen-bottom", "blue", []],
  ],
  viewBox: [-86, -86, 172, 450],
});
const o17 = AuthoredDrawingSchema.parse({
  ...o16,
  key: "o17",
  name: "Oxygen-17",
  neutrons: 9,
  edges: [
    ...o16.edges,
    [21, "upper-left", "nitrogen-left", "green", []],
    [22, "upper-right", "nitrogen-right", "green", []],
  ],
  undirectedEdges: [5, 8, 13, 18, 21, 22],
});
const o18 = AuthoredDrawingSchema.parse({
  ...o16,
  key: "o18",
  name: "Oxygen-18",
  neutrons: 10,
  edges: [
    ...o16.edges,
    [21, "upper-left", "lower-left", "green", []],
    [22, "upper-right", "lower-right", "green", []],
    [
      23,
      "left",
      "nitrogen-left",
      "green",
      [
        [-60, 84],
        [-60, 284],
      ],
    ],
    [
      24,
      "right",
      "nitrogen-right",
      "green",
      [
        [60, 84],
        [60, 284],
      ],
    ],
  ],
  undirectedEdges: [5, 8, 13, 18, 21, 22, 23, 24],
});
const f19 = AuthoredDrawingSchema.parse({
  ...o18,
  key: "f19",
  name: "Fluorine-19",
  symbol: "F",
  protons: 9,
  vertices: [...o18.vertices, ["fluorine-left", -50, 384], ["fluorine-right", 50, 384]],
  edges: [
    ...o16.edges,
    [21, "upper-left", "lower-left", "green", []],
    [22, "upper-right", "lower-right", "green", []],
    [23, "lower-left", "fluorine-left", "green", []],
    [24, "lower-right", "fluorine-right", "green", []],
    [25, "oxygen-bottom", "fluorine-left", "red", []],
    [26, "fluorine-right", "oxygen-bottom", "blue", []],
    [27, "fluorine-left", "fluorine-right", "green", []],
  ],
  undirectedEdges: [5, 8, 13, 18, 21, 22, 23, 24, 27],
  viewBox: [-86, -86, 172, 500],
});

export function lithium6(): DiagramDocument {
  return authoredIsotope(li6);
}
export function lithium7(): DiagramDocument {
  return authoredIsotope(li7);
}
export function beryllium9(): DiagramDocument {
  return authoredIsotope(be9);
}
export function boron10(): DiagramDocument {
  return authoredIsotope(b10);
}
export function boron11(): DiagramDocument {
  return authoredIsotope(b11);
}
export function carbon12(): DiagramDocument {
  return authoredIsotope(c12);
}
export function carbon13(): DiagramDocument {
  return authoredIsotope(c13);
}
export function nitrogen14(): DiagramDocument {
  return authoredIsotope(n14);
}
export function nitrogen15(): DiagramDocument {
  return authoredIsotope(n15);
}
export function oxygen16(): DiagramDocument {
  return authoredIsotope(o16);
}
export function oxygen17(): DiagramDocument {
  return authoredIsotope(o17);
}
export function oxygen18(): DiagramDocument {
  return authoredIsotope(o18);
}
export function fluorine19(): DiagramDocument {
  return authoredIsotope(f19);
}
