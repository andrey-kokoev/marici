<script setup lang="ts">
import { nextTick, ref, watch, onScopeDispose } from "vue";
import { VERSION_LIBRARY_PREFIX } from "../named-version-storage.js";
import { useVersions } from "./stores/versions.js";
const versions = useVersions();
const panel = ref<HTMLDialogElement | null>(null);
const opener = ref<HTMLButtonElement | null>(null);
const nameInput = ref<HTMLInputElement | null>(null);
const savedSelect = ref<HTMLSelectElement | null>(null);
const isOpen = ref(false);
let focusGraphOnClose = false;
const name = ref(""),
  selected = ref("");
watch(
  () => versions.names,
  (names) => {
    if (!names.includes(selected.value)) selected.value = "";
  },
  { immediate: true },
);
async function storageChanged(event: StorageEvent): Promise<void> {
  if (event.key !== null && event.key !== VERSION_LIBRARY_PREFIX + versions.documentId) return;
  const focused = document.activeElement;
  versions.refresh();
  await nextTick();
  if (
    isOpen.value &&
    focused !== null &&
    (!focused.isConnected ||
      (focused instanceof HTMLButtonElement && focused.disabled) ||
      (focused instanceof HTMLInputElement && focused.disabled) ||
      (focused instanceof HTMLSelectElement && focused.disabled))
  )
    focusAvailable();
}
if (typeof window !== "undefined") {
  window.addEventListener("storage", storageChanged);
  onScopeDispose(() => window.removeEventListener("storage", storageChanged));
}
watch(
  () => versions.documentId,
  () => {
    name.value = "";
    selected.value = "";
    close();
  },
);
function focusAvailable(): void {
  if (!versions.saveBlockedReason) nameInput.value?.focus();
  else if (versions.names.length) savedSelect.value?.focus();
  else document.getElementById("refresh-versions")?.focus();
}
watch(
  () => versions.saveBlockedReason,
  async () => {
    if (isOpen.value) {
      await nextTick();
      focusAvailable();
    }
  },
);
async function open(): Promise<void> {
  versions.refresh();
  panel.value?.showModal();
  isOpen.value = true;
  await nextTick();
  focusAvailable();
}
function close(): void {
  panel.value?.close();
  closed();
}
function closed(): void {
  if (panel.value?.open || !isOpen.value) return;
  isOpen.value = false;
  const svg = document.querySelector(".active-diagram svg");
  if (focusGraphOnClose && svg instanceof SVGSVGElement) svg.focus();
  else opener.value?.focus();
  focusGraphOnClose = false;
}
function dismissOutside(event: MouseEvent): void {
  if (event.target !== panel.value || panel.value === null) return;
  const bounds = panel.value.getBoundingClientRect();
  if (
    event.clientX < bounds.left ||
    event.clientX > bounds.right ||
    event.clientY < bounds.top ||
    event.clientY > bounds.bottom
  )
    close();
}
async function save(): Promise<void> {
  const savedName = name.value.trim();
  if (versions.save(savedName)) {
    selected.value = savedName;
    name.value = "";
  }
  await nextTick();
  focusAvailable();
  if (versions.error && !versions.saveBlockedReason) nameInput.value?.select();
}
function load(): void {
  if (
    selected.value &&
    window.confirm(
      `Load “${selected.value}”? This replaces current edge edits and clears the route.`,
    ) &&
    versions.load(selected.value)
  ) {
    focusGraphOnClose = true;
    close();
  }
}
async function remove(): Promise<void> {
  if (!selected.value || !window.confirm(`Delete saved version “${selected.value}”?`)) return;
  if (!versions.remove(selected.value)) return;
  await nextTick();
  if (versions.names.length) savedSelect.value?.focus();
  else nameInput.value?.focus();
}
</script>
<template>
  <button
    ref="opener"
    id="versions-toggle"
    type="button"
    aria-haspopup="dialog"
    aria-controls="named-versions"
    :aria-expanded="isOpen"
    @click="open"
  >
    Versions
  </button>
  <dialog
    ref="panel"
    id="named-versions"
    class="version-panel"
    aria-labelledby="versions-title"
    @close="closed"
    @cancel.prevent="close"
    @click="dismissOutside"
  >
    <header>
      <h2 id="versions-title">Versions — {{ versions.diagramTitle }}</h2>
      <button type="button" aria-label="Close versions" @click="close">Close</button>
    </header>
    <p v-if="versions.libraryError" id="version-library-error" class="feedback" role="alert">
      {{ versions.libraryError }}
    </p>
    <p v-if="versions.error" id="version-error" class="feedback" role="alert" tabindex="0">
      {{ versions.error }}
    </p>
    <p v-else-if="versions.notice" id="version-notice" class="feedback" role="status" tabindex="0">
      {{ versions.notice }}
    </p>
    <p
      v-if="versions.saveBlockedReason && !versions.libraryError"
      id="version-save-blocked"
      class="feedback"
    >
      {{ versions.saveBlockedReason }}
    </p>
    <div class="version-body">
      <p v-if="versions.names.length" id="version-working-state" role="status">
        <strong class="version-status">{{ versions.workingStatus }}</strong
        ><span v-if="versions.matchingNames.length">: {{ versions.matchingSummary }}</span>
      </p>
      <form @submit.prevent="save">
        <label
          >Version name<input
            ref="nameInput"
            id="version-name"
            v-model="name"
            maxlength="80"
            autocomplete="off"
            :disabled="!!versions.saveBlockedReason"
            @input="versions.clearFeedback"
            autofocus
        /></label>
        <button
          id="save-version"
          type="submit"
          :disabled="!name.trim() || !!versions.saveBlockedReason"
        >
          Save new
        </button>
      </form>
      <p v-if="versions.names.length === 0 && versions.isLibraryReady" id="versions-empty">
        No saved versions yet.
      </p>
      <label v-if="versions.names.length > 0"
        >Saved version<select
          ref="savedSelect"
          id="saved-version"
          v-model="selected"
          @change="versions.clearFeedback"
        >
          <option value="" disabled>Select a saved version</option>
          <option v-for="entry in versions.names" :key="entry" :value="entry">{{ entry }}</option>
        </select></label
      >
      <div class="version-actions">
        <button
          v-if="versions.names.length > 0"
          id="load-version"
          type="button"
          :disabled="!selected"
          @click="load"
        >
          Load
        </button>
        <button
          v-if="versions.names.length > 0"
          id="delete-version"
          type="button"
          :disabled="!selected"
          @click="remove"
        >
          Delete
        </button>
        <button id="refresh-versions" type="button" @click="versions.refresh">
          {{ versions.libraryError ? "Retry reading library" : "Refresh list" }}
        </button>
      </div>
      <details>
        <summary>What is saved?</summary>
        <p>
          This browser only: colors, arrows, next-click states and start/turn settings. Later edits
          do not change saved versions.
        </p>
      </details>
    </div>
  </dialog>
