// Native finite winding patch; no helices, periodic phase quotient or PE extension imposed.
import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseFrame,phaseAdvanceWitness} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=new URL('../../../',import.meta.url),base=new URL('../results/',import.meta.url),hashes={};
const hash=x=>createHash('sha256').update(x).digest('hex');
async function load(url){const bytes=await readFile(url);hashes[fileURLToPath(url).slice(fileURLToPath(root).length).replaceAll('\\','/')]=hash(bytes);return JSON.parse(bytes);}
const hydrogen=await load(new URL('hydrogen-edge-attachment/verification.json',base));
assert.equal(hydrogen.rows.length,24);
assert.equal(new Set(hydrogen.rows.map(row=>JSON.stringify(['C0','M0','C1','M1'].map(k=>row.bodies[0].aliases[k])))).size,24);
const operation=(r,source,kind)=>{const index=r.outgoing(source).find(i=>r.operations[i].kind===kind);return index===undefined?null:r.operations[index];};
const chart=(r,id)=>r.charts[r.packets[id].chart],vertices=(r,id)=>r.geometry.cells[chart(r,id).cell].vertices;
function rulesFor(row){return new GenerativeAssemblyRules({seedBindings:Object.fromEntries(['C0','M0','C1','M1'].map(k=>[k,row.bodies[0].aliases[k]]))});}
function auditWord(r,word){
 const selected=[r.root],prefixes=[{packets:[r.root],inspection:r.inspect([r.root])}],advances=[];
 for(const op of word){
  assert(selected.includes(op.source)&&!selected.includes(op.target));r.validateTransfer(op);selected.push(op.target);
  assert(r.describe(selected).valid);prefixes.push({packets:[...selected],inspection:r.inspect(selected)});
  if(op.phaseDelta===1)advances.push(phaseAdvanceWitness(chart(r,op.source),chart(r,op.target),r.packets[op.source].origin));
 }
 const inspection=r.inspect(selected);assert(inspection.valid&&inspection.certifiedExit&&inspection.allContactsWitnessed&&inspection.allPacketsCanReachExit);
 // Direct selected-edge reverse traversal, independent of inspect's exit traversal.
 const ops=inspection.links.map(i=>r.operations[i]),seen=new Set(inspection.exitPackets),queue=[...seen];
 for(let i=0;i<queue.length;i++)for(const op of ops)if(op.target===queue[i]&&!seen.has(op.source)){seen.add(op.source);queue.push(op.source);}
 assert.equal(seen.size,selected.length);
 return {selectedPackets:selected,word:word.map(op=>op.id),operations:ops,prefixes,advances,inspection,
   packets:selected.map(i=>r.packets[i]),charts:[...new Set(selected.map(i=>r.packets[i].chart))].map(i=>r.charts[i]),
   occurrenceFrames:selected.map(id=>({packet:id,...phaseFrame(chart(r,id),r.packets[id].origin)}))};
}
const census=[];
for(const [mark,row] of hydrogen.rows.entries()){
 const r=rulesFor(row),initial=operation(r,r.root,'PN').target,orbit=[initial],edges=[];
 for(let k=0;k<4;k++){const op=operation(r,orbit.at(-1),'NN-phase-advance');if(!op)break;r.validateTransfer(op);edges.push(op.id);orbit.push(op.target);}
 const closed=orbit.length===5&&r.packets[orbit[0]].chart===r.packets[orbit[4]].chart;
 if(closed){assert.deepEqual(r.packets[orbit[0]].permutation,r.packets[orbit[4]].permutation);assert.equal(r.packets[orbit[4]].origin-r.packets[orbit[0]].origin,4);}
 census.push({mark,NNsteps:edges.length,geometryReturnsAfterFour:closed,packetOrbit:orbit});
}
assert.equal(census.filter(row=>row.geometryReturnsAfterFour).length,8);
assert.equal(census.filter(row=>row.NNsteps===0).length,16);
// Deterministic canonical marking, not a search fitted to a desired helix.
const r=rulesFor(hydrogen.rows[0]),pn=operation(r,r.root,'PN'),n0=pn.target;
const nn0=operation(r,n0,'NN-phase-advance'),n1=nn0.target;
const nn1=operation(r,n1,'NN-phase-advance'),n2=nn1.target;
const ne2=operation(r,n2,'NE'),e2=ne2.target;
const sparse=[r.root,n0,n1,n2,e2],sparseInspection=r.inspect(sparse);
assert(sparseInspection.valid&&sparseInspection.allPacketsCanReachExit&&!sparseInspection.allContactsWitnessed);
assert.equal(sparseInspection.pendingContacts.length,1);
const reread=operation(r,n0,'reader-phase-advance'),nRead=reread.target,neRead=operation(r,nRead,'NE'),eRead=neRead.target;
assert.equal(chart(r,n0).cell,chart(r,nRead).cell);assert.equal(chart(r,e2).cell,chart(r,eRead).cell);
const word=[pn,nn0,nn1,ne2,reread,neRead],patch=auditWord(r,word);
assert.deepEqual(patch.inspection.counts,{proton:1,neutron:3,electron:1});
assert.equal(patch.selectedPackets.length,7);assert.equal(new Set(patch.inspection.cells).size,5);
assert.equal(r.packets[e2].origin,2);assert.equal(r.packets[eRead].origin,1);
assert.equal(r.outgoing(e2).length,0);assert.equal(r.outgoing(eRead).length,0);
assert.notDeepEqual(r.packets[e2].permutation,r.packets[eRead].permutation);
// Four occupied ring cells are exactly one octahedron's fixed subdivision.
const ring=[n0,n1,n2,e2].map(id=>chart(r,id).cell),cells=ring.map(id=>r.geometry.cells[id]);
assert.equal(new Set(ring).size,4);assert(cells.every(cell=>cell.owner.kind==='octahedron'));
const key=vs=>[...vs].sort().join('|');
const ownerKeys=cells[0].owner.components.map(component=>key(component.map(p=>p.join(',')))).sort();
assert.deepEqual(cells.map(cell=>key(cell.vertices)).sort(),ownerKeys);
const common=cells[0].vertices.filter(v=>cells.every(cell=>cell.vertices.includes(v)));assert.equal(common.length,2);
const ringVertices=[...new Set(cells.flatMap(cell=>cell.vertices))];assert.equal(ringVertices.length,6);
const faceOwners=new Map();for(const cell of cells)for(const face of cell.faces){const k=key(face);if(!faceOwners.has(k))faceOwners.set(k,{face,cells:[]});faceOwners.get(k).cells.push(cell.id);}
const interior=[...faceOwners.values()].filter(f=>f.cells.length===2),boundary=[...faceOwners.values()].filter(f=>f.cells.length===1);
assert.equal(interior.length,4);assert.equal(boundary.length,8);assert(interior.every(f=>common.every(v=>f.face.includes(v))));
const ringDegree=new Map(ring.map(id=>[id,0]));for(const face of interior)for(const id of face.cells)ringDegree.set(id,ringDegree.get(id)+1);assert([...ringDegree.values()].every(n=>n===2));
const boundaryEdges=new Map();for(const {face} of boundary)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){const k=key([face[i],face[j]]);boundaryEdges.set(k,(boundaryEdges.get(k)??0)+1);}
assert.equal(boundaryEdges.size,12);assert([...boundaryEdges.values()].every(n=>n===2));assert.equal(6-12+8,2);
// Integer-scaled centroids prove zero axial rise without floating-point fitting.
const point=v=>v.split(',').map(Number),axis=point(common[1]).map((v,i)=>v-point(common[0])[i]);
const dot=(a,b)=>a.reduce((sum,v,i)=>sum+v*b[i],0);
const axialNumerators=cells.map(cell=>dot(cell.vertices.map(point).reduce((a,b)=>a.map((v,i)=>v+b[i]),[0,0,0,0]),axis));
assert(axialNumerators.every(x=>x===axialNumerators[0]));
const faceAxialNumerators=interior.map(({face})=>dot(face.map(point).reduce((a,b)=>a.map((v,i)=>v+b[i]),[0,0,0,0]),axis));
assert(faceAxialNumerators.every(x=>4*x===3*axialNumerators[0]));
const midTwice=point(common[0]).map((v,i)=>v+point(common[1])[i]);
const radialFour=cells.map(cell=>cell.vertices.map(point).reduce((a,b)=>a.map((v,i)=>v+b[i]),[0,0,0,0]).map((v,i)=>v-2*midTwice[i]));
assert(dot(radialFour[0],radialFour[0])>0);
for(let i=0;i<4;i++){
 assert.equal(dot(radialFour[i],axis),0);
 assert.equal(dot(radialFour[i],radialFour[(i+1)%4]),0);
 assert.equal(dot(radialFour[i],radialFour[i]),dot(radialFour[0],radialFour[0]));
 assert(radialFour[i].every((v,j)=>v===-radialFour[(i+2)%4][j]));
}
const roles=r.describe(patch.selectedPackets).roles;
assert(common.every(v=>roles.get(v)==='C'));
assert(ringVertices.filter(v=>!common.includes(v)).every(v=>roles.get(v)==='M'));
// The available all-N circuit is four +1 steps, not a zero-grade identity.
const nOrbit=[n0];const orbitOps=[];
for(let k=0;k<4;k++){const op=operation(r,nOrbit.at(-1),'NN-phase-advance');assert(op);r.validateTransfer(op);orbitOps.push(op);nOrbit.push(op.target);}
assert.equal(r.packets[nOrbit[4]].chart,r.packets[nOrbit[0]].chart);
assert.deepEqual(r.packets[nOrbit[2]].permutation,r.packets[nOrbit[0]].permutation);
assert.notEqual(r.packets[nOrbit[2]].chart,r.packets[nOrbit[0]].chart);
assert.deepEqual(r.packets[nOrbit[4]].permutation,r.packets[nOrbit[0]].permutation);
const orbitFrames=nOrbit.map(id=>phaseFrame(chart(r,id),r.packets[id].origin));
for(let i=0;i<3;i++){
 assert.equal(orbitFrames[4].window[i].index-orbitFrames[0].window[i].index,4);
 assert.equal(orbitFrames[4].window[i].vertex,orbitFrames[0].window[i].vertex);
}
assert.equal(orbitFrames[4].context.index-orbitFrames[0].context.index,4);
assert.equal(orbitFrames[0].window[1].vertex,orbitFrames[2].window[1].vertex);
assert.notEqual(orbitFrames[0].window[0].vertex,orbitFrames[2].window[0].vertex);
assert.equal(orbitFrames[0].window[0].vertex,orbitFrames[4].window[0].vertex);
// Opposite spatial sector at two steps, same sector at four; no index folding.
let rejected=0;
assert.throws(()=>r.validateTransfer(orbitOps[3],r.packets[orbitOps[3].source],r.packets[n0]));rejected++;
const earlyE=operation(r,n0,'NE').target;
assert.equal(chart(r,earlyE).cell,chart(r,n1).cell);
assert(!r.describe([...patch.selectedPackets,earlyE]).valid);rejected++;
assert.equal(chart(r,nOrbit[3]).cell,chart(r,e2).cell);
assert(!r.describe([...patch.selectedPackets,nOrbit[3]]).valid);rejected++;
assert(!r.inspect(patch.selectedPackets.filter(id=>id!==eRead)).allContactsWitnessed);rejected++;
// A separate two-step P reader motif repeats geometry, not spatial position.
const pr=rulesFor(hydrogen.rows[0]);let p=pr.root;const pWord=[],pStages=[];
for(let k=0;k<3;k++){
 const a=operation(pr,p,'PN'),b=operation(pr,a.target,'NE');pWord.push(a,b);pStages.push({origin:k,p,n:a.target,e:b.target});
 if(k<2){const advance=operation(pr,p,'reader-phase-advance');pWord.push(advance);p=advance.target;}
}
const rereadingPatch=auditWord(pr,pWord);
assert.equal(pr.packets[pStages[0].p].chart,pr.packets[pStages[2].p].chart);
assert.deepEqual(pr.packets[pStages[0].p].permutation,pr.packets[pStages[2].p].permutation);
assert.equal(pr.packets[pStages[2].p].origin-pr.packets[pStages[0].p].origin,2);
const result={schema:'marici.native-winding-patch.v1',status:'pass',census,
 sparseAttempt:{selectedPackets:sparse,inspection:sparseInspection},completedPatch:patch,
 rereadingPatch:{stages:pStages,...rereadingPatch},
 geometry:{occupiedCells:patch.inspection.cells.map(id=>{const {owner,...cell}=r.geometry.cells[id];return {...cell,owner:{kind:owner.kind,origin:owner.origin,inverted:owner.inverted}};}),ringCells:ring,axisVertices:common,axisRoles:'CC',outerRoles:'MMMM',ringVertices,internalFaces:interior,boundaryFaces:boundary,boundaryEulerCharacteristic:2,axialCentroidNumerators:axialNumerators,centroidDivisor:4,axialFaceNumerators:faceAxialNumerators,faceDivisor:3,radialCentroidNumerators:radialFour,centroidTurn:'four exact quarter-turns',axialRise:0},
 availableNOrbit:nOrbit.map(id=>({packet:r.packets[id],chart:chart(r,id)})),
 occurrenceOrbit:orbitFrames,negativeControls:rejected,coefficientPeriod:2,CVertexPeriod:2,MVertexPeriod:4,NNGeometryPeriod:4,originShiftAtGeometryReturn:4,
 nonzeroPitchHelixEstablished:false,fullA4ForSelectedDirectedPatchEstablished:false,
 scope:'Native finite face-attached patch and retained reader winding; not a global helical tessellation, periodic phase quotient, isotope stability certificate or reference-only-N constructor.'};
