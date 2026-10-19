import {lattice,faces} from './simplex-model.mjs';
export {lattice};
export const identity=Object.freeze({id:'id',source:'inner realization',target:'next realization'});
export const items=lattice.assembly.items.map((item,index)=>{
 const nodeIds=[...new Set(item.children.flatMap(id=>lattice.cells[id]))];
 return {...item,index,nodeIds,center:nodeIds.reduce((s,id)=>s.map((x,i)=>x+lattice.nodes[id].point[i]/nodeIds.length),[0,0,0]),frame:item.layer%2};
});
// Local frame parity is a chart convention, not a fixed physical C/M typing.
// Transport is the change of frame; a closed walk preserves the identity.
const owner=new Map(items.flatMap(i=>i.children.map(c=>[c,i.index]))),faceTable=new Map();
for(const [id,cell] of lattice.cells.entries())for(const face of faces){
 const nodes=face.map(i=>cell[i]).sort((a,b)=>a-b),key=nodes.join(',');
 if(!faceTable.has(key))faceTable.set(key,{nodes,owners:[]});faceTable.get(key).owners.push(owner.get(id));
}
const edgeTable=new Map();
for(const f of faceTable.values())if(f.owners.length===2&&f.owners[0]!==f.owners[1]){
 const [a,b]=[...f.owners].sort((a,b)=>a-b),key=a+','+b;
 if(!edgeTable.has(key))edgeTable.set(key,{a,b,faces:[],transition:items[a].frame^items[b].frame});edgeTable.get(key).faces.push(f.nodes);
}
export const connections=[...edgeTable.values()];
export const adjacency=items.map(()=>[]);
for(const {a,b} of connections){adjacency[a].push(b);adjacency[b].push(a);}
adjacency.forEach(a=>a.sort((a,b)=>a-b));
export function pathBetween(start,end){
 if(!items[start]||!items[end])throw RangeError('Unknown item');
 const parent=new Map([[start,null]]),q=[start];
 for(let i=0;i<q.length&&!parent.has(end);i++)for(const next of adjacency[q[i]])if(!parent.has(next)){parent.set(next,q[i]);q.push(next);}
 if(!parent.has(end))throw Error('Disconnected space');
 const path=[];for(let at=end;at!==null;at=parent.get(at))path.push(at);return path.reverse();
}
export function transport(path,perspective=0){
 if(!path.length||![0,1].includes(perspective)||path.some(i=>!items[i]))throw RangeError('Invalid fiber path');
 let local=items[path[0]].frame^perspective;
 for(let i=1;i<path.length;i++){
  if(!adjacency[path[i-1]].includes(path[i]))throw Error('Transport requires a shared-face connection');
  local^=items[path[i-1]].frame^items[path[i]].frame;
 }
 return {identity,local,canonical:local^items[path.at(-1)].frame^perspective};
}
const seen=new Set([0]);export const traversal=[0];
function visit(at){for(const next of adjacency[at])if(!seen.has(next)){seen.add(next);traversal.push(next);visit(next);traversal.push(at);}}
visit(0);
if(seen.size!==items.length)throw Error('Traversal does not cover space');
const inner=items.filter(i=>i.layer===2),outer=items.filter(i=>i.layer===3);
const neighborList=new Map(inner.map(i=>[i.index,adjacency[i.index].filter(j=>items[j].layer===3)]));
const matched=new Map();
function augment(a,visited){for(const b of neighborList.get(a)){if(visited.has(b))continue;visited.add(b);if(!matched.has(b)||augment(matched.get(b),visited)){matched.set(b,a);return true;}}return false;}
for(const a of inner)augment(a.index,new Set());
if(matched.size!==44)throw Error('Full witness loadout unavailable');
export const witnessPairs=[...matched].map(([outer,inner])=>({inner,outer})).sort((a,b)=>a.inner-b.inner);
export const reserved=new Set(witnessPairs.map(p=>p.outer));
export const available=new Set(outer.filter(i=>!reserved.has(i.index)).map(i=>i.index));
export const loadout=Object.freeze({outer:outer.length,witnesses:reserved.size,available:available.size,electrons:null});
export const itemByCell=owner;
