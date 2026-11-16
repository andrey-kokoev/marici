// Imperative rendering boundary. No Vue proxies or DOM panel state belong here.
import { palette } from './palette.js';
import { createSpanLayer } from './spanLayer.js';
function loadScript(relative, signal) {
  return new Promise((resolve, reject) => {
    signal.throwIfAborted();
    const script = document.createElement('script');
    const finish = error => {
      script.onload = script.onerror = null;
      signal.removeEventListener('abort', abort);
      if (error) { script.remove(); reject(error); } else resolve();
    };
    const abort = () => finish(new DOMException('Viewer stopped', 'AbortError'));
    script.src = new URL(relative, document.baseURI).href;
    script.onload = () => finish();
    script.onerror = () => finish(new Error(`Failed to load ${relative}`));
    signal.addEventListener('abort', abort, { once: true });
    document.head.append(script);
  });
}

export async function createViewer({ host, signal, onFailure }) {
  // The existing legacy pair is deliberately retained in this UI migration.
  await loadScript('./vendor/three.min.js', signal);
  signal.throwIfAborted();
  await loadScript('./vendor/OrbitControls.js', signal);
  signal.throwIfAborted();
  const THREE = globalThis.THREE;
  if (!THREE?.OrbitControls) throw new Error('Local Three.js dependencies unavailable');
  const lifetime = new AbortController();
  const resources = new Set();
  const track = resource => { resources.add(resource); return resource; };
  const listen = (target, event, callback) => target.addEventListener(event, callback, { signal: lifetime.signal });
  let renderer, controls, scene, camera, span, resizeObserver, intersectionObserver;
  let disposed = false, frame = 0, inView = true;
  const fallback = host.querySelector('#fallback');
  function stopFrame() { cancelAnimationFrame(frame); frame = 0; }
  function requestRender() {
    if (!disposed && !frame && !document.hidden && inView) frame = requestAnimationFrame(render);
  }
  function render() {
    frame = 0;
    if (disposed || document.hidden || !inView) return;
    try {
      renderer.render(scene, camera);
    } catch (error) { fail(error); }
  }
  function dispose() {
    if (disposed) return;
    disposed = true;
    stopFrame(); lifetime.abort(); signal.removeEventListener('abort', dispose);
    resizeObserver?.disconnect(); intersectionObserver?.disconnect();
    controls?.removeEventListener('change', requestRender); controls?.dispose();
    for (const resource of resources) resource.dispose();
    resources.clear(); renderer?.dispose(); renderer?.domElement.remove();
    fallback.removeAttribute('hidden');
  }
  function fail(error) { dispose(); onFailure(error); }
  signal.addEventListener('abort', dispose, { once: true });
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setClearColor(palette.background);
    renderer.domElement.setAttribute('role', 'img');
    renderer.domElement.setAttribute('aria-label', 'Outer simplicial shell of ESD7: a subdivided tetrahedral boundary with 196 triangles. Adjacent controls provide camera navigation.');
    renderer.domElement.setAttribute('aria-describedby', 'instructions');
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(40, 1, 0.1, 50);
    camera.position.set(8, 6, 10);
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = false; controls.enablePan = false;
    controls.minDistance = 3; controls.maxDistance = 60;
    controls.update(); controls.saveState();
    span = createSpanLayer(THREE, scene, track);
    host.append(renderer.domElement);
    listen(renderer.domElement, 'webglcontextlost', event => {
      event.preventDefault(); fail(new Error('3D context lost. Reload to retry.'));
    });
    // Three.EventDispatcher is not a DOM EventTarget: explicit removal in dispose.
    controls.addEventListener('change', requestRender);
    listen(document, 'visibilitychange', () => { stopFrame(); requestRender(); });
    listen(window, 'pagehide', event => { if (event.persisted) stopFrame(); else dispose(); });
    listen(window, 'pageshow', event => { if (event.persisted) requestRender(); });
    let lastWidth = 0, lastHeight = 0, lastRatio = 0;
    const resize = () => {
      const { width, height } = host.getBoundingClientRect();
      const ratio = Math.min(devicePixelRatio || 1, 2);
      if (disposed || width <= 0 || height <= 0) return;
      if (width === lastWidth && height === lastHeight && ratio === lastRatio) return;
      lastWidth = width; lastHeight = height; lastRatio = ratio;
      renderer.setPixelRatio(ratio); renderer.setSize(width, height, false);
      camera.aspect = width / height; camera.updateProjectionMatrix(); requestRender();
    };
    resizeObserver = new ResizeObserver(resize); resizeObserver.observe(host);
    listen(window, 'resize', resize);
    intersectionObserver = new IntersectionObserver(([entry]) => { inView = entry.isIntersecting; stopFrame(); requestRender(); });
    intersectionObserver.observe(host);
    resize(); fallback.setAttribute('hidden', ''); requestRender();
    return Object.freeze({
      update(state) {
        if (disposed) return;
        span.update(state);requestRender();
      },
      orbit(azimuth, elevation = 0) {
        if (disposed) return;
        const offset = camera.position.clone().sub(controls.target);
        const spherical = new THREE.Spherical().setFromVector3(offset);
        spherical.theta += azimuth; spherical.phi += elevation; spherical.makeSafe();
        camera.position.copy(controls.target).add(offset.setFromSpherical(spherical));
        controls.update(); requestRender();
      },
      zoom(factor) {
        if (disposed) return;
        const offset = camera.position.clone().sub(controls.target).multiplyScalar(factor).clampLength(3, 60);
        camera.position.copy(controls.target).add(offset); controls.update(); requestRender();
      },
      reset() { if (!disposed) { controls.reset(); requestRender(); } },
      dispose,
      snapshot: () => ({ disposed, scheduled: Boolean(frame), ...span.snapshot(),
        azimuth: controls.getAzimuthalAngle(), elevation: controls.getPolarAngle(),
        distance: camera.position.distanceTo(controls.target), calls: renderer.info.render.calls }),
    });
  } catch (error) { dispose(); throw error; }
}
