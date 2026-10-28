import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPatch,sourceItem,specification,macroKeys,primitiveKeys,validateMarks,F,PatchResourceError} from '../ramsey-marked-patch.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/',import.meta.url);
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const specs=[{kind:'tetrahedron',origin:[0,0,0,0]},
 {kind:'tetrahedron',origin:[2,0,0,0],inverted:true},
 {kind:'octahedron',origin:[0,0,0,-1]}];
const add=(a,b)=>a.map((x,i)=>x+b[i]),scale=(a,m)=>a.map(x=>x*m);
function determinant(a,b,c){return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);}
const rows=[];let replayTotal=0;
for(const spec of specs)for(const a of [[0,0,0],[2,0,0],[-1,1,0]])for(const m of [1,2,3]){
 const p=buildPatch(spec,a,m),source=sourceItem(spec);
 assert.equal(p.components.size,source.components.length*m**3);
 assert.equal(p.tree.length,p.components.size-1);
 assert.equal(p.boundaryFaces.length,(spec.kind==='octahedron'?8:4)*m*m);
 assert(validateMarks(p,[...p.marks].reverse()));
 for(const {component} of p.components.values()){
  const v=component.map(F),d=v.slice(1).map(b=>b.map((x,i)=>x-v[0][i]));
  assert.equal(Math.abs(determinant(...d)),2);
 }
 rows.push({kind:spec.kind,inverted:spec.inverted??false,a,m,macroCells:p.items.length,primitives:p.components.size,boundaryTriangles:p.boundaryFaces.length,sourceNeighborReplays:p.neighborReplays});
 replayTotal+=p.neighborReplays;
}
const composition=[];
for(const spec of specs)for(const [m,n] of [[1,2],[2,1],[2,2]]){
 const a=[2,0,0],b=[-1,1,0],inner=buildPatch(spec,b,n);
 const nested=inner.items.map(item=>buildPatch(specification(item),a,m));
 const direct=buildPatch(spec,add(a,scale(b,m)),m*n);
 assert.deepEqual([...new Set(nested.flatMap(macroKeys))].sort(),macroKeys(direct));
 assert.deepEqual([...new Set(nested.flatMap(primitiveKeys))].sort(),primitiveKeys(direct));
 assert.equal(nested.reduce((s,p)=>s+p.components.size,0),direct.components.size);
 const transported=inner.marks.map(mark=>({...mark,point:add(a,scale(mark.point,m))}));
 assert(validateMarks(direct,transported));
 composition.push({kind:spec.kind,inverted:spec.inverted??false,m,n,finestPrimitives:direct.components.size,
  directHistorySha256:hash(JSON.stringify(direct.tree)),nestedHistoriesSha256:hash(JSON.stringify(nested.map(p=>p.tree))),
  equalityScope:'finest geometry and original marked vertices; histories retained, not equated as native processes'});
 replayTotal+=direct.neighborReplays+nested.reduce((s,p)=>s+p.neighborReplays,0)+inner.neighborReplays;
}
const p=buildPatch(specs[0],[0,0,0],2),bad=[];
function reject(name,fn,expected=RangeError){assert.throws(fn,expected);bad.push(name);}
reject('zero scale',()=>buildPatch(specs[0],[0,0,0],0));
reject('fractional scale',()=>buildPatch(specs[0],[0,0,0],1.5));
reject('odd-sum translation',()=>buildPatch(specs[0],[1,0,0],2));
reject('fractional translation',()=>buildPatch(specs[0],[0.5,0.5,0],2));
reject('duplicate source labels',()=>buildPatch(specs[0],[0,0,0],2,['A','A','C','D']));
reject('unverified history in source specification',()=>buildPatch({...specs[0],history:[]},[0,0,0],2));
reject('missing original mark',()=>validateMarks(p,p.marks.slice(1)));
reject('subdivision vertex substituted for source mark',()=>{const x=structuredClone(p.marks);x[0].point=[1,1,0];validateMarks(p,x);});
reject('labels silently swapped',()=>{const x=structuredClone(p.marks);[x[0].label,x[1].label]=[x[1].label,x[0].label];validateMarks(p,x);});
reject('resource refusal kept distinct from no-witness',()=>buildPatch(specs[0],[0,0,0],17),PatchResourceError);
assert(p.marks.every(mark=>mark.point[0]%2===0));
assert([...p.spatialVertices.values()].some(v=>Math.abs(v[0]%2)===1));
const fixture={
 instance:{N:2,r:2,pattern:p.marks.map(mark=>({label:mark.label,point:mark.source})),coloring:[]},
 certificate:{a:[0,0,0],m:2,color:0,image:p.marks.map(mark=>({label:mark.label,point:mark.point}))},
 patchHasOppositeColoredSubdivisionVertex:true};
for(let x=-2;x<=2;x++)for(let y=-2;y<=2;y++)for(let z=-2;z<=2;z++)if((x+y+z)%2===0)fixture.instance.coloring.push({point:[x,y,z],color:((x%2)+2)%2});
const sourceHashes={};
async function pin(path){if(path in sourceHashes)return;const bytes=await readFile(new URL(path,ROOT));sourceHashes[path]=hash(bytes);
 if(path.endsWith('.mjs'))for(const match of bytes.toString('utf8').matchAll(/(?:from\s*|import\s*)['"]([^'"]+\.mjs)['"]/g)){
  if(!match[1].startsWith('.'))continue;
  const target=new URL(match[1],new URL(path,ROOT));
  const relative=decodeURIComponent(target.href.slice(ROOT.href.length));assert(!relative.startsWith('../'));await pin(relative);
 }
}
await pin('research/voevodsky/ramsey-marked-patch.mjs');
await pin('research/voevodsky/checkers/check_ramsey_marked_patch.mjs');
const result={schema:'marici.ramsey-marked-patch.geometry.v1',status:'passed',rows,composition,rejectedControls:bad,
 sourcePrimitiveNeighborReplays:replayTotal,sourceHashes,
 primitiveAPI:'LocalPrimitiveGeometry.register/neighbor; makeLatticeItem; existing fixed octahedral components',
 nativeReaderPacketsProduced:false,nativeParticleAdmissionProved:false,uniformRamseyBoundProved:false,rootResolved:false};
await mkdir(OUT,{recursive:true});
await writeFile(new URL('ramsey-marked-patch-geometry-v1.json',OUT),JSON.stringify(result,null,2)+'\n');
await writeFile(new URL('ramsey-marked-patch-fixture-v1.json',OUT),JSON.stringify(fixture,null,2)+'\n');
console.log(JSON.stringify({status:'passed',patchCases:rows.length,compositionCases:composition.length,negativeControls:bad.length,sourcePrimitiveNeighborReplays:replayTotal}));
