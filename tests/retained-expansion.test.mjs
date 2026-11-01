import {test} from 'node:test';
import assert from 'node:assert/strict';
import * as T from 'three';
import {readFileSync} from 'node:fs';
import {createRetainedExpansion,retainedExpansionAtoms} from '../examples/normal-ray/retained-expansion-renderer.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('card abundance and stability match the isotope reference table',()=>{
 const table=readFileSync(new URL('../research/kitaev/isotope-electron-shells.html',import.meta.url),'utf8');
 assert.equal(Object.keys(retainedExpansionAtoms).length,17);
 for(const atom of Object.values(retainedExpansionAtoms)){
  assert(table.includes(`'${atom.name}': '${atom.abundancePercent}'`));
  assert(Number(atom.abundancePercent)>0&&Number(atom.abundancePercent)<=100);
  assert.equal(atom.stability,'Stable');
 }
});
test('step 3 opens two white triangles; step 4 colors both without a shared white line',()=>{
 for(let step=1;step<=4;step++){
  const g=createRetainedExpansion(step),[dot,arrow,plane,tip]=g.children;
  assert.equal(dot.visible,step<3);assert.equal(arrow.visible,step===2);assert.equal(plane.visible,step>=3);assert.equal(tip.visible,false);
  assert.equal(g.userData.audit.triangles,step>=3?2:0);assert.equal(g.userData.audit.arrowDirections,0);assert.equal(g.userData.audit.growingLines,step===2?1:0);
  if(step>=3){
   const lower=g.children[16];assert.equal(lower.visible,true);assert.equal(lower.scale.y,1);
   assert.deepEqual(Array.from(lower.children[0].geometry.attributes.position.array),[0,0,0,1.5,-1.5,0,3,0,0]);
   assert.equal(lower.children[0].material.color.getHex(),step===3?0xffffff:0x3080ff);
   assert.equal(lower.children[1].material.color.getHex(),step===3?0xffffff:0xff3030);
   assert.equal(g.userData.audit.horizontalSeparator,false);
  }
  assert.equal(arrow.children.length,1);assert.equal(arrow.children[0].geometry.parameters.radiusTop,.018);
  const [front,back,border]=plane.children;assert.equal(front.geometry,back.geometry);assert.equal(front.material.side,T.FrontSide);assert.equal(back.material.side,T.BackSide);
  assert.deepEqual(Array.from(front.geometry.attributes.position.array),[0,0,0,3,0,0,1.5,1.5,0]);
  assert.equal(front.material.color.getHex(),step===4?0xff3030:0xffffff);assert.equal(back.material.color.getHex(),step===4?0x3080ff:0xffffff);
  for(const e of border.children)assert.equal(e.geometry.parameters.radiusTop,.018);
 }
});
test('growth, reverse seeking, dot disappearance and edges-only retain their gates',()=>{
 const g=createRetainedExpansion(3),[dot,arrow,plane,tip]=g.children;
 for(const [time,p] of [[0,0],[450,.5],[Infinity,1],[0,0]]){
  g.userData.animate(time);assert.equal(dot.visible,false);assert.equal(arrow.scale.x,1);assert.equal(plane.scale.y,p);
  assert.equal(g.children[16].scale.y,p);assert.equal(g.children[16].children[3].visible,p<1);
  assert.deepEqual(g.userData.audit.tipPositions,[[1.5,1.5*p,0],[1.5,-1.5*p,0]]);assert.equal(tip.visible,p<1);assert.equal(tip.position.y,1.5*p);
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(plane.children[0].visible,false);assert.equal(plane.children[1].visible,false);assert.equal(tip.visible,false);
 const colored=createRetainedExpansion(4);colored.userData.animate(0);assert.equal(colored.children[2].children[0].material.color.getHex(),0xffffff);
 colored.userData.animate(Infinity);assert.equal(colored.children[2].children[0].material.color.getHex(),0xff3030);
});
test('step 5 reveals only the white X-axis diagonal on the already colored square',()=>{
 const g=createRetainedExpansion(5),upper=g.children[2],lower=g.children[16],line=g.children[1].children[0];
 const previous=createRetainedExpansion(4);
 for(const time of [0,450,900,Infinity,0]){
  g.userData.animate(time);
  assert.equal(lower.scale.y,1);assert.equal(g.children[1].scale.x,Math.min(1,time/900));
  assert.equal(g.children[1].visible,time>0);assert.equal(g.children[3].visible,false);
  for(const index of [2,16])for(let i=0;i<2;i++){
   const a=g.children[index].children[i],b=previous.children[index].children[i];
   assert.deepEqual(Array.from(a.geometry.attributes.position.array),Array.from(b.geometry.attributes.position.array));assert.equal(a.material.color.getHex(),b.material.color.getHex());
  }
  assert.equal(upper.scale.y,1);assert.equal(g.children[4].visible,false);assert.equal(g.children[5].visible,false);
  assert.equal(upper.children[0].visible,true);
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 assert.equal(g.userData.audit.square,true);assert.equal(g.userData.audit.droppedArrows,0);
 assert.deepEqual(g.userData.audit.sharedEdge,[[0,0,0],[3,0,0]]);
 const corners=[[0,0,0],[1.5,-1.5,0],[3,0,0],[1.5,1.5,0]].map(p=>new T.Vector3(...p));
 for(let i=0;i<4;i++){
  const a=corners[(i+1)%4].clone().sub(corners[i]),b=corners[(i+2)%4].clone().sub(corners[(i+1)%4]);
  assert.equal(a.lengthSq(),4.5);assert.equal(a.dot(b),0);
 }
 const endpoints=[-1.5,1.5].map(y=>new T.Vector3(0,y,0).applyMatrix4(line.matrixWorld));
 assert(endpoints[0].distanceTo(corners[0])<1e-6);assert(endpoints[1].distanceTo(corners[2])<1e-6);
 assert.equal(line.material.color.getHex(),0xffffff);
 for(const [y,frontColor,backColor] of [[.5,0xff3030,0x3080ff],[-.5,0x3080ff,0xff3030]])for(const [z,color] of [[2,frontColor],[-2,backColor]]){
  const ray=new T.Raycaster(new T.Vector3(1.5,y,z),new T.Vector3(0,0,-Math.sign(z)));
  const hits=ray.intersectObjects([...upper.children.slice(0,2),...lower.children.slice(0,2)]);
  assert.equal(hits.length,1);assert.equal(hits[0].object.material.color.getHex(),color);
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert(upper.children.slice(0,2).every(f=>!f.visible));assert(lower.children.slice(0,2).every(f=>!f.visible));assert.equal(lower.children[2].visible,true);
 g.userData.animate(0);assert.equal(lower.visible,true);assert.equal(g.children[1].visible,false);
 for(let step=9;step<=20;step++){const later=createRetainedExpansion(step);assert.equal(later.children.length,16);assert.equal(later.userData.audit.rectangle,false);}
});
test('step 6 splits both square halves vertically in color without shrinking or a new line',()=>{
 const previous=createRetainedExpansion(5),g=createRetainedExpansion(6),faces=g.children[17];
 assert.equal(faces.children.length,8);assert.equal(g.children[18].children.length,0);
 assert.deepEqual(g.userData.audit.splitFields,['upper','lower']);assert.equal(g.userData.audit.colouredTriangles,4);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(g.children[16].scale.y,1);assert.equal(g.userData.audit.whiteningProgress,0);
  for(const mesh of faces.children)assert.equal(mesh.material.opacity,1);
  for(const index of [4,5,6,8])assert.equal(g.children[index].visible,false,'Legacy divisions must not show');
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 for(const region of ['upper','lower'])for(const reading of ['front','back']){
  const pair=faces.children.filter(f=>f.userData.region===region&&f.userData.reading===reading);
  const original=previous.children[region==='upper'?2:16].children[0].geometry.attributes.position;
  const parent=new T.Triangle(...Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(original,i)));
  const points=pair.map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
  assert.equal(points.reduce((sum,p)=>sum+new T.Triangle(...p).getArea(),0),parent.getArea());
  assert(points.flat().every(p=>parent.containsPoint(p)));
  const shared=points[0].filter(p=>points[1].some(q=>q.equals(p)));assert.equal(shared.length,2);assert(shared.every(p=>p.x===1.5&&p.z===0));
  for(const [i,mesh] of pair.entries()){
   const red=(region==='upper')===(i===0),color=(reading==='front'?red:!red)?0xff3030:0x3080ff;
   assert.equal(mesh.material.color.getHex(),color);
   const center=points[i].reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3),z=reading==='front'?2:-2;
   const hits=new T.Raycaster(center.add(new T.Vector3(0,0,z)),new T.Vector3(0,0,-Math.sign(z))).intersectObjects(faces.children);
   assert.equal(hits.length,1);assert.equal(hits[0].object,mesh);
  }
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(faces.visible,false);
});
test('step 7 adds only the vertical white diagonal while preserving all four faces',()=>{
 const previous=createRetainedExpansion(6),g=createRetainedExpansion(7),faces=g.children[17],separator=g.children[18],line=separator.children[0];
 assert.equal(separator.children.length,1);assert.equal(line.material.color.getHex(),0xffffff);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(line.scale.y,Math.min(1,time/1200));assert.equal(line.visible,time>0);
  for(const [i,mesh] of faces.children.entries()){
   const old=previous.children[17].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,1);
  }
  assert.equal(g.children[1].visible,true);assert.equal(g.userData.audit.whiteningProgress,0);
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 const ends=[-1.5,1.5].map(y=>new T.Vector3(0,y,0).applyMatrix4(line.matrixWorld));
 assert(ends[0].distanceTo(new T.Vector3(1.5,-1.5,0))<1e-6);assert(ends[1].distanceTo(new T.Vector3(1.5,1.5,0))<1e-6);
 for(const y of [-.75,.75])for(const z of [-2,2])assert(new T.Raycaster(new T.Vector3(1.5,y,z),new T.Vector3(0,0,-Math.sign(z))).intersectObject(line).length>0);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(faces.visible,false);assert.equal(separator.visible,false);
});
test('white planes stay fully opaque throughout growth, whitening and reverse seek',()=>{
 for(const step of [3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]){
  const g=createRetainedExpansion(step);
  for(const time of [0,300,600,Infinity,0]){
   g.userData.animate(time,{faceOpacity:1});
   const faces=step>=6?g.children[5].children:g.children[2].children.slice(0,2);
   for(const face of faces)assert.equal(face.material.opacity,1);
  }
 }
});
test('steps 2 and 5 introduce plain lines with no arrowheads retained in later steps',()=>{
 for(let step=1;step<=20;step++){
  const g=createRetainedExpansion(step);
  g.traverse(mesh=>assert.notEqual(mesh.geometry?.type,'ConeGeometry'));
  assert.equal(g.children[1].children.length,1);
  assert(g.children[4].children.every(drop=>drop.children.length===1));
  for(const time of [0,450,Infinity]){g.userData.animate(time);assert.equal(g.userData.audit.arrowDirections,0);}
 }
});
test('step 10 carries the correction into a full-size left-center split',()=>{
 const previous=createRetainedExpansion(9),g=createRetainedExpansion(10),insets=g.children[6],split=g.children[7];
 assert.equal(g.userData.audit.viewportLabel,'Beryllium-9\nneutrons: 5\nprotons: 4\nelectrons: 4\n- shell 1: 2/2\n- shell 2: 2/8');
 assert.equal(g.userData.audit.colouredTriangles,5);
 assert.equal(insets.children.filter(f=>f.userData.splitParent).length,2);
 assert.deepEqual(g.userData.audit.splitColoredFace,{face:'left',slot:1});
 assert(insets.children.filter(f=>f.userData.splitParent).every(f=>f.userData.face==='left'&&f.userData.slot===1));
 assert.deepEqual(split.children.map(f=>f.material.color.getHex()),[0x3080ff,0xff3030,0xff3030,0x3080ff]);
 for(const time of [0,300,600,900,Infinity,0]){
  g.userData.animate(time);
  assert(g.children[5].children.slice(0,2).every(f=>f.material.color.getHex()===0xffffff&&f.material.opacity===1));
  assert.deepEqual(g.children[5].children.slice(2).map(f=>f.material.color.getHex()),[0x3080ff,0xff3030]);
  for(const [i,mesh] of insets.children.entries()){
   assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(previous.children[6].children[i].geometry.attributes.position.array));
   if(!mesh.userData.splitParent){assert.equal(mesh.visible,true);assert.equal(mesh.material.opacity,1);assert.equal(mesh.material.color.getHex(),previous.children[6].children[i].material.color.getHex());}
   else assert.equal(mesh.visible,false);
  }
  assert.equal(split.visible,true);
  assert(split.children.every(f=>f.material.opacity===1));
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 for(const reading of ['front','back']){
  const parent=insets.children.find(f=>f.userData.splitParent&&f.userData.reading===reading),p=parent.geometry.attributes.position;
  const triangle=new T.Triangle(...Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(p,i)));
  const children=split.children.filter(f=>f.userData.reading===reading);assert.equal(children.length,2);
  const vertices=children.map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
  assert.equal(vertices[0].filter(v=>vertices[1].some(w=>v.equals(w))).length,2,'Color regions retain a common geometric edge underneath the separator');
  assert.equal(vertices.reduce((sum,points)=>sum+new T.Triangle(...points).getArea(),0),triangle.getArea(),'Step 10 must preserve the full original area');
  assert([triangle.a,triangle.b,triangle.c].every(v=>vertices.flat().some(w=>v.equals(w))),'Step 10 must preserve original boundary vertices');
  for(const child of children){assert.equal(child.material.side,parent.material.side);const v=child.geometry.attributes.position;
   for(let i=0;i<3;i++){const point=new T.Vector3().fromBufferAttribute(v,i);assert.equal(point.z,0);assert(triangle.containsPoint(point));}
   const center=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(v,i)).reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3);
   const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert.equal(ray.intersectObjects(split.children).length,1);
  }
 }
 const lines=g.children[8];assert.equal(lines.children.length,3);
 for(const z of [-2,2]){const ray=new T.Raycaster(new T.Vector3(1.125,.75,z),new T.Vector3(0,0,-Math.sign(z)));assert(ray.intersectObject(lines.children[2]).length>0,'Step 10 separator follows the left-center split');}
 for(const time of [0,600,Infinity]){
  g.userData.animate(time);assert.equal(lines.children[2].scale.y,Math.min(1,time/1200));
  assert(lines.children.slice(0,2).every(line=>line.visible&&line.scale.y===1));
  for(let i=0;i<2;i++){const a=previous.children[9].children[i],b=g.children[9].children[i];assert.deepEqual(Array.from(a.geometry.attributes.position.array),Array.from(b.geometry.attributes.position.array));assert.equal(a.material.color.getHex(),b.material.color.getHex());assert.equal(b.material.opacity,1);}
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(split.visible,false);assert.equal(insets.visible,false);
});
test('step 9 preserves step 8 full-size triangles and adds only a white separator',()=>{
 const previous=createRetainedExpansion(8),g=createRetainedExpansion(9),separator=g.children[8];
 assert.equal(g.userData.audit.viewportLabel,'Lithium-7\nneutrons: 4\nprotons: 3\nelectrons: 3\n- shell 1: 2/2\n- shell 2: 1/8');
 assert.equal(separator.children.length,2);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(g.children[9].visible,true);
  for(let i=0;i<2;i++){
   const a=previous.children[9].children[i],b=g.children[9].children[i];
   assert.deepEqual(Array.from(b.geometry.attributes.position.array),Array.from(a.geometry.attributes.position.array),'Step 9 must not shrink or move the step 8 triangles');
   assert.equal(a.material.color.getHex(),b.material.color.getHex());assert.equal(b.material.opacity,1);
  }
  assert(g.children[6].children.every(f=>f.visible));
  assert.equal(separator.children[0].scale.y,1);assert.equal(separator.children[1].scale.y,Math.min(1,time/1200));
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 const p=g.children[9].children[0].geometry.attributes.position;
 const center=new T.Vector3().fromBufferAttribute(p,0).add(new T.Vector3().fromBufferAttribute(p,1)).multiplyScalar(.5);
 for(const z of [-2,2]){const ray=new T.Raycaster(center.clone().add(new T.Vector3(0,0,z)),new T.Vector3(0,0,-Math.sign(z)));assert(ray.intersectObject(separator.children[1]).length>0);}
 assert.equal(separator.children[1].material.color.getHex(),0xffffff);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(separator.visible,false);
});
test('step 8 splits only the positive-x positive-y square quadrant along local x=y',()=>{
 const previous=createRetainedExpansion(7),g=createRetainedExpansion(8),separator=g.children[18],recolored=g.children[9];
 assert.equal(g.userData.audit.viewportLabel,'Lithium-6\nneutrons: 3\nprotons: 3\nelectrons: 3\n- shell 1: 2/2\n- shell 2: 1/8');
 assert.deepEqual(g.userData.audit.splitColoredFace,{face:'upper',slot:1});
 assert.equal(g.userData.audit.square,true);assert.equal(g.userData.audit.colouredTriangles,5);
 assert(g.userData.audit.diagonalSplit.every(([x,y,z])=>x-1.5===y&&z===0));assert.equal(separator.children.length,2);
 assert.equal(g.userData.audit.newPairSeparator,true);assert.equal(g.children[7].children.length,0);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(g.userData.audit.whiteningProgress,0);
  assert.equal(separator.children[0].scale.y,1);assert.equal(separator.visible,true);
  assert.equal(separator.children[1].scale.y,Math.min(1,time/1200));assert.equal(separator.children[1].visible,time>0);
  for(const index of [17])for(const [i,mesh] of g.children[index].children.entries()){
   const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.visible,old.visible);assert.equal(mesh.material.opacity,old.material.opacity);
  }
 }
 const right=previous.children[17].children.find(f=>f.userData.region==='upper'&&f.userData.part===1&&f.userData.reading==='front').geometry.attributes.position;
 const area=p=>new T.Triangle(...Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(p,i))).getArea();
 assert.equal(area(right),1.125,'Parent is the upper-right quarter of the square');
 assert.equal(area(recolored.children[0].geometry.attributes.position),area(right)/2);
 const upper=new T.Triangle(new T.Vector3(1.5,0,0),new T.Vector3(2.25,.75,0),new T.Vector3(1.5,1.5,0));
 const lower=new T.Triangle(new T.Vector3(1.5,0,0),new T.Vector3(3,0,0),new T.Vector3(2.25,.75,0));
 assert.equal(upper.getArea()+lower.getArea(),area(right));
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 for(const [z,upperColor,lowerColor] of [[2,0xff3030,0x3080ff],[-2,0x3080ff,0xff3030]])for(const [x,y,color] of [[1.75,.75,upperColor],[2.25,.25,lowerColor]]){
  const ray=new T.Raycaster(new T.Vector3(x,y,z),new T.Vector3(0,0,-Math.sign(z)));
  const hits=ray.intersectObjects([...g.children[17].children,...recolored.children]).sort((a,b)=>b.object.renderOrder-a.object.renderOrder);
  assert(hits.length>0);assert.equal(hits[0].object.material.color.getHex(),color);
 }
 const line=separator.children[1];assert.equal(line.material.color.getHex(),0xffffff);
 const length=line.geometry.parameters.height,ends=[-length/2,length/2].map(y=>new T.Vector3(0,y,0).applyMatrix4(line.matrixWorld));
 assert(ends[0].distanceTo(new T.Vector3(1.5,0,0))<1e-6);assert(ends[1].distanceTo(new T.Vector3(2.25,.75,0))<1e-6);
 for(const z of [-2,2])assert(new T.Raycaster(new T.Vector3(1.875,.375,z),new T.Vector3(0,0,-Math.sign(z))).intersectObject(line).length>0);
 assert(recolored.children.every(f=>f.material.opacity===1));
 g.userData.animate(0);assert.equal(recolored.visible,false);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(separator.visible,false);assert.equal(recolored.visible,false);
});
test('step 11 splits the upper-right face into a touching red/blue pair for Boron-10',()=>{
 const previous=createRetainedExpansion(10),g=createRetainedExpansion(11),pair=g.children[10];
 assert.equal(g.userData.audit.viewportLabel,'Boron-10\nneutrons: 5\nprotons: 5\nelectrons: 5\n- shell 1: 2/2\n- shell 2: 3/8');
 assert.equal(g.userData.audit.colouredTriangles,6);assert.equal(g.children[8].children.length,3,'No additional white separator');
 for(const time of [0,300,600,900,Infinity,0]){
  g.userData.animate(time);assert.equal(pair.visible,true);assert.equal(g.userData.audit.whiteningProgress,0);
  assert(pair.children.every(f=>f.material.opacity===1));
  for(const index of [5,6,7])for(const [i,mesh] of g.children[index].children.entries()){
   const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.visible,old.visible);
  }
  assert(g.children[8].children.every(line=>line.visible&&line.scale.y===1));
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 assert.deepEqual(g.children[9].children.map(face=>face.material.color.getHex()),[0xff3030,0x3080ff]);
 assert.deepEqual(pair.children.map(face=>face.material.color.getHex()),[0xff3030,0x3080ff,0x3080ff,0xff3030]);
 for(const reading of ['front','back']){
  const children=pair.children.filter(f=>f.userData.reading===reading);
  const vertices=children.map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
  assert.equal(vertices[0].filter(v=>vertices[1].some(w=>v.equals(w))).length,2,'New pair must touch without white between');
  const positions=previous.children[9].children.find(f=>f.userData.reading===reading).geometry.attributes.position;
  const parent=new T.Triangle(...Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i)));
  assert.equal(vertices.reduce((sum,points)=>sum+new T.Triangle(...points).getArea(),0),parent.getArea(),'Step 11 must preserve full face area');
  assert([parent.a,parent.b,parent.c].every(v=>vertices.flat().some(w=>v.equals(w))),'Step 11 must preserve original boundary vertices');
  for(const points of vertices){assert(points.every(p=>p.z===0&&parent.containsPoint(p)));const center=points.reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3);
   const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert.equal(ray.intersectObjects(pair.children).length,1);
  }
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(pair.visible,false);
});
test('step 12 retains Boron-10 geometry and adds a white separator for Boron-11',()=>{
 const previous=createRetainedExpansion(11),g=createRetainedExpansion(12),separator=g.children[8],line=separator.children[3];
 assert.equal(g.userData.audit.viewportLabel,'Boron-11\nneutrons: 6\nprotons: 5\nelectrons: 5\n- shell 1: 2/2\n- shell 2: 3/8');
 assert.equal(separator.children.length,4);assert.equal(line.material.color.getHex(),0xffffff);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(line.scale.y,Math.min(1,time/1200));assert.equal(line.visible,time>0);
  assert(separator.children.slice(0,3).every(f=>f.scale.y===1&&f.visible));
  for(const index of [5,6,7,9,10]){
   assert.equal(g.children[index].visible,previous.children[index].visible);
   for(const [i,mesh] of g.children[index].children.entries()){
    const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,old.material.opacity);assert.equal(mesh.visible,old.visible);
   }
  }
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 const p=g.children[10].children[0].geometry.attributes.position;
 const center=new T.Vector3().fromBufferAttribute(p,1).add(new T.Vector3().fromBufferAttribute(p,2)).multiplyScalar(.5);
 for(const z of [-2,2]){const ray=new T.Raycaster(center.clone().add(new T.Vector3(0,0,z)),new T.Vector3(0,0,-Math.sign(z)));assert(ray.intersectObject(line).length>0);}
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(separator.visible,false);
});
test('Carbon-12 subdivides a step 11 small face; Carbon-13 separates its children',()=>{
 const previous=createRetainedExpansion(12),carbon=createRetainedExpansion(13),isotope=createRetainedExpansion(14);
 for(const [g,mass,neutrons] of [[carbon,12,6],[isotope,13,7]]){
  assert.equal(g.userData.audit.viewportLabel,`Carbon-${mass}\nneutrons: ${neutrons}\nprotons: 6\nelectrons: 6\n- shell 1: 2/2\n- shell 2: 4/8`);
  assert.equal(g.userData.audit.colouredTriangles,7);assert.equal(g.children[8].children.length,mass===12?4:5);
  const pair=g.children[11];assert.equal(pair.children.length,4);
  for(const time of [0,600,Infinity,0]){
   g.userData.animate(time);assert.equal(pair.visible,true);assert(pair.children.every(f=>f.material.opacity===1));
   if(mass===12)assert.equal(g.userData.audit.whiteningProgress,0);
   assert(g.children[8].children.slice(0,4).every(f=>f.scale.y===1&&f.visible));
   assert.equal(g.children[10].children.filter(f=>f.userData.carbonParent).length,2);
   for(const index of [5,7,9,10])for(const [i,mesh] of g.children[index].children.entries()){
    const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,old.material.opacity);
   }
   if(mass===13)assert.equal(g.children[8].children[4].scale.y,Math.min(1,time/1200));
  }
  g.userData.animate(Infinity);g.updateMatrixWorld(true);
  assert.deepEqual(pair.children.map(f=>f.material.color.getHex()),[0x3080ff,0xff3030,0xff3030,0x3080ff]);
  for(const reading of ['front','back']){
   const parent=previous.children[10].children.find(f=>f.userData.part===1&&f.userData.reading===reading);
   const original=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(parent.geometry.attributes.position,i));
   const children=pair.children.filter(f=>f.userData.reading===reading);
   const triangles=children.map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
   const shared=triangles[0].filter(v=>triangles[1].some(w=>v.equals(w)));assert.equal(shared.length,2);
   assert.equal(triangles.reduce((sum,t)=>sum+new T.Triangle(...t).getArea(),0),new T.Triangle(...original).getArea());
   assert(original.every(v=>triangles.flat().some(w=>v.equals(w))));
   for(const [i,child] of children.entries()){
    const center=triangles[i].reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3);
    const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));
    assert.equal(ray.intersectObjects(pair.children).length,1);assert.equal(child.material.side,parent.material.side);
   }
   if(mass===13){const line=g.children[8].children[4],center=shared[0].clone().add(shared[1]).multiplyScalar(.5);assert.equal(line.material.color.getHex(),0xffffff);
    const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert(ray.intersectObject(line).length>0);
   }
  }
  g.userData.animate(Infinity,{edgesOnly:true});assert.equal(pair.visible,false);assert.equal(g.children[8].visible,false);
 }
 for(let i=0;i<4;i++)assert.deepEqual(Array.from(carbon.children[11].children[i].geometry.attributes.position.array),Array.from(isotope.children[11].children[i].geometry.attributes.position.array),'Neutron step must not resize or move the colored pair');
});
test('Nitrogen-14 splits the opposite larger upper-left face; Nitrogen-15 adds its line',()=>{
 const previous=createRetainedExpansion(14),fourteen=createRetainedExpansion(15),fifteen=createRetainedExpansion(16);
 const positions=previous.children[7].children[1].geometry.attributes.position;
 const original=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i)),parent=new T.Triangle(...original);
 assert.equal(parent.getArea(),.28125,'Target is the opposite larger upper-left face, not a Carbon child');
 for(const [g,mass,neutrons] of [[fourteen,14,7],[fifteen,15,8]]){
  assert.equal(g.userData.audit.viewportLabel,`Nitrogen-${mass}\nneutrons: ${neutrons}\nprotons: 7\nelectrons: 7\n- shell 1: 2/2\n- shell 2: 5/8`);
  const pair=g.children[12],separators=g.children[8];assert.equal(pair.children.length,4);assert.equal(separators.children.length,mass===14?5:6);
  for(const time of [0,600,Infinity,0]){
   g.userData.animate(time);assert.equal(pair.visible,true);assert(pair.children.every(f=>f.material.opacity===1));
   if(mass===14)assert.equal(g.userData.audit.whiteningProgress,0);
   assert(separators.children.slice(0,5).every(f=>f.visible&&f.scale.y===1));
   if(mass===15)assert.equal(separators.children[5].scale.y,Math.min(1,time/1200));
   for(const index of [5,6,7,9,10,11])for(const [i,mesh] of g.children[index].children.entries()){
    const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,old.material.opacity);assert.equal(mesh.visible,old.visible);
   }
  }
  g.userData.animate(Infinity);g.updateMatrixWorld(true);
  assert.deepEqual(pair.children.map(f=>f.material.color.getHex()),[0x3080ff,0xff3030,0xff3030,0x3080ff]);
  for(const reading of ['front','back']){
   const triangles=pair.children.filter(f=>f.userData.reading===reading).map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
   const shared=triangles[0].filter(v=>triangles[1].some(w=>v.equals(w)));assert.equal(shared.length,2);
   assert.equal(triangles.reduce((sum,t)=>sum+new T.Triangle(...t).getArea(),0),parent.getArea());
   assert(original.every(v=>triangles.flat().some(w=>v.equals(w))));assert(triangles.flat().every(v=>parent.containsPoint(v)&&v.z===0));
   for(const triangle of triangles){const center=triangle.reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3);
    const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert.equal(ray.intersectObjects(pair.children).length,1);
   }
   if(mass===15){const line=separators.children[5],center=shared[0].clone().add(shared[1]).multiplyScalar(.5);assert.equal(line.material.color.getHex(),0xffffff);
    const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert(ray.intersectObject(line).length>0);
   }
  }
  g.userData.animate(Infinity,{edgesOnly:true});assert.equal(pair.visible,false);assert.equal(separators.visible,false);
 }
 for(let i=0;i<4;i++)assert.deepEqual(Array.from(fourteen.children[12].children[i].geometry.attributes.position.array),Array.from(fifteen.children[12].children[i].geometry.attributes.position.array),'Neutron step must preserve full-size geometry');
});
test('Oxygen-16 adds a full-size color split; Oxygen-17 only separates the new pair',()=>{
 const previous=createRetainedExpansion(16),sixteen=createRetainedExpansion(17),seventeen=createRetainedExpansion(18);
 for(const [g,mass,neutrons] of [[sixteen,16,8],[seventeen,17,9]]){
  assert.equal(g.userData.audit.viewportLabel,`Oxygen-${mass}\nneutrons: ${neutrons}\nprotons: 8\nelectrons: 8\n- shell 1: 2/2\n- shell 2: 6/8`);
  const pair=g.children[13],separators=g.children[8];assert.equal(pair.children.length,4);assert.equal(separators.children.length,mass===16?6:7);
  for(const time of [0,600,Infinity,0]){
   g.userData.animate(time);assert.equal(pair.visible,true);assert(pair.children.every(f=>f.material.opacity===1));
   if(mass===16)assert.equal(g.userData.audit.whiteningProgress,0);
   assert(separators.children.slice(0,6).every(f=>f.visible&&f.scale.y===1));
   if(mass===17)assert.equal(separators.children[6].scale.y,Math.min(1,time/1200));
   for(const index of [5,6,7,9,10,11,12])for(const [i,mesh] of g.children[index].children.entries()){
    const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,old.material.opacity);assert.equal(mesh.visible,old.visible);
   }
  }
  g.userData.animate(Infinity);g.updateMatrixWorld(true);
  assert.deepEqual(pair.children.map(f=>f.material.color.getHex()),[0x3080ff,0xff3030,0xff3030,0x3080ff]);
  for(const reading of ['front','back']){
   const old=previous.children[12].children.find(f=>f.userData.part===0&&f.userData.reading===reading),positions=old.geometry.attributes.position;
   assert(Array.from({length:3},(_,i)=>positions.getY(i)).includes(1.5),'The split parent must include the top apex');
   const original=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i)),parent=new T.Triangle(...original);
   const triangles=pair.children.filter(f=>f.userData.reading===reading).map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
   const shared=triangles[0].filter(v=>triangles[1].some(w=>v.equals(w)));assert.equal(shared.length,2);
   assert.equal(triangles.reduce((sum,t)=>sum+new T.Triangle(...t).getArea(),0),parent.getArea());
   assert(original.every(v=>triangles.flat().some(w=>v.equals(w))));assert(triangles.flat().every(v=>parent.containsPoint(v)&&v.z===0));
   for(const triangle of triangles){const center=triangle.reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3);
    const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert.equal(ray.intersectObjects(pair.children).length,1);
   }
   if(mass===17){const line=separators.children[6],center=shared[0].clone().add(shared[1]).multiplyScalar(.5);assert.equal(line.material.color.getHex(),0xffffff);
    const ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));assert(ray.intersectObject(line).length>0);
   }
  }
  g.userData.animate(Infinity,{edgesOnly:true});assert.equal(pair.visible,false);assert.equal(separators.visible,false);
 }
 for(let i=0;i<4;i++)assert.deepEqual(Array.from(sixteen.children[13].children[i].geometry.attributes.position.array),Array.from(seventeen.children[13].children[i].geometry.attributes.position.array),'Neutron step must not shrink or move the new pair');
});
test('Fluorine-19 adds a full-size PE split and white neutron separator',()=>{
 const previous=createRetainedExpansion(18),g=createRetainedExpansion(19),pair=g.children[14];
 assert.equal(g.userData.audit.viewportLabel,'Fluorine-19\nneutrons: 10\nprotons: 9\nelectrons: 9\n- shell 1: 2/2\n- shell 2: 7/8');
 assert.equal(g.userData.audit.unplacedAdditionalNeutrons,0);assert.equal(g.children[8].children.length,8);
 assert.equal(g.userData.audit.fluorinePairSeparator,true);
 assert.equal(pair.children.length,4);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(pair.visible,true);assert.equal(g.userData.audit.whiteningProgress,0);assert(pair.children.every(f=>f.material.opacity===1));
  assert(g.children[8].children.slice(0,7).every(f=>f.visible&&f.scale.y===1));
  const line=g.children[8].children[7];assert.equal(line.scale.y,Math.min(1,time/1200));assert.equal(line.visible,time>0);
  for(const index of [5,6,7,9,10,11,12,13])for(const [i,mesh] of g.children[index].children.entries()){
   const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,old.material.opacity);assert.equal(mesh.visible,old.visible);
  }
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 assert.deepEqual(pair.children.map(f=>f.material.color.getHex()),[0xff3030,0x3080ff,0x3080ff,0xff3030]);
 for(const reading of ['front','back']){
  const line=g.children[8].children[7],positions=pair.children[0].geometry.attributes.position;
  const shared=[1,2].map(i=>new T.Vector3().fromBufferAttribute(positions,i));
  assert.equal(line.material.color.getHex(),0xffffff);
  const length=line.geometry.parameters.height,endpoints=[-length/2,length/2].map(y=>new T.Vector3(0,y,0).applyMatrix4(line.matrixWorld));
  assert(shared.every(p=>endpoints.some(q=>p.distanceTo(q)<1e-6)),'White line follows the exact shared edge');
  const center=shared[0].clone().add(shared[1]).multiplyScalar(.5),z=reading==='front'?2:-2;
  assert(new T.Raycaster(center.add(new T.Vector3(0,0,z)),new T.Vector3(0,0,-Math.sign(z))).intersectObject(line).length>0);
  const parent=previous.children[11].children.find(f=>f.userData.part===1&&f.userData.reading===reading),p=parent.geometry.attributes.position;
  assert(Array.from({length:3},(_,i)=>p.getY(i)).includes(1.5),'Fluorine must split the topmost right triangle containing the apex');
  const original=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(p,i)),triangle=new T.Triangle(...original);
  const children=pair.children.filter(f=>f.userData.reading===reading),triangles=children.map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
  assert.equal(triangles[0].filter(v=>triangles[1].some(w=>v.equals(w))).length,2,'New triangles touch without white');
  assert.equal(triangles.reduce((sum,t)=>sum+new T.Triangle(...t).getArea(),0),triangle.getArea());
  assert(original.every(v=>triangles.flat().some(w=>v.equals(w))));assert(triangles.flat().every(v=>v.z===0&&triangle.containsPoint(v)));
  for(const [i,points] of triangles.entries()){
   const center=points.reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3),ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));
   assert.equal(ray.intersectObjects(pair.children).length,1);assert.equal(children[i].material.side,parent.material.side);
  }
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(pair.visible,false);
});
test('Neon-20 adds a full-size left-center PE split without another neutron line',()=>{
 const previous=createRetainedExpansion(19),g=createRetainedExpansion(20),pair=g.children[15];
 assert.equal(g.userData.audit.viewportLabel,'Neon-20\nneutrons: 10\nprotons: 10\nelectrons: 10\n- shell 1: 2/2\n- shell 2: 8/8');
 assert.equal(g.userData.audit.unplacedAdditionalNeutrons,0);assert.equal(g.children[8].children.length,8);assert.equal(pair.children.length,4);
 assert.equal(g.userData.audit.fluorinePairSeparator,true);
 for(const time of [0,600,Infinity,0]){
  g.userData.animate(time);assert.equal(pair.visible,true);assert.equal(g.userData.audit.whiteningProgress,0);assert(pair.children.every(f=>f.material.opacity===1));
  assert(g.children[8].children.every(f=>f.visible&&f.scale.y===1));
  for(const index of [5,6,7,9,10,11,12,13,14])for(const [i,mesh] of g.children[index].children.entries()){
   const old=previous.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.material.color.getHex(),old.material.color.getHex());assert.equal(mesh.material.opacity,old.material.opacity);assert.equal(mesh.visible,old.visible);
  }
 }
 g.userData.animate(Infinity);g.updateMatrixWorld(true);
 assert.deepEqual(pair.children.map(f=>f.material.color.getHex()),[0x3080ff,0xff3030,0xff3030,0x3080ff]);
 for(const reading of ['front','back']){
  const parent=previous.children[7].children.find(f=>f.userData.part===0&&f.userData.reading===reading),p=parent.geometry.attributes.position;
  const original=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(p,i)),triangle=new T.Triangle(...original);
  const children=pair.children.filter(f=>f.userData.reading===reading),triangles=children.map(f=>Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(f.geometry.attributes.position,i)));
  assert.equal(triangles[0].filter(v=>triangles[1].some(w=>v.equals(w))).length,2,'New triangles touch without white');
  assert.equal(triangles.reduce((sum,t)=>sum+new T.Triangle(...t).getArea(),0),triangle.getArea());
  assert(original.every(v=>triangles.flat().some(w=>v.equals(w))));assert(triangles.flat().every(v=>v.z===0&&triangle.containsPoint(v)));
  for(const [i,points] of triangles.entries()){
   const center=points.reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3),ray=new T.Raycaster(center.add(new T.Vector3(0,0,reading==='front'?2:-2)),new T.Vector3(0,0,reading==='front'?-1:1));
   assert.equal(ray.intersectObjects(pair.children).length,1);assert.equal(children[i].material.side,parent.material.side);
  }
 }
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(pair.visible,false);
});
test('steps 13 and 15 split opposite upper faces of equal size and retain outer faces',()=>{
 const g=createRetainedExpansion(16),area=mesh=>{const p=mesh.geometry.attributes.position;return new T.Triangle(...Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(p,i))).getArea();};
 assert.equal(area(g.children[10].children[1]),.28125);
 for(const child of g.children[11].children){const p=child.geometry.attributes.position;for(let i=0;i<3;i++){assert(p.getX(i)>=1.5);assert(p.getY(i)>=.75,'Carbon split must lie in the upper-right triangle');}}
 assert.equal(area(g.children[11].children[0]),.140625);
 assert.equal(area(g.children[12].children[0]),.140625);
 for(const child of g.children[12].children){const p=child.geometry.attributes.position;for(let i=0;i<3;i++){assert(p.getX(i)<=1.5,'Nitrogen split must be on the opposite left side');assert(p.getY(i)>=.75);}}
 const before=createRetainedExpansion(12);
 for(let step=13;step<=20;step++){
  const current=createRetainedExpansion(step);
  for(const index of [5,6])for(const [i,mesh] of current.children[index].children.entries()){
   const old=before.children[index].children[i];assert.deepEqual(Array.from(mesh.geometry.attributes.position.array),Array.from(old.geometry.attributes.position.array));assert.equal(mesh.visible,old.visible);assert.equal(mesh.material.color.getHex(),old.material.color.getHex());
  }
 }
 g.updateMatrixWorld(true);
 const meshes=[];g.traverse(o=>{if(o.isMesh&&o.material&&o.geometry&&o.visible&&o.parent.visible)meshes.push(o);});
 for(const child of g.children[12].children){
  const p=child.geometry.attributes.position,center=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(p,i)).reduce((a,b)=>a.add(b),new T.Vector3()).divideScalar(3),z=child.userData.reading==='front'?2:-2;
  const ray=new T.Raycaster(center.add(new T.Vector3(0,0,z)),new T.Vector3(0,0,-Math.sign(z)));
  const hits=ray.intersectObjects(meshes).sort((a,b)=>b.object.renderOrder-a.object.renderOrder);assert.equal(hits[0].object,child,'Nested color must render above its ancestors');
 }
});
test('view and step persist with bounded input',()=>{
 const s=normalizeSceneSettings({appearance:{sulfurRetainedExpansion:true,retainedExpansionStep:4,retainedExpansionAnimate:false}});
 assert.equal(s.appearance.sulfurRetainedExpansion,true);assert.equal(s.appearance.retainedExpansionStep,4);assert.equal(s.appearance.retainedExpansionAnimate,false);
 assert.equal(normalizeSceneSettings({appearance:{retainedExpansionStep:99}}).appearance.retainedExpansionStep,20);
});
