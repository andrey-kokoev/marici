// One renderer implementation, used by both coordinate frames.
import { names, pointOnPath } from './model.mjs';

export function createScene({ host, sectors, transform = p => p, frame = 'lattice', onSelect }) {
  const THREE = globalThis.THREE;
  if (!THREE?.OrbitControls) throw new Error('Local Three.js dependencies are unavailable.');
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setClearColor(0x101827);
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.domElement.setAttribute('aria-label', frame === 'tetrahedral'
    ? 'Orbitable tetrahedral frame with twelve selectable rhombi and the common center l. Use the sector selector for keyboard access.'
    : 'Orbitable three-sheet configuration complex with twelve selectable square sectors. Use the sector selector for keyboard access.');
  renderer.domElement.setAttribute('role', 'img');
  host.prepend(renderer.domElement);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(40, 1, 0.01, 60);
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.minDistance = 3; controls.maxDistance = 12;
  const V = p => new THREE.Vector3(...transform(p));
  const colors = [0xc59bff, 0xffc179, 0x78d6e8];
  function line(points, color, opacity = 1, dashed = false) {
    const material = dashed ? new THREE.LineDashedMaterial({ color, transparent: true, opacity, dashSize: 0.045, gapSize: 0.035 })
      : new THREE.LineBasicMaterial({ color, transparent: opacity < 1, opacity });
    const object = new THREE.Line(new THREE.BufferGeometry().setFromPoints(points.map(V)), material);
    if (dashed) object.computeLineDistances();
    return object;
  }
  function dot(point, color, size = 0.045) {
    const mesh = new THREE.Mesh(new THREE.SphereGeometry(size, 16, 10), new THREE.MeshBasicMaterial({ color })); mesh.position.copy(V(point)); return mesh;
  }
  function text(value, point, color = '#edf3fa', size = 0.28) {
    const canvas = document.createElement('canvas'); canvas.width = 256; canvas.height = 96;
    const ctx = canvas.getContext('2d'); ctx.font = '600 45px system-ui'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillStyle = color; ctx.fillText(value, 128, 48);
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(canvas), depthTest: false, depthWrite: false }));
    sprite.position.copy(V(point)); sprite.scale.set(0.75 * size / 0.28, size, 1); return sprite;
  }
  function arrow(points, color, group) {
    for (let j = 0; j < points.length - 1; j++) {
      const start = V(points[j]), delta = V(points[j + 1]).sub(start);
      group.add(new THREE.ArrowHelper(delta.clone().normalize(), start, delta.length(), color, 0.10, 0.055));
    }
  }
  const faces = sectors.map(s => {
    const vertices = s.boundary.slice(0, 4);
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.Float32BufferAttribute([0, 1, 2, 0, 2, 3].flatMap(i => transform(vertices[i])), 3));
    geometry.computeVertexNormals();
    const material = new THREE.MeshBasicMaterial({ color: colors[s.omitted], side: THREE.DoubleSide, transparent: true, opacity: 0.12, depthWrite: false });
    const mesh = new THREE.Mesh(geometry, material); mesh.userData.sector = s.id;
    const border = line(s.boundary, colors[s.omitted], 0.45);
    const group = new THREE.Group(); group.add(mesh, border); scene.add(group);
    return { s, mesh, border, group };
  });
  const negatives = new THREE.Group(); scene.add(negatives);
  for (let axis = 0; axis < 3; axis++) {
    const positive = [0, 0, 0], negative = [0, 0, 0]; positive[axis] = 1; negative[axis] = -1;
    arrow([[0, 0, 0], positive], 0xdcebf8, scene);
    scene.add(dot(positive, 0xe9f2ff));
    const p = [...positive]; p[axis] = 1.24; scene.add(text(names[axis], p));
    negatives.add(line([[0, 0, 0], negative], 0x73839b, 0.7), dot(negative, 0x8c9cb3, 0.035));
    const m = [...negative]; m[axis] = -1.24; negatives.add(text('−' + names[axis], m, '#a6b6ce'));
  }
  const mark = text('l', [0.22, 0.22, 0.14], '#ffe4a0', 0.42);
  // A readable world-space offset from the unchanged center, not a new coordinate.
  if (frame === 'tetrahedral') mark.position.set(0.16, 0.19, 0.12);
  scene.add(dot([0, 0, 0], 0xffe4a0, 0.075), mark);
  const guide = new THREE.Group(); scene.add(guide);
  if (frame === 'tetrahedral') {
    const vertices = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]];
    for (let i = 0; i < 4; i++) for (let j = i + 1; j < 4; j++) guide.add(line([vertices[i], vertices[j]], 0x9daec6, 0.65, true));
    guide.add(dot(vertices[3], 0xaab8ca), text('d', [-1.18, -1.18, -1.18], '#b8cada'));
  }
  let routeGroup = null, markers = [], mode = 'compare', pickable = true;
  function dispose(group) {
    group.traverse(o => { o.geometry?.dispose(); const materials = Array.isArray(o.material) ? o.material : [o.material]; for (const m of materials) { m?.map?.dispose(); m?.dispose(); } });
  }
  const view = {
    update(state, paths) {
      mode = state.mode; pickable = state.fills;
      for (const f of faces) {
        const chosen = f.s.id === state.selected;
        f.group.visible = !state.only || chosen;
        f.mesh.visible = state.fills;
        f.mesh.material.opacity = chosen ? 0.32 : 0.10;
        f.mesh.material.color.set(chosen ? 0xffe4a0 : colors[f.s.omitted]);
        f.border.material.opacity = chosen ? 0.95 : 0.38;
      }
      negatives.visible = state.signed;
      guide.visible = frame === 'tetrahedral' && state.frameGuide;
      if (routeGroup) { scene.remove(routeGroup); dispose(routeGroup); }
      routeGroup = new THREE.Group(); markers = [];
      paths.forEach((points, i) => {
        const color = mode === 'return' ? 0x9bf0bd : i ? 0xffc179 : 0x78d6e8;
        arrow(points, color, routeGroup);
        const marker = dot(points[0], color, 0.057); markers.push({ marker, points }); routeGroup.add(marker);
      });
      scene.add(routeGroup); view.move(state.progress);
    },
    move(progress) { for (const { marker, points } of markers) marker.position.copy(V(pointOnPath(points, progress))); },
    reset() {
      // Avoid looking almost straight down the first tetrahedral ray.
      if (frame === 'tetrahedral') camera.position.set(4.2, 1.8, 0.9);
      else camera.position.set(3.1, 2.3, 3.8);
      controls.target.set(0, 0, 0); controls.update();
    },
    render() { controls.update(); renderer.render(scene, camera); },
    stats() { return { frame, sectors: faces.length, visibleSectors: faces.filter(f => f.group.visible).length,
      guideVisible: guide.visible, mode, markerPositions: markers.map(({ marker }) => marker.position.toArray()) }; },
  };
  const resize = new ResizeObserver(() => {
    const { width, height } = host.getBoundingClientRect();
    camera.aspect = width / height; camera.updateProjectionMatrix(); renderer.setSize(width, height);
  });
  resize.observe(host); view.reset();
  const ray = new THREE.Raycaster(), pointer = new THREE.Vector2(); let down = null;
  renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
  renderer.domElement.addEventListener('pointerup', e => {
    if (!pickable || !down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) { down = null; return; }
    const bounds = renderer.domElement.getBoundingClientRect();
    pointer.set(2 * (e.clientX - bounds.left) / bounds.width - 1, 1 - 2 * (e.clientY - bounds.top) / bounds.height);
    ray.setFromCamera(pointer, camera);
    const hit = ray.intersectObjects(faces.filter(f => f.group.visible && f.mesh.visible).map(f => f.mesh))[0];
    if (hit) onSelect(hit.object.userData.sector);
    down = null;
  });
  return view;
}
