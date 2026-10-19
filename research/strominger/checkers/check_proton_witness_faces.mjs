// Exact finite witness-capacity and exterior-boundary audit. Source rules unchanged.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../demos/particle-overlap-tetrahedron/local-reference-universe.mjs';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/proton-witness-faces/',import.meta.url);
const hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
async function load(path){const b=await readFile(new URL(path,ROOT));sourceHashes[path]=hash(b);return JSON.parse(b);}
function matching(left,neighbors){
 const owner=new Map();
 function augment(a,seen){for(const b of neighbors.get(a)??[]){if(seen.has(b))continue;seen.add(b);if(!owner.has(b)||augment(owner.get(b),seen)){owner.set(b,a);return true;}}return false;}
 for(const a of left)augment(a,new Set());
 const unmatched=left.filter(a=>![...owner.values()].includes(a)),hallLeft=new Set(unmatched),hallRight=new Set(),queue=[...unmatched];
 for(let i=0;i<queue.length;i++)for(const b of neighbors.get(queue[i])??[]){hallRight.add(b);if(owner.has(b)&&!hallLeft.has(owner.get(b))){hallLeft.add(owner.get(b));queue.push(owner.get(b));}}
 if(unmatched.length)assert(hallLeft.size>hallRight.size,'Maximum matching must expose a Hall deficit');
 return {size:owner.size,assignment:[...owner].map(([slot,neutron])=>({neutron,slot})),unmatched,
         hallDeficit:unmatched.length?{neutrons:[...hallLeft],slots:[...hallRight],deficit:hallLeft.size-hallRight.size}:null};
}
function audit(r,ids,name,certificate){
 const d=r.describe(ids);assert(d.valid);const protons=[...d.bodies].filter(([,s])=>s==='proton').map(([c])=>c),neutrons=[...d.bodies].filter(([,s])=>s==='neutron').map(([c])=>c);
 const occupied=new Set(d.bodies.keys()),points=[...occupied].flatMap(c=>r.geometry.cells[c].vertices.map(v=>v.split(',').map(Number)));
 const bounds=[0,1,2,3].map(i=>({min:Math.min(...points.map(p=>p[i])),max:Math.max(...points.map(p=>p[i]))}));
 const exteriorMemo=new Map(),cavityComponents=[];let floodVisits=0;
 function exterior(seed){
  assert(!occupied.has(seed));if(exteriorMemo.has(seed))return exteriorMemo.get(seed);
  const seen=new Set([seed]),queue=[seed];let verdict=null;
  for(let i=0;i<queue.length;i++){
   if(queue.length>100000){verdict='unknown-resource-stop';break;}
   const c=queue[i];floodVisits++;
   if(exteriorMemo.has(c)){verdict=exteriorMemo.get(c);break;}
   const cell=r.geometry.cells[c];
   if(cell.vertices.some(v=>v.split(',').map(Number).some((x,j)=>x<bounds[j].min||x>bounds[j].max))){verdict='exterior';break;}
   for(const f of cell.faces){const n=r.geometry.neighbor(c,f);if(!occupied.has(n)&&!seen.has(n)){seen.add(n);queue.push(n);}}
  }
  if(verdict===null){
   verdict='bounded-cavity';const boundary=[];
   for(const c of seen)for(const face of r.geometry.cells[c].faces){const n=r.geometry.neighbor(c,face);assert(seen.has(n)||occupied.has(n));if(occupied.has(n))boundary.push({vacantCell:c,occupiedNeighbor:n,face});}
   cavityComponents.push({cells:[...seen].sort((a,b)=>a-b),geometry:[...seen].map(c=>({cell:c,vertices:r.geometry.cells[c].vertices})),boundary,allBoundaryNeighborsOccupied:true});
  }
  if(verdict!=='unknown-resource-stop')for(const c of seen)exteriorMemo.set(c,verdict);
  return verdict;
 }
 const byNeutron=new Map(neutrons.map(n=>[n,[]])),byNeutronFace=new Map(neutrons.map(n=>[n,[]])),faces=[];
 for(const p of protons){
  const pf=r.geometry.cells[p].faces;assert.equal(pf.length,4);let eligible=0;
  for(let i=0;i<pf.length;i++){
   const face=pf[i],m=face.filter(v=>d.roles.get(v)==='M').length;if(m===2)eligible++;
   const n=r.geometry.neighbor(p,face),species=d.bodies.get(n),slot=`${p}:${i}`;
   if(species){assert.equal(species,'neutron');assert.equal(m,2);byNeutron.get(n).push(p);byNeutronFace.get(n).push(slot);}
   faces.push({proton:p,faceIndex:i,vertices:face,MCount:m,neighbor:n,neighborSpecies:species??null,
               witness:species==='neutron'?'neutron':exterior(n),neutron:species==='neutron'?n:null});
  }
  assert.equal(eligible,2,'Source MMCC tetrahedron must have exactly two MCM faces');
 }
 const body=matching(neutrons,byNeutron),face=matching(neutrons,byNeutronFace);
 const isolated=neutrons.filter(n=>byNeutron.get(n).length===0);
 assert.equal(face.unmatched.length,isolated.length,'Face identities cannot be shared by distinct neighboring neutrons');
 const boundary=faces.filter(f=>f.witness==='exterior'),cavities=faces.filter(f=>f.witness==='bounded-cavity'),unknown=faces.filter(f=>f.witness==='unknown-resource-stop');
 const allProtonFacesClosed=cavities.length===0&&unknown.length===0;
 const assigned=new Set(body.assignment.map(a=>a.slot));
 const remainingProtonsAdmissible=protons.filter(p=>!assigned.has(p)).every(p=>faces.some(f=>f.proton===p&&(f.witness==='exterior'||f.witness==='neutron')));
 const bodyPass=body.unmatched.length===0&&remainingProtonsAdmissible;
 const facePass=face.unmatched.length===0&&allProtonFacesClosed;
 const shared=protons.map(p=>({proton:p,neutrons:faces.filter(f=>f.proton===p&&f.witness==='neutron').map(f=>f.neutron)})).filter(x=>x.neutrons.length>1);
 return {name,certificate,counts:{proton:protons.length,neutron:neutrons.length,electron:[...d.bodies.values()].filter(s=>s==='electron').length},
         bodyRule:{passes:bodyPass,...body},faceRule:{passes:facePass,...face,isolatedNeutrons:isolated},
         protonFaces:{total:faces.length,eligibleMCM:2*protons.length,neutronWitnessed:faces.filter(f=>f.witness==='neutron').length,
                      exterior:boundary.length,cavity:cavities.length,unknown:unknown.length},
         multiNeutronProtons:shared,faces,floodVisits,cavityComponents,
         occupiedGeometry:[...d.bodies].map(([cell,species])=>({cell,species,vertices:r.geometry.cells[cell].vertices})),
         scope:'Boundary tokens label exposed faces connected to infinity. They are not electrons, amplitudes, closure dynamics, or additional particles.'};
}
async function saved(isotope){
 const base=`research/strominger/results/reference-${isotope}-search/`,summary=await load(base+'verification.json'),row=summary.rows.find(x=>x.witnessFile);assert(row);
 const w=(await load(base+row.witnessFile)).witness,u=phaseUniverse({maxOrigin:row.maxOrigin});assert(u.complete);
 for(const p of w.packets)assert.deepEqual(u.rules.packets[p.id],p);
 for(const o of w.operations)assert.deepEqual(u.rules.operations[o.id],o);
 assert(u.rules.inspect(w.selectedPackets).certifiedExit);
 return {r:u.rules,w};
}
function verifyCavity(row,component){
 const all=[...row.occupiedGeometry,...component.geometry],componentIds=new Set(component.cells),occupiedIds=new Set(row.occupiedGeometry.map(c=>c.cell));
 assert(component.cells.every(c=>!occupiedIds.has(c)));
 const faceIndices=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
 for(const c of component.geometry)for(const indices of faceIndices){
  const face=indices.map(i=>c.vertices[i]),neighbors=all.filter(other=>other.cell!==c.cell&&face.every(v=>other.vertices.includes(v)));
  assert.equal(neighbors.length,1,'Cavity face has no unique retained geometric neighbor');
  assert(componentIds.has(neighbors[0].cell)||occupiedIds.has(neighbors[0].cell));
 }
 return true;
}
const protocol=await load('research/strominger/inputs/proton-witness-protocol-v1.json'),rows=[];
const h=new GenerativeAssemblyRules(),p=h.root,pn=h.operations[h.outgoing(p).find(i=>h.operations[i].kind==='PN')],n=pn.target,ne=h.operations[h.outgoing(n).find(i=>h.operations[i].kind==='NE')],e=ne.target;
rows.push(audit(h,[p,e],'H1','experimental PE geometry; prior constructor certificate'));
rows.push(audit(h,[p,n,e],'H2','native PN-NE'));
for(const isotope of ['n15','o16','o17','o18','f19','ne20','ne22','na23']){
 const {r,w}=await saved(isotope);rows.push(audit(r,w.selectedPackets,isotope,'saved native local-reference witness, fresh packet/operation/exit replay'));
}
const old=await load('research/strominger/results/isotope-obstruction-atlas/verification.json');assert.equal(old.status,'pass');
for(const [family,names] of [['n15-single',['n15:delete:16','n15:delete:17']],['ne22-single',['ne22:delete:16','ne22:delete:29']],['ne22-double',['ne22:delete-pair:16,29']]]){
 const {r}=await saved(family.startsWith('n15')?'n15':'ne22');
 for(const name of names){const candidate=old.families[family].find(x=>x.label===name);assert(candidate?.fullAuditPass);rows.push(audit(r,candidate.selectedPackets,name,'saved experimental fixed-footprint PE certificate'));}
}
assert(rows.find(r=>r.name==='H2').bodyRule.passes);
assert(rows.filter(r=>r.counts.neutron>r.counts.proton).every(r=>!r.bodyRule.passes));
assert(rows.some(r=>r.multiNeutronProtons.length>0));
assert(rows.some(r=>r.cavityComponents.length>0),'Need actual counterevidence to treating every vacant neighbor as outer closure');
assert(rows.filter(r=>r.cavityComponents.length).every(r=>!r.faceRule.passes));
let cavityChecks=0;
for(const row of rows)for(const component of row.cavityComponents){
 assert(verifyCavity(row,component));cavityChecks++;
 const corrupted=structuredClone(row),missing=component.boundary[0].occupiedNeighbor;
 corrupted.occupiedGeometry=corrupted.occupiedGeometry.filter(c=>c.cell!==missing);
 assert.throws(()=>verifyCavity(corrupted,component),'Missing enclosing body must break the cavity certificate');
}
// Hostile to the body-capacity model: collapsing distinct faces loses coverage.
const faceBetter=rows.filter(r=>r.faceRule.size>r.bodyRule.size);assert(faceBetter.length>0);
for(const path of ['research/strominger/checkers/check_proton_witness_faces.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-universe.mjs'])sourceHashes[path]=hash(await readFile(new URL(path,ROOT)));
const result={schema:'marici.proton-witness-faces.v1',status:'pass',protocol,sourceHashes,rows,cavityCertificatesIndependentlyChecked:cavityChecks,
 hostileRejections:['body-capacity-collapse-loses-neutron-coverage','vacant-neighbor-is-not-necessarily-exterior','deleted-enclosing-body-breaks-cavity-certificate'],
 disposition:'Separate compatibility of the new body/face hypotheses from existing source certification; rejected native constructions remain counterevidence, not silently repaired.',
 allFaceRulePass:rows.every(r=>r.faceRule.passes),resourceUnknown:rows.some(r=>r.protonFaces.unknown>0)};
await mkdir(OUT,{recursive:true});await writeFile(new URL('verification.json',OUT),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,allFaceRulePass:result.allFaceRulePass,rows:rows.map(({name,counts,bodyRule,faceRule,protonFaces,multiNeutronProtons})=>({name,counts,bodyPass:bodyRule.passes,facePass:faceRule.passes,unwitnessedN:faceRule.isolatedNeutrons,protonFaces,multiNeutronProtons}))},null,2));
