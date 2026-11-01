<script setup>
import {computed,ref,watch,onUnmounted} from 'vue';
import BeOctahedralAssembly from './BeOctahedralAssembly.vue';
import {buildBranchingSeed} from '../../research/realization-tower/branching-seed.mjs';
import {buildBerylliumDirectionComponents} from '../../research/realization-tower/beryllium-8-direction-components.mjs';
import {buildBeryllium9Reference} from '../../research/realization-tower/beryllium-9-reference.mjs';
import {buildBeryllium8Reference} from '../../research/realization-tower/beryllium-8-reference.mjs';
import {buildSulfurIncomingBundle} from '../../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurRouteComparison,projectComparisonColumns} from '../../research/realization-tower/sulfur-route-comparison.mjs';
const props=defineProps({centralSleeve:{type:Boolean,default:true},processId:{type:String,default:'sulfur-32'},visibleLayers:{type:Array,required:true},rule:{type:String,default:'pending'},gap:{type:Number,default:2},referenceOn:Boolean,combinedOn:Boolean,processOpen:Boolean,sceneOpen:{type:Boolean,default:true}});
const emit=defineEmits(['update:rule','close']);
const hoveredStrand=ref(null);
watch(()=>[props.referenceOn,props.processId],()=>{hoveredStrand.value=null;});
const isBe=computed(()=>['beryllium-8','beryllium-9'].includes(props.processId));
const reference=computed(()=>props.processId==='beryllium-9'?buildBeryllium9Reference({centralSleeve:props.centralSleeve}):isBe.value?buildBeryllium8Reference():buildSulfurIncomingBundle());
const referenceName=computed(()=>isBe.value?(props.processId==='beryllium-9'?(props.centralSleeve?'Be-9 reference · central sleeve trial':'Be-9 reference (Be-8 clone)'):'Be-8 reference candidate'):'Su-32 reference');
const seed=computed(()=>buildBranchingSeed({processId:props.processId,seedLayerGap:props.gap}));
const comparison=computed(()=>buildSulfurRouteComparison(seed.value,{reference:reference.value,visibleLayers:props.visibleLayers,rule:props.rule}));
const slotCount=computed(()=>comparison.value.reference.length),slotWidth=computed(()=>600/slotCount.value);
const top=computed(()=>projectComparisonColumns(comparison.value.reference,slotCount.value));
const bottom=computed(()=>projectComparisonColumns(comparison.value.combined,slotCount.value));
const directionComponents=computed(()=>isBe.value?buildBerylliumDirectionComponents(comparison.value.reference):[]);
const directionPlots=computed(()=>directionComponents.value.map(row=>({...row,columns:projectComparisonColumns(row.columns,slotCount.value)})));
const colour=n=>'#'+n.toString(16).padStart(6,'0');
const polarityGlyph=q=>q===1?'P/E →':q===-1?'P/E ←':'';
watch(comparison,c=>{globalThis.normalRayComparisonAudit={...c.counts,processId:props.processId,referenceKind:reference.value.kind??'sulfur-native-reference',rule:c.rule,status:c.status,sourceLayers:c.sourceLayers,correspondenceEstablished:c.correspondenceEstablished,referenceIds:c.reference.map(s=>s.id),combinedIds:c.combined.map(s=>s.id),referenceComponentRows:directionComponents.value.map(row=>({direction:row.direction,ids:row.columns.map(s=>s.id),components:row.columns.map(s=>s.selectedComponent),selectionSigns:row.columns.map(s=>s.selectionSign)}))};},{immediate:true});
onUnmounted(()=>{delete globalThis.normalRayComparisonAudit;});
</script>
<template>
 <section id="sulfur-reference-panel"  :aria-label="referenceName+' comparison'" :style="{'--comparison-left':processOpen?'310px':'12px','--comparison-top':processOpen?'10px':'62px','--comparison-gutter':((processOpen?324:24)+(isBe&&sceneOpen?280:0))+'px','--comparison-width':isBe?'1120px':'620px'}">
  <button class="comparison-close" aria-label="Close strand comparison" @click="emit('close')">×</button>
  <h2>Strand comparison</h2>
  <p class="comparison-note">{{slotCount}} aligned columns, one complete projected route per strand. Column positions do not establish an identity correspondence.</p>
  <section v-if="referenceOn" id="sulfur-reference-top">
   <h3>{{isBe?'1 · ':''}}{{referenceName}} · {{slotCount}} identities</h3>
   <small v-if="reference.sleeve">Retained (t,p,e) identities. Strands 7, 2, 1 and 8 pass through one central sleeve; their output matching is unchanged. Two incoming pairs → two outgoing pairs.</small>
   <small v-else-if="isBe">Labels: (t,p,e). Four entry ports; t=± chooses clockwise/counterclockwise around the rim.</small>
   <small v-else>Labels: (a,b,p,e).</small>
   <small>Bottom number: actual output slot. Dot: route start.</small>
   <small v-if="isBe" class="polarity-legend">White/blue strands have forward route arrows. Both mixed groups are white–red; their polarity arrows are: (+,−) along the original route; (−,+) against it. P/E →/← labels mean along/against the original route, independently of t.</small>
   <div :class="{'reference-assembly-row':isBe}">
   <svg viewBox="0 0 640 210" role="img" :aria-label="slotCount+' '+referenceName+' routes'">
    <g v-for="s in top" :key="s.id" class="reference-strand" :class="{'is-highlighted':hoveredStrand===s.id}" :data-strand="s.id" :data-column="s.column" :data-polarity="s.polarityDirection" @pointerenter="hoveredStrand=s.id" @pointerleave="hoveredStrand=null">
     <title>{{s.id}} · output {{s.outputSlot+1}} · {{s.edgeIds.length}} route segments</title>
     <rect pointer-events="all" :x="s.x-slotWidth/2+.75" y="24" :width="slotWidth-1.5" height="160" fill="none" stroke="#ffffff18"/>
     <text :x="s.x" y="16" text-anchor="middle">{{s.label}}</text>
     <text v-if="s.polarityDirection" class="polarity-label" :x="s.x" y="28" text-anchor="middle">{{polarityGlyph(s.polarityDirection)}}</text>
     <polyline :points="s.paths[0].svg" fill="none" :stroke="colour(s.colours[0])" stroke-width="1.8"/>
     <polyline v-if="s.colours.length>1" :points="s.paths[0].svg" fill="none" :stroke="colour(s.colours[1])" stroke-width="1.8" stroke-dasharray="3 3" :stroke-dashoffset="isBe?3:0"/>
     <path v-for="arrow in s.paths[0].polarityArrows" :key="arrow.segment" :class="arrow.kind==='route'?'route-arrow':'polarity-arrow'" :data-segment="arrow.segment" d="M-3,-3 L3,0 L-3,3 Z" fill="#ffffff" :transform="`translate(${arrow.centre.join(',')}) rotate(${arrow.angle})`"/>
     <circle :cx="s.paths[0].coordinates[0][0]" :cy="s.paths[0].coordinates[0][1]" r="2.5" fill="#ffd36b"/>
     <text :x="s.x" y="200" text-anchor="middle">{{s.outputSlot+1}}</text>
     <rect class="strand-hit" :x="s.x-slotWidth/2" y="0" :width="slotWidth" height="210" fill="transparent" pointer-events="all"/>
    </g>
   </svg>
   <BeOctahedralAssembly v-if="isBe" :columns="comparison.reference" :reference="reference" :highlight-id="hoveredStrand" :label="referenceName+' traced octahedron'" />
   </div>
  </section>
  <template v-if="referenceOn && isBe">
   <section v-for="row in directionPlots" :key="row.id" :id="row.id" class="reference-direction-row" :data-direction="row.direction">
    <h3>{{row.title}}</h3>
    <small>The four mixed strands resolve to two white and two red. Only the component changes; paths, identities, polarity arrows and output slots stay fixed.</small>
    <div class="reference-assembly-row">
    <svg viewBox="0 0 640 240" role="img" :aria-label="row.title+' · eight retained strands'">
     <g v-for="s in row.columns" :key="s.id" class="reference-direction-strand" :class="{'is-highlighted':hoveredStrand===s.id}" :data-strand="s.id" :data-column="s.column" :data-polarity="s.polarityDirection" :data-component="s.selectedComponent" @pointerenter="hoveredStrand=s.id" @pointerleave="hoveredStrand=null">
      <title>{{s.id}} · {{s.selectedComponent}} · output slot {{s.outputSlot+1}}</title>
      <text :x="s.x" y="16" text-anchor="middle">{{s.label}}</text>
      <text v-if="s.polarityDirection" class="polarity-label" :x="s.x" y="28" text-anchor="middle">{{polarityGlyph(s.polarityDirection)}}</text>
      <text class="direction-component" :x="s.x" y="38" text-anchor="middle">{{s.selectedComponent}}</text>
      <rect pointer-events="all" :x="s.x-slotWidth/2+.75" y="40" :width="slotWidth-1.5" height="160" fill="none" stroke="#ffffff18"/>
      <g transform="translate(0,16)">
       <polyline :points="s.paths[0].svg" fill="none" :stroke="colour(s.colours[0])" stroke-width="2"/>
       <path v-for="arrow in s.paths[0].polarityArrows" :key="arrow.segment" :class="arrow.kind==='route'?'route-arrow':'polarity-arrow'" :data-segment="arrow.segment" d="M-3,-3 L3,0 L-3,3 Z" fill="#ffffff" :transform="`translate(${arrow.centre.join(',')}) rotate(${arrow.angle})`"/>
       <circle :cx="s.paths[0].coordinates[0][0]" :cy="s.paths[0].coordinates[0][1]" r="2.5" fill="#ffd36b"/>
      </g>
      <text class="direction-output-slot" :x="s.x" y="224" text-anchor="middle">{{s.outputSlot+1}}</text>
      <rect class="strand-hit" :x="s.x-slotWidth/2" y="0" :width="slotWidth" height="240" fill="transparent" pointer-events="all"/>
     </g>
    </svg>
    <BeOctahedralAssembly :columns="row.columns" :reference="reference" :highlight-id="hoveredStrand" :label="row.title+' traced octahedron'" />
    </div>
   </section>
  </template>
  <section v-if="combinedOn" id="sulfur-combined-bottom">
   <h3>Combined · selected layers {{comparison.sourceLayers.join(', ') || 'none'}}</h3>
   <label>Continuation rule
    <select id="seed-comparison-rule" :value="rule" @change="emit('update:rule',$event.target.value)">
     <option value="pending">Not determined</option>
     <option value="same-colour">Candidate: same-colour sleeves / boundary trunks</option>
     <option value="cross-colour">Candidate: crossed sleeves / boundary trunks</option>
    </select>
   </label>
   <p v-if="comparison.status==='rule-pending'" id="comparison-rule-pending">Rule not set. No combined routes are fabricated.</p>
   <p v-else-if="comparison.status==='no-visible-layers'" id="comparison-no-layers">No layers selected.</p>
   <small v-else>{{comparison.counts.combinedStrands}} retained layer identities · {{comparison.counts.sourceCopies}} selected-layer occurrences · {{comparison.counts.projectedPaths}} distinct directed projections. Labels: bottom sleeve + conductor; not native IDs.</small>
   <div :class="{'reference-assembly-row':isBe}">
   <svg viewBox="0 0 640 210" role="img"  :aria-label="'Combined layer routes on '+slotCount+' comparison positions'">
    <g v-for="n in slotCount" :key="'slot'+n"><rect :x="20+(n-1)*slotWidth+.75" y="24" :width="slotWidth-1.5" height="160" fill="none" stroke="#ffffff18"/></g>
    <g v-for="s in bottom" :key="s.id" class="combined-strand" :data-strand="s.id" :data-column="s.column">
     <title>{{s.id}} · {{s.copies.map(c=>'layer '+c.layer+': '+c.word).join('; ')}}</title>
     <text :x="s.x" y="16" text-anchor="middle">{{s.label}}</text>
     <g v-for="(path,i) in s.paths" :key="i" class="combined-route" :data-layers="path.sourceLayers.join(',')">
      <polyline :points="path.svg" fill="none" :stroke="colour(s.colours[0])" stroke-width="1.4" :opacity="s.paths.length>1?.7:1"/>
      <circle :cx="path.coordinates[0][0]" :cy="path.coordinates[0][1]" r="2.2" fill="#ffd36b"/>
     </g>
     <text :x="s.x" y="200" text-anchor="middle">{{s.column+1}}</text>
    </g>
   </svg>
   <div v-if="isBe" aria-hidden="true"></div>
   </div>
  </section>
 </section>
