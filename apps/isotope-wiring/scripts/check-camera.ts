import { createPinia, setActivePinia } from "pinia";
import { useCamera } from "../src/vue/stores/camera.js";
import { useInspection } from "../src/vue/stores/inspection.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
setActivePinia(createPinia());
const inspection = useInspection(),
  camera = useCamera();
const original = JSON.stringify(inspection.state.document),
  fit = camera.viewBox;
inspection.run();
inspection.advancePlayback(400);
const route = JSON.stringify(inspection.state.route),
  playback = JSON.stringify(inspection.state.playback);
camera.zoomBy(2);
expect(camera.state.zoom === 2 && camera.viewBox !== fit, "Zoom failed");
inspection.toggleLabels();
expect(camera.state.zoom === 2, "Labels reset camera");
camera.panBy(15, -25);
expect(camera.state.offsetX === 15 && camera.state.offsetY === -25, "Pan failed");
camera.toggleMove();
expect(camera.state.moveMode, "Move toggle failed");
expect(
  JSON.stringify(inspection.state.document) === original &&
    JSON.stringify(inspection.state.route) === route &&
    JSON.stringify(inspection.state.playback) === playback,
  "Camera changed model, route or playback",
);
camera.fit();
expect(camera.viewBox === fit, "Fit did not restore bounds");
const box = inspection.activeDocument?.layout.viewBox;
if (box === undefined) throw new Error("Missing view box");
const anchor = { x: box.x + box.width / 4, y: box.y + box.height / 4 };
camera.zoomBy(2, anchor);
expect(
  Math.abs(camera.state.offsetX + box.width / 8) < 1e-9 &&
    Math.abs(camera.state.offsetY + box.height / 8) < 1e-9,
  "Anchored zoom moved the cursor's diagram point",
);
camera.zoomBy(1000);
expect(camera.state.zoom === 8, "Maximum zoom not enforced");
camera.zoomBy(0.00001);
expect(camera.state.zoom === 0.25, "Minimum zoom not enforced");
const valid = JSON.stringify(camera.state);
camera.zoomBy(NaN);
camera.panBy(Infinity, 0);
expect(JSON.stringify(camera.state) === valid, "Invalid camera values accepted");
inspection.loadExample();
expect(
  camera.state.zoom === 1 && camera.state.offsetX === 0 && !camera.state.moveMode,
  "Document switch retained stale camera",
);
inspection.unload();
expect(camera.viewBox === undefined, "Unloaded diagram retained view box");
console.log(
  "PASS: zoom limits, anchored zoom, pan, Fit, camera lifecycle and model/route/playback invariance",
);
