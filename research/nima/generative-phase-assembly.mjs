// Seed-driven construction. No isotope layouts, target compositions or finite ambient cell list.
import {makeLatticeItem,acrossFace,itemKey} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {windowProtocol} from '../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {phaseFrame,phaseAdvanceWitness,applyPhasePermutation} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseCombination} from '../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';

const FACES=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]],ID=[0,1,2,3,4],PN=[3,1,2,0,4],NE=[0,4,2,3,1];
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),pointKey=p=>p.join(','),faceKey=f=>[...f].sort().join('|');
const pairKey=(a,b)=>a<b?a+':'+b:b+':'+a;
const sorted=xs=>[...xs].sort((a,b)=>a-b);

export class LocalPrimitiveGeometry {
 constructor(){this.cells=[];this.byKey=new Map();this.points=new Map();this.neighborCache=new Map();}
 register(owner,component){
  const key=itemKey(component);if(this.byKey.has(key))return this.byKey.get(key);
  const id=this.cells.length,vertices=component.map(p=>{this.points.set(pointKey(p),[...p]);return pointKey(p);});
  this.cells.push({id,key,owner,vertices,faces:FACES.map(f=>f.map(i=>vertices[i])),geometry:owner.kind==='tetrahedron'?'proton':'split'});
  this.byKey.set(key,id);return id;
 }
 neighbor(id,face){
  const cell=this.cells[id],fk=faceKey(face),cache=id+'#'+fk;
  if(!cell||!cell.faces.some(f=>faceKey(f)===fk))throw Error('Not a full primitive face');
  if(this.neighborCache.has(cache))return this.neighborCache.get(cache);
  const matches=c=>FACES.some(f=>faceKey(f.map(i=>pointKey(c[i])))===fk);
  let owner=cell.owner,candidates=owner.components.filter(c=>itemKey(c)!==cell.key&&matches(c));
  if(!candidates.length){
   if(!owner.faces.some(f=>faceKey(f.map(pointKey))===fk))throw Error('Missing primitive neighbor');
   owner=acrossFace(owner,face.map(k=>this.points.get(k)));candidates=owner.components.filter(matches);
  }
  if(candidates.length!==1)throw Error('Primitive face does not have a unique neighbor');
  const result=this.register(owner,candidates[0]);
  this.neighborCache.set(cache,result);this.neighborCache.set(result+'#'+fk,id);return result;
 }
 apex(id,face){const a=this.cells[id].vertices.filter(v=>!face.includes(v));if(a.length!==1)throw Error('Not a tetrahedral attachment');return a[0];}
}

