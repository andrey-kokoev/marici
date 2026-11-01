import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildSulfur32Wiring} from '../../realization-tower/sulfur-32-wiring.mjs';
import {buildNativeAxisPortGraph,faceKey} from '../native-axis-port-graph.mjs';
const root='research/strominger',contractPath=root+'/contracts/su32-edge5-native-bulk-v1.json';
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const smallSector=buildPESymmetricSector(1),largeSector=buildPESymmetricSector(2);
const small=buildNativeAxisPortGraph(smallSector),large=buildNativeAxisPortGraph(largeSector),closed=buildSulfur32Wiring();
const droppedFace=structuredClone(largeSector);droppedFace.cells[0].faces.pop();
assert.throws(()=>buildNativeAxisPortGraph(droppedFace));
const edgeKey=(a,b,kind)=>JSON.stringify([kind,...[a,b].sort()]);
// Exact calibration against the source's global quotient, using its actual lifts.
const portMap=new Map();for(const p of closed.ports)for(const l of p.lifts){
 const id=l.cell+'@'+faceKey(l.vertices);assert(!portMap.has(id)||portMap.get(id)===p.id);portMap.set(id,p.id);
}
assert.equal(portMap.size,small.ports.length);for(const p of small.ports)assert(portMap.has(p.id));
const closedPorts=new Map(closed.ports.map(p=>[p.id,p]));
for(const p of small.ports){const q=closedPorts.get(portMap.get(p.id));assert.equal(q.axis,p.axis);assert.equal(q.role,p.role);}
const closedEdges=new Map(closed.edges.map(e=>[edgeKey(e.from,e.to,e.kind),e]));
const image=new Set(small.edges.map(e=>{
 const k=edgeKey(portMap.get(e.from),portMap.get(e.to),e.kind==='shared-native-face'?'shared-quotient-face':e.kind);
 assert(closedEdges.has(k),'Source quotient did not preserve a bulk edge');return k;
}));
const seams=[...closedEdges].filter(([k])=>!image.has(k)).map(([,e])=>e);
assert(seams.every(e=>e.kind==='shared-quotient-face'));assert.equal(seams.length,closed.seamLinks.length);assert.equal(seams.length,24);
assert.equal(new Set(portMap.values()).size,closed.ports.length);
const beforeWire=new Map();for(const w of closed.wires)for(const p of w.ports)beforeWire.set(p,w.id);
for(const c of small.components)assert.equal(new Set(c.ports.map(p=>beforeWire.get(portMap.get(p)))).size,1);
// Reconstruct closed components independently from mapped bulk plus declared seams.
const allEdges=[...image].map(k=>closedEdges.get(k)).concat(seams),adj=new Map(closed.ports.map(p=>[p.id,[]]));
for(const e of allEdges){adj.get(e.from).push(e.to);adj.get(e.to).push(e.from);}
const unseen=new Set(adj.keys()),reconstructed=[];
while(unseen.size){const todo=[unseen.values().next().value];unseen.delete(todo[0]);
 for(let i=0;i<todo.length;i++)for(const q of adj.get(todo[i]))if(unseen.delete(q))todo.push(q);
 reconstructed.push(todo.sort());
}
assert.deepEqual(reconstructed.map(x=>JSON.stringify(x)).sort(),closed.wires.map(w=>JSON.stringify([...w.ports].sort())).sort());
function capacity(sector,graph){
 const ports=new Map(graph.ports.map(p=>[p.id,p]));
 const degrees=new Map(sector.cells.filter(c=>c.role==='neutron').map(c=>[c.id,0]));
 for(const e of graph.edges.filter(e=>e.kind==='shared-native-face'))for(const id of [e.from,e.to]){
  const p=ports.get(id);if(p.role==='neutron')degrees.set(p.cell,degrees.get(p.cell)+1);
 }
 const low=[...degrees].filter(([,d])=>d===4),high=[...degrees].filter(([,d])=>d>4);
 assert([...degrees.values()].every(d=>d>=4&&d<=8));
 const admissiblePairs=[];for(const [a,da] of degrees)for(const [b,db] of degrees)if(a<b&&da+db<=8){
  assert.equal(da,4);assert.equal(db,4);admissiblePairs.push([a,b]);
 }
 // Three distinct physical N cells already contribute at least twelve retained
 // incidences. A class containing any degree>4 cell cannot contain another cell.
 assert(3*Math.min(...degrees.values())>8);
 const lowerBound=high.length+Math.ceil(low.length/2);
 const P=sector.cells.filter(c=>c.role==='proton').length,E=sector.cells.filter(c=>c.role==='electron').length;assert.equal(P,E);
 return {degrees:Object.fromEntries(degrees),histogram:Object.fromEntries([...new Set(degrees.values())].sort().map(d=>[d,[...degrees.values()].filter(x=>x===d).length])),
  possibleCapacityPairs:admissiblePairs,minimumNCellFibres:lowerBound,
  requiredNCellFibresForLiteralInterface:P,requiredWireSlots:4*P,
  necessaryConditionPasses:lowerBound<=P,
  reason:'A class has capacity eight. Every degree>4 cell must be singleton; degree-four cells can be grouped at most in pairs.'};
}
const sourceCapacity=capacity(smallSector,small),edge5Capacity=capacity(largeSector,large);
assert.equal(sourceCapacity.minimumNCellFibres,16);assert.equal(sourceCapacity.necessaryConditionPasses,true);
for(const g of closed.groups.filter(g=>g.role==='neutron')){
 const used=g.members.reduce((s,m)=>s+sourceCapacity.degrees[m.id],0);assert(used<=8);
}
assert.equal(edge5Capacity.minimumNCellFibres,82);assert.equal(edge5Capacity.requiredNCellFibresForLiteralInterface,80);
assert.equal(edge5Capacity.necessaryConditionPasses,false);
// Native bulk conservation: one value per component, no hidden copying or merging.
const values=new Map(large.components.map((c,i)=>[c.id,{opaque:[i,false,null],component:c.id}]));
const atPort=new Map(large.components.flatMap(c=>c.ports.map(p=>[p,structuredClone(values.get(c.id))])));
for(const e of large.edges)assert.deepEqual(atPort.get(e.from),atPort.get(e.to));
for(const c of large.components){const recovered=c.ports.map(p=>atPort.get(p));assert(recovered.every(v=>JSON.stringify(v)===JSON.stringify(values.get(c.id))));}
const perAxis=[0,1,2,3].map(axis=>({axis,components:large.components.filter(c=>c.axis===axis).length,
 complete:large.components.filter(c=>c.axis===axis&&c.kind==='complete-PNE').length,
 openN:large.components.filter(c=>c.axis===axis&&c.kind==='open-N-half').length,
 openCharged:large.components.filter(c=>c.axis===axis&&c.kind==='open-charged-port').length}));
