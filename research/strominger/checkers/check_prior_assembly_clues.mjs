// Small fresh replay of prior Nima constructors; writes owner-local evidence only.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {enumerateAssemblies,GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const sources=['../../nima/generative-phase-assembly.mjs','../../nima/generative-phase-assembly-v1.md','../../nima/origin-bounded-assemblies-v1.md','../emergent-cm-incidence-audit-v1.md','../packet-handoff-naturality-06-v1.md','../../voevodsky/belt-three-by-twelve.md','../../voevodsky/three-tetrahedron-belt.md','../cmc-mcm-carrier-semantics-audit.md','../neutron-arrow-native-bridge.md',...['window-construction-model.mjs','lattice-items.mjs','simplex-components.mjs','carrier.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f),'./check_prior_assembly_clues.mjs'],hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};for(const f of sources)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
const run=enumerateAssemblies({maxTransitions:4,maxStates:1000});assert.equal(run.complete,true);assert.deepEqual(run.summary.minimalStageCounts,[1,2,6,21,82]);
let witness=null;
for(const node of run.nodes){
 if(!node.inspection.certifiedExit)continue;const d=run.rules.describe(node.packets),missing=[];
 for(const id of node.packets){const packet=run.rules.packets[id],c=run.rules.charts[packet.chart];if(c.species!=='neutron')continue;
  const face=['M0','C1','M1'].map(k=>c.aliases[k]),reference=run.rules.geometry.neighbor(c.cell,face);assert.equal(run.rules.geometry.cells[reference].geometry,'proton');
  if(!d.bodies.has(reference))missing.push({packet:id,neutronCell:c.cell,referenceCell:reference,referenceKey:run.rules.geometry.cells[reference].key});
 }
 if(missing.length){const steps=[];let at=node;while(at.parent!==null){const op=run.operations[at.operation];steps.push({kind:op.kind,phaseDelta:op.phaseDelta});at=run.nodes[at.parent];}steps.reverse();witness={node:node.id,counts:node.inspection.counts,selectedPackets:node.packets,missingOccupiedReferences:missing,allContactsWitnessed:node.inspection.allContactsWitnessed,allPacketsCanReachExit:node.inspection.allPacketsCanReachExit,constructionSteps:steps};break;}
}
assert.ok(witness,'Prior rules should exhibit a certified reference without an occupied P on every N native face');
function* permutations(a){if(!a.length)yield [];for(const x of a)for(const p of permutations(a.filter(y=>y!==x)))yield [x,...p];}
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),histogram={regularE:0,splitE:0};
for(const p of permutations([0,1,2,3])){
 const rules=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(['C0','M0','C1','M1'].map((k,i)=>[k,seed.vertices[p[i]].join(',')]))});
 const pn=rules.outgoing(rules.root).map(i=>rules.operations[i]).find(o=>o.kind==='PN');assert.ok(pn);
 const ne=rules.outgoing(pn.target).map(i=>rules.operations[i]).find(o=>o.kind==='NE');assert.ok(ne);rules.validateTransfer(pn);rules.validateTransfer(ne);
 const chart=rules.charts[rules.packets[ne.target].chart],g=rules.geometry.cells[chart.cell].geometry;histogram[g==='proton'?'regularE':'splitE']++;
}
assert.deepEqual(histogram,{regularE:8,splitE:16});
for(const f of sources)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);
const result={status:'prior-source-clues-and-small-replay-verified',sourceHashes,replay:{operationBound:4,complete:true,summary:run.summary,witness,seedMarkingTargetHistogram:histogram},scope:'Small current-source replay only; not a fresh nine-operation or D2 certification, N14 construction, whole-octahedron binding or physical model. Earlier full-source/belt/gluing results read but not independently rerun. Nima sources and receipts unchanged.'};
await mkdir('research/strominger/results/prior-assembly-clues',{recursive:true});await writeFile('research/strominger/results/prior-assembly-clues/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,configurations:run.summary.configurations,witness,seedMarkingTargetHistogram:histogram},null,2));