const out=new URL('native-winding-patch/',base);await mkdir(out,{recursive:true});
// Actual lattice geometry, projected for illustration; right panel is history,
// not a physical axial coordinate. No geometry is moved to manufacture pitch.
const tetra=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]];
const xyz=v=>point(v).reduce((sum,a,i)=>sum.map((x,j)=>x+a*tetra[i][j]),[0,0,0]);
const occupied=patch.inspection.cells.map(id=>r.geometry.cells[id]),allPoints=[...new Set(occupied.flatMap(c=>c.vertices))];
const project=v=>{const [x,y,z]=xyz(v);return [x+.45*y,z+.30*y];};
const ps=allPoints.map(project),minX=Math.min(...ps.map(p=>p[0])),maxX=Math.max(...ps.map(p=>p[0])),minY=Math.min(...ps.map(p=>p[1])),maxY=Math.max(...ps.map(p=>p[1]));
const scale=Math.min(430/(maxX-minX),420/(maxY-minY));
const screen=v=>{const [x,y]=project(v);return [40+(x-minX)*scale,490-(y-minY)*scale];};
const species=new Map([...r.describe(patch.selectedPackets).bodies]),colors={proton:'#2980b9',neutron:'#d68910',electron:'#148f77'};
const svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">','<rect width="1000" height="620" fill="white"/>',
 '<text x="25" y="28" font-family="sans-serif" font-size="19">Native tessellated turn: actual geometry, no imposed helix</text>',
 '<text x="25" y="55" font-family="sans-serif" font-size="13">Left: four octahedral sectors plus the root P. Right: distinct phase occurrences, not spatial height.</text>'];
