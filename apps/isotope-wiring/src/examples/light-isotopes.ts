import { z } from "zod";
import { type DiagramDocument } from "../schemas/document.js";
import { authoredIsotope, AuthoredVertexSchema, AuthoredEdgeSchema } from "./authored-isotope.js";

// Shape references: legacy hydrogenSketch and He-4 crossed diamond.
// He-3 follows the operator correction: horizontal bar, no outer triangles.
// Colored arrows are explicitly authored here; the old H/He paths were all green.
const triangle = z.array(AuthoredVertexSchema).parse([
  ["left", -50, 0],
  ["top", 0, -50],
  ["right", 50, 0],
]);
const upper = z.array(AuthoredEdgeSchema).parse([
  [1, "top", "left", "red", []],
  [2, "right", "top", "blue", []],
]);
const diamond = z.array(AuthoredVertexSchema).parse([
  ["top", 0, -50],
  ["right", 50, 0],
  ["bottom", 0, 50],
  ["left", -50, 0],
]);
const sides = z
  .array(AuthoredEdgeSchema)
  .parse([...upper, [3, "right", "bottom", "red", []], [4, "bottom", "left", "blue", []]]);
export function hydrogen1(): DiagramDocument {
  return authoredIsotope({
    key: "h1",
    name: "Hydrogen-1",
    symbol: "H",
    protons: 1,
    neutrons: 0,
    vertices: triangle,
    edges: upper,
    undirectedEdges: [],
    viewBox: [-125, -75, 250, 150],
  });
}
export function hydrogen2(): DiagramDocument {
  return authoredIsotope({
    key: "h2",
    name: "Hydrogen-2",
    symbol: "H",
    protons: 1,
    neutrons: 1,
    vertices: triangle,
    edges: [...upper, [3, "left", "right", "green", []]],
    undirectedEdges: [3],
    viewBox: [-125, -75, 250, 150],
  });
}
export function helium3(): DiagramDocument {
  return authoredIsotope({
    key: "he3",
    name: "Helium-3",
    symbol: "He",
    protons: 2,
    neutrons: 1,
    vertices: diamond,
    edges: [
      ...upper,
      [3, "bottom", "right", "blue", []],
      [4, "left", "bottom", "red", []],
      [5, "left", "right", "green", []],
    ],
    undirectedEdges: [5],
    viewBox: [-125, -75, 250, 150],
  });
}
export function helium4(): DiagramDocument {
  return authoredIsotope({
    key: "he4",
    name: "Helium-4",
    symbol: "He",
    protons: 2,
    neutrons: 2,
    vertices: diamond,
    edges: [...sides, [5, "left", "right", "green", []], [6, "top", "bottom", "green", []]],
    undirectedEdges: [5, 6],
    viewBox: [-125, -75, 250, 150],
  });
}
