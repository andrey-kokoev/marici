import * as THREE from 'three';
import { TrackballControls } from 'three/addons/controls/TrackballControls.js';

export function createPlanesViewer({ host, onFailure }) {
  const lifetime = new AbortController();
  const owned = new Set();
  const own = resource => { owned.add(resource); return resource; };
  const listen = (target, event, fn) => target.addEventListener(event, fn, { signal: lifetime.signal });
  const fallback = host.querySelector('#fallback');
  let renderer, controls, resizeObserver, intersectionObserver, densityQuery;
  let disposed = false, frame = 0, interacting = false, inView = true, pending, rebuilds = 0;
  const scene = new THREE.Scene();
  const objects = new THREE.Group(); scene.add(objects);
  const camera = new THREE.OrthographicCamera(-7, 7, 7, -7, 0.1, 200);
  camera.position.set(5, 4, 7);
  const diskMaterial = new THREE.MeshBasicMaterial({ color: 0xf4c430, transparent: true,
    opacity: 0.2, side: THREE.DoubleSide, depthWrite: false });
  function clearObjects() { objects.clear(); for (const resource of owned) resource.dispose(); owned.clear(); }
  function stop() { cancelAnimationFrame(frame); frame = 0; }
  function requestRender() { if (!disposed && !frame && !document.hidden && inView) frame = requestAnimationFrame(render); }
  function dispose() {
    if (disposed) return;
    disposed = true; stop(); lifetime.abort();
    resizeObserver?.disconnect(); intersectionObserver?.disconnect();
    densityQuery?.removeEventListener('change', densityChanged);
    controls?.removeEventListener('change', requestRender);
    controls?.removeEventListener('start', start); controls?.removeEventListener('end', end);
    controls?.dispose(); clearObjects(); diskMaterial.dispose();
    renderer?.dispose(); renderer?.domElement.remove(); fallback.hidden = false;
  }
  function fail(error) { dispose(); onFailure(error); }
  function lines(points, color) {
    const object = new THREE.LineSegments(own(new THREE.BufferGeometry().setFromPoints(points)),
      own(new THREE.LineBasicMaterial({ color, depthTest: false })));
    object.renderOrder = 4; return object;
  }
  function rebuild(packet) {
    clearObjects(); rebuilds++;
    const circle = own(new THREE.CircleGeometry(packet.radius, 96));
    const z = new THREE.Vector3(0, 0, 1);
    for (const plane of packet.planes) {
      const disk = new THREE.Mesh(circle, diskMaterial);
      disk.quaternion.setFromUnitVectors(z, plane.normal);
      disk.position.copy(plane.normal).multiplyScalar(plane.offset);
      disk.renderOrder = 1; objects.add(disk);
    }
    if (packet.segments.length) objects.add(lines(packet.segments, 0xffd86b));
    if (packet.solid && packet.region.faces.length) {
      const triangles = [];
      for (const face of packet.region.faces) for (let i = 1; i < face.points.length - 1; i++) {
        triangles.push(...face.points[0].toArray(), ...face.points[i].toArray(), ...face.points[i + 1].toArray());
      }
      const geometry = own(new THREE.BufferGeometry());
      geometry.setAttribute('position', new THREE.Float32BufferAttribute(triangles, 3));
      const solid = new THREE.Mesh(geometry, own(new THREE.MeshBasicMaterial({ color: 0xffe1a0,
        transparent: true, opacity: 0.13, side: THREE.DoubleSide, depthWrite: false })));
      solid.renderOrder = 3; objects.add(solid);
    }
    if (packet.edges) {
      const edges = [], seen = new Set();
      for (const face of packet.region.faces) face.points.forEach((a, i) => {
        const b = face.points[(i + 1) % face.points.length];
        const key = [packet.region.vertices.indexOf(a), packet.region.vertices.indexOf(b)].sort((a, b) => a - b).join(':');
        if (!seen.has(key)) { seen.add(key); edges.push(a, b); }
      });
      if (edges.length) objects.add(lines(edges, 0xffffff));
      const sphere = own(new THREE.SphereGeometry(0.035, 10, 8));
      const material = own(new THREE.MeshBasicMaterial({ color: 0xffffff, depthTest: false }));
      for (const vertex of packet.region.vertices) {
        const dot = new THREE.Mesh(sphere, material); dot.position.copy(vertex); dot.renderOrder = 5; objects.add(dot);
      }
    }
  }
  function render() {
    frame = 0;
    if (disposed || document.hidden || !inView) return;
    try {
      if (pending) { const packet = pending; pending = null; rebuild(packet); }
      controls.update(); renderer.render(scene, camera);
      if (interacting) requestRender();
    } catch (error) { fail(error); }
  }
  function start() { interacting = true; requestRender(); }
  function end() { interacting = false; requestRender(); }
  let width = 0, height = 0, ratio = 0;
  function resize() {
    if (disposed) return;
    const size = host.getBoundingClientRect(), dpr = Math.min(devicePixelRatio || 1, 2);
    if (size.width <= 0 || size.height <= 0 || (size.width === width && size.height === height && dpr === ratio)) return;
    width = size.width; height = size.height; ratio = dpr;
    renderer.setPixelRatio(ratio); renderer.setSize(width, height, false);
    const aspect = width / height;
    camera.left = -7 * aspect; camera.right = 7 * aspect; camera.top = 7; camera.bottom = -7;
    camera.updateProjectionMatrix(); controls.handleResize(); requestRender();
  }
  function densityChanged() {
    densityQuery?.removeEventListener('change', densityChanged);
    densityQuery = matchMedia(`(resolution: ${devicePixelRatio}dppx)`);
    densityQuery.addEventListener('change', densityChanged);
    resize();
  }
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setClearColor(0x0b1120); renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.domElement.setAttribute('role', 'img');
    renderer.domElement.setAttribute('aria-label', 'Four tetrahedrally arranged disks. Camera controls are available in the adjacent panel.');
    renderer.domElement.setAttribute('aria-describedby', 'instructions');
    host.append(renderer.domElement);
    controls = new TrackballControls(camera, renderer.domElement);
    controls.rotateSpeed = 3; controls.staticMoving = true; // Free roll, no idle damping loop.
    controls.minZoom = 0.15; controls.maxZoom = 15;
    controls.update();
    controls.addEventListener('change', requestRender); controls.addEventListener('start', start); controls.addEventListener('end', end);
    listen(renderer.domElement, 'webglcontextlost', event => { event.preventDefault(); fail(new Error('3D context lost. Reload to retry.')); });
    listen(document, 'visibilitychange', () => { interacting = false; stop(); requestRender(); });
    listen(window, 'pagehide', event => { interacting = false; if (event.persisted) stop(); else dispose(); });
    listen(window, 'pageshow', event => { if (event.persisted) requestRender(); });
    listen(window, 'resize', resize);
    resizeObserver = new ResizeObserver(resize); resizeObserver.observe(host);
    intersectionObserver = new IntersectionObserver(([entry]) => {
      inView = entry.isIntersecting; if (!inView) interacting = false; stop(); requestRender();
    });
    intersectionObserver.observe(host); densityChanged();
    fallback.hidden = true;
    return Object.freeze({
      updateGeometry(packet) { if (!disposed) { pending = packet; requestRender(); } },
      setOpacity(opacity) { if (!disposed) { diskMaterial.opacity = opacity; requestRender(); } },
      rotate(axis, angle) {
        if (disposed) return;
        const direction = axis === 'roll' ? camera.position.clone().sub(controls.target).normalize()
          : new THREE.Vector3(axis === 'pitch' ? 1 : 0, axis === 'yaw' ? 1 : 0, 0).applyQuaternion(camera.quaternion).normalize();
        const q = new THREE.Quaternion().setFromAxisAngle(direction, angle);
        camera.position.sub(controls.target).applyQuaternion(q).add(controls.target);
        camera.up.applyQuaternion(q); controls.update(); requestRender();
      },
      zoom(factor) { if (!disposed) { camera.zoom = THREE.MathUtils.clamp(camera.zoom * factor, 0.15, 15); camera.updateProjectionMatrix(); requestRender(); } },
      reset() { if (!disposed) { controls.reset(); requestRender(); } },
      dispose,
      snapshot: () => ({ disposed, scheduled: Boolean(frame), rebuilds, opacity: diskMaterial.opacity,
        objects: objects.children.length, geometries: renderer.info.memory.geometries, calls: renderer.info.render.calls,
        position: camera.position.toArray(), up: camera.up.toArray(), zoom: camera.zoom }),
    });
  } catch (error) { dispose(); throw error; }
}
