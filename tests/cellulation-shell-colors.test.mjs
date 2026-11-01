import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=(face,size=1)=>face.map(p=>p.map(x=>Math.round(x*Math.SQRT2/size)).join(',')).sort().join('|');
test('shell colors follow retained red/blue seed face planes, while octahedral boundary fillers stay white',()=>{
 for(const size of [.5,1,2])for(let step=23;step<=26;step++){
  const m=buildCellulationStep(step,size),fill=m.shellFace,prior=new Set(m.previous.faces.map(f=>key(f.vertices,size))),faces=new Map(m.faces.map(f=>[key(f.vertices,size),f]));
  const colors={red:0,blue:0,white:0};
  for(const r of fill.boundaryReadings){
   const k=key(r.vertices,size);assert(!prior.has(k));assert.equal(faces.get(k).owners.length,1);assert.equal(faces.get(k).owners[0],r.owner);
   if(r.kind==='octahedron'){assert.equal(r.colour,0xffffff);assert.equal(r.source,'white-octahedral-filler');colors.white++;}
   else{
    const seed=fill.seedFaces.find(s=>s.id===r.source);assert(seed);assert.equal(r.colour,seed.colour);
    const a=r.vertices[1].map((x,i)=>x-r.vertices[0][i]),b=r.vertices[2].map((x,i)=>x-r.vertices[0][i]),n=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],length=Math.hypot(...n);
    assert(Math.abs(n.reduce((sum,x,i)=>sum+x*seed.normal[i],0)/length)>1-1e-8);
    colors[r.colour===0xff3030?'red':'blue']++;
   }
  }
  assert.deepEqual(colors,step<25?{red:15,blue:0,white:20}:{red:0,blue:15,white:10});
 }
});
test('renderer uses the recorded per-face colors without repainting existing bars or double-painting shared interfaces',()=>{
 const m=buildCellulationStep(26),g=createCellulation(m);g.userData.animate(Infinity,{});
 let model=m,group=g;
 while(model.shellFace){
  const expected=new Map(model.shellFace.boundaryReadings.map(r=>[key(r.vertices),r.colour])),seen=new Set(),prior=new Set(model.previous.faces.map(f=>key(f.vertices)));
  for(const mesh of group.children.filter(o=>o.userData.cellulationFaces)){
   for(const k of mesh.userData.shellFaceKeys){assert(!seen.has(k));assert(!prior.has(k));seen.add(k);assert.equal(mesh.material.color.getHex(),expected.get(k)??0xffffff);}
  }
  for(const k of expected.keys())assert(seen.has(k));model=model.previous;group=group.children[0];
 }
 const before=[];group.traverse(o=>{if(o.material?.color)before.push(o.material.color.getHex());});
 g.userData.animate(0,{});const after=[];group.traverse(o=>{if(o.material?.color)after.push(o.material.color.getHex());});assert.deepEqual(after,before);
});
