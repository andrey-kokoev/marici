// Global integral-flow existence under a declared geometric corridor policy.
// Individual paths are extracted AFTER solving, not grown by reader admission.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const paths={contract:'research/strominger/contracts/su32-edge5-global-routing-witness-v1.json',
 binding:'research/strominger/results/su32-edge5-fibre-placement-binding-v1/verification.json',
 carrier:'research/strominger/results/su32-edge5-extension-contract-v1/verification.json'};
const hash=x=>createHash('sha256').update(x).digest('hex'),docs={},sourceHashes={};
for(const [name,path] of Object.entries(paths)){
 const bytes=await fs.readFile(path);sourceHashes[path]=hash(bytes);docs[name]=JSON.parse(bytes);
 for(const [p,h] of Object.entries(docs[name].sourceHashes??{}))assert.equal(hash(await fs.readFile(p)),h,`Stale input: ${p}`);
}
const {contract,binding,carrier}=docs;assert.equal(contract.binding,paths.binding);
const geometry=carrier.edge5Carrier,cells=geometry.cells,byCell=new Map(cells.map(c=>[c.id,c]));
const layer=new Map(geometry.layers.flatMap(l=>l.cells.map(id=>[id,l.layer])));
const entry=binding.boundaries.entry.attachment.cell,exit=binding.boundaries.exit.attachment.cell;
const count=binding.fibres.length;assert.equal(count,80);assert.equal(cells.length,245);
const faceById=new Map(geometry.faces.map(f=>[f.id,f]));
const directed=geometry.faces.filter(f=>f.owners.length===2).map(f=>{
 const [from,to]=[...f.owners].sort((a,b)=>layer.get(a)-layer.get(b));assert.equal(layer.get(to)-layer.get(from),1);
 return {face:f.id,from,to};
});assert.equal(directed.length,560);
// Lower-bound circulation solver, with no cost function or candidate ranking.
class Flow {
 constructor(n){this.g=Array.from({length:n},()=>[]);}
 add(u,v,capacity){const a={to:v,rev:this.g[v].length,cap:capacity,initial:capacity},b={to:u,rev:this.g[u].length,cap:0,initial:0};this.g[u].push(a);this.g[v].push(b);return a;}
 max(s,t){let total=0;
  for(;;){const level=Array(this.g.length).fill(-1),q=[s];level[s]=0;
   for(let k=0;k<q.length;k++)for(const e of this.g[q[k]])if(e.cap>0&&level[e.to]<0){level[e.to]=level[q[k]]+1;q.push(e.to);}
   if(level[t]<0)return total;
   const at=Array(this.g.length).fill(0);
   const send=(v,f)=>{if(v===t)return f;for(;at[v]<this.g[v].length;at[v]++){
    const e=this.g[v][at[v]];if(e.cap<=0||level[e.to]!==level[v]+1)continue;
    const got=send(e.to,Math.min(f,e.cap));if(got){e.cap-=got;this.g[e.to][e.rev].cap+=got;return got;}
   }return 0;};
   for(let f;(f=send(s,Number.MAX_SAFE_INTEGER))>0;)total+=f;
  }
 }
}
function circulation(nodeCount,arcs){
 const S=nodeCount,T=nodeCount+1,net=new Flow(nodeCount+2),balance=Array(nodeCount).fill(0);
 const refs=arcs.map(a=>{balance[a.from]-=a.lower;balance[a.to]+=a.lower;return net.add(a.from,a.to,a.upper-a.lower);});
 let demand=0;for(let i=0;i<nodeCount;i++)if(balance[i]>0){net.add(S,i,balance[i]);demand+=balance[i];}else if(balance[i]<0)net.add(i,T,-balance[i]);
 const sent=net.max(S,T);return {feasible:sent===demand,demand,sent,
 flows:arcs.map((a,i)=>a.lower+refs[i].initial-refs[i].cap)};
}
const index=new Map(cells.map((c,i)=>[c.id,i]));
const input=id=>2*index.get(id),output=id=>2*index.get(id)+1;
const arcs=[...cells.map(c=>({kind:'cell',id:c.id,from:input(c.id),to:output(c.id),lower:1,upper:count})),
 ...directed.map(e=>({kind:'face',id:e.face,from:output(e.from),to:input(e.to),lower:0,upper:count})),
 {kind:'bookkeeping',id:'fixed-total-not-a-physical-edge',from:output(exit),to:input(entry),lower:count,upper:count}];
