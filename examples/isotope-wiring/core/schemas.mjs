import { defineSchema } from './finite-diagrams.mjs';

export const directedGraphSchema = defineSchema({
  id: 'isotope-wiring.directed-graph.v1',
  sorts: ['vertex', 'edge'],
  arrows: [
    { name: 'source', from: 'edge', to: 'vertex' },
    { name: 'target', from: 'edge', to: 'vertex' },
  ],
});

// Provisional incidence-only schema. This does NOT import the legacy drawing
// grammar, prescribe capacities, identify EP records physically, or encode a
// metric. Boundary support is named, not certified as a geometric closed cycle.
const arrow = (name, from, to) => ({ name, from, to });
const routeSlots = [
  { at: 'pair', owner: 'pairCell', edge: 'redEdge', start: 'redStart', end: 'redEnd' },
  { at: 'pair', owner: 'pairCell', edge: 'blueEdge', start: 'blueStart', end: 'blueEnd' },
  { at: 'lineWitness', owner: 'lineCell', edge: 'lineEdge', start: 'lineStart', end: 'lineEnd' },
];
export const isotopeIncidenceSchema = defineSchema({
  id: 'isotope-wiring.incidence-proposal.v0',
  sorts: ['shell', 'cell', 'port', 'vertex', 'edge', 'pair', 'lineWitness', 'boundary', 'boundaryWitness'],
  arrows: [
    arrow('cellShell', 'cell', 'shell'),
    arrow('portCell', 'port', 'cell'), arrow('portVertex', 'port', 'vertex'),
    arrow('source', 'edge', 'vertex'), arrow('target', 'edge', 'vertex'),
    arrow('pairCell', 'pair', 'cell'), arrow('lineCell', 'lineWitness', 'cell'),
    arrow('boundaryShell', 'boundary', 'shell'),
    arrow('witnessBoundary', 'boundaryWitness', 'boundary'),
    arrow('boundaryWitnessShell', 'boundaryWitness', 'shell'),
    ...routeSlots.flatMap(s => [arrow(s.edge, s.at, 'edge'), arrow(s.start, s.at, 'port'), arrow(s.end, s.at, 'port')]),
  ],
  equations: [
    ...routeSlots.flatMap(s => [
      { at: s.at, left: [s.start, 'portCell'], right: [s.owner] },
      { at: s.at, left: [s.end, 'portCell'], right: [s.owner] },
      { at: s.at, left: [s.start, 'portVertex'], right: [s.edge, 'source'] },
      { at: s.at, left: [s.end, 'portVertex'], right: [s.edge, 'target'] },
    ]),
    { at: 'boundaryWitness', left: ['witnessBoundary', 'boundaryShell'], right: ['boundaryWitnessShell'] },
  ],
});

// Directed route edges can refer to the same undirected support occurrence.
export const isotopeSupportSchema = defineSchema({
  ...isotopeIncidenceSchema,
  id: 'isotope-wiring.support-incidence.v1',
  sorts: [...isotopeIncidenceSchema.sorts, 'support'],
  arrows: [...isotopeIncidenceSchema.arrows, arrow('edgeSupport', 'edge', 'support')],
});