</template>
<style scoped>
#sulfur-reference-panel{position:absolute;left:var(--comparison-left);top:var(--comparison-top);z-index:6;width:min(var(--comparison-width),calc(100vw - var(--comparison-gutter)));max-height:calc(100% - var(--comparison-top) - 10px);overflow:auto;padding:14px;background:var(--viewer-panel);border:1px solid var(--viewer-border);border-radius:6px;box-shadow:0 4px 20px #0007;}
h2{margin:0 0 8px;}h3{font-size:14px;margin:12px 0 6px;}.comparison-close{float:right;min-height:30px;padding:2px 9px;}.comparison-note,small,p{font-size:11px;line-height:1.4;margin:6px 0;}svg{display:block;width:100%;background:#0b1020;margin-top:8px;border-radius:4px;}svg text{fill:#e8e8e8;font:10px monospace;}label{font-size:12px;margin-top:8px;}select{font-size:12px;}#sulfur-combined-bottom{border-top:1px solid var(--viewer-border);margin-top:10px;}
.reference-direction-row{border-top:1px solid var(--viewer-border);margin-top:10px;}svg .direction-component{font-size:9px;}svg .polarity-label{fill:#ffffff;font-size:8px;}
.strand-hit{cursor:crosshair;}.is-highlighted>.strand-hit{fill:#ffffff10;stroke:#ffd36b;stroke-width:1;}
.reference-assembly-row{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(200px,1fr);gap:12px;align-items:start;}
@media(max-width:760px){.reference-assembly-row{grid-template-columns:minmax(0,1fr);}#sulfur-reference-panel{position:fixed;left:12px!important;right:12px;width:auto;top:60px;max-height:calc(100vh - 72px);}}
</style>