export class GenerativeAssemblyRules {
 constructor({seedBindings=null}={}){
  this.geometry=new LocalPrimitiveGeometry();this.charts=[];this.chartKeys=new Map();this.packets=[];this.packetKeys=new Map();this.operations=[];this.operationCache=new Map();
  const owner=makeLatticeItem('tetrahedron',[0,0,0,0]),cell=this.geometry.register(owner,owner.components[0]);
  const aliases=seedBindings??Object.fromEntries(windowProtocol[0].nodes.map((n,i)=>[n,pointKey(owner.vertices[i])]));
  if(Object.keys(aliases).length!==4||!same(Object.values(aliases).sort(),[...this.geometry.cells[cell].vertices].sort()))throw Error('Seed must bijectively mark C0,M0,C1,M1');
  const chart=this.completeP(cell,aliases);if(chart===null)throw Error('Seed has no native PN reference');
  this.root=this.packet(chart,0,ID);
 }
 chart(cell,species,aliases){
  const names=species==='electron'?['C0','M0','C1','M1','C2','M2']:['C0','M0','C1','M1','C2'];
  const a=Object.fromEntries(names.map(n=>[n,aliases[n]]));
  if(Object.values(a).some(v=>typeof v!=='string'||!this.geometry.points.has(v))||new Set(Object.values(a)).size!==names.length)throw Error('Distinct complete geometric reference marks required');
  const spec=windowProtocol.find(p=>p.species===species);
  if(!same(spec.nodes.map(n=>a[n]).sort(),[...this.geometry.cells[cell].vertices].sort()))throw Error('Chart does not bind its actual primitive');
  const geometry=this.geometry.cells[cell].geometry;
  if(species==='proton'&&geometry!=='proton'||species==='neutron'&&geometry!=='split')throw Error('Wrong native P/N reference geometry');
  const key=cell+':'+species+':'+names.map(n=>a[n]).join(';');
  if(this.chartKeys.has(key))return this.chartKeys.get(key);
  const id=this.charts.length;this.charts.push({id:'chart-'+id,cell,species,aliases:a});this.chartKeys.set(key,id);return id;
 }
 completeP(cell,a){
  const face=[a.M0,a.C1,a.M1],next=this.geometry.neighbor(cell,face);
  if(this.geometry.cells[next].geometry!=='split')return null;
  return this.chart(cell,'proton',{C0:a.C0,M0:a.M0,C1:a.C1,M1:a.M1,C2:this.geometry.apex(next,face)});
 }
 completeN(cell,a){
  const face=[a.M0,a.C1,a.M1],reference=this.geometry.neighbor(cell,face);
  if(this.geometry.cells[reference].geometry!=='proton')return null;
  return this.chart(cell,'neutron',{C0:this.geometry.apex(reference,face),M0:a.M0,C1:a.C1,M1:a.M1,C2:a.C2});
 }
 packet(chart,origin,permutation){
  if(!Number.isSafeInteger(origin)||origin<0||!same([...permutation].sort(),ID))throw Error('Invalid full reference packet');
  const key=chart+'@'+origin+':'+permutation.join('');if(this.packetKeys.has(key))return this.packetKeys.get(key);
  const id=this.packets.length;this.packets.push({id,chart,origin,permutation:[...permutation]});this.packetKeys.set(key,id);return id;
 }
 validateTransfer(op,source=this.packets[op.source],target=this.packets[op.target]){
  const a=this.charts[source.chart],b=this.charts[target.chart],delta=['reader-phase-advance','NN-phase-advance'].includes(op.kind)?1:0;
  if(op.phaseDelta!==delta||target.origin!==source.origin+delta)throw Error('Incorrect realization increment');
  let permutation;
  if(delta){
   if((op.kind==='reader-phase-advance')!==(a.cell===b.cell))throw Error('Wrong realization attachment kind');
   permutation=phaseAdvanceWitness(a,b,source.origin).permutation;
  }else{
   const inverse=op.kind==='inverse-PN';
   if(!['PN','inverse-PN','NE'].includes(op.kind))throw Error('Unknown native transfer');
   if(op.kind==='PN'&&(a.species!=='proton'||b.species!=='neutron')||inverse&&(a.species!=='neutron'||b.species!=='proton')||op.kind==='NE'&&(a.species!=='neutron'||b.species!=='electron'))throw Error('Wrong source/target carrier types');
   for(const n of ['C0','M0','C1','M1','C2'])if(a.aliases[n]!==b.aliases[n])throw Error('Native reference mark changed');
   const from=phaseFrame(inverse?b:a,source.origin),to=phaseFrame(inverse?a:b,source.origin);
   if(auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind:inverse?'PN':op.kind,identification:'same-occurrence',vertices:to.window.map(o=>o.vertex)}]).status!=='native-phase-compatible')throw Error('Unwitnessed native occurrence identification');
   permutation=op.kind==='NE'?NE:PN;
  }
  if(!same(op.permutation,permutation)||!same(target.permutation,permutation.map(i=>source.permutation[i])))throw Error('Lost a full coefficient coordinate');
  if(a.cell!==b.cell){
   const common=this.geometry.cells[a.cell].vertices.filter(v=>this.geometry.cells[b.cell].vertices.includes(v));
   if(common.length!==3||faceKey(common)!==faceKey(op.face)||this.geometry.neighbor(a.cell,op.face)!==b.cell)throw Error('Transfer is not across its actual shared face');
  }else if(op.face!==null)throw Error('A reader advance does not add a geometric interface');
  return true;
 }
 outgoing(id){
  if(this.operationCache.has(id))return this.operationCache.get(id);
  const source=this.packets[id],c=this.charts[source.chart],a=c.aliases,result=[];
  const add=(chart,kind,face=null)=>{
   if(chart===null)return;const delta=['reader-phase-advance','NN-phase-advance'].includes(kind)?1:0;
   const p=delta?phaseAdvanceWitness(c,this.charts[chart],source.origin).permutation:kind==='NE'?NE:PN;
   const target=this.packet(chart,source.origin+delta,p.map(i=>source.permutation[i]));
   const op={id:this.operations.length,source:id,target,kind,phaseDelta:delta,permutation:[...p],face:face?[...face]:null};
   this.validateTransfer(op);this.operations.push(op);result.push(op.id);
  };
  if(c.species==='proton'){
   const face=[a.M0,a.C1,a.M1],n=this.geometry.neighbor(c.cell,face);
   if(this.geometry.cells[n].geometry==='split')add(this.completeN(n,a),'PN',face);
   add(this.completeP(c.cell,{C0:a.C1,M0:a.M1,C1:a.C0,M1:a.M0}),'reader-phase-advance');
  }else if(c.species==='neutron'){
   const incoming=[a.M0,a.C1,a.M1],p=this.geometry.neighbor(c.cell,incoming);
   if(this.geometry.cells[p].geometry==='proton')add(this.completeP(p,a),'inverse-PN',incoming);
   const face=[a.M1,a.C1,a.C2],n=this.geometry.neighbor(c.cell,face);
   const apex=this.geometry.apex(n,face);
   // The common NE protocol does not select a split versus regular E target.
   if(!Object.values(a).includes(apex))add(this.chart(n,'electron',{...a,M2:apex}),'NE',face);
   if(this.geometry.cells[n].geometry==='split')add(this.completeN(n,{M0:a.M1,C1:a.C2,M1:apex,C2:a.C1}),'NN-phase-advance',face);
   add(this.completeN(c.cell,{M0:a.M1,C1:a.C2,M1:a.M0,C2:a.C1}),'reader-phase-advance');
  }
  this.operationCache.set(id,result);return result;
 }
 describe(packetIds){
  const bodies=new Map(),roles=new Map();
  for(const id of packetIds){
   const p=this.packets[id],c=this.charts[p.chart];
   if(bodies.has(c.cell)&&bodies.get(c.cell)!==c.species)return {valid:false,reason:'occupied-cell-species-conflict'};
   bodies.set(c.cell,c.species);
   for(const [mark,v] of Object.entries(c.aliases)){
    if(roles.has(v)&&roles.get(v)!==mark[0])return {valid:false,reason:'global-CM-role-conflict'};
    roles.set(v,mark[0]);
   }
  }
  const contacts=[];
  for(const [cell,species] of bodies)for(const face of this.geometry.cells[cell].faces){
   const neighbor=this.geometry.neighbor(cell,face);if(neighbor<=cell||!bodies.has(neighbor))continue;
   const other=bodies.get(neighbor),pair=[species,other];
   if(species===other&&species!=='neutron'||pair.includes('proton')&&pair.includes('electron'))return {valid:false,reason:'forbidden-face-contact'};
   const kind=pair.includes('electron')?'NE':species===other?'NN':'PN',count=face.filter(v=>roles.get(v)==='M').length;
   if(count!==(kind==='PN'?2:1))return {valid:false,reason:'shared-face-CM-conflict'};
   contacts.push({cells:[cell,neighbor],face:[...face],kind,key:pairKey(cell,neighbor)});
  }
  return {valid:true,bodies,roles,contacts};
 }
 inspect(packetIds,description=null){
  const d=description??this.describe(packetIds);if(!d.valid)return d;
  const selected=new Set(packetIds),reverse=new Map(packetIds.map(id=>[id,[]])),witnessed=new Set(),links=[];
  for(const id of packetIds)for(const index of this.outgoing(id)){
   const op=this.operations[index];if(!selected.has(op.target))continue;
   reverse.get(op.target).push(id);links.push(index);
   const a=this.charts[this.packets[id].chart].cell,b=this.charts[this.packets[op.target].chart].cell;
   if(a!==b)witnessed.add(pairKey(a,b));
  }
  const exits=packetIds.filter(id=>this.charts[this.packets[id].chart].species==='electron'),canExit=new Set(exits),queue=[...exits];
  for(let i=0;i<queue.length;i++)for(const from of reverse.get(queue[i]))if(!canExit.has(from)){canExit.add(from);queue.push(from);}
  const coveredCells=new Set([...canExit].map(id=>this.charts[this.packets[id].chart].cell));
  const missingContacts=d.contacts.filter(c=>!witnessed.has(c.key));
  const counts={proton:0,neutron:0,electron:0};for(const s of d.bodies.values())counts[s]++;
  return {valid:true,counts,cells:sorted(d.bodies.keys()),exitPackets:exits,links,
   pendingContacts:missingContacts,allContactsWitnessed:missingContacts.length===0,
   allCellsOnEntryExitPaths:coveredCells.size===d.bodies.size,allPacketsCanReachExit:canExit.size===packetIds.length,
   certifiedExit:exits.length>0&&missingContacts.length===0&&canExit.size===packetIds.length};
 }
}

