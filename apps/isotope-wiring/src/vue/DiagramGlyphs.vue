<script setup lang="ts">
import { type DiagramProjection, type Selection } from "../schemas/inspection.js";
// Vue component contract; graph and selection data retain their schema-derived types.
const props = defineProps<{
  projection: DiagramProjection;
  selection?: Selection;
  namespace: string;
  showLabels: boolean;
  interactive: boolean;
  edgeHint?: (id: string) => string;
}>();
const emit = defineEmits<{ edge: [id: string]; vertex: [id: string] }>();
function edge(id: string): void {
  if (props.interactive) emit("edge", id);
}
function vertex(id: string): void {
  if (props.interactive) emit("vertex", id);
}
function arrowPath(bidirectional: boolean): string {
  return bidirectional ? "M 1 -3 L 5 0 L 1 3 M -1 -3 L -5 0 L -1 3" : "M -3 -3 L 2 0 L -3 3";
}
</script>
<template>
  <g
    v-for="item in projection.edges"
    :key="item.id"
    :id="`${namespace}-${item.id}`"
    :class="{ interactive }"
    :role="interactive ? 'button' : undefined"
    :tabindex="interactive ? 0 : undefined"
    :aria-label="
      interactive ? `${item.label}: ${edgeHint ? edgeHint(item.id) : item.id}` : undefined
    "
    @click="edge(item.id)"
    @keydown.enter="edge(item.id)"
    @keydown.space.prevent="edge(item.id)"
  >
    <title>
      {{ item.id }} · {{ item.direction }}{{ edgeHint ? " · " + edgeHint(item.id) : "" }}
    </title>
    <polyline
      :points="item.points"
      fill="none"
      :stroke="`var(--${item.color})`"
      :stroke-width="selection?.kind === 'edge' && selection.edgeId === item.id ? 4 : 2"
    />
    <template v-if="item.arrowAngle !== null">
      <path
        class="direction-arrow-halo"
        :transform="`translate(${item.midpoint.x} ${item.midpoint.y}) rotate(${item.arrowAngle})`"
        :d="arrowPath(item.direction === 'both')"
        fill="none"
        stroke="var(--surface)"
        stroke-width="3"
        stroke-linecap="round"
        stroke-linejoin="round"
        pointer-events="none"
        aria-hidden="true"
      />
      <path
        class="direction-arrow"
        :transform="`translate(${item.midpoint.x} ${item.midpoint.y}) rotate(${item.arrowAngle})`"
        :d="arrowPath(item.direction === 'both')"
        fill="none"
        :stroke="`var(--${item.color})`"
        stroke-width="1"
        stroke-linecap="round"
        stroke-linejoin="round"
        pointer-events="none"
      />
    </template>
    <polyline
      v-if="interactive"
      :points="item.points"
      fill="none"
      stroke="transparent"
      stroke-width="12"
    />
  </g>
  <circle
    v-for="item in projection.vertices"
    :key="item.id"
    :id="`${namespace}-${item.id}`"
    :cx="item.point.x"
    :cy="item.point.y"
    :r="selection?.kind === 'vertex' && selection.vertexId === item.id ? 6 : 4"
    :class="{ interactive }"
    :role="interactive ? 'button' : undefined"
    :tabindex="interactive ? 0 : undefined"
    :aria-label="interactive ? item.id : undefined"
    @click="vertex(item.id)"
    @keydown.enter="vertex(item.id)"
    @keydown.space.prevent="vertex(item.id)"
    ><title>{{ item.id }}</title></circle
  >
  <!-- Paint every label after geometry so crossing strokes cannot hide it. -->
  <template v-if="showLabels">
    <text
      v-for="item in projection.edges"
      :key="`label-${item.id}`"
      :id="`${namespace}-label-${item.id}`"
      :class="{ interactive }"
      :x="item.labelPoint.x"
      :y="item.labelPoint.y"
      text-anchor="middle"
      @click="edge(item.id)"
      >{{ item.label }}</text
    >
  </template>
</template>
<style scoped>
text {
  font: 9px sans-serif;
  fill: var(--ink);
  paint-order: stroke;
  stroke: var(--surface);
  stroke-width: 2px;
}
circle {
  fill: var(--green);
}
.interactive {
  cursor: pointer;
}
</style>
