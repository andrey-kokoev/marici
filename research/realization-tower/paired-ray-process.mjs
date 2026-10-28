import {edgeProcedure,cornerRay,secondEdgeRay,exteriorFaceNeighbors,interiorNeutronRound} from './edge-ray-model.mjs';
import {apex,seed,cells} from './normal-ray-model.mjs';
import {surfaceDiamondGaps} from './surface-diamond-gaps.mjs';
import {fillRayDiamonds} from './ray-diamond-pattern.mjs';
import {surfaceNeutronBoundaryGaps} from './surface-neutron-boundary.mjs';
import {identifiedSurfaceNeutrons} from './identified-surface-neutrons.mjs';
import {f134InteriorDiamonds,f123InteriorDiamonds,surfaceDiamondRemainders,remainingFaceCompletion} from './surface-interior-diamonds.mjs';

const center=vertices=>vertices[0].map((_,i)=>vertices.reduce((sum,p)=>sum+p[i]/vertices.length,0));

export function meetingSurfaceRays(k,point){
 return [1,3].map(vertex=>{
  const coordinate=vertex===1?3:1;
  const end=apex.map((x,i)=>x+(i===0?k:i===vertex?-k:0));
  const ray=cornerRay(k,point,end);
  const surfaceCells=ray.contacts.map(c=>({...c,face:cells[c.cell].vertices.filter(p=>p[coordinate]===2)})).filter(c=>c.face.length===3&&c.interval[1]-c.interval[0]>1e-9).sort((a,b)=>a.interval[0]-b.interval[0]);
  return {...ray,id:`meeting-to-V${vertex+1}`,coordinate,value:2,length:Math.sqrt(point.reduce((sum,x,i)=>sum+(x-end[i])**2,0)/2),contacts:surfaceCells.map(({cell,interval})=>({cell,interval})),surfaceCells};
 });
}

export function faceMedianRay(k,source){
 const corners=[apex,...[1,2,3].map(vertex=>apex.map((x,i)=>x+(i===0?k:i===vertex?-k:0)))];
 const start=corners[source-1],end=corners[1].map((x,i)=>(x+corners[3][i])/2);
 const coordinate=source===3?0:2,value=coordinate===0?-5+k:2;
 // Reverse clipping starts at the midpoint and ends at a unique corner cell.
 // A midpoint is not itself a unique tetrahedral-cell endpoint.
 const reverse=cornerRay(k,end,start);
 const surfaceCells=reverse.contacts.map(c=>({...c,interval:[1-c.interval[1],1-c.interval[0]],face:cells[c.cell].vertices.filter(p=>p[coordinate]===value)})).filter(c=>c.face.length===3&&c.interval[1]-c.interval[0]>1e-9).sort((a,b)=>a.interval[0]-b.interval[0]);
 return {id:`ray${source}-24`,start:[...start],end,length:Math.sqrt(start.reduce((sum,x,i)=>sum+(x-end[i])**2,0)/2),coordinate,value,cell:surfaceCells.at(-1).cell,contacts:surfaceCells.map(({cell,interval})=>({cell,interval})),surfaceCells};
}

