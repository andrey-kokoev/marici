<script setup lang="ts">
import { computed, onScopeDispose, watch } from "vue";
import { useDiagramInspection } from "./useDiagramInspection.js";
import { useCatalog } from "./stores/catalog.js";
import { useDiagramCamera } from "./useDiagramCamera.js";
import DiagramGlyphs from "./DiagramGlyphs.vue";
import NamedVersions from "./NamedVersions.vue";
import MorseSurface from "./MorseSurface.vue";
const view = useDiagramCamera();
const camera = view.camera;
const catalog = useCatalog();
function choose(event: Event, field: "edge" | "turn" | "speed"): void {
  if (!(event.target instanceof HTMLSelectElement)) return;
  if (field === "edge") selectEdge(event.target.value);
  if (field === "turn") catalog.setTurn(event.target.value);
  if (field === "speed") catalog.setSpeed(event.target.value);
}
const { store, projection, selectEdge, selectVertex, routeLabels, marker, visitedSteps } =
  useDiagramInspection();
const playAction = computed(() =>
  store.state.playback.playing
    ? "Pause"
    : store.state.route === null
      ? "Start"
      : store.routeFinished
        ? "Restart"
        : "Resume",
);
function togglePlayback(): void {
  if (store.state.playback.playing) store.pause();
  else if (store.state.route === null || store.routeFinished) store.run(catalog.state.initialTurn);
  else store.resume();
}
function clickEdge(edgeId: string): void {
  if (camera.state.moveMode) return;
  const edge = projection.value?.edges.find((value) => value.id === edgeId);
  if (edge?.color === "green" || edge?.direction === "unresolved") selectEdge(edgeId);
  else store.cycleEdge(edgeId);
}
let timer: number | undefined;
function stopClock(): void {
  if (timer !== undefined) window.clearInterval(timer);
  timer = undefined;
}
watch(
  () => store.state.playback.playing,
  (playing) => {
    stopClock();
    if (!playing) return;
    let previous = performance.now();
    timer = window.setInterval(() => {
      const now = performance.now();
      store.advancePlayback(Math.min(100, now - previous) * Number(catalog.state.speed));
      previous = now;
    }, 16);
  },
  { flush: "sync" },
);
onScopeDispose(() => {
  stopClock();
  store.pause();
});
</script>

<template>
  <section class="active-diagram" aria-labelledby="diagram-heading">
    <header class="diagram-title">
      <h2 id="diagram-heading">{{ catalog.state.selected }}</h2>
      <p v-if="catalog.state.showCounts && catalog.selected">
        {{ catalog.selected.protons }} P · {{ catalog.selected.neutrons }} N
      </p>
    </header>
    <template v-if="projection !== null">
      <section class="route-readouts" aria-label="Traversal readouts">
        <p
          v-if="store.colorBalance && !store.colorBalance.balanced"
          id="color-balance-error"
          role="alert"
        >
          Invalid color balance: {{ store.colorBalance.red }} red,
          {{ store.colorBalance.blue }} blue. Red and blue segment counts must be equal. Editing and
          diagnostic playback remain available.
        </p>
        <p v-if="store.editError" id="edge-edit-error" role="alert">{{ store.editError }}</p>
        <p
          v-if="store.activeDocument?.policy.status === 'unresolved'"
          id="route-status"
          tabindex="0"
          aria-label="Route status"
        >
          {{ store.activeDocument.policy.questions.join(" ") }}
        </p>
        <template v-else>
          <p id="path-taken" aria-live="polite">Path taken: {{ routeLabels }}</p>
          <p id="route-status" tabindex="0" aria-label="Route status" aria-live="polite">
            {{ store.routeFinished ? store.state.route?.message : "" }}
          </p>
        </template>
      </section>
      <Teleport defer to="#diagram-toolbar">
        <div class="toolbar">
          <template v-if="store.activeDocument?.policy.status === 'alternating'">
            <button
              id="step-back"
              type="button"
              title="step back"
              aria-label="step back"
              :disabled="store.state.route === null || store.state.playback.elapsedMs === 0"
              @click="store.stepBack"
            >
              &lt;
            </button>
            <button
              id="play-pause"
              type="button"
              :title="playAction"
              :aria-label="playAction"
              :disabled="
                (store.state.route === null || store.routeFinished) &&
                store.state.selection.kind !== 'edge'
              "
              @click="togglePlayback"
            >
              {{ store.state.playback.playing ? "||" : "|>" }}
            </button>
            <button
              id="step-forward"
              type="button"
              title="step forward"
              aria-label="step forward"
              :disabled="
                store.state.route === null
                  ? store.state.selection.kind !== 'edge'
                  : store.routeFinished
              "
              @click="store.stepForward(catalog.state.initialTurn)"
            >
              &gt;
            </button>
            <button type="button" @click="store.clearRoute">Clear path</button>
          </template>
          <div class="zoom-controls" aria-label="View controls">
            <button
              aria-label="Zoom out"
              :disabled="camera.state.zoom <= 0.25"
              @click="camera.zoomBy(0.8)"
            >
              −
            </button>
            <button aria-label="Fit graph" @click="camera.fit">Fit</button>
            <output id="zoom-level">{{ Number(camera.state.zoom.toFixed(2)) }}×</output>
            <button
              aria-label="Zoom in"
              :disabled="camera.state.zoom >= 8"
              @click="camera.zoomBy(1.25)"
            >
              +
            </button>
            <button
              :aria-pressed="camera.state.moveMode"
              title="Drag to pan; arrow keys when the graph is focused"
              @click="camera.toggleMove"
            >
              Move
            </button>
          </div>
          <label
            >Start edge<select
              id="start-edge"
              :value="store.state.selection.kind === 'edge' ? store.state.selection.edgeId : ''"
              @change="choose($event, 'edge')"
            >
              <option disabled value="">Select</option>
              <option
                v-for="edge in [...projection.edges].sort(
                  (a, b) => Number(a.label) - Number(b.label),
                )"
                :key="edge.id"
                :value="edge.id"
              >
                {{ edge.label }}
              </option>
            </select></label
          >
          <label
            >First turn<select
              id="first-turn"
              :value="catalog.state.initialTurn"
              @change="choose($event, 'turn')"
            >
              <option value="left">Left</option>
              <option value="right">Right</option>
            </select></label
          >
          <label
            >Speed<select
              id="playback-speed"
              :value="catalog.state.speed"
              @change="choose($event, 'speed')"
            >
              <option value="0.5">0.5×</option>
              <option value="1">1×</option>
              <option value="2">2×</option>
              <option value="4">4×</option>
            </select></label
          >
          <label
            ><input
              id="edge-labels"
              type="checkbox"
              :checked="store.state.showEdgeLabels"
              @change="store.toggleLabels"
            />
            Show edge labels</label
          >
          <NamedVersions />
          <MorseSurface />
        </div>
      </Teleport>
      <svg
        :viewBox="camera.viewBox"
        role="group"
        aria-label="Diagram"
        tabindex="0"
        :class="{ moving: camera.state.moveMode, dragging: view.dragging.value }"
        @pointerdown="view.pointerDown"
        @pointermove="view.pointerMove"
        @pointerup="view.pointerUp"
        @pointercancel="view.pointerUp"
        @lostpointercapture="view.endDrag"
        @wheel.prevent="view.wheel"
        @keydown="view.keydown"
        @click.capture="view.click"
      >
        <polyline
          v-for="(step, index) in store.routeFinished ? visitedSteps : visitedSteps.slice(0, -1)"
          :key="`${index}:${step.edgeId}`"
          :points="projection.edges.find((edge) => edge.id === step.edgeId)?.points"
          class="route-trail"
        />
        <DiagramGlyphs
          :projection="projection"
          :selection="store.state.selection"
          namespace="inspection"
          :show-labels="store.state.showEdgeLabels"
          interactive
          :edge-hint="store.edgeEditHint"
          @edge="clickEdge"
          @vertex="selectVertex"
        />
        <circle v-if="marker !== null" id="route-marker" :cx="marker.x" :cy="marker.y" r="5" />
      </svg>
    </template>
    <p v-else class="unavailable">Diagram not yet available.</p>
  </section>
