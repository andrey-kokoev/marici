<script setup>
import {computed,ref,watch,onUnmounted} from 'vue';
import {buildNNPEComposition} from '../../research/realization-tower/sulfur-nnpe-composition.mjs';
const props=defineProps({joins:{type:Array,default:()=>[]},collapsed:Boolean,processOpen:Boolean,sceneOpen:Boolean,projectedPorts:{type:Array,default:()=>[]}});
const emit=defineEmits(['update:joins']);
const selected=ref(null),message=ref('');
const model=computed(()=>buildNNPEComposition(props.joins));
const positions=computed(()=>new Map(props.projectedPorts.map(p=>[p.id,p])));
const groups=computed(()=>props.collapsed?model.value.components:model.value.stars.map(s=>({id:s.id,stars:[s.id],boundary:s.ports.map(p=>p.id),inventory:s.inventory,history:{star:s.id}})));
function choose(id){
 if(model.value.usedPorts.includes(id))return;
 message.value='';
 if(selected.value===id){selected.value=null;return;}
 if(!selected.value){selected.value=id;return;}
 const next=buildNNPEComposition([...model.value.joins,[selected.value,id]]);
 if(next.rejected.length){message.value=next.rejected.at(-1).reason.includes('loop')?'That join would create a loop.':'These surfaces cannot be joined.';return;}
 selected.value=null;emit('update:joins',next.joins);
}
watch(()=>props.collapsed,()=>{selected.value=null;message.value='';});
function audit(){globalThis.normalRayCompositionAudit={...model.value.audit,collapsed:props.collapsed,representation:'diagonal-half-cube',componentsData:model.value.components};}
watch(model,m=>{if(selected.value&&m.usedPorts.includes(selected.value))selected.value=null;audit();},{immediate:true});
watch(()=>props.collapsed,audit);
onUnmounted(()=>{delete globalThis.normalRayCompositionAudit;});
</script>
<template>
 <section id="nnpe-composition" aria-label="Coloured half-cube composition" :style="{'--composition-left':processOpen?'320px':'12px','--composition-right':sceneOpen?'300px':'12px'}">
  <header v-if="message"><div class="composition-status" role="status">{{message}}</div></header>
  <div v-for="c in groups" :key="c.id" class="nnpe-operation" :data-stars="c.stars.join(',')">
   <button v-for="id in c.boundary" :key="id" v-show="positions.get(id)?.visible" class="nnpe-port" :class="{selected:selected===id}" :data-port="id" :aria-label="id" :aria-pressed="selected===id" :disabled="model.usedPorts.includes(id)" :style="{left:(positions.get(id)?.x??0)+'px',top:(positions.get(id)?.y??0)+'px'}" @click="choose(id)"></button>
  </div>
 </section>
</template>
<style scoped>
#nnpe-composition{position:absolute;inset:0;z-index:5;pointer-events:none;color:#eee;}header{position:absolute;left:var(--composition-left);right:var(--composition-right);top:14px;display:flex;justify-content:space-between;gap:8px;font-size:13px;flex-wrap:wrap;text-shadow:0 1px 3px #000;}header span{font-size:11px;color:#bbc1cd}.composition-status{width:100%;height:20px;font-size:12px;color:#ffd36b}.nnpe-operation{display:contents}.nnpe-port{position:absolute;transform:translate(-50%,-50%);width:22px;height:22px;min-height:0;padding:0;border:0;border-radius:50%;background:transparent;pointer-events:auto;cursor:pointer;}.nnpe-port.selected,.nnpe-port:focus-visible{outline:2px solid #ffd36b;background:#ffd36b22}.nnpe-port:disabled{pointer-events:none;}@media(max-width:760px){header{left:12px;right:12px;top:62px;}}
</style>
