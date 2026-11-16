<script setup lang="ts">
import { nextTick } from "vue";
import DiagramInspection from "./DiagramInspection.vue";
import CatalogPanel from "./CatalogPanel.vue";
import ReferenceGraphs from "./ReferenceGraphs.vue";
import { useCatalog } from "./stores/catalog.js";
const catalog = useCatalog();
async function toggleCatalog(): Promise<void> {
  catalog.setOpen(!catalog.state.open);
  await nextTick();
  if (catalog.state.open) {
    const input = document.querySelector("#catalog input[type=search]");
    if (input instanceof HTMLInputElement) input.focus();
  }
}
</script>
<template>
  <main class="app-shell">
    <header class="appbar">
      <h1>Isotope Wiring</h1>
      <button
        id="catalog-toggle"
        :aria-expanded="catalog.state.open"
        aria-controls="catalog"
        @click="toggleCatalog"
      >
        {{ catalog.state.selected }} <span aria-hidden="true">▾</span>
      </button>
      <div class="history">
        <button
          aria-label="Previous isotope"
          :disabled="catalog.state.historyIndex === 0"
          @click="catalog.navigate(-1)"
        >
          ‹</button
        ><button
          aria-label="Next isotope"
          :disabled="catalog.state.historyIndex === catalog.state.history.length - 1"
          @click="catalog.navigate(1)"
        >
          ›
        </button>
      </div>
      <div id="diagram-toolbar" />
      <label
        ><input
          type="checkbox"
          :checked="catalog.state.showCounts"
          @change="catalog.toggleCounts"
        />
        Counts</label
      >
    </header>
    <div class="workarea">
      <CatalogPanel />
      <div class="canvas-scene" tabindex="0" role="region" aria-label="Graph comparisons">
        <DiagramInspection /><ReferenceGraphs />
      </div>
    </div>
  </main>
</template>
<style>
:root {
  color-scheme: dark;
  --ink: #dfdfd6;
  --muted: #a2a2a8;
  --line: #2e2e32;
  --paper: #1b1b1f;
  --surface: #202127;
  --hover: #313136;
  --accent: #e2aa72;
  --accent-soft: #3d2c1d;
  --red: #f08078;
  --blue: #82b5ef;
  --green: #8ab78e;
  font:
    13px/1.4 system-ui,
    sans-serif;
  color: var(--ink);
  background: var(--surface);
}
* {
  box-sizing: border-box;
}
body {
  margin: 0;
}
button,
input,
select {
  font: inherit;
  color: inherit;
}
button,
select {
  cursor: pointer;
}
button {
  padding: 6px 10px;
  border: 1px solid transparent;
  background: transparent;
  border-radius: 6px;
}
button:hover {
  background: var(--hover);
}
button:disabled {
  opacity: 0.4;
  cursor: default;
}
button[aria-pressed="true"] {
  background: var(--accent-soft);
  color: var(--accent);
}
input,
select {
  padding: 6px;
  border: 1px solid var(--line);
  border-radius: 5px;
  background: var(--paper);
}
input[type="checkbox"] {
  accent-color: var(--accent);
}
button:focus-visible,
input:focus-visible,
select:focus-visible,
[tabindex]:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
h1,
h2,
p {
  margin: 0;
}
h1,
h2 {
  font-size: 13px;
  font-weight: 600;
}
.app-shell {
  height: 100dvh;
  min-height: 420px;
  display: flex;
  flex-direction: column;
}
.appbar {
  position: relative;
  z-index: 4;
  min-height: 48px;
  flex: none;
  flex-wrap: wrap;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 6px 14px;
  background: var(--paper);
  border-bottom: 1px solid var(--line);
}
#catalog-toggle {
  min-width: 140px;
  text-align: left;
}
.history {
  display: flex;
}
.history button {
  font-size: 22px;
  padding: 0 9px;
}
#diagram-toolbar {
  flex: 1 1 560px;
  min-width: 0;
}
.appbar label {
  font-size: 12px;
  white-space: nowrap;
}
.workarea {
  position: relative;
  flex: 1;
  min-height: 0;
  display: flex;
}
.canvas-scene {
  flex: 1;
  min-width: 0;
  display: flex;
  overflow: auto;
  background-image: radial-gradient(var(--line) 0.7px, transparent 0.7px);
  background-size: 24px 24px;
}
@media (max-width: 700px) {
  .appbar {
    padding: 0 8px;
    gap: 4px;
  }
  .appbar h1 {
    display: none;
  }
  #catalog-toggle {
    min-width: 0;
    flex: 1;
  }
}
@media (pointer: coarse) {
  button,
  select {
    min-height: 44px;
  }
}
</style>
