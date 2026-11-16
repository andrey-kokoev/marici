// Bounded Ca44/Ca46 local-cycle binding. This is NOT a global junction-routing map.
import {auditFrameReturn} from './frame-return.mjs';
const transpose=a=>a[0].map((_,i)=>a.map(r=>r[i]));
const multiply=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0)));
const zRotation=a=>[[Math.cos(a),-Math.sin(a),0],[Math.sin(a),Math.cos(a),0],[0,0,1]];
function polygon(d){
 if(!/^M[-\d., L]+Z$/.test(d))throw Error('Expected a straight closed polygon');
 const n=d.match(/-?\d+(?:\.\d+)?/g).map(Number);
 if(n.length%2)throw Error('Unpaired coordinates');
 return Array.from({length:n.length/2},(_,i)=>n.slice(2*i,2*i+2));
}
export function bindCa46LocalPaths(definition,svg){
 if(definition.id!=='Ca46')throw Error('This entrypoint is scoped to Ca46');
 return bindCalciumLocalPaths(definition,svg);
}
export function bindCalciumLocalPaths(definition,svg){
 if(!['Ca44','Ca46'].includes(definition.id))throw Error('This trial is scoped to Ca44/Ca46');
 const cells=new Map();
 for(const m of svg.matchAll(/<g class="cell-hit" data-cell="([^"]+)"[^>]*><path fill="transparent" d="([^"]+)"/g)){
  const points=polygon(m[2]);if(points.length!==4)throw Error('Expected crossed-square cell');
  cells.set(m[1],Object.fromEntries(['T','R','B','L'].map((p,i)=>[p,points[i]])));
 }
 const topology={vertices:[],edges:[],walks:[]},bindings=[];
 function addCycle(id,kind,points,source){
  if(points.some((p,i)=>p[0]===points[(i+1)%points.length][0]&&p[1]===points[(i+1)%points.length][1]))throw Error('Degenerate cycle');
  const ids=points.map((position,i)=>{const vertex=`${id}:v${i}`;topology.vertices.push({id:vertex,role:i===0?kind:'junction',position});return vertex;});
  const edgeIds=[];
  for(let i=0;i<points.length;i++){
   const edge=`${id}:e${i}`,inverse=edge+':reverse',from=ids[i],to=ids[(i+1)%ids.length],support=`${id}:support${i}`;
   // Directions are explicit trial assignments, not extracted native arrows.
   topology.edges.push({id:edge,from,to,support,reverse:inverse},{id:inverse,from:to,to:from,support,reverse:edge});edgeIds.push(edge);
  }
  topology.walks.push({id,kind,base:ids[0],edges:edgeIds});bindings.push({walk:id,source,positions:points});
 }
 for(const p of definition.graph.pairs){
  const ports=cells.get(p.cell);if(!ports)throw Error(`No rendered cell for ${p.id}`);
  const common=p.red.filter(port=>p.blue.includes(port));if(common.length!==1)throw Error('Pair needs one shared PE port');
  const main=common[0],red=p.red.find(port=>port!==main),blue=p.blue.find(port=>port!==main);
  // Trial convention: red leg enters PE, blue leg leaves it; base closes cycle.
  addCycle(p.id,'PE',[ports[main],ports[blue],ports[red]],{pair:p.id,cell:p.cell,mainPort:main,incomingPort:red,outgoingPort:blue});
 }
 let n=0;
 for(const m of svg.matchAll(/<path class="space-frame trial-shell(\d)-wrapper" data-shell="[^"]+" data-shells="([^"]+)" d="([^"]+)"/g))addCycle(`wrapper:${++n}`,'N',polygon(m[3]),{wrapper:n,ownerShell:Number(m[1]),spans:m[2].split(' ')});
 if(n!==definition.N-definition.Z)throw Error('Wrapper/inventory mismatch');
 return {definitionId:definition.id,topology,bindings,scope:'Local cycles with occurrence-local vertices; coincident screen points are not identified.',
  assumptions:['Red leg incoming, blue leg outgoing at PE; base segment closes each triangle.','Wrapper orientation follows rendered polygon order.','Reverse arrows are candidate declarations, not evidence of native reverse execution.'],
  residuals:['Global junction identifications and routing are not supplied.','The crossed squares vertical diagonals are not assigned to these triangle/base cycles.','Per-edge SO(3) transports are not supplied by the drawing.'],
  counts:{PE:definition.Z,localPEWalks:definition.graph.pairs.length,neutronWrapperWalks:n,unboundVerticalDiagonals:cells.size}};
}
export function planarFrameControl(binding){
 const topology=structuredClone(binding.topology),edges=new Map(topology.edges.map(e=>[e.id,e]));
 for(const [i,w] of topology.walks.entries()){
  const points=binding.bindings[i].positions;
  for(let j=0;j<points.length;j++){
   const a=points[j],b=points[(j+1)%points.length],c=points[(j+2)%points.length],u=[b[0]-a[0],b[1]-a[1]],v=[c[0]-b[0],c[1]-b[1]];
   const angle=Math.atan2(u[0]*v[1]-u[1]*v[0],u[0]*v[0]+u[1]*v[1]),edge=edges.get(w.edges[j]);
   edge.transport=zRotation(angle);edges.get(edge.reverse).transport=transpose(edge.transport);
  }
 }
 return topology;
}
export function studyDiagramFrameReturn(definition,svg){
 const binding=bindCa46LocalPaths(definition,svg),control=planarFrameControl(binding),twisted=structuredClone(control),e=twisted.edges.find(e=>e.id===twisted.walks[0].edges[0]);
 e.transport=multiply(zRotation(Math.PI/2),e.transport);twisted.edges.find(r=>r.id===e.reverse).transport=transpose(e.transport);
 return {binding,unassigned:auditFrameReturn(binding.topology),planarControl:auditFrameReturn(control),twistedControl:auditFrameReturn(twisted),
  status:'unknown',conclusion:'The same rendered local paths admit returning and nonreturning frame assignments. Planar turning is an SO(2) subgroup control and closes by construction; it does not derive a physical transport law or verify global routing.'};
}