</template>
<style scoped>
h2 {
  min-width: 0;
  overflow-wrap: anywhere;
}
header button {
  flex: none;
}
.version-panel {
  position: fixed;
  inset: 0;
  margin: auto;
  width: min(380px, calc(100vw - 24px));
  max-width: calc(100vw - 24px);
  max-height: calc(100dvh - 24px);
  padding: 0;
  background: var(--surface);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 6px;
  box-shadow: 0 4px 16px #0008;
}
.version-panel[open] {
  display: flex;
  flex-direction: column;
}
.version-panel::backdrop {
  background: #0006;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  flex: none;
}
.version-body {
  padding: 0 12px 12px;
  overflow: auto;
  min-height: 0;
}
form,
.version-actions {
  display: flex;
  gap: 8px;
  align-items: end;
  flex-wrap: wrap;
}
label {
  display: grid;
  gap: 4px;
  margin-bottom: 8px;
  min-width: 0;
}
input,
select {
  max-width: 100%;
  min-width: 0;
}
p {
  font-size: 12px;
  line-height: 1.4;
  margin-bottom: 8px;
  overflow-wrap: anywhere;
}
summary {
  cursor: pointer;
  margin-top: 8px;
}
#version-error {
  color: var(--red);
}
.feedback {
  flex: none;
  max-height: 25dvh;
  overflow: auto;
  margin: 0 12px 8px;
}
</style>
