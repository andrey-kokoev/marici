import {singleOctahedralEnvelope} from './single-octahedral-process.mjs';
import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
import {buildSulfur32Wiring} from './sulfur-32-wiring.mjs';
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,p)=>s+p[i]/vs.length,0));
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const key=p=>p.map(x=>Math.round(x*1e9)/1e9).join(',');
const edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
const interpolate=(a,b,t)=>a.map((x,i)=>x+t*(b[i]-x));

// Explicit candidate, not a derivation of the periodic model's 16 N channels.
// a,b label the two successive binary route choices in canonical coordinate order.
// Their physical interpretation remains retained metadata, not a signal operation.
export function buildSulfurIncomingBundle({radius=1}={}){
 if(!Number.isInteger(radius)||radius<1||radius>3)throw Error('Supported octahedral radius is 1..3');
 const sector=buildPESymmetricSector(radius),envelope=singleOctahedralEnvelope(radius),tip=envelope[1],exitTip=envelope[0];
 const axis=[-.5,-.5,.5,.5],u=[.5,-.5,.5,-.5],v=[.5,-.5,-.5,.5];
 const height=p=>dot(p.map((x,i)=>x-sector.centre[i]),axis);
 const reflect=p=>p.map((x,i)=>x-2*height(p)*axis[i]);
 const same=(a,b)=>key(a)===key(b),length2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
 const charged=sector.cells.filter(c=>c.role!=='neutron'),top=Math.max(...charged.map(c=>height(centre(c.vertices))));
 const joins=charged.filter(c=>Math.abs(height(centre(c.vertices))-top)<1e-9).map(c=>{
  const face=sector.boundary.find(f=>f.owners.includes(c.id)).vertices;
  const point=face.reduce((a,b)=>height(a)<height(b)?a:b);
  const touching=sector.boundary.filter(f=>f.vertices.some(p=>same(p,point)));
  const lower=[...new Map(touching.flatMap(f=>f.vertices).filter(p=>height(p)<height(point)-1e-9&&length2(p,point)===2).map(p=>[key(p),p])).values()].sort((a,b)=>key(a).localeCompare(key(b)));
  if(lower.length!==2)throw Error('Expected two descending surface edges');
  return {cell:c.id,face,point,lower};
 }).sort((a,b)=>a.cell.localeCompare(b.cell));
 const styles=[{label:'white',colors:[0xffffff]},{label:'blue-white',colors:[0x168fff,0xffffff]},{label:'red-white',colors:[0xff3030,0xffffff]},{label:'blue',colors:[0x168fff]}];
 const targets=[3,4,5,2],strands=[];
 for(let pe=0;pe<4;pe++){
  const contact=interpolate(tip,envelope[targets[pe]],1/sector.edgeUnits),adjacent=joins.filter(j=>j.face.some(p=>same(p,contact)));
  if(adjacent.length!==2)throw Error('Expected two faces adjoining each entry edge');
  for(let ai=0;ai<2;ai++)for(let bi=0;bi<2;bi++){
   const a=ai===0?'+':'-',b=bi===0?'+':'-',p=pe<2?'+':'-',e=pe%2===0?'+':'-';
   const join=adjacent[ai],upper=[tip,contact,join.point,join.lower[bi]],step=join.lower[bi].map((x,i)=>x-join.point[i]);
   // Carry the same face-edge direction through the extra layers, rather than
   // embedding a small three-edge core inside the larger octahedron.
   for(let i=0;i<2*(radius-1);i++)upper.push(upper.at(-1).map((x,j)=>x+step[j]));
   const middle=upper.at(-1);
   if(Math.abs(height(middle))>1e-9)throw Error('Route does not reach the reflection plane');
   const guide=[...upper,...upper.slice(0,-1).reverse().map(reflect)];
   const row=2*(pe<2?-1:1)+(ai===0?-1:1),column=2*(pe%2===0?-1:1)+(bi===0?-1:1);
   const incoming=tip.map((x,i)=>x+2.14*axis[i]+.07*(row*u[i]+column*v[i]));
   strands.push({id:`wire:${a}${b}${p}${e}`,polarities:{a,b,p,e},row,column,...styles[pe],guide,upperGuide:upper,joinCell:join.cell,incoming, outgoing:reflect(incoming),branches:[]});
  }
 }
 // Complete a global middle-plane matching: one occurrence at each port goes
 // around the rim to the next port; the other crosses to the opposite port.
 // These are explicit candidate routing conventions, not new signal operations.
 const middleEdges=new Map();
 for(const cell of sector.cells)for(const a of cell.vertices)for(const b of cell.vertices){
  if(Math.abs(height(a))>1e-9||Math.abs(height(b))>1e-9||length2(a,b)!==2)continue;
  const id=edgeKey(a,b),surface=sector.boundary.some(f=>f.vertices.some(p=>same(p,a))&&f.vertices.some(p=>same(p,b)));
  middleEdges.set(id,{guide:[a,b],surface});
 }
 const portGroups=[...new Map(strands.map(s=>[key(s.upperGuide.at(-1)),s.upperGuide.at(-1)])).values()].sort((a,b)=>Math.atan2(dot(a,v)-dot(sector.centre,v),dot(a,u)-dot(sector.centre,u))-Math.atan2(dot(b,v)-dot(sector.centre,v),dot(b,u)-dot(sector.centre,u))).map(point=>({point,slots:strands.map((s,i)=>({s,i})).filter(({s})=>same(s.upperGuide.at(-1),point)).sort((a,b)=>a.s.id.localeCompare(b.s.id)).map(x=>x.i)}));
 if(portGroups.length!==8||portGroups.some(p=>p.slots.length!==2))throw Error('Expected eight two-strand middle ports');
 const routeMiddle=(start,end,rimOnly)=>{
  const queue=[[start]],seen=new Set([key(start)]);
  for(let cursor=0;cursor<queue.length;cursor++){
   const path=queue[cursor],last=path.at(-1);if(same(last,end))return path;
   const neighbours=[...middleEdges.values()].filter(e=>(!rimOnly||e.surface)&&e.guide.some(p=>same(p,last))).map(e=>e.guide.find(p=>!same(p,last))).sort((a,b)=>length2(a,sector.centre)-length2(b,sector.centre)||key(a).localeCompare(key(b)));
   for(const next of neighbours)if(!seen.has(key(next))){seen.add(key(next));queue.push([...path,next]);}
  }
  throw Error('No native middle-plane route');
 };
 const uppers=strands.map(s=>s.upperGuide);
 for(let port=0;port<8;port++)for(let slot=0;slot<2;slot++){
  const source=portGroups[port].slots[slot],target=portGroups[(port+(slot===0?1:4))%8].slots[slot],s=strands[source];
  const middle=routeMiddle(uppers[source].at(-1),uppers[target].at(-1),slot===0);
  s.guide=[...uppers[source],...middle.slice(1),...uppers[target].slice(0,-1).reverse().map(reflect)];
  s.middleRoute=middle;s.middleRouting=slot===0?'rim':'interior';s.inputSlot=source;s.outputSlot=target;s.outgoing=reflect(strands[target].incoming);
 }
 if(new Set(strands.map(s=>s.outputSlot)).size!==16)throw Error('Middle matching is not bijective');
 // Group shared native edges, but never merge or copy the retained wire records.
 const edges=new Map();
 for(const s of strands)for(let i=1;i<s.guide.length;i++){
  const start=s.guide[i-1],end=s.guide[i],id=edgeKey(start,end);
  if(!edges.has(id)){
   const surfaceFace=sector.boundary.find(f=>f.vertices.some(p=>same(p,start))&&f.vertices.some(p=>same(p,end)));
   const nativeFace=sector.cells.flatMap(c=>c.faces).find(f=>f.some(p=>same(p,start))&&f.some(p=>same(p,end)));
   const face=surfaceFace??(nativeFace?{vertices:nativeFace}:null);
   if(!face)throw Error('Route leaves the native edge graph');
   const d=end.map((x,j)=>x-start[j]),toward=centre(face.vertices).map((x,j)=>x-(start[j]+end[j])/2);
   const lateral=toward.map((x,j)=>x-d[j]*dot(toward,d)/dot(d,d)),norm=Math.sqrt(dot(lateral,lateral));
   edges.set(id,{id,guide:[start,end],surface:Boolean(surfaceFace),side:lateral.map(x=>x/norm),strandIds:[],carrierCells:sector.cells.filter(c=>c.role==='neutron'&&c.vertices.some(p=>same(p,start))&&c.vertices.some(p=>same(p,end))).map(c=>c.id)});
  }
  edges.get(id).strandIds.push(s.id);
 }
 for(const edge of edges.values())edge.strandIds.sort();
 for(const s of strands){
  const points=[s.incoming];s.edgeRuns=[];
  for(let i=1;i<s.guide.length;i++){
   const start=s.guide[i-1],end=s.guide[i],edge=edges.get(edgeKey(start,end));
   const lane=edge.strandIds.indexOf(s.id)-(edge.strandIds.length-1)/2,run=[];
   for(let k=0;k<=24;k++){
    let t=k/24;if(i===1)t=.12+.88*t;if(i===s.guide.length-1)t=.88*t;
    const taper=i===1?Math.min(1,(1-t)*8):i===s.guide.length-1?Math.min(1,t*8):Math.min(1,t*8,(1-t)*8);
    const point=interpolate(start,end,t).map((x,j)=>x+.1*lane*taper*edge.side[j]);
    points.push(point);run.push(point);
   }
   s.edgeRuns.push({edgeId:edge.id,points:run});
  }
  points.push(s.outgoing);
  s.points=points.filter((p,i)=>i===0||length2(p,points[i-1])>1e-18);
  s.incomingPoints=s.points.slice(0,2);s.outgoingPoints=s.points.slice(-2);
  s.edgeIds=s.guide.slice(1).map((p,i)=>edgeKey(s.guide[i],p));
 }
 const layer2Joins=joins.map(j=>({...j,inputs:strands.filter(s=>s.joinCell===j.cell).map(s=>s.id),labels:[...new Set(strands.filter(s=>s.joinCell===j.cell).map(s=>s.label))]}));
 const layer3Mixes=[...edges.values()].filter(g=>Math.abs(height(g.guide[0])-1)<1e-9&&Math.abs(height(g.guide[1]))<1e-9);
 const carriers=[...new Set([...edges.values()].flatMap(g=>g.carrierCells))].sort();
 const uncovered=sector.cells.filter(c=>c.role==='neutron'&&!carriers.includes(c.id)).map(c=>c.id);
 const periodic=radius===1?buildSulfur32Wiring():{groups:sector.cells.filter(c=>c.role==='neutron').map((c,i)=>({id:c.id,label:`N${i+1}`})),channels:sector.cells.filter(c=>c.role==='neutron').map(c=>({id:c.id,members:[{id:c.id}]}))};
 const channelGroups=periodic.channels.map(c=>({id:c.id,label:periodic.groups.find(g=>g.id===c.id).label,members:c.members.map(m=>m.id),strandIds:strands.filter(s=>s.edgeIds.some(id=>edges.get(id).carrierCells.some(cell=>c.members.some(m=>m.id===cell)))).map(s=>s.id)}));
 if(radius===1&&(uncovered.length||channelGroups.some(g=>g.strandIds.length===0)))throw Error('Incomplete N carrier/group coverage');
 const endpoints=strands.map(s=>({strandId:s.id,polarities:{...s.polarities}}));
 return {tip,exitTip,axis,strands,edges:[...edges.values()],input:endpoints,output:strands.toSorted((a,b)=>a.outputSlot-b.outputSlot).map(s=>({strandId:s.id,polarities:{...s.polarities}})),channelGroups,layer2Joins,layer3Mixes,
  stripeReferencePoints:[tip,tip.map((x,i)=>x+2*axis[i])],
  audit:{bundles:2,incomingBundles:1,outgoingBundles:1,strands:16,rows:4,columns:4,white:4,blue:4,blueWhite:4,redWhite:4,internalSegments:[...edges.values()].filter(e=>!e.surface).length,displayTurns:0,edgeGuideCount:edges.size,firstSplit:{kind:'vertex-fanout'},layer2Recombinations:layer2Joins,layer3Mixes,branchSegments:0,completePaths:16,endpointBijection:true,NCarrierCoverage:{count:carriers.length,cells:carriers,uncovered},NGroupCoverage:{count:channelGroups.length,groups:channelGroups},endpointPermutation:strands.map(s=>s.outputSlot),NChannelCount:null,routingStatus:'candidate: bijective rim/interior middle matching; full N-group incidence coverage, not periodic wiring equivalence'}};
}
