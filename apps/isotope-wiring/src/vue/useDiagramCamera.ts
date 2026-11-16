import { onScopeDispose, ref, watch } from "vue";
import { useCamera } from "./stores/camera.js";

/** Screen measurements affect presentation only, never incidence or traversal. */
export function useDiagramCamera() {
  const camera = useCamera(),
    dragging = ref(false);
  let pointer: number | null = null,
    captured: SVGSVGElement | null = null,
    lastX = 0,
    lastY = 0,
    suppressClick = false;
  function endDrag(): void {
    const target = captured,
      id = pointer;
    captured = null;
    pointer = null;
    dragging.value = false;
    if (target !== null && id !== null && target.hasPointerCapture(id))
      target.releasePointerCapture(id);
  }
  watch(() => camera.state.moveMode, endDrag, { flush: "sync" });
  onScopeDispose(endDrag);
  function pointerDown(event: PointerEvent): void {
    if (!camera.state.moveMode) {
      suppressClick = false;
      return;
    }
    if (
      !camera.state.moveMode ||
      event.button !== 0 ||
      pointer !== null ||
      !(event.currentTarget instanceof SVGSVGElement)
    )
      return;
    event.preventDefault();
    event.currentTarget.setPointerCapture(event.pointerId);
    captured = event.currentTarget;
    suppressClick = true;
    pointer = event.pointerId;
    lastX = event.clientX;
    lastY = event.clientY;
    dragging.value = true;
  }
  function pointerMove(event: PointerEvent): void {
    if (
      event.pointerId !== pointer ||
      !camera.state.moveMode ||
      !(event.currentTarget instanceof SVGSVGElement)
    )
      return;
    const matrix = event.currentTarget.getScreenCTM();
    if (matrix === null || matrix.a === 0 || matrix.d === 0) return;
    camera.panBy(-(event.clientX - lastX) / matrix.a, -(event.clientY - lastY) / matrix.d);
    lastX = event.clientX;
    lastY = event.clientY;
  }
  function pointerUp(event: PointerEvent): void {
    if (event.pointerId !== pointer) return;
    endDrag();
  }
  function wheel(event: WheelEvent): void {
    if (!(event.currentTarget instanceof SVGSVGElement)) return;
    const matrix = event.currentTarget.getScreenCTM();
    if (matrix === null) return;
    const anchor = new DOMPoint(event.clientX, event.clientY).matrixTransform(matrix.inverse());
    const unit =
      event.deltaMode === WheelEvent.DOM_DELTA_LINE
        ? 16
        : event.deltaMode === WheelEvent.DOM_DELTA_PAGE
          ? event.currentTarget.clientHeight
          : 1;
    camera.zoomBy(Math.pow(2, (-event.deltaY * unit) / 400), { x: anchor.x, y: anchor.y });
  }
  function keydown(event: KeyboardEvent): void {
    if (event.ctrlKey || event.metaKey || event.altKey || event.isComposing) return;
    if (event.key === "+" || event.key === "=") {
      event.preventDefault();
      camera.zoomBy(1.25);
    } else if (event.key === "-") {
      event.preventDefault();
      camera.zoomBy(0.8);
    } else if (event.key.toLowerCase() === "f") {
      event.preventDefault();
      camera.fit();
    } else if (event.key === "Escape" && camera.state.moveMode) {
      event.preventDefault();
      camera.toggleMove();
    } else if (
      camera.state.moveMode &&
      ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(event.key)
    ) {
      event.preventDefault();
      const step = 20 / camera.state.zoom;
      camera.panBy(
        event.key === "ArrowLeft" ? -step : event.key === "ArrowRight" ? step : 0,
        event.key === "ArrowUp" ? -step : event.key === "ArrowDown" ? step : 0,
      );
    }
  }
  function click(event: MouseEvent): void {
    if (camera.state.moveMode || suppressClick) {
      event.preventDefault();
      event.stopPropagation();
      suppressClick = false;
    }
  }
  return { camera, dragging, pointerDown, pointerMove, pointerUp, endDrag, wheel, keydown, click };
}
