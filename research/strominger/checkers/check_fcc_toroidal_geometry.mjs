// FCC quotient versus the actual fixed octahedral subdivision.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {makeLatticeItem,itemKey,acrossFace} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const root=new URL('../../../',import.meta.url),out=new URL('../results/fcc-toroidal-geometry/',import.meta.url);
const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]);
const norm=v=>v.reduce((s,x)=>s+x*x,0),mod=v=>v.map(x=>(x%2+2)%2);
const F=b=>[b[1]+b[2],b[1]+b[3],b[2]+b[3]];
const lift=t=>[-(t[0]+t[1]+t[2])/2,(t[0]+t[1]-t[2])/2,(t[0]+t[2]-t[1])/2,(-t[0]+t[1]+t[2])/2];
const rho=v=>[v[2],v[0],v[1]],bp=[0,3,1,2];
const rotateB=v=>{const a=[0,0,0,0];v.forEach((x,i)=>a[bp[i]]=x);return a;};
const power=(v,k,fn)=>{for(let i=0;i<k;i++)v=fn(v);return v;};
const classes=[[0,0,0],[1,1,0],[1,0,1],[0,1,1]],classIndex=v=>classes.findIndex(w=>String(w)===String(mod(v)));
const tetra=makeLatticeItem('tetrahedron',[0,0,0,0]),octa=makeLatticeItem('octahedron',[-1,0,0,0]);
assert.deepEqual(tetra.vertices.map(F),classes);
for(const a of tetra.vertices)for(const b of tetra.vertices)assert.equal(norm(sub(a,b)),norm(sub(F(a),F(b))));
const partsKey=parts=>parts.map(itemKey).sort().join(';');
// Sum integer coordinates before dividing: the model's drawing centers use
// floating accumulation, which must not enter exact equality tests.
const center=owner=>owner.vertices.reduce((a,v)=>add(a,v),[0,0,0,0]).map(x=>x/owner.vertices.length);
// All three diagonal triangulations, built from opposite pairs and equatorial edges.
function refinements(owner){
 const center2=center(owner).map(x=>2*x),result=[];
 for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)if(String(add(owner.vertices[i],owner.vertices[j]))===String(center2)){
  const axis=[owner.vertices[i],owner.vertices[j]],rim=owner.vertices.filter((_,k)=>k!==i&&k!==j),parts=[];
  for(let a=0;a<4;a++)for(let b=a+1;b<4;b++)if(norm(sub(rim[a],rim[b]))===2)parts.push([...axis,rim[a],rim[b]]);
  assert.equal(parts.length,4);result.push({axis,parts});
 }
 assert.equal(result.length,3);return result;
}
const choices=refinements(octa);assert(choices.some(c=>partsKey(c.parts)===partsKey(octa.components)));
const maps=[],products=[];let boundarySquares=0;
const inverted=makeLatticeItem('tetrahedron',[2,0,0,0],true);
for(const t of classes)for(let k=0;k<3;k++){
 const delta=lift(t);assert(delta.every(Number.isInteger));
 const move=v=>add(power(v,k,rotateB),delta),physical=v=>add(power(v,k,rho),t);
 const p=classes.map(v=>classIndex(physical(v)));
 assert.equal(p.filter((x,i)=>p.slice(0,i).includes(x)).length,0);
 const targetT=makeLatticeItem('tetrahedron',delta),targetO=makeLatticeItem('octahedron',move(octa.origin));
 assert.equal(itemKey(tetra.vertices.map(move)),targetT.key);
 assert.equal(itemKey(octa.vertices.map(move)),targetO.key);
 for(const owner of [tetra,inverted,octa]){
  const target=makeLatticeItem(owner.kind,move(owner.origin),owner.inverted);
  assert.equal(itemKey(owner.vertices.map(move)),target.key);
  for(const face of owner.faces){
   const neighbor=acrossFace(owner,face),other=acrossFace(target,face.map(move));
   assert.equal(itemKey(neighbor.vertices.map(move)),other.key);boundarySquares++;
  }
 }
 assert(octa.vertices.every(v=>String(F(move(v)))===String(physical(F(v)))));
 const fixed=partsKey(octa.components.map(c=>c.map(move)))===partsKey(targetO.components);
 assert.equal(fixed,k===0);
 const targetChoices=new Set(refinements(targetO).map(c=>partsKey(c.parts)));
 assert(choices.every(c=>targetChoices.has(partsKey(c.parts.map(part=>part.map(move))))));
 // Center-star subdivision is an alternative invariant construction, not native.
 const stars=octa.faces.map(face=>[center(octa),...face]);
 const targetStars=targetO.faces.map(face=>[center(targetO),...face]);
 assert.equal(partsKey(stars.map(c=>c.map(move))),partsKey(targetStars));
 maps.push({translation:t,rotationPower:k,vertexPermutation:p,fixedSubdivisionPreserved:fixed,refinementFamilyPreserved:true,
            transformedRootVertices:tetra.vertices.map(v=>F(move(v)))});
}
assert.equal(new Set(maps.map(m=>String(m.vertexPermutation))).size,12);
for(const a of maps)for(const b of maps){
 const raw=add(a.translation,power(b.translation,a.rotationPower,rho)),t=mod(raw),k=(a.rotationPower+b.rotationPower)%3;
 const target=maps.find(m=>String(m.translation)===String(t)&&m.rotationPower===k);assert(target);
 assert.deepEqual(target.vertexPermutation,b.vertexPermutation.map(i=>a.vertexPermutation[i]));
 const deck=sub(raw,t).map(x=>x/2);assert(deck.every(Number.isInteger));
 products.push({left:maps.indexOf(a),right:maps.indexOf(b),result:maps.indexOf(target),deck});
}
// Distinct comparison: actual proper rotations fixing the root tetrahedron.
function perms(xs){return xs.length?xs.flatMap((v,i)=>perms(xs.filter((_,j)=>j!==i)).map(p=>[v,...p])):[[]];}
const rootActions=[];
const native=new GenerativeAssemblyRules(),marks=native.charts[native.packets[native.root].chart].aliases;
const C=new Set(['C0','C1'].map(n=>marks[n]));
for(const p of perms([0,1,2,3])){
 if(p.reduce((n,v,i)=>n+p.slice(i+1).filter(w=>v>w).length,0)%2)continue;
 const move=v=>{const a=[0,0,0,0];v.forEach((x,i)=>a[p[i]]=x);return a;};
 const target=makeLatticeItem('octahedron',move(octa.origin));
 const preserved=partsKey(octa.components.map(c=>c.map(move)))===partsKey(target.components);
 const cm=[...C].every(text=>C.has(move(text.split(',').map(Number)).join(',')));
 rootActions.push({permutation:p,fixedSubdivisionPreserved:preserved,fixedRootCMPartitionPreserved:cm});
}
assert.equal(rootActions.filter(a=>a.fixedSubdivisionPreserved).length,4);
assert.equal(rootActions.filter(a=>a.fixedSubdivisionPreserved&&a.fixedRootCMPartitionPreserved).length,2);
const report={schema:'marici.fcc-toroidal-geometry.v1',status:'pass',
 fccMap:'(b0,b1,b2,b3) -> (b1+b2,b1+b3,b2+b3), sum(b)=1',classes,
 sourceTetrahedron:tetra,sourceOctahedron:octa,refinements:choices,affineActions:maps,products,rootActions,
 affineA4Order:12,unrefinedTemplateActionsChecked:36,unrefinedBoundarySquares:boundarySquares,affineActionsPreservingFixedSubdivision:4,properRootA4ActionsPreservingFixedSubdivision:4,
 properRootActionsPreservingSubdivisionAndNamedCMPartition:2,
 threeChoiceRefinementFamilyEquivariant:true,centerStarAlternative:{tetrahedra:8,equivariant:true,nativePrimitive:false,centerFCC:F(center(octa)),centerIsFCCVertex:F(center(octa)).reduce((a,b)=>a+b,0)%2===0},
 scope:'Source honeycomb geometry and spatial quotient only. Alternate subdivisions are not simultaneous occupancy or newly admitted native operations; no realization origin is quotiented.'};
assert.equal(report.centerStarAlternative.centerIsFCCVertex,false);assert.equal(boundarySquares,192);
report.sourceHashes={};for(const p of ['research/strominger/checkers/check_fcc_toroidal_geometry.mjs',...['lattice-items','simplex-components','local-reference-rules','phase-advance-model','window-construction-model'].map(n=>'research/strominger/demos/particle-overlap-tetrahedron/'+n+'.mjs')])report.sourceHashes[p]=createHash('sha256').update(await readFile(new URL(p,root))).digest('hex');
await mkdir(out,{recursive:true});await writeFile(new URL('verification.json',out),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'pass',affineA4Order:12,fixedSubdivisionPreservedBy:4,refinementFamilyEquivariant:true,rootRotationsPreservingSubdivisionAndCM:2},null,2));
