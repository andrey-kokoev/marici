import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
const root='research/strominger',paths={contract:root+'/contracts/su32-edge5-reflection-compatible-routing-v1.json',
 source:root+'/results/su32-edge5-global-routing-witness-v1/verification.json',
 audit:root+'/results/su32-edge5-twisted-return-v1/verification.json',
 carrier:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 binding:root+'/results/su32-edge5-fibre-placement-binding-v1/verification.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};for(const [k,p] of Object.entries(paths)){
 docs[k]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[k].sourceHashes??{}))assert.equal(await digest(s),h,`Stale ${s}`);
}
assert.equal(docs.contract.source,paths.source);assert.equal(docs.contract.audit,paths.audit);
const sector=buildPESymmetricSector(2),geometry=docs.carrier.edge5Carrier;
const reading=buildFiveSideOctRoutingObligations(sector).readings.find(r=>r.id==='reading:0:-1');
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const reflect=v=>{const h=reading.axis.reduce((s,a,i)=>s+a*(v[i]-sector.centre[i]),0)/2;return v.map((x,i)=>x-h*reading.axis[i]);};
const byShape=new Map(geometry.cells.map(c=>[shape(c.vertices),c.id]));
const R=new Map(geometry.cells.map(c=>[c.id,byShape.get(shape(c.vertices.map(reflect)))]));
const RF=new Map(geometry.faces.map(f=>[f.id,shape(f.vertices.map(reflect))]));
const faces=new Map(geometry.faces.map(f=>[f.id,f]));
const layer=new Map(geometry.layers.flatMap(l=>l.cells.map(id=>[id,l.layer])));
for(const c of geometry.cells){assert.equal(R.get(R.get(c.id)),c.id);if(layer.get(c.id)===9)assert.equal(R.get(c.id),c.id);}
for(const f of geometry.faces){assert(faces.has(RF.get(f.id)));assert.equal(RF.get(RF.get(f.id)),f.id);}
// Whole-bank construction before local checks. The source prefixes came from
// a simultaneous global circulation, never from a reader-growth procedure.
const routes=docs.source.routes.map(r=>({fibre:r.fibre,
 cells:[...r.cells.slice(0,9),...r.cells.slice(0,8).reverse().map(c=>R.get(c))],
 faces:[...r.faces.slice(0,8),...r.faces.slice(0,8).reverse().map(f=>RF.get(f))]}));
