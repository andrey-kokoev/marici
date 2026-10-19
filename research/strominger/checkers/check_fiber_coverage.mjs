import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {auditStateCoverage,windowPrefixGraph,auditWindowCoverage} from '../demos/particle-overlap-tetrahedron/fiber-coverage-model.mjs';
import {createWindowConstruction,windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {makeLatticeItem,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {lattice,faces} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {lead208AddedBodies} from '../demos/particle-overlap-tetrahedron/lead208-model.mjs';
const required=lattice.cells.map(c=>itemKey(c.map(id=>lattice.nodes[id].address))),idByKey=new Map(required.map((k,i)=>[k,i]));
const engine=createWindowConstruction(),prefix=engine.snapshot();
const pending=auditWindowCoverage(prefix,required);assert.equal(pending.status,'pending-boundary');assert.equal(pending.fromEntryCells,1);assert.equal(pending.coveredCells,0);assert.deepEqual(pending.deadEndCells,[]);assert.equal(pending.allEnteredStatesReachExit,null);
engine.step();const intermediate=auditWindowCoverage(engine.snapshot(),required);assert.equal(intermediate.fromEntryCells,2);assert.equal(intermediate.coveredCells,0);
engine.step();const final=engine.snapshot(),graph=windowPrefixGraph(final),coverage=auditWindowCoverage(final,required);
assert.equal(graph.states.length,3);assert.equal(graph.transitions.length,2);assert.equal(graph.exitStates.length,1);
assert.equal(coverage.status,'incomplete');assert.equal(coverage.entryExitRouteExists,true);assert.equal(coverage.coveredCells,3);assert.equal(coverage.unmodeledCells.length,340);
assert.deepEqual(coverage.coveredCellKeys.map(k=>idByKey.get(k)),[0,13,16]);
assert.equal(auditWindowCoverage(final,final.items.map(s=>s.key)).status,'covered');
for(const mutate of [s=>s.mode.branch='positive',s=>s.history.splice(4,1),s=>s.events[1].orderedFace.reverse(),s=>s.bindings.C1[0]=999]){
 const bad=structuredClone(final);mutate(bad);assert.throws(()=>windowPrefixGraph(bad),'Unadmitted windows/history/phases must not become graph edges');
}
// Distinct frame/history states on the same cells must not be spliced together.
const splice={states:[0,1].flatMap(phase=>['A','X','Z'].map(cell=>({id:cell+phase,cell,mode:{phaseExponent:phase}}))),transitions:[['A0','X0'],['X0','Z0'],['A1','X1'],['X1','Z1']],entryStates:['A0'],exitStates:['Z1'],requiredCells:['A','X','Z']};
const rejected=auditStateCoverage(splice);assert.equal(rejected.coveredCells,0);assert.equal(rejected.rows.filter(r=>r.fromEntry&&r.toExit).length,3);assert.equal(rejected.incompatibleStateCells.length,3);assert.equal(rejected.deadEndStateIds.length,3);assert.equal(rejected.allEnteredStatesReachExit,false);
// Branching is permitted: no Hamiltonian traversal or electron-to-proton edge.
const branch={states:['s','a','b','e1','e2'].map(id=>({id,cell:id})),transitions:[['s','a'],['s','b'],['a','e1'],['b','e2']],entryStates:['s'],exitStates:['e1','e2'],requiredCells:['s','a','b','e1','e2']};
assert.equal(auditStateCoverage(branch).status,'covered');
const dead=auditStateCoverage({...branch,states:[...branch.states,{id:'dead',cell:'dead'}],transitions:[...branch.transitions,['a','dead']],requiredCells:[...branch.requiredCells,'dead']});assert.deepEqual(dead.deadEndCells,['dead']);assert.equal(dead.status,'incomplete');
assert.throws(()=>auditStateCoverage({...branch,transitions:[...branch.transitions,['e1','a']]}));
assert.throws(()=>auditStateCoverage({...branch,transitions:[['s','missing']]}));
// Geometry-only hostile: bare face incidence appears to cover the whole space,
// even though it carries no ordered windows or phases and is NOT admitted.
const incidence=new Map();
for(const [id,cell] of lattice.cells.entries())for(const f of faces){const k=f.map(i=>cell[i]).sort((a,b)=>a-b).join(',');if(!incidence.has(k))incidence.set(k,[]);incidence.get(k).push(id);}
const terminal=idByKey.get(final.items.at(-1).key),geometryEdges=[];
for(const owners of incidence.values())if(owners.length===2){const [a,b]=owners;if(a!==terminal)geometryEdges.push(['g'+a,'g'+b]);if(b!==terminal)geometryEdges.push(['g'+b,'g'+a]);}
const bare=auditStateCoverage({states:required.map((cell,i)=>({id:'g'+i,cell})),transitions:geometryEdges,entryStates:['g0'],exitStates:['g'+terminal],requiredCells:required});assert.equal(bare.coveredCells,343);
// Alternative seed markings are separate experiments, not simultaneous branches.
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),alternativeUnion=new Set(),alternatives=[];
for(const permutation of permutations([0,1,2,3])){
 const bindings=Object.fromEntries(windowProtocol[0].nodes.map((n,i)=>[n,seed.vertices[permutation[i]]]));
 const run=createWindowConstruction({bindings});run.step();run.step();const c=auditWindowCoverage(run.snapshot(),required);
 assert.equal(c.coveredCells,3);c.coveredCellKeys.forEach(k=>alternativeUnion.add(k));alternatives.push({permutation,coveredCells:c.coveredCellKeys.map(k=>idByKey.get(k))});
}
assert.equal(alternativeUnion.size,15);
const layerCoverage=lattice.assembly.layers.map(layer=>{const cells=layer.items.flatMap(i=>i.children);return {layer:layer.id,items:layer.items.length,primitiveCells:cells.length,covered:cells.filter(id=>coverage.coveredCellKeys.includes(required[id])).length,alternativeMarkingUnion:cells.filter(id=>alternativeUnion.has(required[id])).length};});
const touched=lattice.assembly.items.filter(i=>i.children.some(id=>coverage.coveredCellKeys.includes(required[id]))).length;
const fullyCovered=lattice.assembly.items.filter(i=>i.children.every(id=>coverage.coveredCellKeys.includes(required[id]))).length;
const extended=[...required,...lead208AddedBodies.flatMap(b=>b.components.map(itemKey))];assert.equal(new Set(extended).size,761);
const extendedCoverage=auditWindowCoverage(final,extended);assert.equal(extendedCoverage.coveredCells,3);
const report={status:'coverage-condition-tested-not-satisfied-globally',condition:'Intersect forward-from-entry and backward-from-exit reachability on admitted marked states, then project onto cells.',
 currentWindow:{states:3,covered:coverage.coveredCells,total:343,coveredCellIds:coverage.coveredCellKeys.map(k=>idByKey.get(k)),unmodeledCells:coverage.unmodeledCells.length,assemblyItemsTouched:touched,assemblyItemsFullyCovered:fullyCovered,assemblyItemsTotal:175},layerCoverage,
 extendedPbSpace:{covered:extendedCoverage.coveredCells,total:extended.length,admission:'Only the root window is admitted; legacy Pb packets are not connected to the entry by fiat.'},
 geometryOnlyControl:{covered:bare.coveredCells,total:343,admitted:false},alternativeSeedMarks:{experiments:24,unionCovered:alternativeUnion.size,unionIsNotOneCoherentConstruction:true,alternatives},
 controls:{incompatibleSameCellStatesRejected:true,branchesAccepted:true,deadEndsDetected:true,noForwardContinuationFromExit:true,mutatedWindowPacketsRejected:true},
 conclusion:'The criterion distinguishes geometric connectivity from valid window-state coverage. Current rules admit only the root P–N–E packet, not the branching transfers needed to cover the whole lattice. This is missing model coverage, not an impossibility theorem.'};
const out='research/strominger/results/fiber-coverage';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,windowCoverage:'3/343',extendedSpaceCoverage:'3/761',layerCoverage,alternativeMarkingUnion:alternativeUnion.size,bareAdjacencyCoverage:'343/343 (not window-admitted)'},null,2));
