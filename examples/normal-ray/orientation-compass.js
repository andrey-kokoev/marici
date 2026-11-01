import {Quaternion,Vector3} from 'three';
export function orientationCompass(quaternion=[0,0,0,1]){
 const inverse=new Quaternion(...quaternion).normalize().invert(),center={x:76,y:70};
 const project=p=>{const v=new Vector3(...p).applyQuaternion(inverse);return {x:center.x+42*v.x,y:center.y-42*v.y,depth:v.z};};
 const axes=[{name:'X',vector:[1,0,0],color:'#ff7878'},{name:'Y',vector:[0,1,0],color:'#77dfa7'},{name:'Z',vector:[0,0,1],color:'#78adff'}];
 const directions=axes.flatMap(a=>[-1,1].map(sign=>{
  const p=a.vector.map(v=>v*sign),end=project(p),label=project(p.map(v=>v*1.3));
  if(Math.hypot(end.x-center.x,end.y-center.y)<7){label.x=center.x+(end.depth>=0?16:-16);label.y=center.y+(end.depth>=0?-11:11);}
  return {key:`${sign>0?'+':'−'}${a.name}`,color:a.color,positive:sign>0,...end,labelX:label.x,labelY:label.y};
 })).sort((a,b)=>a.depth-b.depth);
 const planes=[[0,1,'XY',axes[2].color],[0,2,'XZ',axes[1].color],[1,2,'YZ',axes[0].color]].map(([i,j,name,color],index)=>{
  const a=axes[i].vector.map(x=>x*.8),b=axes[j].vector.map(x=>x*.8),points=[[0,0,0],a,a.map((x,k)=>x+b[k]),b].map(project);
  return {name,color,legendX:25+index*51,points:points.map(p=>`${p.x},${p.y}`).join(' '),depth:points.reduce((s,p)=>s+p.depth,0)/4};
 }).sort((a,b)=>a.depth-b.depth);
 return {center,directions,planes};
}
