import { computed, reactive, ref } from 'vue';

// Pure panel state: this graph is intentionally independent of WebGL.
export function useViewerModel() {
  const appearance = reactive({ opacity: 0.35 });
  const motion = reactive({ spin: false });
  const phase = ref('loading');
  const error = ref('');
  const ready = computed(() => phase.value === 'ready');
  const opacity = computed(() => Math.min(1, Math.max(0, Number(appearance.opacity) || 0)));
  const opacityPercent = computed(() => Math.round(opacity.value * 100));
  const surface = computed(() => opacity.value === 0 ? 'Edges only' : opacity.value === 1 ? 'Full-opacity faces' : 'Translucent faces');
  // Second- and third-level computations demonstrate expressive derived panels.
  const appearanceSummary = computed(() => `${surface.value} · ${opacityPercent.value}% opacity`);
  const motionSummary = computed(() => ready.value && motion.spin ? 'Automatic motion is on.' : 'Automatic motion is off.');
  const summary = computed(() => `${appearanceSummary.value} · ${motionSummary.value}`);
  const status = computed(() => phase.value === 'loading'
    ? 'Loading the local 3D view. A static diagram is available.'
    : ready.value ? `Interactive 3D ready. ${motionSummary.value}`
      : `Static diagram shown. ${error.value || 'Viewer stopped.'}`);
  const renderState = computed(() => ({ opacity: opacity.value, spin: ready.value && motion.spin }));
  return { appearance, motion, phase, error, ready, opacity, opacityPercent, surface, appearanceSummary, motionSummary, summary, status, renderState };
}
