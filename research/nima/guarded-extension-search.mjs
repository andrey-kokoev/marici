import {deriveObstruction} from './pne-source-obstructions.mjs';
import {inspectContraction} from './experimental-terminal-pe.mjs';
// Target-directed source search; no atlas or completed-family membership.
export function searchExtension(u,core,{maxNodes=50000,maxMilliseconds=60000}={}){
 const start=performance.now(),g=u.rules;let nodes=0,contradictions=0,inspections=0;
 const mandatory=[...new Set([g.root,...core])],schemas=[...u.operations.map(i=>g.operations[i]),...u.shortcuts];
 function branch(required,forbidden){
  if(++nodes>maxNodes)throw Error('search-node-resource-limit');if(performance.now()-start>maxMilliseconds)throw Error('search-time-resource-limit');
  const direct=inspectContraction(u,required);inspections++;if(direct.certifiedExit)return {kind:'witness',selectedPackets:required};
  const local=deriveObstruction(u,required,{forbidden});if(local.status==='obstructed'){contradictions++;return {kind:'contradiction',required,forbidden,reason:local.reason,impossible:local.impossible??[]};}
  const optional=local.survivors.filter(p=>!required.includes(p)&&!forbidden.includes(p));if(!optional.length)throw Error('Surviving full assignment did not certify');
  const stranded=new Set(direct.unrooted??[]),noExit=new Set(direct.noExit??[]);
  const score=p=>schemas.filter(o=>o.source===p&&stranded.has(o.target)).length*20+schemas.filter(o=>o.target===p&&noExit.has(o.source)).length*10+(g.charts[g.packets[p].chart].species==='electron'?5:0)-g.packets[p].origin;
  optional.sort((a,b)=>score(b)-score(a)||a-b);const p=optional[0];
  const present=branch([...required,p],forbidden);if(present.kind==='witness')return present;
  const absent=branch(required,[...forbidden,p]);if(absent.kind==='witness')return absent;
  return {kind:'split',packet:p,present,absent};
 }
 try{const result=branch(mandatory,[]);return {status:result.kind==='witness'?'sat':'unsat',nodes,contradictions,inspections,elapsedMilliseconds:performance.now()-start,...(result.kind==='witness'?{selectedPackets:result.selectedPackets}:{proof:result})};}
 catch(e){if(!['search-node-resource-limit','search-time-resource-limit'].includes(e.message))throw e;return {status:'incomplete',reason:e.message,nodes,contradictions,inspections,elapsedMilliseconds:performance.now()-start};}
}
