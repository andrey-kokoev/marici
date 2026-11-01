import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas,encodeSignedReferences,decodeSignedReferences,mapReferencePayloads} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,readRecords} from '../su32-layer4-comparison.mjs';
const root='research/strominger',fixturePath=root+'/results/su32-hopf-tests-v1/fixture.json';
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(await digest(p),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),labels=['P+','P-','E+','E-'];
const zero=()=>Object.fromEntries(labels.map(k=>[k,0]));
const key=JSON.stringify;
function permutations(xs){return xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>j!==i)).map(p=>[x,...p])):[[]];}
let sites=0,registryChecks=0,equivalenceGraphs=0,reencodingControls=0,example;
for(const chart of atlas.charts)for(const binding of [[0,0],[0,1],[1,0],[1,1]]){
 const layout=comparisonLayout(atlas,fixture,chart.id,binding);
 for(const c of layout.template.comparisons){
  const varyingPlus=c.varyingRole+'+',varyingMinus=c.varyingRole+'-';
  const aId=c.inputs.find(id=>Object.hasOwn(channelOperand(layout,id,zero()).records,varyingPlus));
  const bId=c.inputs.find(id=>id!==aId);assert(aId&&bId);
  const left=new Map(),right=new Map(),joints=new Map();
  for(let bits=0;bits<16;bits++){
   const registry=Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
   const a=channelOperand(layout,aId,registry),b=channelOperand(layout,bId,registry),j=compareAt(layout,c.cell,a,b);
   assert.deepEqual(j.children,[a,b]);assert.deepEqual(readRecords(layout,j),Object.fromEntries([varyingPlus,varyingMinus,c.sharedRecord].sort().map(k=>[k,registry[k]])));
   left.set(key(a),a);right.set(key(b),b);joints.set(key([a,b]),j);registryChecks++;
  }
  const as=[...left.values()],bs=[...right.values()];assert.equal(as.length,4);assert.equal(bs.length,4);assert.equal(joints.size,8);
  const admissible=permutations([0,1,2,3]).filter(p=>as.every((a,i)=>key(a.records[c.sharedRecord])===key(bs[p[i]].records[c.sharedRecord])));
  assert.equal(admissible.length,4);
  const coverage=new Map([...joints.keys()].map(k=>[k,0]));
  for(const p of admissible){
   const image=new Map();
   for(let i=0;i<4;i++){
    const a=as[i],b=bs[p[i]],pairKey=key([a,b]);assert(coverage.has(pairKey));coverage.set(pairKey,coverage.get(pairKey)+1);
    // This is an available payload reencoding, not a postulated native
    // naturality law: collapse only the independent plus-reference value.
    const registry={...zero(),...readRecords(layout,a),...readRecords(layout,b)};
    const mapped=decodeSignedReferences(atlas,mapReferencePayloads(atlas,encodeSignedReferences(atlas,chart.id,binding,registry),
     (value,label)=>label===varyingPlus?0:value));
    const ma=channelOperand(layout,aId,mapped),mb=channelOperand(layout,bId,mapped);
    compareAt(layout,c.cell,ma,mb); // The relation survives the same reencoding.
    const ak=key(ma);if(!image.has(ak))image.set(ak,new Set());image.get(ak).add(key(mb));
   }
   // The image of any equivalence graph is not even a function graph.
   assert.equal(image.size,2);assert([...image.values()].every(s=>s.size===2));
   equivalenceGraphs++;reencodingControls++;
  }
  assert([...coverage.values()].every(n=>n===2));sites++;
  if(!example&&chart.reading==='reading:0:-1'&&chart.source==='neutron:0,0,2,1'&&binding[0]===0&&binding[1]===0&&c.sharedRecord==='E+'){
   example={chartId:chart.id,binding,comparison:c,leftCell:aId,rightCell:bId,
    leftCarrier:as,rightCarrier:bs,readerPreservingEquivalences:admissible,
    compatiblePairs:[...coverage].map(([k,n])=>({operands:JSON.parse(k),fillersAtThisPair:n})),
    distinction:'There is no single fixed whole-operand equivalence whose graph covers all eight independently prepared compatible pairs.'};
  }
 }
}
assert(example);
const sourceHashes={};for(const p of [fixturePath,root+'/su32-signed-reference-encoder.mjs',root+'/su32-layer4-comparison.mjs',
 root+'/checkers/check_su32_join_type_boundary.mjs',root+'/agda/NativeSharedReaderJoin.agda',
 'research/nima/agda/NativeTableRules.agda','research/nima/agda/NativeTableResolution.agda'])sourceHashes[p]=await digest(p);
const result={passed:true,schema:'su32.join-type-boundary.v1',counts:{charts:atlas.charts.length,sites,registryChecks,equivalenceGraphs,reencodingControls},
 example,sourceHashes,
 conclusion:'Every tested source comparison interface has an eight-element Boolean compatibility relation, while each of the four shared-reader-preserving whole-operand bijections has only four graph pairs. Each compatible pair permits two such bijections; the relation itself selects neither.',
 limits:['This exhausts the Boolean interface fragment, not arbitrary payloads or native histories.',
 'The reencoding obstruction applies if independent payload-map naturality is demanded; the existence of the map API alone does not assert that policy.',
 'NativeSharedReaderJoin derives the appropriate retained join generically; these finite checks are not a native Su-32 geometry/port adapter.']};
const dir=root+'/results/su32-join-type-boundary-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts:result.counts,conclusion:result.conclusion,limits:result.limits},null,2));
