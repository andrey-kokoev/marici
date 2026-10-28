// First fix the equivalence contract; distinguish full labelled/provenance
// states from explicitly weaker geometric projections. No physical selector.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const inputs={wiring:'research/strominger/results/su32-global-reference-wiring-v1/verification.json',
 trace:'research/strominger/results/su32-fixed-reading-trace-v1/verification.json',
 fixture:'research/strominger/results/su32-hopf-tests-v1/fixture.json'};
const hash=x=>createHash('sha256').update(x).digest('hex'),docs={};
for(const [name,path] of Object.entries(inputs)){
 docs[name]=JSON.parse(await fs.readFile(path,'utf8'));
 for(const [p,h] of Object.entries(docs[name].sourceHashes))assert.equal(hash(await fs.readFile(p)),h,`Stale input: ${p}`);
}
const {wiring,trace,fixture}=docs,copy=x=>structuredClone(x),base=wiring.witness.plan;
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const byShape=new Map(fixture.cells.map(c=>[shape(c.vertices),c.id]));
const centre=[0,0,0,0];let count=0;
for(const c of fixture.cells)for(const v of c.vertices){count++;v.forEach((x,i)=>centre[i]+=x);}
centre.forEach((_,i)=>centre[i]/=count);
// Verify the full-hull octahedron used in the point-group completeness argument.
const axes=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
const projected=fixture.cells.flatMap(c=>c.vertices).map(v=>axes.map(a=>a.reduce((s,x,i)=>s+x*(v[i]-centre[i])/2,0)));
const radius=Math.max(...projected.map(p=>p.reduce((s,x)=>s+Math.abs(x),0)));
for(let i=0;i<3;i++)for(const sign of [-1,1])assert(projected.some(p=>p.every((x,j)=>x===(i===j?sign*radius:0))));
assert(projected.every(p=>p.reduce((s,x)=>s+Math.abs(x),0)<=radius));
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const group=[];
for(const permutation of permutations([0,1,2,3]))for(const sign of [1,-1]){
 const point=v=>centre.map((c,i)=>c+sign*(v[permutation[i]]-centre[permutation[i]]));
 const map=Object.fromEntries(fixture.cells.map(c=>[c.id,byShape.get(shape(c.vertices.map(point)))]));
 assert(Object.values(map).every(Boolean));assert.equal(new Set(Object.values(map)).size,51);
 const faces=Object.fromEntries(fixture.interfaces.map(f=>[f.id,shape(f.id.split('|').map(v=>point(v.split(',').map(Number))))]));
 const byFace=new Map(fixture.interfaces.map(f=>[f.id,f]));
 for(const f of fixture.interfaces){const target=byFace.get(faces[f.id]);assert(target);
  assert.deepEqual(target.ports.map(p=>p.split('@')[0]).sort(),f.ports.map(p=>map[p.split('@')[0]]).sort());}
 for(const c of fixture.cells){const target=fixture.cells.find(n=>n.id===map[c.id]);
  assert.equal(target.role,sign===1?c.role:({proton:'electron',electron:'proton',neutron:'neutron'})[c.role]);}
 group.push({id:(sign===1?'+':'-')+permutation.join(''),permutation,sign,map,faces});
}
const mapKey=g=>JSON.stringify(fixture.cells.map(c=>g.map[c.id]));
const groupKeys=new Set(group.map(mapKey));assert.equal(groupKeys.size,48);
for(const a of group)for(const b of group)assert(groupKeys.has(JSON.stringify(fixture.cells.map(c=>a.map[b.map[c.id]]))));
const identity=group.find(g=>fixture.cells.every(c=>g.map[c.id]===c.id));assert(identity);
const between=(a,b)=>fixture.interfaces.filter(f=>f.ports.some(p=>p.split('@')[0]===a)&&f.ports.some(p=>p.split('@')[0]===b));
// Reconstruct all four already-fixed plans from the saved complete covers.
// No new paths or wiring choices are selected in this symmetry audit.
const plans=trace.middleAssignments.map(cover=>{
 const plan=copy(base);plan.cover=cover.index;
 const nodes=new Map(plan.nodes.map(n=>[n.cell,n]));
 plan.channels=cover.routes.map(r=>({channel:r.channel,members:copy(r.members)}));
 plan.bridges=[];
 for(const r of cover.routes)for(const [source,target] of [[r.sourceP,r.targetE],[r.sourceE,r.targetP]]){
  const members=r.members.filter(m=>between(source,m).length&&between(m,target).length);assert.equal(members.length,1);
  plan.bridges.push({channel:r.channel,source,middle:members[0],target,kind:'peripheral',records:copy(nodes.get(source).records)});
 }
 plan.bridges.push(...copy(base.bridges.filter(b=>b.kind==='central-comparison-context')));
 for(const n of plan.nodes)if(n.layer===5)n.records=[...new Set(plan.bridges.filter(b=>b.middle===n.cell).flatMap(b=>b.records))].sort();
 plan.edges=copy(base.edges.filter(e=>nodes.get(e.from).layer!==4&&nodes.get(e.from).layer!==5));
 for(const bridge of plan.bridges)for(const [from,to] of [[bridge.source,bridge.middle],[bridge.middle,bridge.target]]){
  const faces=between(from,to);assert.equal(faces.length,1);const face=faces[0];
  plan.edges.push({face:face.id,from,to,fromPort:from+'@'+face.id,toPort:to+'@'+face.id,records:copy(bridge.records)});
 }
 return plan;
});
assert.deepEqual(plans.find(p=>p.cover===base.cover),base);
const candidates=wiring.localizedSurvivors.map((placement,i)=>({id:i,plan:plans.find(p=>p.cover===placement.cover),placement}));
assert.equal(candidates.length,16);
const endFixed=g=>g.map[base.entry]===base.entry&&g.map[base.exit]===base.exit;
const endSetFixed=g=>[base.entry,base.exit].includes(g.map[base.entry])&&[base.entry,base.exit].includes(g.map[base.exit]);
const refs=base.boundaryViews.entry.referenceCells;
const recordsFixed=g=>Object.values(refs).every(cell=>g.map[cell]===cell);
function renaming(g){
 const view=g.map[base.entry]===base.entry?base.boundaryViews.entry:base.boundaryViews.exit;
 return Object.fromEntries(Object.entries(refs).map(([label,cell])=>{
  const local=Object.keys(view.referenceCells).find(k=>view.referenceCells[k]===g.map[cell]);assert(local);
  return [label,view.localToRecordId[local]];
 }));
}
function tree(node,g,rename){
 return {kind:node.kind,at:g.map[node.at],records:Object.entries(node.records).map(([k,v])=>[rename[k],g.map[v.referenceCell]]).sort(),
  ...(node.children?{children:node.children.map(c=>tree(c,g,rename))}:{})};
}
const core=base.retainedCentralComparisons;
const treeKey=(g,rename)=>JSON.stringify([tree(core.byE,g,rename),tree(core.byP,g,rename)]);
const unchanged=Object.fromEntries(Object.keys(refs).map(k=>[k,k]));
const orderedTyped=group.filter(g=>endFixed(g)&&g.sign===1);
const orderedHistoryFixed=orderedTyped.filter(g=>treeKey(g,renaming(g))===treeKey(identity,unchanged));
const strict=orderedTyped.filter(g=>recordsFixed(g)&&treeKey(g,unchanged)===treeKey(identity,unchanged));
// The key below deliberately projects away payloads and ordered constructor
// histories. Its use outside the strict stabilizer is labelled as relaxation.
function key(candidate,g,allowRename){
 const rename=allowRename?renaming(g):unchanged,plan=candidate.plan;
 const reversed=g.map[plan.entry]===base.exit;
 const nodes=plan.nodes.map(n=>[g.map[n.cell],n.records.map(k=>rename[k]).sort()]).sort();
 const edges=plan.edges.map(e=>[g.map[reversed?e.to:e.from],g.map[reversed?e.from:e.to],e.records.map(k=>rename[k]).sort()]).sort();
 const placements=candidate.placement.placements.map(p=>{
  const members=plan.channels.find(c=>c.channel===p.channel).members.map(c=>g.map[c]).sort();
  return [members,g.map[p.at],p.pair.map(k=>rename[k]).sort()];
 }).sort();
 return JSON.stringify({nodes,edges,placements});
}
const lookup=new Map(candidates.map(c=>[key(c,identity,false),c.id]));assert.equal(lookup.size,16);
const cellCentres=new Map(fixture.cells.map(c=>[c.id,[0,1,2,3].map(i=>c.vertices.reduce((s,v)=>s+v[i],0)/c.vertices.length)]));
function splitTipDistances(candidate){
 const split=candidate.plan.channels.filter(c=>c.members.length===2&&c.members.every(id=>candidate.plan.nodes.find(n=>n.cell===id).records.length));
 assert.equal(split.length,1);
 const tip=candidate.placement.placements.find(p=>p.channel===split[0].channel).at;
 const pairSites=candidate.placement.placements.filter(p=>p.pair[0][0]===p.pair[1][0]);assert.equal(pairSites.length,2);
 return pairSites.map(p=>cellCentres.get(tip).reduce((s,x,i)=>s+(x-cellCentres.get(p.at)[i])**2,0)).sort((a,b)=>a-b);
}
function classify(name,subgroup,allowRename,contract){
 const action=subgroup.map(g=>({symmetry:g.id,images:candidates.map(c=>{
  const image=lookup.get(key(c,g,allowRename));assert.notEqual(image,undefined,`Family not closed under ${name}/${g.id}`);return image;
 })}));
 for(const row of action)assert.equal(new Set(row.images).size,16,'Action must permute candidates');
 for(const a of subgroup)for(const b of subgroup){
  const composedKey=JSON.stringify(fixture.cells.map(c=>a.map[b.map[c.id]]));
  const composed=subgroup.find(g=>mapKey(g)===composedKey);assert(composed,'Subgroup not closed');
  const ar=action.find(r=>r.symmetry===a.id),br=action.find(r=>r.symmetry===b.id),cr=action.find(r=>r.symmetry===composed.id);
  assert.deepEqual(br.images.map(id=>ar.images[id]),cr.images,'Induced action violates composition');
 }
 const remaining=new Set(candidates.map(c=>c.id)),orbits=[];
 while(remaining.size){const first=remaining.values().next().value;
  const orbit=[...new Set(action.map(a=>a.images[first]))].sort((a,b)=>a-b);
  for(const id of orbit)remaining.delete(id);
  orbits.push({members:orbit,representative:copy(candidates[first].placement),
   invariantSummaries:orbit.map(id=>{const c=candidates[id];return {id,cover:c.plan.cover,
    splitTipToPPandEESquaredDistances:splitTipDistances(c),
    inactiveTip:c.plan.nodes.find(n=>!n.records.length).cell};})});
 }
 return {name,contract,groupSize:subgroup.length,symmetries:subgroup.map(g=>g.id),orbitCount:orbits.length,
  orbitSizes:orbits.map(o=>o.members.length),kernel:action.filter(a=>a.images.every((id,i)=>id===i)).map(a=>a.symmetry),orbits,action};
}
const classifications=[
 classify('fixed-boundary-records-and-provenance',strict,false,'Both ends individually fixed; each attached record identity fixed; full ordered central provenance fixed. This is the primary equivalence contract.'),
 classify('ordered-boundary-role-preserving-shapes',orderedTyped,true,'Diagnostic only: discard payload identity/value and ordered provenance, allow induced record-name permutation; keep ends ordered and geometric P/E roles.'),
 classify('ordered-boundary-PE-dual-shapes',group.filter(endFixed),true,'Further diagnostic relaxation: allow global P/E geometric duality. Not a native equivalence claim.'),
 classify('unoriented-boundary-PE-dual-shapes',group.filter(endSetFixed),true,'Further diagnostic relaxation: allow endpoint exchange and normalize edge direction by reversal. Not admitted in the primary contract.')];
