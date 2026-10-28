import test from 'node:test';
import assert from 'node:assert/strict';
import { isReactive } from 'vue';
import { useViewerModel } from '../examples/threejs-reference/useViewerModel.js';

test('layered panel computations propagate without WebGL or DOM', () => {
  const model = useViewerModel();
  assert.ok(isReactive(model.appearance));
  assert.equal(model.ready.value, false);
  assert.equal(model.renderState.value.spin, false);
  assert.match(model.status.value, /Loading/);
  model.phase.value = 'ready';
  model.appearance.opacity = 0.7;
  assert.equal(model.opacity.value, 0.7);
  assert.equal(model.opacityPercent.value, 70);
  assert.equal(model.appearanceSummary.value, 'Translucent faces · 70% opacity');
  assert.equal(model.summary.value, 'Translucent faces · 70% opacity · Automatic motion is off.');
  model.motion.spin = true;
  assert.equal(model.renderState.value.spin, true);
  assert.match(model.status.value, /motion is on/);
  model.phase.value = 'fallback';
  model.error.value = 'WebGL unavailable';
  assert.equal(model.renderState.value.spin, false);
  assert.equal(model.status.value, 'Static diagram shown. WebGL unavailable');
  assert.match(model.summary.value, /motion is off/);
});

test('derived opacity is bounded and panel instances are independent', () => {
  const a = useViewerModel(), b = useViewerModel();
  a.appearance.opacity = 2;
  assert.equal(a.opacity.value, 1);
  assert.equal(a.surface.value, 'Full-opacity faces');
  a.appearance.opacity = -1;
  assert.equal(a.opacity.value, 0);
  assert.equal(a.surface.value, 'Edges only');
  a.appearance.opacity = 'not a number';
  assert.equal(a.opacity.value, 0);
  assert.equal(b.opacity.value, 0.35);
  assert.equal(b.phase.value, 'loading');
});
