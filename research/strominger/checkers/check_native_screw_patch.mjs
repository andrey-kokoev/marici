// Exact finite native screw-periodic continuation, retaining the previous patch.
import assert from 'node:assert/strict';
import {mkdir,writeFile,readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const r=new GenerativeAssemblyRules(),selected=new Set([r.root]),construction=[],walk=[],prefixes=[];
const chart=id=>r.charts[r.packets[id].chart],cell=id=>r.geometry.cells[chart(id).cell];
const point=s=>s.split(',').map(Number),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]);
function step(source,kind){
 const i=r.outgoing(source).find(i=>r.operations[i].kind===kind);assert.notEqual(i,undefined,kind);
 const op=r.operations[i];r.validateTransfer(op);assert(selected.has(source));walk.push(i);
 if(!selected.has(op.target)){
  selected.add(op.target);construction.push(i);assert(r.describe([...selected]).valid);
  prefixes.push({operation:i,records:selected.size,compatible:true});
 }
 return op.target;
}
// Retain the entire preceding certified five-body patch, including both E readers.
const n0=step(r.root,'PN'),n1=step(n0,'NN-phase-advance'),n2=step(n1,'NN-phase-advance');
step(n2,'NE');const nr=step(n0,'reader-phase-advance');step(nr,'NE');
const original=[...selected],originalInspection=r.inspect(original);assert(originalInspection.certifiedExit);
const B=['PN','NN-phase-advance','NN-phase-advance','inverse-PN','reader-phase-advance'];
const A=['PN','reader-phase-advance','inverse-PN'];
const word=[...B,...A],repeats=4,blocks=[],boundaries=[r.root];let p=r.root;
for(let k=0;k<repeats;k++){
 const stages=[];
 for(const kind of word){p=step(p,kind);stages.push(p);}
 blocks.push(stages);boundaries.push(p);
}
let exit=step(p,'PN');exit=step(exit,'NE');
const sparse=r.inspect([...selected]);assert(sparse.valid&&sparse.allPacketsCanReachExit&&!sparse.allContactsWitnessed);
assert.equal(sparse.pendingContacts.length,repeats);
const fixedBodies=new Set(sparse.cells),repairs=[];
// Witness each incidental PN face. Follow the corresponding native suffix to
// an existing E body; do not equate different permutations at equal geometry.
for(let k=0;k<repeats;k++){
 const first=construction.length,branch=[];let q=blocks[k][2];
 const take=kind=>{q=step(q,kind);branch.push(q);assert(fixedBodies.has(chart(q).cell));};
 for(const kind of ['reader-phase-advance','inverse-PN','reader-phase-advance','PN'])take(kind);
 const expected=k+1<repeats?blocks[k+1][0]:blocks[k][6];
 assert.equal(r.packets[q].chart,r.packets[expected].chart);assert.equal(r.packets[q].origin,r.packets[expected].origin);
 for(let j=k+1;j<repeats;j++)for(const kind of j===k+1?word.slice(1):word)take(kind);
 for(const kind of k+1<repeats?['PN','NE']:['NE'])take(kind);
 repairs.push({block:k,packets:branch,newRecords:construction.length-first});
}
const ids=[...selected],inspection=r.inspect(ids);assert(inspection.certifiedExit&&inspection.allContactsWitnessed&&inspection.allPacketsCanReachExit);
assert(original.every(id=>selected.has(id)));assert.deepEqual(inspection.cells,sparse.cells);
// Fresh root-reachable replay from construction operations (not just cell coverage).
const reached=new Set([r.root]);for(const i of construction){const op=r.operations[i];assert(reached.has(op.source));r.validateTransfer(op);assert(!reached.has(op.target));reached.add(op.target);}
assert.deepEqual([...reached].sort((a,b)=>a-b),[...selected].sort((a,b)=>a-b));
const canExit=new Set(inspection.exitPackets),queue=[...canExit];
for(let j=0;j<queue.length;j++)for(const i of inspection.links){const op=r.operations[i];if(op.target===queue[j]&&!canExit.has(op.source)){canExit.add(op.source);queue.push(op.source);}}
assert.equal(canExit.size,selected.size);
// Replay into a second engine: packet/chart/cell IDs may differ because lazy
// generation order differs. Compare semantic records and occupied geometry.
const fresh=new GenerativeAssemblyRules(),mapping=new Map([[r.root,fresh.root]]);
for(const i of construction){
 const op=r.operations[i],source=mapping.get(op.source);assert.notEqual(source,undefined);
 const nextOp=fresh.operations[fresh.outgoing(source).find(j=>fresh.operations[j].kind===op.kind)];assert(nextOp);fresh.validateTransfer(nextOp);
 const actual=fresh.packets[nextOp.target],expected=r.packets[op.target];
 assert.equal(actual.origin,expected.origin);assert.deepEqual(actual.permutation,expected.permutation);
 const actualChart=fresh.charts[actual.chart],expectedChart=chart(op.target);
 assert.equal(actualChart.species,expectedChart.species);assert.deepEqual(actualChart.aliases,expectedChart.aliases);
 assert.deepEqual([...fresh.geometry.cells[actualChart.cell].vertices].sort(),[...cell(op.target).vertices].sort());
 mapping.set(op.target,nextOp.target);assert(fresh.describe([...mapping.values()]).valid);
}
const freshInspection=fresh.inspect([...mapping.values()]);assert(freshInspection.certifiedExit);
assert.deepEqual(freshInspection.counts,inspection.counts);assert.equal(mapping.size,selected.size);
// Root marks are the barycentric unit basis. Thus four images specify the
// affine map exactly on sum(x)=1, using an integer 4x4 matrix.
const marks=['C0','M0','C1','M1'];
assert.deepEqual(marks.map(n=>point(chart(r.root).aliases[n])),[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]);
const cols=marks.map(n=>point(chart(boundaries[1]).aliases[n]));
const T=Array.from({length:4},(_,i)=>cols.map(v=>v[i]));
const apply=v=>T.map(row=>dot(row,v));
const d=[-1,0,1,0],D=[-1,1,-1,1],axisPoint=[0,.5,0,.5];
function determinant(M){if(M.length===1)return M[0][0];return M[0].reduce((s,v,j)=>s+(-1)**j*v*determinant(M.slice(1).map(row=>row.filter((_,k)=>k!==j))),0);}
assert.equal(determinant(T),1);
const basis=[[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]];
for(const u of basis)for(const v of basis)assert.equal(dot(apply(u),apply(v)),dot(u,v));
assert.deepEqual(apply(d),d);assert.deepEqual(apply(D),D.map(x=>-x));
for(let j=0;j<4;j++){const e=Array.from({length:4},(_,i)=>Number(i===j));assert.deepEqual(apply(apply(e)),add(e,d.map(x=>2*x)));}
assert.deepEqual(apply(axisPoint),add(axisPoint,d));
// Test all five reference marks, every intermediate native chart, and phase grade.
for(let k=0;k<repeats;k++){
 for(const name of Object.keys(chart(boundaries[k]).aliases))assert.deepEqual(apply(point(chart(boundaries[k]).aliases[name])),point(chart(boundaries[k+1]).aliases[name]));
 assert.equal(r.packets[boundaries[k+1]].origin-r.packets[boundaries[k]].origin,4);
 if(k+1<repeats)for(let j=0;j<word.length;j++)for(const name of Object.keys(chart(blocks[k][j]).aliases))assert.deepEqual(apply(point(chart(blocks[k][j]).aliases[name])),point(chart(blocks[k+1][j]).aliases[name]));
}
const centroid=id=>cell(id).vertices.map(point).reduce(add,[0,0,0,0]).map(x=>x/4);
const centroids=boundaries.map(centroid),radial=sub(centroids[0],axisPoint);
assert.equal(dot(radial,d),0);assert.equal(dot(radial,radial),.25);
for(let k=0;k<centroids.length;k++)assert.deepEqual(centroids[k],add(add(axisPoint,d.map(x=>k*x)),radial.map(x=>(-1)**k*x)));
// This is a cell screw orbit, not a constant-radius centroid helix: the N
// pathway actually meets the screw axis. Do not hide this in a smooth drawing.
const axisHits=blocks[0].filter(id=>{const v=sub(centroid(id),axisPoint),t=dot(v,d)/dot(d,d);return sub(v,d.map(x=>t*x)).every(x=>x===0);});
assert(axisHits.length>0);
// Original octahedral axis sees bounded alternation, not sustained advancement.
const oldAxisHeights=centroids.map(v=>dot(v,D));assert.deepEqual(oldAxisHeights,[0,2,0,2,0]);
// The endpoint E caps continuation: an available next NN cannot be occupied
// simultaneously in that E body. This does not imply retained-prefix growth forever.
const lastN=step(boundaries.at(-1),'PN');assert(selected.has(lastN));
const nextIndex=r.outgoing(lastN).find(i=>r.operations[i].kind==='NN-phase-advance');assert.notEqual(nextIndex,undefined);
const next=r.operations[nextIndex].target;assert.equal(chart(next).cell,chart(exit).cell);assert(!r.describe([...ids,next]).valid);
// Replacing the +4 origin at a block boundary by its previous origin is rejected.
const lastOp=r.operations[walk.find(i=>r.operations[i].target===boundaries[1])];
assert.throws(()=>r.validateTransfer(lastOp,r.packets[lastOp.source],{...r.packets[lastOp.target],origin:0}));
const report={schema:'marici.native-screw-patch.v1',status:'pass',word,repeats,
 originalPackets:original,originalInspection,retainsOriginalPatch:true,construction,walk,prefixes,
 sparseInspection:sparse,repairs,inspection,freshReplay:{records:mapping.size,certifiedExit:freshInspection.certifiedExit,counts:freshInspection.counts},boundaries,blocks,
 screw:{matrix:T,determinant:1,rotation:'half-turn',axisPoint,direction:d,translationPerBlock:d,translationPerFullTurn:d.map(x=>2*x),pitch:'2*sqrt(2) in barycentric Euclidean units',rootEdgeLength:'sqrt(2)',originAdvancePerBlock:4,centroids,radiusSquared:.25,oldOctahedralAxis:D,oldAxisHeights,intermediateAxisHits:axisHits},
 claims:{nativeFiniteScrewPeriodicPatch:true,originalPatchRetained:true,constantRadiusCentroidPath:false,smoothHelixProven:false,handednessSelected:false,doubleHelixProven:false,separatingMiddleSheetProven:false,infiniteRetainedPrefixExtensionProven:false},
 packets:ids.map(i=>r.packets[i]),charts:[...new Set(ids.map(i=>r.packets[i].chart))].map(i=>r.charts[i]),
 occurrences:ids.map(i=>({packet:i,...phaseFrame(chart(i),r.packets[i].origin)})),
 operations:inspection.links.map(i=>r.operations[i]),cells:inspection.cells.map(i=>{const {owner,...c}=r.geometry.cells[i];return {...c,owner:{kind:owner.kind,origin:owner.origin,inverted:owner.inverted}};}),
 scope:'Finite native screw-periodic cell patch; not isotope stability, a smooth or double helix, a separating sheet, or a binding to the rung-12 field metric.'};
