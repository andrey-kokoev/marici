import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {lattice,faces,nodeIds,centralCellId} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>j!==i)).map(p=>[x,...p])):[[]];
const key=a=>a.join(','),cellKey=addresses=>addresses.map(key).sort().join('|');
const nodes=lattice.nodes,items=lattice.assembly.items,cells=lattice.cells;
const lookup=new Map(nodes.map((n,id)=>[key(n.address),id]));
const itemVertices=items.map(item=>[...new Set(item.children.flatMap(id=>cells[id]))]);
const itemKey=(ids,item)=>item.layer+':'+item.kind+':'+cellKey(ids.map(id=>nodes[id].address));
const itemSet=new Set(items.map((item,i)=>itemKey(itemVertices[i],item)));
const cellSet=new Set(cells.map(cell=>cellKey(cell.map(id=>nodes[id].address))));
const primitiveEdges=new Set(lattice.edges.filter(([a,b])=>nodes[a].address.reduce((s,x,i)=>s+(x-nodes[b].address[i])**2,0)===2).map(e=>[...e].sort((a,b)=>a-b).join(',')));
const faceIncidence=new Map();
cells.forEach((cell,id)=>{for(const f of faces){const k=f.map(i=>cell[i]).sort((a,b)=>a-b).join(',');if(!faceIncidence.has(k))faceIncidence.set(k,[]);faceIncidence.get(k).push(id);}});
const itemByCell=new Map(items.flatMap((item,i)=>item.children.map(id=>[id,i])));
const layerArrows=new Set();
for(const ids of faceIncidence.values())if(ids.length===2){
 let [a,b]=ids.map(id=>itemByCell.get(id));if(a===b||items[a].layer===items[b].layer)continue;
 if(items[a].layer>items[b].layer)[a,b]=[b,a];layerArrows.add(a+','+b);
}
const itemLookup=new Map(items.map((item,i)=>[itemKey(itemVertices[i],item),i]));
const seed=cells[centralCellId];
const parity=p=>{let inversions=0;for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)if(p[i]>p[j])inversions++;return inversions%2?-1:1;};
const results=permutations([0,1,2,3]).map(permutation=>{
 const transform=a=>permutation.map(i=>a[i]);
 const nodeMap=nodes.map(n=>lookup.get(key(transform(n.address))));
 assert.ok(nodeMap.every(id=>id!==undefined));
 const itemMap=items.map((item,i)=>itemLookup.get(itemKey(itemVertices[i].map(id=>nodeMap[id]),item)));
 const preservesItems=itemMap.every(id=>id!==undefined);
 const preservesNearestEdges=[...primitiveEdges].every(k=>{const mapped=k.split(',').map(Number).map(id=>nodeMap[id]).sort((a,b)=>a-b).join(',');return primitiveEdges.has(mapped);});
 const preservesTriangulation=cells.every(cell=>cellSet.has(cellKey(cell.map(id=>transform(nodes[id].address)))));
 const preservesLayerArrows=preservesItems&&[...layerArrows].every(k=>{const [a,b]=k.split(',').map(Number);return layerArrows.has(itemMap[a]+','+itemMap[b]);});
 return {permutation,orientation:parity(permutation),preservesItems,preservesNearestEdges,preservesTriangulation,preservesLayerArrows,seedImage:seed.map(id=>nodeMap[id])};
});
assert.equal(results.length,24);
assert.ok(results.every(r=>r.preservesItems&&r.preservesNearestEdges&&r.preservesLayerArrows));
const triangulated=results.filter(r=>r.preservesTriangulation),oriented=triangulated.filter(r=>r.orientation===1);
assert.equal(triangulated.length,8);assert.equal(oriented.length,4);
const orbit=group=>[...new Set(group.map(r=>r.seedImage[0]))].sort((a,b)=>a-b);
assert.equal(orbit(results).length,4);assert.equal(orbit(triangulated).length,4);assert.equal(orbit(oriented).length,4);
// Unordered 2+2 partitions are weaker than labeled C/M classes: exchanging
// the two blocks is allowed, but exchanging just one vertex across them is not.
const partitions=[[[seed[0],seed[1]],[seed[2],seed[3]]],[[seed[0],seed[2]],[seed[1],seed[3]]],[[seed[0],seed[3]],[seed[1],seed[2]]]];
const partitionKey=p=>p.map(block=>[...block].sort((a,b)=>a-b).join(',')).sort().join('|');
const invariantPartitions=group=>partitions.filter(p=>group.every(r=>{
 const map=new Map(seed.map((id,i)=>[id,r.seedImage[i]]));return partitionKey(p.map(block=>block.map(id=>map.get(id))))===partitionKey(p);
}));
assert.equal(invariantPartitions(results).length,0);
assert.equal(invariantPartitions(triangulated).length,1);
assert.equal(invariantPartitions(oriented).length,3);
const displayedPartition=[[nodeIds.C0,nodeIds.C1],[nodeIds.M0,nodeIds.M1]];
assert.equal(partitionKey(invariantPartitions(triangulated)[0]),partitionKey(displayedPartition));
const swapWitness=oriented.find(r=>r.seedImage[seed.indexOf(nodeIds.C0)]===nodeIds.M0);
assert.ok(swapWitness);
const vertexSignatures=seed.map(id=>{
 const neighbors=lattice.edges.filter(e=>e.includes(id)).map(e=>e.find(v=>v!==id));
 const layerIncidence={};let tetrahedra=0,octahedra=0;
 items.forEach((item,i)=>{if(itemVertices[i].includes(id)){layerIncidence[item.layer]=(layerIncidence[item.layer]||0)+1;if(item.kind==='tetrahedron')tetrahedra++;else octahedra++;}});
 return {nodeId:id,address:nodes[id].address,carrierEdges:3,
  nearestEdges:neighbors.filter(v=>nodes[v].address.reduce((s,x,i)=>s+(x-nodes[id].address[i])**2,0)===2).length,
  subdivisionDiagonals:neighbors.filter(v=>nodes[v].address.reduce((s,x,i)=>s+(x-nodes[id].address[i])**2,0)===4).length,
  tetrahedra,octahedra,layerIncidence};
});
const signature=({nodeId,address,...rest})=>JSON.stringify(rest);
assert.equal(new Set(vertexSignatures.map(signature)).size,1);
assert.ok(vertexSignatures.every(v=>v.nearestEdges===12&&v.subdivisionDiagonals===2&&v.tetrahedra===8&&v.octahedra===6));
const files=['research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs','research/strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs'];
const sourceHashes=Object.fromEntries(await Promise.all(files.map(async f=>[f,createHash('sha256').update(await readFile(path.join(root,f))).digest('hex')])));
const report={schema:'marici.emergent-cm-incidence-audit.v1',scope:'Existing finite assembly, seed cell marked, item types and construction layers retained; UI C/M labels excluded from structural input',
 vertexSignatures,symmetryCounts:{untriangulated:24,triangulated:8,orientationPreservingTriangulated:4},
 seedVertexOrbitSizes:{untriangulated:orbit(results).length,triangulated:orbit(triangulated).length,orientationPreservingTriangulated:orbit(oriented).length},
 invariantUnorderedPartitions:{untriangulated:invariantPartitions(results),triangulated:invariantPartitions(triangulated),orientationPreservingTriangulated:invariantPartitions(oriented)},
 existingLabelsMatchTriangulationPartition:true,orientationPreservingRoleSwap:swapWitness,
 barycenterIsLatticeNode:lookup.has('0.25,0.25,0.25,0.25'),
 conclusion:{intrinsicLabeledCMVertexClasses:false,unorderedPairingFromChosenSubdivision:true,pairingWithoutSubdivision:false,
 intrinsicThreeEdgeLocalVersusTwelveEdgeAmbientIncidence:true,directedTwelveInThreeOutRuleEstablished:false},
 caveat:'These are explicit symmetry witnesses, not a computation of the complete abstract automorphism group. Their transitivity is already sufficient to obstruct an invariant labeled two-class assignment on seed vertices. No claim excludes roles from additional marked faces, directed transport, or dynamical data.',
 permutations:results,sourceHashes};
const out=path.join(root,'research/strominger/results/emergent-cm-roles');await mkdir(out,{recursive:true});await writeFile(path.join(out,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({symmetryCounts:report.symmetryCounts,orbitSizes:report.seedVertexOrbitSizes,partitionCounts:{untriangulated:0,triangulated:1,orientationPreservingTriangulated:3},roleSwap:swapWitness.permutation,conclusion:report.conclusion},null,2));
