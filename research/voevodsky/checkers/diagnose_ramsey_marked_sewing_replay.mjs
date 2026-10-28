// Diagnose the failed frozen all-markings claim without repairing the history.
import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const source='research/strominger/results/channel-assembled-native-fixture.json';
const f=JSON.parse(fs.readFileSync(source,'utf8'));
const perms=a=>a.length?a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(t=>[x,...t])):[[]];
const vs=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1'],results=[];
for(const marking of perms([0,1,2,3])){
 const r=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,vs[marking[i]]]))});
 const retained=new Set([r.root]),histories=[];let failed=null;
 for(const h of f.histories){
  let active=r.root;const operations=[];
  for(const [index,kind] of h.word.entries()){
   const offered=r.outgoing(active).map(j=>r.operations[j]),op=offered.find(o=>o.kind===kind);
   if(!op){failed={history:h.id,index,requested:kind,offered:offered.map(o=>o.kind),packet:r.packets[active],chart:r.charts[r.packets[active].chart]};break;}
   assert(r.validateTransfer(op));operations.push(op);active=op.target;retained.add(active);
  }
  histories.push({history:h.id,operations});if(failed)break;
 }
 const audit=failed?null:r.inspect([...retained]);
 if(audit)assert(audit.valid&&audit.certifiedExit&&audit.allContactsWitnessed&&!audit.pendingContacts.length);
 results.push({marking,failed,histories,audit});
}
assert(results.some(x=>x.failed)&&results.some(x=>!x.failed));
const paths=[source,'research/nima/generative-phase-assembly.mjs','research/voevodsky/checkers/diagnose_ramsey_marked_sewing_replay.mjs'];
const result={schema:'marici.ramsey-marked-sewing-replay.diagnosis.v1',
 status:'unchanged-history-all-markings-claim-falsified',contexts:24,
 successfulHistoryReplays:results.filter(x=>!x.failed).length,blockedHistoryReplays:results.filter(x=>x.failed).length,
 fullReferenceCovarianceEstablished:false,generalMarkedFamilyImpossible:false,parentDescentResolved:false,
 firstFailure:results.find(x=>x.failed),
 source_sha256:Object.fromEntries(paths.map(p=>[p,createHash('sha256').update(fs.readFileSync(p)).digest('hex')])),results};
fs.writeFileSync('research/voevodsky/results/ramsey-marked-sewing-replay-diagnosis-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({contexts:24,successful:result.successfulHistoryReplays,blocked:result.blockedHistoryReplays,firstFailure:result.firstFailure.failed}));
