// Geometry-only adapter to prior source rules. No new particle/transport law.
import assert from 'node:assert/strict';
import {GenerativeAssemblyRules,LocalPrimitiveGeometry} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem,acrossFace,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {primitives} from '../demos/particle-overlap-tetrahedron/simplex-components.mjs';
const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]],permutations=[[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]],spatial=[[0,1,2,3],[0,2,1,3],[0,1,3,2]],point=p=>p.join(','),faceKey=f=>[...f].sort().join('|');
export class MissingDiagonal extends Error {constructor(key){super('Missing global diagonal: '+key);this.itemKey=key;}}
export class MixedGeometry extends LocalPrimitiveGeometry {
 constructor(){super();this.choices=new Map();this.defaultChoice=null;this.trace=new Map();this.octahedra=new Map();this.shapes=new Map();}
 setWorld(choices,defaultChoice=null){this.choices=new Map(choices);this.defaultChoice=defaultChoice;this.trace=new Map();}
 owner(item){
  if(item.kind!=='octahedron')return item;
  this.octahedra.set(item.key,{key:item.key,origin:[...item.origin]});
  const choice=this.choices.get(item.key)??this.defaultChoice;if(choice===null||choice===undefined)throw new MissingDiagonal(item.key);assert.ok([0,1,2].includes(choice));this.trace.set(item.key,choice);
  const k=item.key+'#'+choice;if(!this.shapes.has(k)){
   const components=permutations.map(p=>primitives.splitOctahedron.vertices.map(v=>item.origin.map((x,i)=>x+v[p[spatial[choice][i]]])));
   this.shapes.set(k,{...item,components,diagonal:choice});
  }return this.shapes.get(k);
 }
 neighbor(id,face){
  const cell=this.cells[id],fk=faceKey(face);if(!cell||!cell.faces.some(f=>faceKey(f)===fk))throw Error('Not a full primitive face');
  const matches=c=>faces.some(f=>faceKey(f.map(i=>point(c[i])))===fk);
  let owner=this.owner(cell.owner),candidates=owner.components.filter(c=>itemKey(c)!==cell.key&&matches(c));
  if(owner.kind==='octahedron'&&!owner.components.some(c=>itemKey(c)===cell.key))throw Error('Source cell conflicts with world diagonal');
  if(!candidates.length){
   if(!owner.faces.some(f=>faceKey(f.map(point))===fk))throw Error('Missing primitive neighbor');
   owner=this.owner(acrossFace(owner,face.map(p=>this.points.get(p))));candidates=owner.components.filter(matches);
  }
  if(candidates.length!==1)throw Error('Primitive face must have a unique neighbor');return this.register(owner,candidates[0]);
 }
}
export class MixedRules extends GenerativeAssemblyRules {
 constructor(){
  super();this.geometry=new MixedGeometry();this.charts=[];this.chartKeys=new Map();this.packets=[];this.packetKeys=new Map();this.operations=[];this.operationCache=new Map();this.chartRequirements=new Map();
  const seed=makeLatticeItem('tetrahedron',[0,0,0,0]);this.seedCell=this.geometry.register(seed,seed.components[0]);this.seedAliases=Object.fromEntries(['C0','M0','C1','M1'].map((k,i)=>[k,point(seed.vertices[i])]));
  const oct=acrossFace(seed,['M0','C1','M1'].map(k=>seed.vertices[['C0','M0','C1','M1'].indexOf(k)]));this.rootItem=oct.key;this.roots=[];
  for(let d=0;d<3;d++){this.geometry.setWorld([[oct.key,d]]);const c=this.completeP(this.seedCell,this.seedAliases);assert.notEqual(c,null);this.roots.push(this.packet(c,0,[0,1,2,3,4]));}this.root=this.roots[0];
 }
 chart(cell,species,aliases){
  const id=super.chart(cell,species,aliases);if(!this.chartRequirements)return id;
  const nVertices=['M0','C1','M1','C2'].map(k=>this.geometry.points.get(aliases[k]));
  const n=this.geometry.byKey.get(itemKey(nVertices));assert.notEqual(n,undefined,'Chart needs its actual reference N geometry');const owner=this.geometry.cells[n].owner;assert.equal(owner.kind,'octahedron');assert.ok([0,1,2].includes(owner.diagonal));
  const requirement=[[owner.key,owner.diagonal]];
  if(this.chartRequirements.has(id))assert.deepEqual(this.chartRequirements.get(id),requirement);else this.chartRequirements.set(id,requirement);return id;
 }
 requirements(id){return this.chartRequirements.get(this.packets[id].chart);}
 selectedWorld(ids,assignments=null){
  const world=new Map(assignments??[]);for(const id of ids)for(const [k,d] of this.requirements(id)){
   if(world.has(k)&&world.get(k)!==d)return null;world.set(k,d);
  }return world;
 }
 describe(ids){
  const world=this.selectedWorld(ids);if(world===null)return {valid:false,reason:'global-diagonal-conflict'};this.geometry.setWorld(world,0);return super.describe(ids);
 }
 inspectWorld(ids,world){
  assert.ok(this.selectedWorld(ids,world));this.geometry.setWorld(world,0);this.operationCache.clear();
  // describe() normally only needs selected-record geometry. Restore ALL
  // chosen lookahead diagonals before original inspect() generates operations.
  const description=super.describe(ids);assert.equal(description.valid,true);this.geometry.setWorld(world,0);return super.inspect(ids,description);
 }
}
export function mixedUniverse({maxOrigin,maxPackets=5000,maxEvaluations=100000,maxOperations=50000}={}){
 assert.ok(Number.isInteger(maxOrigin)&&maxOrigin>=0&&maxOrigin<=10);const rules=new MixedRules(),queue=[...rules.roots],seen=new Set(queue),operations=[],unique=new Set();let evaluations=0,complete=true,stop=null;
 outer:for(let cursor=0;cursor<queue.length;cursor++){
  const id=queue[cursor],pending=[new Map(rules.requirements(id))];
  while(pending.length){
   if(++evaluations>maxEvaluations){complete=false;stop='local-diagonal-evaluation-cap';break outer;}
   const choices=pending.pop();rules.geometry.setWorld(choices);rules.operationCache.delete(id);let outgoing;
   try{outgoing=rules.outgoing(id);}catch(e){
    if(!(e instanceof MissingDiagonal))throw e;
    for(let d=2;d>=0;d--)pending.push(new Map([...choices,[e.itemKey,d]]));continue;
   }
   for(const index of outgoing){
    const op=rules.operations[index];if(rules.packets[op.target].origin>maxOrigin)continue;
    const requirements=[...choices].sort(([a],[b])=>a.localeCompare(b));const key=JSON.stringify([op.source,op.target,op.kind,op.face,requirements]);if(unique.has(key))continue;unique.add(key);
    operations.push({...op,sourceOperation:index,requirements,id:operations.length});
    if(operations.length>maxOperations){complete=false;stop='conditional-operation-cap';break outer;}
    if(!seen.has(op.target)){if(queue.length>=maxPackets){complete=false;stop='packet-cap';break outer;}seen.add(op.target);queue.push(op.target);}
   }
  }
 }
 return {rules,maxOrigin,roots:rules.roots,packets:queue,operations,complete,stop,evaluations};
}
export function buildMixedInput(universe,target){
 const {rules,packets,operations}=universe,conflicts=[],chartPairValidity=new Map();
 // describe uses chart cells/aliases and diagonal requirements, not origins
 // or packet permutations. Repeated readers therefore share this exact guard.
 for(let a=0;a<packets.length;a++)for(let b=a+1;b<packets.length;b++){
  const ca=rules.packets[packets[a]].chart,cb=rules.packets[packets[b]].chart,key=ca<cb?ca+':'+cb:cb+':'+ca;
  if(!chartPairValidity.has(key))chartPairValidity.set(key,rules.describe([packets[a],packets[b]]).valid);
  if(!chartPairValidity.get(key))conflicts.push([packets[a],packets[b]]);
 }
 const bodies=[],which=new Map();for(const id of packets){const c=rules.charts[rules.packets[id].chart],k=c.cell+':'+c.species;if(!which.has(k)){which.set(k,bodies.length);bodies.push({cell:c.cell,species:c.species,packets:[]});}bodies[which.get(k)].packets.push(id);}
 const contacts=[];for(let a=0;a<bodies.length;a++)for(let b=a+1;b<bodies.length;b++){
  const u=bodies[a],v=bodies[b];if(u.cell===v.cell||rules.geometry.cells[u.cell].vertices.filter(p=>rules.geometry.cells[v.cell].vertices.includes(p)).length!==3)continue;
  const links=operations.filter(op=>u.packets.includes(op.source)&&v.packets.includes(op.target)||v.packets.includes(op.source)&&u.packets.includes(op.target)).map(op=>op.id);contacts.push({bodies:[a,b],links});
 }
 const requirements=Object.fromEntries(packets.map(p=>[p,rules.requirements(p)]));const items=new Set([...packets.flatMap(p=>rules.requirements(p).map(([k])=>k)),...operations.flatMap(o=>o.requirements.map(([k])=>k))]);
 return {maxOrigin:universe.maxOrigin,target,roots:universe.roots,packets,conflicts,operations,bodies,contacts,exits:packets.filter(p=>rules.charts[rules.packets[p].chart].species==='electron'),requirements,items:[...items].sort()};
}
