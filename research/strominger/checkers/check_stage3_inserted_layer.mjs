// Geometric collar experiment, NOT a native esd7 unit-cell realization.
// Coordinates are integral, sum-zero A3 coordinates scaled by 12.
// Outer carriers are dilated by 2, not translated rigid unit cells.
import assert from 'node:assert/strict';
const ids=[0,1,2,3],roles=['P','E','N','N'];
const points={};
for(const i of ids){
 points[`i${i}`]=ids.map(j=>12*(i===j?1:0)-3);
 points[`o${i}`]=points[`i${i}`].map(x=>2*x);
 points[`a${i}`]=points[`i${i}`].map(x=>-5*x/3);
 points[`b${i}`]=points[`a${i}`].map(x=>2*x);
}
const face=(prefix,i)=>ids.filter(j=>j!==i).map(j=>`${prefix}${j}`);
const center={id:'central-P',type:'P',vertices:ids.map(i=>`i${i}`)};
const stage2=[center,...ids.map(i=>({id:`boundary-${i}`,type:roles[i],vertices:[...face('i',i),`a${i}`]}))];
const collar=ids.flatMap(i=>{
 const [a,b,c]=ids.filter(j=>j!==i);
 return [
  [`i${a}`,`i${b}`,`i${c}`,`o${c}`],
  [`i${a}`,`i${b}`,`o${b}`,`o${c}`],
  [`i${a}`,`o${a}`,`o${b}`,`o${c}`],
 ].map((vertices,j)=>({id:`inserted-${i}-${j}`,type:null,vertices,oldInterface:i}));
});
const stage3=[center,...collar,...ids.map(i=>({id:`boundary-${i}`,type:roles[i],vertices:[...face('o',i),`b${i}`]}))];
const key=vs=>[...vs].sort().join('|');
const faces=cell=>ids.map(i=>cell.vertices.filter((_,j)=>j!==i));
function incidence(cells){
 const table=new Map();
 for(const c of cells)for(const f of faces(c)){
  const k=key(f);if(!table.has(k))table.set(k,[]);table.get(k).push(c.id);
 }
 assert.ok([...table.values()].every(os=>os.length<=2));
 return table;
}
function contacts(cells){return [...incidence(cells)].filter(([,os])=>os.length===2).map(([face,owners])=>({face,owners}));}
const before=contacts(stage2),after=contacts(stage3);
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const volume6=cell=>{
 const vs=cell.vertices.map(v=>points[v].slice(0,3));
 return Math.abs(det(...vs.slice(1).map(v=>v.map((x,i)=>x-vs[0][i]))));
};
assert.ok(stage3.every(c=>volume6(c)>0));
assert.equal(collar.reduce((s,c)=>s+volume6(c),0),7*volume6(center));
// A homothetic tetrahedron of scale two has eight times the central volume.
// Shared global vertex order makes all six lateral seam triangulations agree.
const collarBoundary=[...incidence(collar)].filter(([,os])=>os.length===1).map(([f])=>f).sort();
assert.deepEqual(collarBoundary,[...ids.map(i=>key(face('i',i))),...ids.map(i=>key(face('o',i)))].sort());
assert.equal(before.filter(c=>c.owners.includes(center.id)).length,4);
assert.equal(after.filter(c=>c.owners.includes(center.id)).length,4);
assert.ok(after.filter(c=>c.owners.includes(center.id)).every(c=>c.owners.some(id=>id.startsWith('inserted-'))));
assert.ok(!after.some(c=>c.owners.includes(center.id)&&c.owners.some(id=>id.startsWith('boundary-'))));
const routes=ids.map(i=>[center.id,...[0,1,2].map(j=>`inserted-${i}-${j}`),`boundary-${i}`]);
for(const route of routes)for(let i=1;i<route.length;i++)assert.ok(after.some(c=>c.owners.includes(route[i-1])&&c.owners.includes(route[i])));
for(const i of ids){
 assert.equal(stage2.find(c=>c.id===`boundary-${i}`).type,stage3.find(c=>c.id===`boundary-${i}`).type);
 assert.equal(volume6(stage3.find(c=>c.id===`boundary-${i}`)),8*volume6(stage2.find(c=>c.id===`boundary-${i}`)));
}
const pairContacts=ids.flatMap(i=>ids.filter(j=>j>i).map(j=>{
 const shared=cells=>cells.find(c=>c.id===`boundary-${i}`).vertices.filter(v=>cells.find(c=>c.id===`boundary-${j}`).vertices.includes(v));
 assert.equal(shared(stage2).length,2);assert.equal(shared(stage3).length,2);
 return {carriers:[i,j],types:[roles[i],roles[j]],stage2Intersection:'edge',stage3Intersection:'edge',retained:true};
}));
console.log(JSON.stringify({
 scope:'Piecewise-linear homothetic collar; no P/N/E rule for inserted cells; not an esd7 primitive filling',
 stage2:stage2.map(({id,type})=>({id,type})),
 stage3Counts:{central:1,insertedUntyped:collar.length,retainedBoundary:4},
 centralCellUnchanged:true,
 directCentralBoundaryFaceContacts:{before:4,after:0},
 replacementFacePaths:routes,
 closedCollarWithConsistentSixEdgeSeams:true,
 collarVolumeInCentralUnits:7,
 boundaryPairContacts:pairContacts,
 geometricCaveat:'Boundary carriers are doubled in linear size, not preserved as unit cells. No identification with the proposed unit-length increment is asserted.',
 removedContacts:'Central P to each boundary carrier, including its former E face-neighbor',
 notRemoved:'Boundary P-E and N-N edge contacts remain; insertion alone does not remove those relations',
 typingForced:false
},null,2));
