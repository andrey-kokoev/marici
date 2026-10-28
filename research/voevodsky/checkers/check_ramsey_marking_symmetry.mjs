import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem,itemKey} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
import {phaseFrame,phaseAdvanceWitness} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const ROOT=new URL('../../../',import.meta.url);
const canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
const key=x=>JSON.stringify(canonical(x));
const perms=a=>a.length?a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const all=perms([0,1,2,3]),identity=[0,1,2,3],move=(p,v)=>{const out=[];v.forEach((x,i)=>out[p[i]]=x);return out;};
const point=(p,v)=>move(p,v.split(',').map(Number)).join(',');
const parts=x=>x.map(itemKey).sort();
const names=['C0','M0','C1','M1'];
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell,vertices=r.geometry.cells[cell].vertices;
const frames=all.map(m=>{
 const chart=r.completeP(cell,Object.fromEntries(names.map((n,i)=>[n,vertices[m[i]]])));
 const base=r.packet(chart,0,[0,1,2,3,4]),ops=r.outgoing(base).map(i=>r.operations[i]);
 const pn=ops.find(o=>o.kind==='PN'),reader=ops.find(o=>o.kind==='reader-phase-advance');
 const readerPN=r.outgoing(reader.target).map(i=>r.operations[i]).find(o=>o.kind==='PN');
 for(const op of [pn,reader,readerPN])assert.equal(r.validateTransfer(op),true);
 return {m,base,ops:[pn,reader,readerPN]};
});
// Preserve explicit IDs separately; covariance below is not literal record equality.
function profile(id,p){const s=packetSnapshot(r,id);return {
 origin:s.packet.origin,permutation:s.packet.permutation,species:s.chart.species,
 aliases:Object.fromEntries(Object.entries(s.chart.aliases).map(([n,v])=>[n,point(p,v)])),
 vertices:s.cell.vertices.map(v=>point(p,v)).sort(),
 owner:{kind:s.cell.owner.kind,inverted:s.cell.owner.inverted,origin:move(p,s.cell.owner.origin)}};}
