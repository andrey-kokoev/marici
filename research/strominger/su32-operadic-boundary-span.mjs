// Finite ribbon-tree envelope. Composite OPERATIONS retain their generators;
// no operation tree is identified with a static content value.
import assert from 'node:assert/strict';
const copy=structuredClone;
export const canonicalCycle=xs=>Array.from({length:xs.length},(_,i)=>[...xs.slice(i),...xs.slice(0,i)]).sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b)))[0];
export function tree(profile=0){
 const ends={a:['a','C'],b:['b','C'],z:['z','J'],k:['k','D'],o:['D','o'],u:['C','J'],v:['J','D']};
 const cycles={C:['a:C','b:C','u:C'],J:['u:J','z:J','v:J'],D:['v:D','k:D','o:D']};
 const blocks=Object.entries(cycles).map(([id,arcs],i)=>({members:[id],arcs:(profile>>i)&1?[...arcs].reverse():arcs,sewn:[]}));
 for(const id of ['a','b','z','k','o'])blocks.push({members:[id],arcs:[id+':'+id],sewn:[]});
 const alpha={};for(const [e,[a,b]] of Object.entries(ends)){alpha[e+':'+a]=e+':'+b;alpha[e+':'+b]=e+':'+a;}
 return {blocks,alpha,primitiveProfiles:Object.fromEntries(blocks.filter(b=>['C','J','D'].includes(b.members[0])).map(b=>[b.members[0],copy(b.arcs)])),planarProfile:profile};
}
export function contour(t){
 const sigma={};for(const b of t.blocks)b.arcs.forEach((a,i)=>sigma[a]=b.arcs[(i+1)%b.arcs.length]);
 const start=Object.keys(t.alpha)[0],walk=[];let a=start;
 do{assert(!walk.includes(a));walk.push(a);a=sigma[t.alpha[a]];}while(a!==start);
 assert.equal(walk.length,Object.keys(t.alpha).length,'Tree must have one boundary contour');
 const external=walk.filter(a=>a.split(':')[0]===a.split(':')[1]);assert.equal(external.length,5);
 return canonicalCycle(external);
}
export const gaps=t=>{const c=contour(t);return c.map((a,i)=>[a,c[(i+1)%c.length]]);};
export function contract(t,edge){
 const out=copy(t),arcs=Object.keys(out.alpha).filter(a=>a.startsWith(edge+':'));assert.equal(arcs.length,2);
 const [a,b]=arcs,ia=out.blocks.findIndex(x=>x.arcs.includes(a)),ib=out.blocks.findIndex(x=>x.arcs.includes(b));assert.notEqual(ia,ib,'No self-gluing is supplied');
 const A=out.blocks[ia],B=out.blocks[ib];
 const after=(xs,x)=>{const i=xs.indexOf(x);return [...xs.slice(i+1),...xs.slice(0,i)];};
 const merged={members:[...A.members,...B.members].sort(),arcs:canonicalCycle([...after(A.arcs,a),...after(B.arcs,b)]),sewn:[...A.sewn,...B.sewn,edge].sort()};
 out.blocks=out.blocks.filter((_,i)=>i!==ia&&i!==ib);out.blocks.push(merged);delete out.alpha[a];delete out.alpha[b];return out;
}
export function normal(t){return {blocks:t.blocks.map(b=>({...b,arcs:canonicalCycle(b.arcs)})).sort((a,b)=>a.members.join().localeCompare(b.members.join())),alpha:t.alpha,planarProfile:t.planarProfile};}
export function boundaryOperation(t,sourceGenerators){
 const full=contract(contract(t,'u'),'v'),operation=full.blocks.find(b=>b.members.length===3);assert(operation);
 return {kind:'formal-source-composite-operation',boundary:contour(full),gaps:gaps(full),
  sourceGenerators:copy(sourceGenerators),sewnInternalEdges:operation.sewn,
  planarProfile:t.planarProfile,contentValue:null};
}
export function rootLifts(t,root){
 const owner=new Map(t.blocks.flatMap((b,i)=>b.arcs.map(a=>[a,i]))),r=owner.get(root);assert.notEqual(r,undefined);
 const distance=new Map([[r,0]]),queue=[r];
 for(let k=0;k<queue.length;k++)for(const a of t.blocks[queue[k]].arcs){const n=owner.get(t.alpha[a]);if(!distance.has(n)){distance.set(n,distance.get(queue[k])+1);queue.push(n);}}
 assert.equal(distance.size,t.blocks.length);
 return t.blocks.filter(b=>b.members.some(m=>['C','J','D'].includes(m))).map(b=>{
  const i=owner.get(b.arcs[0]),out=b.arcs.filter(a=>distance.get(owner.get(t.alpha[a]))<distance.get(i));assert.equal(out.length,1);
  return {component:b.members,outputArc:out[0],outputColour:t.alpha[out[0]]};
 });
}
