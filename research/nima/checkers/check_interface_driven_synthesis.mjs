import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync,createWriteStream,createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGzip,createGunzip} from 'node:zlib';
import {pipeline} from 'node:stream/promises';
import {once} from 'node:events';
import {createInterface} from 'node:readline';
import {contractionUniverse,guardedFamily,inspectContraction} from '../experimental-terminal-pe.mjs';
import {compileInterfaces,synthesize} from '../interface-synthesis.mjs';
const contractPath='research/nima/contracts/pne-structural-synthesis-net.v3.json',contract=JSON.parse(readFileSync(contractPath)),test=contract.added_tests.find(t=>t.id==='interface-driven-synthesis-D2');assert.ok(test);
const catalogPath='research/nima/results/pne-interface-catalog/verification.json',catalog=JSON.parse(readFileSync(catalogPath));
const paths=[contractPath,catalogPath,'research/nima/interface-synthesis.mjs','research/nima/checkers/check_interface_driven_synthesis.mjs','research/nima/experimental-terminal-pe.mjs','research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs'];
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),sourceHashes=Object.fromEntries(paths.map(p=>[p,hash(p)])),out='research/nima/results/interface-driven-synthesis';mkdirSync(out,{recursive:true});
const report={schema:'marici.nima.interface-driven-synthesis.v1',test:test.id,mode:'experimental-terminal-PE',sourceHashes,cases:[]};
for(const D of [0,1,2]){
 const u=contractionUniverse({maxOrigin:D}),c=compileInterfaces(u,catalog.cases.find(x=>x.summary.maxOrigin===D)),f=guardedFamily(u,{maxDiagramNodes:test.domain.maxDiagramNodes}),r=synthesize(c,{maxConfigurations:test.domain.maxConfigurations});
 if(!r.complete){report.status='incomplete';report.cases.push({maxOrigin:D,reason:r.reason,configurations:r.nodes.length});break;}
 assert.equal(String(r.nodes.length),f.counts.configurations);
 let exits=0,edges=0,revisits=0,peEdges=0,disabledShortcutEdges=0,maxBodies=0,maxRecords=0;
 const profiles=new Map(),nativeKey=o=>o.kind+':'+o.source+':'+o.target;
 for(let i=0;i<r.nodes.length;i++){
 const n=r.nodes[i],ids=c.decode(n.mask),a=inspectContraction(u,ids);assert.ok(a.valid&&a.rooted);assert.equal(f.accepts(ids),true);assert.equal(f.accepts(ids,true),a.certifiedExit);exits+=+a.certifiedExit;
 // Compare the entire active interface set with direct native + conditional
 // source operations. Together with target membership this audits all fanouts.
 const direct=u.operations.map(i=>u.rules.operations[i]).filter(o=>ids.includes(o.source)&&ids.includes(o.target)).map(nativeKey).concat(a.shortcuts.map(nativeKey)).sort();
 const actual=c.interfaces.filter(o=>!!(n.active&o.bit)).map(nativeKey).sort();assert.deepEqual(actual,direct);
 if(n.parent>=0){const p=r.nodes[n.parent],slot=c.index.get(n.added);assert.equal(p.mask|c.bit[slot],n.mask);assert.equal(c.update(p.active,n.mask,slot),n.active);assert.ok(c.interfaces.some(o=>(p.mask&o.sourceBit)&&o.target===n.added&&(n.active&o.bit)));}
 const count=a.counts.proton+a.counts.neutron+a.counts.electron;maxBodies=Math.max(maxBodies,count);maxRecords=Math.max(maxRecords,ids.length);const k=[a.counts.proton,a.counts.neutron,a.counts.electron].join('/');if(!profiles.has(k))profiles.set(k,{counts:a.counts,configurations:0,exitCertificates:0});profiles.get(k).configurations++;profiles.get(k).exitCertificates+=+a.certifiedExit;
 }
 assert.equal(String(exits),f.counts.exitCertificates);
 console.log(JSON.stringify({stage:'all-states-verified',maxOrigin:D,configurations:r.nodes.length,exits}));
 const gzip=createGzip({level:6}),writing=pipeline(gzip,createWriteStream(`${out}/D${D}-graph.jsonl.gz`));let buffer='';
 const put=async row=>{buffer+=JSON.stringify(row)+'\n';if(buffer.length>131072){if(!gzip.write(buffer))await once(gzip,'drain');buffer='';}};
 await put({type:'header',maxOrigin:D,mode:report.mode,configurationCount:r.nodes.length,interfaceColumns:'registry below',edgeColumns:['from','to','interfaceIndex']});
 await put({type:'registry',packets:u.rules.packets,charts:u.rules.charts,cells:u.rules.geometry.cells.map(({owner,...v})=>v),interfaces:c.interfaces.map(({forbidden,bit,sourceBit,targetBit,required,...o})=>({...o,forbiddenMask:forbidden.toString()})),variablePackets:c.packets});
 for(let i=0;i<r.nodes.length;i++){const n=r.nodes[i];await put({type:'configuration',id:i,mask:n.mask.toString(),active:n.active.toString(),parent:n.parent,added:n.added});
 for(const o of c.interfaces){if(!(n.mask&o.sourceBit))continue;const m=n.mask|o.targetBit,to=r.byMask.get(m);if(to===undefined||!(r.nodes[to].active&o.bit))continue;
 edges++;if(i===to)revisits++;if(o.kind==='experimental-terminal-PE')peEdges++;
 if(c.interfaces.some(q=>q.kind==='experimental-terminal-PE'&&(n.active&q.bit)&&!(r.nodes[to].active&q.bit)))disabledShortcutEdges++;
 await put({type:'edge',data:[i,to,o.index]});
 }}
 await put({type:'end',complete:true,configurations:r.nodes.length,edges});if(buffer)gzip.write(buffer);gzip.end();await writing;
 let decodedStates=0,decodedEdges=0,footer=null;for await(const line of createInterface({input:createReadStream(`${out}/D${D}-graph.jsonl.gz`).pipe(createGunzip()),crlfDelay:Infinity})){const row=JSON.parse(line);if(row.type==='configuration')decodedStates++;if(row.type==='edge')decodedEdges++;if(row.type==='end')footer=row;}
 assert.equal(decodedStates,r.nodes.length);assert.equal(decodedEdges,edges);assert.ok(footer.complete);assert.equal(footer.edges,edges);
 const summary={maxOrigin:D,complete:true,packets:c.packets.length,interfaces:c.interfaces.length,configurations:r.nodes.length,exitCertificates:exits,booleanCounts:f.counts,diagramNodes:f.diagram.nodes.length,edges,revisits,peEdges,disabledShortcutEdges,maxBodies,maxRecords,guardDisablingCandidates:r.guardDisablingCandidates,lostRootCandidates:r.lostRootCandidates,profiles:[...profiles.values()],archiveFooterChecked:true,graphSha256:hash(`${out}/D${D}-graph.jsonl.gz`)};
 report.cases.push(summary);console.log(JSON.stringify({...summary,profiles:summary.profiles.length}));
 if(D===0){assert.equal(synthesize(c,{maxConfigurations:1}).complete,false);report.resourceStopControl=true;}
 writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
}
assert.deepEqual(Object.fromEntries(paths.map(p=>[p,hash(p)])),sourceHashes);report.status=report.cases.every(c=>c.complete)?'pass-complete-interface-driven-D012':'incomplete';writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
