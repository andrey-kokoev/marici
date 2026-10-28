// Fixed finite relations of EXISTING operations. Re-root queries do not install
// new native inverse commands or a cyclic action on operation spaces.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileAt} from '../su32-layer4-comparison.mjs';
import {comparisonPort,decomposeRootedComparison,glueRootedComparison} from '../su32-rooted-comparison-gluing.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const domain=buildFiveSideOctComparisonDomain(buildPESymmetricSector(1),{readingIds:[reading.id]}).readings[0];
const labels=['P+','P-','E+','E-'];
const json=x=>JSON.stringify(x),unique=xs=>[...new Map(xs.map(x=>[json(x),x])).values()];
const same=(a,b)=>json(a)===json(b);
const solve=(rows,missing,known)=>unique(rows.filter(row=>row.every((v,i)=>i===missing||same(v,known[i]))).map(row=>row[missing]));
function one(rows,missing,known){const answers=solve(rows,missing,known);assert.equal(answers.length,1);return answers[0];}
function rootAudit(rows){
 return rows[0].map((_,missing)=>{
  const knownIndices=rows[0].map((_,i)=>i).filter(i=>i!==missing);
  const domains=knownIndices.map(i=>unique(rows.map(row=>row[i])));
  let tested=0,compatible=0,ambiguous=0;
  function walk(index,known){
   if(index===knownIndices.length){const answers=solve(rows,missing,known);tested++;if(answers.length)compatible++;if(answers.length>1)ambiguous++;return;}
   for(const value of domains[index]){const next=[...known];next[knownIndices[index]]=value;walk(index+1,next);}
  }
  walk(0,Array(rows[0].length).fill(null));assert.equal(ambiguous,0);
  return {missing,tested,compatible,incompatible:tested-compatible,ambiguous};
 });
}
let localRecoveries=0,compositeRecoveries=0,gluingSquares=0,exactGlueChecks=0;const reports=[];let ambiguityWitness;
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 const plus=layout.template.comparisons.find(c=>c.sharedRecord==='E+'),minus=layout.template.comparisons.find(c=>c.sharedRecord==='E-');
 const cRows=[],rRows=[];
 for(let bits=0;bits<16;bits++){
  const registry=Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]));
  const plusInputs=plus.inputs.map(id=>channelOperand(layout,id,registry));
  const minusInputs=minus.inputs.map(id=>channelOperand(layout,id,registry));
  const c=compareAt(layout,plus.cell,...plusInputs);
  cRows.push([...plusInputs,c]);
  // Histories are actual constructor outputs, not fabricated tags. The opaque
  // comparison boundary permits either order of its two retained channel children.
  for(const flipC of [false,true])for(const flipB of [false,true]){
   const internal=compareAt(layout,plus.cell,...(flipC?[...plusInputs].reverse():plusInputs));
   const external=compareAt(layout,minus.cell,...(flipB?[...minusInputs].reverse():minusInputs));
   rRows.push([internal,external,reconcileAt(layout,internal,external)]);
  }
 }
 const C=unique(cRows),R=unique(rRows);assert.equal(C.length,8);assert.equal(R.length,64);
 // Construct the global relation by matching the FULL internal port. No separate
 // output map is chosen for any root. C's two ordered input slots are fixed.
 const composite=unique(C.flatMap(c=>R.filter(r=>same(c[2],r[0])).map(r=>[c[0],c[1],r[1],r[2]])));
 assert.equal(composite.length,32);
 for(const table of [C,R])for(const row of table)for(let root=0;root<3;root++){
  const known=[...row];known[root]=null;assert.deepEqual(one(table,root,known),row[root]);localRecoveries++;
 }
 for(const row of composite){
  const [a,b,external,output]=row;
  assert.deepEqual(glueRootedComparison(layout,decomposeRootedComparison(layout,output,[0])),output);exactGlueChecks++;
  for(let root=0;root<4;root++){
   const known=[...row];known[root]=null;const global=one(composite,root,known);assert.deepEqual(global,row[root]);compositeRecoveries++;
   let staged;
   if(root===3){const internal=one(C,2,[a,b,null]);staged=one(R,2,[internal,external,null]);}
   else if(root===2){const internal=one(C,2,[a,b,null]);staged=one(R,1,[internal,null,output]);}
   else{const internal=one(R,0,[null,external,output]);staged=root===0?one(C,0,[null,b,internal]):one(C,1,[a,null,internal]);}
   assert.deepEqual(staged,global);gluingSquares++;
  }
 }
 // Hide histories ONLY in the supplied observations, while continuing to ask
 // for the missing FULL operand. Two different histories must not be merged.
 const historyQueries=new Map();
 for(const row of composite){
  const k=json([comparisonPort(row[0]),comparisonPort(row[1]),comparisonPort(row[3])]);
  if(!historyQueries.has(k))historyQueries.set(k,[]);historyQueries.get(k).push(row);
 }
 const ambiguous=[...historyQueries.values()].filter(rows=>unique(rows.map(row=>row[2])).length>1);
 assert.equal(ambiguous.length,16);
 if(!ambiguityWitness){
  const [x,y]=ambiguous[0];
  assert.deepEqual(x[0],y[0]);assert.deepEqual(x[1],y[1]);assert.deepEqual(comparisonPort(x[3]),comparisonPort(y[3]));
  assert.deepEqual(comparisonPort(x[2]),comparisonPort(y[2]));assert.notDeepEqual(x[2],y[2]);
  assert.notDeepEqual(x[3],y[3]);
  ambiguityWitness={knownInputs:[x[0],x[1]],knownOutputHeader:comparisonPort(x[3]),
   possibleMissingOperands:[x[2],y[2]],reason:'The external comparison has the same records/attachments but opposite retained child order. Full output trees distinguish it; output headers do not.'};
 }
 // Internal wires reversed by re-rooting are geometric shared faces, but not
 // arrows in this fixed incoming reading. No reverse execution is licensed here.
 const hasArrow=(from,to)=>domain.arrows.some(a=>a.from===from&&a.to===to);
 const forward=[[plus.inputs[0],plus.cell],[plus.inputs[1],plus.cell],[plus.cell,chart.target],[minus.cell,chart.target]];
 for(const [from,to] of forward){assert(hasArrow(from,to));assert(!hasArrow(to,from));}
 const reversedPathsByRoot=[[[chart.target,plus.cell],[plus.cell,plus.inputs[0]]],
  [[chart.target,plus.cell],[plus.cell,plus.inputs[1]]],[[chart.target,minus.cell]],[]];
 const attachmentAudit=reversedPathsByRoot.map((steps,root)=>({root,reversedSteps:steps,
  allStepsInFixedReading:steps.every(([from,to])=>hasArrow(from,to)),nativeRerootOperation:null}));
 assert.deepEqual(attachmentAudit.map(a=>a.allStepsInFixedReading),[false,false,false,true]);
 reports.push({binding:[p,e],comparisonRows:C.length,reconciliationRows:R.length,compositeRows:composite.length,
  comparisonRoots:rootAudit(C),reconciliationRoots:rootAudit(R),
  headerOnlyAmbiguousMissingHistoryQueries:ambiguous.length,attachmentAudit});
}
const sources=[fixturePath,'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/strominger/su32-rooted-comparison-gluing.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs',
 'research/strominger/checkers/check_su32_rerooting_and_gluing.mjs'];
