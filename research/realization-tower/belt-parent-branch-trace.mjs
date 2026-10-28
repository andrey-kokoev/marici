import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {analyzeSeamLattice} from './seam-lattice.mjs';
// Trace existing admission witnesses only. Reachability labels do not assign
// flux weights, independent fibers, or identify growth rounds with dynamics.
export function traceBeltParentBranches(){
 const model=buildFoldedFibration(),seam=analyzeSeamLattice(model.occurrences),owners=new Map(model.occurrences.map(o=>[o.id,o]));
 const parents=[['original',model.back],['clone',model.outward]].map(([copy,traversal])=>{
  const roots=traversal.rounds[2],ancestry=new Map(roots.map((id,i)=>[id,new Set([i])]));
  for(const a of traversal.admissions){if(ancestry.has(a.body))continue;ancestry.set(a.body,new Set(a.witnesses.flatMap(w=>[...(ancestry.get(w.parent)??[])])));}
  const boundary=seam.pairs.map(pair=>{const owner=pair.cells.find(id=>owners.get(id).copy===copy);return {seamPair:pair.id,owner,rootIndices:[...ancestry.get(owner)].sort(),rootIds:[...ancestry.get(owner)].sort().map(i=>roots[i])};});
  const rounds=traversal.rounds.map((ids,round)=>({round,ownParentBodies:ids.filter(id=>owners.get(id).copy===copy)}));
  const earlyWitnesses=traversal.admissions.filter(a=>a.round<=3).map(a=>({...a,roots:[...ancestry.get(a.body)].sort()}));
  return {copy,endpoint:traversal.rounds[0][0],firstMediator:traversal.rounds[1],candidateRoots:roots.map((id,index)=>({index,id,sourceGeometry:owners.get(id).sourceGeometry,sourceParticleRole:owners.get(id).role,reachableSeamFaces:boundary.filter(p=>p.rootIndices.includes(index)).length})),earlyWitnesses,rounds,boundary,rootMultiplicityHistogram:boundary.reduce((a,p)=>(a[p.rootIndices.length]=(a[p.rootIndices.length]??0)+1,a),{}),disjointBoundaryPartition:boundary.every(p=>p.rootIndices.length===1)};
 });
 const crossings=Object.fromEntries([['outward',model.outward],['return',model.back]].map(([name,t])=>[name,t.admissions.flatMap(a=>a.witnesses.filter(w=>owners.get(w.parent).copy!==owners.get(a.body).copy).map(w=>({from:w.parent,to:a.body,round:a.round,face:w.face,seamPair:seam.pairs.find(p=>p.cells.includes(w.parent)&&p.cells.includes(a.body)).id})))]));
 return {status:'four-early-roots-overlap-at-boundary',scope:'Exact ancestry in existing whole-face admission traversals, not a physical flux or fiber decomposition.',parents,crossings,findings:['Each parent endpoint reaches one mediator, then four cells: one source-role electron and three source-role protons.','The four roots do not give disjoint geometric branches: their descendants merge in the next round. This does not decide fiber independence.','Every seam face has ancestry from at least two roots; no face has a unique root assignment.','The common root reaches all 49 seam faces; each of the other three reaches 36.','Outward and return traversals cross all 49 seam faces in opposite directions.','No four-star boundary map or fiber decomposition follows from these overlapping reachability sets.'],attachment:null};
}
