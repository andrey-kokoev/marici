import test from 'node:test';import assert from 'node:assert/strict';
import {buildBeltParentPortInventory} from '../research/realization-tower/belt-parent-port-inventory.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {buildCentralBeltLayout} from '../research/realization-tower/central-belt-layout.mjs';
const audit=buildBeltParentPortInventory();
test('inventory retains both actual owner faces for every one of the 49 seam pairs',()=>{
 const owners=new Map(buildFoldedFibration().occurrences.map(o=>[o.id,o])),ports=new Map(audit.ports.map(p=>[p.id,p]));assert.equal(ports.size,98);
 for(const p of audit.ports){assert.deepEqual(p.nativeFace,owners.get(p.owner).faces[p.ownerFaceIndex]);assert.equal(p.nativeFace.length,3);assert.ok(p.area>0);assert.ok(Math.abs(Math.hypot(...p.outwardNormal)-1)<1e-10);assert.equal(ports.get(p.pairedPort).pairedPort,p.id);assert.equal(ports.get(p.pairedPort).seamPair,p.seamPair);assert.notEqual(ports.get(p.pairedPort).copy,p.copy);}
 for(const s of audit.summary){assert.equal(s.facePorts,49);assert.equal(s.uniqueOwners,49);assert.deepEqual(s.sourceParticleRoles,{neutron:23,proton:25,electron:1});}
});
test('requirements retain four balanced stars per parent with correct headings and rates',()=>{
 assert.equal(audit.requirements.length,32);
 for(const copy of ['original','clone'])for(let star=0;star<4;star++){
  const rs=audit.requirements.filter(r=>r.copy===copy&&r.star===star),central=rs.filter(r=>r.starCentre),satellites=rs.filter(r=>!r.starCentre);assert.equal(central.length,1);assert.equal(satellites.length,3);assert.equal(central[0].requiredFlux,3);assert.equal(central[0].flow,'belt-to-parent');assert.equal(central[0].transportDirection,copy==='original'?'P':'E');
  for(const r of satellites){assert.equal(r.requiredFlux,1);assert.equal(r.flow,'parent-to-belt');assert.equal(r.transportDirection,copy==='original'?'E':'P');}
 }
 for(const s of audit.summary){assert.equal(s.requiredIncomingFlux,12);assert.equal(s.requiredOutgoingFlux,12);}
});
test('missing direction, capacity and fiber contracts block assignment rather than inferring from roles',()=>{
 assert.equal(audit.status,'blocked-missing-parent-transport-contract');assert.equal(audit.assignment,null);for(const p of audit.ports){assert.equal(p.transportDirections,null);assert.equal(p.fluxCapacity,null);assert.equal(p.fiberBoundaryMap,null);}
 assert.equal(buildCentralBeltLayout().links.length,74,'inventory must not install speculative attachments');
});
