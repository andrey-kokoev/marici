// A restriction of the declared global wire assignment, not a charged-cell
// transfer and not a conversion of comparison packets into wire contents.
import assert from 'node:assert/strict';
import {groupSulfurPayloads} from '../realization-tower/sulfur-32-wiring.mjs';
const clone=structuredClone;
const labels=['P+','P-','E+','E-'];
const grid=xs=>[xs.slice(0,2),xs.slice(2,4)];
function json(x){assert.deepEqual(JSON.parse(JSON.stringify(x)),x,'Wire rows must survive JSON encoding');}
export function referenceBoundaryContext(model,layout){
 const wires=new Map(model.wires.map(w=>[w.id,w]));
 const groupOf=physical=>{const gs=model.groups.filter(g=>g.members.some(m=>m.id===physical));assert.equal(gs.length,1);return gs[0];};
 const refs=labels.map(record=>{
  const cells=Object.entries(layout.template.referenceBinding).filter(([,r])=>r===record).map(([c])=>c);assert.equal(cells.length,1);
  const physicalCell=cells[0],g=groupOf(physicalCell),role=record[0]==='P'?'proton':'electron';assert.equal(g.role,role);
  const slots=[0,1,2,3].map(axis=>{const ws=model.wires.filter(w=>w.axis===axis&&(role==='proton'?w.source:w.target)===g.id);assert.equal(ws.length,1);return ws[0].id;});
  return {record,physicalCell,cell:g.id,slots,role};
 });
 const targetGroup=groupOf(layout.chart.target);assert.equal(targetGroup.role,'neutron');
 const channel=model.channels.find(c=>c.id===targetGroup.id);assert(channel);
 const observed=[...new Set(refs.flatMap(r=>r.slots))].sort(),targetWires=[...channel.slots];
 const missing=targetWires.filter(w=>!observed.includes(w)).sort();
 const anchor=clone(layout.anchor);
 const referenceFromMap=rows=>({anchor:clone(anchor),records:Object.fromEntries(refs.map(r=>[r.record,
  {physicalCell:r.physicalCell,cell:r.cell,slots:grid(r.slots.map(w=>clone(rows.get(w))))}]))});
 function globalRows(rows){
  json(rows);assert.equal(rows.length,model.wires.length);const map=new Map(rows.map(r=>[r.wire,r]));assert.equal(map.size,rows.length);
  for(const w of wires.keys())assert(map.has(w),'Missing global wire');return map;
 }
 function referenceProfile(rows){
  const map=globalRows(rows),profile=referenceFromMap(map);
  // Independently verify restriction against the existing global presentations.
  const presentations={proton:groupSulfurPayloads(model,rows,'P|E'),electron:groupSulfurPayloads(model,rows,'E|P')};
  for(const r of refs)assert.deepEqual(profile.records[r.record].slots,presentations[r.role].find(f=>f.cell===r.cell).slots);
  return profile;
 }
 function readReferences(profile){
  json(profile);const map=new Map();assert.deepEqual(profile.anchor,anchor);assert.deepEqual(Object.keys(profile.records).sort(),[...labels].sort());
  for(const r of refs){
   const p=profile.records[r.record];assert(Array.isArray(p.slots));const rows=p.slots.flat();assert.equal(rows.length,4);
   for(let i=0;i<4;i++){const row=rows[i];assert.equal(row.wire,r.slots[i],'Wrong reference slot/wire identity');
    if(map.has(row.wire))assert.deepEqual(map.get(row.wire),row,'Repeated wire records disagree');else map.set(row.wire,clone(row));}
  }
  assert.deepEqual(profile,referenceFromMap(map),'Reference metadata or slot shape changed');return map;
 }
 const targetFromMap=map=>({physicalCell:layout.chart.target,channel:channel.id,slots:grid(targetWires.map(w=>clone(map.get(w))))});
 function boundaryRows(rows){const map=globalRows(rows);return missing.map(w=>clone(map.get(w)));}
 function targetProfile(rows){return targetFromMap(globalRows(rows));}
 function forward(references,boundary){
  const map=readReferences(references);json(boundary);assert.deepEqual(boundary.map(r=>r.wire),missing,'Exact additional boundary rows required');
  for(const row of boundary)map.set(row.wire,clone(row));
  return {references:clone(references),target:targetFromMap(map)};
 }
 function recover(output){
  json(output);const map=readReferences(output.references),rows=output.target.slots.flat();assert.equal(rows.length,4);
  for(let i=0;i<4;i++){const row=rows[i];assert.equal(row.wire,targetWires[i],'Wrong target slot/wire identity');
   if(map.has(row.wire))assert.deepEqual(map.get(row.wire),row,'Reference/target overlap disagrees');else map.set(row.wire,clone(row));}
  const boundary=missing.map(w=>clone(map.get(w)));
  assert.deepEqual(output,forward(output.references,boundary),'Output metadata or retained context changed');
  return {references:clone(output.references),boundary};
 }
 return {observed,targetWires,missing,references:refs,anchor,
  routes:[...new Set([...observed,...targetWires])].map(w=>clone(wires.get(w))),
  referenceProfile,boundaryRows,targetProfile,forward,recover};
}