const solution=circulation(cells.length*2,arcs);assert(solution.feasible,'Declared global circulation has no witness');
// Independent conservation/bounds check of the ENTIRE solved assignment.
const balance=Array(cells.length*2).fill(0);
for(let i=0;i<arcs.length;i++){const a=arcs[i],f=solution.flows[i];assert(Number.isInteger(f)&&f>=a.lower&&f<=a.upper);balance[a.from]-=f;balance[a.to]+=f;}
assert(balance.every(x=>x===0));
const cellFlow=new Map(cells.map((c,i)=>[c.id,solution.flows[i]]));
const faceFlow=new Map(directed.map((e,i)=>[e.face,solution.flows[cells.length+i]]));
// Decompose the solved integral DAG flow. Enumeration order only picks one
// witness decomposition; it is not a native selector or an optimization law.
const remaining=new Map(faceFlow),routes=[];
for(const fibre of binding.fibres){
 const route={fibre:fibre.id,cells:[entry],faces:[]};let at=entry;
 while(at!==exit){
  const edge=directed.find(e=>e.from===at&&remaining.get(e.face)>0);assert(edge);
  remaining.set(edge.face,remaining.get(edge.face)-1);route.faces.push(edge.face);route.cells.push(edge.to);at=edge.to;
 }
 routes.push(route);
}
assert([...remaining.values()].every(n=>n===0));
const centre=vertices=>[0,1,2,3].map(i=>vertices.reduce((s,v)=>s+v[i],0)/vertices.length);
function validateRoutes(rs,start,end,sign){
 assert.equal(rs.length,80);assert.equal(new Set(rs.map(r=>r.fibre)).size,80);
 assert.deepEqual(rs.map(r=>r.fibre).sort(),binding.fibres.map(f=>f.id).sort());
 const visits=new Map(cells.map(c=>[c.id,0])),hops=new Map(directed.map(e=>[e.face,0]));
 for(const route of rs){
  assert.equal(route.cells[0],start);assert.equal(route.cells.at(-1),end);
  assert.equal(route.cells.length,17);assert.equal(route.faces.length,16);assert.equal(new Set(route.cells).size,17);
  for(const id of route.cells)visits.set(id,visits.get(id)+1);
  for(let i=0;i<route.faces.length;i++){
   const face=faceById.get(route.faces[i]);assert(face);assert.deepEqual([...face.owners].sort(),[route.cells[i],route.cells[i+1]].sort());
   assert.equal(layer.get(route.cells[i+1])-layer.get(route.cells[i]),sign);
   hops.set(face.id,hops.get(face.id)+1);
  }
 }
 assert.deepEqual(visits,cellFlow);assert.deepEqual(hops,faceFlow);return {visits,hops};
}
validateRoutes(routes,entry,exit,1);
const reverse=rs=>rs.map(r=>({...structuredClone(r),cells:[...r.cells].reverse(),faces:[...r.faces].reverse()}));
const reverseRoutes=reverse(routes);validateRoutes(reverseRoutes,exit,entry,-1);assert.deepEqual(reverse(reverseRoutes),routes);
// Actual face-to-centre-to-face corridor supports. All points are convex
// averages of cell vertices, so the segments lie in their whole convex cell.
const corridors=routes.map(r=>({fibre:r.fibre,passages:r.cells.map((id,i)=>({cell:id,
 entryFace:i?r.faces[i-1]:null,exitFace:i<r.faces.length?r.faces[i]:null,
 points:[...(i?[centre(faceById.get(r.faces[i-1]).vertices)]:[]),centre(byCell.get(id).vertices),
 ...(i<r.faces.length?[centre(faceById.get(r.faces[i]).vertices)]:[])]}))}));
