<script setup>
import { onMounted, onUnmounted, watch } from 'vue';
import { createViewer } from './scene.js';
import { useViewerModel } from './useViewerModel.js';
import { defaults } from './model.js';

const props = defineProps({ host: { type: HTMLElement, required: true } });
const model = useViewerModel();
const { parameters, motion, ready, weights, damping, summary, status, phase } = model;
const lifetime = new AbortController();
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
// Plain imperative handle: never put a renderer, scene, camera or material in reactive().
let viewer;
function fail(error) {
  motion.running = false;
  model.error.value = error.message;
  phase.value = 'fallback';
}
function reset() { viewer?.reset(); }
function dispose() {
  lifetime.abort(); viewer?.dispose(); motion.running = false; phase.value = 'fallback';
}
watch(model.renderState, state => viewer?.update(state), { flush: 'post' });
watch(phase, value => { document.documentElement.dataset.view = value === 'ready' ? 'webgl' : value; }, { immediate: true });
onMounted(async () => {
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) motion.running = false;
  }, { signal: lifetime.signal });
  try {
    viewer = await createViewer({ host: props.host, signal: lifetime.signal, onFailure: fail,
      onParticlePlaced: () => { motion.running = true; } });
    if (lifetime.signal.aborted) { viewer.dispose(); return; }
    phase.value = 'ready';
    viewer.update(model.renderState.value);
  } catch (error) {
    if (!lifetime.signal.aborted) fail(error);
  }
});
onUnmounted(dispose);
defineExpose({ dispose, snapshot: () => ({ ...viewer?.snapshot(), phase: phase.value,
  panel: { ...model.renderState.value, summary: summary.value } }) });
</script>

<template>
  <p id="status" role="status">{{ status }}</p>
  <p id="instructions">Click the plane to place a particle, replacing the previous one. Drag to orbit; scroll or pinch to zoom. Placement starts motion automatically; use Pause to stop it.</p>
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
      <summary>Attractors · XY plane</summary>
      <label for="weight-a">A (−3, 0) <output>{{ weights.weightA.toFixed(2) }}</output></label>
      <input id="weight-a" v-model.number="parameters.weightA" type="range" min="0" max="5" step="0.05">
      <label for="weight-b">B (3, 0) <output>{{ weights.weightB.toFixed(2) }}</output></label>
      <input id="weight-b" v-model.number="parameters.weightB" type="range" min="0" max="5" step="0.05">
    </details>
    <details open>
      <summary>Momentum</summary>
      <label for="damping">Damping γ <output>{{ damping.toFixed(2) }} s⁻¹</output></label>
      <input id="damping" v-model.number="parameters.damping" type="range" min="0" max="3" step="0.05">
      <p>Lower γ retains momentum; higher γ damps it. At γ = 0 there is no drag.</p>
      <p>Only one particle is present at a time. Each click replaces it at rest and clears its trail.</p>
      <p>The gold ring marks the active pole. After the particle passes closest to that center within 0.6 units, attraction switches to the opposite pole without resetting velocity. The nearer pole attracts first.</p>
      <p>Low damping favors repeated passes. Strong damping can stop the particle approaching a center without passing it; a zero-weight active pole cannot pull it onward.</p>
      <div class="button-row">
        <button id="run" type="button" :aria-pressed="motion.running" @click="motion.running = !motion.running">{{ motion.running ? 'Pause' : 'Run particle' }}</button>
        <button id="reset-particles" type="button" @click="viewer?.resetParticles()">Clear particle</button>
        <button id="reset-settings" type="button" @click="Object.assign(parameters, defaults())">Reset parameters</button>
      </div>
    </details>
  </fieldset>
  <p id="panel-summary">{{ summary }}</p>
  <p>dx/dt = v; dv/dt = F(x) − γv. Unit mass; particles start at rest. Clear particle removes the particle and its trail.</p>
  <p>Saffron arrows show the active pole’s attraction; the green particle and trail show motion. Automatic motion is off initially. The static diagram remains usable if WebGL or dependencies fail.</p>
</template>
