import {geometryBeltSurface} from './belt-geometry-layout.js';
import {buildParentCellulations} from './parent-cellulation.js';
const roles=['proton','neutron','electron'],tally=records=>{const result={proton:0,neutron:0,electron:0,total:0};for(const r of records)if(roles.includes(r.role)){result[r.role]++;result.total++;}return result;};
export function exposedParentFaces(proc){return buildParentCellulations(proc).flatMap(p=>p.faces.filter(f=>f.owners.length===1).map(f=>({...f,copy:p.copy,owner:f.owners[0],role:f.colorRole,face:f.indices.map(i=>p.vertices[i])})));}
const total=r=>({...r,total:r.proton+r.neutron+r.electron});
// Common structural convention: P/E are exposed native faces (E-tip overrides
// included); N is the count of whole octahedral fillers, in parents AND belt.
export function buildPneInventory(proc){
 const parents=buildParentCellulations(proc),rows=parents.map(p=>total({id:p.copy,label:p.copy==='original'?'Original parent':'Second parent',...tally(p.faces.filter(f=>f.owners.length===1).map(f=>({role:f.colorRole}))),neutron:p.counts.octahedra}));
 const parent=total({id:'parents-exposed',label:'Parents',...Object.fromEntries(roles.map(role=>[role,rows.reduce((s,r)=>s+r[role],0)])),scope:'P/E: exposed native faces. N: whole octahedral fillers. Uses the same cellulation convention as belt, not growth-rule colors.'});rows.push(parent);
 if(proc.beltSurface){const s=geometryBeltSurface(proc.beltSurface,proc.centralBeltAudit),belt=total({id:'belt-faces',label:'Belt',...tally(s.faces.map(f=>({role:f.colorRole}))),neutron:s.cellulation.counts.octahedra});rows.push(belt);rows.push(total({id:'combined',label:'Combined total',...Object.fromEntries(roles.map(role=>[role,parent[role]+belt[role]])),scope:'Exposed P/E faces and whole octahedral N fillers across parents and belt.'}));}
 return {rows,displayRows:rows.filter(r=>['parents-exposed','belt-faces','combined'].includes(r.id)),unassigned:0,neutronFillerCells:parent.neutron,exposedParentFaceCount:parents.reduce((s,p)=>s+p.counts.exposedFaces,0),scope:'Common native cellulation: P/E exposed faces; N whole octahedral fillers. Explicit E tips retained. Independent of selected growth rules and visibility masks.'};
}
