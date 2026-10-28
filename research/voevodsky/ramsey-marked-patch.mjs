// Read-only composite of the existing honeycomb geometry API, not particle rules.
import {makeLatticeItem,itemKey} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {LocalPrimitiveGeometry} from '../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
export class PatchResourceError extends Error {}
const LIMIT=2**20,faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]],e0=[1,0,0,0];
const sum=a=>a.reduce((x,y)=>x+y,0),key=p=>p.join(','),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function require(c,message){if(!c)throw new RangeError(message);}
export const F=b=>[b[1]+b[2],b[1]+b[3],b[2]+b[3]];
export const t=v=>[(v[0]+v[1]+v[2])/2,(-v[0]-v[1]+v[2])/2,(-v[0]+v[1]-v[2])/2,(v[0]-v[1]-v[2])/2];
function integral(a,n){return Array.isArray(a)&&a.length===n&&a.every(Number.isSafeInteger);}
export function sourceItem(spec){
 require(spec&&['tetrahedron','octahedron'].includes(spec.kind)&&integral(spec.origin,4),'invalid source specification');
 require(Object.keys(spec).every(k=>['kind','origin','inverted'].includes(k)),'unknown source specification fields');
 require(spec.inverted===undefined||typeof spec.inverted==='boolean','invalid inversion');
 require(spec.kind==='tetrahedron'||!spec.inverted,'octahedron has no inversion flag');
 if(spec.origin.some(x=>Math.abs(x)>LIMIT))throw new PatchResourceError('source coordinates outside exact execution envelope');
 return makeLatticeItem(spec.kind,spec.origin,spec.inverted??false);
}
export function chamberIndex(owner){return owner.origin.map((x,i)=>e0[i]-x-(owner.kind==='tetrahedron'&&owner.inverted?0:1));}
export function chamberItem(k){
 const q=-sum(k);require([1,2,3].includes(q),'not a chamber');
 const origin=k.map((x,i)=>e0[i]-x-(q===1?0:1));
 return makeLatticeItem(q===2?'octahedron':'tetrahedron',origin,q===1);
}
export function transformPoint(v,a,m){return v.map((x,i)=>a[i]+m*x);}
export function buildPatch(spec,a,m,labels=null){
 const source=sourceItem(spec);
 require(integral(a,3)&&sum(a)%2===0,'translation must be in D3');
 require(Number.isSafeInteger(m)&&m>=1,'positive integral scale required');
 // Resource refusals are not no-witness results. All used structural integer
 // arithmetic stays far below 2^53; drawing centers are never read.
 if(m>16||a.some(x=>Math.abs(x)>LIMIT))throw new PatchResourceError('patch exceeds execution envelope');
 const k=chamberIndex(source),shift=t(a),lo=k.map((x,i)=>shift[i]+m*x);
 if(lo.some(x=>Math.abs(x)+m>LIMIT))throw new PatchResourceError('target coordinates outside exact execution envelope');
 labels=labels??source.vertices.map((_,i)=>String(i));
 require(Array.isArray(labels)&&labels.length===source.vertices.length&&labels.every(x=>typeof x==='string'&&x.length)&&new Set(labels).size===labels.length,'distinct complete source labels required');
 const items=[];
 for(let r0=0;r0<m;r0++)for(let r1=0;r1<m;r1++)for(let r2=0;r2<m;r2++)for(let r3=0;r3<m;r3++){
  const j=[r0,r1,r2,r3].map((r,i)=>lo[i]+r);
  if([1,2,3].includes(-sum(j)))items.push(chamberItem(j));
 }
 items.sort((a,b)=>a.key<b.key?-1:a.key>b.key?1:0);
 require(items.length>0,'empty full-dimensional patch');
 const components=new Map(),incidences=new Map(),vertices=new Map();
 for(const owner of items)for(const component of owner.components){
  const ck=itemKey(component);require(!components.has(ck),'duplicate primitive');
  components.set(ck,{owner,component});
  component.forEach(p=>vertices.set(key(p),p));
  for(const f of faces){const face=f.map(i=>component[i]),fk=itemKey(face);
   if(!incidences.has(fk))incidences.set(fk,[]);
   incidences.get(fk).push({ck,face});
  }
 }
 require([...incidences.values()].every(xs=>xs.length===1||xs.length===2),'nonmanifold primitive face');
 // Replay the actual source primitive-neighbor API, retaining full owner and
 // fixed-octahedron-component data; no PN/NE packet is fabricated.
 const geometry=new LocalPrimitiveGeometry(),first=[...components.keys()].sort()[0],seed=components.get(first);
 const ids=new Map([[first,geometry.register(seed.owner,seed.component)]]),queue=[first],tree=[];
 let neighborReplays=0;
 for(let cursor=0;cursor<queue.length;cursor++){
  const ck=queue[cursor],entry=components.get(ck);
  for(const f of faces){const face=f.map(i=>entry.component[i]),fk=itemKey(face),xs=incidences.get(fk);
   if(xs.length!==2)continue;
   const target=xs.find(x=>x.ck!==ck);
   const id=geometry.neighbor(ids.get(ck),face.map(key));neighborReplays++;
   require(geometry.cells[id].key===target.ck,'source primitive neighbor disagrees');
   require(geometry.cells[id].owner.key===components.get(target.ck).owner.key,'source macro-owner changed');
   if(!ids.has(target.ck)){
    ids.set(target.ck,id);queue.push(target.ck);
    tree.push({from:ck,face:fk,to:target.ck});
   }else require(ids.get(target.ck)===id,'primitive identity changed on replay');
  }
 }
 require(ids.size===components.size,'disconnected patch');
 const sourceVertices=source.vertices.map(F),marks=labels.map((label,i)=>({label,source:sourceVertices[i],point:transformPoint(sourceVertices[i],a,m)}));
 const spatialVertices=new Map([...vertices.values()].map(b=>[key(F(b)),F(b)]));
 require(marks.every(mark=>spatialVertices.has(key(mark.point))),'marked corner missing');
 return {source:{kind:source.kind,origin:[...source.origin],inverted:source.inverted,key:source.key},a:[...a],m,
  marks,items,components,spatialVertices,seed:first,tree,neighborReplays,
  boundaryFaces:[...incidences].filter(([,xs])=>xs.length===1).map(([fk])=>fk).sort()};
}
export function validateMarks(patch,marks){
 require(Array.isArray(marks)&&marks.length===patch.marks.length,'incomplete marked vertices');
 const table=new Map();
 for(const mark of marks){require(mark&&typeof mark.label==='string'&&!table.has(mark.label),'duplicate or invalid mark');table.set(mark.label,mark);}
 for(const expected of patch.marks){const actual=table.get(expected.label);
  require(actual&&same(actual.source,expected.source)&&same(actual.point,expected.point),'mark differs from declared affine image');
 }
 return true;
}
export const macroKeys=p=>p.items.map(x=>x.key).sort();
export const primitiveKeys=p=>[...p.components.keys()].sort();
export function specification(owner){return {kind:owner.kind,origin:[...owner.origin],inverted:owner.inverted};}
