import {buildRuthenium98Carrier} from './ruthenium-98-model.mjs';
const key=p=>p.join(','),edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,p)=>s+p[i]/vs.length,0));
const same=(a,b)=>key(a)===key(b);

// Explicit edge-to-opposite-edge candidate, not a derivation of 54 N tubes.
// (a,b) select four native entry/exit ports. p orders deposition into coordinates
// 0/1; e orders withdrawal from 2/3. Each transfer is one actual honeycomb edge.
export function buildRuthenium98Wiring(){
 const cells=buildRuthenium98Carrier(),axis=[-.5,-.5,.5,.5],u=[.5,-.5,.5,-.5],v=[.5,-.5,-.5,.5];
 const inputCentre=[-1,-1,1.5,1.5],outputCentre=[1.5,1.5,-1,-1];
 const styles=[{label:'white',colors:[0xffffff]},{label:'blue-white',colors:[0x168fff,0xffffff]},{label:'red-white',colors:[0xff3030,0xffffff]},{label:'blue',colors:[0x168fff]}],strands=[],edges=new Map();
 for(let ai=0;ai<2;ai++)for(let bi=0;bi<2;bi++)for(let pi=0;pi<2;pi++)for(let ei=0;ei<2;ei++){
  const k=1+2*ai+bi,a=ai?'-':'+',b=bi?'-':'+',p=pi?'-':'+',e=ei?'-':'+';
  const deposit=pi?[...Array(5-k).fill(1),...Array(k).fill(0)]:[...Array(k).fill(0),...Array(5-k).fill(1)];
  const withdraw=ei?[...Array(5-k).fill(3),...Array(k).fill(2)]:[...Array(k).fill(2),...Array(5-k).fill(3)];
  const guide=[[-1,-1,k-1,4-k]];
  for(let i=0;i<5;i++){const next=[...guide.at(-1)];next[deposit[i]]++;next[withdraw[i]]--;guide.push(next);}
  const row=2*(pi?1:-1)+(ai?1:-1),column=2*(ei?1:-1)+(bi?1:-1);
  const incoming=inputCentre.map((x,i)=>x+2*axis[i]+.07*(row*u[i]+column*v[i]));
  const outgoing=outputCentre.map((x,i)=>x-2*axis[i]+.07*(row*u[i]+column*v[i]));
  const strand={id:`ru:wire:${a}${b}${p}${e}`,polarities:{a,b,p,e},row,column,port:k,...styles[2*pi+ei],guide,incoming,outgoing,edgeIds:[],edgeRuns:[],branches:[]};
  for(let i=1;i<guide.length;i++){
   const start=guide[i-1],end=guide[i],id=edgeKey(start,end);strand.edgeIds.push(id);
   if(!edges.has(id)){
    const owners=cells.filter(c=>c.faces.some(f=>f.some(p=>same(p,start))&&f.some(p=>same(p,end))));
    if(!owners.length)throw Error('Ru wire leaves the native edge graph');
    const face=owners[0].faces.find(f=>f.some(p=>same(p,start))&&f.some(p=>same(p,end))),d=end.map((x,j)=>x-start[j]),toward=centre(face).map((x,j)=>x-(start[j]+end[j])/2);
    const side=toward.map((x,j)=>x-d[j]*dot(toward,d)/dot(d,d)),norm=Math.hypot(...side);
    edges.set(id,{id,guide:[start,end],strandIds:[],side:side.map(x=>x/norm),carrierCells:owners.filter(c=>c.role==='neutron').map(c=>c.id)});
   }
   edges.get(id).strandIds.push(strand.id);
  }
  strands.push(strand);
 }
 for(const edge of edges.values())edge.strandIds.sort();
 for(const strand of strands){
  const points=[strand.incoming];
  for(let i=0;i<5;i++){
   const edge=edges.get(strand.edgeIds[i]),start=strand.guide[i],end=strand.guide[i+1],lane=edge.strandIds.indexOf(strand.id)-(edge.strandIds.length-1)/2,run=[];
   for(let j=0;j<=24;j++){
    let t=j/24;if(i===0)t=.12+.88*t;if(i===4)t=.88*t;
    const taper=Math.min(1,t*8,(1-t)*8),point=start.map((x,k)=>x+t*(end[k]-x)+.1*lane*taper*edge.side[k]);
    run.push(point);if(!same(points.at(-1),point))points.push(point);
   }
   strand.edgeRuns.push({edgeId:edge.id,points:run});
  }
  points.push(strand.outgoing);strand.points=points;strand.incomingPoints=points.slice(0,2);strand.outgoingPoints=points.slice(-2);
 }
 const nativeEdges=new Map();
 for(const cell of cells)for(const face of cell.faces)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){
  const id=edgeKey(face[i],face[j]);if(!nativeEdges.has(id))nativeEdges.set(id,{id,guide:[face[i],face[j]],carrierCells:[]});
  if(cell.role==='neutron'&&!nativeEdges.get(id).carrierCells.includes(cell.id))nativeEdges.get(id).carrierCells.push(cell.id);
 }
 const otherColours=new Set(strands.filter(s=>s.label!=='blue').flatMap(s=>s.edgeIds));
 const blueEdges=[...nativeEdges.values()].filter(e=>!otherColours.has(e.id)),additionalEdges=blueEdges.filter(e=>!edges.has(e.id));
 const blueCompletion={transportPolarities:{p:'-',e:'-'},edges:blueEdges,additionalEdges,continuity:'a/b assignments at junctions remain unresolved'};
 const carriers=[...new Set([...edges.values()].flatMap(e=>e.carrierCells))].sort(),uncovered=cells.filter(c=>c.role==='neutron'&&!carriers.includes(c.id)).map(c=>c.id);
 const endpointRecords=strands.map(s=>({strandId:s.id,polarities:{...s.polarities},port:s.port}));
 if(new Set(strands.map(s=>s.id)).size!==16||uncovered.length)throw Error('Incomplete Ru candidate');
 return {axis,strands,edges:[...edges.values()],blueCompletion,input:endpointRecords,output:endpointRecords.map(e=>({...e,polarities:{...e.polarities}})),stripeReferencePoints:[inputCentre,inputCentre.map((x,i)=>x+2*axis[i])],
  audit:{status:'blue-complement-network',strands:16,completePaths:16,bundles:2,rows:4,columns:4,nativeEdgeCount:edges.size,displayedEdgeCount:nativeEdges.size,otherColourEdges:otherColours.size,blueComplementEdges:blueEdges.length,additionalBlueEdges:additionalEdges.length,blueContinuityAssigned:false,stepsPerPath:5,branchSegments:0,endpointBijection:true,carrierCells:cells.length,NCarrierCoverage:{count:carriers.length,cells:carriers,uncovered},NChannelCount:null,scope:'Retained (a,b,p,e) inventory; four ports on each of two opposite tetrahedral edges. Blue fills every edge not occupied by the other colours. Extra blue edges do not yet have a/b continuation assignments. Not an identification with the 54 retained N records.'}};
}