const owners=[makeLatticeItem('tetrahedron',[0,0,0,0]),makeLatticeItem('tetrahedron',[2,0,0,0],true),makeLatticeItem('octahedron',[0,0,0,-1])];
const rows=[],actions=new Map();let operationCells=0,compositionCells=0,readerWitnessCells=0;
for(const p of all){
 const preserves=owners.every(o=>key(parts(o.components.map(c=>c.map(v=>move(p,v)))))===key(parts(makeLatticeItem(o.kind,move(p,o.origin),o.inverted).components)));
 const row={permutation:p,setwiseSeedChamberPreserved:true,fixedVertices:p.map((v,i)=>v===i?i:null).filter(v=>v!==null),
  fixedPrimitiveSubdivisionPreserved:preserves,complementaryRoles:[p[0],p[2]].sort().join(',')==='1,3'};
 assert.equal(itemKey(vertices.map(v=>move(p,v.split(',').map(Number)))),itemKey(vertices.map(v=>v.split(',').map(Number))));
 if(preserves){
  const packetMap=new Map(),chartMap=new Map(),cellMap=new Map(),operationMap=new Map(),bind=(map,a,b)=>{if(map.has(a))assert.equal(map.get(a),b);map.set(a,b);};
  const compare=(a,b)=>{assert.equal(key(profile(a,p)),key(profile(b,identity)));bind(packetMap,a,b);bind(chartMap,r.packets[a].chart,r.packets[b].chart);bind(cellMap,r.charts[r.packets[a].chart].cell,r.charts[r.packets[b].chart].cell);};
  const frameMap=[];
  for(const f of frames){
   const targetIndex=all.findIndex(m=>key(m)===key(f.m.map(i=>p[i]))),t=frames[targetIndex];frameMap.push(targetIndex);
   compare(f.base,t.base);
   f.ops.forEach((op,i)=>{const to=t.ops[i];bind(operationMap,op.id,to.id);compare(op.source,to.source);compare(op.target,to.target);
    assert.equal(key({kind:op.kind,phaseDelta:op.phaseDelta,permutation:op.permutation,face:op.face?.map(v=>point(p,v)).sort()??null}),
                 key({kind:to.kind,phaseDelta:to.phaseDelta,permutation:to.permutation,face:to.face?.slice().sort()??null}));operationCells++;});
  }
  for(const map of [packetMap,chartMap,cellMap,operationMap])assert.equal(new Set(map.values()).size,map.size);
  const transportWitness=x=>Array.isArray(x)?x.map(transportWitness):x&&typeof x==='object'?Object.fromEntries(Object.entries(x).map(([k,v])=>[k,k==='vertex'?point(p,v):k==='id'&&/^chart-[0-9]+@[0-9]+$/.test(v)?v.replace(/^chart-([0-9]+)/,(_,n)=>'chart-'+chartMap.get(Number(n))):transportWitness(v)])):x;
  for(const [a,b] of packetMap){const s=r.packets[a],t=r.packets[b];assert.equal(key(transportWitness(phaseFrame(r.charts[s.chart],s.origin))),key(phaseFrame(r.charts[t.chart],t.origin)));}
  for(const f of frames){const op=f.ops[1],to=r.operations[operationMap.get(op.id)];
   const witness=o=>phaseAdvanceWitness(r.charts[r.packets[o.source].chart],r.charts[r.packets[o.target].chart],r.packets[o.source].origin);
   assert.equal(key(transportWitness(witness(op))),key(witness(to)));readerWitnessCells++;
  }
  actions.set(key(p),packetMap);Object.assign(row,{frameMap,packetMap:[...packetMap],chartMap:[...chartMap],cellMap:[...cellMap],operationMap:[...operationMap]});
 }else{
  row.referenceCovarianceCounterexample=frames.findIndex(f=>{
   const t=frames[all.findIndex(m=>key(m)===key(f.m.map(i=>p[i])))];return key(profile(f.base,p))!==key(profile(t.base,identity));});
  assert(row.referenceCovarianceCounterexample>=0);
 }
 rows.push(row);
}
const group=rows.filter(x=>x.fixedPrimitiveSubdivisionPreserved);
assert.equal(group.length,8);assert.equal(rows.filter(x=>x.complementaryRoles).length,4);
assert(rows.filter(x=>x.complementaryRoles).every(x=>x.fixedPrimitiveSubdivisionPreserved&&x.fixedVertices.length===0));
for(const g of group)for(const h of group){
 const gh=h.permutation.map(i=>g.permutation[i]),G=actions.get(key(g.permutation)),H=actions.get(key(h.permutation)),GH=actions.get(key(gh));assert(GH);
 for(const [s,t] of H){assert.equal(G.get(t),GH.get(s));compositionCells++;}
}
const q=rows.find(x=>key(x.permutation)===key([1,0,3,2]));assert.equal(q.frameMap[0],7);assert.equal(q.fixedVertices.length,0);
const priorPath='research/voevodsky/results/ramsey-native-PN-overlap-span-v1.json';
const prior=JSON.parse(readFileSync(new URL(priorPath,ROOT),'utf8'));
for(const port of prior.witness.ports){
 const f=frames[port.chart];assert.equal(key(packetSnapshot(r,f.base)),key(port.base));
 const op=f.ops.find(o=>o.kind==='PN'&&o.face.every(v=>port.faceVertices.includes(v)));
 assert(op);assert.equal(key(op),key(port.operation));
 assert.equal(key(packetSnapshot(r,op.source)),key(port.source));assert.equal(key(packetSnapshot(r,op.target)),key(port.target));
}
const targetPort=prior.witness.ports.find(p=>p.chart===7&&p.face===1);
assert.equal(key(packetSnapshot(r,frames[7].base)),key(targetPort.base));
// Hostile gates: support equality must not count as pointwise identity;
// a fresh geometry permutation must not be silently admitted as an old rule kind.
assert.throws(()=>assert.deepEqual(q.permutation,identity));
const op=frames[0].ops[0];assert.throws(()=>r.validateTransfer({...op,kind:'global-marking-symmetry'}));
const hashes={};function pin(path){if(path in hashes)return;const bytes=readFileSync(new URL(path,ROOT));hashes[path]=createHash('sha256').update(bytes).digest('hex');
 if(path.endsWith('.mjs'))for(const m of bytes.toString().matchAll(/(?:from\s*|import\s*)['"]([^'"]+\.mjs)['"]/g))if(m[1].startsWith('.'))pin(decodeURIComponent(new URL(m[1],new URL(path,ROOT)).href.slice(ROOT.href.length)));}
pin('research/voevodsky/checkers/check_ramsey_marking_symmetry.mjs');pin(priorPath);
pin('research/voevodsky/contracts/ramsey-marking-symmetry-attempt.v1.json');pin('research/voevodsky/checkers/check_ramsey_marking_symmetry.py');
for(const [path,digest] of Object.entries(prior.source_sha256))assert.equal(createHash('sha256').update(readFileSync(new URL(path,ROOT))).digest('hex'),digest);
const out={schema:'marici.ramsey-marking-symmetry.verification.v1',status:'passed',scope_id:'covariant-marking-action-versus-fixed-vertex-identity-v1',
 markingPermutations:24,fixedSubdivisionSymmetries:8,complementaryRoleSymmetries:4,complementarySymmetriesFixingVertices:0,
 operationCovarianceCells:operationCells,readerWitnessCovarianceCells:readerWitnessCells,packetActionCompositionCells:compositionCells,selectedComplement:q,
 controls:['setwise covariance rejected as pointwise identity','new symmetry kind rejected by existing transfer validator'],
 nativeOperationAdded:false,pointwiseVertexIdentityPreserved:false,allNativeDerivationCovarianceProved:false,
 independentTargetInputsEliminated:false,parentDescentResolved:false,rows,source_sha256:hashes};
writeFileSync(new URL('../results/ramsey-marking-symmetry-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({...out,selectedComplement:undefined,rows:undefined,source_sha256:undefined},null,2));