const hashes={};for(const file of sources)hashes[file]=createHash('sha256').update(await fs.readFile(file)).digest('hex');
const report={schema:'su32.rerooting-gluing-test.v1',passed:true,reading:reading.id,
 localRecoveries,compositeRecoveries,gluingSquares,exactGlueChecks,reports,ambiguityWitness,
 verdict:{fullStateRecovery:'Every compatible finite relation row uniquely recovers any missing port; staged and whole-composite recovery agree.',
  independentInverseEvidence:'Recovery of prior operands uses their retention inside the full output. This is not independent evidence of native reversible dynamics.',
  headerOnlyRecovery:'Falsified for exact opaque operand history: equal record/attachment observations can require two different histories.',
  nativeRerooting:'Not established: input-root choices reverse interfaces absent from the fixed directed reading; no native reverse command was supplied.'},
 limits:['Finite Boolean relation tables, four bindings, one fixed two-operation shape; not an all-payload or all-tree cyclic-operad theorem.',
  'Unique recovery is tested only on compatible data. Incompatible supplied pairs have no completion.',
  'Deterministic missing-port recovery is a proposed stronger interface property, not a defining requirement of every abstract cyclic operad.',
  'No color duality, cyclic group action, units or higher coherence is inferred from these recovery queries.',
  'Failure in the fixed directed reading does not rule out a separately specified richer, root-changing attachment grammar.'],sourceHashes:hashes};
const dir='research/strominger/results/su32-rerooting-and-gluing-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,ambiguityWitness:undefined,sourceHashes:undefined},null,2));
