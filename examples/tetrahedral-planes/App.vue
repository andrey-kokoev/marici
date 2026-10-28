<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from 'vue';
import { usePlanesModel } from './usePlanesModel.js';
const props = defineProps({ host: { type: HTMLElement, required: true } });
const model = usePlanesModel();
const { state, summary, volume } = model;
const phase = ref('loading'), error = ref('');
const ready = computed(() => phase.value === 'ready');
const status = computed(() => ready.value ? summary.value : phase.value === 'loading'
  ? 'Loading local 3D view. Static diagram available.' : `Static diagram shown. ${error.value || 'Viewer stopped.'}`);
let viewer, stopped = false; // Never proxy Three.js objects with reactive().
function fail(reason) { error.value = reason.message; phase.value = 'fallback'; }
function dispose() { stopped = true; viewer?.dispose(); phase.value = 'fallback'; }
watch(model.geometry, packet => viewer?.updateGeometry(packet), { flush: 'post' });
watch(() => state.opacity, opacity => viewer?.setOpacity(opacity), { flush: 'post' });
watch(phase, value => { document.documentElement.dataset.view = value === 'ready' ? 'webgl' : value; }, { immediate: true });
onMounted(async () => {
  try {
    // Mount the expressive panel first; the renderer is a separately cached chunk.
    const { createPlanesViewer } = await import('./scene.js');
    if (stopped) return;
    viewer = createPlanesViewer({ host: props.host, onFailure: fail });
    viewer.setOpacity(state.opacity); viewer.updateGeometry(model.geometry.value); phase.value = 'ready';
  } catch (reason) { if (!stopped) fail(reason); }
});
onUnmounted(dispose);
defineExpose({ dispose, snapshot: () => ({ ...viewer?.snapshot(), phase: phase.value,
  summary: summary.value, disks: model.repeated.value.length, vertices: model.region.value.vertices.length,
  faces: model.region.value.faces.length, segments: model.segments.value.length / 2, volume: volume.value }) });
</script>

<template>
  <p id="status" role="status">{{ status }}</p>
  <p id="instructions">Drag to rotate freely, including camera roll. Scroll or pinch to zoom. Buttons provide keyboard camera navigation.</p>
  <fieldset id="controls" :disabled="!ready">
    <legend>Tetrahedral planes</legend>
    <details open>
      <summary>Planes · {{ state.repeats * 4 }} disks</summary>
      <label for="opacity">Plane opacity <output id="opacityOut">{{ state.opacity.toFixed(2) }}</output></label>
      <input id="opacity" v-model.number="state.opacity" type="range" min="0" max="0.7" step="0.01">
      <label for="offset">Plane distance <output id="offsetOut">{{ state.distance.toFixed(2) }}</output></label>
      <input id="offset" v-model.number="state.distance" type="range" min="0" max="2" step="0.01">
      <label for="repeats">Plane repeats <output id="repeatOut">{{ state.repeats }}</output></label>
      <input id="repeats" v-model.number="state.repeats" type="range" min="1" max="15" step="1">
      <label for="size">Disk radius <output id="sizeOut">{{ state.radius.toFixed(2) }}</output></label>
      <input id="size" v-model.number="state.radius" type="range" min="1" max="20" step="0.05">
    </details>
    <details open>
      <summary>Layers and region</summary>
      <label><input id="showIntersections" v-model="state.intersections" type="checkbox"> Disk intersections</label>
      <label><input id="showEdges" v-model="state.edges" type="checkbox"> Tetrahedron edges</label>
      <label><input id="showSolid" v-model="state.solid" type="checkbox"> Tetrahedron interior</label>
      <p id="volume">Half-space volume: {{ volume.toFixed(4) }}</p>
    </details>
    <details open>
      <summary>Camera</summary>
      <div class="button-row">
        <button id="left" type="button" @click="viewer?.rotate('yaw', -Math.PI / 12)">Rotate left</button>
        <button id="right" type="button" @click="viewer?.rotate('yaw', Math.PI / 12)">Rotate right</button>
        <button id="up" type="button" @click="viewer?.rotate('pitch', -Math.PI / 12)">Rotate up</button>
        <button id="down" type="button" @click="viewer?.rotate('pitch', Math.PI / 12)">Rotate down</button>
        <button id="roll-left" type="button" @click="viewer?.rotate('roll', -Math.PI / 12)">Roll left</button>
        <button id="roll-right" type="button" @click="viewer?.rotate('roll', Math.PI / 12)">Roll right</button>
        <button id="zoom-in" type="button" @click="viewer?.zoom(1.2)">Zoom in</button>
        <button id="zoom-out" type="button" @click="viewer?.zoom(1 / 1.2)">Zoom out</button>
        <button id="reset" type="button" @click="viewer?.reset()">Reset camera</button>
      </div>
    </details>
  </fieldset>
  <p class="small">The region uses four infinite half-spaces. Finite disks only display the planes; changing their radius does not change the tetrahedron. Repeats add disks, not new region constraints.</p>
</template>
