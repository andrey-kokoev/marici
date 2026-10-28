import test from 'node:test';import assert from 'node:assert/strict';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {trimParentHalfStep} from '../research/realization-tower/p-first-parent-trim.mjs';
import {filterBeltView} from '../examples/normal-ray/complex-visibility.js';
import {buildPneInventory} from '../examples/normal-ray/pne-inventory.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const source=()=>processState('double-esd7',7,0,1,{rimAssembly:true});
test('half-step removes only outer P cells, protects E tips and leaves source/belt unchanged',()=>{
 const p=source(),snapshot=JSON.stringify(p),q=trimParentHalfStep(p);assert.equal(JSON.stringify(p),snapshot);assert.equal(q.beltSurface,p.beltSurface);assert.equal(q.attachmentBodies,p.attachmentBodies);
 assert.deepEqual(q.parentTrimAudit.removed,{proton:146,neutron:0,electron:0});assert.deepEqual(q.parentTrimAudit.remaining,{proton:20,neutron:112,electron:72});assert.equal(q.parentTrimAudit.protectedTipIds.length,2);
 for(const id of q.parentTrimAudit.protectedTipIds)assert.ok([...q.retainedBodies,...q.emptyBodies].some(c=>c.id===id));
 const g=filterBeltView(q,'geometry');for(const s of g.parentCellulations){const boundary=s.faces.filter(f=>f.owners.length===1),edgeCounts=new Map();for(const f of boundary)for(let i=0;i<3;i++){const k=[f.indices[i],f.indices[(i+1)%3]].sort((a,b)=>a-b).join(',');edgeCounts.set(k,(edgeCounts.get(k)??0)+1);}assert.ok([...edgeCounts.values()].every(n=>n===2));assert.equal(boundary.length,270);}
});
test('trimmed graph remains connected with both contacts, but the surface-face bias worsens',()=>{
 const p=trimParentHalfStep(source()),w=filterBeltView(p,'wiring'),g=w.nativeWiringGraph;
 assert.equal(g.nodes.length,238);assert.equal(g.links.length,428);assert.equal(w.nativeWiringAudit.tipContactLinks,2);assert.deepEqual(w.nativeWiringAudit.nodeRoles,{proton:30,neutron:126,electron:82});
 const reached=new Set([g.nodes[0].id]);for(let changed=true;changed;){changed=false;for(const e of g.links)if(reached.has(e.from)||reached.has(e.to))for(const id of[e.from,e.to])if(!reached.has(id)){reached.add(id);changed=true;}}assert.equal(reached.size,238);
 const rows=buildPneInventory(p).displayRows;assert.deepEqual([rows[0].proton,rows[0].electron],[366,174]);assert.deepEqual([rows[2].proton,rows[2].neutron,rows[2].electron],[398,126,206]);
});
test('trim is explicit, persisted, and inactive outside separated assembly',()=>{
 assert.equal(normalizeSceneSettings({}).appearance.parentHalfStepTrim,false);assert.equal(normalizeSceneSettings({appearance:{parentHalfStepTrim:true}}).appearance.parentHalfStepTrim,true);
 assert.equal(source().parentTrimAudit,undefined);assert.equal(processState('double-esd7',7,0,1,{parentHalfStepTrim:true,rimAssembly:false}).parentTrimAudit,undefined);
 assert.equal(processState('double-esd7',7,0,1,{parentHalfStepTrim:true,rimAssembly:true}).parentTrimAudit.removed.proton,146);
});
