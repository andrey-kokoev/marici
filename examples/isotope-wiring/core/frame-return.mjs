// Current diagram contract: a PE is ONE distinguished vertex; a path carries
// explicit SO(3) transports. SVG angles do not supply those transports.
const I=[[1,0,0],[0,1,0],[0,0,1]];
const transpose=a=>a[0].map((_,i)=>a.map(row=>row[i]));
const multiply=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((s,x,k)=>s+x*b[k][j],0)));
const error=(a,b)=>Math.max(...a.flatMap((row,i)=>row.map((x,j)=>Math.abs(x-b[i][j]))));
const determinant=a=>a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]);
const matrix=a=>Array.isArray(a)&&a.length===3&&a.every(row=>Array.isArray(row)&&row.length===3&&row.every(Number.isFinite));
export function auditFrameReturn(topology,{tolerance=1e-9}={}){
 if(!Number.isFinite(tolerance)||tolerance<=0||tolerance>1e-3)throw Error('Tolerance must be in (0, 1e-3].');
 const report={status:'unknown',tolerance,scope:'Numerical SO(3) frame return for explicitly supplied PE-based walks; not inferred topology, a native proof, or physical validation.',issues:[],walks:[]};
 if(topology==null){report.issues.push({code:'missing-frame-topology'});return report;}
 const fail=(code,detail={})=>report.issues.push({code,...detail});
 const index=(rows,name)=>{const m=new Map();if(!Array.isArray(rows)){fail('invalid-collection',{collection:name});return m;}for(const r of rows){if(!r||typeof r.id!=='string'||!r.id||m.has(r.id))fail('invalid-or-duplicate-id',{collection:name});else m.set(r.id,r);}return m;};
 const vertices=index(topology.vertices,'vertices'),edges=index(topology.edges,'edges'),walks=index(topology.walks,'walks');
 for(const v of vertices.values())if(!['PE','N','junction'].includes(v.role))fail('invalid-vertex-role',{vertex:v.id});
 for(const e of edges.values()){
  if(!vertices.has(e.from)||!vertices.has(e.to))fail('unbound-endpoint',{edge:e.id});
  if(typeof e.support!=='string'||!e.support)fail('missing-support',{edge:e.id});
  if(e.transport!==undefined&&(!matrix(e.transport)||error(multiply(transpose(e.transport),e.transport),I)>tolerance||Math.abs(determinant(e.transport)-1)>tolerance))fail('not-SO3',{edge:e.id});
 }
 // All composable turns are admitted unless the caller supplies restrictions.
 let turns=null;
 if(topology.turns!==undefined){turns=new Set();if(!Array.isArray(topology.turns))fail('invalid-turns');else for(const t of topology.turns){if(!Array.isArray(t)||t.length!==2||!edges.has(t[0])||!edges.has(t[1]))fail('invalid-turn');else turns.add(JSON.stringify(t));}}
 if(report.issues.length){report.status='refuted';return report;}
 for(const w of walks.values()){
  const result={id:w.id,status:'unknown',issues:[]};report.walks.push(result);
  const issue=(code,detail={})=>result.issues.push({code,...detail});
  const kind=w.kind??'PE';
  if(!['PE','N'].includes(kind))issue('invalid-walk-kind');
  else if(vertices.get(w.base)?.role!==kind)issue(kind==='PE'?'base-is-not-PE':'base-is-not-N');
  if(!Array.isArray(w.edges)||!w.edges.length){issue('empty-or-invalid-walk');result.status='refuted';continue;}
  const forward=w.edges.map(id=>edges.get(id));
  if(forward.some(e=>!e)){issue('unknown-edge');result.status='refuted';continue;}
  const checkWalk=rows=>{
   let at=w.base;
   for(const e of rows){if(e.from!==at)issue('noncomposable-walk',{edge:e.id});at=e.to;}
   if(at!==w.base)issue('vertex-does-not-return');
   if(turns)for(let i=0;i<rows.length;i++)if(!turns.has(JSON.stringify([rows[i].id,rows[(i+1)%rows.length].id])))issue('forbidden-turn',{edge:rows[i].id});
  };
  checkWalk(forward);
  const reverse=[...forward].reverse().map(e=>edges.get(e.reverse));
  for(const e of forward){const r=edges.get(e.reverse);if(!r)issue('missing-explicit-reverse',{edge:e.id});else if(r.from!==e.to||r.to!==e.from||r.support!==e.support||r.reverse!==e.id)issue('invalid-reverse-incidence',{edge:e.id});}
  if(reverse.every(Boolean))checkWalk(reverse);
  if(result.issues.length){result.status='refuted';continue;}
  if([...forward,...reverse].some(e=>e.transport===undefined)){issue('missing-frame-transport');continue;}
  for(const e of forward)if(error(edges.get(e.reverse).transport,transpose(e.transport))>tolerance)issue('reverse-transport-not-inverse',{edge:e.id});
  // Column frames: F_next = R_edge F. Traversal e1,e2,... gives ...R2 R1.
  result.forwardHolonomy=forward.reduce((h,e)=>multiply(e.transport,h),I);
  result.reverseHolonomy=reverse.reduce((h,e)=>multiply(e.transport,h),I);
  result.forwardError=error(result.forwardHolonomy,I);result.reverseError=error(result.reverseHolonomy,I);
  if(result.forwardError>tolerance||result.reverseError>tolerance)issue('frame-does-not-return');
  result.status=result.issues.length?'refuted':'verified';
 }
 const covered=new Set([...walks.values()].map(w=>w.base)),uncovered=[...vertices.values()].filter(v=>v.role==='PE'&&!covered.has(v.id)).map(v=>v.id);
 if(uncovered.length)fail('uncovered-PE-vertices',{vertices:uncovered});
 if(report.walks.some(w=>w.status==='refuted'))report.status='refuted';
 else if(!report.walks.length||uncovered.length||report.walks.some(w=>w.status==='unknown'))report.status='unknown';
 else report.status='verified';
 return report;
}
