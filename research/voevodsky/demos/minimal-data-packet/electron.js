import { loadFixture, stateAt, bloch, gauge, relativePhase, preparedSpinor, sourceBlocks, decodeBlocks,
  distance, norm2, scale, localDirections, formatComplex, electronSvg } from './electron-model.mjs';

const $ = id => document.getElementById(id);
const radians = degrees => degrees * Math.PI / 180;
export async function mountElectronView() {
  const responses = await Promise.all(['electron-trial.json', 'electron-native-store.json'].map(file => fetch(new URL(file, import.meta.url))));
  if (responses.some(response => !response.ok)) throw new Error('The recorded electron fixture is unavailable.');
  const [trial, store] = await Promise.all(responses.map(response => response.json()));
  const fixture = loadFixture(trial, store);
  const state = { initial: fixture.initial.map(z => [...z]), progress: 0, playing: false, erased: false };
  let view = null, visible = true;
  const rows = fixture.projectors.map((_, i) => {
    const row = document.createElement('tr');
    const name = document.createElement('th'); name.scope = 'row'; name.textContent = String(i + 1);
    const amplitudes = document.createElement('td'), weight = document.createElement('td');
    row.append(name, amplitudes, weight); $('electron-blocks').append(row);
    return { amplitudes, weight };
  });
  function syncPreparation() {
    const [a, b] = state.initial;
    $('electron-theta').value = (2 * Math.acos(Math.min(1, Math.sqrt(norm2(a)))) * 180 / Math.PI).toFixed(2);
    const alphaPhase = Math.atan2(a[1], a[0]), betaPhase = Math.atan2(b[1], b[0]);
    $('electron-phi').value = ((betaPhase - alphaPhase) * 180 / Math.PI + 360) % 360;
    $('electron-initial-phase').value = (alphaPhase * 180 / Math.PI + 360) % 360;
  }
  function setPlaying(playing) {
    state.playing = playing;
    $('electron-play').textContent = playing ? 'Pause spinor loop' : 'Play spinor loop';
    $('electron-play').setAttribute('aria-pressed', String(playing));
  }
  function update() {
    const z = stateAt(fixture, state.initial, state.progress), r = bloch(z), phase = gauge(z);
    const blocks = sourceBlocks(fixture, z), recovered = decodeBlocks(fixture, blocks);
    const returned = relativePhase(state.initial, z);
    $('electron-progress').value = state.progress;
    $('electron-progress-value').value = `${state.progress.toFixed(2)} / 4`;
    $('electron-theta-value').value = `${Number($('electron-theta').value).toFixed(2)}°`;
    $('electron-phi-value').value = `${Number($('electron-phi').value).toFixed(2)}°`;
    $('electron-initial-phase-value').value = `${Number($('electron-initial-phase').value).toFixed(2)}°`;
    const completed = Math.floor(state.progress + 1e-10);
    $('electron-word').textContent = completed === 4 ? 'U → V → U inverse → V inverse · source loop complete'
      : `Completed ${completed} source steps; next: ${fixture.labels[completed]}. Between steps, the interpolation is supplied illustration.`;
    $('electron-spinor').textContent = `α = ${formatComplex(z[0])}; β = ${formatComplex(z[1])}`;
    $('electron-ray').textContent = `Ray coordinates: (${r.map(x => Number(x.toFixed(4))).join(', ')}).`;
    $('electron-phase-readout').textContent = `${phase.index ? 'β' : 'α'} chart: local phase ${(phase.angle * 180 / Math.PI).toFixed(1)}°. ${returned === null ? 'The ray has not returned to its initial point.' : `The ray has returned; relative amplitude phase ${(returned * 180 / Math.PI).toFixed(1)}°.`}`;
    $('electron-sign').textContent = distance(z, state.initial.map(x => scale(-1, x))) < 1e-9
      ? 'Same ray; opposite retained spinor sign.' : distance(z, state.initial) < 1e-9
        ? 'Same ray and same retained spinor.' : 'Transporting the ray and its retained lift.';
    $('electron-erased-readout').hidden = !state.erased;
    $('electron-erased-readout').textContent = `Ray-only chart representative: (${phase.canonical.map(formatComplex).join('; ')}). At the completed loop this agrees with the initial ray-only representative, erasing the source sign.`;
    $('electron-pairing').textContent = `With fixed reference p=(1,0), B(p,z)=β=${formatComplex(z[1])}. This is a signed amplitude, not an isolated-state probability.`;
    $('electron-decoder').textContent = `Native face-block recovery error: ${distance(z, recovered).toExponential(1)} (numerical display).`;
    rows.forEach(({ amplitudes, weight }, i) => {
      amplitudes.textContent = blocks[i].map(formatComplex).join('; ');
      weight.textContent = blocks[i].reduce((sum, x) => sum + norm2(x), 0).toFixed(4);
    });
    $('electron-next').disabled = state.progress >= 4;
    if (view) view.update(z, phase, state.erased);
    else $('electron-fallback').src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(electronSvg(fixture, state.initial, state.progress, state.erased));
  }
  $('electron-progress').addEventListener('input', e => { setPlaying(false); state.progress = Number(e.target.value); update(); });
  $('electron-play').addEventListener('click', () => { if (state.progress >= 4) state.progress = 0; setPlaying(!state.playing); update(); });
  $('electron-next').addEventListener('click', () => { setPlaying(false); state.progress = Math.min(4, Math.floor(state.progress) + 1); update(); });
  $('electron-restart').addEventListener('click', () => { setPlaying(false); state.progress = 0; update(); });
  $('electron-erase').addEventListener('change', e => { state.erased = e.target.checked; update(); });
  for (const id of ['electron-theta', 'electron-phi', 'electron-initial-phase']) $(id).addEventListener('input', () => {
    setPlaying(false); state.progress = 0;
    state.initial = preparedSpinor(...['electron-theta', 'electron-phi', 'electron-initial-phase'].map(key => radians(Number($(key).value))));
    view?.prepare(state.initial); update();
  });
  $('electron-default').addEventListener('click', () => {
    setPlaying(false); state.initial = fixture.initial.map(z => [...z]); state.progress = 0;
    syncPreparation(); view?.prepare(state.initial); update();
  });
  $('electron-reset-view').addEventListener('click', () => view?.reset());
  syncPreparation();
  try {
    view = createElectronScene(fixture);
    $('electron-fallback').hidden = true; $('electron-status').hidden = true;
    document.documentElement.dataset.electronView = 'webgl';
  } catch (error) {
    $('electron-scene').querySelectorAll('canvas').forEach(canvas => canvas.remove());
    $('electron-status').textContent = `3D view unavailable. The source-bound readouts and SVG remain interactive. ${error.message}`;
    document.documentElement.dataset.electronView = 'svg';
  }
  $('electron-controls').disabled = false;
  $('electron-reset-view').disabled = !view;
  $('electron-evidence').textContent = `Recorded exact trial: ${Object.keys(trial.checks).length} passing checks; native producer replay: ${trial.native_replay.isolated_replay_check_count} checks. The browser displays numerical evaluations of that fixture.`;
  update();
  new IntersectionObserver(entries => { visible = entries[0].isIntersecting; }).observe($('electron-scene'));
  let previous = performance.now();
  function frame(now) {
    const dt = Math.min((now - previous) / 1000, 0.05); previous = now;
    if (!document.hidden) {
      if (state.playing) {
        state.progress = Math.min(4, state.progress + dt / 1.5);
        if (state.progress === 4) setPlaying(false);
        update();
      }
      if (visible) view?.render();
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  globalThis.ElectronPacket = { snapshot: () => {
    const z = stateAt(fixture, state.initial, state.progress), phase = gauge(z);
    return { initial: state.initial, spinor: z, ray: bloch(z), initialRay: bloch(state.initial), progress: state.progress,
      erased: state.erased, canonical: phase.canonical, relativePhase: relativePhase(state.initial, z),
      decoderError: distance(z, decodeBlocks(fixture, sourceBlocks(fixture, z))),
      sourceSteps: fixture.labels, view: document.documentElement.dataset.electronView };
  } };
}

function createElectronScene(fixture) {
  const THREE = globalThis.THREE;
  if (!THREE?.OrbitControls) throw new Error('Local Three.js dependencies are unavailable.');
  const host = $('electron-scene'), renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setClearColor(0x101827); renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.domElement.setAttribute('role', 'img');
  renderer.domElement.setAttribute('aria-label', 'Spin-ray sphere with two local signed directions beside the retained phase circle. The source loop returns to the same ray with the opposite spinor sign.');
  host.prepend(renderer.domElement);
  const scene = new THREE.Scene(), camera = new THREE.PerspectiveCamera(40, 1, 0.01, 80);
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.minDistance = 4; controls.maxDistance = 20;
  const left = new THREE.Vector3(-1.65, 0, 0), right = new THREE.Vector3(1.65, 0, 0);
  const position = p => new THREE.Vector3(...p).add(left);
  function line(points, color, opacity = 1) {
    return new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), new THREE.LineBasicMaterial({ color, transparent: true, opacity }));
  }
  function dot(point, color, radius = 0.055) {
    const o = new THREE.Mesh(new THREE.SphereGeometry(radius, 16, 10), new THREE.MeshBasicMaterial({ color })); o.position.copy(point); return o;
  }
  function text(value, point, color = '#edf3fa', size = 0.24) {
    const canvas = document.createElement('canvas'); canvas.width = 640; canvas.height = 96;
    const ctx = canvas.getContext('2d'); ctx.font = '500 42px system-ui'; ctx.fillStyle = color; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(value, 320, 48);
    const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(canvas), depthTest: false, depthWrite: false }));
    s.position.copy(point); s.scale.set(size * 640 / 96, size, 1); return s;
  }
  const sphere = new THREE.Mesh(new THREE.SphereGeometry(1, 28, 18), new THREE.MeshBasicMaterial({ color: 0x6689ab, transparent: true, opacity: 0.14, wireframe: true }));
  sphere.position.copy(left); scene.add(sphere);
  scene.add(text('two-direction ray base', left.clone().add(new THREE.Vector3(0, 1.55, 0))), text('retained local phase', right.clone().add(new THREE.Vector3(0, 1.55, 0))));
  const circle = Array.from({ length: 65 }, (_, i) => right.clone().add(new THREE.Vector3(0.85 * Math.cos(2 * Math.PI * i / 64), 0.85 * Math.sin(2 * Math.PI * i / 64), 0)));
  scene.add(line(circle, 0x6986a3), dot(right, 0xffe4a0, 0.035));
  scene.add(text('+1', right.clone().add(new THREE.Vector3(1.04, 0, 0)), '#b8cada', 0.19), text('−1', right.clone().add(new THREE.Vector3(-1.04, 0, 0)), '#b8cada', 0.19));
  const phaseArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), right, 0.85, 0x9bf0bd, 0.13, 0.07);
  const erasedArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), right, 0.75, 0xa8b2c2, 0.10, 0.05);
  const rayArrow = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), left, 1, 0x78d6e8, 0.12, 0.06);
  const marker = dot(left, 0x78d6e8);
  scene.add(phaseArrow, erasedArrow, rayArrow, marker);
  let prepared = null;
  function dispose(group) { group.traverse(o => { o.geometry?.dispose(); o.material?.map?.dispose(); o.material?.dispose(); }); }
  const view = {
    prepare(initial) {
      if (prepared) { scene.remove(prepared); dispose(prepared); }
      prepared = new THREE.Group();
      const r = bloch(initial), mark = position(r), directions = localDirections(r);
      prepared.add(dot(mark, 0xffe4a0, 0.075), text('l', mark.clone().add(new THREE.Vector3(0.10, 0.17, 0)), '#ffe4a0', 0.30));
      directions.forEach((v, i) => {
        const color = i ? 0xffc179 : 0x78d6e8;
        for (const sign of [-1, 1]) {
          const d = new THREE.Vector3(...v).multiplyScalar(sign);
          prepared.add(new THREE.ArrowHelper(d, mark, 0.40, color, sign > 0 ? 0.08 : 0.045, 0.04));
        }
        const endpoint = mark.clone().addScaledVector(new THREE.Vector3(...v), 0.54);
        prepared.add(text(i ? 'v' : 'u', endpoint, i ? '#ffc179' : '#78d6e8', 0.22));
      });
      const trajectory = Array.from({ length: 161 }, (_, i) => position(bloch(stateAt(fixture, initial, i / 40))));
      prepared.add(line(trajectory, 0x78d6e8, 0.45)); scene.add(prepared);
    },
    update(z, phase, erased) {
      const r = new THREE.Vector3(...bloch(z));
      marker.position.copy(r).add(left); rayArrow.setDirection(r);
      phaseArrow.setDirection(new THREE.Vector3(Math.cos(phase.angle), Math.sin(phase.angle), 0));
      erasedArrow.visible = erased;
    },
    reset() {
      const distance = Math.max(8, 3.1 / (Math.tan(Math.PI / 9) * camera.aspect));
      camera.position.set(0.65, distance * 0.18, distance); controls.target.set(0, 0, 0); controls.update();
    },
    render() { controls.update(); renderer.render(scene, camera); },
  };
  const resize = new ResizeObserver(() => {
    const { width, height } = host.getBoundingClientRect();
    camera.aspect = width / height; camera.updateProjectionMatrix(); renderer.setSize(width, height); view.reset();
  });
  resize.observe(host); view.prepare(fixture.initial); view.reset(); return view;
}
