// Candidate composite carrier: one external port, all member coordinates retained.
// This is not an extra tetrahedron or a claim of new independent particle states.
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
export function buildCollectivePairCell(model){
 const members=model.geometry.filter(g=>g.polarityRoles.positive==='electron'&&g.polarityRoles.negative==='proton');
 if(!members.length)throw Error('No minority pair sector');
 const exposed=new Set(model.outer.flatMap(f=>f.owners)),ports=members.filter(g=>exposed.has(g.id));
 if(ports.length!==1)throw Error('Collective cell needs a unique existing outer port');
 const faces=new Map(),neighbors=new Map(model.geometry.map(g=>[g.id,new Set()]));
 for(const g of model.geometry)for(const f of g.faces){const k=key(f);if(!faces.has(k))faces.set(k,[]);faces.get(k).push(g.id);}
 for(const ids of faces.values())if(ids.length===2){neighbors.get(ids[0]).add(ids[1]);neighbors.get(ids[1]).add(ids[0]);}
 const links=new Map(),graph=new Map(members.map(g=>[g.id,new Set()]));
 for(const n of model.geometry.filter(g=>g.role==='neutron')){
  const touching=members.filter(g=>neighbors.get(n.id).has(g.id));
  for(let i=0;i<touching.length;i++)for(let j=i+1;j<touching.length;j++){
   const endpoints=[touching[i].id,touching[j].id].sort(),id=endpoints.join('|');
   if(!links.has(id))links.set(id,{endpoints,mediators:[]});links.get(id).mediators.push(n.id);
   graph.get(endpoints[0]).add(endpoints[1]);graph.get(endpoints[1]).add(endpoints[0]);
  }
 }
 const reached=new Set([ports[0].id]),queue=[ports[0].id];
 for(let i=0;i<queue.length;i++)for(const id of graph.get(queue[i]))if(!reached.has(id)){reached.add(id);queue.push(id);}
 if(reached.size!==members.length)throw Error('Minority sector is not connected through neutral interfaces');
 const n=members.length;
 return {id:'collective-PE',kind:'collective-comparison-cell',support:members.map(g=>g.id),port:ports[0].id,point:center(ports[0].vertices),
  polarityRoles:{positive:'electron',negative:'proton'},links:[...links.values()],
  projection:{numerator:members.map(()=>1),denominator:n,sourceCoordinates:members.map(g=>`${g.id}:amplitude`),coefficientFiber:5},
  retention:{anchor:members[0].id,contrasts:members.slice(1).map(g=>({plus:g.id,minus:members[0].id})),recoverable:true},
  witness:{connected:true,outerPorts:ports.length,memberCount:n,contrastCount:n-1},
  counts:effectiveCollectiveCounts(model.geometry,members.map(g=>g.id)),
  physicalCellAdded:false,independentPolarityParticles:false,nativeParticleRealization:false,
  assumption:'Treat the connected minority sector as one external comparison carrier; retain its internal members and contrast coordinates. No equality of unknown amplitudes or new physical tetrahedron is asserted.'};
}
export function encodeCollective(values){
 if(!Array.isArray(values)||!values.length||values.some(x=>!Number.isFinite(x)))throw Error('Finite retained member values required');
 return {sum:values.reduce((s,x)=>s+x,0),contrasts:values.slice(1).map(x=>x-values[0]),members:values.length};
}
export function decodeCollective({sum,contrasts,members}){
 if(!Number.isInteger(members)||members<1||contrasts.length!==members-1||![sum,...contrasts].every(Number.isFinite))throw Error('Complete collective/contrast record required');
 const anchor=(sum-contrasts.reduce((s,x)=>s+x,0))/members;return [anchor,...contrasts.map(x=>anchor+x)];
}
function effectiveCollectiveCounts(geometry,support){
 const set=new Set(support),counts={};
 for(const sheet of ['positive','negative']){
  const c={proton:0,neutron:0,electron:0,total:0};
  for(const g of geometry)if(!set.has(g.id)){c[g.polarityRoles[sheet]]++;c.total++;}
  c[sheet==='positive'?'electron':'proton']++;c.total++;counts[sheet]=c;
 }
 return {...counts,chargedReadings:{proton:counts.positive.proton+counts.negative.proton,electron:counts.positive.electron+counts.negative.electron},
  sharedCarrierCount:counts.positive.total,scope:'External comparison readings. The polarity rows share carriers; charged readings are not independent particles. Physical members are retained.'};
}
