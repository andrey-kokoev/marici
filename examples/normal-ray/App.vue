<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import {useClipboard} from '@vueuse/core';
import {orientationCompass} from './orientation-compass.js';
import {cellulationStartTranslation} from '../../research/realization-tower/cellulation-placement.mjs';
import {cellulationSteps} from '../../research/realization-tower/cellulation-steps.mjs';
import NNPEComposition from './NNPEComposition.vue';
import SulfurReferencePanel from './SulfurReferencePanel.vue';
import {hexStrandIds,hexStrandStageNames,hexStrandStages} from '../../research/realization-tower/hex-strands-view.mjs';
import {buildFiveSideOctWiring} from '../../research/realization-tower/five-side-oct-wiring.mjs';
import {buildSulfurIncomingBundle} from '../../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurTubeNetwork} from '../../research/realization-tower/sulfur-32-tube-network.mjs';
import {esd7NodePlanes} from './esd7-node-planes.js';
import {retainedExpansionAtoms} from './retained-expansion-renderer.js';
import { useViewerModel } from './useViewerModel.js';
import {cellFibrationStages} from '../../research/realization-tower/cell-fibration-process.mjs';
import {esd7CellId} from '../../research/realization-tower/esd7-cell-ids.mjs';
import {zeroNeutralValues} from '../../research/realization-tower/neutral-state-extension.mjs';
const props=defineProps({host:{type:HTMLElement,required:true}});
const m=useViewerModel({processId:'retained-construction'});
const {process,appearance,motion,locks,panels,sections,phase,error,view,k,status,summary,counts,pneInventory,polarityCounts,neutralValues,selectedNeutralMode,cut,cutAudit}=m;
const compass=computed(()=>orientationCompass(view.quaternion));
const isBeryllium=computed(()=>['beryllium-8','beryllium-9'].includes(process.id));
const berylliumLabel=computed(()=>process.id==='beryllium-9'?'Be-9':'Be-8');
const seedActive=computed(()=>isBeryllium.value||process.id==='sulfur-32'&&appearance.sulfurBranchSeed);
const cellulationView=computed(()=>process.id==='sulfur-32'&&appearance.sulfurCellulation);
let cellulationCamera=cellulationView.value?m.savedCamera:null;
const compositionView=computed(()=>process.id==='sulfur-32'&&appearance.sulfurComposition);
const channelView=computed(()=>process.id==='sulfur-32'&&appearance.sulfurChannels);
const retainedExpansionView=computed(()=>process.id==='sulfur-32'&&appearance.sulfurRetainedExpansion);
const retainedExpansionLabels=['White dot','Grow one arrow','Open two white triangles into a square','Color the square red / blue','Add the white X-axis diagonal','Helium-3 · split both halves vertically','Helium-4 · add the vertical white diagonal','Lithium-6 · split the upper-right along x=y','Lithium-7 · separate the right pair','Beryllium-9 · divide the left-center face','Boron-10 · split the upper-right face','Boron-11 · separate the upper-right pair','Carbon-12 · subdivide the upper-right triangle','Carbon-13 · separate the smaller pair','Nitrogen-14 · split the opposite upper face','Nitrogen-15 · separate the upper-left pair','Oxygen-16 · subdivide the topmost left triangle','Oxygen-17 · separate the smaller left pair','Fluorine-19 · split the topmost right triangle','Neon-20 · split the left-center face'];
const compactSulfurView=computed(()=>channelView.value||compositionView.value||cellulationView.value||retainedExpansionView.value);
const be9Wiring=computed(()=>process.id==='beryllium-9'&&appearance.be9View==='wiring-single-procedure');
const be9Assembly=computed(()=>process.id==='beryllium-9'&&appearance.be9View==='3d-assembly');
const seedDepth=computed(()=>isBeryllium.value?4:8);
const nIdentityNetwork=computed(()=>process.id==='sulfur-32'&&appearance.sulfurWireBundle?buildSulfurTubeNetwork(buildSulfurIncomingBundle()):null);
watch(()=>appearance.cellulationStep,()=>{appearance.cellulationWitnessAction=-1;});
watch(()=>appearance.cellulationAnimate,on=>{if(on)appearance.cellulationWitnessAction=-1;});
watch(()=>appearance.hexStrandStage,()=>{if(appearance.hexStrandCopy>=2**appearance.hexStrandStage)appearance.hexStrandCopy=-1;});
const selectedReflectionCopy=computed(()=>process.id==='sulfur-32-reflection'?m.state.value.copies.find(c=>c.id===appearance.reflectionCopy):null);
watch(()=>[process.id,process.step],()=>{if(process.id==='sulfur-32-reflection'&&!m.state.value.copies.some(c=>c.id===appearance.reflectionCopy))appearance.reflectionCopy='all';});
const selectedNIdentity=computed(()=>nIdentityNetwork.value?.identities.find(g=>g.id===appearance.sulfurNIdentity));
import {doubleEsd7Rules as doubleRules} from '../../research/realization-tower/double-esd7-process.mjs';
const publishedBelt=globalThis.location?.pathname.startsWith('/experiments/native-belt/');
if(new URLSearchParams(globalThis.location?.search).get('preset')==='native-belt'){
 m.selectProcess('double-esd7');process.k=7;appearance.rimAssembly=true;appearance.parentHalfStepTrim=false;appearance.cellGraph=false;appearance.edgesOnly=false;appearance.doubleRules=['P-branch'];
 appearance.complexVisibility={original:true,clone:true,belt:true};appearance.beltLayers.fill(true);appearance.nativeBeltLayers.fill(true);appearance.esd7Layers.fill(true);cut.enabled=false;motion.spin=false;motion.axialRotation=false;
 const url=new URL(globalThis.location.href);url.searchParams.delete('preset');globalThis.history.replaceState(null,'',url);
}
const vertexLabels=ref([]),lifetime=new AbortController();
const inventoryDetails=ref(false),coherenceGroup=ref('all');
const coherenceGroups=computed(()=>process.id==='ruthenium-98'&&appearance.rutheniumView==='wiring'?buildFiveSideOctWiring().coherenceGroups:[]);
const cutVertices=[{value:'all',label:'All'},{value:2,label:'P',color:'#1265a8'},{value:1,label:'N1',color:'#e5eaf0'},{value:4,label:'N2',color:'#e5eaf0'},{value:3,label:'E',color:'#a82664'}];
const hoveredCell=ref(null),copyFeedback=ref(''),dotCopyError=ref('');
const {copy:copyDotClipboard,text:copiedDotId,copied:dotIdCopied,isSupported:dotCopySupported}=useClipboard({copiedDuring:4000});
const {copy:copyCellClipboard,isSupported:cellCopySupported}=useClipboard();
const dotCopyFeedback=computed(()=>dotCopyError.value||(dotIdCopied.value?`Copied ID: ${copiedDotId.value}`:''));
async function copyDotId(dot){
 dotCopyError.value='';
 try{
  if(!dotCopySupported.value)throw Error('Clipboard unavailable');
  await copyDotClipboard(dot.id);
 }catch{dotCopyError.value=`Clipboard unavailable. ID: ${dot.id}`;}
}
const formatPosition=xs=>xs.map(x=>Number(x.toFixed(4))).join(', ');
function cellulationDotLabel(dot){return `ID: ${dot.id}\nLattice (x, y, z): (${dot.latticePoint.join(', ')})\nWorld (x, y, z): (${formatPosition(dot.point)})\nClick to ${dot.locked?'release':'fix'} this dot and its normal.\nDouble-click to copy its ID.`;}
const formatFaces=fs=>fs.map(f=>f.join('–')).join(' / ');
async function copyCellInfo(mode='info'){
 if(!hoveredCell.value)return;
 const {x,y,pinned,...info}=hoveredCell.value;
 try{if(!cellCopySupported.value)throw Error('Clipboard unavailable');await copyCellClipboard(mode==='id'?String(info.id):JSON.stringify(info,null,2));copyFeedback.value=mode==='id'?'ID copied':'Copied';}
 catch{copyFeedback.value='Copy unavailable; select the text below.';}
}
const fillerDisplay=ref('input'),fillerCoordinate=ref(0),neutralCoordinate=ref(0);
function editNeutral(part,event){
 const raw=event.target.value,n=Number(raw);
 if(raw.trim()===''||!Number.isFinite(n)||Math.abs(n)>1e6){if(event.type==='change')event.target.value=neutralValues.value[selectedNeutralMode.value][neutralCoordinate.value][part];return;}
 if(neutralValues.value[selectedNeutralMode.value][neutralCoordinate.value][part]===n)return;
 neutralValues.value=neutralValues.value.map((p,i)=>i===selectedNeutralMode.value?p.map((z,c)=>c===neutralCoordinate.value?z.map((x,j)=>j===part?n:x):z):p);
}
function setCutDepth(n,field){
 if(!Number.isInteger(n)||n<0||n>6)return;
 cut[field]=n;
 if(cut.startLayer>cut.layer){if(field==='startLayer')cut.layer=n;else cut.startLayer=n;}
}
const formatFillerCoefficient=z=>`${z[0]}${z[1]<0?'':'+'}${z[1]}i`;
let viewer;
function failure(e){motion.spin=false;motion.axialRotation=false;error.value=e.message;phase.value='fallback';}
function reset(){motion.spin=false;motion.axialRotation=false;Object.assign(locks,{v1:false,v2:false,v3:false,v4:false,v5:false});viewer?.reset();}
function recenter(){motion.spin=false;motion.axialRotation=false;viewer?.recenter();}
function dispose(){m.disposeSettings();lifetime.abort();viewer?.dispose();motion.spin=false;motion.axialRotation=false;phase.value='fallback';}
function angles(axis,event){const value=Number(event.target.value);viewer?.angles(axis==='azimuth'?value:view.azimuth,axis==='elevation'?value:view.elevation);}
function togglePanel(name){panels[name]=!panels[name];requestAnimationFrame(()=>document.getElementById(`${panels[name]?'close':'open'}-${name}`)?.focus());}
watch(()=>({...m.renderState.value,coherenceGroup:coherenceGroup.value}),s=>viewer?.update(s),{flush:'post'});
watch(()=>process.id,id=>{if(id==='sulfur-32-reflection')viewer?.angles(15,20);},{flush:'post'});
watch(()=>process.id==='sulfur-32'&&appearance.sulfurHexStrands,on=>{if(on)viewer?.angles(55,20);},{flush:'post'});
function planarSeedView(){motion.spin=false;motion.axialRotation=false;viewer?.restoreView({targetOffset:[0,0,0],offset:[0,0,40],up:[0,1,0],zoom:1});}
function seedLayersView(){motion.spin=false;motion.axialRotation=false;viewer?.restoreView({targetOffset:[0,0,0],offset:be9Wiring.value?[0,0,32]:[24,16,32],up:[0,1,0],zoom:1});}
watch(retainedExpansionView,on=>{if(on)planarSeedView();},{flush:'post'});
watch(compositionView,on=>{if(on){motion.spin=false;motion.axialRotation=false;viewer?.restoreView({targetOffset:[0,0,0],offset:[12,8,24],up:[0,1,0],zoom:1});}},{flush:'post'});
watch(cellulationView,on=>{if(on){if(cellulationCamera)viewer?.restoreView(cellulationCamera);else reset();}},{flush:'post'});
watch(be9Wiring,()=>{if(seedActive.value)seedLayersView();},{flush:'post'});
watch(seedActive,on=>{if(on)seedLayersView();},{flush:'post'});
watch(()=>[panels.process,panels.scene],([p,s])=>{document.body.classList.toggle('process-closed',!p);document.body.classList.toggle('scene-closed',!s);},{immediate:true});
onMounted(async ()=>{
 window.addEventListener('pagehide',event=>{if(event.persisted)m.flushSettings();else m.disposeSettings();},{signal:lifetime.signal});
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 if(reduced.matches)m.suspendMotion();
 // Ignore media-query teardown notifications from the departing document.
 reduced.addEventListener('change',()=>requestAnimationFrame(()=>{if(!lifetime.signal.aborted&&reduced.matches)m.suspendMotion();}),{signal:lifetime.signal});
 try{
  const {createViewer}=await import('./scene.js');
  if(lifetime.signal.aborted)return;
  viewer=createViewer({host:props.host,signal:lifetime.signal,onFailure:failure,onCellHover:info=>{hoveredCell.value=info;copyFeedback.value='';},onView:(v,a)=>{
   view.cellulationWitness=v.cellulationWitness;view.loopValidation=v.loopValidation;view.loopOverlay=v.loopOverlay;view.quaternion=v.quaternion;view.azimuth=v.azimuth;view.elevation=v.elevation;view.nnpePorts=v.nnpePorts;view.cellulationDots=v.cellulationDots;view.cellulationGridLabels=v.cellulationGridLabels;view.gridVertexCandidate=v.gridVertexCandidate;vertexLabels.value=v.vertexLabels;m.captureCamera(v.camera);
   if(a?.view==='cellulation'){
    cellulationCamera=v.camera;
    if(appearance.cellulationTranslation===null)appearance.cellulationTranslation=cellulationStartTranslation(v.quaternion);
   }
   // Compatibility diagnostics, now emitted only on rendered changes.
   globalThis.normalRayViewAudit=v;globalThis.normalRayAudit=a;
  }});
  if(lifetime.signal.aborted){viewer.dispose();return;}
  phase.value='ready';viewer.update(m.renderState.value);
  if(m.savedCamera)viewer.restoreView(m.savedCamera);else if(cellulationView.value)reset();
  if(seedActive.value)seedLayersView();
  if(retainedExpansionView.value)planarSeedView();
 }catch(e){if(!lifetime.signal.aborted)failure(e);}
});
onUnmounted(()=>{dispose();document.body.classList.remove('process-closed','scene-closed');});
defineExpose({dispose,inspectView:({cell,zoom=3,axis}={})=>{if(axis){if(!['x','y','z'].includes(axis))throw Error('Invalid inspection axis');viewer?.axis(axis);}viewer?.focusCell(cell,zoom);},snapshot:()=>({...viewer?.snapshot(),phase:phase.value})});
</script>

