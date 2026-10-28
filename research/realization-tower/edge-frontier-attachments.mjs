// Trace the next attachment dependencies without admitting new cells or roles.
import {cells} from './normal-ray-model.mjs';
import {edgeProcedure,interiorNeutronRound} from './edge-ray-model.mjs';
import {auditEdgePairSymmetry,exchangeEP} from './edge-pair-symmetry.mjs';
import {assembleComponents} from '../strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const same=(a,b)=>a.every((x,i)=>x===b[i]);
const index=new Map(cells.map(c=>[key(c.vertices),c.id]));
const groups=assembleComponents().groups;
export function auditFrontierAttachments(k,branch=1){
 const symmetry=auditEdgePairSymmetry(k,branch),state=edgeProcedure(k,symmetry.terminalStep,branch);
 const roles=new Map(state.assignments.map(a=>[a.cell,a.role]));
 const region=cells.filter(c=>c.vertices.every(v=>v[0]<=k-5));
 const adjacency=new Map(region.map(c=>[c.id,region.filter(d=>d.id!==c.id&&d.vertices.filter(p=>c.vertices.some(q=>same(p,q))).length===3).map(d=>d.id)]));
 const mirror=id=>index.get(key(cells[id].vertices.map(p=>exchangeEP(k,p))));
 const exterior=id=>[0,1,2,3].filter(i=>cells[id].vertices.filter(v=>v[i]===(i===0?k-5:2)).length===3);
 const describe=id=>({cell:id,mirrorCell:mirror(id),role:roles.get(id)??null,exteriorFaces:exterior(id),assignedFaceNeighbors:adjacency.get(id).filter(n=>roles.has(n)).map(n=>({cell:n,role:roles.get(n)})),unassignedFaceNeighbors:adjacency.get(id).filter(n=>!roles.has(n))});
 const frontier=symmetry.segments.filter(s=>s.role===null).map(s=>({segment:s.segment,...describe(s.cell),missingSupports:s.faceNeighbors.filter(n=>n.role===null).map(n=>describe(n.cell))}));
 const required=new Set(frontier.flatMap(f=>f.missingSupports.map(s=>s.cell)));
 const dependencyGroups=groups.filter(g=>g.children.some(id=>required.has(id))).map(g=>{
  const vertices=[...new Map(g.children.flatMap(id=>cells[id].vertices).map(v=>[v.join(','),v])).values()];
  const assignedEdgeContacts=[...roles].filter(([id])=>!g.children.includes(id)).map(([cell,role])=>({cell,role,edge:cells[cell].vertices.filter(p=>vertices.some(q=>same(p,q)))})).filter(c=>c.edge.length===2&&c.edge[0].reduce((s,x,i)=>s+(x-c.edge[1][i])**2,0)===2);
  const center=vertices[0].map((_,i)=>vertices.reduce((s,p)=>s+p[i]/vertices.length,0));
  const pairedOppositeEdges=assignedEdgeContacts.length===2&&center.every((x,i)=>Math.abs(assignedEdgeContacts.flatMap(c=>c.edge).reduce((s,p)=>s+p[i]/4,0)-x)<1e-9);
  return {group:g.id,cells:g.children.map(describe),unassigned:g.children.every(id=>!roles.has(id)),assignedExternalFaceContacts:g.children.flatMap(id=>adjacency.get(id).filter(n=>!g.children.includes(n)&&roles.has(n)).map(n=>({from:id,to:n,role:roles.get(n)}))),assignedEdgeContacts,pairedOppositeEdges};
 });
 const eligible=interiorNeutronRound(k,state.assignments);
 if(eligible.length)throw Error('Attachment audit must start after closure reaches a fixed point');
 for(const f of frontier){
  const other=frontier.find(g=>g.cell===f.mirrorCell);
  if(!other)throw Error('Unassigned frontier is not paired by symmetry');
  const mapped=f.missingSupports.map(s=>mirror(s.cell)).sort((a,b)=>a-b);
  if(JSON.stringify(mapped)!==JSON.stringify(other.missingSupports.map(s=>s.cell).sort((a,b)=>a-b)))throw Error('Missing supports do not transform together');
 }
 return {k,branch,step:symmetry.terminalStep,frontier,dependencyGroups,eligibleInteriorCells:eligible.map(c=>c.cell),newAssignments:[]};
}
