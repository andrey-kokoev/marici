import test from 'node:test';import assert from 'node:assert/strict';
import {presentCentralBelt,centralBeltEnvelope,buildCentralBeltLayout} from '../research/realization-tower/central-belt-layout.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {filterBeltView,filterComplexVisibility} from '../examples/normal-ray/complex-visibility.js';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {geometryParentPoint,geometryParentShift} from '../examples/normal-ray/belt-geometry-layout.js';
import {wiringParentPoint,nativeWiringInventory} from '../examples/normal-ray/native-belt-wiring.js';
const source=()=>presentCentralBelt(doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id))),distance=(a,b)=>Math.hypot(...a.map((v,i)=>v-b[i]));
test('native dual replaces synthetic ports with 384 real cells and 794 witnessed links',()=>{
 const p=source(),snapshot=JSON.stringify(p),v=filterBeltView(p,'wiring'),g=v.nativeWiringGraph,a=v.nativeWiringAudit;
 assert.equal(a.nodeCount,384);assert.equal(a.beltNodes,34);assert.equal(a.terminalBundleNodes,0);assert.equal(a.sharedFaceLinks,792);assert.equal(a.tipContactLinks,2);assert.equal(a.directedLinks,0);assert.deepEqual(a.nodeRoles,{proton:176,neutron:126,electron:82});assert.deepEqual(a.planes.map(p=>p.count),[1,4,4,6,4,6,4,4,1]);assert.equal(g.links.length,794);assert.equal(v.beltGraphLinks.length,0);assert.equal(v.terminalBundles.length,0);
 const nodes=new Map(g.nodes.map(n=>[n.id,n])),faceKey=f=>f.map(p=>p.map(x=>Number(x.toFixed(7))).join(',')).sort().join('|'),reached=new Set([g.nodes[0].id]);
 for(const e of g.links){assert.ok(nodes.has(e.from)&&nodes.has(e.to));assert.equal(e.directed,false);if(e.kind==='native-face'){const faces=new Set(nodes.get(e.from).body.faces.map(faceKey));assert.equal(nodes.get(e.to).body.faces.filter(f=>faces.has(faceKey(f))).length,1);}else{assert.equal(e.kind,'native-tip-contact');assert.equal(e.sharedVertices.length,1);assert.equal(nodes.get(e.from).body.role,'electron');assert.equal(nodes.get(e.to).body.nativeWiring.shape,'belt');}}
 for(let changed=true;changed;){changed=false;for(const e of g.links)if(reached.has(e.from)||reached.has(e.to))for(const id of [e.from,e.to])if(!reached.has(id)){reached.add(id);changed=true;}}assert.equal(reached.size,384);
 assert.deepEqual(nativeWiringInventory(p).displayRows.map(r=>[r.proton,r.neutron,r.electron,r.total]),[[166,112,72,350],[10,14,10,34],[176,126,82,384]]);assert.equal(JSON.stringify(p),snapshot);
});
test('geometry retains unit edges, axis alignment, two E-tip contacts and no rays',()=>{
 const p=source(),v=filterBeltView(p,'geometry'),s=v.beltSurface,origin=worldPoint(p.centralBeltAudit.origin),normal=p.centralBeltAudit.normal;
 assert.equal(s.counts.faces,64);assert.equal(v.geometryLayoutAudit.parentShift,geometryParentShift);assert.equal(v.parentEdgeRays.length,0);
 for(const e of s.cellulation.edges)assert.ok(Math.abs(distance(...e.indices.map(i=>s.cellulation.vertices[i]))-s.cellulation.unitEdge)<1e-10);
 for(const id of p.parentCutAudit.removedCellIds){const before=p.retainedBodies.find(b=>b.id===id),after=v.retainedBodies.find(b=>b.id===id),tipIndex=before.vertices.findIndex(p=>distance(worldPoint(p),origin)<1e-10),tip=worldPoint(after.vertices[tipIndex]);assert.equal(after.role,'electron');assert.ok(Math.min(...s.vertices.map(p=>distance(p,tip)))<1e-10);}
 for(const sign of [1,-1]){const projection=p=>sign*p.reduce((sum,x,i)=>sum+(x-origin[i])*normal[i],0);assert.ok(s.vertices.every(p=>projection(p)<=geometryParentShift+1e-10));for(const b of [...v.retainedBodies,...v.emptyBodies].filter(b=>b.id.startsWith(sign===1?'original:':'clone:')))assert.ok(b.vertices.every(p=>projection(worldPoint(p))>=geometryParentShift-1e-10));}
 for(const [i,p] of centralBeltEnvelope.entries()){const copy=i<4?'original':'clone';assert.ok(distance(worldPoint(wiringParentPoint(p,copy,buildCentralBeltLayout())),worldPoint(geometryParentPoint(p,copy,buildCentralBeltLayout())))>0);}
});
test('native plane and parent visibility remove nodes and all incident links',()=>{
 const p=source(),check=v=>{const ids=new Set(v.nativeWiringGraph.nodes.map(n=>n.id));assert.ok(v.nativeWiringGraph.links.every(e=>ids.has(e.from)&&ids.has(e.to)));};
 for(let i=0;i<9;i++){const mask=Array(9).fill(true);mask[i]=false;const v=filterBeltView(p,'wiring',{nativeBeltLayers:mask});assert.equal(v.nativeWiringAudit.nodeCount,384-v.nativeWiringAudit.planes[i].count);assert.equal(v.nativeWiringAudit.tipContactLinks,[0,8].includes(i)?1:2);check(v);}
 const none=filterBeltView(p,'wiring',{nativeBeltLayers:Array(9).fill(false)});assert.equal(none.nativeWiringAudit.nodeCount,350);assert.equal(none.nativeWiringAudit.tipContactLinks,0);check(none);
 for(const visibility of [{original:false},{clone:false},{belt:false}]){const v=filterBeltView(filterComplexVisibility(p,visibility),'wiring');assert.equal(v.nativeWiringAudit.nodeCount,visibility.belt===false?350:209);assert.equal(v.nativeWiringAudit.tipContactLinks,visibility.belt===false?0:1);check(v);}
});
