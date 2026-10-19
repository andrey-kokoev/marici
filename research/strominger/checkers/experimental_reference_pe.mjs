// Explicit experimental extension. Not imported by production rules or viewers.
import assert from 'node:assert/strict';
export const POLICY='experimental-reference-mediated-PE-v1';
const sorted=xs=>[...xs].sort((a,b)=>a-b),clone=x=>structuredClone(x);
function context(r,ids,policy){
 if(policy!==POLICY)throw Error('Explicit experimental policy opt-in required');
 if(!Array.isArray(ids)||new Set(ids).size!==ids.length||ids.some(i=>!Number.isSafeInteger(i)||!r.packets[i]))throw Error('Invalid selected reader set');
 const selected=new Set(ids),ordered=sorted(selected),description=r.describe(ordered);
 if(!description.valid)throw Error('Invalid global role/species/contact context');
 const native=ordered.flatMap(id=>r.outgoing(id).map(i=>r.operations[i])).filter(op=>selected.has(op.target));
 return {selected,ordered,description,native};
}
export function constructReferencePE(r,ids,{pnId,neId,policy}={}){
 const c=context(r,ids,policy),pn=r.operations[pnId],ne=r.operations[neId];
 if(!pn||!ne||pn.kind!=='PN'||ne.kind!=='NE'||pn.target!==ne.source)throw Error('Actual consecutive PN/NE factors required');
 if(!r.outgoing(pn.source).includes(pnId)||!r.outgoing(ne.source).includes(neId))throw Error('Factors are not source-owned operations');
 r.validateTransfer(pn);r.validateTransfer(ne);
 const p=r.packets[pn.source],n=r.packets[pn.target],e=r.packets[ne.target];
 const pc=r.charts[p.chart],nc=r.charts[n.chart],ec=r.charts[e.chart];
 if(!c.selected.has(p.id)||!c.selected.has(e.id))throw Error('Both endpoint readers must be selected');
 if(pc.species!=='proton'||nc.species!=='neutron'||ec.species!=='electron')throw Error('Wrong reader types');
 if(new Set([pc.cell,nc.cell,ec.cell]).size!==3)throw Error('Three distinct body sites required');
 if(c.description.bodies.has(nc.cell))throw Error('Reference neutron body is occupied');
 if(pn.phaseDelta!==0||ne.phaseDelta!==0||p.origin!==n.origin||n.origin!==e.origin)throw Error('Grade-zero reference pair required');
 if(c.native.some(op=>op.source===p.id))throw Error('Selected proton reader is not terminal');
 if(r.outgoing(e.id).length!==0)throw Error('Electron reader is not native terminal');
 const edge=r.geometry.cells[pc.cell].vertices.filter(v=>r.geometry.cells[ec.cell].vertices.includes(v)).sort();
 assert.deepEqual(edge,[pc.aliases.C1,pc.aliases.M1].sort(),'Exact C1/M1 endpoint edge required');
 const permutation=ne.permutation.map(i=>pn.permutation[i]);
 assert.deepEqual(permutation.map(i=>p.permutation[i]),e.permutation,'Endpoint coefficient response mismatch');
 return {schema:'marici.experimental-reference-PE-constructor.v1',policy,admission:'experimental-only',native:false,
  kind:'reference-mediated-PE',source:p.id,target:e.id,origin:p.origin,grade:0,permutation,
  nativeFactors:[pnId,neId],nativeWord:clone([pn,ne]),occupiedSupport:sorted([pc.cell,ec.cell]),
  referenceSupport:sorted([pc.cell,nc.cell,ec.cell]),referenceNeutronCell:nc.cell,edge,
  referenceFrames:clone([p,n,e].map(packet=>({packet,chart:r.charts[packet.chart]}))),
  contextSelected:c.ordered,boundary:'source reader terminal in selected native graph; target native terminal'};
}
export function verifyReferencePE(r,ids,witness,{policy}={}){
 const expected=constructReferencePE(r,ids,{pnId:witness.nativeFactors?.[0],neId:witness.nativeFactors?.[1],policy});
 assert.deepEqual(witness,expected,'Stale or corrupted experimental constructor witness');
 return true;
}
export function referencePECandidates(r,ids,{policy}={}){
 const c=context(r,ids,policy),witnesses=[],rejections=[];
 for(const p of c.ordered){
  if(r.charts[r.packets[p].chart].species!=='proton')continue;
  for(const pnId of r.outgoing(p)){
   const pn=r.operations[pnId];if(pn.kind!=='PN')continue;
   if(c.description.bodies.has(r.charts[r.packets[pn.target].chart].cell))continue;
   for(const neId of r.outgoing(pn.target)){
    const ne=r.operations[neId];if(ne.kind!=='NE'||!c.selected.has(ne.target))continue;
    try{witnesses.push(constructReferencePE(r,ids,{pnId,neId,policy}));}
    catch(error){rejections.push({pnId,neId,reason:error.message});}
   }
  }
 }
 return {witnesses,rejections};
}
function reachability(r,ids,root,edges){
 const selected=new Set(ids),seen=new Set([root]),queue=[root],construction=[];
 for(let i=0;i<queue.length;i++)for(const op of edges)if(op.source===queue[i]&&!seen.has(op.target)){
  assert(selected.has(op.target));seen.add(op.target);queue.push(op.target);
  assert(r.describe(queue).valid,'Construction prefix violates original guards');
  let prefixWitness=null;
  if(op.kind==='reference-mediated-PE')prefixWitness=constructReferencePE(r,queue,{pnId:op.nativeFactors[0],neId:op.nativeFactors[1],policy:POLICY});
  else r.validateTransfer(op);
  construction.push({source:op.source,target:op.target,kind:op.kind,prefix:[...queue],prefixWitness});
 }
 const exits=ids.filter(id=>r.charts[r.packets[id].chart].species==='electron'),canExit=new Set(exits),back=[...exits];
 for(let i=0;i<back.length;i++)for(const op of edges)if(op.target===back[i]&&!canExit.has(op.source)){canExit.add(op.source);back.push(op.source);}
 return {unrooted:ids.filter(id=>!seen.has(id)),noExit:ids.filter(id=>!canExit.has(id)),construction};
}
export function auditReferencePEAssembly(r,ids,{root=r.root,expectedCounts,policy}={}){
 const c=context(r,ids,policy);if(!c.selected.has(root))throw Error('Root must be selected');
 if(!expectedCounts)throw Error('Explicit target counts required');
 const inspection=r.inspect(c.ordered);assert.deepEqual(inspection.counts,expectedCounts,'Wrong isotope counts');
 const {witnesses,rejections}=referencePECandidates(r,c.ordered,{policy});
 for(const witness of witnesses)verifyReferencePE(r,c.ordered,witness,{policy});
 const native=reachability(r,c.ordered,root,c.native),extended=reachability(r,c.ordered,root,[...c.native,...witnesses]);
 const nuclear=id=>r.charts[r.packets[id].chart].species!=='electron';
 assert.deepEqual(native.unrooted.filter(nuclear),extended.unrooted.filter(nuclear),'Sink-only extension changed nuclear reachability');
 // Occupied triangular contacts require NATIVE witnesses. An edge shortcut
 // cannot be counted as a replacement for a missing face witness.
 const nativePass=inspection.allContactsWitnessed&&native.unrooted.length===0&&native.noExit.length===0;
 const experimentalPass=inspection.allContactsWitnessed&&extended.unrooted.length===0&&extended.noExit.length===0;
 return {schema:'marici.experimental-reference-PE-assembly.v1',policy,admission:'experimental-only',selectedPackets:c.ordered,
  counts:inspection.counts,nativePass,experimentalPass,allOccupiedContactsNativelyWitnessed:inspection.allContactsWitnessed,
  pendingContacts:inspection.pendingContacts,witnesses,rejections,native,extended};
}
