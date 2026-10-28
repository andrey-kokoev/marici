import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {assembleComponents} from '../demos/particle-overlap-tetrahedron/simplex-components.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const contract='research/strominger/contracts/screw-esd7-geometric-attachment-attempt.v1.json';
const snapshot='research/strominger/contracts/persistent-seam-pe-conjecture-net.snapshot.rev32.json';
const source='research/strominger/results/native-screw-patch/verification.json';
const output='research/strominger/results/screw-esd7-geometric-attachment';
const load=async p=>JSON.parse(await fs.readFile(path.join(root,p),'utf8'));
const spec=await load(contract),pre=await load(snapshot),s=await load(source);
const checks=[];function check(name,f){f();checks.push(name);}
const point=v=>typeof v==='string'?v.split(',').map(Number):v;
const key=vs=>vs.map(v=>point(v).join(',')).sort().join('|');
const unique=vs=>[...new Map(vs.map(v=>[point(v).join(','),point(v)])).values()];
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const perms=permutations([0,1,2,3]);
function bound(vertices,sign){const maxima=[0,1,2,3].map(i=>Math.max(...vertices.map(v=>sign*v[i])));return {sign,maxima,minimumResolution:maxima.reduce((a,b)=>a+b,0)-sign};}
function compositions(n,k=4){if(k===1)return [[n]];return Array.from({length:n+1},(_,i)=>compositions(n-i,k-1).map(rest=>[i,...rest])).flat();}
const target=assembleComponents(7),targetPrimitives=target.components.map(c=>c.addresses),targetKeys=new Set(targetPrimitives.map(key));
const occupied=s.cells.map(c=>c.vertices.map(point)),occupiedVertices=unique(occupied.flat());
const references=unique(s.charts.flatMap(c=>Object.values(c.aliases)));
const allVertices=unique([...occupiedVertices,...references]);
function placements(primitives,vertices){
 const candidates=[],accepted=[];let eliminatedByEnvelope=0;
 for(const sign of [1,-1])for(const permutation of perms){
  const b=bound(vertices,sign),slack=7-b.minimumResolution;
  if(slack<0){eliminatedByEnvelope++;continue;}
  for(const excess of compositions(slack)){
   const translation=permutation.map((i,j)=>2-b.maxima[i]-excess[j]);
   assert.equal(translation.reduce((a,b)=>a+b,0),1-sign);
   const map=v=>permutation.map((i,j)=>sign*v[i]+translation[j]);
   assert.ok(vertices.every(v=>map(v).every(x=>x<=2)));
   const missing=primitives.map(p=>key(p.map(map))).filter(k=>!targetKeys.has(k));
   const row={sign,permutation,translation,missingPrimitiveCount:missing.length};candidates.push(row);if(!missing.length)accepted.push(row);
  }
 }
 return {eliminatedByEnvelope,candidates,accepted};
}
check('literal geometric interpretation registered before execution',()=>{
 const n=pre.conjectures.find(n=>n.id==='screw-esd7-geometric-attachment-attempt');assert.equal(n.status,'open');assert.equal(n.registration_before_execution,true);assert.ok(n.evidence.includes(contract));
});
check('actual occupied and reference coordinates stay on the declared integral affine plane',()=>{
 assert.equal(s.cells.length,24);assert.equal(s.packets.length,66);for(const v of allVertices){assert.equal(v.length,4);assert.ok(v.every(Number.isInteger));assert.equal(v.reduce((a,b)=>a+b,0),1);}
});
check('target is the generated343-primitive esd7 carrier, not a cell-count substitute',()=>{
 assert.equal(targetKeys.size,343);for(const v of targetPrimitives.flat()){assert.equal(v.reduce((a,b)=>a+b,0),1);assert.ok(v.every(x=>x<=2));}
});
const occupiedBounds=[1,-1].map(sign=>bound(occupiedVertices,sign));
const fullBounds=[1,-1].map(sign=>bound(allVertices,sign));
check('coordinate permutations preserve the envelope obstruction',()=>{
 for(const p of perms)for(const sign of [1,-1])assert.equal(bound(occupiedVertices.map(v=>p.map(i=>v[i])),sign).minimumResolution,bound(occupiedVertices,sign).minimumResolution);
});
const result=placements(occupied,allVertices);
const occupiedOnly=placements(occupied,occupiedVertices);
const externalContext=occupiedOnly.accepted.map(c=>{
 const map=v=>c.permutation.map((i,j)=>c.sign*v[i]+c.translation[j]);
 return {...c,outsideReferenceVertices:references.filter(v=>map(v).some(x=>x>2)).map(v=>({source:v,target:map(v)}))};
});
check('full registered signed-permutation family is accounted for',()=>{
 assert.equal(perms.length,24);assert.equal(result.eliminatedByEnvelope,fullBounds.filter(b=>b.minimumResolution>7).length*24);
});
const identityControl=placements(targetPrimitives,unique(targetPrimitives.flat()));
check('positive control accepts the actual target in its identity frame',()=>{
 assert.ok(identityControl.accepted.some(c=>c.sign===1&&c.permutation.join(',')==='0,1,2,3'&&c.translation.every(x=>x===0)));
});
check('every returned placement preserves all primitives, not only selected corners',()=>{
 for(const c of result.accepted){const map=v=>c.permutation.map((i,j)=>c.sign*v[i]+c.translation[j]);assert.equal(occupied.filter(p=>targetKeys.has(key(p.map(map)))).length,occupied.length);}
});
const charts=new Map(s.charts.map(c=>[Number(c.id.slice(6)),c])),packets=new Map(s.packets.map(p=>[p.id,p])),operations=new Map(s.operations.map(o=>[o.id,o])),cells=new Map(s.cells.map(c=>[c.id,c]));
const ids=new Set([charts.get(packets.get(0).chart).cell]),prefixes=[];
function addPrefix(operation){const vs=unique([...ids].flatMap(id=>cells.get(id).vertices));prefixes.push({operation,bodies:ids.size,bounds:[1,-1].map(sign=>bound(vs,sign).minimumResolution)});}
addPrefix(null);
for(const i of s.construction){ids.add(charts.get(packets.get(operations.get(i).target).chart).cell);addPrefix(i);}
const firstOccupiedObstruction=prefixes.find(p=>p.bounds.every(k=>k>7))??null;
check('prefix witness uses actual construction order and preserves monotone occupancy',()=>{
 assert.equal(ids.size,s.cells.length);for(let i=1;i<prefixes.length;i++){assert.ok(prefixes[i].bodies>=prefixes[i-1].bodies);for(let j=0;j<2;j++)assert.ok(prefixes[i].bounds[j]>=prefixes[i-1].bounds[j]);}
});
check('occupied-only diagnostic does not silently discard external reference context',()=>{
 for(const c of externalContext)assert.ok(c.outsideReferenceVertices.length>0 || result.accepted.some(p=>JSON.stringify(p)===JSON.stringify({sign:c.sign,permutation:c.permutation,translation:c.translation,missingPrimitiveCount:0})));
});
// Diagnostic minimization, not selection of a physical frame or a new attachment rule.
const selected=externalContext.length?externalContext.reduce((a,b)=>b.outsideReferenceVertices.length<a.outsideReferenceVertices.length?b:a):null;
const minimalExternalWitness=selected?{
 selection:'First enumerated occupied placement among those with the fewest distinct external references; diagnostic only.',
 sign:selected.sign,permutation:selected.permutation,translation:selected.translation,
 references:selected.outsideReferenceVertices.map(v=>{
  const aliases=s.charts.flatMap(c=>Object.entries(c.aliases).filter(([,x])=>point(x).join(',')===v.source.join(',')).map(([alias])=>({chart:c.id,species:c.species,alias,packets:s.packets.filter(p=>p.chart===Number(c.id.slice(6))).map(p=>p.id)})));
  const affected=new Set(aliases.flatMap(a=>a.packets));
  return {...v,violatedBounds:v.target.flatMap((x,i)=>x>2?[{coordinate:i,value:x,maximum:2}]:[]),aliases,
   incidentInterfaces:s.operations.filter(o=>affected.has(o.source)||affected.has(o.target)).map(o=>({id:o.id,kind:o.kind,source:o.source,target:o.target,faceContainsExternalReference:(o.face??[]).some(x=>point(x).join(',')===v.source.join(','))}))};
 })
}:null;
check('minimal external witness reconstructs every referenced source alias and names its retained packets',()=>{
 if(!minimalExternalWitness)return;
 const w=minimalExternalWitness;
 for(const v of w.references){
  const restored=[];w.permutation.forEach((i,j)=>{restored[i]=w.sign*(v.target[j]-w.translation[j]) || 0;});assert.deepEqual(restored,v.source);
  assert.ok(v.violatedBounds.length>0);assert.ok(v.aliases.length>0);
  for(const a of v.aliases){assert.ok(a.packets.length>0);for(const p of a.packets)assert.equal(charts.get(packets.get(p).chart).id,a.chart);}
 }
});
check('external-context failure is not misreported as an occupied shared-face failure',()=>{
 for(const v of minimalExternalWitness?.references??[]){
  assert.ok(!occupiedVertices.some(x=>x.join(',')===v.source.join(',')));
  assert.ok(v.incidentInterfaces.every(o=>!o.faceContainsExternalReference));
 }
});
const artifact={registration:contract,preExecutionSnapshot:snapshot,interpretation:spec.interpretation,minimalExternalWitness,
 occupiedOnlyDiagnostic:{candidateCount:occupiedOnly.candidates.length,acceptedPlacements:occupiedOnly.accepted,externalContext},
 occupiedBounds,occupiedAndReferenceBounds:fullBounds,placements:result,
 constructionPrefixes:prefixes,firstOccupiedObstruction,
 geometricAttachmentEstablished:result.accepted.length>0,
 actualAnalyticalFaceBindingEstablished:false,coherencePresentationInterpretationRefuted:false,fullPbConstructionEstablished:false,
 derivation:'For sign s, transformed coordinates sum to s before translation. Set m_i=max(s*x_i). A k-simplex in these coordinate directions requires sum(m_i)-s<=k. For k7, t_i<=2-m_perm(i) and sum(t)=1-s; slack=7-[sum(m_i)-s]. Enumerate all nonnegative slack compositions if slack>=0. Permuting axes cannot change this bound.',
 scope:spec.scope};
