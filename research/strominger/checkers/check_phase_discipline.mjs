import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {nativePhaseFrame,auditPhaseFrame,auditPhaseSuccessor,auditPhaseCombination,auditNamedConstruction} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
import {createDeuteriumTunnel} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
import {createHelium3Tunnel} from '../demos/particle-overlap-tetrahedron/helium3-tunnel-model.mjs';
import {createHelium4Window,helium4ReaderHypothesis} from '../demos/particle-overlap-tetrahedron/helium4-window-model.mjs';
import {createAssemblyDisplay} from '../demos/particle-overlap-tetrahedron/assembly-display-model.mjs';
import {selectLithium6Reference,createLithium6Assembly} from '../demos/particle-overlap-tetrahedron/lithium6-viewer-model.mjs';
const bindings=Object.fromEntries(['C0','M0','C1','M1','C2','M2'].map((n,i)=>[n,'geometric-vertex-'+i]));
const frames=['proton','neutron','electron'].map((s,i)=>nativePhaseFrame(String(i),s,bindings)),interfaces=[{kind:'PN',from:'0',to:'1',identification:'same-occurrence',vertices:['M0','C1','M1'].map(n=>bindings[n])},{kind:'NE',from:'1',to:'2',identification:'same-occurrence',vertices:['M1','C1','C2'].map(n=>bindings[n])}];
assert.ok(frames.every(f=>auditPhaseFrame(f).status==='native-template-compatible'));assert.equal(auditPhaseCombination(frames,interfaces).status,'native-phase-compatible');
const jump=structuredClone(frames[2]);jump.context.index=4;assert.equal(auditPhaseFrame(jump).status,'invalid');assert.equal(auditPhaseSuccessor({role:'M',index:2},{role:'M',index:4}).status,'invalid');assert.equal(auditPhaseSuccessor({role:'M',index:2},{role:'M',index:3}).status,'consecutive');
const wrongRole=structuredClone(frames[0]);wrongRole.context.role='C';assert.equal(auditPhaseFrame(wrongRole).status,'invalid');
const anchored=structuredClone(frames);anchored[0].origin=0;anchored[1].origin=1;assert.ok(auditPhaseCombination(anchored,interfaces).issues.some(i=>i.kind==='declared-phase-origin-conflict'));
const noIdentification=structuredClone(interfaces);delete noIdentification[0].identification;assert.equal(auditPhaseCombination(frames,noIdentification).status,'not-phase-admitted');
const native=createDeuteriumTunnel();native.step();native.step();const nativeAudit=auditNamedConstruction(native.snapshot());assert.equal(nativeAudit.status,'native-phase-compatible');
const audits={};
for(const [name,factory,count] of [['deuterium',()=>createDeuteriumTunnel(),3],['helium3',()=>createHelium3Tunnel(),5],['helium4',()=>createHelium4Window({protonReaderRule:helium4ReaderHypothesis}),6]]){
 const display=createAssemblyDisplay(factory),first=display.snapshot();assert.equal(first.items.length,1);assert.equal(first.assemblyDisplay.canPrevious,false);
 for(let n=2;n<=count;n++){const before=display.snapshot(),after=display.next();assert.equal(after.items.length,n);assert.deepEqual(after.items.slice(0,-1),before.items);}
 const complete=display.snapshot();audits[name]=complete.phaseAudit;assert.equal(complete.assemblyDisplay.canNext,false);assert.deepEqual(display.next(),complete);
 if(name==='deuterium')assert.equal(complete.phaseAudit.status,'native-phase-compatible');else {assert.equal(complete.phaseAudit.status,'not-phase-admitted');assert.ok(complete.phaseAudit.issues.some(i=>i.kind==='local-frame'));assert.ok(Object.keys(complete.displayBindings).every(n=>n.startsWith('vertex-')));}
 for(let n=count-1;n>=1;n--)assert.equal(display.previous().items.length,n);assert.deepEqual(display.snapshot(),first);assert.deepEqual(display.previous(),first);
 for(let n=1;n<count;n++)display.next();assert.deepEqual(display.snapshot(),complete);
}
const li=selectLithium6Reference();assert.equal(li.reference.phaseAudit.status,'not-phase-admitted');assert.equal(li.reference.viewerAdmitted,false);
const nn=li.reference.edges.find(e=>e.kind==='NN-reference'),conflict=li.reference.phaseAudit.issues.find(i=>i.kind==='shared-face-phase-conflict'&&i.from===String(nn.from)&&i.to===String(nn.to));
assert.ok(conflict);assert.deepEqual(conflict.demands.map(d=>d.requiredTargetOffset).sort((a,b)=>a-b),[0,0,1]);assert.throws(()=>createLithium6Assembly(),/withdrawn/);
const out='research/strominger/results/phase-discipline';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'pass-fail-closed-phase-audit',nativePNE:nativeAudit,helium3:audits.helium3,helium4:audits.helium4,lithiumNNConflict:conflict,withdrawnLithiumModelViewerAdmitted:false,correctedViewerReceipt:'../phase-assembly/verification.json',phaseGapRejected:'M2 -> M4',validSuccessor:'M2 -> M3',geometryIDsSeparatedFromPhaseOccurrences:true,assemblyDisplayRoundTrips:true,scope:'Necessary checks from the retained local P/N/E phase templates and explicit shared-occurrence identification. These are negative controls for the withdrawn frozen-C and mixed-index models. Corrected phase-advance reference assemblies are checked separately in check_phase_assembly.mjs; physical interaction laws are still not derived.'},null,2)+'\n');
console.log('PASS phase gate and historical negatives: native P/N/E compatible; old mixed-index He readers and frozen-C Li gluing rejected. M2 -> M4 rejected. Corrected assemblies are checked separately.');
