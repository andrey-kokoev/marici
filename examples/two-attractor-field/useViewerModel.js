import { computed, reactive, ref } from 'vue';
import { defaults } from './model.js';

// Reference-template panel state, independent of WebGL.
export function useViewerModel() {
  const parameters = reactive(defaults());
  const motion = reactive({ running: false });
  const phase = ref('loading'), error = ref('');
  const ready = computed(() => phase.value === 'ready');
  const bounded = (value, max) => Math.min(max, Math.max(0, Number(value) || 0));
  const weights = computed(() => ({ weightA: bounded(parameters.weightA, 5), weightB: bounded(parameters.weightB, 5) }));
  const damping = computed(() => bounded(parameters.damping, 3));
  const fieldSummary = computed(() => `Alternating poles · A weight ${weights.value.weightA.toFixed(2)}, B weight ${weights.value.weightB.toFixed(2)}.`);
  const motionSummary = computed(() => ready.value && motion.running ? 'Particles running.' : 'Particles paused.');
  const summary = computed(() => `${fieldSummary.value} Damping γ = ${damping.value.toFixed(2)} s⁻¹. ${motionSummary.value}`);
  const status = computed(() => phase.value === 'loading'
    ? 'Loading the local Three.js view. A static diagram is available.'
    : ready.value ? `Interactive 3D ready. ${motionSummary.value}`
      : `Static diagram shown. ${error.value || 'Viewer stopped.'}`);
  const renderState = computed(() => ({ ...weights.value, damping: damping.value, running: ready.value && motion.running }));
  return { parameters, motion, phase, error, ready, weights, damping, summary, status, renderState };
}
