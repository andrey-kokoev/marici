import {cells} from './normal-ray-model.mjs';
const shared=(a,b)=>a.filter(p=>b.some(q=>p.every((x,i)=>x===q[i])));
const charged=role=>role==='electron'||role==='proton';

// The repeating unit is a face-sharing domain/codomain diamond, then N.
// The predecessor at the entry vertex is part of that unit, not an extra
// particle inserted after assigning a separate domain to an edge segment.
export function fillRayDiamonds(k,ray,pattern,assignments,assign){
 const contacts=ray.contacts.filter(c=>c.interval[1]-c.interval[0]>1e-9).sort((a,b)=>a.interval[0]-b.interval[0]);
 const edgeAssignments=[],predecessors=[],diamonds=[],blocked=[];
 const [domain,codomain]=pattern;let awaitingWitness=false;
 function sameColorContact(cell,role,other){
  if(role!==other.role||!charged(role)||cell===other.cell)return false;
  const a=cells[cell].vertices,b=cells[other.cell].vertices;
  if(shared(a,b).length!==2)return false;
  return [0,1,2,3].some(i=>{
   const value=i===0?-5+k:2;
   return a.filter(p=>p[i]===value).length===3&&b.filter(p=>p[i]===value).length===3;
  });
 }
 contacts.forEach((contact,index)=>{
  const cell=contact.cell,existing=assignments.find(a=>a.cell===cell);
  const expectedRole=index===0?domain:awaitingWitness?'neutron':codomain;
  if(index===0){
   edgeAssignments.push({cell,index,role:existing?.role??domain,expectedRole,previousRole:existing?.role??null});return;
  }
  if(awaitingWitness){
   if(!existing)assign(cell,'neutron',`${ray.id}-witness`);
   if(!existing||existing.role==='neutron')awaitingWitness=false;
  }else if(!existing){
   const candidates=ray.contacts.filter(c=>c.cell!==cell&&Math.abs(c.interval[0]-contact.interval[0])<1e-9&&Math.abs(c.interval[1]-contact.interval[0])<1e-9).map(c=>({cell:c.cell,sharedFace:shared(cells[c.cell].vertices,cells[cell].vertices)})).filter(c=>c.sharedFace.length===3);
   if(candidates.length===1){
    const predecessor=candidates[0],prior=assignments.find(a=>a.cell===predecessor.cell);
    const pair=[{cell:predecessor.cell,role:domain},{cell,role:codomain}];
    const conflicts=assignments.filter(a=>pair.some(p=>sameColorContact(p.cell,p.role,a))).map(a=>a.cell);
    if((!prior||prior.role===domain)&&!conflicts.length){
     // Validate both members before making either assignment.
     if(!prior){assign(predecessor.cell,domain,`${ray.id}-predecessor`);predecessors.push({...predecessor,[codomain]:cell});}
     assign(cell,codomain,`${ray.id}-diamond`);
     diamonds.push({domain:predecessor.cell,codomain:cell,sharedFace:predecessor.sharedFace});awaitingWitness=true;
    }else blocked.push({cell,predecessor:predecessor.cell,existingRole:prior?.role??null,conflicts});
   }
  }else if(existing.role===codomain){
   // Existing roles remain constraints; a previously placed codomain is
   // followed by its witness, rather than recolored to restart the sequence.
   awaitingWitness=true;
  }
  edgeAssignments.push({cell,index,role:assignments.find(a=>a.cell===cell)?.role??null,expectedRole,previousRole:existing?.role??null});
 });
 return {contacts,edgeAssignments,predecessors,diamonds,blocked};
}
