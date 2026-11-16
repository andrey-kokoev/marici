// Imperative rendering boundary. No Vue proxies or DOM panel state belong here.
import { palette } from './palette.js';
import { createFieldLayer } from './fieldLayer.js';
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

export async function createViewer({ host, signal, onFailure, onParticlePlaced = () => {} }) {
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
  let renderer, controls, scene, camera, field, resizeObserver, intersectionObserver;
  let disposed = false, frame = 0, running = false, inView = true, previousTime = 0, draws = 0;
  const fallback = host.querySelector('#fallback');
  function stopFrame() { cancelAnimationFrame(frame); frame = 0; previousTime = 0; }
  function requestRender() {
    if (!disposed && !frame && !document.hidden && inView) frame = requestAnimationFrame(render);
  }
  function render(time) {
    frame = 0;
    if (disposed || document.hidden || !inView) return;
    try {
      if (running) field.advance(Math.min(previousTime ? (time - previousTime) / 1000 : 0, 0.05));
      previousTime = time;
      renderer.render(scene, camera);draws++;
      if (running) requestRender();
    } catch (error) { fail(error); }
  }
  function dispose() {
    if (disposed) return;
    disposed = true; running = false;
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
    renderer.domElement.setAttribute('aria-label', 'Three.js planar attraction field with momentum particles. A is at minus three, zero; B at three, zero. Side panel provides camera and simulation controls.');
    renderer.domElement.setAttribute('aria-describedby', 'instructions');
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
    camera.position.set(0, 0, 28);
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = false; controls.enablePan = false;
    controls.minDistance = 6; controls.maxDistance = 60;
    controls.update(); controls.saveState();
    field = createFieldLayer(THREE, scene, track);
    host.append(renderer.domElement);
    const raycaster = new THREE.Raycaster(), pointer = new THREE.Vector2();
    const plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0), hit = new THREE.Vector3();
    let press = null;
    listen(renderer.domElement, 'pointerdown', event => {
      if (!event.isPrimary) { press = null; return; }
      if (event.button === 0) press = { id: event.pointerId, x: event.clientX, y: event.clientY, moved: false };
    });
    listen(renderer.domElement, 'pointermove', event => {
      if (press && event.pointerId === press.id && Math.hypot(event.clientX - press.x, event.clientY - press.y) > 5) press.moved = true;
    });
    listen(renderer.domElement, 'pointercancel', () => { press = null; });
    listen(renderer.domElement, 'pointerup', event => {
      const click = press; press = null;
      if (!click || click.id !== event.pointerId || click.moved || event.button !== 0) return;
      const rect = renderer.domElement.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) return;
      pointer.set(2 * (event.clientX - rect.left) / rect.width - 1, 1 - 2 * (event.clientY - rect.top) / rect.height);
      raycaster.setFromCamera(pointer, camera);
      if (raycaster.ray.intersectPlane(plane, hit)) {
        field.place(hit.x, hit.y); onParticlePlaced(); stopFrame(); requestRender();
      }
    });
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
        field.update(state);
        if (running !== state.running) { running = state.running; stopFrame(); }
        requestRender();
      },
      resetParticles() { if (!disposed) { field.reset(); stopFrame(); requestRender(); } },
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
        const offset = camera.position.clone().sub(controls.target).multiplyScalar(factor).clampLength(6, 60);
        camera.position.copy(controls.target).add(offset); controls.update(); requestRender();
      },
      reset() { if (!disposed) { controls.reset(); requestRender(); } },
      dispose,
      snapshot: () => ({ disposed, running, scheduled: Boolean(frame), draws, ...field.snapshot(),
        azimuth: controls.getAzimuthalAngle(), elevation: controls.getPolarAngle(),
        distance: camera.position.distanceTo(controls.target), calls: renderer.info.render.calls }),
    });
  } catch (error) { dispose(); throw error; }
}