<template>
 <aside id="process-panel" aria-label="Process controls" v-show="panels.process">
  <button id="close-process" class="panel-close" aria-label="Close process panel" aria-controls="process-panel" @click="togglePanel('process')">×</button>
  <p v-if="publishedBelt"><a href="/experiments/">← Gallery</a> · <a href="/experiments/native-belt-guide">Guide and scope</a></p>
  <h2>Process</h2>
  <p v-if="process.id==='fibration-12x12'"><a id="cellulation-view" href="./cellulation.html">Tetrahedral–octahedral cellulation</a></p>
  <label for="process-select">Construction process</label>
  <select id="process-select" :value="process.id" :disabled="phase!=='ready'" @change="m.selectProcess($event.target.value)">
   <option v-for="item in m.processes" :key="item.id" :value="item.id">{{item.name}}</option>
  </select>
  <div v-if="!['double-esd7','neutron-belt'].includes(process.id) && !seedActive && !compactSulfurView" class="row process-navigation"><button id="prev" :disabled="phase!=='ready'||process.step===0" @click="m.move(-1)">← Previous</button><button id="next" :disabled="phase!=='ready'||!m.canAdvance.value" @click="m.move(1)">Next →</button></div>
  <p v-if="be9Wiring" id="wiring-procedure" class="process-stage" role="status">{{['Start · 8 strands / 16 wires','Step 1 · Midpoint twist 180°'][appearance.be9WiringStep]}}</p>
  <div v-if="be9Wiring" class="row process-navigation"><button id="be9-wiring-prev" :disabled="appearance.be9WiringStep===0" @click="appearance.be9WiringStep--">← Previous</button><button id="be9-wiring-next" :disabled="appearance.be9WiringStep===1" @click="appearance.be9WiringStep++">Next →</button></div>
  <p v-if="be9Assembly" id="assembly-procedure" class="process-stage" role="status">Step {{appearance.be9AssemblySides?3:appearance.be9AssemblyFold?2:1}} · {{appearance.be9AssemblySides?'Four triangular faces · side folds 60°':appearance.be9AssemblyFold?'Fold at red/blue midpoints · 60°':'8-simplex · 120°'}}</p>
  <div v-if="be9Assembly" class="row process-navigation"><button id="be9-assembly-prev" :disabled="!appearance.be9AssemblyFold" @click="appearance.be9AssemblySides?appearance.be9AssemblySides=false:appearance.be9AssemblyFold=false">← Previous</button><button id="be9-assembly-next" :disabled="appearance.be9AssemblySides" @click="appearance.be9AssemblyFold?appearance.be9AssemblySides=true:appearance.be9AssemblyFold=true">Next →</button></div>
  <p v-if="!compactSulfurView && !be9Assembly && !be9Wiring && !['double-esd7','neutron-belt'].includes(process.id)" id="procedure" class="process-stage" role="status"><template v-if="m.state.value.cellFibrationAudit">{{process.step===9?'Interior pairs':process.step===8?'Opposite-face quartets':process.step===7?'Layer 3 · remaining cells':process.step===6?'Central cells':process.step===5?'Surface triangles':process.step===4?'Layer 2 · inner hexagons':m.state.value.cellFibrationAudit.complementaryLayer?'Complementary layer '+m.state.value.cellFibrationAudit.complementaryLayer:'Layer '+m.state.value.cellFibrationAudit.layer}}</template><template v-else>Step {{process.step}}</template><small v-if="m.state.value.cellFibrationAudit" id="process-step-index">Step {{process.step}} / {{cellFibrationStages.length-1}}<span v-if="!m.canAdvance.value"> · End of defined steps</span></small><small v-else-if="!m.canAdvance.value">End of defined steps</small></p>
  <section v-if="process.id==='pair-context-7x4'" id="pair-context-audit" aria-label="Seven contexts and four depths">
   <p>Depth {{m.state.value.pairContextAudit.depth}}/4 · {{m.state.value.pairContextAudit.context.join('–')}} · {{m.state.value.pairContextAudit.confirmation}}</p>
   <p>Blue: P face · magenta: E face · pale: N witness · gold: selected context / flow. The seven endpoint contexts exclude the mixed N face.</p>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
    <div v-for="(entry,key) in m.state.value.pairContextAudit.bank" :key="key" style="border:1px solid #52697d;padding:6px">
     <strong>{{key}}</strong> · {{entry.kind}}
     <p v-if="entry.readFrom">{{entry.readFrom==='P'?'P → E':'E → P'}}</p>
     <small>{{entry.coefficients.map(z=>`${z[0]}${z[1]<0?'':'+'}${z[1]}i`).join(', ')}}</small>
    </div>
   </div>
   <details><summary>Confirmed reversal history</summary><p v-for="(h,i) in m.state.value.pairContextAudit.actionHistory" :key="i">{{i+1}}. {{h.action}} · orientation {{h.orientation}}</p></details>
   <p>28 indexed positions, not 28 particles. Four is a chosen retained depth. Coefficients are test values; this is not surface-layer growth.</p>
  </section>
  <section v-if="m.state.value.neutronBeltAudit" id="neutron-belt-audit"><h3>Annular belt</h3><p>6 cones · 3 opposite-circulation pairs · 2 caps excluded</p><p>Teal: + circulation · violet: − circulation</p><p>Intrinsic transfers: 432 + 108 + 1296 = 1836</p><p>Circulation signs are not P/E labels. Parent attachment and branch-converting interface remain undefined.</p></section>
  <section v-if="m.state.value.doubleEsd7Audit" id="double-esd7-audit"><h3>ESD7</h3><div id="complex-visibility" class="row" role="group" aria-label="Complex visibility"><button id="toggle-first-esd7" type="button" :aria-pressed="appearance.complexVisibility.original" @click="appearance.complexVisibility.original=!appearance.complexVisibility.original">1</button><button id="toggle-second-esd7" type="button" :aria-pressed="appearance.complexVisibility.clone" @click="appearance.complexVisibility.clone=!appearance.complexVisibility.clone">2</button><button id="toggle-connecting-belt" type="button" :aria-pressed="appearance.complexVisibility.belt" @click="appearance.complexVisibility.belt=!appearance.complexVisibility.belt">Belt</button></div><details id="esd7-layer-visibility"><summary>Both ESD7s · node planes · face → tip</summary><div class="row esd7-plane-buttons" role="group" aria-label="Synchronized ESD7 node planes"><button id="esd7-planes-all" type="button" @click="appearance.esd7Layers=esd7NodePlanes.map(()=>true)">All</button><button id="esd7-planes-none" type="button" @click="appearance.esd7Layers=esd7NodePlanes.map(()=>false)">None</button><button v-for="plane in esd7NodePlanes" :key="plane.index" type="button" :id="'toggle-esd7-plane-'+(plane.index+1)" :aria-pressed="appearance.esd7Layers[plane.index]" :title="plane.label+' · '+plane.count+' nodes per half'" @click="appearance.esd7Layers[plane.index]=!appearance.esd7Layers[plane.index]">{{plane.index+1}} ({{plane.count}})</button></div></details><label class="check"><input id="rim-assembly" v-model="appearance.rimAssembly" type="checkbox"> Separated central belt</label><label v-if="appearance.rimAssembly" class="check"><input id="parent-half-step-trim" v-model="appearance.parentHalfStepTrim" type="checkbox"> Experimental P-first half-step trim</label><p v-if="m.state.value.parentTrimAudit" id="parent-trim-audit">Removed {{m.state.value.parentTrimAudit.removed.proton}} P cells. Whole-cell centre cut; E contact tips retained. Exposes more P-oriented N-cell faces—not a balanced surface or verified duality cycle.</p><label for="shape-view">All shapes <select id="shape-view" :value="appearance.cellGraph?'wiring':'geometry'" @change="appearance.cellGraph=$event.target.value==='wiring'"><option value="wiring">Wiring</option><option value="geometry">Geometry</option></select></label><div v-if="m.state.value.centralBeltAudit && appearance.cellGraph" id="belt-layer-visibility" class="row" role="group" aria-label="Belt layer visibility"><button v-for="plane in m.nativePlanes.value" :key="plane.index" :id="'toggle-native-belt-plane-'+(plane.index+1)" type="button" :aria-pressed="appearance.nativeBeltLayers[plane.index]" :title="'Native cell-centre plane '+(plane.index+1)+' · '+plane.count+' cells'" @click="appearance.nativeBeltLayers[plane.index]=!appearance.nativeBeltLayers[plane.index]">{{plane.label}}</button></div><p>{{m.state.value.doubleEsd7Audit.filledCount}} / {{m.state.value.doubleEsd7Audit.bodyCount}} filled · {{m.state.value.doubleEsd7Audit.unfilledCount}} empty</p><details id="rule-preview"><summary>Rules</summary><label v-for="r in doubleRules" :key="r.id" class="check"><input type="checkbox" :data-double-rule="r.id" :checked="appearance.doubleRules.includes(r.id)" :disabled="phase!=='ready'" @change="m.toggleDoubleRule(r.id,$event.target.checked)">{{r.label}}</label><p id="rule-preview-count">{{m.state.value.doubleEsd7Audit.rulePreview.candidates.length}} new cells · {{m.state.value.doubleEsd7Audit.rulePreview.rounds.length}} rounds · {{m.state.value.doubleEsd7Audit.rulePreview.conflicts.length}} conflicts</p><label class="check"><input id="highlight-rule-preview" v-model="appearance.highlightRulePreview" type="checkbox"> Highlight candidates with all rules</label><p v-if="!m.state.value.doubleEsd7Audit.rulePreview.valid">Blocked: conflicting assignments.</p><details v-if="m.state.value.doubleEsd7Audit.rulePreview.conflicts.length"><summary>Conflicts</summary><p v-for="c in m.state.value.doubleEsd7Audit.rulePreview.conflicts" :key="c.id">{{c.id}}: existing {{c.existingRole??'empty'}}; {{c.arrivals.map(a=>a.source+' → '+a.role+' ('+a.rule+')').join('; ')}}</p></details></details></section>
  <section v-if="['single-octahedral','signed-octahedral-belt','native-octahedral-bridge'].includes(process.id)" id="signed-octahedral-audit"><h3>{{process.id==='single-octahedral'?'Single octahedron':process.id==='native-octahedral-bridge'?'Native grown bridge':'Octahedral pair + belt'}}</h3><label>Edge units <select id="octahedral-size" v-model.number="process.step"><option v-for="r in (process.id==='native-octahedral-bridge'?[0,1,2]:[0,1,2,3])" :key="r" :value="r">{{2*r+1}}</option></select></label><label>View <select id="octahedral-view" :value="appearance.cellGraph?'wiring':'geometry'" @change="appearance.cellGraph=$event.target.value==='wiring'"><option value="geometry">Geometry</option><option value="wiring">Wiring</option></select></label><div v-if="process.id!=='single-octahedral'" class="row"><button v-for="part in ['original','clone','belt']" :key="part" :id="'octahedral-toggle-'+part" :aria-pressed="appearance.complexVisibility[part]" @click="appearance.complexVisibility[part]=!appearance.complexVisibility[part]">{{part==='original'?'1':part==='clone'?'2':process.id==='native-octahedral-bridge'?'Bridge':'Belt'}}</button></div><p v-if="process.id==='native-octahedral-bridge'" id="native-bridge-audit">49 added cells + 2 shared N terminals. 576 shortest paths; four shared faces per parent, no point-only links. Shared terminals remain visible with either their parent or the bridge. Growth criterion is a trial, not a transport law.</p><p v-else-if="process.id==='single-octahedral'">One native octahedron; no second shape or bridge. ±P / ±N / ±E are boundary ports, not cell-role overrides.<br><label>Surface colouring <select id="single-face-colouring" v-model="appearance.singleFaceColoring"><option value="cell-role">P / N / E cell roles</option><option value="orientation">P / E face orientations</option></select></label><br>Void trial: P/E occupied, N empty. Shared-face connectivity gives {{m.state.value.emptyRegionAudit.enclosedRegions}} enclosed filler regions. Edge-touching closures form {{m.state.value.emptyRegionAudit.edgeTouchComponents}} component(s), but edges are not open passages.</p><p v-else>Each parent: +P / −P, +N / −N, +E / −E. Signed boundary ports, not cell-role assignments. Same extended belt; two vertex contacts, no directed transport.</p><details v-if="m.state.value.nTubeAudit" id="n-tube-trial"><summary>N tube routing trial</summary><label>Overlay <select id="n-tube-axis" v-model="appearance.nTubeAxis"><option value="off">Off</option><option value="all">All six directions</option><option value="response">Uncoupled response (reference)</option><option value="coupled">P/E-coupled response (trial)</option><option v-for="a in m.state.value.nTubeAudit.axisCounts" :key="a.axis" :value="String(a.axis)">{{a.label}} · {{a.paths}} channels</option></select></label><p>Six opposite-edge strands per N cell. {{m.state.value.nTubeAudit.localPasses}} local passes compress to {{m.state.value.nTubeAudit.compressedPaths}} distinct channels; crossings do not merge.</p><p>White dashed overlay, including interior strands. Edge-port assumption—not open voids or particle counts. P/E strands themselves remain undefined.</p><p v-if="m.state.value.ambientNeutralAudit" id="ambient-neutral-audit">Ambient comparison: {{m.state.value.ambientNeutralAudit.ambientMatchedChannels}} unchanged channels; {{m.state.value.ambientNeutralAudit.addedOrChangedChannels}} changed/new. All {{m.state.value.ambientNeutralAudit.channelsExtendingAtBothEnds}} continue beyond both ends of the observation window.<br>The uncoupled reference ignores P/E occupancy. Localized neutron count remains undefined—not zero.</p><p v-if="m.state.value.peCoupledRoutingAudit" id="pe-coupled-routing-audit">P/E-coupled trial: {{m.state.value.peCoupledRoutingAudit.changedOpenChannels}} rerouted channels, {{m.state.value.peCoupledRoutingAudit.dualResponsePairs}} geometric dual pairs; {{m.state.value.peCoupledRoutingAudit.closedLoops}} closed loops.<br>Reference rule only: symmetry does not force 126 pairs. An equally symmetric companion-strand rule gives 198 pairs and closed loops. Route pairs are not identified with neutrons. Overlay shows the response-bearing portions; ambient tails are omitted.</p></details><details v-if="m.state.value.interiorNPairingAudit" id="interior-n-trial"><summary>Interior N pairing trial</summary><p>{{m.state.value.interiorNPairingAudit.interiorNCells}} N cells = {{m.state.value.interiorNPairingAudit.inversionPairs}} inversion pairs + {{m.state.value.interiorNPairingAudit.fixedCells.length}} fixed cell(s).</p><p>Uniform amplitude net: {{m.state.value.interiorNPairingAudit.uniform.total}}.<br>Opposed pairs + central 1: {{m.state.value.interiorNPairingAudit.opposedWithCentralOne.total}}.<br>Odd N-axis amplitude net: {{m.state.value.interiorNPairingAudit.axialOdd.total}}.</p><p>Trial scalar amplitudes, not particle counts. All cells and pair contrasts retained; opposite signs are imposed, not derived dynamics.</p></details></section>
  <section v-if="process.id==='ruthenium-98'" id="ruthenium-98-audit">
   <h3>5-side oct</h3>
   <p>Edge units: 5 · octahedral carrier · 245 native cells.</p>
   <label>View <select id="ruthenium-98-view" v-model="appearance.rutheniumView"><option value="geometry">Geometry</option><option value="lattice">Lattice</option><option value="wiring">Wiring</option></select></label>
   <p v-if="appearance.rutheniumView==='wiring'" id="ruthenium-wiring-info">80 P/E fibres · 320 slot wires. Explicit routing through all 340 channels inside 85 N fillers, linked into 62 coherence groups. Solid lines are cell-internal connections; dashed gold lines are boundary-lift seams, not native adjacencies.</p>
   <template v-if="appearance.rutheniumView==='wiring'">
    <label>Coherence group <select id="oct-coherence-group" v-model="coherenceGroup" @change="appearance.faceOpacity=.12"><option value="all">All groups</option><option v-for="g in coherenceGroups" :key="g.id" :value="g.id">{{g.id}} · {{g.members.length}} N · {{g.wireIds.length}} wires</option></select></label>
    <button id="oct-inspect-interior" @click="appearance.faceOpacity=.12">Reveal internal routing</button>
   </template>
   <label v-if="appearance.rutheniumView==='wiring'">Wiring opacity {{Math.round(appearance.rutheniumWireOpacity*100)}}% <input id="ruthenium-wire-opacity" type="range" min="0" max="1" step="0.01" v-model.number="appearance.rutheniumWireOpacity"></label>
   <p v-else>Whole-cell geometry and native shared-face lattice. P/E colours distinguish tetrahedral orientations; N marks octahedra.</p>
  </section>
  <section v-if="process.id==='sulfur-32-reflection'" id="sulfur-reflection-audit">
   <h3>Sulfur-32 reflection</h3>
   <label>Stage <select id="reflection-stage" v-model.number="process.step"><option :value="0">0 · Regular 4-simplex</option><option :value="1">1 · White reflection</option><option :value="2">2 · First 120° rotation</option><option :value="3">3 · Outer-red reflection</option><option :value="4">4 · Second 120° rotation</option></select></label>
   <label>View <select id="reflection-view" v-model="appearance.reflectionView"><option value="geometry">Geometry</option><option value="wiring">Wiring</option></select></label>
   <label>4D projection angle {{appearance.reflectionAngle}}° <input id="reflection-angle" type="range" min="-90" max="90" step="1" v-model.number="appearance.reflectionAngle"></label>
   <label v-if="appearance.reflectionView==='geometry'" class="check"><input id="reflection-cycle" type="checkbox" v-model="appearance.reflectionCycle"> Show central contact circuit</label>
   <label>Copy history <select id="reflection-copy" v-model="appearance.reflectionCopy"><option value="all">All copies</option><option v-for="c in m.state.value.copies" :key="c.id" :value="c.id">{{c.id}} · {{c.word.join(' → ') || 'seed'}}</option></select></label>
   <p id="reflection-counts">{{m.state.value.reflectionAudit.histories}} retained histories · {{m.state.value.reflectionAudit.cells}} distinct regular 4-simplexes · {{m.state.value.reflectionAudit.contacts}} shared-edge contacts.</p>
   <p v-if="appearance.reflectionView==='wiring'">{{m.state.value.reflectionBundle.strands.length}} retained strands, present at both ends. White, blue-white, red-white and blue strands follow copy histories through the reflected assembly, without merging coincident copies.</p>
   <label v-if="appearance.reflectionView==='wiring'">Wiring opacity {{Math.round(100*appearance.reflectionWireOpacity)}}% <input id="reflection-wire-opacity" type="range" min="0" max="1" step=".01" v-model.number="appearance.reflectionWireOpacity"></label>
   <p v-if="appearance.reflectionView==='geometry'">Blue cells form the central circuit. Pink and gold vertices are v₃ and v₄. Every simplex retains all five vertices and ten edges.</p>
   <p v-if="process.step===4 && appearance.reflectionView==='geometry'">Six seam reflections return the complete frame and all five labels exactly.</p>
   <p v-if="selectedReflectionCopy">{{selectedReflectionCopy.id}} · parent {{selectedReflectionCopy.parent ?? 'none'}} · {{selectedReflectionCopy.word.join(' → ') || 'seed'}}</p>
  </section>
  <section v-if="['sulfur-32','beryllium-8','beryllium-9'].includes(process.id)" :id="process.id+'-audit'">
   <h3 v-if="!compactSulfurView">{{isBeryllium?berylliumLabel:'Sulfur-32'}}</h3><p v-if="process.id==='sulfur-32' && !appearance.sulfurBranchSeed && !compactSulfurView">Edge units: 3 · {{m.state.value.retainedBodies.length}} whole geometric cells.</p>
   <label v-if="process.id==='beryllium-9'">View <select id="beryllium-9-view" v-model="appearance.be9View"><option value="branching-seed">White-rooted hex simplex</option><option value="3d-assembly">3D assembly</option><option value="wiring-single-procedure">Wiring single procedure</option></select></label>
   <label v-else-if="process.id==='beryllium-8'">View <select id="beryllium-8-view" value="branching-seed"><option value="branching-seed">White-rooted hex simplex</option></select></label>
   <label v-else>View <select id="sulfur-32-view" :value="appearance.sulfurRetainedExpansion?'retained-expansion':appearance.sulfurCellulation?(appearance.cellulationStep===0?'cellulation-reference':'cellulation'):appearance.sulfurComposition?'nnpe-composition':appearance.sulfurBranchSeed?'branching-seed':appearance.sulfurHexStrands?'hex-strands':appearance.sulfurChannels?'channels':appearance.sulfurWireBundle?'wiring':appearance.sulfurTubes?'tubes':appearance.sulfurHandlebody?'handlebody':appearance.cellGraph?'lattice':'geometry'" @change="appearance.sulfurRetainedExpansion=$event.target.value==='retained-expansion';appearance.sulfurCellulation=['cellulation','cellulation-reference'].includes($event.target.value);if($event.target.value==='cellulation-reference')appearance.cellulationStep=0;else if($event.target.value==='cellulation' && appearance.cellulationStep===0)appearance.cellulationStep=1;appearance.sulfurComposition=$event.target.value==='nnpe-composition';appearance.sulfurBranchSeed=$event.target.value==='branching-seed';appearance.sulfurHexStrands=$event.target.value==='hex-strands';appearance.sulfurChannels=$event.target.value==='channels';appearance.sulfurWireBundle=$event.target.value==='wiring';appearance.sulfurTubes=$event.target.value==='tubes';appearance.sulfurHandlebody=$event.target.value==='handlebody';appearance.cellGraph=$event.target.value==='lattice'"><option value="retained-expansion">Retained expansion</option><option value="cellulation">Cellulation</option><option value="cellulation-reference">Full cellulation · reference</option><option value="nnpe-composition">NNPE composition</option><option value="geometry">Geometry</option><option value="tubes">Tubes</option><option value="lattice">Lattice</option><option value="wiring">Wiring</option><option value="channels">Channels / cutaway</option><option value="handlebody">Handlebody — empty tubes</option><option value="hex-strands">Hex strands · 3D</option><option value="branching-seed">White-rooted hex simplex</option></select></label>
   <template v-if="retainedExpansionView">
    <div class="row process-navigation"><button id="retained-expansion-prev" :disabled="phase!=='ready'||appearance.retainedExpansionStep<=1" @click="appearance.retainedExpansionStep--">← Previous</button><button id="retained-expansion-next" :disabled="phase!=='ready'||appearance.retainedExpansionStep>=20" @click="appearance.retainedExpansionStep++">Next →</button></div>
    <p id="retained-expansion-step" role="status">Step {{appearance.retainedExpansionStep}} · {{retainedExpansionLabels[appearance.retainedExpansionStep-1]}}</p>
    <label class="check"><input id="retained-expansion-animate" type="checkbox" v-model="appearance.retainedExpansionAnimate"> Animate expansion</label>
   </template>
   <template v-if="cellulationView && appearance.cellulationStep>0">
    <div class="row process-navigation"><button id="cellulation-prev" :disabled="phase!=='ready'||appearance.cellulationStep<=1" @click="appearance.cellulationStep--">← Previous</button><button id="cellulation-next" :disabled="phase!=='ready'||appearance.cellulationStep>=cellulationSteps.length||view.cellulationWitness?.phase==='blocked'" @click="appearance.cellulationStep++">Next →</button></div>
    <p id="cellulation-step-label" role="status">Step {{appearance.cellulationStep}} · {{cellulationSteps[appearance.cellulationStep-1].label}}</p>
    <label v-if="appearance.cellulationStep>=4" class="check"><input id="cellulation-animate" type="checkbox" v-model="appearance.cellulationAnimate"> Animate</label>
   </template>
   <label v-if="cellulationView" for="cellulation-cell-size">Cell scale <output>{{appearance.cellulationCellSize.toFixed(2)}}</output><input id="cellulation-cell-size" type="range" min="0.5" max="2" step="0.05" v-model.number="appearance.cellulationCellSize"></label>
   <section v-if="cellulationView && appearance.cellulationStep>=23 && view.cellulationWitness" id="shell-witness-controls">
    <h3>Witnessed construction</h3>
    <p id="shell-order-warning">Order dependence detected: permitted reorderings can change dot colors/normals, and changing face order can change arrows. This displays one selected sequence—not a confluence certificate.</p>
    <p id="shell-role-compatibility">Source-role compatibility: {{view.cellulationWitness.compatibilityStatus}} · {{view.cellulationWitness.sourceRoleViolations}} source-role violations. Geometry completion below does not certify compatible gluing.</p>
    <details v-if="view.cellulationWitness.dot422?.status==='unresolved'" id="shell-dot-422-unresolved" open>
     <summary>Dot 422: unresolved — no recoloring or role-changing transport admitted</summary>
     <ul><li v-for="claim in view.cellulationWitness.dot422.claims" :key="claim.event+claim.role">{{claim.cell}} · {{claim.role}} · {{claim.colour===0xffffff?'white':claim.colour===0xff3030?'red':'blue'}} ({{claim.kind}})</li></ul>
     <small>The displayed dot and click normal retain the legacy selected reading, not an agreed shared-vertex reading.</small>
    </details>
    <p id="shell-witness-status">{{view.cellulationWitness.phase}} · {{view.cellulationWitness.completedCells}} / {{view.cellulationWitness.targetCells}} cells</p>
    <small>Action {{Math.min(view.cellulationWitness.action+1,view.cellulationWitness.totalActions)}} / {{view.cellulationWitness.totalActions}} · {{view.cellulationWitness.cell}}</small>
    <div class="row"><button id="shell-witness-start" @click="appearance.cellulationAnimate=false;appearance.cellulationWitnessAction=0">Inspect from start</button><button id="shell-witness-complete" @click="appearance.cellulationAnimate=false;appearance.cellulationWitnessAction=-1">Show complete</button></div>
    <div class="row"><button id="shell-action-prev" :disabled="appearance.cellulationWitnessAction<=0" @click="appearance.cellulationWitnessAction--">Previous action</button><button id="shell-action-next" :disabled="appearance.cellulationWitnessAction<0||appearance.cellulationWitnessAction>=view.cellulationWitness.totalActions-1" @click="appearance.cellulationWitnessAction++">Next action</button></div>
    <small>{{view.cellulationWitness.requires.length}} recorded prerequisites for this action. Normal playback: {{Math.ceil(view.cellulationWitness.duration/1000)}} seconds.</small>
    <small>Opposite-direction additions: {{view.cellulationWitness.newOpposingArrows}}. Existing arrows are retained, not reversed or counted as the missing direction.</small>
    <p v-if="view.cellulationWitness.blockers.length">Blocked: {{view.cellulationWitness.blockers}}</p>
   </section>
   <section v-if="cellulationView && appearance.cellulationValidateLoop && view.loopValidation" id="loop-validation-report" aria-label="Loop validation report">
    <h3>Loop validation</h3>
    <p v-if="view.loopValidation.status==='pending'">{{view.loopValidation.message}}</p>
    <template v-else>
     <strong>{{view.loopValidation.issues.length}} findings · roles unassigned</strong>
     <ul><li v-for="check in view.loopValidation.checks" :key="check.name" :data-validation-status="check.status"><b>{{check.status==='pass'?'✓':check.status==='fail'?'!':'?'}} {{check.name}}</b><small>{{check.detail}}</small></li></ul>
     <ol v-if="view.loopValidation.issues.length"><li v-for="issue in view.loopValidation.issues" :key="issue.message">{{issue.message}}</li></ol>
     <small>{{view.loopValidation.scope}}</small>
    </template>
   </section>
   <div v-if="compositionView" id="nnpe-controls">
    <p>Target: 16 N · 16 P</p>
    <label class="check"><input id="nnpe-collapse" type="checkbox" v-model="appearance.sulfurCompositionCollapsed"> Collapse composites</label>
    <div class="row"><button id="nnpe-undo" :disabled="!appearance.sulfurCompositionJoins.length" @click="appearance.sulfurCompositionJoins=appearance.sulfurCompositionJoins.slice(0,-1)">Undo join</button><button id="nnpe-reset" :disabled="!appearance.sulfurCompositionJoins.length" @click="appearance.sulfurCompositionJoins=[]">Reset</button></div>
    <details id="nnpe-rules"><summary>Composition rules</summary><p>Each complex is shown as a diagonal half-cube with blue, red and white surfaces. Attachment labels are retained internally. N ↔ N; P ↔ E. Tree compositions only.</p><p>Trial inventory: each generator contributes 1 N and 1 P. Port labels add no particles; joining retains the inventory and history.</p></details>
   </div>
   <div v-if="seedActive && !be9Assembly && !be9Wiring" id="branching-seed-controls">
    <div id="seed-pair-controls" role="group" aria-label="Show twisted pairs">
     <span>Show twisted pairs</span>
     <label class="check"><input id="seed-pairs-by-layer" type="checkbox" v-model="appearance.seedPairsByLayer"> By layer</label>
     <label class="check"><input id="seed-pairs-combined" type="checkbox" v-model="appearance.seedPairsCombined"> Combined</label>
     <label class="check"><input id="seed-show-reference" type="checkbox" v-model="appearance.seedShowReference"> Show {{isBeryllium?berylliumLabel:'Su-32'}} reference</label>
     <label v-if="process.id==='beryllium-9' && appearance.seedShowReference" class="check"><input id="be9-central-sleeve" type="checkbox" v-model="appearance.be9CentralSleeve"> Central neutron sleeve (trial)</label>
    </div>
    <p v-if="appearance.seedPairsCombined">Combined uses the selected layers and continuation rule in the strand-comparison panel.</p>
    <p v-else-if="appearance.seedShowReference">The reference appears in the strand-comparison panel.</p>
    <div v-if="appearance.seedPairsByLayer" id="seed-layer-geometry-notes">
    <p>Eight layers: layers 1–4 are retained; layers 5–8 copy all four lower and point-reflect each within its own plane. Colours are retained; arrows follow every reflection.</p>
    <p>Original directions: vertical white · 120° blue · 240° red, clockwise from upward vertical. The mirrored pair keeps its inherited colours.</p>
    <p>Depth {{seedDepth}} = {{seedDepth}} white-plus-branch steps ({{2*seedDepth}} edge layers). Each layer retains its own vertices, edges and routes.</p>
    </div>
    <div v-if="appearance.seedPairsByLayer || appearance.seedPairsCombined" id="seed-layer-selector" role="group" :aria-label="appearance.seedPairsByLayer?'Visible layers':'Combined source layers'">
     <span>{{appearance.seedPairsByLayer?'Layers':'Combined source layers'}}</span>
     <button v-for="n in 8" :key="n" :id="'seed-layer-'+n" type="button" :aria-label="'Show layer '+n" :aria-pressed="appearance.seedVisibleLayers[n-1]" @click="appearance.seedVisibleLayers[n-1]=!appearance.seedVisibleLayers[n-1]">{{n}}</button>
    </div>
    <div v-if="appearance.seedPairsByLayer" id="seed-spatial-controls">
    <label>Layer gap {{appearance.seedLayerGap.toFixed(2)}} <input id="seed-layer-gap" type="range" min="0" max="6" step=".25" v-model.number="appearance.seedLayerGap"></label>
    <p>Layers lie at Z = 0 through −7gap. Layers 3–4 mirror 1–2 perpendicular to the central white arrow. Layers 5–8 are four gaps below 1–4, with XY reflected about the same center; their layer order is unchanged. Gold points mark the centers. No inter-layer connections are added.</p>
    <button id="seed-layers-view" type="button" @click="seedLayersView">Oblique view</button>
    <button id="seed-face-on" type="button" @click="planarSeedView">Face-on view</button>
    </div>
   </div>
   <template v-if="process.id==='sulfur-32' && !compositionView && !cellulationView">
   <div v-if="appearance.sulfurHexStrands" id="hex-strands-controls">
    <label>Hex process stage <select id="hex-strand-stage" v-model.number="appearance.hexStrandStage"><option v-for="(name,index) in hexStrandStageNames" :key="index" :value="index">{{index}} · {{name}}</option></select></label>
    <label>Strand <select id="hex-strand-select" v-model="appearance.hexStrandSelection"><option value="all">All 16 strands</option><option v-for="id in hexStrandIds" :key="id" :value="id">{{id}}</option></select></label>
    <label>Transformed copy <select id="hex-strand-copy" v-model.number="appearance.hexStrandCopy"><option :value="-1">All copies</option><option v-for="(trace,index) in hexStrandStages[appearance.hexStrandStage].strands[0].traces" :key="index" :value="index">{{index}} · {{trace.history.join(' → ') || 'original'}}</option></select></label>
    <label>Layer spacing {{appearance.hexStrandSpacing.toFixed(2)}} <input id="hex-strand-spacing" type="range" min="0" max="1" step=".02" v-model.number="appearance.hexStrandSpacing"></label>
    <label class="check"><input id="hex-strand-isolate" type="checkbox" v-model="appearance.hexStrandIsolate"> Isolate selected strand</label>
    <p>16 depth-4 seed strands · {{16*2**appearance.hexStrandStage}} retained transformed paths. Each strand has its own depth layer; rotate the scene to separate overlaps. Show shape adds the original planar graph.</p>
    <p>Depth is display-only, not an octahedral folding. Coincident edges within a strand are drawn once; their copy histories are retained. Added seam continuations remain unassigned.</p>
   </div>
   <div v-if="appearance.sulfurChannels" id="sulfur-channel-info">
    <label class="check"><input id="sulfur-channel-open" type="checkbox" v-model="appearance.sulfurChannelOpen"> Peel exterior</label>
    <button id="sulfur-channel-expose" type="button" @click="appearance.sulfurChannelCut=.35;appearance.sulfurChannelOpen=true;appearance.sulfurChannelNormal=[...(view.camera?.offset??[.35,-.85,.4])];appearance.sulfurWireOpacity=.2">Cut from current view</button>
    <label>Retained depth {{Math.round(appearance.sulfurChannelCut*100)}}% <input id="sulfur-channel-cut" type="range" min="0" max="1" step="0.05" v-model.lazy.number="appearance.sulfurChannelCut"></label>
   </div>
   <p v-if="appearance.sulfurHandlebody" id="sulfur-handlebody-info">19 N chambers, joined through 32 neutral connector spaces and 104 shared-face necks. Six open mouths; matching rim colours mark opposite-tip identities. No wires or direction assignments. Periodic seam links are not drawn as physical tubes.</p>
   <p v-if="appearance.sulfurWireBundle" id="sulfur-wire-info">16 retained (a,b,p,e) strands, present at both ends. Complete native-edge paths cover all 19 N carriers and all 16 retained N groups, with no copied branches. This is an incidence-coverage result, not equivalence to the 64-wire periodic model.</p>
   <label v-if="appearance.sulfurWireBundle || appearance.sulfurChannels">Wiring opacity {{Math.round(appearance.sulfurWireOpacity*100)}}% <input id="sulfur-wire-opacity" type="range" min="0" max="1" step="0.01" v-model.number="appearance.sulfurWireOpacity"></label>
   <label v-if="appearance.sulfurWireBundle && appearance.sulfurNTubeMarkers">Tube opacity {{Math.round(appearance.sulfurNTubeOpacity*100)}}% <input id="sulfur-tube-opacity" type="range" min="0" max="1" step="0.01" v-model.number="appearance.sulfurNTubeOpacity"></label>
   <label v-if="appearance.sulfurWireBundle"><input id="sulfur-n-tube-markers" type="checkbox" v-model="appearance.sulfurNTubeMarkers"> Show 16 N-tube groups</label>
   <p v-if="appearance.sulfurWireBundle && appearance.sulfurNTubeMarkers">Cyan tubes follow the honeycomb wiring, with automatic junction skins at actual splits and recombinations. Gold collars mark segment ends. Unrelated crossings remain separate; the 16 N-group identities are retained.</p>
   <div v-if="appearance.sulfurWireBundle && appearance.sulfurNTubeMarkers" id="sulfur-n-identification">
    <label>N identity <select id="sulfur-n-identity" v-model="appearance.sulfurNIdentity"><option value="all">All 16 identities</option><option v-for="g in nIdentityNetwork.identities" :key="g.id" :value="g.id">{{g.label}}{{g.members.length===2?' · opposite-tip pair':''}}</option></select></label>
    <p v-if="selectedNIdentity">{{selectedNIdentity.label}}: {{selectedNIdentity.segmentIds.length}} continuous segments; {{selectedNIdentity.components.length}} connected locations; {{selectedNIdentity.sharedSegmentIds.length}} segments shared with another N identity.</p>
    <details><summary>Native membership and segment mapping</summary>
     <div v-for="g in selectedNIdentity?[selectedNIdentity]:nIdentityNetwork.identities" :key="g.id"><strong>{{g.label}}</strong> · {{g.edgeIds.length}} edges · {{g.segmentIds.length}} segments · {{g.components.length}} connected locations<ul><li v-for="id in g.members" :key="id"><code>{{id}}</code></li></ul></div>
    </details>
   </div>
   <p v-if="!retainedExpansionView && process.step===0 && !appearance.sulfurBranchSeed && !appearance.sulfurHexStrands && !appearance.sulfurWireBundle && !appearance.sulfurChannels">Single octahedron starting geometry. Existing colours indicate geometric roles.</p>
   <button v-show="!retainedExpansionView && !appearance.sulfurBranchSeed && !appearance.sulfurHandlebody && !channelView" id="sulfur-32-fibrate" type="button" @click="process.step=process.step===0?1:0">{{process.step===0?'Fibrate globally':'Return to geometry'}}</button>
   <div v-if="!retainedExpansionView && process.step===1 && !appearance.sulfurHandlebody" v-show="!appearance.sulfurBranchSeed && !appearance.sulfurHexStrands && !appearance.sulfurWireBundle && !appearance.sulfurChannels" id="sulfur-32-fibration">
    <p>16 N channels · 64 wires · four slots per channel. All 51 cell records retained in 48 cell fibers.</p>
    <label>Read from <select id="sulfur-32-direction" v-model.number="process.branch"><option :value="1">P | E</option><option :value="3">E | P</option></select></label>
    <p>Candidate global periodic closure. Gold links sew 24 boundary interfaces; teal links identify the three opposite-tip pairs. These are retained comparisons, not straight passages through intervening cells.</p>
    <details id="sulfur-32-channel-ports"><summary>16 channel fibers · 2×2 ports</summary>
     <div v-for="channel in m.state.value.sulfur32Audit.channelPorts" :key="channel.id" class="sulfur-channel">
      <strong>{{channel.label}}</strong><small v-if="channel.members.length===2"> · paired tips</small>
      <table :aria-label="channel.label+' 2 by 2 ports'"><tbody><tr v-for="row in [0,1]" :key="row"><td v-for="port in channel.slots.filter(p=>p.slot[0]===row)" :key="port.wire" :title="port.wire">{{port.from}} → {{port.to}}</td></tr></tbody></table>
     </div>
    </details>
   </div>
   </template>
  </section>
  <section v-if="process.id==='unsplit-octahedron'" id="octahedron-audit" aria-label="Unsplit octahedron">
   <p>6 vertices · 12 edges · 8 triangular faces · 1 body.</p>
   <p>No internal diagonal, no tetrahedral subdivision, no P/N/E assignments.</p>
   <p>Next shows both sides of every face: teal points outward; amber points inward. Reduce face opacity to inspect the inner side.</p>
  </section>
  <section v-if="process.id==='cell-fibration'" id="cell-fibration-audit" aria-label="Cell-level fibration">
   <div class="process-metrics" aria-label="Construction progress"><span><strong>{{m.state.value.cellFibrationAudit.bodyCount}}</strong> whole cells</span><span>+{{process.step===0?4:m.state.value.cellFibrationAudit.growth.filter(g=>g.layer===m.state.value.cellFibrationAudit.layer).length}} this step</span></div>
   <fieldset id="cell-cut-controls" :disabled="phase!=='ready'"><legend>Layer cut</legend>
    <label class="check"><input id="cut-enabled" type="checkbox" v-model="cut.enabled"> Enable cut</label>
    <div id="cut-vertex-label" class="cut-vertex-label">From vertex</div>
    <div id="cut-vertex" class="cut-vertex-buttons" role="group" aria-labelledby="cut-vertex-label"><button v-for="v in cutVertices" :key="v.value" type="button" :data-cut-vertex="v.value" :aria-pressed="cut.vertex===v.value" :aria-label="v.value==='all'?'All vertices':v.label+' · V'+v.value" :title="v.value==='all'?'All vertices':'V'+v.value+(v.value===2?' ≡ V5':'')" :style="v.color?{backgroundColor:v.color,color:v.label.startsWith('N')?'#18212b':'#fff'}:null" @click="cut.vertex=v.value">{{v.label}}</button></div>
    <div id="cut-start-layer-label" class="cut-vertex-label">From layer</div>
    <div id="cut-start-layer" class="cut-layer-buttons" role="group" aria-labelledby="cut-start-layer-label"><button v-for="n in 7" :key="n" type="button" :data-cut-start-layer="n-1" :aria-pressed="cut.startLayer===n-1" :aria-label="'From layer '+n" @click="setCutDepth(n-1,'startLayer')">{{n}}</button></div>
    <div id="cut-layer-label" class="cut-vertex-label">Through layer</div>
    <div id="cut-layer" class="cut-layer-buttons" role="group" aria-labelledby="cut-layer-label"><button v-for="n in 7" :key="n" type="button" :data-cut-layer="n-1" :aria-pressed="cut.layer===n-1" :aria-label="'Through layer '+n" @click="setCutDepth(n-1,'layer')">{{n}}</button></div>
    <small id="cut-range-hint">Inclusive · 1 is the corner</small>
    <label class="check"><input id="cut-empty" type="checkbox" v-model="cut.showEmpty"> Unfilled positions (∅)</label>
    <label class="check"><input id="highlight-unassigned" type="checkbox" v-model="cut.highlightUnassigned"> Highlight unassigned</label>
    <p id="cut-status" role="status"><template v-if="cutAudit">{{cutAudit.counts.total}} coloured<span v-if="cutAudit.conflictBodyCount"> · {{cutAudit.conflictBodyCount}} colourless</span> · {{cutAudit.emptyCount}} unfilled · {{cutAudit.startLayer+1}}–{{cutAudit.layer+1}}</template><template v-else>Cut off · {{m.state.value.cellFibrationAudit.bodyCount}} coloured<span v-if="m.state.value.conflictBodies?.length"> · {{m.state.value.conflictBodies.length}} colourless</span> cells shown</template></p>
    <button id="clear-cut" @click="cut.enabled=false">Show all layers</button>
   </fieldset>
   <button id="restart-cell-fibration" class="process-restart" :disabled="phase!=='ready'||process.step===0" @click="process.step=0">Restart construction</button>
   <details id="cut-help"><summary>How cuts work</summary>
    <p>Layers outside the inclusive range are hidden. Equal bounds isolate one layer. Moving a bound past the other moves both to that layer.</p>
    <p>All vertices combines the range from each vertex; shared cells are counted once. Corner references and the outer outline stay visible. References outside the range are excluded from the visible count.</p>
    <p>Unfilled positions show same-orientation gaps as wireframes. Conflicting octahedra are neutral-grey cells, visible without this option. Admitted complementary cells are included. The adjoining octahedron belongs to layer 1; the tetrahedron beyond it belongs to layer 2.</p>
   </details>
   <details v-if="m.state.value.cellFibrationAudit.unresolvedOctahedra.length" id="hex-conflicts"><summary>{{m.state.value.cellFibrationAudit.unresolvedOctahedra.length}} conflicting whole-cell demands</summary><p>Every matching surface hexagon is processed. These neutral-grey octahedra receive different colours from their two exposed faces. Hover a grey cell to see both assignments. They are not included in P/N/E counts.</p><p v-for="g in m.state.value.cellFibrationAudit.unresolvedOctahedra" :key="g.cell"><strong>{{esd7CellId(g.cell)}}</strong><br><span v-for="w in g.hexWitnesses" :key="w.face.join('-')">Face {{w.face.join('–')}}: opposite {{esd7CellId(w.oppositeCell)}} → {{w.role}}<br></span></p></details>
   <details id="cell-construction-rules"><summary>Construction rules</summary><p>k=7 · V₂≡V₅. Whole-cell colours.</p><ol start="0"><li v-for="(rule,i) in cellFibrationStages" :key="i" :aria-current="process.step===i?'step':undefined">{{rule}}</li></ol></details>
   <details><summary>Growth attachments</summary><p v-for="g in m.state.value.cellFibrationAudit.growth" :key="g.child">{{g.complementaryLayer?'Complementary layer '+g.complementaryLayer:'Layer '+g.layer}} · <template v-if="g.kind==='filler-coherence'">{{g.layers.join('')}} · {{g.pattern}} · {{g.neighbors.map(n=>esd7CellId(n.cell)+': '+n.role).join(' + ')}}</template><template v-else-if="g.kind==='nearest-vertex-color'">V{{g.vertex}} ({{g.vertexRole}}) → {{g.role}}</template><template v-else-if="g.kind==='vertex-2-path'">V{{g.vertex}}: {{g.source}} → {{g.target}}</template><template v-else-if="g.kind==='interior-pair'">{{g.layers.join('')}} ← {{g.parents.map(p=>p.layers.join('')).join(' / ')}}</template><template v-else-if="g.kind==='opposite-quartet'">Face {{g.face.join('–')}} · copy {{esd7CellId(g.parent)}}</template><template v-else-if="g.kind==='layer-3-fill'">V{{g.sources.join(' / V')}} · layer 3 → N</template><template v-else-if="g.kind==='central-quartet'">V{{g.source}} · {{g.pattern}} · {{g.neighbors.map(n=>esd7CellId(n.cell)+': '+n.role).join(' + ')}}</template><template v-else-if="g.kind==='face-middle'">Faces {{formatFaces(g.faces)}} · cell {{esd7CellId(g.parent)}}: {{g.sourceRole}} → {{g.role}}</template><template v-else-if="g.kind==='inner-hex-reflection'"><span v-for="w in g.hexWitnesses" :key="w.face.join('-')">Inside V{{w.source}}, layer 2: opposite {{esd7CellId(w.oppositeCell)}} ({{w.role}}) → {{w.assignedRole}}; </span></template><template v-else-if="g.kind==='complementary'">V{{g.source}} · face-attached to {{esd7CellId(g.parent)}}</template><template v-else-if="g.kind==='shared-interior'">Shared interior · {{g.proposals.map(p=>`V${p.source}→V${p.target}: ${p.role}`).join('; ')}} · P > N > E</template><template v-else-if="g.kind==='corner-interior'">V{{g.source}} · interior (1,1,1)</template><template v-else-if="g.kind==='face-center'">Face {{g.face.join('–')}}; opposite V{{g.opposite}}</template><template v-else-if="g.kind==='face'">V{{g.source}}, face {{g.face.join('–')}}; opposite V{{g.opposite}}</template><template v-else-if="g.kind==='face-completion'">V{{g.source}}, face {{g.face.join('–')}}; nearest other V{{g.target}}</template><template v-else-if="g.kind==='midpoint'">Edge V{{g.source}}–V{{g.target}} · {{g.word}} (new cell in the middle)</template><template v-else>V{{g.source}} → V{{g.target}}</template>: {{g.role}} · {{esd7CellId(g.child)}}</p></details>
  </section>
  <details v-if="process.id!=='double-esd7' && !compactSulfurView" id="process-notes" :key="process.id"><summary>About this process &amp; current step</summary><p>{{m.selectedProcess.value.description}}</p><p>{{summary}}</p></details>
  <section v-if="process.id==='fibration-12x12'" id="fibration12-audit" aria-label="12x12 fibration construction">
   <button id="restart-fibration" :disabled="phase!=='ready'" @click="process.step=0">Restart at −P</button>
   <label for="polarity-sheet">Whole-face polarity reading</label>
   <select id="polarity-sheet" v-model="appearance.polaritySheet"><option value="positive">Original sheet</option><option value="negative">Opposite sheet</option></select>
   <p><strong>5134 is folded onto 2134; V₅ ≡ V₂ geometrically.</strong> −P and +P remain distinct flow occurrences at that shared location. Only −P starts growth; the other corner roles are constraints.</p>
   <p><strong>{{m.state.value.fibrationAudit.flow}}</strong> · {{m.state.value.fibrationAudit.bodyCount}} / {{m.state.value.fibrationAudit.totalBodies}} whole geometric cells; {{m.state.value.fibrationAudit.admittedOccurrences}} / {{m.state.value.fibrationAudit.totalOccurrences}} retained flow occurrences.</p>
   <p>{{m.state.value.fibrationAudit.growthRounds}} face-adjacent outward rounds; {{m.state.value.fibrationAudit.returnRounds}} return rounds from +P. Blue/pink arrows retain opposite flows. Both polarity sheets stay present; neither overwrites the other. The traversal count is not derived from the channel bank.</p>
   <p v-if="m.state.value.fibrationAudit.returnedToMinusP"><strong>Return to −P positively confirmed.</strong></p>
   <p v-if="m.state.value.fibrationAudit.returnedToMinusP && m.state.value.fibrationAudit.filler.step===0">Next applies the candidate 4×4 filler operator; the following step confirms reconstruction.</p>
   <section v-if="m.state.value.fibrationAudit.filler.step>0" id="filler-audit" aria-label="4 by 4 filler comparison">
    <h3>4×4 filler · {{m.state.value.fibrationAudit.filler.state}}</h3>
    <p>Candidate boundary operator: 1 positive + 1 negative + 14 zero-charge slot modes. This is a mode decomposition, not fourteen new neutron tiles.</p>
    <label for="filler-display">Matrix reading</label><select id="filler-display" v-model="fillerDisplay"><option value="input">Native input</option><option value="charge">Boundary operator Q(input)</option><option value="collective">Collective P/E projection</option><option value="residual">Fourteen-direction residual</option></select>
    <label for="filler-coordinate">Retained coefficient</label><select id="filler-coordinate" v-model.number="fillerCoordinate"><option v-for="i in 5" :key="i" :value="i-1">Coefficient {{i-1}}</option></select>
    <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:4px" id="filler-matrix">
     <strong v-for="channel in ['aa','ab','ba','bb']" :key="channel">{{channel}}</strong>
     <div v-for="slot in m.state.value.fibrationAudit.filler.slots" :key="slot.index" data-filler-slot :title="`Depth ${slot.depth}, ${slot.channel}`" style="border:1px solid #52697d;padding:4px;overflow-wrap:anywhere;font-size:11px">
      <small>d{{slot.depth}}</small><br>{{formatFillerCoefficient(m.state.value.fibrationAudit.filler[fillerDisplay][slot.index][fillerCoordinate])}}
     </div>
    </div>
    <details><summary>Fourteen residual coordinates</summary><p v-for="mode in m.state.value.fibrationAudit.filler.modes" :key="mode.index" data-filler-mode>{{mode.index+1}}. {{mode.kind}} d{{mode.depth}}: {{formatFillerCoefficient(mode.coefficients[fillerCoordinate])}}</p></details>
    <p v-if="m.state.value.fibrationAudit.filler.state==='confirmed'" id="filler-confirmation">Confirmed on all five complex coefficients: input = collective + residual; Q(residual) = 0. Reconstruction error: {{m.state.value.fibrationAudit.filler.confirmation.maxReconstructionError}}.</p>
    <p>These sixteen native packet occurrences reuse five independent input coefficients. Six charged history contrasts vanish in this replay. The free 14-dimensional kernel has not been realized as fourteen independent neutron states; the two 56-site sheets remain linked.</p>
   </section>
   <section v-if="m.state.value.fibrationAudit.collective" id="collective-cell-audit" aria-label="Materialized collective comparison cell">
    <h3>Collective P*/E* cell</h3>
    <p>{{m.state.value.fibrationAudit.collective.witness.memberCount}} member cells now have one external comparison port. The graph marks it P* on the opposite sheet and E* on the original sheet.</p>
    <p>All members and {{m.state.value.fibrationAudit.collective.witness.contrastCount}} internal contrasts remain retained. No tetrahedron is inserted or overlapped. The 36→1 grouping is a separate collective-carrier rule, not a consequence of Q or a new independently established particle.</p>
    <p>Charged external readings: P {{m.state.value.fibrationAudit.collective.counts.chargedReadings.proton}}, E {{m.state.value.fibrationAudit.collective.counts.chargedReadings.electron}}. These are dual readings of shared carriers; N is not doubled.</p>
    <details><summary>Retained member cells</summary><p>{{m.state.value.fibrationAudit.collective.support.join(', ')}}</p></details>
   </section>
   <section v-if="m.state.value.fibrationAudit.neutral" id="neutral-extension-audit" aria-label="Declared independent neutral channels">
    <h3>Neutral extension · 126 channels</h3>
    <p>56 original-site + 56 opposite-site + 14 residual channels. Each has five independently editable complex coefficients. These are added fields beyond the native linked replay; they do not derive 126 physical neutrons.</p>
    <label for="neutral-mode">Inspect neutral channel</label><select id="neutral-mode" v-model.number="selectedNeutralMode"><option v-for="(mode,i) in m.state.value.fibrationAudit.neutral.modes" :key="mode.id" :value="i">{{i+1}} · {{mode.id}}</option></select>
    <label for="neutral-coordinate">Coefficient</label><select id="neutral-coordinate" v-model.number="neutralCoordinate"><option v-for="i in 5" :key="i" :value="i-1">{{i-1}}</option></select>
    <label for="neutral-real">Real</label><input id="neutral-real" type="number" min="-1000000" max="1000000" step="any" :value="neutralValues[selectedNeutralMode][neutralCoordinate][0]" @input="editNeutral(0,$event)" @change="editNeutral(0,$event)">
    <label for="neutral-imag">Imaginary</label><input id="neutral-imag" type="number" min="-1000000" max="1000000" step="any" :value="neutralValues[selectedNeutralMode][neutralCoordinate][1]" @input="editNeutral(1,$event)" @change="editNeutral(1,$event)">
    <p id="neutral-active">Nonzero channels: {{m.state.value.fibrationAudit.neutral.activeChannels}} / 126 (not particle occupancy).</p>
    <p>Boundary change, selected coefficient: P {{formatFillerCoefficient(m.state.value.fibrationAudit.neutral.boundaryDelta.P[neutralCoordinate])}}, E {{formatFillerCoefficient(m.state.value.fibrationAudit.neutral.boundaryDelta.E[neutralCoordinate])}}.</p>
    <button id="clear-neutral" @click="neutralValues=zeroNeutralValues()">Clear extension amplitudes</button>
   </section>
   <p><strong>Both polarity sheets retained:</strong> P ↔ E, N unchanged. Faces are whole—no P/E half-face split. Choose which sheet to display; changing this does not modify either state. Corner labels refer to the original sheet.</p>
   <p v-if="m.state.value.fibrationAudit.complete">Surface E readings: {{m.state.value.fibrationAudit.polarity.sheets.positive.exposedElectrons}} original-sheet bodies and {{m.state.value.fibrationAudit.polarity.sheets.negative.exposedElectrons}} opposite-sheet bodies. These are sheet-labelled readings, not additional particles.</p>
   <details><summary>Retained 2×2×2 interface bank (test coefficients)</summary>
    <div v-for="sheet in ['positive','negative']" :key="sheet"><strong>{{sheet}} sheet</strong>
     <div style="display:grid;grid-template-columns:1fr 1fr;gap:5px"><div v-for="(pair,slot) in m.state.value.fibrationAudit.polarity.bank" :key="slot" style="border:1px solid #52697d;padding:5px">
      <strong>{{slot}}</strong> · {{pair[sheet].role}} · flow {{pair[sheet].interfaceFlow}}
      <p><small>{{pair[sheet].coefficients.map(z=>`${z[0]}${z[1]<0?'':'+'}${z[1]}i`).join(', ')}}</small></p>
     </div></div>
    </div>
    <p>The full-state polarity map is checked on the local native interface. Its application to all tiling roles remains a candidate, not a certified particle dynamics.</p>
   </details>
   <p>{{m.state.value.fibrationAudit.coarse.tetrahedra}} tetrahedra + {{m.state.value.fibrationAudit.coarse.octahedra}} whole octahedra. All {{m.state.value.fibrationAudit.coarse.matchedFoldPairs}} cell pairs match under the fold. Internal octahedral subdivision faces are removed, not overlaid.</p>
   <p v-if="m.state.value.fibrationAudit.geometryComplete"><strong>Complete folded geometry:</strong> {{m.state.value.fibrationAudit.coarse.outerTriangles}} whole outer triangles. Flow histories may still be advancing on the retained occurrences.</p>
   <p>Confirmed return rounds: {{m.state.value.fibrationAudit.confirmations.length}} / {{m.state.value.fibrationAudit.returnRounds}}.</p>
   <details><summary>Geometric certificate and interpretation</summary><p>Each folded cell retains its two original flow occurrences and both polarity readings. Return checks use the actual unfolded face incidences; coincident coordinates do not identify histories. This is a geometric quotient, not a derived particle law or a derivation of the channel count.</p></details>
  </section>
  <section v-if="process.id==='from-center-cell'" id="center-interface-audit" aria-label="Recursive interface proposal">
   <p>{{m.state.value.presentationAudit.typedCarriers}} retained carriers. Cell edge lengths and volumes stay fixed.</p>
   <p>Blue P, pink E, pale N are retained carrier roles, not derived particle counts.</p>
   <p v-if="m.state.value.presentationAudit.gapOpen">Two existing esd7 cell positions are open between the center and each boundary.</p>
   <p>All cells use actual esd7 vertices. Boundary cells are congruent octahedral wedges, reoriented without resizing. Step 5 fills the eight arrow positions; consecutive cells share triangular faces. The remaining octahedral wedges are not yet filled.</p>
   <details><summary>Native cell routes</summary><p v-for="route in m.state.value.presentationAudit.routes" :key="route.branch">Branch {{route.branch+1}}: {{route.nativeCellIds.join(' → ')}}</p></details>
   <p v-if="m.state.value.presentationAudit.arrowCells">P [N N] E · P [P P] P · P [N E] N · P [N P] N</p>
   <details><summary>Numbered steps</summary><p v-for="h in m.state.value.history" :key="h.round">Step {{h.round}} — {{h.rule}}</p></details>
   <details><summary>Retained interfaces</summary><p v-for="layer in m.state.value.presentationAudit.layerRecords" :key="layer.id">{{layer.id}}<span v-if="layer.parents"> — inserted between {{layer.parents.join(' and ')}}</span></p></details>
  </section>
  <section v-if="process.id==='retained-construction'" id="retained-pb-audit" aria-label="Seed-first construction">
   <p>Constructed: {{m.state.value.retainedAudit.bodyCount}} whole cells — {{m.state.value.retainedAudit.tetrahedra}} tetrahedra, {{m.state.value.retainedAudit.octahedra}} octahedra. {{m.state.value.retainedAudit.contacts}} retained shared faces.</p>
   <p>{{m.state.value.retainedAudit.primitiveComponents}} primitive tetrahedra. These are geometry counts, not particle counts.</p>
   <details><summary>Construction history and four branches</summary>
    <p v-for="h in m.state.value.history" :key="h.round">Round {{h.round}}: +{{h.added.length}} — {{h.rule}}</p>
    <p v-for="b in m.state.value.retainedAudit.branches" :key="b.branch">Branch {{b.branch}}: {{b.bodies}} cells retain this ancestry. Shared cells can retain several branches.</p>
   </details>
   <p v-if="m.state.value.retainedAudit.envelopeComplete">Carrier complete. Pb particle roles and native marked-contact bindings are not yet constructed.</p>
   <a :href="publishedBelt?'https://github.com/andrey-kokoev/marici/blob/main/research/realization-tower/process4.md':'./process4.md'" target="_blank" rel="noopener">Construction rule ↗</a>
  </section>
  <p v-if="process.id==='diamond-construction'"><a :href="publishedBelt?'https://github.com/andrey-kokoev/marici/blob/main/research/realization-tower/four-channel-rod.html':'/research/realization-tower/four-channel-rod.html'" target="_blank" rel="noopener">Open four-channel P–E rod study ↗</a> (schematic; no filling changes)</p>
  <details id="radial-audit" v-if="process.id==='diamond-construction'">
   <summary>Radial constraints (inside → outside)</summary>
   <p>Center cell: {{m.state.value.radial.centralCell ?? 'not unique'}}. Grouped depth counts whole tetrahedra/octahedra; it need not identify a unique center.</p>
   <p v-if="m.state.value.radial.status==='branch-orientation-ambiguous'">{{m.state.value.radial.orientationCount}} equally short branch orientations. The central tetrahedron points differently at this k; no orientation is selected automatically.</p>
   <p v-if="!m.state.value.radial.available">Center candidates: {{m.state.value.radial.centerCandidates.join(', ')}}. A distinct central P cannot yet be assigned.</p>
   <p v-if="m.process.step<7 && m.state.value.radial.centralChannel">V₁ branch neighbor {{m.state.value.radial.centralChannel.cell}} remains unresolved. E belongs on the surface only. Dashed routes are geometric guides, not established particle chains.</p>
   <div v-if="m.process.step>=6 && m.state.value.collectiveCore">
    <p>Collective P core: {{m.state.value.collectiveCore.core.join(', ')}}. {{m.state.value.collectiveCore.disconnectedProtons.length}} disconnected filler Ps. {{m.state.value.collectiveCore.blocked.length}} blocked E connections.</p>
    <ul><li v-for="route in m.state.value.collectiveCore.routes" :key="route.electron">E{{route.electron}}: {{route.established?'assigned trial':'planned N corridor'}} — {{route.path.join(' → ')}}<span v-if="route.viaSurfaceProton"> (through its surface P partner)</span>.</li></ul>
   </div>
   <ul><li v-for="layer in m.state.value.radial.layers" :key="layer.insideLayer">Layer {{layer.insideLayer}}: {{layer.allowedRoles.map(r=>r[0].toUpperCase()).join('/')}}; {{layer.assigned.length}} assigned, {{layer.unassigned.length}} unresolved.<span v-if="layer.exceptions.length"> Explicit core constraints: {{layer.exceptions.map(e=>`${e.cell}=${e.allowedRoles.join('/')}`).join(', ')}}.</span></li></ul>
   <p v-if="m.state.value.radial.surfaceElectrons.some(e=>!e.hasInteriorFaceNeighbor)">Surface E without an interior face-neighbor: {{m.state.value.radial.surfaceElectrons.filter(e=>!e.hasInteriorFaceNeighbor).map(e=>e.cell).join(', ')}}. Hidden pairing here needs a different rule or a corner exception.</p>
  </details>
  <label v-show="!seedActive && !['sulfur-32-reflection','ruthenium-98','sulfur-32','single-octahedral','native-octahedral-bridge','signed-octahedral-belt','unsplit-octahedron','cell-fibration','double-esd7'].includes(process.id)" for="step">{{process.id==='from-center-cell'?'Reference envelope k':'Input k'}} = <output id="kval">{{k}}</output></label><input v-show="!seedActive && !['sulfur-32-reflection','ruthenium-98','sulfur-32','single-octahedral','native-octahedral-bridge','signed-octahedral-belt','unsplit-octahedron','cell-fibration','double-esd7'].includes(process.id)" id="step" v-model.number="process.k" :disabled="phase!=='ready'||['cell-fibration','pair-context-7x4','retained-construction','from-center-cell','fibration-12x12','unsplit-octahedron'].includes(process.id)" type="range" min="1" max="7" step="1">
  <p v-if="status" id="status">{{status}}</p><p v-if="error" id="error" role="alert">{{error}}</p>
 </aside>
 <NNPEComposition v-if="compositionView" :projected-ports="view.nnpePorts??[]" v-model:joins="appearance.sulfurCompositionJoins" :collapsed="appearance.sulfurCompositionCollapsed" :process-open="panels.process" :scene-open="panels.scene" />
 <SulfurReferencePanel v-if="seedActive && !be9Assembly && !be9Wiring && (appearance.seedShowReference || appearance.seedPairsCombined)"
  :process-id="process.id" :central-sleeve="appearance.be9CentralSleeve" :reference-on="appearance.seedShowReference" :combined-on="appearance.seedPairsCombined" :process-open="panels.process" :scene-open="panels.scene"
  :visible-layers="appearance.seedVisibleLayers" :gap="appearance.seedLayerGap" v-model:rule="appearance.seedComparisonRule"
  @close="appearance.seedShowReference=false; appearance.seedPairsCombined=false" />
 <aside id="scene-panel" aria-label="Scene controls" v-show="panels.scene">
  <button id="close-scene" class="panel-close" aria-label="Close scene panel" aria-controls="scene-panel" @click="togglePanel('scene')">×</button><h2>Scene</h2>
  <fieldset :disabled="phase!=='ready'" class="controls">
   <details :open="sections.appearance" @toggle="sections.appearance=$event.target.open"><summary>Appearance</summary>
    <label v-if="!cellulationView" class="check"><input id="grid" v-model="appearance.grid" :disabled="!(cellulationView && appearance.cellulationStep!==0) && ['beryllium-8','beryllium-9','sulfur-32-reflection','ruthenium-98','sulfur-32','single-octahedral','native-octahedral-bridge','signed-octahedral-belt','cell-fibration','fibration-12x12','pair-context-7x4','from-center-cell','unsplit-octahedron'].includes(process.id)" type="checkbox"> {{cellulationView?'Lattice grid':'Lattice above k-floor'}}</label>
    <label for="opacity">Grid opacity</label><input id="opacity" v-model.number="appearance.opacity" type="range" min="0.01" max="0.5" step="0.01">
    <label v-if="cellulationView && appearance.cellulationStep>=20" class="check"><input id="cellulation-validate-loop" v-model="appearance.cellulationValidateLoop" type="checkbox"> Validate loop</label>
    <label v-if="cellulationView" class="check"><input id="cellulation-grid-vertex-hover" v-model="appearance.cellulationGridVertexHover" type="checkbox"> Show grid vertex candidates on hover</label>
    <label v-if="cellulationView && appearance.cellulationStep!==0" class="check"><input id="cellulation-highlight-grid-edges" v-model="appearance.cellulationHighlightGridEdges" type="checkbox"> Highlight grid edges on dot hover</label>
    <small v-if="cellulationView && appearance.cellulationHighlightGridEdges">Edges: XYZ Euler degrees, shortest rotation from +X. Dot: FCC coordinates.</small>
    <label v-if="!cellulationView" class="check"><input id="cell-hover-enabled" v-model="appearance.showCellInfo" type="checkbox"> Show cell / tube info on hover</label>
    <small v-if="!cellulationView && appearance.showCellInfo">Hover a cell or visible tube (an edge in edges-only mode). Click to pin and copy; Esc closes.</small>
    <label class="check"><input id="edges-only" v-model="appearance.edgesOnly" type="checkbox"> {{cellulationView?'Edges only':'Edges only · thick outlines'}}</label>
    <label for="face-opacity">Cell face opacity <output>{{Math.round(m.renderState.value.faceOpacity*100)}}%</output></label>
    <input id="face-opacity" v-model.number="appearance.faceOpacity" :disabled="appearance.edgesOnly" type="range" min="0" max="1" step="0.01" :title="cellulationView?'Opacity of cell faces; edges and arrows are unchanged.':'Opacity of all cell faces. At 100%, the nearest face fully hides faces behind it. Outlines and labels are unchanged.'">
    <label v-if="!cellulationView" class="check"><input id="prior" v-model="appearance.prior" :disabled="['beryllium-8','beryllium-9','ruthenium-98','sulfur-32','single-octahedral','native-octahedral-bridge','signed-octahedral-belt','pair-context-7x4','from-center-cell','unsplit-octahedron'].includes(process.id)" type="checkbox"> Earlier plane outlines</label>
    <label class="check"><input id="bodies" v-model="appearance.bodies" type="checkbox"> {{cellulationView?(appearance.cellulationStep===0?'Show faces':'Show construction'):['beryllium-8','beryllium-9','sulfur-32-reflection','ruthenium-98','sulfur-32','single-octahedral'].includes(process.id)?'Show shape':['signed-octahedral-belt','native-octahedral-bridge'].includes(process.id)?'Show assembly':process.id==='pair-context-7x4'?'Show interface faces':['cell-fibration','fibration-12x12'].includes(process.id)?'Show tiling bodies':process.id==='unsplit-octahedron'?'Show octahedron':process.id==='from-center-cell'?'Show layer bodies':'Cells intersected along ray'}}</label>
   </details>
   <details :open="sections.view" @toggle="sections.view=$event.target.open"><summary>{{cellulationView?'Camera':'View direction & rotation'}}</summary>
    <template v-if="!cellulationView"><label for="azimuth">Azimuth {{view.azimuth.toFixed(1)}}°</label><input id="azimuth" :value="view.azimuth" @input="angles('azimuth',$event)" type="range" min="-180" max="180" step="1">
    <label for="elevation">Elevation {{view.elevation.toFixed(1)}}°</label><input id="elevation" :value="view.elevation" @input="angles('elevation',$event)" type="range" min="-180" max="180" step="1"></template>
    <div class="row camera-presets"><button v-for="a in ['x','y','z']" :key="a" :data-view-axis="a" @click="viewer?.axis(a)">+{{a.toUpperCase()}}</button><button v-if="!cellulationView" id="ray-view" @click="viewer?.ray()">Along edge</button><span class="view-framing"><button id="reset-view" @click="reset">Reset view</button><button v-if="cellulationView && appearance.cellulationStep!==0" id="recenter-view" aria-label="Recenter" title="Recenter: fit the construction without rotating" @click="recenter"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M12 7v10M7 12h10"/></svg></button></span></div>
    <div class="row"><button aria-label="Rotate left" @click="viewer?.orbit('y',-.15)">←</button><button aria-label="Rotate right" @click="viewer?.orbit('y',.15)">→</button><button aria-label="Rotate up" @click="viewer?.orbit('x',-.15)">↑</button><button aria-label="Rotate down" @click="viewer?.orbit('x',.15)">↓</button><button aria-label="Roll left" @click="viewer?.orbit('z',-.15)">↶</button><button aria-label="Roll right" @click="viewer?.orbit('z',.15)">↷</button></div>
    <div class="row"><button id="zoom-in" @click="viewer?.zoom(1.2)">Zoom +</button><button id="zoom-out" @click="viewer?.zoom(1/1.2)">Zoom −</button></div>
   </details>
   <details :open="sections.motion" @toggle="sections.motion=$event.target.open"><summary>Motion</summary><label class="check"><input id="auto-rotate" v-model="motion.spin" type="checkbox"> Auto-rotate view</label><label v-if="!cellulationView" class="check"><input id="axial-rotation" v-model="motion.axialRotation" type="checkbox" :disabled="process.id!=='double-esd7'"> Axial rotation (−P → +P)</label><template v-if="!cellulationView || motion.spin"><label for="rotation-speed">Rotation speed</label><input id="rotation-speed" v-model.number="motion.speed" type="range" min="-4" max="4" step="0.25"></template></details>
  </fieldset>

 </aside>
 <button id="open-process" class="panel-open" v-show="!panels.process" aria-controls="process-panel" :aria-expanded="panels.process" @click="togglePanel('process')">Process</button>
 <button id="open-scene" class="panel-open" v-show="!panels.scene" aria-controls="scene-panel" :aria-expanded="panels.scene" @click="togglePanel('scene')">Scene</button>
 <Teleport to="#scene">
  <div v-if="retainedExpansionView && appearance.retainedExpansionStep>=4" id="retained-expansion-label" role="status" style="position:absolute;top:14px;left:14px;z-index:5;color:#e5eaf3;background:rgba(10,15,28,.9);border:1px solid #ffffff20;padding:10px 14px;border-radius:9px;font-size:12px;line-height:1.65;min-width:145px;pointer-events:none;box-shadow:0 4px 16px #0003;font-variant-numeric:tabular-nums">
   <template v-for="atom in [retainedExpansionAtoms[appearance.retainedExpansionStep]]" :key="atom.name">
    <strong style="display:block;color:white;font-size:14px;letter-spacing:.02em;margin-bottom:6px;padding-bottom:5px;border-bottom:1px solid #ffffff18">{{atom.name}}</strong>
    <div v-for="(count,name) in {neutrons:atom.neutrons,protons:atom.protons,electrons:atom.shells.reduce((sum,n)=>sum+n,0)}" :key="name" style="display:flex;justify-content:space-between;gap:24px"><span style="color:#aab7cb">{{name}}:</span><b>{{count}}</b></div>
    <div v-for="(count,i) in atom.shells" :key="i" style="display:flex;justify-content:space-between;gap:24px;padding-left:8px;color:#aab7cb"><span>- shell {{i+1}}:</span><span style="color:#e5eaf3">{{count}}/{{2*(i+1)**2}}</span></div>
    <div style="margin-top:6px;padding-top:5px;border-top:1px solid #ffffff18" aria-label="Reference data: representative natural abundance varies by sample; stable means no observed radioactive decay.">
     <div style="display:flex;justify-content:space-between;gap:24px"><span style="color:#aab7cb">natural abundance:</span><b data-isotope-abundance>{{atom.abundancePercent}}%</b></div>
     <div style="display:flex;justify-content:space-between;gap:24px"><span style="color:#aab7cb">stability:</span><b data-isotope-stability>{{atom.stability}}</b></div>
    </div>
   </template>
  </div>
  <div v-if="!cellulationView&&hoveredCell&&appearance.showCellInfo" id="cell-hover-info" class="cell-hover-info" :class="{'is-pinned':hoveredCell.pinned}" :style="{left:hoveredCell.x+'px',top:hoveredCell.y+'px'}" :role="hoveredCell.pinned?'region':'tooltip'" :aria-label="hoveredCell.kind==='tube'?'Tube information':'Cell information'">
   <template v-if="hoveredCell.selection">
    <header class="cell-hover-heading">Selected items · {{hoveredCell.selection.length}}</header>
    <div v-for="cell in hoveredCell.selection" :key="cell.id" class="selected-cell-summary"><strong>#{{cell.id}} · {{cell.shape}}</strong><span v-if="cell.role"> · {{cell.role}}</span><div v-if="cell.layers">Simplex code: {{cell.layers.join(' · ')}}</div></div>
    <section v-if="hoveredCell.sharedConstraints.length" id="cell-selection-constraints"><strong>Shared coherence constraints</strong>
     <div v-for="pair in hoveredCell.sharedConstraints" :key="pair.from+'-'+pair.to">#{{pair.from}} ↔ #{{pair.to}}: {{pair.sharedFacets}} shared facets; common layer coordinates {{pair.commonLayers.length?pair.commonLayers.join(', '):'none'}}; {{pair.roleCompatible?'same':'different'}} colours.</div>
     <details v-for="pair in hoveredCell.sharedConstraints" :key="'paths-'+pair.from+'-'+pair.to"><summary>Paths #{{pair.from}} ↔ #{{pair.to}}</summary>
      <div v-if="pair.forward"><strong>#{{pair.from}} → #{{pair.to}}</strong>: {{pair.forward.code.join(' → ')}}<small>{{pair.forward.steps.map(s=>s.to).join(' → ')}}</small></div>
      <div v-if="pair.reverse"><strong>#{{pair.to}} → #{{pair.from}}</strong>: {{pair.reverse.code.join(' → ')}}<small>{{pair.reverse.steps.map(s=>s.to).join(' → ')}}</small></div>
     </details>
    </section>
    <small>Ctrl-click cells to add; click outside without Ctrl to clear.</small>
   </template>
   <template v-else>
   <header class="cell-hover-heading"><span>ID</span> <code id="cell-hover-id">{{hoveredCell.id}}</code></header>
   <div>{{hoveredCell.shape}}<span v-if="hoveredCell.role"> · {{hoveredCell.role}}</span><span v-else-if="hoveredCell.unfilled"> · unfilled</span><span v-else-if="hoveredCell.conflicts?.length"> · colourless</span></div>
   <section v-if="hoveredCell.tube" id="tube-hover-details">
    <div><strong>N identities:</strong> {{hoveredCell.tube.groups.map(g=>g.label).join(' / ')}}<span v-if="hoveredCell.tube.groups.length>1"> · shared segment</span></div>
    <div>{{hoveredCell.tube.edgeIds.length}} native edges · {{hoveredCell.tube.strands.length}} strands · radius {{hoveredCell.tube.radius.toFixed(3)}}</div>
    <details><summary>Strand identities</summary><div v-for="s in hoveredCell.tube.strands" :key="s.id"><code>{{s.id}}</code> · (a,b,p,e): {{[s.polarities.a,s.polarities.b,s.polarities.p,s.polarities.e].join(' ')}}</div></details>
    <details><summary>Native N cells</summary><div v-for="id in hoveredCell.tube.sourceCells" :key="id"><code>{{id}}</code></div></details>
   </section>
   <section v-if="hoveredCell.conflicts?.length" id="cell-hover-conflicts"><strong>Conflicting assignments</strong><div v-for="w in hoveredCell.conflicts" :key="w.face.join('-')">Face V{{w.face.join('–V')}}: {{w.oppositeCell}} → {{w.role}}</div></section>
   <div v-if="hoveredCell.reflection" id="cell-hover-reflection">Inside V{{hoveredCell.reflection.source}}, layer 2: opposite {{hoveredCell.reflection.oppositeCell}} ({{hoveredCell.reflection.role}}) → {{hoveredCell.reflection.assignedRole}}</div>
   <div v-if="hoveredCell.edgeSource" id="cell-hover-edge-source">Faces {{formatFaces(hoveredCell.edgeSource.faces)}} · cell {{hoveredCell.edgeSource.cell}}: {{hoveredCell.edgeSource.role}} → {{hoveredCell.edgeSource.assignedRole}}</div>
   <div v-if="hoveredCell.beltPort">{{hoveredCell.beltPort.structure}} · {{hoveredCell.beltPort.label ?? ('layer '+hoveredCell.beltPort.layer)}} · slot {{hoveredCell.beltPort.slot}}<div>{{hoveredCell.beltPort.scope}}</div><div v-if="hoveredCell.beltPort.capacity">{{hoveredCell.beltPort.capacity}} ports · {{hoveredCell.beltPort.internalPorts}} internal · {{hoveredCell.beltPort.freePorts.length}} free</div></div>
   <div v-if="hoveredCell.refinement">Belt panel {{hoveredCell.refinement.panel+1}} · {{hoveredCell.refinement.sourceCell}} · circulation {{hoveredCell.refinement.circulation>0?'+':'−'}}<div>{{hoveredCell.refinement.metric}}</div></div>
   <div v-if="hoveredCell.seamFlows?.length">Seam flows: {{hoveredCell.seamFlows.map(f=>f.id+' · loop '+(f.cycle+1)).join(', ')}}</div>
   <div v-if="hoveredCell.neutralWire">N-sector neutral wire · source N record retained</div>
   <div v-if="hoveredCell.attachment">Attached at {{hoveredCell.attachment.label}} · visual link · excluded from main counts</div>
   <div v-if="hoveredCell.internalSector">Sector {{hoveredCell.internalSector.sector}} · circulation {{hoveredCell.internalSector.circulation>0?'+':'−'}} · face {{hoveredCell.internalSector.face}}<div>{{hoveredCell.internalSector.scope}}</div></div>
   <div v-if="hoveredCell.ruleClosure">Applied rule closure · round {{hoveredCell.ruleClosure.round}}<div v-for="(a,i) in hoveredCell.arrivals" :key="i">{{a.source}} · {{a.rule}} · {{a.front}}</div></div>
   <div v-if="hoveredCell.rulePreview" id="cell-rule-preview">Preview only: {{hoveredCell.rulePreview.role}} · round {{hoveredCell.rulePreview.round}}<div v-for="(a,i) in hoveredCell.rulePreview.arrivals" :key="i">{{a.source}} · {{a.rule}}</div></div>
   <div v-if="hoveredCell.coherence" id="cell-hover-coherence">{{hoveredCell.coherence.pattern}} · {{hoveredCell.coherence.neighbors.map(n=>n.cell+': '+n.role).join(' + ')}} → {{hoveredCell.coherence.role}}<div v-if="hoveredCell.coherence.word">{{hoveredCell.coherence.rule}}<div v-for="n in hoveredCell.coherence.neighbors" :key="n.vertex">V{{n.vertex}}: #{{n.cell}} · {{n.layers.join(' · ')}} · {{n.role}}</div></div></div>
   <div v-if="hoveredCell.translation" id="cell-hover-translation">Copied from {{hoveredCell.translation.cell}} · face {{hoveredCell.translation.face.join('–')}}</div>
   <div v-if="hoveredCell.nearestVertex" id="cell-hover-nearest-vertex">Nearest V{{hoveredCell.nearestVertex.index}} ({{hoveredCell.nearestVertex.role}}) · P/E → P; N → N</div>
   <div v-if="hoveredCell.interiorCopy" id="cell-hover-interior-copy">{{hoveredCell.interiorCopy.layers.join('')}} ← {{hoveredCell.interiorCopy.sources.map(s=>s.layers.join('')+' (cell '+s.cell+')').join(' / ')}}<div v-if="hoveredCell.interiorCopy.boundaryCrossing">{{hoveredCell.interiorCopy.rule}}</div><div v-if="hoveredCell.interiorCopy.directions">Moves: {{hoveredCell.interiorCopy.directions.map(v=>'V'+v+' +1').join(', ')}} · fixed {{hoveredCell.interiorCopy.fixedVertices.map(v=>'V'+v).join(', ')}} · copy source colour</div></div>
   <dl><dt>Lattice centre (4D)</dt><dd>({{formatPosition(hoveredCell.position)}})</dd>
    <dt>World centre (XYZ)</dt><dd>({{formatPosition(hoveredCell.worldPosition)}})</dd>
    <template v-if="hoveredCell.layers"><dt>Simplex movement code (V₁ · V₂ · V₃ · V₄)</dt><dd>{{hoveredCell.layers.join(' · ')}}</dd></template>
    <template v-if="hoveredCell.constructionStep!==null"><dt>Added at step</dt><dd>{{hoveredCell.constructionStep}}</dd></template>
   </dl>
   <small v-if="hoveredCell.context">Orientation reference · outside the cut</small>
   <div v-if="hoveredCell.pinned" class="row"><button id="copy-cell-id" @click="copyCellInfo('id')">Copy ID</button><button id="copy-cell-info" @click="copyCellInfo()">Copy info</button><button id="close-cell-info" @click="viewer?.clearCellHover()">Close</button></div>
   <small v-else>Click to pin this cell</small><small v-if="copyFeedback" role="status">{{copyFeedback}}</small>
   </template>
  </div>
  <details id="inventory-panel" open :class="{'has-inventory': !!pneInventory, 'show-breakdown': inventoryDetails}" v-show="phase==='ready' && !retainedExpansionView && !compositionView && !cellulationView && !seedActive && !(process.id==='sulfur-32' && (appearance.sulfurHexStrands || appearance.sulfurBranchSeed)) && process.id!=='sulfur-32-reflection' && !(process.id==='sulfur-32' && appearance.sulfurHandlebody) && (pneInventory || process.id==='fibration-12x12' || counts.total.total>0) && !['neutron-belt','pair-context-7x4','retained-construction','from-center-cell','unsplit-octahedron'].includes(process.id)">
   <summary>Counts</summary>
   <div class="inventory-content">
   <table id="particle-counts" :aria-label="pneInventory?'P N E inventory by counting domain':process.id==='fibration-12x12'?'Retained P N E cell-role counts by polarity sheet':'Assigned particle counts: surface and interior filler'">
   <caption>{{pneInventory?.faceRows?(inventoryDetails?'Cells, faces & trial records':'Whole cells'):pneInventory?(pneInventory.unit==='nodes'?'P / N / E nodes':'P / N / E counts'):process.id==='fibration-12x12'?'Retained cell roles · not particle counts':'Assigned cells'}}</caption>
   <thead><tr><th scope="col">{{pneInventory?'Counted records':process.id==='fibration-12x12'?'Sheet':'Location'}}</th><th scope="col">P</th><th scope="col">N</th><th scope="col">E</th><th scope="col">Total</th></tr></thead>
   <tbody v-if="pneInventory">
    <tr v-if="pneInventory.faceRows"><th colspan="5" scope="rowgroup">Whole cells</th></tr>
    <tr v-for="row in pneInventory.displayRows" :key="row.id" class="count-primary" :data-count-row="row.id" :title="row.scope"><th scope="row">{{row.label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{row[role]}}</td></tr>
    <template v-if="pneInventory.cellLocationRows"><tr><th colspan="5" scope="rowgroup">Cell locations (same whole-cell total)</th></tr><tr v-for="row in pneInventory.cellLocationRows" :key="row.id" :data-count-row="row.id"><th scope="row">{{row.label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{row[role]}}</td></tr></template>
    <template v-if="pneInventory.voidRows"><tr><th colspan="5" scope="rowgroup">Empty regions · shared-face connectivity</th></tr><tr v-for="row in pneInventory.voidRows" :key="row.id" :data-count-row="row.id"><th scope="row">{{row.label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{row[role]??'—'}}</td></tr></template>
    <template v-if="pneInventory.channelRows"><tr><th colspan="5" scope="rowgroup">Trial N fibres · not cells or voids</th></tr><tr v-for="row in pneInventory.channelRows" :key="row.id" :data-count-row="row.id"><th scope="row">{{row.label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{row[role]??'—'}}</td></tr></template>
    <template v-if="pneInventory.faceRows"><tr><th colspan="5" scope="rowgroup">Exposed faces</th></tr><tr v-for="row in pneInventory.faceRows" :key="row.id" :data-count-row="row.id"><th scope="row">{{row.label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{row[role]??'—'}}</td></tr></template>
   </tbody>
   <tbody v-else-if="process.id==='fibration-12x12' && polarityCounts">
    <tr v-for="[sheet,label] in [['positive','Original'],['negative','Opposite']]" :key="sheet" :data-count-sheet="sheet" :data-displayed="appearance.polaritySheet===sheet">
     <th scope="row">{{label}}{{appearance.polaritySheet===sheet?' •':''}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{polarityCounts[sheet][role]}}</td>
    </tr>
    <template v-if="m.state.value.fibrationAudit.collective">
     <tr v-for="[sheet,label] in [['positive','Effective original'],['negative','Effective opposite']]" :key="sheet" :data-count-row="`effective-${sheet}`"><th scope="row">{{label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role">{{m.state.value.fibrationAudit.collective.counts[sheet][role]}}</td></tr>
     <tr data-count-row="charged-readings" title="Dual-labelled external comparison carriers, not independent particle totals"><th scope="row">External P/E</th><td>{{m.state.value.fibrationAudit.collective.counts.chargedReadings.proton}}</td><td>—</td><td>{{m.state.value.fibrationAudit.collective.counts.chargedReadings.electron}}</td><td>—</td></tr>
    </template>
    <tr v-if="m.state.value.fibrationAudit.neutral" data-count-row="neutral-extension" title="Independent channels in the declared extension, not established neutron particles"><th scope="row">Added N channels</th><td>—</td><td>{{m.state.value.fibrationAudit.neutral.counts.total}}</td><td>—</td><td>{{m.state.value.fibrationAudit.neutral.counts.total}}</td></tr>
    <tr data-count-row="cells" title="Unique geometric cells classified by the displayed polarity sheet"><th scope="row">Cells (shown)</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-cell-role="role" :data-cell-total="role==='total'?'':null">{{polarityCounts[appearance.polaritySheet][role]}}</td></tr>
   </tbody>
   <tfoot v-if="process.id==='fibration-12x12'"><tr><td colspan="5">Same geometry; do not sum sheets.<template v-if="m.state.value.fibrationAudit.collective"><br>Effective = collective comparison carriers.</template></td></tr></tfoot>
   <tfoot v-else-if="pneInventory"><tr><td colspan="5"><template v-if="pneInventory.unassigned">{{pneInventory.unassigned}} unassigned exposed parent faces.<br></template><template v-if="pneInventory.faceRows">Surface cell = at least one exposed face.<br>Filler = interior cell; N may occur in either.<br>Faces counted separately; N denotes an owner, not orientation.<template v-if="pneInventory.voidRows"><br>Void regions assume P/E occupied, N empty.<br>Surface openings join the exterior; not enclosed cavities.</template><br>Full assembly totals; independent of visibility.</template><template v-else-if="pneInventory.note">{{pneInventory.note}}</template><template v-else-if="pneInventory.unit==='nodes'">One node per whole cell.<br>{{process.id==='native-octahedral-bridge'?'Shared-face links; undirected.':'Face links + tip contacts; undirected.'}}</template><template v-else>P/E: exposed faces · N: octahedral fillers.<br>Same cellulation in parents and belt.</template></td></tr></tfoot>
   <tbody v-else><tr v-for="[key,label] in [['surface','Surface'],['filler','Interior filler'],['total','Total']]" :key="key" :data-count-row="key">
    <th scope="row">{{label}}</th><td v-for="role in ['proton','neutron','electron','total']" :key="role" :data-count-role="role">{{counts[key][role]}}</td>
   </tr><tr v-if="cutAudit" data-count-row="cut"><th scope="row">Visible cut</th><td v-for="role in ['proton','neutron','electron','total']" :key="role">{{cutAudit.counts[role]}}</td></tr></tbody>
   </table>
   <label class="inventory-detail-toggle"><input id="inventory-details" v-model="inventoryDetails" type="checkbox"> Breakdown &amp; notes</label>
   </div>
  </details>
  <div v-if="cellulationView" id="cellulation-dot-controls" role="group" aria-label="Dot rotation locks">
   <button v-for="dot in view.cellulationDots??[]" :key="dot.id" v-show="dot.visible" class="cellulation-dot-lock" :data-dot-lock="dot.id" :style="{left:dot.x+'px',top:dot.y+'px'}" :aria-pressed="dot.locked" :aria-label="`${dot.locked?'Release':'Fix'} dot and normal; ID: ${dot.id}; lattice coordinates: ${dot.latticePoint.join(', ')}`" :title="cellulationDotLabel(dot)" @click="viewer?.toggleCellulationAnchor(dot.id)" @dblclick.stop="copyDotId(dot)" @pointerenter="viewer?.hoverCellulationDot(dot.id)" @pointerleave="viewer?.hoverCellulationDot(null)" @pointercancel="viewer?.hoverCellulationDot(null)"></button>
  </div>
  <div v-if="cellulationView" id="cellulation-grid-labels" aria-hidden="true">
   <svg width="100%" height="100%"><line v-for="label in (view.cellulationGridLabels??[]).filter(l=>l.visible)" :key="label.key" :x1="label.anchorX" :y1="label.anchorY" :x2="label.leaderX" :y2="label.leaderY" /></svg>
   <span v-for="label in view.cellulationGridLabels??[]" :key="label.key" v-show="label.visible" class="cellulation-grid-label" :data-grid-label="label.kind" :style="{left:label.x+'px',top:label.y+'px'}">{{label.text}}</span>
  </div>
  <div v-if="cellulationView && view.gridVertexCandidate" id="grid-vertex-candidate" aria-hidden="true">
   <span class="grid-vertex-candidate-ring" :style="{left:view.gridVertexCandidate.x+'px',top:view.gridVertexCandidate.y+'px'}"></span>
   <span class="cellulation-grid-label" :style="{left:view.gridVertexCandidate.labelX+'px',top:view.gridVertexCandidate.labelY+'px'}">{{view.gridVertexCandidate.text}}</span>
  </div>
  <div v-if="cellulationView && dotCopyFeedback" id="cellulation-copy-status" role="status" aria-live="polite">{{dotCopyFeedback}}</div>
  <svg v-if="cellulationView && appearance.cellulationValidateLoop && view.loopOverlay" id="loop-validation-overlay" width="100%" height="100%" aria-hidden="true">
   <g v-for="issue in view.loopOverlay.issues" :key="issue.id" v-show="issue.visible" class="loop-issue" :data-loop-issue="issue.type">
    <line v-if="issue.start && issue.end" :x1="issue.start.x" :y1="issue.start.y" :x2="issue.end.x" :y2="issue.end.y" stroke="#ffb84d" stroke-width="5" stroke-opacity=".8" />
    <circle :cx="issue.x" :cy="issue.y" r="10" fill="#161019" stroke="#ffb84d" stroke-width="2" /><text :x="issue.x" :y="issue.y+4" text-anchor="middle" fill="#ffb84d">{{issue.id+1}}</text>
   </g>
   <g v-for="join in view.loopOverlay.joins" :key="join.id" v-show="join.visible" :data-loop-join="join.id" :data-status="join.status">
    <circle :cx="join.x" :cy="join.y" r="9" fill="none" :stroke="join.status==='pass'?'#77dfa7':'#ffb84d'" stroke-width="2" />
    <text :x="join.x+13" :y="join.y-12" :fill="join.status==='pass'?'#77dfa7':'#ffb84d'">{{join.id}}</text>
   </g>
  </svg>
  <svg id="orientation-compass" v-show="phase==='ready'" viewBox="0 0 152 160" role="img" aria-label="Camera orientation: XYZ directions and XY, XZ, YZ planes">
   <rect x="1" y="1" width="150" height="158" rx="9" fill="#0b1020" fill-opacity=".82" stroke="#8ba9d0" stroke-opacity=".3" />
   <defs><marker id="compass-arrowhead" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L6 3L0 6Z" fill="context-stroke" /></marker></defs>
   <polygon v-for="plane in compass.planes" :key="plane.name" :data-compass-plane="plane.name" :points="plane.points" :fill="plane.color" fill-opacity=".14" :stroke="plane.color" stroke-opacity=".4" />
   <g v-for="axis in compass.directions" :key="axis.key" :data-compass-direction="axis.key">
    <line :x1="compass.center.x" :y1="compass.center.y" :x2="axis.x" :y2="axis.y" :stroke="axis.color" :stroke-width="axis.positive?1.8:1" :stroke-dasharray="axis.positive?undefined:'3 3'" marker-end="url(#compass-arrowhead)" />
    <text :x="axis.labelX" :y="axis.labelY" :fill="axis.color" text-anchor="middle" dominant-baseline="central">{{axis.key}}</text>
   </g>
   <circle :cx="compass.center.x" :cy="compass.center.y" r="2.5" fill="white" />
   <text v-for="plane in compass.planes" :key="plane.name+'-legend'" :x="plane.legendX" y="147" :fill="plane.color" text-anchor="middle">{{plane.name}}</text>
  </svg>
  <button id="viewport-reset" v-show="phase==='ready'" aria-label="Reset view" title="Reset view" @click="reset">↺</button>
  <button v-if="cellulationView && appearance.cellulationStep!==0" id="viewport-recenter" v-show="phase==='ready'" aria-label="Recenter" title="Recenter: fit the construction without rotating" @click="recenter"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M12 7v10M7 12h10"/></svg></button>
  <button id="role-label-toggles" v-show="!compositionView && !cellulationView && phase==='ready' && (m.state.value.assignments.length>0 || m.state.value.presentationLabels?.length>0)" aria-label="Particle labels" :title="appearance.labels?'Hide particle labels':'Show particle labels'" :aria-pressed="appearance.labels" @click="appearance.labels=!appearance.labels">P|N|E</button>
  <div id="vertex-labels" v-show="phase==='ready' && !seedActive && !['sulfur-32-reflection','sulfur-32','single-octahedral','native-octahedral-bridge','signed-octahedral-belt','neutron-belt','pair-context-7x4','unsplit-octahedron'].includes(process.id)" role="group" aria-label="Vertex rotation anchors">
   <svg aria-hidden="true" width="100%" height="100%" style="position:absolute;inset:0;pointer-events:none;overflow:visible">
    <line v-for="v in vertexLabels.filter(v=>v.visible)" :key="v.key" :x1="v.anchorX" :y1="v.anchorY" :x2="v.leaderX" :y2="v.leaderY" stroke="currentColor" stroke-opacity=".45" stroke-width="1" />
   </svg>
   <button v-for="v in vertexLabels" :key="v.key" v-show="v.visible" class="vertex-label" :data-lock-vertex="v.index" :style="{left:v.x+'px',top:v.y+'px'}" :aria-pressed="locks[v.key]" :aria-label="`${v.text}: ${locks[v.key]?'release':'fix'} rotation anchor`" :title="`${v.text}: ${locks[v.key]?'fixed — click to release':'click to fix rotation'}`" @click="locks[v.key]=!locks[v.key]">{{['cell-fibration','fibration-12x12'].includes(process.id)&&v.index===2?'V₂≡V₅':v.text}}</button>
  </div>
 </Teleport>
</template>