const payloads=Object.fromEntries(binding.fibres.map((f,i)=>[f.id,{id:f.id,opaque:{index:i,history:['input']}}]));
const deliver=(rs,state)=>Object.fromEntries(rs.map(r=>{assert(Object.hasOwn(state,r.fibre));return [r.fibre,structuredClone(state[r.fibre])];}));
const delivered=deliver(routes,payloads);assert.deepEqual(delivered,payloads);assert.deepEqual(deliver(reverseRoutes,delivered),payloads);
// No confluence/merging operation: each named occurrence has its own successor.
const boundaryAllocation=routes.map(r=>({fibre:r.fibre,entryFace:r.faces[0],exitFace:r.faces.at(-1)}));
for(const a of boundaryAllocation){assert(binding.boundaries.entryFaceDomain.some(f=>f.face===a.entryFace));assert(binding.boundaries.exitFaceDomain.some(f=>f.face===a.exitFace));}
const placementChecks=binding.placementDomain.triples.map(t=>({triple:t.id,
 namedDeliveries:Object.fromEntries([...new Set([t.T,t.U,t.V,...t.tipGroup])].map(id=>[id,routes.filter(r=>r.cells.includes(id)).map(r=>r.fibre)])),
 selectedRecordPairReadout:null}));
assert(placementChecks.every(p=>Object.values(p.namedDeliveries).every(ids=>ids.length>0)));
const waypointObstructions=binding.fibres.filter(f=>layer.get(f.sourcePresentation)>=layer.get(f.targetPresentation)).map(f=>({fibre:f.id,
 P:f.sourcePresentation,PLayer:layer.get(f.sourcePresentation),E:f.targetPresentation,ELayer:layer.get(f.targetPresentation),
 reason:'A strictly forward path cannot visit this P anchor before its earlier reflected E anchor.'}));
assert.equal(waypointObstructions.length,40);
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
const bad=structuredClone(routes);bad[1].fibre=bad[0].fibre;reject(()=>validateRoutes(bad,entry,exit,1));
const broken=structuredClone(routes);broken[0].faces[0]=routes[0].faces[1];reject(()=>validateRoutes(broken,entry,exit,1));
reject(()=>validateRoutes(routes,entry,exit,-1));
// Independently exercise infeasibility in the lower-bound solver.
assert.equal(circulation(2,[{from:0,to:1,lower:2,upper:2},{from:1,to:0,lower:0,upper:1}]).feasible,false);negativeControls++;
const self='research/strominger/checkers/check_su32_edge5_global_routing_witness.mjs';sourceHashes[self]=hash(await fs.readFile(self));
const report={schema:'su32.edge5-global-routing-witness.v1',passed:true,contractPath:paths.contract,
 result:'A complete 80-fibre geometric corridor routing exists under the anchor-only, multiplexed, arbitrary-cell-turn policy.',
 counts:{fibres:80,coveredCells:[...cellFlow.values()].filter(n=>n>0).length,usedSharedFaces:[...faceFlow.values()].filter(n=>n>0).length,
 faceTraversals:routes.reduce((s,r)=>s+r.faces.length,0),distinctGeometricRoutes:new Set(routes.map(r=>JSON.stringify(r.cells))).size,
 markedTriplesReached:placementChecks.length,waypointObstructions:waypointObstructions.length,negativeControls},
 globalFlow:{solver:'Integral lower-bound circulation; no objective',demand:solution.demand,satisfied:solution.sent,
 cells:Object.fromEntries(cellFlow),faces:Object.fromEntries(faceFlow),bookkeepingReturnIsNotPhysical:true},
 routes,reverseRoutes,corridors,boundaryAllocation,placementChecks,waypointObstructions,
 limitations:['Any distinct face-to-face turn inside a convex cell is allowed by this candidate policy; native junction/phase rules are not derived.',
 'Multiplexing is allowed. Centreline support is verified, not nonintersecting finite-width strands or physical capacity.',
 'P/E associations remain presentation anchors. Requiring P then E as waypoints falsifies this monotone contract for forty fibres.',
 'All eight triples are geometrically reached; no triple is selected and no P/P or E/E payload map is supplied.',
 'Fibre conservation is an identity/path statement, not proof of comparison maps or higher coherence on the forty-four cones.',
 'The eight-triple reachability check is implied by the stronger all-cell coverage requirement; it is not an independent selector.'],
 signedRecordToFibreMap:null,nativeExecution:null,sourceHashes};
const dir='research/strominger/results/su32-edge5-global-routing-witness-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:true,result:report.result,counts:report.counts,limitations:report.limitations},null,2));
