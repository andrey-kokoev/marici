<script setup>
import { onMounted, onUnmounted, watch } from 'vue';
import { createViewer } from './scene.js';
import { useViewerModel } from './useViewerModel.js';
const props=defineProps({host:{type:HTMLElement,required:true}});
const model=useViewerModel();
const {opacity,phase,ready,status}=model;
const lifetime=new AbortController();let viewer;
function fail(error){model.error.value=error.message;phase.value='fallback';}
function dispose(){lifetime.abort();viewer?.dispose();phase.value='fallback';}
watch(model.renderState,state=>viewer?.update(state),{flush:'post'});
onMounted(async()=>{
  try {
    viewer=await createViewer({host:props.host,signal:lifetime.signal,onFailure:fail});
    if(lifetime.signal.aborted){viewer.dispose();return;}
    phase.value='ready';viewer.update(model.renderState.value);
  }catch(error){if(!lifetime.signal.aborted)fail(error);}
});
onUnmounted(dispose);
defineExpose({dispose,snapshot:()=>({...viewer?.snapshot(),phase:phase.value})});
</script>
<template>
  <p id="status" role="status">{{ status }}</p>
  <p id="instructions">Drag to orbit; scroll or pinch to zoom.</p>
  <fieldset :disabled="!ready"><legend>Outer shell only</legend>
    <p>ESD₇(Δ³) boundary: 100 vertices, 294 edges, 196 triangular faces.</p>
    <label for="opacity">Surface opacity <output>{{ Number(opacity).toFixed(2) }}</output></label>
    <input id="opacity" v-model.number="opacity" type="range" min="0" max="0.5" step="0.01">
    <div class="button-row">
      <button id="left" @click="viewer?.orbit(-Math.PI/12)">Rotate left</button>
      <button id="right" @click="viewer?.orbit(Math.PI/12)">Rotate right</button>
      <button id="up" @click="viewer?.orbit(0,-Math.PI/12)">Rotate up</button>
      <button id="down" @click="viewer?.orbit(0,Math.PI/12)">Rotate down</button>
      <button id="zoom-in" @click="viewer?.zoom(0.85)">Zoom in</button>
      <button id="zoom-out" @click="viewer?.zoom(1/0.85)">Zoom out</button>
      <button id="reset" @click="viewer?.reset()">Reset view</button>
    </div>
  </fieldset>
  <p>No interior cells, paths, arrows, or growth rules.</p>
</template>