const sourceHashes={};for(const p of [contractPath,root+'/native-axis-port-graph.mjs',root+'/pe-symmetric-sector.mjs',
 root+'/checkers/check_su32_edge5_native_bulk.mjs','research/realization-tower/sulfur-32-wiring.mjs'])sourceHashes[p]=await digest(p);
const result={schema:'su32.edge5-native-bulk.v1',passed:true,literalClosureNecessaryConditionPassed:false,
 negativeControls:{droppedNativeFaceRejected:true,nonTipMergingExceedsEightPortCapacity:true}, 
 calibration:{open:small.counts,physicalPorts:portMap.size,quotientPorts:closed.ports.length,declaredSeamsAdded:seams.length,
 reconstructedWires:reconstructed.length,exactSourceComponentsRecovered:true,capacity:sourceCapacity},
 edgeFive:{counts:large.counts,perAxis,capacity:edge5Capacity,graph:large,closure:null},
 conclusion:'The calibrated native rule constructs the complete open edge-five bulk. A literal whole-cell, nonbranching copy of the edge-three closure interface fails the N-port capacity bound (at least 82 N fibres, but 80 required).',
 limits:['Conditional on retaining all 80 P/E fibres and every native face incidence, eight ports per N fibre and exactly one N channel per wire.',
 '320 denotes axis-labelled wire slots under the inherited four-port interface, not a claim of 320 independent physical contents.',
 'No impossibility of a more general edge-five fibration, contextual operation or different global attachment law is inferred.',
 'No boundary pairing, period lattice, N-N seam or extra mixing operation is silently installed.'],sourceHashes};
const dir=root+'/results/su32-edge5-native-bulk-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,literalClosureNecessaryConditionPassed:false,
 calibration:{...result.calibration,capacity:sourceCapacity.histogram},
 edgeFive:{counts:large.counts,perAxis,degreeHistogram:edge5Capacity.histogram,
 minimumNCellFibres:edge5Capacity.minimumNCellFibres,requiredNCellFibres:80},conclusion:result.conclusion,limits:result.limits},null,2));
