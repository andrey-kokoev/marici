import * as T from 'three';
export const retainedExpansionSteps=['White dot','Grow one arrow','Open two white triangles into a square','Color the square red / blue','Add the white X-axis diagonal','Helium-3 · split both halves vertically','Helium-4 · add the vertical white diagonal','Lithium-6 · split the upper-right along x=y','Lithium-7 · separate the right pair','Beryllium-9 · divide the left-center face','Boron-10 · split the upper-right face','Boron-11 · separate the upper-right pair','Carbon-12 · subdivide the upper-right triangle','Carbon-13 · separate the smaller pair','Nitrogen-14 · split the opposite upper face','Nitrogen-15 · separate the upper-left pair','Oxygen-16 · subdivide the topmost left triangle','Oxygen-17 · separate the smaller left pair','Fluorine-19 · split the topmost right triangle','Neon-20 · split the left-center face'];
export const retainedExpansionAtoms=Object.freeze({
 4:{name:'Hydrogen-1',protons:1,neutrons:0,shells:[1]},
 5:{name:'Hydrogen-2',protons:1,neutrons:1,shells:[1]},
 6:{name:'Helium-3',protons:2,neutrons:1,shells:[2]},
 7:{name:'Helium-4',protons:2,neutrons:2,shells:[2]},
 8:{name:'Lithium-6',protons:3,neutrons:3,shells:[2,1]},
 9:{name:'Lithium-7',protons:3,neutrons:4,shells:[2,1]},
 10:{name:'Beryllium-9',protons:4,neutrons:5,shells:[2,2]},
 11:{name:'Boron-10',protons:5,neutrons:5,shells:[2,3]},
 12:{name:'Boron-11',protons:5,neutrons:6,shells:[2,3]},
 13:{name:'Carbon-12',protons:6,neutrons:6,shells:[2,4]},
 14:{name:'Carbon-13',protons:6,neutrons:7,shells:[2,4]},
 15:{name:'Nitrogen-14',protons:7,neutrons:7,shells:[2,5]},
 16:{name:'Nitrogen-15',protons:7,neutrons:8,shells:[2,5]},
 17:{name:'Oxygen-16',protons:8,neutrons:8,shells:[2,6]},
 18:{name:'Oxygen-17',protons:8,neutrons:9,shells:[2,6]},
 19:{name:'Fluorine-19',protons:9,neutrons:10,shells:[2,7]},
 20:{name:'Neon-20',protons:10,neutrons:10,shells:[2,8]},
});
// Reference data, not derived from geometry: NIST representative natural
// abundances and IAEA/ENSDF stability, as in isotope-electron-shells.html.
const naturalAbundancePercent={
 'Hydrogen-1':'99.9885','Hydrogen-2':'0.0115','Helium-3':'0.000134','Helium-4':'99.999866',
 'Lithium-6':'7.59','Lithium-7':'92.41','Beryllium-9':'100','Boron-10':'19.9','Boron-11':'80.1',
 'Carbon-12':'98.93','Carbon-13':'1.07','Nitrogen-14':'99.636','Nitrogen-15':'0.364',
 'Oxygen-16':'99.757','Oxygen-17':'0.038','Fluorine-19':'100','Neon-20':'90.48',
};
for(const atom of Object.values(retainedExpansionAtoms)){
 atom.abundancePercent=naturalAbundancePercent[atom.name];
 atom.stability='Stable';
}
export const retainedExpansionViewportLabels=Object.freeze(Object.fromEntries(Object.entries(retainedExpansionAtoms).map(([step,atom])=>[
 step,[atom.name,`neutrons: ${atom.neutrons}`,`protons: ${atom.protons}`,`electrons: ${atom.shells.reduce((sum,n)=>sum+n,0)}`,...atom.shells.map((n,i)=>`- shell ${i+1}: ${n}/${2*(i+1)**2}`)].join('\n'),
])));
export const retainedExpansionEnvelope=[[-.3,-.3,0],[3.3,-.3,0],[3.3,1.8,0],[-.3,1.8,0]];
export const retainedExpansionSquareEnvelope=[[-.3,-1.8,0],[3.3,-1.8,0],[3.3,1.8,0],[-.3,1.8,0]];
export function createRetainedExpansion(step=1){
 if(!Number.isInteger(step)||step<1||step>20)throw Error('Retained expansion has twenty steps');
 const group=new T.Group(),white=0xffffff;
 function marker(){const dot=new T.Mesh(new T.SphereGeometry(.07,16,12),new T.MeshBasicMaterial({color:white,depthTest:false,transparent:true,depthWrite:false}));dot.renderOrder=5;return dot;}
 function edge(from,to){
  const a=new T.Vector3(...from),b=new T.Vector3(...to),direction=b.clone().sub(a);
  const mesh=new T.Mesh(new T.CylinderGeometry(.018,.018,direction.length(),12),new T.MeshBasicMaterial({color:white,depthTest:false,transparent:true,depthWrite:false}));
  mesh.position.copy(a).add(b).multiplyScalar(.5);mesh.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),direction.normalize());mesh.renderOrder=4;return mesh;
 }
 const dot=marker();group.add(dot);
 const arrow=new T.Group();arrow.add(edge([0,0,0],[3,0,0]));
 group.add(arrow);
 const vertices=[[0,0,0],[3,0,0],[1.5,1.5,0]],geometry=new T.BufferGeometry().setFromPoints(vertices.map(p=>new T.Vector3(...p)));
 const plane=new T.Group();
 // Opposite sides of ONE geometric triangle, not two adjacent colored triangles.
 const front=new T.Mesh(geometry,new T.MeshBasicMaterial({color:white,side:T.FrontSide,transparent:false,opacity:1,depthWrite:true}));
 const back=new T.Mesh(geometry,new T.MeshBasicMaterial({color:white,side:T.BackSide,transparent:false,opacity:1,depthWrite:true}));
 const border=new T.Group();border.add(edge(vertices[0],vertices[2]),edge(vertices[2],vertices[1]));plane.add(front,back,border);group.add(plane);
 const tip=marker();group.add(tip);
 const midpoint=[1.5,0,0],drops=new T.Group(),sideFaces=new T.Group();
 const dropSources=[vertices[2]],dropTargets=[midpoint];
 for(const [i,from] of dropSources.entries()){
  const a=new T.Vector3(...from),direction=new T.Vector3(...dropTargets[i]).sub(a),length=direction.length(),drop=new T.Group();
  drop.position.copy(a);drop.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),direction.normalize());
  const shaft=new T.Mesh(new T.CylinderGeometry(.018,.018,1,12),arrow.children[0].material.clone());shaft.renderOrder=4;
  drop.add(shaft);drop.userData.length=length;drops.add(drop);
 }
 for(const [name,colour,points] of [['left',0xff3030,[vertices[0],midpoint,vertices[2]]],['right',0x3080ff,[midpoint,vertices[1],vertices[2]]]]){
  const geometry=new T.BufferGeometry().setFromPoints(points.map(p=>new T.Vector3(...p)));
  for(const [side,reading,color] of [[T.FrontSide,'front',colour],[T.BackSide,'back',colour===0xff3030?0x3080ff:0xff3030]]){
   const face=new T.Mesh(geometry,new T.MeshBasicMaterial({color,side,transparent:true,opacity:0,depthTest:false,depthWrite:false}));face.renderOrder=1;Object.assign(face.userData,{face:name,reading,baseColour:color});sideFaces.add(face);
  }
 }
 group.add(drops,sideFaces);
 const insets=new T.Group();
 for(const field of sideFaces.children){
  if(step>=6&&field.userData.face==='right')continue;
  const positions=field.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const left=field.userData.face==='left',anchor=points[left?1:0],mid=points[left?0:1].clone().add(points[2]).multiplyScalar(.5);
  const split=left?[[points[0],anchor,mid],[anchor,points[2],mid]]:[[anchor,points[1],mid],[anchor,mid,points[2]]];
  for(const [slot,triangle] of split.entries()){
   // Step 6 only changes color: its two regions exactly cover the original field.
   const center=triangle.reduce((sum,p)=>sum.add(p),new T.Vector3()).divideScalar(3);
   const geometry=new T.BufferGeometry().setFromPoints(left&&step>=6?triangle.map(p=>p.clone()):triangle.map(p=>p.clone().sub(center).multiplyScalar(.84).add(center)));
   const red=(slot===0)===(field.userData.reading==='front');
   const inset=new T.Mesh(geometry,new T.MeshBasicMaterial({color:red?0xff3030:0x3080ff,side:field.material.side,transparent:true,opacity:0,depthTest:false,depthWrite:false}));inset.renderOrder=2;Object.assign(inset.userData,{face:field.userData.face,reading:field.userData.reading,slot});insets.add(inset);
  }
 }
 group.add(insets);
 const splitFaces=new T.Group();
 if(step>=10)for(const parent of insets.children.filter(mesh=>mesh.userData.face==='left'&&mesh.userData.slot===1)){
  parent.userData.splitParent=true;
  const positions=parent.geometry.attributes.position;
  const points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[0].clone().add(points[1]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],mid,points[2]],[mid,points[1],points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const material=parent.material.clone();
   if(part===1)material.color.setHex(parent.material.color.getHex()===0xff3030?0x3080ff:0xff3030);
   const child=new T.Mesh(geometry,material);child.renderOrder=2;
   Object.assign(child.userData,{face:'left',reading:parent.userData.reading,part});splitFaces.add(child);
  }
 }
 group.add(splitFaces);
 const separator=new T.Group();
 if(step>=7){
  const positions=insets.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,1).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;separator.add(line);
 }
 if(step>=9){
  const line=edge(midpoint,[2.25,.75,0]);
  line.renderOrder=3;line.userData.newPair=true;separator.add(line);
 }
 if(step>=10){
  const positions=splitFaces.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,1).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;line.userData.largeFace=true;separator.add(line);
 }
 group.add(separator);
 const recoloredFace=new T.Group();
 if(step>=8){
  const geometry=new T.BufferGeometry().setFromPoints([midpoint,[2.25,.75,0],vertices[2]].map(p=>new T.Vector3(...p)));
  for(const [side,reading,color] of [[T.FrontSide,'front',0xff3030],[T.BackSide,'back',0x3080ff]]){
   const face=new T.Mesh(geometry,new T.MeshBasicMaterial({color,side,transparent:true,opacity:1,depthTest:false,depthWrite:false}));
   face.renderOrder=2;Object.assign(face.userData,{reading,baseColour:color});recoloredFace.add(face);
  }
 }
 group.add(recoloredFace);
 const rightSplit=new T.Group();
 if(step>=11)for(const parent of recoloredFace.children){
  const positions=parent.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[0].clone().add(points[2]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],points[1],mid],[mid,points[1],points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const material=parent.material.clone();
   if(part===1)material.color.setHex(parent.userData.baseColour===0xff3030?0x3080ff:0xff3030);
   const child=new T.Mesh(geometry,material);child.renderOrder=2.5;
   Object.assign(child.userData,{face:'right',reading:parent.userData.reading,part});rightSplit.add(child);
  }
 }
 group.add(rightSplit);
 if(step>=12){
  const positions=rightSplit.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,1).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;line.userData.rightPair=true;separator.add(line);
 }
 const carbonSplit=new T.Group();
 if(step>=13)for(const parent of rightSplit.children.filter(mesh=>mesh.userData.part===1)){
  parent.userData.carbonParent=true;
  const positions=parent.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[1].clone().add(points[2]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],points[1],mid],[points[0],mid,points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const child=new T.Mesh(geometry,parent.material.clone());child.renderOrder=2.7;
   Object.assign(child.userData,{face:'right',reading:parent.userData.reading,part});carbonSplit.add(child);
  }
 }
 group.add(carbonSplit);
 if(step>=14){
  const positions=carbonSplit.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,0).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;line.userData.carbonPair=true;separator.add(line);
 }
 const nitrogenSplit=new T.Group();
 if(step>=15)for(const parent of splitFaces.children.filter(mesh=>mesh.userData.part===1)){
  const positions=parent.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[1].clone().add(points[2]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],points[1],mid],[points[0],mid,points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const child=new T.Mesh(geometry,parent.material.clone());child.renderOrder=2.8;
   Object.assign(child.userData,{face:'left',reading:parent.userData.reading,part});nitrogenSplit.add(child);
  }
 }
 group.add(nitrogenSplit);
 if(step>=16){
  const positions=nitrogenSplit.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,0).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;line.userData.nitrogenPair=true;separator.add(line);
 }
 const oxygenSplit=new T.Group();
 if(step>=17)for(const parent of nitrogenSplit.children.filter(mesh=>mesh.userData.part===0)){
  const positions=parent.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[0].clone().add(points[1]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],mid,points[2]],[mid,points[1],points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const child=new T.Mesh(geometry,parent.material.clone());child.renderOrder=2.9;
   Object.assign(child.userData,{face:'left',reading:parent.userData.reading,part});oxygenSplit.add(child);
  }
 }
 group.add(oxygenSplit);
 if(step>=18){
  const positions=oxygenSplit.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,1).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;line.userData.oxygenPair=true;separator.add(line);
 }
 const fluorineSplit=new T.Group();
 if(step>=19)for(const parent of carbonSplit.children.filter(mesh=>mesh.userData.part===1)){
  const positions=parent.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[0].clone().add(points[2]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],points[1],mid],[mid,points[1],points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const child=new T.Mesh(geometry,parent.material.clone());child.renderOrder=2.75;
   Object.assign(child.userData,{face:'right',reading:parent.userData.reading,part});fluorineSplit.add(child);
  }
 }
 group.add(fluorineSplit);
 if(step>=19){
  const positions=fluorineSplit.children[0].geometry.attributes.position;
  const line=edge(new T.Vector3().fromBufferAttribute(positions,1).toArray(),new T.Vector3().fromBufferAttribute(positions,2).toArray());
  line.renderOrder=3;line.userData.fluorinePair=true;separator.add(line);
 }
 const neonSplit=new T.Group();
 if(step>=20)for(const parent of splitFaces.children.filter(mesh=>mesh.userData.part===0)){
  const positions=parent.geometry.attributes.position,points=Array.from({length:3},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));
  const mid=points[0].clone().add(points[2]).multiplyScalar(.5);
  for(const [part,triangle] of [[points[0],points[1],mid],[mid,points[1],points[2]]].entries()){
   const geometry=new T.BufferGeometry().setFromPoints(triangle.map(p=>p.clone()));
   const child=new T.Mesh(geometry,parent.material.clone());child.renderOrder=2.75;
   Object.assign(child.userData,{face:'left',reading:parent.userData.reading,part});neonSplit.add(child);
  }
 }
 group.add(neonSplit);
 // Square construction for steps 3–8; later steps retain the legacy layout.
 const squareStage=step>=3&&step<=8;
 const oppositePlane=new T.Group();
 if(squareStage){
  const points=[vertices[0],[1.5,-1.5,0],vertices[1]];
  const geometry=new T.BufferGeometry().setFromPoints(points.map(p=>new T.Vector3(...p)));
  for(const [side,color] of [[T.FrontSide,0x3080ff],[T.BackSide,0xff3030]]){
   oppositePlane.add(new T.Mesh(geometry,new T.MeshBasicMaterial({color,side,transparent:false,opacity:1,depthWrite:true})));
  }
  const outline=new T.Group();outline.add(edge(points[0],points[1]),edge(points[1],points[2]));oppositePlane.add(outline);
  const lowerTip=marker();lowerTip.position.set(1.5,-1.5,0);oppositePlane.add(lowerTip);
  group.add(oppositePlane);
 }
 const squareFaces=new T.Group(),squareSeparator=new T.Group();
 if(step>=6&&step<=8){
  const center=[1.5,0,0],bottom=[1.5,-1.5,0];
  for(const [region,colour,triangles] of [
   ['upper',0xff3030,[[vertices[0],center,vertices[2]],[center,vertices[1],vertices[2]]]],
   ['lower',0x3080ff,[[vertices[0],bottom,center],[center,bottom,vertices[1]]]],
  ])for(const [part,points] of triangles.entries()){
   const geometry=new T.BufferGeometry().setFromPoints(points.map(p=>new T.Vector3(...p)));
   for(const [side,reading] of [[T.FrontSide,'front'],[T.BackSide,'back']]){
    const own=reading==='front'?colour:colour===0xff3030?0x3080ff:0xff3030;
    const face=new T.Mesh(geometry,new T.MeshBasicMaterial({color:own,side,depthTest:false,depthWrite:false}));
    face.renderOrder=2;Object.assign(face.userData,{region,part,reading,baseColour:own});squareFaces.add(face);
   }
  }
  group.add(squareFaces);
  if(step>=7){
   const line=edge(bottom,vertices[2]);line.renderOrder=3;squareSeparator.add(line);
  }
  if(step===8){
   const line=edge([1.5,0,0],[2.25,.75,0]);line.renderOrder=3;squareSeparator.add(line);
  }
  group.add(squareSeparator);
 }
 const audit={viewportLabel:retainedExpansionViewportLabels[step]??null,insetPairsPerSide:step>=6?1:0,splitFields:step>=8?['left','right']:step>=6?['left']:[],whiteSeparator:step>=7,newPairSeparator:step>=9,largeFaceSeparator:step>=10,splitColoredFace:step>=10?{face:'left',slot:1}:step>=8?{face:'right',slot:null}:null,rightSplit:step>=11,rightPairSeparator:step>=12,carbonSplit:step>=13,carbonPairSeparator:step>=14,nitrogenSplit:step>=15,nitrogenPairSeparator:step>=16,oxygenSplit:step>=17,oxygenPairSeparator:step>=18,fluorineSplit:step>=19,fluorinePairSeparator:step>=19,neonSplit:step>=20,unplacedAdditionalNeutrons:0,insetTriangles:step>=20?10:step>=19?9:step>=17?8:step>=15?7:step>=13?6:step>=11?5:step>=10?3:step>=8?2:step>=6?2:0,whiteningProgress:0,insetProgress:0,droppedArrows:step>=5?1:0,planar:true,dropSources,dropTargets,dropProgress:0,sideFaceProgress:0,step,label:retainedExpansionSteps[step-1],dot:step<4,dots:step<4?1:0,arrowDirections:0,growingLines:step>=5?2:step>=2?1:0,rectangle:false,triangles:step>=20?12:step>=19?11:step>=17?10:step>=15?9:step>=13?8:step>=11?7:step>=10?6:step>=8?5:step>=6?4:step===5?2:step>=3?1:0,colouredTriangles:step>=20?11:step>=19?10:step>=17?9:step>=15?8:step>=13?7:step>=11?6:step>=10?5:step>=8?4:step>=6?3:step>=5?2:step>=4?1:0,insetSides:step>=20?{front:{left:['red','blue','red','blue','red','red'],right:['red','blue','red','blue']},back:{left:['blue','red','blue','red','blue','blue'],right:['blue','red','blue','red']}}:step>=19?{front:{left:['red','blue','blue','red','red'],right:['red','blue','red','blue']},back:{left:['blue','red','red','blue','blue'],right:['blue','red','blue','red']}}:step>=17?{front:{left:['red','blue','blue','red','red'],right:['red','blue','red']},back:{left:['blue','red','red','blue','blue'],right:['blue','red','blue']}}:step>=15?{front:{left:['red','blue','blue','red'],right:['red','blue','red']},back:{left:['blue','red','red','blue'],right:['blue','red','blue']}}:step>=13?{front:{left:['red','blue','red'],right:['red','blue','red']},back:{left:['blue','red','blue'],right:['blue','red','blue']}}:step>=11?{front:{left:['red','blue','red'],right:['red','blue']},back:{left:['blue','red','blue'],right:['blue','red']}}:step>=10?{front:{left:['red','blue','red']},back:{left:['blue','red','blue']}}:step>=6?{front:{left:['red','blue']},back:{left:['blue','red']}}:null,faceSides:step>=8?{front:{left:'white',right:{lower:'blue',upper:'red'}},back:{left:'white',right:{lower:'red',upper:'blue'}}}:step>=7?{front:{left:'white',right:'blue'},back:{left:'white',right:'red'}}:step>=5?{front:{left:'red',right:'blue'},back:{left:'blue',right:'red'}}:step>=4?{front:'red',back:'blue'}:{front:'white',back:'white'},sharedEdge:[[0,0,0],[3,0,0]],tipPositions:[],progress:0};group.userData.audit=audit;
 group.userData.animate=(elapsed,state={})=>{
  const p=Math.min(1,Math.max(0,elapsed/(step>=6?1200:900))),spread=step===3?p:1;audit.progress=p;group.visible=state.bodies!==false;
  dot.visible=step<3;dot.scale.setScalar(step===1?Math.max(.001,p):1);
  arrow.visible=step>=2;arrow.scale.x=step===2?Math.max(.001,p):1;
  plane.visible=step>=3;plane.scale.y=spread;tip.visible=step===3&&p<1;
  tip.position.set(1.5,1.5*spread,0);
  audit.dots=step<3?1:tip.visible?1:0;audit.dot=audit.dots>0;audit.tipPositions=step>=3?[tip.position.toArray()]:[];
  for(const [mesh,colour] of [[front,0xff3030],[back,0x3080ff]]){
   mesh.visible=!state.edgesOnly;mesh.material.color.setHex(white);
   if(step>=4)mesh.material.color.lerp(new T.Color(colour),step===4?p:1);
   mesh.material.opacity=state.faceOpacity??1;
   mesh.material.transparent=mesh.material.opacity<1;mesh.material.depthWrite=!mesh.material.transparent;
  }
  const dropProgress=step>=6?1:Math.min(1,Math.max(0,elapsed/1200)),faceProgress=step>=6?1:Math.min(1,Math.max(0,(elapsed-1200)/600));
  const whitening=step>=7&&step!==8&&step!==11&&step!==13&&step!==15&&step!==17&&step!==19&&step!==20?Math.min(1,Math.max(0,elapsed/600)):0,insetProgress=step===6||step===8||step===11||step===13||step===15||step===17||step===19||step===20?p:step>=7?Math.min(1,Math.max(0,(elapsed-600)/600)):0;
  drops.visible=step>=5;sideFaces.visible=step>=5&&!state.edgesOnly&&faceProgress>0;
  drops.children.forEach(drop=>{const length=drop.userData.length*dropProgress;drop.visible=length>0;drop.children[0].scale.y=length;drop.children[0].position.y=length/2;});
  sideFaces.children.forEach(face=>{const retained=step>=7&&face.userData.face==='left',unsplit=step>=6&&face.userData.face==='right';face.material.color.setHex(face.userData.baseColour).lerp(new T.Color(white),retained?1:unsplit?0:whitening);face.material.opacity=faceProgress*(state.faceOpacity??1);});
  insets.visible=step>=6&&!state.edgesOnly&&(step>=7||insetProgress>0);
  insets.children.forEach(mesh=>{const progress=step>=8?(mesh.userData.splitParent||mesh.userData.carbonParent?0:1):step===7&&mesh.userData.face==='left'?1:insetProgress;mesh.visible=progress>0;mesh.material.opacity=progress*(state.faceOpacity??1);});
  recoloredFace.visible=step>=8&&!state.edgesOnly&&(step>=9||p>0);
  recoloredFace.children.forEach(face=>{face.material.color.setHex(face.userData.baseColour);face.material.opacity=(step>=9?1:p)*(state.faceOpacity??1);});
  rightSplit.visible=step>=11&&!state.edgesOnly;
  rightSplit.children.forEach(face=>{const own=face.userData.reading==='front'?0xff3030:0x3080ff,opposite=own===0xff3030?0x3080ff:0xff3030;face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===1?(step===11?p:1):0);face.material.opacity=state.faceOpacity??1;});
  separator.visible=step>=7&&!state.edgesOnly;
  separator.children.forEach(line=>{line.scale.y=(step===7||(step===9&&line.userData.newPair)||(step===10&&line.userData.largeFace)||(step===12&&line.userData.rightPair)||(step===14&&line.userData.carbonPair)||(step===16&&line.userData.nitrogenPair)||(step===18&&line.userData.oxygenPair)||(step===19&&line.userData.fluorinePair))?p:1;line.visible=line.scale.y>0;});
  splitFaces.visible=step>=10&&!state.edgesOnly;
  splitFaces.children.forEach(mesh=>{const own=mesh.userData.reading==='front'?0x3080ff:0xff3030,opposite=own===0xff3030?0x3080ff:0xff3030;mesh.material.color.setHex(own).lerp(new T.Color(opposite),mesh.userData.part===1?(step===10?p:1):0);mesh.material.opacity=state.faceOpacity??1;});
  carbonSplit.visible=step>=13&&!state.edgesOnly;
  carbonSplit.children.forEach(face=>{const own=face.userData.reading==='front'?0x3080ff:0xff3030,opposite=own===0xff3030?0x3080ff:0xff3030;face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===1?(step===13?p:1):0);face.material.opacity=state.faceOpacity??1;});
  nitrogenSplit.visible=step>=15&&!state.edgesOnly;
  nitrogenSplit.children.forEach(face=>{const own=face.userData.reading==='front'?0xff3030:0x3080ff,opposite=own===0xff3030?0x3080ff:0xff3030;face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===0?(step===15?p:1):0);face.material.opacity=state.faceOpacity??1;});
  oxygenSplit.visible=step>=17&&!state.edgesOnly;
  oxygenSplit.children.forEach(face=>{const own=face.userData.reading==='front'?0x3080ff:0xff3030,opposite=own===0xff3030?0x3080ff:0xff3030;face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===1?(step===17?p:1):0);face.material.opacity=state.faceOpacity??1;});
  fluorineSplit.visible=step>=19&&!state.edgesOnly;
  fluorineSplit.children.forEach(face=>{const own=face.userData.reading==='front'?0xff3030:0x3080ff,opposite=own===0xff3030?0x3080ff:0xff3030;face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===1?(step===19?p:1):0);face.material.opacity=state.faceOpacity??1;});
  neonSplit.visible=step>=20&&!state.edgesOnly;
  neonSplit.children.forEach(face=>{const own=face.userData.reading==='front'?0x3080ff:0xff3030,opposite=own===0xff3030?0x3080ff:0xff3030;face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===1?(step===20?p:1):0);face.material.opacity=state.faceOpacity??1;});
  if(step>=5&&faceProgress===1){front.visible=false;back.visible=false;}
  audit.dropProgress=step>=5?dropProgress:0;audit.sideFaceProgress=step>=5?faceProgress:0;audit.whiteningProgress=whitening;audit.insetProgress=insetProgress;
  if(squareStage){
   drops.visible=false;sideFaces.visible=false;insets.visible=false;separator.visible=false;
   front.visible=back.visible=!state.edgesOnly;
   const opening=step===3?p:1;
   arrow.visible=step>=5&&(step!==5||p>0);arrow.scale.x=step===5?p:1;
   oppositePlane.visible=opening>0;oppositePlane.scale.y=opening;
   for(const [i,face] of oppositePlane.children.slice(0,2).entries()){
    face.material.color.setHex(white).lerp(new T.Color(i===0?0x3080ff:0xff3030),step===3?0:step===4?p:1);
    face.visible=!state.edgesOnly;face.material.opacity=state.faceOpacity??1;
    face.material.transparent=face.material.opacity<1;face.material.depthWrite=!face.material.transparent;
   }
   tip.visible=step===3&&p<1&&!state.edgesOnly;
   oppositePlane.children[3].visible=tip.visible;
   squareFaces.visible=!state.edgesOnly;
   for(const face of squareFaces.children){
    const own=face.userData.baseColour,opposite=own===0xff3030?0x3080ff:0xff3030;
    face.material.color.setHex(own).lerp(new T.Color(opposite),face.userData.part===1?(step===6?p:1):0);
    face.material.opacity=state.faceOpacity??1;face.material.transparent=face.material.opacity<1;
   }
   squareSeparator.visible=step>=7&&!state.edgesOnly;
   if(step>=7){squareSeparator.children[0].scale.y=step===7?p:1;squareSeparator.children[0].visible=step!==7||p>0;}
   if(step===8){
    for(const face of recoloredFace.children)face.renderOrder=2.5;
    squareSeparator.children[1].scale.y=p;squareSeparator.children[1].visible=p>0;
   }
   const sides=step===3?{front:{upper:'white',lower:'white'},back:{upper:'white',lower:'white'}}:step<=5?{front:{upper:'red',lower:'blue'},back:{upper:'blue',lower:'red'}}:
    {front:{upper:['red','blue'],lower:['blue','red']},back:{upper:['blue','red'],lower:['red','blue']}};
   Object.assign(audit,{rectangle:true,square:true,droppedArrows:0,dropSources:[],dropTargets:[],dropProgress:0,
    growingLines:step>=7?2:step>=5?1:0,sideFaceProgress:opening,tipPositions:step===3?[tip.position.toArray(),[1.5,-1.5*opening,0]]:[tip.position.toArray()],dot:tip.visible,dots:tip.visible?2:0,
    horizontalSeparator:step>=5,faceSides:sides,splitFields:step>=6?['upper','lower']:[],triangles:step>=6?4:2,colouredTriangles:step===3?0:step>=6?4:2,
    insetTriangles:step>=6?4:0,insetPairsPerSide:step>=6?2:0,insetSides:step>=6?sides:null,
    insetProgress:step===6?p:step>=7?1:0,whiteningProgress:0,
    verticalSplit:step>=6?[[1.5,-1.5,0],[1.5,1.5,0]]:null});
   if(step===8){
    const sides={front:{upper:['red','blue','red'],lower:['blue','red']},back:{upper:['blue','red','blue'],lower:['red','blue']}};
    Object.assign(audit,{triangles:5,colouredTriangles:5,insetTriangles:5,faceSides:sides,insetSides:sides,newPairSeparator:true,growingLines:3,
     splitColoredFace:{face:'upper',slot:1},diagonalSplit:[[1.5,0,0],[2.25,.75,0]],splitOrigin:[1.5,0,0]});
   }
  }
  return p<1;
 };
 group.userData.animate(Infinity);return group;
}
