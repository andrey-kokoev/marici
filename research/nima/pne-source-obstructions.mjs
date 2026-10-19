// Sound over-approximation of possible certified supersets of mandatory packets.
// No atlas membership, target list or family model is consulted here.
export function deriveObstruction(u,core,{forbidden=[]}={}){
 const g=u.rules,mandatory=[...new Set([g.root,...core])].sort((a,b)=>a-b),must=new Set(mandatory),chart=p=>g.charts[g.packets[p].chart],cell=p=>chart(p).cell;
 if(mandatory.some(p=>forbidden.includes(p)))return {status:'obstructed',mandatory,reason:'mandatory-forbidden-clash',rounds:[]};
 const base=g.describe(mandatory);if(!base.valid)return {status:'obstructed',mandatory,reason:'mandatory-incompatibility',detail:base.reason,rounds:[]};
 const operations=u.operations.map(i=>g.operations[i]),schemas=[...operations,...u.shortcuts],available=new Set(),excluded=[];
 for(const p of u.packets){if(forbidden.includes(p)){excluded.push({packet:p,reason:'branch-assumed-absent'});continue;}const d=g.describe([...new Set([...mandatory,p])]);if(d.valid)available.add(p);else excluded.push({packet:p,reason:d.reason});}
 const rounds=[];
 function possible(o,required=mandatory){
  if(!available.has(o.source)||!available.has(o.target))return false;
  const ids=[...new Set([...required,o.source,o.target])],desc=g.describe(ids);if(!desc.valid)return false;
  if(o.kind==='experimental-terminal-PE'){
   if(desc.bodies.has(o.referenceNeutronCell))return false;
   if(operations.some(n=>n.source===o.source&&ids.includes(n.target)))return false;
  }
  return true;
 }
 for(let iteration=0;iteration<=u.packets.length;iteration++){
  const edges=schemas.filter(o=>possible(o)),rooted=new Set(available.has(g.root)?[g.root]:[]),exits=new Set([...available].filter(p=>chart(p).species==='electron'));
  for(let changed=true;changed;){changed=false;for(const o of edges){if(rooted.has(o.source)&&!rooted.has(o.target)){rooted.add(o.target);changed=true;}if(exits.has(o.target)&&!exits.has(o.source)){exits.add(o.source);changed=true;}}}
  const removed=[];
  for(const p of available){
   const reasons=[];if(!rooted.has(p))reasons.push({kind:'no-optimistic-root-path'});if(!exits.has(p))reasons.push({kind:'no-optimistic-exit-path'});
   const required=[...new Set([...mandatory,p])],desc=g.describe(required);
   for(const contact of desc.contacts){
    const witnesses=operations.filter(o=>contact.cells.includes(cell(o.source))&&contact.cells.includes(cell(o.target))&&cell(o.source)!==cell(o.target));
    if(!witnesses.some(o=>possible(o,required)))reasons.push({kind:'mandatory-face-without-possible-native-witness',cells:contact.cells,contactKind:contact.kind,candidateFactors:witnesses.map(o=>o.id)});
   }
   if(reasons.length)removed.push({packet:p,reasons});
  }
  rounds.push({iteration,available:[...available],possibleEdges:edges.map(o=>({kind:o.kind,id:o.id,source:o.source,target:o.target})),removed});
  const impossible=removed.filter(r=>must.has(r.packet));if(impossible.length)return {status:'obstructed',mandatory,reason:'mandatory-packet-eliminated',excluded,rounds,impossible};
  if(!removed.length)return {status:'relaxation-survives',mandatory,excluded,rounds,survivors:[...available]};
  for(const r of removed)available.delete(r.packet);
 }
 throw Error('Elimination did not terminate');
}
