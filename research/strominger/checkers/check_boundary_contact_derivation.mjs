// Derive interface data, not new admission or physical interaction laws.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {createWindowConstruction} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame,phaseAdvanceWitness,applyPhasePermutation,spectralReadout} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame,auditPhaseCombination} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
import {transportCarrierCoefficients} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
const files=['./check_boundary_contact_derivation.mjs',...['phase-assembly-model.mjs','window-construction-model.mjs','carrier.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs','lithium6-assembly-model.mjs','simplex-model.mjs','simplex-components.mjs','lattice-items.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)];
for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
const url=new URL('../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs',import.meta.url),source=await readFile(url,'utf8'),cut=source.indexOf(' const exitPaths=new Map();'),end=source.indexOf('\nconst cache=new Map();',cut);
assert.ok(cut>0&&end>cut);
let adapter=source.slice(0,cut)+" return {status:'nuclear-local-compatible',admitted:false,charts,edges,packets,root,paths:Object.fromEntries(paths)};\n}\n"+source.slice(end);
adapter=adapter.replace(/from '(\.[^']+)'/g,(_,p)=>`from '${new URL(p,url).href}'`);
const localCompiler=await import('data:text/javascript;base64,'+Buffer.from(adapter).toString('base64'));
const pointIds=new Map(lattice.nodes.map((n,i)=>[JSON.stringify(n.address),'vertex-'+i]));
const prior=JSON.parse(await readFile(new URL('../results/carbon13-proton-capture/verification.json',import.meta.url),'utf8'));
const n14=compilePhaseAssembly(prior.witness.reference.candidate,prior.witness.orientation);
function contactAudit(r){
 const key=(a,b)=>[a,b].sort((x,y)=>x-y).join(',');
 const witnessed=new Set(r.edges.filter(e=>['PN','NE','NN-phase-advance'].includes(e.kind)).map(e=>(e.kind==='NN-phase-advance'?'NN':e.kind)+':'+key(r.charts[e.from].cell,r.charts[e.to].cell)));
 const missing=r.candidate.interfaces.filter(e=>!witnessed.has(e.kind+':'+key(e.from,e.to)));
 return {allDeclaredContactsWitnessed:missing.length===0,missing};
}
const contactRecords=[];
for(const name of ['helium3','helium4','lithium6','lithium7','beryllium9','boron10','boron11','carbon12','carbon13','nitrogen15']){
 const r=selectPhaseAssembly(name);auditPhaseAssembly(r);contactRecords.push({name,legacyGatePassed:true,...contactAudit(r)});
}
for(const a of prior.charged.accepted){
 const c=prior.charged.candidates.find(c=>c.addedProton===a.addedProton).candidate,r=compilePhaseAssembly(c,a.orientation);auditPhaseAssembly(r);
 contactRecords.push({name:'nitrogen14-plus-proton-'+a.addedProton,legacyGatePassed:true,...contactAudit(r)});
}
assert.equal(contactRecords.find(r=>r.name==='carbon12').allDeclaredContactsWitnessed,true);
assert.ok(contactRecords.every(r=>r.allDeclaredContactsWitnessed),'Reselected references must cover every contact');
const boundaryRecords=[];
for(const [name,full] of [['carbon12',selectPhaseAssembly('carbon12')],['nitrogen14-plus',n14],['nitrogen15',selectPhaseAssembly('nitrogen15')]]){
 auditPhaseAssembly(full);
 const vertices=new Set(full.candidate.nucleus.flatMap(i=>lattice.cells[i]));
 const bare={nucleus:full.candidate.nucleus,electrons:[],types:Object.fromEntries(Object.entries(full.candidate.types).filter(([v])=>vertices.has(Number(v)))),interfaces:full.candidate.interfaces.filter(e=>e.kind!=='NE')};
 const r=localCompiler.compilePhaseAssembly(bare,full.orientations);assert.equal(r.status,'nuclear-local-compatible');
 const ports=[];
 for(const packet of r.packets){
  if(bare.nucleus.includes(packet.e))continue;
  const p=r.charts[packet.pChart],n=r.charts[packet.nChart],component=lattice.assembly.components[p.cell];
  const bindings=Object.fromEntries(['C0','M0','C1','M1'].map(k=>[k,lattice.nodes[Number(p.aliases[k].slice(7))].address]));
  const model=createWindowConstruction({seed:makeLatticeItem('tetrahedron',component.origin,component.transform.kind==='inversion'),bindings});model.step();const native=model.step();assert.equal(native.status,'complete');
  const aliases=Object.fromEntries(Object.entries(native.bindings).map(([k,v])=>[k,pointIds.get(JSON.stringify(v))??'external:'+JSON.stringify(v)]));
  const target={id:'port-'+ports.length,species:'electron',aliases};
  // Recover the actual origin at the N reader along its rooted entry path.
  let origin=0,value=[[1,2],[3,4],[5,6],[7,8],[9,10]];
  for(const index of r.paths[packet.nChart]){const edge=r.edges[index];if(edge.phaseDelta)phaseAdvanceWitness(r.charts[edge.from],r.charts[edge.to],origin);origin+=edge.phaseDelta;value=applyPhasePermutation(value,edge.permutation);}
  const from=phaseFrame(n,origin),to=phaseFrame(target,origin);
  const audit=auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind:'NE',identification:'same-occurrence',vertices:to.window.map(o=>o.vertex)}]);assert.equal(audit.status,'native-phase-compatible');
  const map=transportCarrierCoefficients([0,1,2,3,4].map(i=>[i,0]),native.events[1]).map(z=>z[0]);assert.deepEqual(map,[0,4,2,3,1]);
  const output=applyPhasePermutation(value,map);assert.deepEqual(applyPhasePermutation(output,map,-1),value);
  ports.push({sourceChart:packet.nChart,sourceCell:n.cell,orderedFace:to.window,origin,fullFiveSlotMap:map,terminalWindowReadout:spectralReadout('electron',output).components,contextProvenance:native.bindings.M2,hypotheticalTargetKey:native.items[2].key,occupied:false,extensionAdmitted:false});
 }
 const reverse=r.charts.map(()=>[]);r.edges.forEach(e=>reverse[e.to].push(e.from));const reached=new Set(ports.map(p=>p.sourceChart)),queue=[...reached];for(let i=0;i<queue.length;i++)for(const from of reverse[queue[i]])if(!reached.has(from)){reached.add(from);queue.push(from);}
 assert.equal(reached.size,r.charts.length);
 boundaryRecords.push({name,nuclearCells:bare.nucleus.length,nuclearCharts:r.charts.length,nativeOpenPorts:ports.length,allChartsHaveRouteToOpenTrace:true,ports,admitted:false,scope:'Native outgoing trace data only. No occupied E cells, E-count assignment, boundary condition, binding or stability law.'});
}
// Exhaust all local MMCC E-frame assignments on both possible shared-face
// role patterns. This tests same-occurrence sewing, not native EE transport.
function frames(id,vertices,types){
 const m=vertices.filter(v=>types[v]==='M'),c=vertices.filter(v=>types[v]==='C'),result=[];
 for(const ms of [m,[...m].reverse()])for(const cs of [c,[...c].reverse()]){const chart={id:id+result.length,species:'electron',aliases:{M1:ms[0],M2:ms[1],C1:cs[0],C2:cs[1]}};assert.equal(auditPhaseFrame(phaseFrame(chart)).status,'native-template-compatible');result.push(chart);}return result;
}
const contacts=[];
for(const faceRoles of [['M','C','C'],['M','M','C']]){
 const shared=['a','b','c'],left=[...shared,'left'],right=[...shared,'right'],apex=faceRoles.filter(r=>r==='M').length===1?'M':'C',types=Object.fromEntries([...shared.map((v,i)=>[v,faceRoles[i]]),['left',apex],['right',apex]]);
 let matches=0,activeFaceCollisions=0,missingContextCoefficient=0;const witnesses=[];
 for(const a of frames('l',left,types))for(const b of frames('r',right,types)){
  const fa=phaseFrame(a),fb=phaseFrame(b),all=f=>[...f.window,f.context],deltas=shared.map(v=>all(fa).find(o=>o.vertex===v).index-all(fb).find(o=>o.vertex===v).index);
  if(new Set(deltas).size!==1)continue;matches++;assert.equal(deltas[0],0);
  const active=shared.every(v=>fa.window.some(o=>o.vertex===v))&&shared.every(v=>fb.window.some(o=>o.vertex===v));
  if(active)activeFaceCollisions++;else {assert.ok(shared.includes(fa.context.vertex)&&shared.includes(fb.context.vertex));missingContextCoefficient++;}
  assert.throws(()=>phaseAdvanceWitness(a,b),/matching P or N/);
  const unsupported=auditPhaseCombination([fa,fb],[{from:fa.id,to:fb.id,kind:'EE',identification:'same-occurrence',vertices:shared}]);assert.ok(unsupported.issues.some(i=>i.kind==='missing-phase-transition-witness'));
  witnesses.push({left:fa,right:fb,requiredOffset:0,activeWindowOnBothSides:active,nativeEEAdmitted:false});
 }
 assert.equal(matches,4);assert.equal(matches,activeFaceCollisions+missingContextCoefficient);contacts.push({faceRoles,framePairs:16,sameOccurrenceMatches:matches,activeFaceCollisions,missingContextCoefficient,witnesses});
}
// In the actual manifold, an incoming E-window's opposite cell is its N
// predecessor. Two E windows facing each other would each require the other's
// occupied E cell to serve as N. This is not the case for all touching faces.
const ee=JSON.parse(await readFile(new URL('../results/n14-assumptions/ee.json',import.meta.url),'utf8')).witness.candidate.interfaces.find(e=>e.kind==='EE');
const {adjacency}=assemblyDomain();for(const [a,b] of [[ee.from,ee.to],[ee.to,ee.from]])assert.deepEqual(adjacency[a].filter(e=>e.face.every(v=>ee.face.includes(v))).map(e=>e.to),[b]);
// Even a fully specified active face does not determine a five-slot law.
// These are mathematical completions, NOT newly authorized native operators.
const x=[[1,2],[3,4],[5,6],[7,8],[9,10]],identity=structuredClone(x),flip=x.map((z,i)=>z.map(a=>i===0?-a:a));
assert.deepEqual(spectralReadout('electron',identity).components,spectralReadout('electron',flip).components);assert.notDeepEqual(identity,flip);
const norm=v=>v.flat().reduce((s,a)=>s+a*a,0);assert.equal(norm(identity),norm(flip));
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);
const receipt={status:'interface-data-derived-admission-laws-still-open',sourceHashes,boundaryRecords,contactRecords,contacts,fullFaceTransportUnderdetermined:{identityAndContextSignFlipHaveSameActiveReadout:true,normPreserved:true,bothNativeAuthorized:false},scope:'No new isotope search or production/viewer changes. Native open traces are derived data, not a nuclear boundary law. EE contact classification assumes literal same-occurrence face identification; other passage laws remain unspecified. Missing M2 coefficient and unsupported EE transitions are not physical nonexistence proofs.'};
await mkdir('research/strominger/results/boundary-contact-derivation',{recursive:true});await writeFile('research/strominger/results/boundary-contact-derivation/verification.json',JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,nuclearBoundary:boundaryRecords.map(({name,nuclearCells,nativeOpenPorts,allChartsHaveRouteToOpenTrace})=>({name,nuclearCells,nativeOpenPorts,allChartsHaveRouteToOpenTrace})),EE:contacts.map(({witnesses,...s})=>s),contactCoverage:contactRecords,newAdmissionLaw:false},null,2));