const root=new URL('../../../',import.meta.url),out=new URL('../results/native-screw-patch/',import.meta.url);await mkdir(out,{recursive:true});
report.sourceHashes={};for(const path of ['research/strominger/checkers/check_native_screw_patch.mjs','research/strominger/native-screw-patch-v1.md',...['local-reference-rules','phase-advance-model','phase-discipline-model','window-construction-model','lattice-items','simplex-components'].map(n=>'research/strominger/demos/particle-overlap-tetrahedron/'+n+'.mjs')])report.sourceHashes[path]=createHash('sha256').update(await readFile(new URL(path,root))).digest('hex');
await writeFile(new URL('verification.json',out),JSON.stringify(report,null,2)+'\n');
// Wireframe drawing of actual lattice points, not fitted helix curves.
const xyz=v=>{const x=point(v);return [dot(x,d),dot(x,D),x[1]-x[3]];};
const raw=v=>{const [x,y,z]=xyz(v);return [x+.35*z,y+.5*z];};
const verts=[...new Set(report.cells.flatMap(c=>c.vertices))],pts=verts.map(raw),lo=[Math.min(...pts.map(p=>p[0])),Math.min(...pts.map(p=>p[1]))],hi=[Math.max(...pts.map(p=>p[0])),Math.max(...pts.map(p=>p[1]))];
const scale=Math.min(1000/(hi[0]-lo[0]),390/(hi[1]-lo[1])),screen=v=>{const [x,y]=raw(v);return [40+scale*(x-lo[0]),480-scale*(y-lo[1])];};
const species=r.describe(ids).bodies,colors={proton:'#2471a3',neutron:'#ca6f1e',electron:'#148f77'};
const svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="600" viewBox="0 0 1100 600">','<rect width="1100" height="600" fill="white"/>','<text x="25" y="28" font-family="sans-serif" font-size="19">Native screw-periodic patch: four half-turn blocks</text>','<text x="25" y="53" font-family="sans-serif" font-size="13">Actual cells; original E cap retained. No smooth helix or separating sheet is drawn.</text>'];
for(const c of report.cells)for(const face of c.faces)svg.push(`<polygon points="${face.map(v=>screen(v).join(',')).join(' ')}" fill="${colors[species.get(c.id)]}" fill-opacity="0.09" stroke="${colors[species.get(c.id)]}" stroke-width="1"/>`);
for(let k=0;k<boundaries.length;k++){const c=centroids[k],xy=screen(c.join(','));svg.push(`<circle cx="${xy[0]}" cy="${xy[1]}" r="5" fill="#17202a"/><text x="${xy[0]+7}" y="${xy[1]-7}" font-family="sans-serif" font-size="14">P${k}, origin ${4*k}</text>`);}
svg.push('<text x="25" y="555" font-family="sans-serif" font-size="14">Blue P; orange N; green E. Native cell-centroid paths can meet the screw axis: this is not a constant-radius strand.</text>','</svg>');
await writeFile(new URL('native-screw-patch.svg',out),svg.join('\n')+'\n');
console.log(JSON.stringify({status:'pass',retainsOriginalPatch:true,blocks:repeats,counts:inspection.counts,records:ids.length,initialMissingContacts:sparse.pendingContacts.length,finalMissingContacts:inspection.pendingContacts.length,properHalfTurn:true,translationPerBlock:d,originAdvancePerBlock:4,intermediateAxisHits:axisHits.length,smoothHelixProven:false},null,2));