await fs.mkdir(path.join(root,output),{recursive:true});await fs.writeFile(path.join(root,output,'attempt.json'),JSON.stringify(artifact,null,2)+'\n');
for(const [p,d] of Object.entries(s.sourceHashes))assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d,'stale input '+p);
const inputs=[contract,snapshot,source,...Object.keys(s.sourceHashes),spec.targetGenerator,'research/strominger/checkers/check_screw_esd7_geometric_attachment.mjs','research/strominger/screw-esd7-geometric-attachment-result-v1.md',output+'/attempt.json'];
const sourceHashes={};for(const p of inputs)sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const report={status:'passed',check_count:checks.length,checks,occupiedMinimumResolutions:occupiedBounds.map(b=>b.minimumResolution),
 fullMinimumResolutions:fullBounds.map(b=>b.minimumResolution),excludedOrientations:result.eliminatedByEnvelope,acceptedPlacements:result.accepted.length,
 occupiedOnlyPlacements:occupiedOnly.accepted.length,minimumOutsideReferences:externalContext.length?Math.min(...externalContext.map(c=>c.outsideReferenceVertices.length)):null,
 geometricAttachmentEstablished:artifact.geometricAttachmentEstablished,actualAnalyticalFaceBindingEstablished:false,coherencePresentationInterpretationRefuted:false,fullPbConstructionEstablished:false,
 firstOccupiedObstruction,minimalExternalWitness,sourceHashes};
await fs.writeFile(path.join(root,output,'verification.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({...report,checks:undefined,sourceHashes:undefined}));
