import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileAt} from '../su32-layer4-comparison.mjs';
import {comparisonPort} from '../su32-rooted-comparison-gluing.mjs';
import {orientAttachmentProblem} from '../su32-undirected-reference-attachment.mjs';
import {key,signature,dual,corolla,rotate,rooted,glue,decompose,assemble} from '../su32-cyclic-port-fragment.mjs';
const root='research/strominger',fixturePath=root+'/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(await digest(p),h,`Stale ${p}`);
const contractPath=root+'/contracts/su32-cyclic-port-fragment-v1.json';
const contract=JSON.parse(await fs.readFile(contractPath,'utf8'));assert.equal(contract.obligation,'route/coherencer compatibility');
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);
const labels=['P+','P-','E+','E-'],unique=xs=>[...new Map(xs.map(x=>[key(x),x])).values()];
const cyclicKey=op=>Array.from({length:op.ports.length},(_,i)=>key(rotate(op,i).ports)).sort()[0];
let rootLifts=0,cyclicGluingChecks=0,segalRoundTrips=0,spuriousHeaderGluings=0,sampleChecks=0;
const bindings=[];let hostileWitness=null,example=null;
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]),sig=signature(layout,fixture);
 for(const c of sig.colours){assert.deepEqual(dual(sig,dual(sig,c)),c);assert.notDeepEqual(dual(sig,c),c);}
 const plus=layout.template.comparisons.find(c=>c.sharedRecord==='E+'),minus=layout.template.comparisons.find(c=>c.sharedRecord==='E-');
 const cs=[],rs=[];
 function operations(registry){
  const a=plus.inputs.map(id=>channelOperand(layout,id,registry)),b=minus.inputs.map(id=>channelOperand(layout,id,registry));
  const c=compareAt(layout,plus.cell,...a);cs.push(corolla(layout,sig,'C',[...a,c]));
  for(const flipC of [false,true])for(const flipB of [false,true]){
   const x=compareAt(layout,plus.cell,...(flipC?[...a].reverse():a)),y=compareAt(layout,minus.cell,...(flipB?[...b].reverse():b));
   rs.push(corolla(layout,sig,'R',[x,y,reconcileAt(layout,x,y)]));
  }
 }
 for(let bits=0;bits<16;bits++)operations(Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1])));
 const C=unique(cs),R=unique(rs);assert.equal(C.length,8);assert.equal(R.length,64);
 const pairs=C.flatMap(c=>R.filter(r=>key(c.ports[2].value)===key(r.ports[0].value)).map(r=>[c,r]));assert.equal(pairs.length,32);
 const headers=C.flatMap(c=>R.filter(r=>key(comparisonPort(c.ports[2].value))===key(comparisonPort(r.ports[0].value))).map(r=>[c,r]));
 assert.equal(headers.length,64);
 for(const [c,r] of headers)if(key(c.ports[2].value)!==key(r.ports[0].value)){
  assert.throws(()=>glue(sig,c,2,r,0),/Full internal packet/);spuriousHeaderGluings++;
  hostileWitness??={binding:[p,e],leftInternal:c.ports[2].value,rightInternal:r.ports[0].value,
   equalHeader:comparisonPort(c.ports[2].value),reason:'Opposite child orders are distinct retained operation histories.'};
 }
 for(const [c,r] of pairs){
  const g=glue(sig,c,2,r,0),output=r.sourceNode,local=decompose(layout,sig,output);
  assert.deepEqual(assemble(layout,sig,local),output);
  assert.deepEqual(local,{left:c,right:r});segalRoundTrips++;
  assert.deepEqual(rooted(sig,c,2).output.colour,r.ports[0].colour);
  assert.deepEqual(rotate(c,3),c);assert.deepEqual(rotate(r,3),r);assert.deepEqual(rotate(g,4),g);
  for(let i=0;i<3;i++)for(let j=0;j<3;j++){
   const a=rotate(c,i),b=rotate(r,j),ai=a.ports.findIndex(x=>x.colour.wire==='C-R'),bi=b.ports.findIndex(x=>x.colour.wire==='C-R');
   const changed=glue(sig,a,ai,b,bi);
   assert.equal(cyclicKey(changed),cyclicKey(g));
   assert.deepEqual(changed.vertices.map(v=>v.sourceNode),g.vertices.map(v=>v.sourceNode));cyclicGluingChecks++;
  }
  for(let k=0;k<4;k++){
   const view=rooted(sig,g,k),boundary=view.output.colour.end;
   const orientation=orientAttachmentProblem(layout,sig.problem,boundary);
   const last=orientation.oriented.filter(a=>a.to===boundary);assert.equal(last.length,1);
   assert.equal(last[0].wire,view.output.colour.wire);
   assert.deepEqual(view.output.value,g.ports[k].value);rootLifts++;
  }
  const bad=structuredClone(r);bad.ports[0].colour=structuredClone(c.ports[2].colour);
  assert.throws(()=>glue(sig,c,2,bad,0),/opposite arcs/);
  example??={binding:[p,e],colours:sig.colours,sourceOutput:output,local,composite:g,
   rootedBoundaryViews:Array.from({length:4},(_,k)=>rooted(sig,g,k))};
 }
 for(const registry of [Object.fromEntries(labels.map(k=>[k,null])),{'P+':{word:[1,2]},'P-':false,'E+':'shared','E-':[3,{tag:'e'}]}]){
  const a=plus.inputs.map(id=>channelOperand(layout,id,registry)),b=minus.inputs.map(id=>channelOperand(layout,id,registry));
  const c=compareAt(layout,plus.cell,...a),r=reconcileAt(layout,c,compareAt(layout,minus.cell,...b));
  assert.deepEqual(assemble(layout,sig,decompose(layout,sig,r)),r);sampleChecks++;
 }
 bindings.push({binding:[p,e],colours:sig.colours.length,comparisonRows:C.length,reconciliationRows:R.length,
  fullMatchingPairs:pairs.length,headerMatchingPairs:headers.length});
}
const sources=[fixturePath,contractPath,root+'/su32-cyclic-port-fragment.mjs',root+'/checkers/check_su32_cyclic_port_fragment.mjs',
 root+'/su32-layer4-comparison.mjs',root+'/su32-signed-reference-encoder.mjs',root+'/su32-rooted-comparison-gluing.mjs',
 root+'/su32-undirected-reference-attachment.mjs','references/2506.15622v2.pdf'];
const sourceHashes={};for(const p of sources)sourceHashes[p]=await digest(p);
const result={schema:'su32.cyclic-port-fragment.v1',passed:true,obligation:contract.obligation,
 counts:{bindings:4,rootLifts,cyclicGluingChecks,segalRoundTrips,spuriousHeaderGluings,mixedAndNullSamples:sampleChecks},bindings,
 conclusion:'Source constructor outputs reconstruct exactly from full matched local decorations on this tree; cyclic reindexing respects gluing and geometry-derived rooting.',
 limits:['Two-corolla fragment only; no arbitrary-tree units, associativity or higher horn fillers established.',
 'Arc duality is not an identification with P/E content duality.',
 'Root lifting changes presentation, not the native execution capability.',
 'Source compareAt/reconcileAt are existing candidate information operations; their physical realization is not asserted.',
 'Edge-five operation fibres and overlapping tree restrictions have not yet been extracted.'],
 example,hostileWitness,sourceHashes};
const dir=root+'/results/su32-cyclic-port-fragment-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,example:undefined,hostileWitness:undefined,sourceHashes:undefined},null,2));