assert.equal(strict.length,1);assert.equal(classifications[0].orbitCount,16);
const coarse=classifications[3];
assert.equal(coarse.orbitCount,2);
for(const orbit of coarse.orbits)assert.equal(new Set(orbit.members.map(id=>JSON.stringify(splitTipDistances(candidates[id])))).size,1);
assert.deepEqual(coarse.orbits.map(o=>splitTipDistances(candidates[o.members[0]])).sort(),[[2,10],[2,2]].sort());
const movedRecord=orderedTyped.find(g=>!recordsFixed(g));assert(movedRecord);
const changedOrder=orderedTyped.find(g=>!orderedHistoryFixed.includes(g));assert(changedOrder);
const sources=[...Object.values(inputs),'research/strominger/pe-symmetric-sector.mjs','research/strominger/checkers/check_su32_global_wiring_symmetry.mjs'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=hash(await fs.readFile(p));
const report={schema:'su32.global-wiring-symmetry-audit.v1',passed:true,carrierIsometries:group.length,
 hullCheck:{orthonormalAxes:axes.map(a=>a.map(x=>x/2)),radius,extremePointsPresent:6,allCarrierVerticesInside:true},
 residualInvariant:'Squared distances from the selected occurrence of the paired-tip channel with BOTH members active to the P/P and E/E pair sites: unordered [2,10] versus [2,2]. These distinguish the two most-relaxed geometric orbits.',
 geometricGroup:'q maps to centre + sign * coordinatePermutation(q-centre): 24 permutations times central inversion. Every cell and all 104 shared faces checked, with group closure.',
 completenessArgument:'The carrier convex hull is a regular octahedron in the sum-zero tangent space; its full Euclidean point group has order 48. The 48 distinct verified transformations exhaust it. This does not enumerate arbitrary nongeometric graph automorphisms.',
 orderedRolePreservingBoundarySymmetries:orderedTyped.length,
 orderedProvenanceStabilizerAfterForgettingPayloads:orderedHistoryFixed.map(g=>g.id),
 classifications,
 refusalWitnesses:{movesFixedReference:{symmetry:movedRecord.id,referenceImages:Object.fromEntries(Object.entries(refs).map(([k,c])=>[k,{from:c,to:movedRecord.map[c]}]))},
  changesOrderedHistory:{symmetry:changedOrder.id,original:JSON.parse(treeKey(identity,unchanged)),transformed:JSON.parse(treeKey(changedOrder,renaming(changedOrder))) }},
 conclusion:'All 16 localized candidates are inequivalent under the fixed labelled boundary and retained ordered provenance. Coarser shape orbits require explicitly dropping distinctions and/or allowing duality/reversal.',
 limits:['Only this fixed reading, binding, four covers and 16 localized survivors are classified.',
  'The projected family is closed under the reported relaxed geometric actions; full provenance-bearing packets need not be.',
  'No payloads, original logs or constructor histories were erased from stored plans.',
  'An orbit classification is not a native selection law or proof of physical equivalence.'],sourceHashes};
const dir='research/strominger/results/su32-global-wiring-symmetry-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,refusalWitnesses:undefined,sourceHashes:undefined,
 classifications:classifications.map(({orbits,action,...rest})=>rest)},null,2));
