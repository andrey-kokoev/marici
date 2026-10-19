import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {contractionUniverse,validateContraction,inspectContraction,guardedFamily,enumerateContractions,MODE} from '../experimental-terminal-pe.mjs';
import {buildPhaseFamily} from '../origin-assembly-family.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
const probePath='research/strominger/results/terminal-pe-probe/verification.json',probe=JSON.parse(readFileSync(probePath,'utf8'));
const paths=[probePath,'research/nima/experimental-terminal-pe.mjs','research/nima/checkers/check_experimental_terminal_pe.mjs','research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs','research/nima/origin-assembly-family.mjs'];
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),hashes=()=>Object.fromEntries(paths.map(p=>[p,hash(p)])),before=hashes();
const graphs=[];
const report={schema:'marici.nima.experimental-terminal-pe.v1',mode:MODE,scope:'Explicit new reference-support permission. Native baseline unchanged. No global sewing, physical binding, free inverse edges or isotope filtering.',families:[],hydrogen:[],deletions:[],negativeControls:[]};
for(const D of [0,1]){
 const u=contractionUniverse({maxOrigin:D}),f=guardedFamily(u),enumerated=enumerateContractions(u);assert.ok(enumerated.complete);
 const keys=new Set(enumerated.nodes.map(ids=>ids.join(',')));let accepted=0,certified=0,native=0,nativeExit=0;
 for(const edge of enumerated.edges){const from=enumerated.nodes[edge.from],to=enumerated.nodes[edge.to];assert.ok(from.includes(edge.source));assert.deepEqual(to,[...new Set([...from,edge.target])].sort((a,b)=>a-b));const a=inspectContraction(u,to);assert.ok(a.rooted);if(edge.kind===MODE)assert.ok(a.shortcuts.some(s=>s.id===edge.operation));}
 graphs.push({maxOrigin:D,nodes:enumerated.nodes,edges:enumerated.edges,shortcuts:u.shortcuts,registry:{packets:u.rules.packets,charts:u.rules.charts,cells:u.rules.geometry.cells.map(({owner,...c})=>c),operations:u.rules.operations}});
 for(let bits=0;bits<2**u.packets.length;bits++){
 const ids=u.packets.filter((p,i)=>bits&(2**i)).sort((a,b)=>a-b),a=inspectContraction(u,ids),valid=!!(a.valid&&a.rooted),exit=!!a.certifiedExit;
 assert.equal(f.accepts(ids),valid);assert.equal(f.accepts(ids,true),exit);assert.equal(keys.has(ids.join(',')),valid);
 accepted+=+valid;certified+=+exit;const n=inspectContraction(u,ids,{mode:'native'});native+=+(n.valid&&n.rooted);nativeExit+=+!!n.certifiedExit;
 }
 assert.equal(String(accepted),f.counts.configurations);assert.equal(String(certified),f.counts.exitCertificates);
 assert.equal(native,D===0?3:108);assert.equal(nativeExit,D===0?1:14);
 // Every new zero-grade edge is a same-origin edge into a native sink;
 // consequently it adds no SCC or return cycle to the native graph.
 for(const o of u.shortcuts){assert.equal(u.rules.outgoing(o.target).length,0);assert.equal(u.rules.packets[o.source].origin,u.rules.packets[o.target].origin);}
 report.families.push({maxOrigin:D,packets:u.packets.length,shortcutSchemas:u.shortcuts.length,configurations:accepted,exitCertificates:certified,nativeConfigurations:native,nativeExitCertificates:nativeExit,subsetsChecked:2**u.packets.length,constructionEdges:enumerated.edges.length,diagramNodes:f.diagram.nodes.length,complete:true});
}
const baseline=buildPhaseFamily({maxOrigin:2});assert.equal(baseline.summary.compatibleConfigurations,'198356');assert.equal(baseline.summary.selectedRecordExitCertificates,'459');report.nativeD2=baseline.summary;
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]);
for(const h of probe.hydrogen){const seedBindings=Object.fromEntries(['C0','M0','C1','M1'].map((k,i)=>[k,seed.vertices[h.marking[i]].join(',')])),u=contractionUniverse({maxOrigin:0,seedBindings}),o=u.shortcuts.find(o=>o.source===u.rules.root);assert.ok(o);
 const h1=inspectContraction(u,[o.source,o.target]),h2=inspectContraction(u,[o.source,o.referenceNeutronPacket,o.target]);assert.ok(h1.certifiedExit);assert.equal(h1.shortcuts.length,1);assert.ok(h2.certifiedExit);assert.equal(h2.shortcuts.length,0);report.hydrogen.push({marking:h.marking,h1:true,nativeH2:true});}
