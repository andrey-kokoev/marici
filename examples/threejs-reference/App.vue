<script setup>
import { onMounted, onUnmounted, watch } from 'vue';
import { createViewer } from './scene.js';
import { useViewerModel } from './useViewerModel.js';

const props = defineProps({ host: { type: HTMLElement, required: true } });
const model = useViewerModel();
const { appearance, motion, ready, opacity, appearanceSummary, summary, status, phase } = model;
const lifetime = new AbortController();
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
// Plain imperative handle: never put a renderer, scene, camera or material in reactive().
let viewer;
function fail(error) {
  motion.spin = false;
  model.error.value = error.message;
  phase.value = 'fallback';
}
function reset() { motion.spin = false; viewer?.reset(); }
function dispose() {
  lifetime.abort(); viewer?.dispose(); motion.spin = false; phase.value = 'fallback';
}
watch(model.renderState, state => viewer?.update(state), { flush: 'post' });
watch(phase, value => { document.documentElement.dataset.view = value === 'ready' ? 'webgl' : value; }, { immediate: true });
onMounted(async () => {
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) motion.spin = false;
  }, { signal: lifetime.signal });
  try {
    viewer = await createViewer({ host: props.host, signal: lifetime.signal, onFailure: fail });
    if (lifetime.signal.aborted) { viewer.dispose(); return; }
    phase.value = 'ready';
    viewer.update(model.renderState.value);
  } catch (error) {
    if (!lifetime.signal.aborted) fail(error);
  }
});
onUnmounted(dispose);
defineExpose({ dispose, snapshot: () => ({ ...viewer?.snapshot(), phase: phase.value,
  panel: { opacity: opacity.value, appearance: appearanceSummary.value, summary: summary.value } }) });
</script>

<template>
  <p id="status" role="status">{{ status }}</p>
  <p id="instructions">Drag to orbit; scroll or pinch to zoom. Keyboard buttons provide camera navigation without dragging.</p>
  <fieldset id="controls" :disabled="!ready">
    <legend>View</legend>
    <details open>
      <summary>Camera</summary>
      <div class="button-row">
        <button id="left" type="button" @click="viewer?.orbit(-Math.PI / 12)">Rotate left</button>
        <button id="right" type="button" @click="viewer?.orbit(Math.PI / 12)">Rotate right</button>
        <button id="up" type="button" @click="viewer?.orbit(0, -Math.PI / 12)">Rotate up</button>
        <button id="down" type="button" @click="viewer?.orbit(0, Math.PI / 12)">Rotate down</button>
        <button id="zoom-in" type="button" @click="viewer?.zoom(0.85)">Zoom in</button>
        <button id="zoom-out" type="button" @click="viewer?.zoom(1 / 0.85)">Zoom out</button>
        <button id="reset" type="button" @click="reset">Reset view</button>
      </div>
    </details>
    <details open>
      <summary>Appearance · {{ appearanceSummary }}</summary>
      <label for="opacity">Face opacity <output id="opacity-value">{{ opacity.toFixed(2) }}</output></label>
      <input id="opacity" v-model.number="appearance.opacity" type="range" min="0" max="1" step="0.05">
    </details>
    <details open>
      <summary>Motion</summary>
      <button id="spin" type="button" :aria-pressed="motion.spin" @click="motion.spin = !motion.spin">Auto-rotate</button>
    </details>
  </fieldset>
  <p id="panel-summary">{{ summary }}</p>
  <p>Automatic motion is off initially. The static diagram and description remain usable if WebGL or dependencies fail.</p>
</template>
