import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {buildSulfurLocalTransitions} from '../research/realization-tower/sulfur-local-transition.mjs';
import {analyzeNativePortFrame,learnGeometricLocalRule,replayGeometricLocalPacket,scanSharedCarriers,testSingleEdgeSheetFolds} from '../research/realization-tower/sulfur-local-geometry.mjs';
const reference=buildSulfurIncomingBundle(),before=JSON.stringify(reference),model=buildSulfurLocalTransitions(reference);
test('intrinsic port frames distinguish straight/oblique arrival and planar/skew departure',()=>{
 for(const m of model.motifs){
  const f=analyzeNativePortFrame(m);
  assert.deepEqual(f.inputs.map(p=>p.kind).sort(),['oblique','straight']);
  assert.deepEqual(f.outputs.map(p=>p.kind).sort(),['coplanar','skew']);
  const cop=f.outputs.find(p=>p.kind==='coplanar'),skew=f.outputs.find(p=>p.kind==='skew');
  assert.equal(cop.gramDeterminant,0);assert.equal(skew.gramDeterminant,4);
  assert(Math.abs(skew.transverseCosine-1/3)<1e-12);
  assert(Math.abs(skew.planeAngleDegrees-Math.acos(1/3)*180/Math.PI)<1e-10);
 }
});
test('held-out intrinsic rule predicts every reference passage and reverse without coordinate port sorting',()=>{
 for(const m of model.motifs){
  const rule=learnGeometricLocalRule(model.motifs.filter(x=>x.id!==m.id));
  assert.deepEqual(rule.outputBySign,{'+':'skew','-':'coplanar'});
  assert.deepEqual(rule.inputByAgreement,{true:'oblique',false:'straight'});
  for(const row of m.rows){
   const s=reference.strands.find(s=>s.id===row.strandId),i=s.edgeIds.indexOf(m.id);
   const packet={strandId:'opaque '+s.id,polarities:s.polarities,payload:{value:[1,null,{x:-7}]},port:s.edgeIds[i-1]};
   const out=replayGeometricLocalPacket(m,packet,rule);assert.deepEqual(out,{...packet,port:s.edgeIds[i+1]});
   assert.deepEqual(replayGeometricLocalPacket(m,out,rule,'reverse'),packet);
   const shuffled={...m,inputs:[...m.inputs].reverse(),outputs:[...m.outputs].reverse()};delete shuffled.rows;delete shuffled.observedPermutation;delete shuffled.selector;
   assert.deepEqual(replayGeometricLocalPacket(shuffled,packet,rule),out);
  }
 }
});
test('classification and routing survive a 3D rotation, reflection, translation and uniform rescaling',()=>{
 const rule=learnGeometricLocalRule(model.motifs);
 const transform=p=>{const [x,y,z]=worldPoint(p);return [7+3*(.6*x-.8*y),-3+3*(.8*x+.6*y),2-3*z];};
 for(const m of model.motifs){
  const moved={...m,tail:transform(m.tail),head:transform(m.head),inputs:m.inputs.map(p=>({...p,point:transform(p.point)})),outputs:m.outputs.map(p=>({...p,point:transform(p.point)}))};
  for(const row of m.rows){const packet={strandId:row.strandId,polarities:row.polarities,port:row.incomingEdge};assert.equal(replayGeometricLocalPacket(moved,packet,rule).port,row.outgoingEdge);}
  assert(Math.abs(analyzeNativePortFrame(moved).outputs.find(p=>p.kind==='skew').planeAngleDegrees-Math.acos(1/3)*180/Math.PI)<1e-10);
 }
});
test('carrier scan covers the independently enumerated common internal runs of every strand pair',()=>{
 const scan=scanSharedCarriers(reference),key=p=>p.join(','),pathKey=ps=>[ps.map(key).join('|'),[...ps].reverse().map(key).join('|')].sort()[0];
 const expected=new Set();
 for(let x=0;x<reference.strands.length;x++)for(let y=x+1;y<reference.strands.length;y++)for(const reversed of [false,true]){
  const sa=reference.strands[x],sb=reference.strands[y],a=sa.guide,b=reversed?[...sb.guide].reverse():sb.guide,ids=[sa.id,sb.id].sort().join('|');
  for(let i=1;i<a.length-2;i++)for(let j=1;j<b.length-2;j++){
   let length=0;
   while(i+length<a.length-1&&j+length<b.length-1&&key(a[i+length])===key(b[j+length])){
    length++;
    if(length<2||key(a[i-1])===key(b[j-1])||key(a[i+length])===key(b[j+length]))continue;
    expected.add(ids+';'+pathKey(a.slice(i,i+length)));
   }
  }
 }
 const actual=new Set(scan.candidates.filter(c=>c.occurrences.length===2).map(c=>c.occurrences.map(o=>o.strandId).sort().join('|')+';'+pathKey(c.path)));
 assert.deepEqual([...actual].sort(),[...expected].sort());assert.equal(actual.size,44);
 assert.equal(scan.windows,432);assert.equal(scan.counts.candidates,46);assert.equal(scan.counts.maxCarrierEdges,4);
 assert.equal(scan.counts.tangentStarMatches,0);assert.equal(scan.counts.chordAngleMatches,0);
});
test('positive control: an actual planar hex carrier passes both the search and non-expansion test',()=>{
 const h=Math.sqrt(3)/2,tail=[0,0,0],head=[0,-1,0],inputs=[[-h,.5,0],[h,.5,0]],outputs=[[-h,-1.5,0],[h,-1.5,0]];
 const reference={strands:inputs.map((p,i)=>({id:'control'+i,guide:[p,tail,head,outputs[i]]}))};
 const scan=scanSharedCarriers(reference);assert.equal(scan.counts.equalScaleChordMatches,1);assert.equal(scan.counts.tangentStarMatches,1);
 const fold=testSingleEdgeSheetFolds([{number:1,tail,head,inputs:inputs.map(point=>({point})),outputs:outputs.map(point=>({point}))}]);
 assert.equal(fold[0].necessaryNonExpansionSatisfied,true);
});
test('single-edge filled-sheet folding violates a necessary distance bound, without claiming a graph-hinge no-go',()=>{
 const folds=testSingleEdgeSheetFolds(model.motifs);assert.equal(folds.length,8);
 for(const f of folds){assert.equal(f.necessaryNonExpansionSatisfied,false);assert(Math.abs(f.tail.maxChordExpansion-4/3)<1e-12);assert.match(f.assumption,/filled planar/);}
 assert.equal(JSON.stringify(reference),before);
});