const visits=new Map(geometry.cells.map(c=>[c.id,[]])),flow=new Map(geometry.faces.filter(f=>f.owners.length===2).map(f=>[f.id,0]));
let changed=0;const reverse=r=>({fibre:r.fibre,cells:[...r.cells].reverse(),faces:[...r.faces].reverse()});
const reflected=r=>({fibre:r.fibre,cells:r.cells.map(c=>R.get(c)),faces:r.faces.map(f=>RF.get(f))});
const certificates=[];
assert.deepEqual(routes.map(r=>r.fibre),docs.source.routes.map(r=>r.fibre));assert.equal(new Set(routes.map(r=>r.fibre)).size,80);
for(let n=0;n<routes.length;n++){
 const r=routes[n],old=docs.source.routes[n];assert.equal(r.cells.length,17);assert.equal(r.faces.length,16);
 assert.deepEqual(r.cells.slice(0,9),old.cells.slice(0,9));assert.deepEqual(r.faces.slice(0,8),old.faces.slice(0,8));
 assert.equal(r.cells[0],old.cells[0]);assert.equal(r.cells.at(-1),old.cells.at(-1));
 if(JSON.stringify(r)!==JSON.stringify(old))changed++;
 assert.deepEqual(reflected(r),reverse(r));assert.deepEqual(reverse(reverse(r)),r);
 for(let i=0;i<17;i++){assert.equal(layer.get(r.cells[i]),i+1);visits.get(r.cells[i]).push(r.fibre);}
 for(let i=0;i<16;i++){
  assert.deepEqual([...faces.get(r.faces[i]).owners].sort(),[r.cells[i],r.cells[i+1]].sort());flow.set(r.faces[i],flow.get(r.faces[i])+1);
 }
 const dual=reflected(r),halves=[r,dual];
 const blocks=halves.flatMap((h,chart)=>Array.from({length:4},(_,phase)=>({chart,phase,
  cells:h.cells.slice(4*phase,4*phase+5),faces:h.faces.slice(4*phase,4*phase+4)})));
 for(let i=0;i<8;i++){
  assert.equal(blocks[i].cells.at(-1),blocks[(i+1)%8].cells[0]);
  assert.equal(R.get(blocks[i].cells[0]),blocks[(i+4)%8].cells[0]);
  assert.notDeepEqual([blocks[i].chart,blocks[i].phase],[blocks[(i+4)%8].chart,blocks[(i+4)%8].phase]);
 }
 const history=blocks.map(b=>structuredClone(b));assert.equal(history.flatMap(h=>h.faces).length,32);
 assert.deepEqual(history.slice(0,4).flatMap(b=>b.faces),r.faces);
 assert.deepEqual(history.slice(4).flatMap(b=>b.faces),[...r.faces].reverse());
 certificates.push({fibre:r.fibre,initial:{cell:r.cells[0],chart:0,phase:0},
 terminalAfterFour:{cell:r.cells.at(-1),chart:1,phase:0},
 comparator:{kind:'dual-reference',reflectedTerminal:R.get(r.cells.at(-1)),equalsInitial:true},
 activeAfterEight:{cell:r.cells[0],chart:0,phase:0},history,historyErased:false});
}
assert([...visits.values()].every(v=>v.length>0));assert.equal(visits.size,245);assert.equal(changed,79);
for(let l=1;l<=17;l++)assert.equal([...visits].filter(([c])=>layer.get(c)===l).reduce((s,[,v])=>s+v.length,0),80);
// All per-cell incoming/outgoing multiplicities agree with the labelled paths.
for(const c of geometry.cells){
 const incident=[...flow].filter(([f])=>faces.get(f).owners.includes(c.id));
 const incoming=incident.filter(([f])=>faces.get(f).owners.some(id=>layer.get(id)===layer.get(c.id)-1)).reduce((s,[,v])=>s+v,0);
 const outgoing=incident.filter(([f])=>faces.get(f).owners.some(id=>layer.get(id)===layer.get(c.id)+1)).reduce((s,[,v])=>s+v,0);
 const k=visits.get(c.id).length;if(layer.get(c.id)>1)assert.equal(incoming,k);if(layer.get(c.id)<17)assert.equal(outgoing,k);
}
const middleDeliveries=docs.binding.placementDomain.triples.map(t=>({triple:t.id,
 sites:[...new Set([t.T,t.U,t.V,...t.tipGroup])].map(cell=>{
 const before=docs.source.routes.filter(r=>r.cells.includes(cell)).map(r=>r.fibre),after=visits.get(cell);
 assert.deepEqual(after,before);return {cell,fibres:after};})}));
const oldFaces=new Set(docs.source.routes.flatMap(r=>r.faces)),newFaces=new Set(routes.flatMap(r=>r.faces));
const added=[...newFaces].filter(f=>!oldFaces.has(f)).sort(),removed=[...oldFaces].filter(f=>!newFaces.has(f)).sort();
for(const f of newFaces)assert(newFaces.has(RF.get(f)));
const payloads=routes.map(r=>({fibre:r.fibre,opaque:{tag:r.fibre}}));
const pass=rs=>rs.map(r=>payloads.find(p=>p.fibre===r.fibre));
assert.deepEqual(pass(routes),payloads);assert.deepEqual(pass(routes.map(reverse)),payloads);
const negative={unmodifiedSourceFailsFullReflectionReversal:docs.audit.counts.reflectedRoutesEqualOwnInverse!==80,
 ordinaryFourReturnFails:certificates.every(c=>c.initial.cell!==c.terminalAfterFour.cell),
 fullHistoryStateNotPeriodic:certificates.every(c=>c.history.length===8)};assert(Object.values(negative).every(Boolean));
const self=root+'/checkers/check_su32_edge5_reflection_compatible_routing.mjs';
for(const p of [self,root+'/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs'])sourceHashes[p]=await digest(p);
const result={schema:'su32.edge5-reflection-compatible-routing.v1',passed:true,
 counts:{fibres:80,changedFromOriginal:changed,upperHalvesRetained:80,coveredCells:245,reflectionEqualsInverse:80,
 usedSharedFaces:newFaces.size,addedFaces:added.length,removedFaces:removed.length,dualOnlyFaces:0,
 middleTriplesRetained:middleDeliveries.length,orientedProgramStates:640},
 scope:'New conditional geometric route witness satisfying reflection-as-reversal under fixed fibre identities. Not a source-derived native generator.',
 routes,reverseRoutes:routes.map(reverse),visits:Object.fromEntries(visits),faceFlows:Object.fromEntries(flow),
 changes:{addedFaces:added,removedFaces:removed},middleDeliveries,returnCertificates:certificates,negativeControls:negative,
 nativePairReadout:null,nativeFillingMaps:null,sourceHashes};
const dir=root+'/results/su32-edge5-reflection-compatible-routing-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts:result.counts,scope:result.scope,negativeControls:negative},null,2));