for(const cell of occupied)for(const face of cell.faces)svg.push(`<polygon points="${face.map(v=>screen(v).join(',')).join(' ')}" fill="${colors[species.get(cell.id)]}" fill-opacity="0.16" stroke="${colors[species.get(cell.id)]}" stroke-width="1.5"/>`);
svg.push(`<path d="M ${screen(common[0]).join(',')} L ${screen(common[1]).join(',')}" stroke="#922b21" stroke-width="4" stroke-dasharray="7 4"/>`);
for(const cell of occupied){const pts=cell.vertices.map(screen),x=pts.reduce((s,p)=>s+p[0],0)/4,y=pts.reduce((s,p)=>s+p[1],0)/4;svg.push(`<text x="${x}" y="${y}" font-family="sans-serif" font-size="15">${species.get(cell.id)[0].toUpperCase()}${cell.id}</text>`);}
for(let k=0;k<nOrbit.length;k++){
 const id=nOrbit[k],frame=phaseFrame(chart(r,id),r.packets[id].origin),marks=[...frame.window,frame.context].map(o=>o.role+o.index).join(' '),y=110+k*65;
 svg.push(`<text x="550" y="${y}" font-family="sans-serif" font-size="15">k=${k}: N cell ${chart(r,id).cell} — ${marks}</text>`);
}
svg.push('<text x="550" y="470" font-family="sans-serif" font-size="14">Two steps: coefficients repeat; geometry does not.</text>','<text x="550" y="495" font-family="sans-serif" font-size="14">Four steps: geometry repeats; origin advances by four.</text>',
 '<text x="25" y="580" font-family="sans-serif" font-size="14">The selected patch uses E in the fourth sector; the all-N orbit is available reference data, not simultaneous occupancy.</text>','</svg>');
await writeFile(new URL('native-patch.svg',out),svg.join('\n')+'\n');
for(const path of ['research/strominger/checkers/check_native_winding_patch.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/native-winding-patch-v1.md'])hashes[path]=hash(await readFile(new URL(path,root)));
result.sourceHashes=hashes;await writeFile(new URL('verification.json',out),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,markingsWithFourSectorTurn:census.filter(r=>r.geometryReturnsAfterFour).length,markingsWithNoFirstNN:census.filter(r=>!r.NNsteps).length,
 counts:patch.inspection.counts,selectedRecords:patch.selectedPackets.length,constructionSteps:word.length,coefficientPeriod:2,NNGeometryPeriod:4,axialRise:0,
 sparseMissingContacts:sparseInspection.pendingContacts.length,completedMissingContacts:patch.inspection.pendingContacts.length,negativeControls:rejected},null,2));
