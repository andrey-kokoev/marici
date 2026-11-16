// Candidate endpoint-gluing model. Crossings are NOT silently made junctions.
import {bindCalciumLocalPaths} from './diagram-path-trial.mjs';
import {auditFrameReturn} from './frame-return.mjs';
const transpose=a=>a[0].map((_,i)=>a.map(r=>r[i]));
const multiply=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0)));
const rotation=(angle,axis)=>{const c=Math.cos(angle),s=Math.sin(angle);return axis==='x'?[[1,0,0],[0,c,-s],[0,s,c]]:[[c,-s,0],[s,c,0],[0,0,1]];};
export function bindCa46ConnectedPaths(definition,svg){
 if(definition.id!=='Ca46')throw Error('This entrypoint is scoped to Ca46');
 return bindCalciumConnectedPaths(definition,svg);
}
export function bindCalciumConnectedPaths(definition,svg){
 const local=bindCalciumLocalPaths(definition,svg),vertices=new Map(),supports=new Map(),segments=[],peBindings=[];
 function vertex(position,role='junction',occurrence){
  const key=position.join(','),v=vertices.get(key)||{id:`v:${key}`,position,role,occurrences:[]};
  if(role==='PE'||(role==='N'&&v.role!=='PE'))v.role=role;
  if(occurrence&&!v.occurrences.includes(occurrence))v.occurrences.push(occurrence);
  vertices.set(key,v);return v.id;
 }
 function segment(a,b,source){
  const from=vertex(a),to=vertex(b);if(from===to)throw Error('Degenerate segment');
  const key=JSON.stringify([from,to].sort());let s=supports.get(key);
  if(!s){s={id:`support:${supports.size}`,from,to,sources:[]};supports.set(key,s);segments.push({a,b,support:s.id});}
  s.sources.push(source);return {support:s.id,from,to};
 }
 const localRoutes=[];
 for(const b of local.bindings){
  const kind=b.source.pair?'PE':'N',base=vertex(b.positions[0],kind,b.walk);
  if(kind==='PE')peBindings.push({pair:b.source.pair,vertex:base});
  const route=b.positions.map((p,i)=>segment(p,b.positions[(i+1)%b.positions.length],b.walk));localRoutes.push({id:b.walk,base,route});
 }
 let verticals=0;
 for(const m of svg.matchAll(/<path class="neutron sketch-cross" data-cell="([^"]+)" d="M(-?\d+(?:\.\d+)?) (-?\d+(?:\.\d+)?) L(-?\d+(?:\.\d+)?) (-?\d+(?:\.\d+)?)"/g)){
  if(Number(m[2])!==Number(m[4]))continue;
  segment([Number(m[2]),Number(m[3])],[Number(m[4]),Number(m[5])],`vertical:${m[1]}`);verticals++;
 }
 if(verticals!==local.counts.unboundVerticalDiagonals)throw Error('Vertical diagonal coverage mismatch');
 // Two PE occurrences form an abstract tetrahedron (K4) in top projection.
 // Its opposite neutron legs cross only in projection, not at a graph vertex.
 const tetrahedra=[],cellBindings=new Map();
 for(const b of local.bindings)if(b.source.pair){const rows=cellBindings.get(b.source.cell)||[];rows.push(b);cellBindings.set(b.source.cell,rows);}
 for(const [cell,rows] of cellBindings){
  if(rows.length!==2)throw Error('Tetrahedron requires two PE occurrences');
  const points=new Map(rows.flatMap(b=>b.positions).map(p=>[p.join(','),p]));
  if(points.size!==4)throw Error('Tetrahedron projection requires four distinct vertices');
  const ids=[...points.keys()].map(p=>`v:${p}`),tetraSupports=[...supports.values()].filter(s=>ids.includes(s.from)&&ids.includes(s.to));
  if(tetraSupports.length!==6)throw Error('Tetrahedron must retain all six edges');
  const diagonals=tetraSupports.filter(s=>{const a=vertices.get(s.from.slice(2)).position,b=vertices.get(s.to.slice(2)).position;return a[0]===b[0]||a[1]===b[1];});
  if(diagonals.length!==2||new Set(diagonals.flatMap(s=>[s.from,s.to])).size!==4)throw Error('Projected neutron legs must be opposite tetrahedron edges');
  for(const s of tetraSupports)s.role=diagonals.includes(s)?'neutron-leg':'PE-leg';
  tetrahedra.push({cell,PEOccurrences:rows.map(b=>b.source.pair),vertices:ids,supports:tetraSupports.map(s=>s.id),oppositeNeutronLegs:diagonals.map(s=>s.id),projection:'top-view',centralJunction:false,depthOrder:'unspecified'});
 }
 const byId=new Map([...vertices.values()].map(v=>[v.id,v])),edges=[],adj=new Map([...byId.keys()].map(id=>[id,[]])),lookup=new Map();
 for(const s of supports.values()){
  const f={id:s.id+':+',from:s.from,to:s.to,support:s.id,reverse:s.id+':-'},r={id:s.id+':-',from:s.to,to:s.from,support:s.id,reverse:f.id};
  edges.push(f,r);adj.get(f.from).push(f);adj.get(r.from).push(r);lookup.set(JSON.stringify([f.from,f.to]),f.id);lookup.set(JSON.stringify([r.from,r.to]),r.id);
 }
 const edgeMap=new Map(edges.map(e=>[e.id,e]));
 const walks=localRoutes.map(w=>({id:w.id,base:w.base,kind:byId.get(w.base).role,edges:w.route.map(s=>lookup.get(JSON.stringify([s.from,s.to])))}));
 // A spanning forest gives a complete fundamental-cycle basis of this candidate
 // graph, without claiming that arbitrary turns are admitted by the model.
 const seen=new Set(),treeSupports=new Set(),components=[],cycles=[];
 for(const initial of byId.keys()){
  if(seen.has(initial))continue;
  const component=[],pending=[initial],found=new Set([initial]);
  for(let i=0;i<pending.length;i++){const v=pending[i];component.push(v);for(const e of adj.get(v))if(!found.has(e.to)){found.add(e.to);pending.push(e.to);}}
  const root=component.find(id=>byId.get(id).role==='PE')||component.find(id=>byId.get(id).role==='N');
  if(!root)throw Error('Component has no declared cycle base');
  const routes=new Map([[root,[]]]),queue=[root];seen.add(root);
  for(let i=0;i<queue.length;i++){const v=queue[i];for(const e of adj.get(v))if(!routes.has(e.to)){routes.set(e.to,[...routes.get(v),e.id]);treeSupports.add(e.support);queue.push(e.to);seen.add(e.to);}}
  const componentSet=new Set(component);
  for(const s of supports.values())if(componentSet.has(s.from)&&!treeSupports.has(s.id)){
   const returning=[...routes.get(s.to)].reverse().map(id=>edgeMap.get(id).reverse),id=`basis:${cycles.length}`;
   const cycle={id,base:root,kind:byId.get(root).role,edges:[...routes.get(s.from),s.id+':+',...returning],chord:s.id};cycles.push(cycle);walks.push(cycle);
  }
  components.push({root,vertices:component});
 }
 const branches=[...adj].filter(([,a])=>a.length>2).map(([id,a])=>({vertex:id,degree:a.length,nonBacktrackingChoicesPerArrival:a.length-1}));
 // Record proper crossings only. Do not identify their two supports.
 const crossings=[];
 const cross=(a,b)=>a[0]*b[1]-a[1]*b[0],sub=(a,b)=>[a[0]-b[0],a[1]-b[1]];
 for(let i=0;i<segments.length;i++)for(let j=i+1;j<segments.length;j++){
  const a=segments[i],b=segments[j],u=sub(a.b,a.a),v=sub(b.b,b.a),d=cross(u,v);if(!d)continue;
  const delta=sub(b.a,a.a),t=cross(delta,v)/d,s=cross(delta,u)/d;
  if(t>0&&t<1&&s>0&&s<1)crossings.push({supports:[a.support,b.support],position:[a.a[0]+t*u[0],a.a[1]+t*u[1]],joined:false});
 }
 for(const t of tetrahedra){const crossing=crossings.find(c=>t.oppositeNeutronLegs.every(id=>c.supports.includes(id)));if(!crossing)throw Error('Missing tetrahedron projection crossing');crossing.reason='opposite-neutron-legs-in-tetrahedron';crossing.cell=t.cell;}
 for(const e of edges)e.kind=[...supports.values()].find(s=>s.id===e.support).role||'neutron-wrapper';
 return {definitionId:definition.id,topology:{vertices:[...vertices.values()],edges,walks},supports:[...supports.values()],tetrahedra,peBindings,components,cycles,branches,crossings,
  counts:{PEOccurrences:peBindings.length,vertices:vertices.size,supports:supports.size,components:components.length,cycleRank:supports.size-vertices.size+components.length,basisCycles:cycles.length,verticalDiagonals:verticals,tetrahedra:tetrahedra.length,tetrahedralProjectionCrossings:crossings.filter(c=>c.cell).length},
  status:'candidate',assumptions:['Equal explicit endpoint coordinates identify a candidate vertex.','Each geometric segment has declared forward and inverse candidate arrows.','Two-PE squares are projected tetrahedra; their opposite neutron legs never join at the projected crossing.','Other interior crossings remain unjoined as a candidate convention; all composable turns are allowed for controls only.'],
  residuals:['Endpoint gluing is a proposed interpretation, not an established incidence law.','Routing choices at branching vertices remain unspecified.','Frame transport still needs a model-derived law; gauge controls cannot select geometry.']};
}
export function studyConnectedCa46(definition,svg){
 if(definition.id!=='Ca46')throw Error('This entrypoint is scoped to Ca46');
 return studyConnectedCalcium(definition,svg);
}
export function studyConnectedCalcium(definition,svg){
 const binding=bindCalciumConnectedPaths(definition,svg),flat=structuredClone(binding.topology);
 const frames=new Map(flat.vertices.map((v,i)=>[v.id,multiply(rotation(i*Math.PI/7,'x'),rotation(i*Math.PI/11,'z'))]));
 for(const e of flat.edges)e.transport=multiply(frames.get(e.to),transpose(frames.get(e.from)));
 const twisted=structuredClone(flat),chord=binding.cycles[0]?.chord;
 if(!chord)throw Error('No cycle for hostile control');
 const e=twisted.edges.find(e=>e.id===chord+':+');e.transport=multiply(rotation(Math.PI/2,'x'),e.transport);twisted.edges.find(r=>r.id===e.reverse).transport=transpose(e.transport);
 return {binding,gaugeControl:auditFrameReturn(flat),twistedControl:auditFrameReturn(twisted),status:'unknown',
  conclusion:'Connected candidate graph and complete cycle basis constructed. Gauge-derived transports return all frames by telescoping; a support twist preserves incidence and inverse transport but breaks return. Actual routing and frame law remain unspecified.'};
}
