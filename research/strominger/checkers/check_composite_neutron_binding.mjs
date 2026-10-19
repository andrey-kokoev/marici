// Native-reader embedding into whole octahedra; no whole-body admission law.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {makeLatticeItem,acrossFace,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {createWindowConstruction} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {auditPhaseCombination} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
import {phaseFrame,applyPhasePermutation} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {transportCarrierCoefficients} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
const files=['./check_composite_neutron_binding.mjs','../composite-neutron-binding-protocol-v1.md',...['lattice-items.mjs','simplex-components.mjs','window-construction-model.mjs','carrier.mjs','phase-discipline-model.mjs','phase-advance-model.mjs','deuterium-tunnel-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
function* perms(a){if(!a.length)yield [];for(const x of a)for(const p of perms(a.filter(y=>y!==x)))yield [x,...p];}
const point=p=>JSON.stringify(p),keys=['C0','M0','C1','M1'],rows=[],examples=[],countercontrols=[];
for(const seed of [makeLatticeItem('tetrahedron',[0,0,0,0]),makeLatticeItem('tetrahedron',[2,0,0,0],true)]){
 const histogram={externalRegularEndpoint:0,internalAbsorbedEndpoint:0},rootTypeControls=[];
 for(const permutation of perms([0,1,2,3])){
  const initial=Object.fromEntries(keys.map((k,i)=>[k,seed.vertices[permutation[i]]])),model=createWindowConstruction({seed,bindings:initial});model.step();const s=model.step();assert.equal(s.status,'complete');
  const incoming=s.events[0].face,outgoing=s.events[1].face,whole=acrossFace(seed,incoming),n=s.items[1],e=s.items[2];assert.equal(whole.kind,'octahedron');
  assert.ok(whole.components.some(c=>itemKey(c)===n.key));assert.ok(whole.faces.some(f=>itemKey(f)===itemKey(incoming)));
  const external=whole.faces.some(f=>itemKey(f)===itemKey(outgoing)),absorbed=whole.components.some(c=>itemKey(c)===e.key);assert.notEqual(external,absorbed);
  if(permutation[1]%2===1&&permutation[3]%2===1)rootTypeControls.push({permutation,external});
  if(!external){histogram.internalAbsorbedEndpoint++;continue;}histogram.externalRegularEndpoint++;
  const endpointOwner=acrossFace(whole,outgoing);assert.equal(endpointOwner.kind,'tetrahedron');assert.equal(endpointOwner.key,e.key);
  assert.equal(incoming.filter(p=>outgoing.some(q=>point(q)===point(p))).length,2);
  const extras=whole.vertices.filter(p=>!n.vertices.some(q=>point(p)===point(q)));assert.equal(extras.length,2);assert.ok(extras.every(p=>!Object.values(s.bindings).some(q=>point(p)===point(q))));
  const allAliases=Object.fromEntries(Object.entries(s.bindings).map(([k,p])=>[k,point(p)])),charts=['proton','neutron','electron'].map((species,i)=>({id:String(i),species,aliases:allAliases})),maps=[];
  for(let i=0;i<2;i++){
   const from=phaseFrame(charts[i]),to=phaseFrame(charts[i+1]),kind=i?'NE':'PN';
   assert.equal(auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind,identification:'same-occurrence',vertices:to.window.map(o=>o.vertex)}]).status,'native-phase-compatible');
   const map=transportCarrierCoefficients([0,1,2,3,4].map(i=>[i,0]),s.events[i]).map(z=>z[0]),v=[[1,2],[3,4],[5,6],[7,8],[9,10]];assert.deepEqual(applyPhasePermutation(applyPhasePermutation(v,map),map,-1),v);maps.push(map);
  }
  assert.deepEqual(maps,[[3,1,2,0,4],[0,4,2,3,1]]);
  const axis=[0,1,2,3].find(i=>incoming.every(p=>p[i]===incoming[0][i]));assert.notEqual(axis,undefined);
  const direction=Math.sign(whole.center[axis]-seed.center[axis]),strictlyOutward=direction*(e.center[axis]-whole.center[axis])>0;assert.equal(strictlyOutward,false);
  const baseComponents=[seed.components[0],...whole.components,e.vertices].map(itemKey);assert.equal(new Set(baseComponents).size,6);
  if(examples.filter(x=>x.inverted===seed.inverted).length<1)examples.push({inverted:seed.inverted,seed:{origin:seed.origin,inverted:seed.inverted},permutation,packet:s,wholeNeutron:{origin:whole.origin,vertices:whole.vertices,components:whole.components},nativeNeutronSkeleton:n.vertices,additionalGeometricVertices:extras,maps,centroidTest:{axis,direction,P:seed.center[axis],wholeN:whole.center[axis],E:e.center[axis],strictlyOutward},wholeBodyAdmitted:false});
  // Existing native all-three-mode branch/phase transfer remains replayable.
  for(const branch of ['common','positive','negative'])for(let phaseExponent=0;phaseExponent<3;phaseExponent++){
   const replay=createWindowConstruction({seed,bindings:initial,branch,phaseExponent});replay.step();const x=replay.step();assert.equal(x.status,'complete');assert.equal(x.events[1].targetCycle,'inverse');assert.equal(x.mode.phaseExponent,phaseExponent);assert.equal(x.mode.branch,branch==='common'?'common':branch==='positive'?'negative':'positive');
  }
 }
 assert.deepEqual(histogram,{externalRegularEndpoint:8,internalAbsorbedEndpoint:16});assert.equal(rootTypeControls.length,4);assert.ok(rootTypeControls.every(x=>!x.external));
 rows.push({seed:{origin:seed.origin,inverted:seed.inverted},markings:24,histogram,rootTypeControls});
}
// A formal action on the retained five coordinates has no unique extension
// to hypothetical extra data. This demonstrates nonuniqueness, NOT that the
// extra geometric vertices must carry new independent native coefficients.
const retained=[[1,2],[3,4],[5,6],[7,8],[9,10]],auxiliary=[[11,12],[13,14]],a=[...retained,...auxiliary],b=[...retained,...auxiliary.map(z=>z.map(x=>-x))];assert.deepEqual(a.slice(0,5),b.slice(0,5));assert.notDeepEqual(a,b);assert.equal(a.flat().reduce((s,x)=>s+x*x,0),b.flat().reduce((s,x)=>s+x*x,0));countercontrols.push({kind:'mathematical-extension-underdetermination',nativeNewCoefficientsAssumed:false,newBodyLaw:false});
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);
const result={status:'partial-native-skeleton-bindings-found-whole-body-law-open',sourceHashes,rows,examples,countercontrols,scope:'All 24 ordered markings for one seed of each regular-tetrahedron orientation, within the local honeycomb. Translation equivalent seeds not re-enumerated. 8/24 allow native PN/NE windows on whole-octahedron boundary; existing fixed root C/M role pattern permits none. No whole-body particle-count/field/reader/contact law derived; not an N14 search or admission. Production/viewer unchanged.'};
await mkdir('research/strominger/results/composite-neutron-binding',{recursive:true});await writeFile('research/strominger/results/composite-neutron-binding/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,rows,examples:examples.map(x=>({inverted:x.inverted,permutation:x.permutation,additionalVertices:x.additionalGeometricVertices.length,centroidTest:x.centroidTest})),wholeBodyAdmitted:false},null,2));
