// Phase occurrences are NOT geometric vertex names or omega exponents.
// This conservative gate recognizes only the retained native P/N/E templates.
// Other interfaces need an explicit phase witness, not an invertible matrix.
import {windowProtocol} from './window-construction-model.mjs';
const specs=Object.fromEntries(windowProtocol.map(p=>[p.species,p]));
const parse=name=>{const m=/^([CM])(\d+)$/.exec(name);if(!m)throw Error('Invalid native phase occurrence');return {role:m[1],index:Number(m[2])};};
export function nativePhaseFrame(id,species,bindings){
 const spec=specs[species];if(!spec)throw Error('Unknown local carrier template');
 const occurrence=name=>({vertex:bindings[name],...parse(name)});
 return {id,species,window:spec.window.map(occurrence),context:occurrence(spec.continuation)};
}
export function auditPhaseFrame(frame){
 const spec=specs[frame.species],issues=[];if(!spec)return {status:'invalid',issues:['unknown-template']};
 const actual=[...(frame.window??[]),frame.context],expected=[...spec.window,spec.continuation].map(parse);
 if(actual.length!==4||actual.some(x=>!x||typeof x.vertex!=='string'||!x.vertex||!['C','M'].includes(x.role)||!Number.isSafeInteger(x.index)||x.index<0))return {status:'invalid',issues:['four-explicit-phase-occurrences-required']};
 if(new Set(actual.map(x=>x.vertex)).size!==4)issues.push('tetrahedron-needs-four-distinct-geometric-vertices');
 if(actual.some((x,i)=>x.role!==expected[i].role))issues.push('wrong-ordered-window-or-context-role');
 const offsets=actual.map((x,i)=>x.index-expected[i].index);
 if(new Set(offsets).size!==1)issues.push('local-phase-spacing-or-context-mismatch');
 return {status:issues.length?'invalid':'native-template-compatible',issues,origin:issues.length?null:offsets[0]};
}
export function auditNamedConstruction(snapshot){
 const frames=snapshot.items.map((body,i)=>({id:String(i),origin:0,species:body.species,window:body.window.map(name=>({vertex:JSON.stringify(snapshot.bindings[name]),...parse(name)})),context:{vertex:JSON.stringify(snapshot.bindings[body.continuation]),...parse(body.continuation)}}));
 const byKey=new Map(snapshot.items.map((body,i)=>[body.key,i]));
 const interfaces=(snapshot.tunnel.interfaces??[]).map(e=>{const a=byKey.get(e.from),b=byKey.get(e.to),source=snapshot.items[a],target=snapshot.items[b];return {from:String(a),to:String(b),kind:source.species==='proton'&&target.species==='neutron'?'PN':source.species==='neutron'&&target.species==='electron'?'NE':'unproved',identification:'same-occurrence',vertices:e.face.map(p=>JSON.stringify(p))};});
 return auditPhaseCombination(frames,interfaces);
}
export function auditPhaseSuccessor(from,to){
 if(from.role!==to.role||!Number.isSafeInteger(from.index)||!Number.isSafeInteger(to.index)||from.index<0||to.index<0)return {status:'invalid',reason:'explicit-same-channel-occurrences-required'};
 return to.index===from.index+1?{status:'consecutive'}:{status:'invalid',reason:'phase-skip-or-reversal',from:from.index,to:to.index};
}
export function auditPhaseCombination(frames,interfaces){
 if(!Array.isArray(frames)||!frames.length||!Array.isArray(interfaces))throw Error('Nonempty reader occurrence collection required');
 const ids=new Set(frames.map(f=>f.id));if(ids.size!==frames.length||frames.some(f=>typeof f.id!=='string'||!f.id))throw Error('Distinct reader occurrence IDs required');
 const byId=new Map(frames.map(f=>[f.id,f])),local=frames.map(f=>({id:f.id,...auditPhaseFrame(f)})),edges=[],issues=[];
 for(const f of local)if(f.status==='invalid')issues.push({kind:'local-frame',id:f.id,issues:f.issues});
 for(const link of interfaces){
  const a=byId.get(link.from),b=byId.get(link.to);if(!a||!b)throw Error('Unknown reader occurrence');
  const registered=(link.kind==='PN'&&a.species==='proton'&&b.species==='neutron')||(link.kind==='NE'&&a.species==='neutron'&&b.species==='electron');
  if(!registered)issues.push({kind:'missing-phase-transition-witness',from:a.id,to:b.id,transition:link.kind});
  // Only an explicitly identified SAME occurrence is constrained here.
  // A more general passage must supply its own phase witness; coincidence
  // of coordinates alone never manufactures such a witness.
  if(link.identification!=='same-occurrence'){issues.push({kind:'missing-occurrence-identification',from:a.id,to:b.id});continue;}
  const left=[...(a.window??[]),a.context],right=[...(b.window??[]),b.context],vertices=link.vertices??[];
  if(registered&&JSON.stringify([...vertices].sort())!==JSON.stringify((b.window??[]).map(o=>o.vertex).sort()))issues.push({kind:'target-window-is-not-interface',from:a.id,to:b.id});
  if(vertices.length!==3||new Set(vertices).size!==3){issues.push({kind:'full-face-identification-required',from:a.id,to:b.id});continue;}
  const demands=[];
  for(const vertex of vertices){
   const x=left.find(o=>o?.vertex===vertex),y=right.find(o=>o?.vertex===vertex);
   if(!x||!y||x.role!==y.role){issues.push({kind:'shared-occurrence-role-mismatch',from:a.id,to:b.id,vertex});continue;}
   demands.push({vertex,role:x.role,sourceIndex:x.index,targetIndex:y.index,requiredTargetOffset:x.index-y.index});
  }
  if(demands.length!==3)continue;
  if(new Set(demands.map(d=>d.requiredTargetOffset)).size!==1){issues.push({kind:'shared-face-phase-conflict',from:a.id,to:b.id,demands});continue;}
  edges.push({from:a.id,to:b.id,delta:demands[0].requiredTargetOffset});
 }
 // Solve one integer origin per reader occurrence. No mod-3 quotient, no
 // per-vertex offsets, and no resetting phase at a loop boundary.
 const connected=new Set([frames[0].id]),reach=[frames[0].id];
 for(let i=0;i<reach.length;i++)for(const link of interfaces){const next=link.from===reach[i]?link.to:link.to===reach[i]?link.from:null;if(next!==null&&!connected.has(next)){connected.add(next);reach.push(next);}}
 if(connected.size!==frames.length)issues.push({kind:'unconnected-combination'});
 const offsets=new Map();
 for(const f of frames)if(!offsets.has(f.id)){
  const component=[f.id],seen=new Set(component);
  for(let i=0;i<component.length;i++)for(const e of edges){const next=e.from===component[i]?e.to:e.to===component[i]?e.from:null;if(next!==null&&!seen.has(next)){seen.add(next);component.push(next);}}
  const root=component.map(id=>byId.get(id)).find(x=>x.origin!==undefined)??f;
  if(root.origin!==undefined&&!Number.isSafeInteger(root.origin))throw Error('Integer phase origin required');
  offsets.set(root.id,root.origin??0);const queue=[root.id];
  for(let i=0;i<queue.length;i++)for(const e of edges){
   const direction=e.from===queue[i]?1:e.to===queue[i]?-1:0;if(!direction)continue;
   const to=direction===1?e.to:e.from,value=offsets.get(queue[i])+direction*e.delta;
   if(byId.get(to).origin!==undefined&&byId.get(to).origin!==value)issues.push({kind:'declared-phase-origin-conflict',from:queue[i],to});
   if(offsets.has(to)){if(offsets.get(to)!==value)issues.push({kind:'combination-phase-cycle-conflict',from:queue[i],to});}
   else {offsets.set(to,value);queue.push(to);}
  }
 }
 return {status:issues.length?'not-phase-admitted':'native-phase-compatible',local,issues,relativeOrigins:Object.fromEntries(offsets),
  scope:'Necessary native-template and explicitly shared-occurrence checks, not a complete physical phase theory. P/N/E templates come from the retained source. Unknown NN or reader comparisons fail closed. Different occurrences at one geometric vertex require an explicit transition witness; no period or phase jump is invented.'};
}
