<script setup lang="ts">
import { computed, ref } from "vue";
import { z } from "zod";
import { useInspection } from "./stores/inspection.js";
import { constructMorseSurface, NE20_MINIMUM_CANCELLATIONS } from "../domain/morse-surface.js";
import { DiagramDocumentSchema } from "../schemas/document.js";
import { MorseSurfaceSchema } from "../schemas/morse-surface.js";
const ReportSchema = z.discriminatedUnion("status", [
  z.strictObject({ status: z.literal("ready"), surface: MorseSurfaceSchema }),
  z.strictObject({ status: z.literal("unavailable") }),
]);
const inspection = useInspection();
const report = computed(() => {
  const document = inspection.activeDocument;
  if (document === null) return ReportSchema.parse({ status: "unavailable" });
  try {
    return ReportSchema.parse({
      status: "ready",
      surface: constructMorseSurface(
        DiagramDocumentSchema.parse(document),
        document.id === "diagram.ne20" ? NE20_MINIMUM_CANCELLATIONS : [],
      ),
    });
  } catch {
    return ReportSchema.parse({ status: "unavailable" });
  }
});
const panel = ref<HTMLDialogElement | null>(null),
  opener = ref<HTMLButtonElement | null>(null),
  isOpen = ref(false);
function open(): void {
  panel.value?.showModal();
  isOpen.value = true;
}
function close(): void {
  panel.value?.close();
  isOpen.value = false;
  opener.value?.focus();
}
function outside(event: MouseEvent): void {
  if (event.target !== panel.value || panel.value === null) return;
  const box = panel.value.getBoundingClientRect();
  if (
    event.clientX < box.left ||
    event.clientX > box.right ||
    event.clientY < box.top ||
    event.clientY > box.bottom
  )
    close();
}
</script>
<template>
  <button
    ref="opener"
    id="morse-toggle"
    type="button"
    aria-haspopup="dialog"
    aria-controls="morse-surface"
    :aria-expanded="isOpen"
    @click="open"
  >
    Morse
  </button>
  <dialog
    ref="panel"
    id="morse-surface"
    aria-labelledby="morse-title"
    @cancel.prevent="close"
    @click="outside"
  >
    <header>
      <h2 id="morse-title">
        Morse surface — {{ inspection.activeDocument?.isotope?.name ?? "diagram" }}
      </h2>
      <button type="button" aria-label="Close Morse surface" @click="close">Close</button>
    </header>
    <div v-if="isOpen" class="surface-body">
      <template v-if="report.status === 'ready'">
        <dl id="morse-invariants">
          <dt>Connected components</dt>
          <dd>{{ report.surface.components.length }}</dd>
          <dt>Genus (total)</dt>
          <dd>{{ report.surface.genus }}</dd>
          <dt>Boundary circles</dt>
          <dd>{{ report.surface.boundaryCount }}</dd>
          <dt>Euler characteristic</dt>
          <dd>{{ report.surface.eulerCharacteristic }}</dd>
          <dt>Independent cycles</dt>
          <dd>{{ report.surface.firstBettiNumber }}</dd>
          <dt>Interior minima / saddles / maxima</dt>
          <dd>{{ report.surface.minima.length }} / {{ report.surface.saddles.length }} / 0</dd>
        </dl>
        <p v-if="report.surface.contractedEdges.length" id="morse-cancellations">
          Edges 8 and 9 are contracted only in this decomposition: upper-left, upper-tip and
          upper-right share one minimum. Wiring and saved versions are unchanged.
        </p>
        <p v-else>One disk per vertex and one untwisted band per edge.</p>
        <p>
          Attachments inherit the original clockwise order. Crossings without junctions stay
          separate.
        </p>
        <p v-if="report.surface.directedCycle.length" id="morse-arrow-obstruction">
          Wiring arrow cycle: {{ report.surface.directedCycle.join(" → ") }}. These arrows cannot
          all descend a single height function.
        </p>
        <p v-else>
          No directed cycle among the original wiring’s resolved arrows. This alone does not make
          them a Morse gradient.
        </p>
        <p v-if="report.surface.unresolvedArrows.length">
          Unresolved arrows: {{ report.surface.unresolvedArrows.join(", ") }}.
        </p>
        <details>
          <summary>Morse height</summary>
          <p>
            Minima lie between levels 0 and 1; saddles between 1 and 2; the boundary is level 3.
            Near a minimum use h + x² + y²; near a saddle use h − x² + y². Regular collars join
            these handle charts. This height is neither physical time nor energy.
          </p>
          <ul>
            <li v-for="point in report.surface.minima" :key="point.vertexId">
              {{ point.vertexId }}: minimum at {{ point.level.numerator }}/{{
                point.level.denominator
              }}
              <span v-if="point.sourceVertices.length > 1">
                (merged: {{ point.sourceVertices.join(", ") }})</span
              >
            </li>
          </ul>
          <ul>
            <li v-for="point in report.surface.saddles" :key="point.edgeId">
              {{ point.edgeId }}: saddle at {{ point.level.numerator }}/{{
                point.level.denominator
              }}
            </li>
          </ul>
        </details>
        <details>
          <summary>Boundary cycles and attachments</summary>
          <section v-for="(component, index) in report.surface.components" :key="index">
            <h3>Component {{ index + 1 }}: genus {{ component.genus }}</h3>
            <ol>
              <li v-for="(cycle, i) in component.boundaries" :key="i">
                {{ cycle.length ? cycle.join(" → ") : "Isolated vertex disk" }}
              </li>
            </ol>
          </section>
          <p>
            Each endpoint is a half-edge. A boundary walk crosses to the opposite endpoint, then
            takes the next clockwise half-edge.
          </p>
          <ul>
            <li v-for="rotation in report.surface.rotations" :key="rotation.vertexId">
              {{ rotation.vertexId }}: {{ rotation.darts.join(" → ") }}
            </li>
          </ul>
        </details>
        <p class="scope">
          Combinatorial surface and Morse handle data—not a rendered 3D mesh. Genus depends on this
          attachment convention. Colored routing remains unchanged and is not identified with
          gradient flow.
        </p>
      </template>
      <p v-else role="alert">
        Surface construction unavailable. Geometry must have distinct, nonzero outgoing tangents,
        and requested contractions must form a forest. Ambiguous attachments are not guessed.
      </p>
    </div>
  </dialog>
</template>
<style scoped>
dialog {
  position: fixed;
  inset: 0;
  margin: auto;
  width: min(600px, calc(100vw - 24px));
  max-width: calc(100vw - 24px);
  max-height: calc(100dvh - 24px);
  padding: 0;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--surface);
  color: var(--ink);
}
dialog[open] {
  display: flex;
  flex-direction: column;
}
dialog::backdrop {
  background: #0006;
}
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 14px;
  flex: none;
}
header button {
  flex: none;
}
.surface-body {
  padding: 0 14px 14px;
  overflow: auto;
  min-height: 0;
}
dl {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 4px 16px;
  margin: 0 0 12px;
}
dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
}
p {
  margin: 10px 0;
}
summary {
  cursor: pointer;
  padding: 6px 0;
}
li {
  overflow-wrap: anywhere;
  margin: 4px 0;
}
.scope {
  font-size: 12px;
  color: var(--muted);
}
</style>
