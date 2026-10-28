// Bounded probe: user P / (P,N,E,E) boundary versus existing occupied-body rules.
// This is NOT an identification of realization-cell types with particle species.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';

const rules = new GenerativeAssemblyRules();
const root = rules.packets[rules.root];
const center = rules.charts[root.chart].cell;
const faces = rules.geometry.cells[center].faces;
const neighbors = faces.map(face => rules.geometry.neighbor(center, face));
assert.equal(new Set(neighbors).size, 4);

// Exact necessary species-contact condition from GenerativeAssemblyRules.describe.
// C/M markings, geometry/species restrictions and operation witnesses are omitted:
// passing this relaxed condition would NOT establish actual native admission.
const source = fs.readFileSync(new URL('../demos/particle-overlap-tetrahedron/local-reference-rules.mjs', import.meta.url), 'utf8');
assert.ok(source.includes("species===other&&species!=='neutron'||pair.includes('proton')&&pair.includes('electron')"));
const species = {P:'proton', N:'neutron', E:'electron'};
function permitted(a,b) {
  a=species[a]; b=species[b]; const pair=[a,b];
  return !((a===b && a!=='neutron') || (pair.includes('proton') && pair.includes('electron')));
}
const assignments = [...new Set(function permute(xs) {
  if (!xs.length) return [''];
  return xs.flatMap((x,i)=>permute(xs.filter((_,j)=>i!==j)).map(t=>x+t));
}(['P','N','E','E']))];
const rows = assignments.map(types => ({types:[...types], failures:[...types].flatMap((t,i)=>permitted('P',t)?[]:[{neighbor:neighbors[i],contact:['P',t]}])}));
assert.equal(rows.length,12);
assert.ok(rows.every(row=>row.failures.length===3));

// Separate local consequence of this contact predicate, without pretending the
// rejected boundary is an admitted assembly. Does it always select a unique type?
const types=['P','N','E'];
const candidateTypes = incoming => types.filter(t=>incoming.every(s=>permitted(s,t)));
assert.deepEqual(candidateTypes(['P']),['N']);
assert.deepEqual(candidateTypes(['E']),['N']);
assert.deepEqual(candidateTypes(['N']),['P','N','E']);
assert.deepEqual(candidateTypes(['P','N']),['N']);
assert.deepEqual(candidateTypes(['N','N']),['P','N','E']);
console.log(JSON.stringify({
  scope:'Necessary occupied-body contact test under an explicit, unestablished type-to-species and face-adjacency adapter',
  center, neighbors, stage2Assignments:rows.length,
  admittedByNecessaryContactRule:rows.filter(row=>!row.failures.length).length,
  example:rows[0],
  localCandidateTable:[['P'],['N'],['E'],['P','N'],['N','N'],['P','E']].map(incoming=>({incoming,allowed:candidateTypes(incoming)})),
  stage3TypingComputed:false,
  userRealizationConjectureRefuted:false,
  conclusion:'Existing occupied-body rules do not admit the proposed boundary under this adapter; they cannot yet test realization-type forcing on it.'
},null,2));
