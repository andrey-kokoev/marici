// Explicit incidence audit, separate from inventory checks and SVG geometry.
// No inverse arrows, vertex identifications, or NNPE/NNNN interpretation is inferred.
export function auditPathReversal(topology) {
 const scope='Declared NNPE/NNNN edge paths only; not a physical claim, native execution proof, or inference from SVG crossings.';
 const report={status:'unknown',scope,issues:[],paths:[],coverage:{NNPE:0,NNNN:0}};
 if(topology==null){report.issues.push({code:'missing-path-topology'});return report;}
 const fail=(code,detail)=>report.issues.push({code,...detail});
 const index=(rows,name)=>{
  const map=new Map();
  if(!Array.isArray(rows)){fail('invalid-collection',{collection:name});return map;}
  for(const row of rows){if(!row||typeof row.id!=='string'||!row.id||map.has(row.id)){fail('invalid-or-duplicate-id',{collection:name,id:row?.id});continue;}map.set(row.id,row);}
  return map;
 };
 const vertices=index(topology.vertices,'vertices'),edges=index(topology.edges,'edges'),paths=index(topology.paths,'paths');
 for(const v of vertices.values())if(!['N','P','E'].includes(v.role))fail('invalid-vertex-role',{id:v.id});
 for(const e of edges.values()){
  if(!vertices.has(e.from)||!vertices.has(e.to))fail('unbound-edge-endpoint',{id:e.id});
  if(typeof e.kind!=='string'||!e.kind||typeof e.support!=='string'||!e.support)fail('missing-edge-role-or-support',{id:e.id});
 }
 // Optional turn restrictions distinguish admissibility from mere connectivity.
 let turns=null;
 if(topology.turns!==undefined){
  turns=new Set();
  if(!Array.isArray(topology.turns))fail('invalid-turns',{});
  else for(const t of topology.turns){if(!Array.isArray(t)||t.length!==2||!edges.has(t[0])||!edges.has(t[1]))fail('invalid-turn',{turn:t});else turns.add(JSON.stringify(t));}
 }
 for(const p of paths.values()){
  const result={id:p.id,generator:p.generator,status:'refuted',issues:[]};report.paths.push(result);
  const issue=(code,detail={})=>result.issues.push({code,...detail});
  if(!['NNPE','NNNN'].includes(p.generator)){issue('unsupported-generator');continue;}
  report.coverage[p.generator]++;
  if(!Array.isArray(p.edges)||!p.edges.length){issue('missing-path-edges');continue;}
  const walk=ids=>{
   const rows=ids.map(id=>edges.get(id));
   if(rows.some(e=>!e)){issue('missing-edge');return null;}
   for(let i=1;i<rows.length;i++){
    if(rows[i-1].to!==rows[i].from)issue('noncomposable-path',{at:i});
    if(turns&&!turns.has(JSON.stringify([ids[i-1],ids[i]])))issue('forbidden-turn',{at:i});
   }
   return rows;
  };
  const forward=walk(p.edges);if(!forward)continue;
  for(const e of forward){
   const r=edges.get(e.reverse);
   if(!r){issue('missing-explicit-reverse',{edge:e.id});continue;}
   if(r.from!==e.to||r.to!==e.from)issue('reverse-incidence-mismatch',{edge:e.id});
   if(r.kind!==e.kind||r.support!==e.support)issue('reverse-role-or-support-mismatch',{edge:e.id});
   if(r.reverse!==e.id)issue('reverse-not-involutive',{edge:e.id});
  }
  const reverseIds=[...forward].reverse().map(e=>e.reverse);
  if(reverseIds.every(id=>edges.has(id))){
   const reverse=walk(reverseIds);
   result.forwardVertices=[forward[0].from,...forward.map(e=>e.to)];
   result.reverseVertices=[reverse[0].from,...reverse.map(e=>e.to)];
   if(JSON.stringify(result.reverseVertices)!==JSON.stringify([...result.forwardVertices].reverse()))issue('reverse-vertex-sequence-mismatch');
   result.reverseEdges=reverseIds;
  }
  if(!result.issues.length)result.status='verified';
 }
 if(report.issues.length||report.paths.some(p=>p.status==='refuted'))report.status='refuted';
 else if(!report.coverage.NNPE||!report.coverage.NNNN){report.issues.push({code:'incomplete-generator-coverage'});}
 else report.status='verified';
 return report;
}

export function auditDefinitionPathReversal(definition){
 return {definitionId:definition?.id??null,...auditPathReversal(definition?.pathTopology)};
}
