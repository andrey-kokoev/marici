import { computed, readonly, shallowRef, watch } from "vue";
import { defineStore } from "pinia";
import { z } from "zod";
import { type ScreenPoint } from "../../schemas/inspection.js";
import { useInspection } from "./inspection.js";

const CameraStateSchema = z.strictObject({
  zoom: z.number().min(0.25).max(8),
  offsetX: z.number().finite(),
  offsetY: z.number().finite(),
  moveMode: z.boolean(),
});
export const useCamera = defineStore("camera", () => {
  const inspection = useInspection();
  const current = shallowRef(
    CameraStateSchema.parse({ zoom: 1, offsetX: 0, offsetY: 0, moveMode: false }),
  );
  const viewBox = computed(() => {
    const box = inspection.activeDocument?.layout.viewBox;
    if (box === undefined) return undefined;
    const width = box.width / current.value.zoom,
      height = box.height / current.value.zoom;
    return `${box.x + (box.width - width) / 2 + current.value.offsetX} ${box.y + (box.height - height) / 2 + current.value.offsetY} ${width} ${height}`;
  });
  function fit(): void {
    current.value = { ...current.value, zoom: 1, offsetX: 0, offsetY: 0 };
  }
  function zoomBy(factor: number, anchor?: ScreenPoint): void {
    const box = inspection.activeDocument?.layout.viewBox;
    if (box === undefined || !Number.isFinite(factor) || factor <= 0) return;
    const zoom = Math.min(8, Math.max(0.25, current.value.zoom * factor));
    const ratio = current.value.zoom / zoom;
    const baseX = box.x + box.width / 2,
      baseY = box.y + box.height / 2;
    const centerX = baseX + current.value.offsetX,
      centerY = baseY + current.value.offsetY;
    const x = anchor?.x ?? centerX,
      y = anchor?.y ?? centerY;
    const next = CameraStateSchema.safeParse({
      ...current.value,
      zoom,
      offsetX: x + (centerX - x) * ratio - baseX,
      offsetY: y + (centerY - y) * ratio - baseY,
    });
    if (next.success) current.value = next.data;
  }
  function panBy(x: number, y: number): void {
    const next = CameraStateSchema.safeParse({
      ...current.value,
      offsetX: current.value.offsetX + x,
      offsetY: current.value.offsetY + y,
    });
    if (next.success) current.value = next.data;
  }
  function toggleMove(): void {
    current.value = { ...current.value, moveMode: !current.value.moveMode };
  }
  watch(
    () =>
      inspection.activeDocument === null
        ? null
        : JSON.stringify([inspection.activeDocument.id, inspection.activeDocument.layout.viewBox]),
    () => {
      fit();
      current.value = { ...current.value, moveMode: false };
    },
    { flush: "sync" },
  );
  return { state: readonly(current), viewBox, fit, zoomBy, panBy, toggleMove };
});
