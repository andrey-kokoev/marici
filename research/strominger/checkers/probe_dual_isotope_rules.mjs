// Direction-indexed experimental dual. Its admission is pulled back through
// an explicit involution, NOT a newly derived physical interaction law.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
import {phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const swap=s=>({proton:'electron',electron:'proton',neutron:'neutron'})[s],flip=s=>s==='M'?'C':'M',inv=p=>p.map((_,i)=>p.indexOf(i)),copy=structuredClone;
const orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]};
function reverse(a){
 const frame=f=>{const all=[...f.window,f.context].map(o=>({...o,role:flip(o.role),index:a.K-o.index})),v=orders[f.species].map(i=>all[i]);return {...f,species:swap(f.species),window:v.slice(0,3),context:v[3]};};
 return {direction:-a.direction,K:a.K,bodies:a.bodies.map(b=>({...b,species:swap(b.species)})),frames:a.frames.map(frame),edges:a.edges.map(e=>({...e,source:e.target,target:e.source,permutation:inv(e.permutation)})),entries:[...a.exits],exits:[...a.entries],roles:a.roles.map(([v,r])=>[v,flip(r)])};
}
function reachable(roots,edges){const found=new Set(roots),q=[...roots];for(let i=0;i<q.length;i++)for(const e of edges)if(e.source===q[i]&&!found.has(e.target)){found.add(e.target);q.push(e.target);}return found;}
const terminalFile='research/strominger/results/terminal-pe-probe/verification.json',terminal=JSON.parse(await readFile(terminalFile)),results=[],sourceHashes={};
for(const isotope of ['n15','o16']){
 const base=`research/strominger/results/reference-${isotope}-search`,summary=JSON.parse(await readFile(base+'/verification.json')),row=summary.rows.find(r=>r.witnessFile),file=base+'/'+row.witnessFile,bytes=await readFile(file),w=JSON.parse(bytes).witness;sourceHashes[file]=createHash('sha256').update(bytes).digest('hex');
 const variants=[{name:isotope,ids:w.selectedPackets,shortcuts:[]}];if(isotope==='n15')for(const d of terminal.deletions.filter(d=>d.sourceIsotope==='n15'&&d.variants['electron-and-proton-record-terminal'].passesHypotheticalChecks))variants.push({name:'n14-delete-'+d.deletedNeutron.cell,ids:d.selectedPackets,shortcuts:d.shortcuts.filter(o=>o.recordTerminal)});
 for(const v of variants){
  const {rules:r}=phaseUniverse({maxOrigin:row.maxOrigin,maxPackets:5000}),ids=v.ids,selected=new Set(ids),chart=p=>r.charts[r.packets[p].chart],cell=p=>chart(p).cell,d=r.describe(ids);assert.equal(d.valid,true);
  const native=ids.flatMap(p=>r.outgoing(p).map(i=>r.operations[i])).filter(o=>selected.has(o.target));for(const o of native)r.validateTransfer(o);
  for(const o of v.shortcuts){const [pn,ne]=o.nativeFactors.map(i=>r.operations[i]);r.validateTransfer(pn);r.validateTransfer(ne);assert.equal(pn.source,o.source);assert.equal(ne.target,o.target);assert.equal(pn.target,ne.source);assert.ok(!d.bodies.has(cell(pn.target)));assert.deepEqual(o.permutation,ne.permutation.map(i=>pn.permutation[i]));assert.equal(r.outgoing(o.target).length,0);assert.ok(!native.some(e=>e.source===o.source));}
  const frames=ids.map(p=>({...phaseFrame(chart(p),r.packets[p].origin),packet:p})),K=Math.max(...frames.flatMap(f=>[...f.window,f.context].map(o=>o.index)));
  const forward={direction:1,K,bodies:[...d.bodies].map(([cell,species])=>({cell,species,geometry:r.geometry.cells[cell].geometry,vertices:r.geometry.cells[cell].vertices})),frames,edges:[...native,...v.shortcuts].map((e,i)=>({id:i,source:e.source,target:e.target,permutation:e.permutation,originalKind:e.kind})),entries:[r.root],exits:ids.filter(p=>chart(p).species==='electron'),roles:[...d.roles]};
  assert.equal(reachable(forward.entries,forward.edges).size,ids.length);assert.equal(reachable(forward.exits,forward.edges.map(e=>({source:e.target,target:e.source}))).size,ids.length);
  const dual=reverse(forward);assert.deepEqual(reverse(dual),forward);
  function validate(a){
   assert.equal(a.direction,-1);const pulled=reverse(a);
   // A dual certificate must pull back to the complete already-audited source
   // certificate, not merely preserve counts or an arbitrary graph.
   assert.deepEqual(pulled,forward);
   assert.ok(a.frames.every(f=>auditPhaseFrame(f).status==='native-template-compatible'));
   // Geometry classes transport with the reader species: dual E corresponds
   // to native P and must be regular, dual N stays split, dual P may be either.
   for(const b of a.bodies){if(b.species==='electron')assert.equal(b.geometry,'proton');if(b.species==='neutron')assert.equal(b.geometry,'split');}
   const roles=new Map(a.roles),species=new Map(a.bodies.map(b=>[b.cell,b.species]));
   for(const c of d.contacts){const pair=c.cells.map(cell=>species.get(cell)),kind=pair.includes('electron')?'NE':pair[0]===pair[1]?'NN':'PN',m=c.face.filter(p=>roles.get(p)==='M').length;assert.equal(m,kind==='NE'?1:2);}
   assert.equal(reachable(a.entries,a.edges).size,a.frames.length);assert.equal(reachable(a.exits,a.edges.map(e=>({source:e.target,target:e.source}))).size,a.frames.length);
   return true;
  }
  assert.equal(validate(dual),true);
  const badMap=copy(dual);[badMap.edges[0].permutation[0],badMap.edges[0].permutation[1]]=[badMap.edges[0].permutation[1],badMap.edges[0].permutation[0]];assert.throws(()=>validate(badMap));
  const badRole=copy(dual);badRole.frames[0].window[0].role=flip(badRole.frames[0].window[0].role);assert.throws(()=>validate(badRole));
  const badBoundary=copy(dual);badBoundary.entries=badBoundary.entries.slice(0,1);assert.throws(()=>validate(badBoundary));
  const bestSingle=Math.max(...dual.entries.map(p=>reachable([p],dual.edges).size));assert.ok(bestSingle<ids.length);
  const nn=d.contacts.filter(c=>c.kind==='NN').length;assert.ok(nn>0);
  results.push({name:v.name,records:ids.length,bodyCounts:Object.fromEntries(['proton','neutron','electron'].map(s=>[s,dual.bodies.filter(b=>b.species===s).length])),contacts:d.contacts.length,dualNNFaces:nn,entries:dual.entries.length,entryBodies:new Set(dual.entries.map(cell)).size,exits:dual.exits.length,bestSingleEntryRecords:bestSingle,fullBoundaryPass:true,doubleReversalExact:true,nativeForwardSource:v.shortcuts.length===0,experimentalPEShortcuts:v.shortcuts.length,negativeControls:{corruptMapRejected:true,corruptRoleRejected:true,collapsedBoundaryRejected:true},dual});
 }
}
for(const file of ['research/strominger/checkers/probe_dual_isotope_rules.mjs',terminalFile,'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs'])sourceHashes[file]=createHash('sha256').update(await readFile(file)).digest('hex');
const out='research/strominger/results/dual-isotope-rules';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'transported-dual-certificates-pass',sourceHashes,results,scope:'Experimental direction-indexed rules defined by pullback through the stated involution. Passing shows internal consistency of transported certificates, not discovery of a new forward witness, derivation of P/E physical equivalence or mode-space Riesz duality. N-14 source already assumes terminal PE. No production/viewer changes.'},null,2)+'\n');console.log(JSON.stringify(results.map(({dual,...r})=>r),null,2));
