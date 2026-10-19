import assert from 'node:assert/strict';
import {phaseUniverse} from './origin-bounded-assemblies.mjs';
import {BooleanDiagram} from './origin-assembly-family.mjs';
export const MODE='experimental-terminal-PE';
const pair=(a,b)=>[a,b].sort((a,b)=>a-b).join(':');
export function validateContraction(g,pn,ne){
 assert.equal(pn.kind,'PN');assert.equal(ne.kind,'NE');assert.equal(pn.target,ne.source);
 g.validateTransfer(pn);g.validateTransfer(ne);
 const p=g.packets[pn.source],n=g.packets[pn.target],e=g.packets[ne.target],pc=g.charts[p.chart],nc=g.charts[n.chart],ec=g.charts[e.chart];
 assert.equal(pn.phaseDelta,0);assert.equal(ne.phaseDelta,0);assert.equal(p.origin,n.origin);assert.equal(n.origin,e.origin);
 assert.equal(new Set([pc.cell,nc.cell,ec.cell]).size,3);
 const edge=g.geometry.cells[pc.cell].vertices.filter(v=>g.geometry.cells[ec.cell].vertices.includes(v)).sort();
 assert.deepEqual(edge,[pc.aliases.C1,pc.aliases.M1].sort());assert.equal(g.outgoing(e.id).length,0);
 const permutation=ne.permutation.map(i=>pn.permutation[i]);assert.deepEqual(permutation,[3,4,2,0,1]);assert.deepEqual(permutation.map(i=>p.permutation[i]),e.permutation);
 return {kind:MODE,source:p.id,target:e.id,phaseDelta:0,permutation,edge,nativeFactors:[pn.id,ne.id],referenceNeutronPacket:n.id,referenceNeutronCell:nc.cell,occupiedSupport:[pc.cell,ec.cell],referenceSupport:[pc.cell,nc.cell,ec.cell],referenceCharts:[p.chart,n.chart,e.chart]};
}
export function contractionUniverse({maxOrigin,seedBindings=null}={}){
 const u=phaseUniverse({maxOrigin,seedBindings});assert.ok(u.complete);const allowed=new Set(u.operations),shortcuts=[];
 for(const id of u.operations){const pn=u.rules.operations[id];if(pn.kind!=='PN')continue;for(const j of u.rules.outgoing(pn.target)){const ne=u.rules.operations[j];if(allowed.has(j)&&ne.kind==='NE')shortcuts.push({...validateContraction(u.rules,pn,ne),id:shortcuts.length});}}
 return {...u,shortcuts,mode:MODE};
}
export function inspectContraction(u,ids,{mode=MODE}={}){
 assert.ok([MODE,'native'].includes(mode));const g=u.rules,selected=new Set(ids),allowed=new Set(u.packets);
 if(selected.size!==ids.length||ids.some(p=>!allowed.has(p))||!selected.has(g.root))return {valid:false,reason:'invalid-selected-packet-set'};
 const d=g.describe(ids);if(!d.valid)return d;
 const native=u.operations.map(i=>g.operations[i]).filter(o=>selected.has(o.source)&&selected.has(o.target));
 const shortcuts=mode==='native'?[]:u.shortcuts.filter(o=>selected.has(o.source)&&selected.has(o.target)&&!d.bodies.has(o.referenceNeutronCell)&&!native.some(n=>n.source===o.source));
 const edges=[...native,...shortcuts],rooted=new Set([g.root]),construction=[];
 for(let changed=true;changed;){changed=false;for(const o of edges)if(rooted.has(o.source)&&!rooted.has(o.target)){rooted.add(o.target);construction.push({kind:o.kind,id:o.id,source:o.source,target:o.target});changed=true;}}
 const exits=ids.filter(p=>g.charts[g.packets[p].chart].species==='electron'),canExit=new Set(exits);
 for(let changed=true;changed;){changed=false;for(const o of edges)if(canExit.has(o.target)&&!canExit.has(o.source)){canExit.add(o.source);changed=true;}}
 // Only actual native face transfers may witness occupied triangular faces.
 const witnessed=new Set(native.map(o=>pair(g.charts[g.packets[o.source].chart].cell,g.charts[g.packets[o.target].chart].cell))),missingContacts=d.contacts.filter(c=>!witnessed.has(pair(...c.cells)));
 const counts={proton:0,neutron:0,electron:0};for(const s of d.bodies.values())counts[s]++;
 const rootPass=rooted.size===ids.length,exitPass=canExit.size===ids.length&&exits.length>0;
 return {valid:true,mode,rooted:rootPass,counts,shortcuts,construction,unrooted:ids.filter(p=>!rooted.has(p)),noExit:ids.filter(p=>!canExit.has(p)),missingContacts,certifiedExit:rootPass&&exitPass&&!missingContacts.length,scope:'Local reference-only support contraction; no global field sewing or physical binding.'};
}
export function guardedFamily(u,{maxDiagramNodes=500000}={}){
 const g=u.rules,packets=u.packets,index=new Map(packets.map((p,i)=>[p,i])),b=new BooleanDiagram(packets.length,{maxNodes:maxDiagramNodes}),x=new Map(packets.map(p=>[p,b.variable(index.get(p))]));let compatible=x.get(g.root);
 for(let i=0;i<packets.length;i++)for(let j=i+1;j<packets.length;j++)if(!g.describe([packets[i],packets[j]]).valid)compatible=b.and(compatible,b.not(b.and(x.get(packets[i]),x.get(packets[j]))));
 const native=u.operations.map(i=>g.operations[i]),edge=native.map(o=>({source:o.source,target:o.target,condition:b.and(x.get(o.source),x.get(o.target))}));
 const body=cell=>b.or(...packets.filter(p=>g.charts[g.packets[p].chart].cell===cell).map(p=>x.get(p)));
 for(const o of u.shortcuts)edge.push({source:o.source,target:o.target,condition:b.and(x.get(o.source),x.get(o.target),b.not(body(o.referenceNeutronCell)),...native.filter(n=>n.source===o.source).map(n=>b.not(x.get(n.target))))});
 // Bounded Boolean reachability, not the old monotone SCC support shortcut.
 // Every simple path has at most |packets|-1 edges, even with zero-grade cycles.
 function reach(initial,reverse=false){let r=new Map(packets.map(p=>[p,initial(p)]));for(let k=1;k<packets.length;k++){const next=new Map(r);for(const o of edge){const a=reverse?o.target:o.source,c=reverse?o.source:o.target;next.set(c,b.or(next.get(c),b.and(r.get(a),o.condition)));}if(packets.every(p=>next.get(p)===r.get(p)))break;r=next;}return r;}
 const rootReach=reach(p=>p===g.root?x.get(p):0),exitReach=reach(p=>g.charts[g.packets[p].chart].species==='electron'?x.get(p):0,true);
 const valid=b.and(compatible,...packets.map(p=>b.implies(x.get(p),rootReach.get(p))));let exit=b.and(valid,...packets.map(p=>b.implies(x.get(p),exitReach.get(p))));
 const cells=[...new Set(packets.map(p=>g.charts[g.packets[p].chart].cell))];
 for(let i=0;i<cells.length;i++)for(let j=i+1;j<cells.length;j++){
 const a=cells[i],c=cells[j];if(g.geometry.cells[a].vertices.filter(v=>g.geometry.cells[c].vertices.includes(v)).length!==3)continue;
 const witnesses=native.filter(o=>pair(g.charts[g.packets[o.source].chart].cell,g.charts[g.packets[o.target].chart].cell)===pair(a,c));
 exit=b.and(exit,b.implies(b.and(body(a),body(c)),b.or(...witnesses.map(o=>b.and(x.get(o.source),x.get(o.target))))));
 }
 return {diagram:b,validRoot:valid,exitRoot:exit,accepts:(ids,certified=false)=>b.accepts(certified?exit:valid,ids.map(p=>index.get(p))),counts:{configurations:b.count(valid).toString(),exitCertificates:b.count(exit).toString()}};
}
export function enumerateContractions(u,{maxConfigurations=250000}={}){
 const nodes=[[u.rules.root]],seen=new Map([[String(u.rules.root),0]]),edges=[];
 const schemas=[...u.operations.map(i=>u.rules.operations[i]),...u.shortcuts];
 for(let i=0;i<nodes.length;i++)for(const op of schemas){
  if(!nodes[i].includes(op.source))continue;
  const ids=[...new Set([...nodes[i],op.target])].sort((a,b)=>a-b),a=inspectContraction(u,ids);
  if(!a.valid||!a.rooted||op.kind===MODE&&!a.shortcuts.some(s=>s.id===op.id))continue;
  const key=ids.join(',');let to=seen.get(key);
  if(to===undefined){if(nodes.length>=maxConfigurations)return {complete:false,reason:'configuration-resource-limit',nodes,edges};to=nodes.length;seen.set(key,to);nodes.push(ids);}
  edges.push({from:i,to,kind:op.kind,operation:op.id,source:op.source,target:op.target});
 }
 return {complete:true,nodes,edges};
}
