import test from 'node:test';
import assert from 'node:assert/strict';
import {createSulfurReflection} from '../examples/normal-ray/sulfur-reflection-renderer.js';
import certificate from '../research/strominger/results/regular-simplex-reflection-v1/verification.json' with {type:'json'};
import {sulfur32ReflectionProcess} from '../research/realization-tower/sulfur-32-reflection-process.mjs';
const cellOf=new Map(certificate.geometryGroups.flatMap(g=>g.copies.map(c=>[c,g.cell])));
test('one continuous non-branching coloured strand per retained history, at both ends',()=>{
 for(let stage=0;stage<=4;stage++){
  const model=sulfur32ReflectionProcess(7,stage),bundle=model.reflectionBundle;
  assert.equal(bundle.strands.length,2**stage);
  assert.deepEqual(bundle.input,bundle.output);
  assert.equal(new Set(bundle.input).size,bundle.strands.length);
  for(const strand of bundle.strands){
   assert.equal(strand.branches.length,0);
   assert.equal(strand.ancestry.at(-1),strand.copyId);
   assert.deepEqual(strand.points[0],strand.incoming);
   assert.deepEqual(strand.points.at(-1),strand.outgoing);
   assert(strand.points.every(p=>p.length===3&&p.every(Number.isFinite)));
   assert(strand.points.slice(1).every((p,i)=>p.some((x,j)=>Math.abs(x-strand.points[i][j])>1e-12)));
   const nativeCells=certificate.stages[stage].copies.map(c=>new Set(c.vertices4.map(p=>JSON.stringify(p))));
   for(let i=1;i<strand.nativeGuide4.length;i++){
    const a=JSON.stringify(strand.nativeGuide4[i-1]),b=JSON.stringify(strand.nativeGuide4[i]);
    assert(nativeCells.some(vs=>vs.has(a)&&vs.has(b)),'Each internal guide segment must be an actual simplex edge');
   }
   for(const id of new Set(strand.ancestry)){
    const vertices=certificate.stages[stage].copies.find(c=>c.id===id).vertices4;
    assert(vertices.every(v=>strand.nativeGuide4.some(p=>JSON.stringify(p)===JSON.stringify(v))),'Visit all five transported vertices');
   }
   for(const run of strand.contactRuns){
    const present=new Set(certificate.stages[run.stage].copies.map(c=>cellOf.get(c.id)));
    assert(present.has(run.from)&&present.has(run.to));
    assert(certificate.contacts.some(c=>c.cells.includes(run.from)&&c.cells.includes(run.to)));
   }
  }
 }
});
test('final wiring retains all sixteen identities, covers all fourteen seams, and uses all four colour styles',()=>{
 const bundle=sulfur32ReflectionProcess(7,4).reflectionBundle;
 for(const label of ['white','blue-white','red-white','blue'])assert.equal(bundle.strands.filter(s=>s.label===label).length,4);
 const seams=new Set(bundle.strands.flatMap(s=>s.contactRuns.map(r=>[r.from,r.to].sort((a,b)=>a-b).join(','))));
 assert.equal(seams.size,14);
 assert.equal(new Set(bundle.strands.map(s=>JSON.stringify(s.incoming))).size,16);
 assert.equal(new Set(bundle.strands.map(s=>JSON.stringify(s.outgoing))).size,16);
 assert.equal(new Set(bundle.strands.map(s=>JSON.stringify(s.decisions))).size,16);
});
test('wiring renderer produces sixteen complete tubes and eight equal-pitch striped materials, not graph links',()=>{
 const model=sulfur32ReflectionProcess(7,4),group=createSulfurReflection(model,{reflectionView:'wiring',bodies:false,reflectionWireOpacity:0});
 try{
  assert.equal(group.children.length,16);
  assert(group.children.every(m=>m.geometry.type==='TubeGeometry'&&m.material.opacity===0));
  const striped=group.children.filter(m=>m.material.userData.spiral);
  assert.equal(striped.length,8);
  assert(striped.every(m=>Math.abs(m.material.userData.spiral.pitch-striped[0].material.userData.spiral.pitch)<1e-12));
  for(const mesh of group.children){
   const strand=model.reflectionBundle.strands.find(s=>s.id===mesh.userData.incomingStrand),curve=mesh.geometry.parameters.path;
   assert.deepEqual(curve.getPoint(0).toArray(),strand.incoming);
   assert(curve.getPoint(1).toArray().every((x,i)=>Math.abs(x-strand.outgoing[i])<1e-10));
  }
 }finally{group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});}
});
test('projection changes neither strand identities nor seam routes, including edge-on projections',()=>{
 const baseline=sulfur32ReflectionProcess(7,4).reflectionBundle;
 for(const angle of [-90,-25,0,90]){
  const bundle=sulfur32ReflectionProcess(7,4,{reflectionAngle:angle}).reflectionBundle;
  assert.deepEqual(bundle.input,baseline.input);
  assert.deepEqual(bundle.strands.map(s=>s.contactRuns),baseline.strands.map(s=>s.contactRuns));
  assert(bundle.strands.every(s=>s.points.every(p=>p.every(Number.isFinite))));
 }
});
