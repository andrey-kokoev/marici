// Distinguish macro-carrier symmetry from the fixed primitive subdivision.
import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {sourceItem,chamberItem,F} from '../ramsey-marked-patch.mjs';
import {itemKey,acrossFace} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {LocalPrimitiveGeometry} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/ramsey-transport-geometry-v1.json',import.meta.url);
const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]],e0=[1,0,0,0],key=p=>p.join(',');
const partsKey=parts=>parts.map(itemKey).sort().join(';');
const perms=xs=>xs.length?xs.flatMap((x,i)=>perms(xs.filter((_,j)=>i!==j)).map(t=>[x,...t])):[[]];
const matrices=[];
for(const p of perms([0,1,2]))for(const signs of [[-1,1],[-1,1],[-1,1]].reduce((xs,ss)=>xs.flatMap(x=>ss.map(s=>[...x,s])),[[]]))matrices.push(p.map((j,i)=>[0,1,2].map(k=>k===j?signs[i]:0)));
assert.equal(matrices.length,48);
const apply=(q,v,b)=>q.map((row,i)=>row.reduce((s,x,j)=>s+x*v[j],b[i]));
const lift=v=>[1-(v[0]+v[1]+v[2])/2,(v[0]+v[1]-v[2])/2,(v[0]+v[2]-v[1])/2,(-v[0]+v[1]+v[2])/2];
const owners=[sourceItem({kind:'tetrahedron',origin:[0,0,0,0]}),sourceItem({kind:'tetrahedron',origin:[2,0,0,0],inverted:true}),sourceItem({kind:'octahedron',origin:[0,0,0,-1]})];
const rows=[];let macroNeighborChecks=0,primitiveNeighborChecks=0;
for(const q of matrices){
 const b=[2,-1,1],move=p=>lift(apply(q,F(p),b));
 const preserves=Math.abs(q[1][1])===1;
 for(const owner of owners){
  const mapped=owner.vertices.map(move);
  assert(mapped.every(p=>p.every(Number.isSafeInteger)&&p.reduce((s,x)=>s+x,0)===1));
  const k=e0.map((x,i)=>Math.min(...mapped.map(p=>x-p[i]))),target=chamberItem(k);
  assert.equal(itemKey(mapped),target.key);
  for(const face of owner.faces){
   const sourceNeighbor=acrossFace(owner,face),targetNeighbor=acrossFace(target,face.map(move));
   assert.equal(itemKey(sourceNeighbor.vertices.map(move)),targetNeighbor.key);macroNeighborChecks++;
  }
  if(owner.kind==='octahedron')assert.equal(partsKey(owner.components.map(c=>c.map(move)))===partsKey(target.components),preserves);
  if(!preserves)continue;
  const sourceGeometry=new LocalPrimitiveGeometry(),targetGeometry=new LocalPrimitiveGeometry();
  for(const component of owner.components){
   const mappedComponent=component.map(move);
   assert(target.components.some(c=>itemKey(c)===itemKey(mappedComponent)));
   const from=sourceGeometry.register(owner,component),to=targetGeometry.register(target,mappedComponent);
   for(const f of faces){
    const face=f.map(i=>component[i]);
    const neighbor=sourceGeometry.neighbor(from,face.map(key));
    const movedNeighbor=targetGeometry.neighbor(to,face.map(move).map(key));
    const sourcePoints=sourceGeometry.cells[neighbor].vertices.map(text=>text.split(',').map(Number));
    assert.equal(itemKey(sourcePoints.map(move)),targetGeometry.cells[movedNeighbor].key);primitiveNeighborChecks++;
   }
  }
 }
 rows.push({Q:q,fixedOctahedralSubdivisionPreserved:preserves});
}
assert.equal(rows.filter(r=>r.fixedOctahedralSubdivisionPreserved).length,16);
assert.equal(macroNeighborChecks,768);assert.equal(primitiveNeighborChecks,384);
const hashes={};
async function pin(path){if(path in hashes)return;const bytes=await readFile(new URL(path,ROOT));hashes[path]=createHash('sha256').update(bytes).digest('hex');
 if(path.endsWith('.mjs'))for(const match of bytes.toString('utf8').matchAll(/(?:from\s*|import\s*)['"]([^'"]+\.mjs)['"]/g))if(match[1].startsWith('.')){
  const target=new URL(match[1],new URL(path,ROOT));const relative=decodeURIComponent(target.href.slice(ROOT.href.length));assert(!relative.startsWith('../'));await pin(relative);
 }
}
await pin('research/voevodsky/checkers/check_ramsey_transport_geometry.mjs');
const result={schema:'marici.ramsey-transport-geometry.v1',status:'passed',rows,macroCarrierMatrices:48,fixedSubdivisionMatrices:16,
 subdivisionChangingMatrices:32,macroNeighborChecks,primitiveNeighborChecks,
 full48NativePrimitiveSymmetryClaimed:false,nativePacketCovarianceProved:false,sourceHashes:hashes};
await writeFile(OUT,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:'passed',macroCarrierMatrices:48,fixedSubdivisionMatrices:16,macroNeighborChecks,primitiveNeighborChecks}));
