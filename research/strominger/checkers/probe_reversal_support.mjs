// Track occupied support separately from coefficient maps. Reversal does not
// silently contract an occupied intermediate carrier into reference geometry.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const sorted=a=>[...new Set(a)].sort((a,b)=>a-b),inv=p=>p.map((_,i)=>p.indexOf(i));
function reverse(t){return {...t,source:t.target,target:t.source,permutation:inv(t.permutation),support:[...t.support]};}
function compose(a,b){assert.equal(a.target,b.source);return {source:a.source,target:b.target,permutation:b.permutation.map(i=>a.permutation[i]),support:sorted([...a.support,...b.support])};}
function reach(root,edges){const seen=new Set([root]),q=[root];for(let i=0;i<q.length;i++)for(const e of edges)if(e.source===q[i]&&!seen.has(e.target)){seen.add(e.target);q.push(e.target);}return seen;}
const file='research/strominger/results/terminal-pe-probe/verification.json',bytes=await readFile(file),terminal=JSON.parse(bytes),rows=[];
for(const isotope of ['n15','ne22']){
 const base=`research/strominger/results/reference-${isotope}-search`,summary=JSON.parse(await readFile(base+'/verification.json')),sourceRow=summary.rows.find(r=>r.witnessFile),{rules:r}=phaseUniverse({maxOrigin:sourceRow.maxOrigin,maxPackets:5000}),cell=p=>r.charts[r.packets[p].chart].cell;
 for(const d of terminal.deletions.filter(d=>d.sourceIsotope===isotope)){
  const ids=d.selectedPackets,selected=new Set(ids),occupied=new Set(ids.map(cell)),native=ids.flatMap(p=>r.outgoing(p).map(i=>r.operations[i])).filter(o=>selected.has(o.target));
  const terms=[];for(const shortcut of d.shortcuts){
   const [pn,ne]=shortcut.nativeFactors.map(i=>r.operations[i]);r.validateTransfer(pn);r.validateTransfer(ne);
   const term=o=>({source:o.source,target:o.target,permutation:o.permutation,support:sorted([cell(o.source),cell(o.target)])});
   const a=term(pn),b=term(ne),c=compose(a,b),back=compose(reverse(b),reverse(a));assert.deepEqual(reverse(c),back);assert.deepEqual(reverse(reverse(c)),c);assert.deepEqual(c.permutation,shortcut.permutation);
   assert.deepEqual(c.support,sorted([cell(pn.source),cell(pn.target),cell(ne.target)]));assert.equal(c.support.length,3);
   const missing=c.support.filter(body=>!occupied.has(body));assert.deepEqual(missing,[shortcut.referenceNeutronCell]);
   const contracted={...c,support:sorted([cell(c.source),cell(c.target)])};assert.equal(contracted.support.length,2);assert.ok(contracted.support.every(body=>occupied.has(body)));
   // Support contraction commutes with reversal here. That establishes
   // compatibility, not derivability: both the 3-body and 2-body rule reverse.
   const reverseContracted=reverse(contracted),contractReverse={...reverse(c),support:sorted([cell(c.source),cell(c.target)])};assert.deepEqual(reverseContracted,contractReverse);
   terms.push({source:shortcut.source,target:shortcut.target,referenceNeutronCell:shortcut.referenceNeutronCell,fullTerm:c,reversedTerm:back,contractedTerm:contracted,missingOccupiedSupport:missing,coefficientMapUnchanged:true,reversalCompatibleBothBeforeAndAfterContraction:true});
  }
  const both=[...native,...native.map(o=>({...o,source:o.target,target:o.source}))],seen=reach(r.root,both);
  rows.push({sourceIsotope:isotope,deletedNeutronCell:d.deletedNeutron.cell,counts:d.counts,selectedRecords:ids.length,shortcutTerms:terms,originalUnrooted:d.baseline.unrootedPackets.length,optimisticBidirectionalNativeUnrooted:ids.filter(p=>!seen.has(p)),terminalShortcutPass:d.variants['electron-and-proton-record-terminal'].passesHypotheticalChecks});
 }
}
// Hydrogen results already retain all 24 native factors and coordinates.
const hFile='research/strominger/results/hydrogen-edge-attachment/verification.json',hBytes=await readFile(hFile),hydrogen=JSON.parse(hBytes),hResults=[];
for(const h of hydrogen.rows){const [p,n,e]=h.packets,cell=Object.fromEntries(h.packets.map((p,i)=>[p.id,h.bodies[i].cell])),[pn,ne]=h.operations,a={source:pn.source,target:pn.target,permutation:pn.permutation,support:sorted([cell[p.id],cell[n.id]])},b={source:ne.source,target:ne.target,permutation:ne.permutation,support:sorted([cell[n.id],cell[e.id]])},c=compose(a,b);assert.equal(c.support.length,3);assert.deepEqual(reverse(c),compose(reverse(b),reverse(a)));assert.deepEqual(c.permutation,h.compositePermutation);hResults.push({marking:h.marking,nativeCompositeNeedsThreeBodies:true,missingBodyForH1:cell[n.id],map:h.compositePermutation});}
const sources=[file,hFile,'research/strominger/checkers/probe_reversal_support.mjs','research/nima/generative-phase-assembly.mjs'],sourceHashes={};for(const s of sources)sourceHashes[s]=createHash('sha256').update(await readFile(s)).digest('hex');
const out='research/strominger/results/reversal-support';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'reversal-and-occupancy-contraction-separated',sourceHashes,hydrogen:hResults,rows,structuralResult:'Reversal preserves occupied support; composition unions support. Neither operation removes a required N carrier. The proposed contraction keeps the map and removes that carrier from support. Both uncontracted and contracted rules are reversal-compatible, so reversal alone does not select between them.',scope:'Support bookkeeping for existing native factors and saved deletion candidates. Bidirectional native graph is an optimistic relaxation, not a native or dual certificate. Not a derivation of reference-mediated physical transfer; no production/viewer changes.'},null,2)+'\n');console.log(JSON.stringify({hydrogenMarkings:hResults.length,shortcutTerms:rows.reduce((s,r)=>s+r.shortcutTerms.length,0),positiveCases:rows.filter(r=>r.terminalShortcutPass).map(r=>({isotope:r.sourceIsotope,deleted:r.deletedNeutronCell,remainingUnrootedEvenWithBidirectionalNative:r.optimisticBidirectionalNativeUnrooted.length,shortcutTerms:r.shortcutTerms.length}))},null,2));
