<script setup lang="ts">
import { computed } from "vue";
import { useCatalog } from "./stores/catalog.js";
import { useInspection } from "./stores/inspection.js";
import { projectDiagram } from "../presentation/diagram.js";
import { DiagramDocumentSchema } from "../schemas/document.js";
import DiagramGlyphs from "./DiagramGlyphs.vue";
const catalog = useCatalog(),
  inspection = useInspection();
const references = computed(() =>
  catalog.state.references.map((document) => ({
    document,
    projection: projectDiagram(DiagramDocumentSchema.parse(document)),
  })),
);
</script>
<template>
  <section v-if="references.length" class="references" aria-label="Pinned graph references">
    <article v-for="reference in references" :key="reference.document.id" class="reference-card">
      <header>
        <h2>{{ reference.document.isotope?.name }}</h2>
        <button
          :aria-label="`Unpin ${reference.document.isotope?.name} reference`"
          @click="catalog.unpin(reference.document.id)"
        >
          ×
        </button>
      </header>
      <p v-if="catalog.state.showCounts">
        {{ reference.document.isotope?.protons }} P · {{ reference.document.isotope?.neutrons }} N
      </p>
      <svg
        :viewBox="reference.projection.viewBox"
        :aria-label="`${reference.document.isotope?.name} reference diagram`"
        role="img"
      >
        <DiagramGlyphs
          :projection="reference.projection"
          :namespace="`reference-${reference.document.id}`"
          :show-labels="inspection.state.showEdgeLabels"
          :interactive="false"
        />
      </svg>
    </article>
  </section>
</template>
<style scoped>
.references {
  display: flex;
  flex: 1;
  min-width: 260px;
}
.reference-card {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 260px;
  border-left: 1px solid var(--line);
  padding: 16px;
}
.reference-card header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.reference-card p {
  font-size: 11px;
  color: var(--muted);
}
svg {
  flex: 1;
  width: 100%;
  min-height: 240px;
}
</style>
