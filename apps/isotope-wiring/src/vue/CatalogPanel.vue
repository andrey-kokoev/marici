<script setup lang="ts">
import { nextTick, watch } from "vue";
import { useCatalog } from "./stores/catalog.js";
const catalog = useCatalog();
watch(
  () => [catalog.state.open, catalog.state.selected, catalog.results.length],
  async () => {
    await nextTick();
    if (catalog.state.open)
      document
        .querySelector('#catalog [aria-current="true"]')
        ?.scrollIntoView({ block: "nearest" });
  },
  { immediate: true },
);
function closeCatalog(): void {
  catalog.setOpen(false);
  document.getElementById("catalog-toggle")?.focus();
}
function select(name: string): void {
  catalog.select(name);
  if (!catalog.state.open || window.matchMedia("(max-width:700px)").matches) closeCatalog();
}
function filter(event: Event, field: "query" | "element" | "mass"): void {
  if (event.target instanceof HTMLInputElement || event.target instanceof HTMLSelectElement)
    catalog.setFilter(field, event.target.value);
}
</script>
<template>
  <nav
    v-if="catalog.state.open"
    id="catalog"
    class="catalog"
    :class="{ floating: !catalog.state.docked }"
    aria-label="Isotopes"
    @keydown.esc="closeCatalog"
  >
    <header class="panel-head">
      <h2>Find isotope</h2>
      <button
        id="catalog-pin"
        :aria-pressed="catalog.state.docked"
        :aria-label="catalog.state.docked ? 'Undock isotope panel' : 'Dock isotope panel'"
        @click="catalog.toggleDock"
      >
        <svg
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          aria-hidden="true"
        >
          <rect x="3" y="4" width="18" height="16" rx="2" />
          <path d="M9 4v16" />
        </svg></button
      ><button aria-label="Close isotope catalog" @click="closeCatalog">×</button>
    </header>
    <div class="search-row">
      <input
        type="search"
        aria-label="Search isotope catalog"
        placeholder="Element or isotope"
        :value="catalog.state.query"
        @input="filter($event, 'query')"
      /><button aria-label="Clear search" @click="catalog.setFilter('query', '')">×</button>
    </div>
    <div class="filters">
      <label
        >Element<select
          aria-label="Element"
          :value="catalog.state.element"
          @change="filter($event, 'element')"
        >
          <option value="">All elements</option>
          <option v-for="element in catalog.elements" :key="element">{{ element }}</option>
        </select></label
      ><label
        >Mass<input
          type="number"
          min="1"
          step="1"
          aria-label="Mass number"
          placeholder="Any"
          :value="catalog.state.mass"
          @input="filter($event, 'mass')"
      /></label>
    </div>
    <div class="result-count" role="status">
      {{ catalog.results.length }} isotopes
      <button
        v-if="catalog.state.query || catalog.state.element || catalog.state.mass"
        @click="catalog.resetFilters"
      >
        Reset filters
      </button>
    </div>
    <div class="catalog-results">
      <div v-for="entry in catalog.results" :key="entry.name" class="catalog-item">
        <button :aria-current="catalog.state.selected === entry.name" @click="select(entry.name)">
          <strong>{{ entry.name }}</strong
          ><small
            >{{ entry.protons }} P · {{ entry.neutrons }} N
            <span v-if="!entry.hasDiagram">· No diagram</span></small
          ></button
        ><button
          v-if="entry.name === catalog.state.selected && entry.hasDiagram"
          aria-label="Pin active isotope as reference"
          :aria-pressed="catalog.state.references.some((item) => item.isotope?.name === entry.name)"
          @click="catalog.pin"
        >
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            aria-hidden="true"
          >
            <path d="M8 3h8l-1 7 4 4v2H5v-2l4-4zM12 16v6" />
          </svg>
        </button>
      </div>
      <p v-if="catalog.results.length === 0">No matching isotopes.</p>
    </div>
  </nav>
</template>
<style scoped>
.catalog {
  width: 280px;
  flex: none;
  background: var(--paper);
  border-right: 1px solid var(--line);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 0;
  z-index: 5;
}
.floating {
  position: absolute;
  top: 8px;
  left: 8px;
  bottom: 8px;
  box-shadow: 0 8px 24px #0002;
  border: 1px solid var(--line);
  border-radius: 8px;
}
.panel-head {
  display: flex;
  align-items: center;
  gap: 6px;
}
.panel-head h2 {
  flex: 1;
}
.search-row {
  display: flex;
}
.search-row input {
  width: 100%;
  min-width: 0;
}
.filters {
  display: flex;
  gap: 10px;
}
.filters label {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}
.filters label:first-child {
  flex: 1;
}
.filters input {
  width: 65px;
}
.filters select {
  width: 100%;
}
.catalog-results {
  overflow: auto;
  min-height: 0;
}
.catalog-item {
  display: flex;
  align-items: center;
}
.catalog-item > button:first-child {
  flex: 1;
  text-align: left;
  min-width: 0;
}
.catalog-item strong,
.catalog-item small {
  display: block;
}
.catalog-item strong {
  font-weight: 500;
}
.catalog-item small,
.result-count {
  font-size: 11px;
  color: var(--muted);
}
button[aria-current="true"] {
  background: var(--accent-soft);
  color: var(--accent);
}
@media (max-width: 700px) {
  .catalog {
    position: absolute;
    top: 8px;
    left: 8px;
    bottom: 8px;
    width: min(280px, calc(100% - 16px));
    box-shadow: 0 8px 24px #0002;
    border: 1px solid var(--line);
    border-radius: 8px;
  }
}
</style>
