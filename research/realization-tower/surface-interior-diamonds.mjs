import {cells} from './normal-ray-model.mjs';
const shared=(a,b)=>a.filter(p=>b.some(q=>p.every((x,i)=>x===q[i])));

// The selected k=7 continuation on F134/F123: fourth layer from V3 and V1.
// Polarity continues the respective vertex orientation; N alone does not fix it.
function interiorDiamonds(k,assignments,faceCoordinate){
 if(k!==7)return [];
 const roles=new Map(assignments.map(a=>[a.cell,a.role]));
 const faces=cells.map(c=>({cell:c.id,face:c.vertices.filter(p=>p[faceCoordinate]===2)})).filter(c=>c.face.length===3);
 const plan=[];
 for(const [source,coordinate,domainRole,codomainRole] of [[3,2,'proton','electron'],[1,0,'electron','proton']]){
  const empty=faces.filter(c=>!roles.has(c.cell)&&Math.min(...c.face.map(p=>p[coordinate]))===-2),pairs=[];
  for(let i=0;i<empty.length;i++)for(let j=i+1;j<empty.length;j++){
   const a=empty[i],b=empty[j],sharedFace=shared(cells[a.cell].vertices,cells[b.cell].vertices);
   if(sharedFace.length!==3||shared(a.face,b.face).length!==2)continue;
   const ordered=[a,b].sort((x,y)=>x.face.reduce((n,p)=>n+p[coordinate],0)-y.face.reduce((n,p)=>n+p[coordinate],0));
   const domain={cell:ordered[0].cell,role:domainRole},codomain={cell:ordered[1].cell,role:codomainRole};
   if([domain,codomain].some(member=>faces.some(f=>roles.get(f.cell)===member.role&&shared(f.face,faces.find(g=>g.cell===member.cell).face).length===2)))continue;
   pairs.push({source,coordinate,faceCoordinate,domain,codomain,sharedFace});
  }
  // Require an unambiguous, fully empty pair at both selected locations.
  if(pairs.length!==1)return [];
  plan.push(pairs[0]);
 }
 return plan;
}
// Complete the two remaining face-sharing slots on each opposite face.
export function remainingFaceCompletion(k,assignments){
 const empty={diamonds:[],neutrons:[]};if(k!==7)return empty;
 const roles=new Map(assignments.map(a=>[a.cell,a.role])),diamonds=[];
 for(const [faceCoordinate,sourceCoordinate,domainRole,codomainRole] of [[0,2,'proton','electron'],[2,0,'electron','proton']]){
  const faces=cells.map(c=>({cell:c.id,face:c.vertices.filter(p=>p[faceCoordinate]===2)})).filter(c=>c.face.length===3);
  const unassigned=faces.filter(c=>!roles.has(c.cell)),pairs=[];
  for(let i=0;i<unassigned.length;i++)for(let j=i+1;j<unassigned.length;j++){
   const a=unassigned[i],b=unassigned[j],sharedFace=shared(cells[a.cell].vertices,cells[b.cell].vertices);
   if(sharedFace.length!==3||shared(a.face,b.face).length!==2)continue;
   const ordered=[a,b].sort((x,y)=>x.face.reduce((n,p)=>n+p[sourceCoordinate],0)-y.face.reduce((n,p)=>n+p[sourceCoordinate],0));
   const domain={cell:ordered[0].cell,role:domainRole},codomain={cell:ordered[1].cell,role:codomainRole};
   if([domain,codomain].some(member=>faces.some(f=>roles.get(f.cell)===member.role&&shared(f.face,faces.find(g=>g.cell===member.cell).face).length===2)))return empty;
   pairs.push({faceCoordinate,sourceCoordinate,domain,codomain,sharedFace});
  }
  if(pairs.length!==2||new Set(pairs.flatMap(p=>[p.domain.cell,p.codomain.cell])).size!==4)return empty;
  diamonds.push(...pairs);
 }
 const planned=diamonds.flatMap(p=>[p.domain,p.codomain]);
 return {diamonds,neutrons:surfaceDiamondRemainders(k,[...assignments,...planned],[0,2])};
}
export const f134InteriorDiamonds=(k,assignments)=>interiorDiamonds(k,assignments,1);
export const f123InteriorDiamonds=(k,assignments)=>interiorDiamonds(k,assignments,3);

// Isolated triangular gaps left between the completed diamonds and N boundary.
export function surfaceDiamondRemainders(k,assignments,coordinates=[1,3]){
 if(k!==7)return [];
 const roles=new Map(assignments.map(a=>[a.cell,a.role])),pending=new Map();
 for(const coordinate of coordinates){
  const faces=cells.map(c=>({cell:c.id,face:c.vertices.filter(p=>p[coordinate]===2)})).filter(c=>c.face.length===3);
  for(const c of faces){
   if(roles.has(c.cell))continue;
   const supports=faces.filter(d=>d.cell!==c.cell&&shared(c.face,d.face).length===2).map(d=>({cell:d.cell,role:roles.get(d.cell)}));
   if(supports.length===3&&supports.filter(s=>s.role==='neutron').length===2&&supports.filter(s=>s.role==='electron'||s.role==='proton').length===1)pending.set(c.cell,{cell:c.cell,coordinate,supports});
  }
 }
 return [...pending.values()].sort((a,b)=>a.cell-b.cell);
}