</template>

<style scoped>
.active-diagram {
  flex: 1;
  min-width: 320px;
  position: relative;
  min-height: 220px;
  isolation: isolate;
}
.diagram-title {
  position: absolute;
  z-index: 1;
  top: 12px;
  left: 12px;
  pointer-events: none;
}
.diagram-title p {
  font-size: 11px;
  color: var(--muted);
}
.route-readouts {
  position: absolute;
  z-index: 1;
  bottom: 12px;
  left: 12px;
  right: 12px;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
}
#play-pause,
#step-back,
#step-forward {
  min-width: 32px;
}
#path-taken {
  grid-column: 1 / -1;
  min-width: 0;
  justify-self: start;
  max-width: 100%;
  white-space: nowrap;
  overflow-x: auto;
  scrollbar-width: thin;
  font:
    12px ui-monospace,
    monospace;
}
#route-status {
  grid-column: 1 / -1;
  min-width: 0;
  justify-self: start;
  max-width: 100%;
  max-height: 64px;
  line-height: 16px;
  white-space: normal;
  overflow: auto;
  scrollbar-width: thin;
  overflow-wrap: anywhere;
}
.route-readouts p {
  font-size: 12px;
  background: var(--surface);
}
.route-readouts p:not(:empty),
.toolbar button,
.toolbar select,
.toolbar label {
  pointer-events: auto;
}
#route-status:empty {
  display: none;
}
.unavailable {
  position: absolute;
  inset: 50% 0 auto;
  text-align: center;
  padding: 24px;
  color: var(--muted);
}
svg {
  display: block;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}
.route-trail {
  fill: none;
  stroke: var(--ink);
  stroke-width: 4;
  stroke-opacity: 0.3;
  pointer-events: none;
}
#route-marker {
  fill: #ffbf00;
  stroke: #111;
  stroke-width: 2;
  pointer-events: none;
}
.toolbar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  font-size: 11px;
}
.zoom-controls {
  display: flex;
  align-items: center;
  gap: 2px;
  border-right: 1px solid var(--line);
  padding-right: 6px;
}
#zoom-level {
  width: 4em;
  text-align: center;
  font-variant-numeric: tabular-nums;
}
svg.moving,
svg.moving :deep(g),
svg.moving :deep(circle) {
  cursor: grab;
  touch-action: none;
}
svg.dragging,
svg.dragging :deep(g),
svg.dragging :deep(circle) {
  cursor: grabbing;
}
.toolbar label {
  display: flex;
  align-items: center;
  gap: 5px;
}
.toolbar select {
  padding: 4px;
}
@media (max-width: 700px) {
  .active-diagram {
    min-width: 300px;
  }
  .toolbar {
    gap: 6px;
  }
}
</style>
