// Finite classification of possible N-reference contractions, not admission.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const {rules:r,packets,operations,complete}=phaseUniverse({maxOrigin:4,maxPackets:5000});assert.equal(complete,true);
const ops=new Set(operations),chart=p=>r.charts[r.packets[p].chart],cell=p=>chart(p).cell,groups=new Map(),rows=[];
for(const start of packets.filter(p=>chart(p).species!=='electron')){
 function walk(current,path,visited){
  if(path.length>=4)return;
  for(const id of r.outgoing(current)){
   if(!ops.has(id))continue;const o=r.operations[id];r.validateTransfer(o);if(visited.includes(o.target))continue;
   const next=[...path,o],ids=[...visited,o.target],c=chart(o.target);
   if(c.species==='electron'){
    if(next.length<2)continue;
    const middle=ids.slice(1,-1);if(!middle.every(p=>chart(p).species==='neutron'))continue;
    const support=[...new Set(middle.map(cell))];if(support.includes(cell(start))||support.includes(c.cell))continue;
    assert.equal(r.outgoing(o.target).length,0);
    let permutation=[0,1,2,3,4];for(const step of next)permutation=step.permutation.map(i=>permutation[i]);assert.deepEqual(permutation.map(i=>r.packets[start].permutation[i]),r.packets[o.target].permutation);
    const shared=r.geometry.cells[cell(start)].vertices.filter(v=>r.geometry.cells[c.cell].vertices.includes(v));
    const endpoints=r.describe([start,o.target]),full=r.describe(ids),delta=r.packets[o.target].origin-r.packets[start].origin;
    const row={source:start,target:o.target,sourceSpecies:chart(start).species,operationIds:next.map(o=>o.id),word:next.map(o=>o.kind),removedSupportCells:support,sharedVertices:shared.length,phaseDelta:delta,permutation,endpointsCompatible:endpoints.valid,fullSupportCompatible:full.valid,endpointFailure:endpoints.reason??null,fullSupportFailure:full.reason??null};rows.push(row);
    const key=[chart(start).species,next.map(o=>o.kind).join('/'),shared.length,delta,endpoints.valid,full.valid].join('|');if(!groups.has(key))groups.set(key,{sourceSpecies:row.sourceSpecies,word:row.word,sharedVertices:row.sharedVertices,phaseDelta:delta,endpointsCompatible:endpoints.valid,fullSupportCompatible:full.valid,count:0});groups.get(key).count++;
   }else if(c.species==='neutron')walk(o.target,next,ids);
  }
 }
 walk(start,[],[start]);
}
const eligible=rows.filter(x=>x.endpointsCompatible&&x.fullSupportCompatible),direct=eligible.filter(x=>x.word.length===2&&x.word[0]==='PN'&&x.word[1]==='NE');assert.ok(direct.length);assert.ok(direct.every(x=>x.sharedVertices===2&&x.phaseDelta===0&&JSON.stringify(x.permutation)==='[3,4,2,0,1]'));
const marked=new Map(),geometric=new Map();for(const x of eligible){
 const p=r.packets[x.target],key=x.source+'|'+p.chart+'|'+p.origin,body=cell(x.source)+'|'+cell(x.target);
 for(const [map,k] of [[marked,key],[geometric,body]]){if(!map.has(k))map.set(k,[]);map.get(k).push(x);}
}
const ambiguity=map=>[...map].filter(([,xs])=>new Set(xs.map(x=>JSON.stringify(x.permutation))).size>1).map(([key,xs])=>({key,paths:xs.map(x=>({source:x.source,target:x.target,word:x.word,phaseDelta:x.phaseDelta,permutation:x.permutation}))}));
const sources=['research/strominger/checkers/probe_boundary_contractions.mjs','research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs'],sourceHashes={};for(const s of sources)sourceHashes[s]=createHash('sha256').update(await readFile(s)).digest('hex');
const result={status:'finite-boundary-contractions-classified',maxOrigin:4,maxNativePathLength:4,universePackets:packets.length,paths:rows.length,compatiblePaths:eligible.length,directPEPaths:direct.length,otherCompatiblePaths:eligible.length-direct.length,groups:[...groups.values()],markedEndpointMapAmbiguities:ambiguity(marked),geometricEndpointMapAmbiguities:ambiguity(geometric),sourceHashes,rows,scope:'All simple native paths of length 2..4 in complete origin-4 universe, ending at terminal E with exclusively N internal readers on bodies distinct from both endpoints. Check original full-support and endpoint role/contact guards. Classifies potential removal of all internal occupied N support; does not admit any contraction or establish path independence beyond the finite family. No production/viewer changes.'};
const out='research/strominger/results/boundary-contractions';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({paths:result.paths,compatiblePaths:result.compatiblePaths,directPEPaths:result.directPEPaths,otherCompatiblePaths:result.otherCompatiblePaths,markedAmbiguities:result.markedEndpointMapAmbiguities.length,geometricAmbiguities:result.geometricEndpointMapAmbiguities.length,groups:result.groups},null,2));