assert.equal(report.hydrogen.length,24);
const u4=contractionUniverse({maxOrigin:4});
for(const d of probe.deletions){const a=inspectContraction(u4,d.selectedPackets),expected=d.variants['electron-and-proton-record-terminal'];assert.equal(a.certifiedExit,expected.passesHypotheticalChecks);assert.equal(a.shortcuts.length,expected.shortcuts);assert.deepEqual(a.counts,d.counts);
 if(a.certifiedExit){const prefix=[u4.rules.root];for(const step of a.construction){prefix.push(step.target);const p=inspectContraction(u4,prefix);assert.ok(p.valid&&p.rooted);}
 assert.equal(prefix.length,d.selectedPackets.length);}
 report.deletions.push({sourceIsotope:d.sourceIsotope,removedCell:d.deletedNeutron.cell,selectedPackets:d.selectedPackets,...a});}
assert.equal(report.deletions.filter(d=>d.certifiedExit).length,4);
// Configuration non-monotonicity: native-successor selection and N-body
// occupancy disable a shortcut, but must not invalidate a native H2 path.
const u=contractionUniverse({maxOrigin:1}),g=u.rules,o=u.shortcuts.find(o=>o.source===g.root),pn=g.operations[o.nativeFactors[0]],ne=g.operations[o.nativeFactors[1]];
assert.equal(inspectContraction(u,[o.source,o.target]).shortcuts.length,1);
const occupied=inspectContraction(u,[o.source,o.referenceNeutronPacket,o.target]);assert.equal(occupied.shortcuts.length,0);report.negativeControls.push('occupied-reference-N-body');
const otherN=u.packets.find(p=>p!==o.referenceNeutronPacket&&g.charts[g.packets[p].chart].cell===o.referenceNeutronCell);
assert.notEqual(otherN,undefined);const other=inspectContraction(u,[o.source,otherN,o.target]);assert.ok(other.valid);assert.equal(other.shortcuts.length,0);report.negativeControls.push('different-packet-on-reference-N-body');
const advance=g.operations[g.outgoing(o.source).find(i=>g.operations[i].kind==='reader-phase-advance')],successor=inspectContraction(u,[o.source,advance.target,o.target]);assert.ok(successor.valid);assert.equal(successor.shortcuts.length,0);report.negativeControls.push('selected-same-body-native-successor');
function corrupted(name,change,restore){change();try{assert.throws(()=>validateContraction(g,pn,ne));report.negativeControls.push(name);}finally{restore();}}
const ep=g.packets[ne.target],origin=ep.origin,map=[...ep.permutation],pc=g.charts[g.packets[pn.source].chart],mark=pc.aliases.M1,vertices=[...g.geometry.cells[pc.cell].vertices];
corrupted('wrong-origin',()=>ep.origin++,()=>ep.origin=origin);
corrupted('wrong-map',()=>[ep.permutation[0],ep.permutation[1]]=[ep.permutation[1],ep.permutation[0]],()=>ep.permutation=map);
corrupted('wrong-reference-edge',()=>pc.aliases.M1=pc.aliases.C0,()=>pc.aliases.M1=mark);
corrupted('wrong-geometric-edge',()=>g.geometry.cells[pc.cell].vertices=vertices.map(v=>v===mark?'corrupt-vertex':v),()=>g.geometry.cells[pc.cell].vertices=vertices);
assert.equal(enumerateContractions(u,{maxConfigurations:1}).complete,false);report.negativeControls.push('configuration-resource-stop');
assert.deepEqual(hashes(),before);report.sourceHashes=before;report.status='pass-small-complete-guarded-families-and-saved-controls';
const out='research/nima/results/experimental-terminal-pe';mkdirSync(out,{recursive:true});writeFileSync(out+'/complete-small-graphs.json',JSON.stringify({mode:MODE,complete:true,cases:graphs})+'\n');writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,families:report.families,hydrogen:report.hydrogen.length,positiveIsotopes:report.deletions.filter(d=>d.certifiedExit).map(d=>({source:d.sourceIsotope,removedCell:d.removedCell,counts:d.counts,shortcuts:d.shortcuts.length})),negativeControls:report.negativeControls},null,2));