export function enumerateAssemblies({maxTransitions=9,maxStates=250000,seedBindings=null,inspect=true,onLayer=null}={}){
 if(!Number.isInteger(maxTransitions)||maxTransitions<0||maxTransitions>12)throw Error('Bound must be an integer in [0,12]');
 if(!Number.isSafeInteger(maxStates)||maxStates<1)throw Error('Positive configuration resource bound required');
 const rules=new GenerativeAssemblyRules({seedBindings}),nodes=[{id:0,minTransitions:0,packets:[rules.root],parent:null,operation:null}],byKey=new Map([[String(rules.root),0]]),edges=[];
 const rejections={},layers=[1];let complete=true,stop=null;
 for(let cursor=0;cursor<nodes.length;cursor++){
  const node=nodes[cursor];if(node.minTransitions===maxTransitions)continue;
  const selected=new Set(node.packets);
  candidateOperations: for(const id of node.packets)for(const index of rules.outgoing(id)){
   const op=rules.operations[index];
   if(selected.has(op.target)){edges.push({from:node.id,to:node.id,operation:index});continue;}
   const ids=sorted([...node.packets,op.target]),key=ids.join(',');let next=byKey.get(key);
   if(next===undefined){
    const d=rules.describe(ids);
    if(!d.valid){rejections[d.reason]=(rejections[d.reason]??0)+1;continue;}
    if(nodes.length===maxStates){complete=false;stop={reason:'explicit-state-resource-limit',cursor,maxStates};break candidateOperations;}
    next=nodes.length;byKey.set(key,next);nodes.push({id:next,minTransitions:node.minTransitions+1,packets:ids,parent:node.id,operation:index});
    layers[node.minTransitions+1]=(layers[node.minTransitions+1]??0)+1;
   }
   edges.push({from:node.id,to:next,operation:index});
  }
  if(!complete)break;
  if(onLayer&&(cursor+1===nodes.length||nodes[cursor+1].minTransitions!==node.minTransitions))onLayer({expandedThrough:node.minTransitions,nodes:nodes.length,layers:[...layers]});
 }
 const profiles={},shapes=new Map();let certified=0,withExits=0,maxCarriers=0;
 if(inspect)for(const node of nodes){
  const result=rules.inspect(node.packets);if(!result.valid)throw Error('Enumerator retained an incompatible configuration');
  node.inspection=result;const n=result.counts.proton+result.counts.neutron+result.counts.electron;maxCarriers=Math.max(maxCarriers,n);
  if(result.exitPackets.length)withExits++;if(result.certifiedExit)certified++;
  const profile=[result.counts.proton,result.counts.neutron,result.counts.electron].join('/');
  profiles[profile]??={counts:result.counts,realizations:0,certifiedRealizations:0,minTransitions:node.minTransitions,sample:node.id};
  profiles[profile].realizations++;if(result.certifiedExit)profiles[profile].certifiedRealizations++;
  const d=rules.describe(node.packets),occupiedVertices=new Set([...d.bodies.keys()].flatMap(id=>rules.geometry.cells[id].vertices));
  const shapeKey=[...d.bodies].sort(([a],[b])=>a-b).map(([a,b])=>a+':'+b).join(',')+'|'+[...d.roles].filter(([v])=>occupiedVertices.has(v)).sort(([a],[b])=>a.localeCompare(b)).map(([a,b])=>a+':'+b).join(';');
  if(!shapes.has(shapeKey))shapes.set(shapeKey,{id:shapes.size,nodes:[],counts:result.counts});shapes.get(shapeKey).nodes.push(node.id);node.shape=shapes.get(shapeKey).id;
 }
 return {schema:'marici.nima.seed-generated-assemblies.v1',complete,stop,
  contract:{maxSourceTransitions:maxTransitions,oneOperationAddsAtMostOneBody:true,seed:'fixed ordered C0/M0/C1/M1 on the origin regular primitive',
   boundaries:'Marked entry C0 on the root P window; marked C-exit C_(origin+2) on every terminal E window. Boundary convention, not a derived physical interface.',
   ruleKinds:['PN','inverse-PN','NE','reader-phase-advance','NN-phase-advance'],
   targetCompositionFilters:false,presetAssemblyGraphs:false,ambient:'locally generated unbounded tetrahedral/octahedral honeycomb with retained subdivision',
   semantics:'Available packets are retained construction maps from five root coefficients, not simultaneous copies of a physical quantum state. A repeated operation is retained as a labelled self-loop; every operation occurrence costs one stage. Histories are paths in the configuration graph, not identified by node reuse.'},
  summary:{configurations:nodes.length,transitions:edges.length,minimalStageCounts:layers,withExits,certifiedExitConfigurations:certified,
   distinctGeometryRoleAssemblies:shapes.size,compositionProfiles:Object.keys(profiles).length,maxCarriers,rejections},
  profiles:Object.values(profiles).sort((a,b)=>a.minTransitions-b.minTransitions||a.counts.proton-b.counts.proton||a.counts.neutron-b.counts.neutron||a.counts.electron-b.counts.electron),
  shapes:[...shapes.values()],nodes,edges,cells:rules.geometry.cells.map(({owner,...c})=>({...c,owner:{kind:owner.kind,origin:owner.origin,inverted:owner.inverted}})),
  points:Object.fromEntries(rules.geometry.points),charts:rules.charts,packets:rules.packets,operations:rules.operations,rules};
}
export {applyPhasePermutation,phaseFrame};
