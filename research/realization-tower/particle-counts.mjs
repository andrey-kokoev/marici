import {cells} from './normal-ray-model.mjs';
const zero=()=>({proton:0,neutron:0,electron:0,total:0});
// Count each retained geometric body once PER sheet. The two rows are
// alternate readings of shared geometry and must not be summed.
export function retainedPolarityCounts(bodies){
 const counts={positive:zero(),negative:zero()},seen=new Set();
 for(const body of bodies){
  if(seen.has(body.id))continue;
  if(body.id===undefined||!body.polarityRoles||!['positive','negative'].every(sheet=>['proton','neutron','electron'].includes(body.polarityRoles[sheet])))throw Error('Complete body identity and both polarity roles required');
  seen.add(body.id);
  for(const sheet of ['positive','negative']){counts[sheet][body.polarityRoles[sheet]]++;counts[sheet].total++;}
 }
 return counts;
}
// Count assigned cells once. Surface means an exterior triangular face;
// edge-/vertex-only boundary contact is counted as interior filler.
export function particleCounts(k,assignments){
 const counts={surface:zero(),filler:zero(),total:zero()},seen=new Set();
 for(const {cell,role} of assignments){
  if(seen.has(cell)||!cells[cell]||!['proton','neutron','electron'].includes(role))continue;
  seen.add(cell);
  const surface=[0,1,2,3].some(i=>cells[cell].vertices.filter(p=>p[i]===(i===0?-5+k:2)).length===3);
  const row=counts[surface?'surface':'filler'];row[role]++;row.total++;counts.total[role]++;counts.total.total++;
 }
 return counts;
}