export function pairedRayProcess(k,step){
 if(!Number.isInteger(step)||step<0||step>7+cells.length)throw Error('Invalid ray process step');
 const setup=edgeProcedure(k,0),assignments=[];
 function assign(cell,role,boundary='corner'){
  // At k=1 all four corners belong to the same seed cell. Never overwrite E.
  if(!assignments.some(a=>a.cell===cell))assignments.push({id:`${role}-${cell}`,kind:'cell-role',cell,role,boundary,point:center(cells[cell].vertices)});
 }
 assign(seed.id,'electron');
 const firstRay=step>=1?{...cornerRay(k,apex,setup.probe.point),id:'ray13'}:null;
 if(firstRay)assign(firstRay.cell,'proton');
 const ray32=step>=2?{...secondEdgeRay(k,1),id:'ray32'}:null;
 if(ray32)assign(ray32.cell,'neutron');
 const ray21=step>=3?{...cornerRay(k,ray32.end,apex),id:'ray21'}:null;
 const rays=[ray32,ray21].filter(Boolean);
 let edgeMeeting=null,edgeFronts=[];
 if(step>=4&&k>1){
  const point=apex.map((x,i)=>(x+firstRay.end[i])/2),eps=1e-9,meetingCells=[];
  for(const contact of firstRay.contacts){
   const [lo,hi]=contact.interval;
   if(hi-lo>eps){
    const meets=lo<.5-eps&&hi>.5+eps;
    assign(contact.cell,meets?'neutron':hi<=.5+eps?'electron':'proton','edge-fill');
    if(meets)meetingCells.push(contact.cell);
   }else if(Math.abs(lo-.5)<eps){
    assign(contact.cell,'neutron','edge-meeting');meetingCells.push(contact.cell);
   }
  }
  edgeMeeting={point,cells:meetingCells,kind:k%2===0?'vertex-filler':'cell'};
  edgeFronts=[{id:'ray13',start:[...apex],end:point,length:k/2},{id:'ray31',start:[...firstRay.end],end:point,length:k/2}];
 }
 const counterpartCandidates=step>=4?exteriorFaceNeighbors(k):[];
 const counterpartsAvailable=counterpartCandidates.length===2&&counterpartCandidates.every(n=>{
  const existing=assignments.find(a=>a.cell===n.cell),role=n.role==='electron'?'proton':'electron';
  return !existing||existing.role===role;
 });
 const faceNeighbors=step>=5&&counterpartsAvailable?counterpartCandidates:[];
 for(const neighbor of faceNeighbors)assign(neighbor.cell,neighbor.role==='electron'?'proton':'electron','face-neighbor');
 // Reuse Process 1's exact neighbor construction, but not its assignments.
 const supportPlan=step>=6&&faceNeighbors.length?edgeProcedure(k,9):null;
 const neutronNeighbors=supportPlan?.neutronNeighbors??[];
 const surfaceNeutronNeighbors=step>=7?(supportPlan?.surfaceNeutronNeighbors??[]):[];
 for(const [neighbors,boundary] of [[neutronNeighbors,'face-neighbor'],[surfaceNeutronNeighbors,'surface-neighbor']])for(const neighbor of neighbors){
  const existing=assignments.find(a=>a.cell===neighbor.cell);
  if(existing&&existing.role!=='neutron')throw Error(`Neutron support conflicts with ${existing.role} on cell ${neighbor.cell}`);
  assign(neighbor.cell,'neutron',boundary);
 }
 const closureRounds=[];
 for(let round=0;round<step-7&&faceNeighbors.length;round++){
  // Snapshot each round: new cells cannot justify one another in that round.
  const additions=interiorNeutronRound(k,assignments);if(!additions.length)break;
  closureRounds.push(additions);
  for(const candidate of additions)assign(candidate.cell,'neutron','interior-closure');
 }
 const nextClosure=step>=7&&faceNeighbors.length?interiorNeutronRound(k,assignments):[];
 const surfacePropagationAvailable=Boolean(edgeMeeting)&&faceNeighbors.length===2&&step>=7&&!nextClosure.length;
 const surfacePropagationVisible=surfacePropagationAvailable&&step>=8+closureRounds.length;
 const surfaceRays=surfacePropagationVisible?meetingSurfaceRays(k,edgeMeeting.point):[];
 for(const ray of surfaceRays)for(const candidate of ray.surfaceCells){
  const existing=assignments.find(a=>a.cell===candidate.cell);
  if(existing&&existing.role!=='neutron')throw Error(`Surface propagation conflicts with ${existing.role} on cell ${candidate.cell}`);
  assign(candidate.cell,'neutron','surface-propagation');
 }
 rays.push(...surfaceRays);
 const baseEdgeVisible=surfacePropagationVisible&&step>=9+closureRounds.length;
 const baseEdgeRays=[];
 if(baseEdgeVisible){
  const v2=surfaceRays[0].end,v4=surfaceRays[1].end,midpoint=v2.map((x,i)=>(x+v4[i])/2);
  const edge=cornerRay(k,v2,v4);
  for(const contact of edge.contacts)if(contact.interval[1]-contact.interval[0]>1e-9){
   const existing=assignments.find(a=>a.cell===contact.cell);
   if(existing&&existing.role!=='neutron')throw Error(`Base-edge propagation conflicts with ${existing.role} on cell ${contact.cell}`);
   assign(contact.cell,'neutron','base-edge-propagation');
  }
  for(const [id,start] of [['ray24',v2],['ray42',v4]]){
   baseEdgeRays.push({id,start:[...start],end:midpoint,length:k/2});
  }
 }
 const ray34Visible=baseEdgeVisible&&step>=10+closureRounds.length;
 const ray14Visible=ray34Visible&&step>=11+closureRounds.length;
 const ray12Visible=ray14Visible&&step>=12+closureRounds.length;
 const ray32PatternVisible=ray12Visible&&step>=13+closureRounds.length;
 let ray34=null,ray14=null,ray12=null,ray32Pattern=null;
 const edge32Assignments=[],edge32Predecessors=[];
 const edge34Assignments=[],edge34Predecessors=[],edge14Assignments=[],edge14Predecessors=[],edge12Assignments=[],edge12Predecessors=[];
 if(ray34Visible){
  function fillPatternRay(id,start,pattern,edgeAssignments,edgePredecessors,end=surfaceRays[1].end){
   const ray=cornerRay(k,start,end);
   const result=fillRayDiamonds(k,{...ray,id},pattern,assignments,assign);
   edgeAssignments.push(...result.edgeAssignments);edgePredecessors.push(...result.predecessors);
   return {...ray,id,contacts:result.contacts,diamonds:result.diamonds,blockedDiamonds:result.blocked};
  }
  ray34=fillPatternRay('ray34',firstRay.end,['proton','electron','neutron'],edge34Assignments,edge34Predecessors);
  rays.push(ray34);
  if(ray14Visible){
   ray14=fillPatternRay('ray14',apex,['electron','proton','neutron'],edge14Assignments,edge14Predecessors);
   rays.push(ray14);
  }
  if(ray12Visible){
   ray12=fillPatternRay('ray12',apex,['electron','proton','neutron'],edge12Assignments,edge12Predecessors,surfaceRays[0].end);
   rays.push(ray12);
  }
  if(ray32PatternVisible){
   ray32Pattern=fillPatternRay('ray32',firstRay.end,['proton','electron','neutron'],edge32Assignments,edge32Predecessors,ray32.end);
   // Ray32 was drawn in step 2; reuse it rather than overlaying a duplicate.
  }
 }
 const patternClosureRounds=[];
 if(ray32PatternVisible)for(let round=0;round<step-(13+closureRounds.length);round++){
  const additions=interiorNeutronRound(k,assignments);if(!additions.length)break;
  patternClosureRounds.push(additions);
  for(const candidate of additions)assign(candidate.cell,'neutron','post-pattern-closure');
 }
 const nextPatternClosure=ray32PatternVisible?interiorNeutronRound(k,assignments):[];
 const baseNeutronPassAvailable=ray32PatternVisible&&!nextPatternClosure.length;
 const baseNeutronPassVisible=baseNeutronPassAvailable&&step>=14+closureRounds.length+patternClosureRounds.length;
 const baseNeutronPass=baseNeutronPassVisible?{...cornerRay(k,surfaceRays[0].end,surfaceRays[1].end),id:'base-neutron-pass'}:null;
 if(baseNeutronPass)for(const contact of baseNeutronPass.contacts){
  const existing=assignments.find(a=>a.cell===contact.cell);
  if(existing&&existing.role!=='neutron')throw Error(`Base neutron pass conflicts with ${existing.role} on cell ${contact.cell}`);
  // Include vertex-only contacts: these are the octahedral filler gaps
  // omitted by the earlier positive-length edge sweep.
  assign(contact.cell,'neutron','base-neutron-pass');
 }
 const edgeVertexNeutrons=[];
 if(baseNeutronPassVisible){
  const corners=[apex,...[1,2,3].map(vertex=>apex.map((x,i)=>x+(i===0?k:i===vertex?-k:0)))],pending=new Map();
  for(const [a,b] of [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])for(const contact of cornerRay(k,corners[a],corners[b]).contacts){
   if(contact.interval[1]-contact.interval[0]>1e-9||assignments.some(role=>role.cell===contact.cell))continue;
   if(!pending.has(contact.cell))pending.set(contact.cell,{cell:contact.cell,contacts:[]});
   pending.get(contact.cell).contacts.push({edge:`${a+1}${b+1}`,interval:contact.interval});
  }
  edgeVertexNeutrons.push(...[...pending.values()].sort((a,b)=>a.cell-b.cell));
 }
 const edgeVertexFillAvailable=edgeVertexNeutrons.length>0;
 const edgeVertexFillVisible=edgeVertexFillAvailable&&step>=15+closureRounds.length+patternClosureRounds.length;
 if(edgeVertexFillVisible)for(const candidate of edgeVertexNeutrons)assign(candidate.cell,'neutron','edge-vertex-completion');
 const edgeClosureRounds=[];
 if(edgeVertexFillVisible)for(let round=0;round<step-(15+closureRounds.length+patternClosureRounds.length);round++){
  // Each round uses only faces assigned before that round.
  const additions=interiorNeutronRound(k,assignments);if(!additions.length)break;
  edgeClosureRounds.push(additions);
  for(const candidate of additions)assign(candidate.cell,'neutron','post-edge-closure');
 }
 const nextEdgeClosure=edgeVertexFillVisible?interiorNeutronRound(k,assignments):[];
 const faceMedianAvailable=baseNeutronPassVisible&&(!edgeVertexFillAvailable||edgeVertexFillVisible)&&!nextEdgeClosure.length;
 const firstMedianStep=15+closureRounds.length+patternClosureRounds.length+edgeClosureRounds.length+(edgeVertexFillAvailable?1:0);
 const median3To24Visible=faceMedianAvailable&&step>=firstMedianStep;
 const median1To24Visible=median3To24Visible&&step>firstMedianStep;
 const faceMedianRays=[],faceMedianAssignments=[];
 for(const [visible,source,pattern] of [[median3To24Visible,3,['proton','electron']],[median1To24Visible,1,['electron','proton']]])if(visible){
  const ray=faceMedianRay(k,source);let phase=0;
  for(const contact of ray.surfaceCells){
   const existing=assignments.find(a=>a.cell===contact.cell),expectedRole=pattern[phase%2],role=existing?.role??expectedRole;
   faceMedianAssignments.push({cell:contact.cell,ray:ray.id,role,expectedRole,previousRole:existing?.role??null});
   if(!existing)assign(contact.cell,role,'face-median-pattern');
   if(role===expectedRole)phase++;
  }
  faceMedianRays.push(ray);rays.push(ray);
 }
 const diamondGapPlan=median1To24Visible?surfaceDiamondGaps(k,assignments,faceMedianRays):{cells:[],witnesses:[]};
 const diamondGapAvailable=diamondGapPlan.cells.length>0;
 const diamondGapVisible=diamondGapAvailable&&step>=firstMedianStep+2;
 if(diamondGapVisible)for(const candidate of diamondGapPlan.cells)assign(candidate.cell,'neutron','surface-diamond-gap');
 const neutronBoundaryPlan=median1To24Visible&&(!diamondGapAvailable||diamondGapVisible)?surfaceNeutronBoundaryGaps(k,assignments,faceMedianRays):{cells:[],witnesses:[]};
 const neutronBoundaryAvailable=neutronBoundaryPlan.cells.length>0;
 const neutronBoundaryVisible=neutronBoundaryAvailable&&step>=firstMedianStep+2+(diamondGapAvailable?1:0);
 if(neutronBoundaryVisible)for(const candidate of neutronBoundaryPlan.cells)assign(candidate.cell,'neutron','surface-neutron-boundary');
 const identifiedSurfacePlan=median1To24Visible&&(!diamondGapAvailable||diamondGapVisible)&&(!neutronBoundaryAvailable||neutronBoundaryVisible)?identifiedSurfaceNeutrons(k,assignments):[];
 const identifiedSurfaceAvailable=identifiedSurfacePlan.length>0;
 const identifiedSurfaceVisible=identifiedSurfaceAvailable&&step>=firstMedianStep+2+(diamondGapAvailable?1:0)+(neutronBoundaryAvailable?1:0);
 if(identifiedSurfaceVisible)for(const candidate of identifiedSurfacePlan)assign(candidate.cell,'neutron','identified-surface-neutron');
 const f134DiamondPlan=identifiedSurfaceVisible?f134InteriorDiamonds(k,assignments):[];
 const f134DiamondAvailable=f134DiamondPlan.length>0;
 const f134DiamondVisible=f134DiamondAvailable&&step>=firstMedianStep+3+(diamondGapAvailable?1:0)+(neutronBoundaryAvailable?1:0);
 if(f134DiamondVisible)for(const pair of f134DiamondPlan)for(const member of [pair.domain,pair.codomain])assign(member.cell,member.role,'f134-interior-diamond');
 const f123DiamondPlan=f134DiamondVisible?f123InteriorDiamonds(k,assignments):[];
 const f123DiamondAvailable=f123DiamondPlan.length>0;
 const f123DiamondVisible=f123DiamondAvailable&&step>=firstMedianStep+4+(diamondGapAvailable?1:0)+(neutronBoundaryAvailable?1:0);
 if(f123DiamondVisible)for(const pair of f123DiamondPlan)for(const member of [pair.domain,pair.codomain])assign(member.cell,member.role,'f123-interior-diamond');
 const surfaceRemainderPlan=f123DiamondVisible?surfaceDiamondRemainders(k,assignments):[];
 const surfaceRemainderAvailable=surfaceRemainderPlan.length>0;
 const surfaceRemainderVisible=surfaceRemainderAvailable&&step>=firstMedianStep+5+(diamondGapAvailable?1:0)+(neutronBoundaryAvailable?1:0);
 if(surfaceRemainderVisible)for(const candidate of surfaceRemainderPlan)assign(candidate.cell,'neutron','surface-diamond-remainder');
 const remainingFacePlan=surfaceRemainderVisible?remainingFaceCompletion(k,assignments):{diamonds:[],neutrons:[]};
 const remainingFaceAvailable=remainingFacePlan.diamonds.length>0;
 const remainingFaceVisible=remainingFaceAvailable&&step>=firstMedianStep+6+(diamondGapAvailable?1:0)+(neutronBoundaryAvailable?1:0);
 if(remainingFaceVisible){
  for(const pair of remainingFacePlan.diamonds)for(const member of [pair.domain,pair.codomain])assign(member.cell,member.role,'remaining-face-diamond');
  for(const candidate of remainingFacePlan.neutrons)assign(candidate.cell,'neutron','remaining-face-neutron');
 }
 return {...setup,step,assignments,firstRay,rays,ray32,ray21,edgeMeeting,edgeFronts,faceNeighbors,counterpartsAvailable,neutronNeighbors,surfaceNeutronNeighbors,closureRounds,nextClosure,patternClosureRounds,nextPatternClosure,surfacePropagationAvailable,surfacePropagationVisible,surfaceRays,baseEdgeVisible,baseEdgeRays,ray34Visible,ray34,edge34Assignments,edge34Predecessors,ray14Visible,ray14,edge14Assignments,edge14Predecessors,ray12Visible,ray12,edge12Assignments,edge12Predecessors,ray32PatternVisible,ray32Pattern,edge32Assignments,edge32Predecessors,baseNeutronPassAvailable,baseNeutronPassVisible,baseNeutronPass,edgeVertexNeutrons,edgeVertexFillAvailable,edgeVertexFillVisible,edgeClosureRounds,nextEdgeClosure,faceMedianAvailable,median3To24Visible,median1To24Visible,faceMedianRays,faceMedianAssignments,diamondGapPlan,diamondGapAvailable,diamondGapVisible,neutronBoundaryPlan,neutronBoundaryAvailable,neutronBoundaryVisible,identifiedSurfacePlan,identifiedSurfaceAvailable,identifiedSurfaceVisible,f134DiamondPlan,f134DiamondAvailable,f134DiamondVisible,f123DiamondPlan,f123DiamondAvailable,f123DiamondVisible,surfaceRemainderPlan,surfaceRemainderAvailable,surfaceRemainderVisible,remainingFacePlan,remainingFaceAvailable,remainingFaceVisible};
}
