// Process 3: independent, incremental reconstruction from geometric rules.
// No Process 2 state, cell-ID patches, target counts, or retroactive recoloring.
import {apex,seed,cells} from './normal-ray-model.mjs';
import {radialConstraints,collectiveCorePlan} from './radial-constraints.mjs';
import {edgeProbe,cornerRay,secondEdgeRay,exteriorFaceNeighbors} from './edge-ray-model.mjs';
const roles=new Set(['electron','proton','neutron']);
const shared=(a,b)=>a.filter(p=>b.some(q=>p.every((x,i)=>x===q[i])));
const center=vs=>vs[0].map((_,i)=>vs.reduce((sum,p)=>sum+p[i]/vs.length,0));

// Validate the complete batch against one snapshot before adding any member.
// In particular, N cannot be displaced to make a diamond fit.
export function commitAssignmentPlan(k,assignments,members,rule){
 const existing=new Map(assignments.map(a=>[a.cell,a.role])),pending=new Map(),conflicts=[];
 for(const member of members){
  const {cell,role}=member;
  if(!Number.isInteger(cell)||!cells[cell]||!roles.has(role)||cells[cell].vertices.some(p=>p[0]>-5+k)){
   conflicts.push({cell,role,reason:'Invalid role or cell outside the construction'});continue;
  }
  const prior=pending.get(cell)?.role??existing.get(cell);
  if(prior&&prior!==role)conflicts.push({cell,role,existingRole:prior,reason:'Existing assignment is immutable'});
  else if(!existing.has(cell))pending.set(cell,{cell,role});
 }
 if(conflicts.length)return {assignments,added:[],conflicts};
 const added=[...pending.values()].map(({cell,role})=>({id:`${role}-${cell}`,kind:'cell-role',cell,role,boundary:rule,point:center(cells[cell].vertices)}));
 return {assignments:[...assignments,...added],added,conflicts};
}
export function commitDiamondPlan(k,assignments,diamonds,rule){
 const conflicts=[];
 for(const {domain,codomain} of diamonds){
  if(!cells[domain.cell]||!cells[codomain.cell]||!['electron','proton'].includes(domain.role)||!['electron','proton'].includes(codomain.role)||domain.role===codomain.role||shared(cells[domain.cell].vertices,cells[codomain.cell].vertices).length!==3)
   conflicts.push({domain,codomain,reason:'A diamond requires opposite roles sharing a complete face'});
 }
 if(conflicts.length)return {assignments,added:[],conflicts};
 return commitAssignmentPlan(k,assignments,diamonds.flatMap(d=>[d.domain,d.codomain]),rule);
}
export const diamondStageTitles=Object.freeze([
 'E seed at V₁.',
 'Cast V₁ → V₃; establish the P corner.',
 'Cast V₃ → V₂; establish the N corner.',
 'Cast V₂ → V₁; return to the existing E.',
 'Complete the two corner diamonds atomically. Edge fronts and N closure are not yet implemented.',
 'Place P in the unique cell containing the tetrahedron center. Audit all four face-connected branches before labeling them.',
 'Trial central shell: leave the V₁ branch neighbor unresolved and place P on the other three branches. E is surface-only. Dashed paths are geometric guides, not particle assignments.',
 'Collective core trial: connect the P component to existing surface E/PE pairs through face-connected N corridors. No individual E partner is required for each filler P.',
]);
export function diamondConstruction(k,step){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 if(!Number.isInteger(step)||step<0||step>=diamondStageTitles.length)throw Error('Invalid Process 3 step');
 const probe=edgeProbe(k),state={k,step,probe,end:probe.end,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],history:[],conflicts:[]};
 function commit(rule,members,diamonds=null){
  const result=diamonds?commitDiamondPlan(k,state.assignments,diamonds,rule):commitAssignmentPlan(k,state.assignments,members,rule);
  state.history.push({rule,added:result.added.map(a=>a.cell),diamonds:diamonds??[],conflicts:result.conflicts});
  state.conflicts.push(...result.conflicts);state.assignments=result.assignments;
  if(diamonds&&!result.conflicts.length)state.diamonds.push(...diamonds);
 }
 commit('seed',[{cell:seed.id,role:'electron'}]);
 if(step>=1){
  state.firstRay={...cornerRay(k,apex,probe.point),id:'ray13'};
  // The k=1 degeneration is explicit: all corners share the E seed.
  commit('corner-v3',k===1?[]:[{cell:state.firstRay.cell,role:'proton'}]);
 }
 if(step>=2){
  const ray={...secondEdgeRay(k,1),id:'ray32'};state.rays.push(ray);
  commit('corner-v2',k===1?[]:[{cell:ray.cell,role:'neutron'}]);
 }
 if(step>=3){state.rays.push({...cornerRay(k,state.rays[0].end,apex),id:'ray21'});commit('return-v1',[{cell:seed.id,role:'electron'}]);}
 if(step>=4){
  const candidates=exteriorFaceNeighbors(k);
  const diamonds=candidates.map(n=>({source:n.role==='electron'?1:3,domain:{cell:n.corner,role:n.role},codomain:{cell:n.cell,role:n.role==='electron'?'proton':'electron'},sharedFace:n.sharedFace}));
  commit('corner-diamonds',[],diamonds);
  if(!state.conflicts.length)state.faceNeighbors=candidates;
 }
 if(step>=5){
  const radial=radialConstraints(k,state.assignments);
  if(radial.available&&radial.centralCell!==null)commit('radial-center',[{cell:radial.centralCell,role:'proton'}]);
 }
 if(step>=6){
  const radial=radialConstraints(k,state.assignments);
  if(radial.available&&radial.centralNeighbors.length===4&&radial.centralChannel)commit('central-shell-trial',radial.centralNeighbors.filter(n=>n.cell!==radial.centralChannel.cell).map(n=>({cell:n.cell,role:'proton'})));
 }
 if(step>=7){const plan=collectiveCorePlan(k,state.assignments);if(plan.members.length)commit('collective-core-n-corridors',plan.members);}
 state.collectiveCore=collectiveCorePlan(k,state.assignments);
 state.radial=radialConstraints(k,state.assignments);
 state.canAdvance=(step<4||(step===4&&state.radial.available&&state.radial.centralCell!==null)||(step===5&&state.radial.available&&state.radial.centralNeighbors.length===4&&Boolean(state.radial.centralChannel))||(step===6&&state.collectiveCore.members.length>0))&&!state.conflicts.length;
 if(step===4&&state.canAdvance&&state.assignments.some(a=>a.cell===state.radial.centralCell&&a.role!=='proton'))state.canAdvance=false;
 state.summary=`Step ${step} — ${diamondStageTitles[step]}${k===1?' At k=1 all corners coincide; the seed stays E.':''}${state.conflicts.length?' Placement blocked: existing roles were preserved.':''}`;
 if(step>=5&&state.radial.status==='branch-orientation-ambiguous')state.summary=`Step ${step} — Central P established. ${state.radial.orientationCount} equally short four-vertex branch orientations exist; no branch roles guessed.`;
 if(step>=5&&!state.radial.available)state.summary=`Step ${step} — The center does not identify a distinct single tetrahedron at k=${k}; an octahedral or degenerate-center rule is needed.`;
 state.connectionGuides=step>=7?state.collectiveCore.routes.map(c=>({...c,pathStatus:'assigned-trial',roleContinuityVerified:c.established,points:c.path.map(id=>center(cells[id].vertices))})):step>=6?state.radial.connections.map(c=>({...c,points:c.path.map(id=>center(cells[id].vertices))})):[];
 state.foundationComplete=step>=4&&!state.conflicts.length;
 return state;
}
