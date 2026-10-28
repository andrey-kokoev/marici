import { computed, reactive } from 'vue';
import { basePlanes, repeatPlanes, computePolyhedron, intersectionSegments } from './geometry.js';

export function usePlanesModel() {
  const state = reactive({ opacity: 0.2, distance: 0.67, repeats: 1, radius: 2.5,
    intersections: true, edges: false, solid: true });
  const planes = computed(() => basePlanes(state.distance));
  const region = computed(() => computePolyhedron(planes.value));
  const repeated = computed(() => repeatPlanes(planes.value, state.repeats));
  const segments = computed(() => state.intersections ? intersectionSegments(repeated.value, state.radius) : []);
  const volume = computed(() => 8 * Math.sqrt(3) * state.distance ** 3);
  const summary = computed(() => state.distance === 0
    ? `Intersection collapsed to a point · 0 volume · ${repeated.value.length} disks`
    : `${region.value.vertices.length} vertices · ${region.value.faces.length} faces · ${repeated.value.length} disks · 4 half-spaces`);
  // Opacity is deliberately excluded: material changes must not rebuild geometry.
  const geometry = computed(() => ({ planes: repeated.value, region: region.value, radius: state.radius,
    segments: segments.value, edges: state.edges, solid: state.solid }));
  return { state, planes, region, repeated, segments, volume, summary, geometry };
}
