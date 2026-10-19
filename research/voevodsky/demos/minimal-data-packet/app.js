import { names, sectors3, counts, pointOnPath, previewSvg, project, tetrahedralPoint } from './model.mjs';
import { createScene } from './scene.js';

const $ = id => document.getElementById(id);
const sectors = sectors3();
const state = { selected: '2:1:1', mode: 'compare', only: false, fills: true, signed: true, frameGuide: true, progress: 0, playing: false };
const configs = [
  { prefix: '', host: 'scene', fallback: 'fallback', status: 'scene-status', frame: 'lattice', dataset: 'view', transform: p => p },
  { prefix: 'tetra-', host: 'tetra-scene', fallback: 'tetra-fallback', status: 'tetra-status', frame: 'tetrahedral', dataset: 'tetraView', transform: tetrahedralPoint },
].map(c => ({ ...c, view: null, visible: true }));
const selected = () => sectors.find(s => s.id === state.selected);
const paths = () => state.mode === 'compare' ? selected().routes : [selected().boundary];

for (const c of configs) {
  for (const s of sectors) $(c.prefix + 'sector').add(new Option(s.title, s.id));
}
function updateCounts() {
  const c = counts(Number($('dimension').value));
  $('dimension-value').value = String(c.n);
  $('dimension-summary').textContent = `${c.n} choices of omitted direction × 2^${c.n - 1} signed-side assignments = ${c.sectors.toLocaleString()} dependency sectors of dimension ${c.cellDimension}. ${c.n} outgoing directions give ${c.encounters.toLocaleString()} candidate sector–direction encounters.`;
  $('count-products').textContent = `n = ${c.n}: ${c.encounters.toLocaleString()} × ${c.n} + ${c.encounters.toLocaleString()} × ${c.sectors.toLocaleString()} + ${c.encounters.toLocaleString()} × ${c.encounters.toLocaleString()} = ${c.terms.map(x => x.toLocaleString()).join(' + ')} = ${c.total.toLocaleString()}.`;
}
function renderFallback(c) {
  if (c.view) return;
  const draw = p => project(c.transform(p));
  let svg = previewSvg(state.selected, state.only, state.fills, c.frame, state.frameGuide);
  const overlay = paths().map((p, i) => {
    const color = i ? '#ffc179' : '#78d6e8';
    const points = p.map(v => draw(v).join(',')).join(' ');
    const [x, y] = draw(pointOnPath(p, state.progress));
    return `<polyline points="${points}" stroke="${color}" stroke-width="4" fill="none"/><circle cx="${x}" cy="${y}" r="6" fill="${color}"/>`;
  }).join('');
  svg = svg.replace('</svg>', overlay + '</svg>');
  $(c.fallback).src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}
function updateProgress() {
  for (const c of configs) {
    $(c.prefix + 'progress').value = state.progress;
    $(c.prefix + 'progress-value').value = `${Math.round(state.progress * 100)}%`;
    c.view?.move(state.progress); renderFallback(c);
  }
}
function update() {
  const s = selected();
  for (const c of configs) {
    $(c.prefix + 'sector').value = s.id;
    $(c.prefix + 'path-mode').value = state.mode;
    for (const [id, key] of [['only-selected', 'only'], ['fills', 'fills'], ['signed', 'signed']]) $(c.prefix + id).checked = state[key];
    const corner = c.transform(s.corner).map(x => Number(x.toFixed(3)));
    $(c.prefix + 'sector-summary').textContent = `Omit ${names[s.omitted]}; retain ${s.labels[0]} and ${s.labels[1]}. ${c.frame === 'tetrahedral' ? 'The oblique-frame corner' : 'The common corner'} is (${corner.join(', ')}).`;
    $(c.prefix + 'route-detail').replaceChildren();
    const lines = state.mode === 'compare'
      ? [`l → ${s.labels[0]} → common corner`, `l → ${s.labels[1]} → common corner`]
      : [`l → ${s.labels[0]} → common corner`, `→ ${s.labels[1]} → l`];
    lines.forEach((text, i) => {
      const row = document.createElement('div'); row.className = `route-${i ? 'b' : 'a'}`; row.textContent = text; $(c.prefix + 'route-detail').append(row);
    });
    $(c.prefix + 'signed').disabled = !c.view;
    $(c.prefix + 'reset-view').disabled = !c.view;
    c.view?.update(state, paths());
  }
  $('tetra-guide').checked = state.frameGuide;
  updateProgress();
}
function setPlaying(playing) {
  state.playing = playing;
  for (const c of configs) {
    $(c.prefix + 'play').textContent = c.prefix ? `${playing ? 'Pause' : 'Play'} tetrahedral paths` : `${playing ? 'Pause' : 'Play'} paths`;
    $(c.prefix + 'play').setAttribute('aria-pressed', String(playing));
  }
}
for (const c of configs) {
  $(c.prefix + 'sector').addEventListener('change', e => { state.selected = e.target.value; state.progress = 0; update(); });
  $(c.prefix + 'path-mode').addEventListener('change', e => { state.mode = e.target.value; state.progress = 0; update(); });
  for (const [id, key] of [['only-selected', 'only'], ['fills', 'fills'], ['signed', 'signed']]) {
    $(c.prefix + id).addEventListener('change', e => { state[key] = e.target.checked; update(); });
  }
  $(c.prefix + 'progress').addEventListener('input', e => { state.progress = Number(e.target.value); setPlaying(false); updateProgress(); });
  $(c.prefix + 'play').addEventListener('click', () => { if (state.progress === 1) state.progress = 0; setPlaying(!state.playing); });
  $(c.prefix + 'reset-view').addEventListener('click', () => c.view?.reset());
}
$('tetra-guide').addEventListener('change', e => { state.frameGuide = e.target.checked; update(); });
$('dimension').addEventListener('input', updateCounts);
updateCounts(); update();

for (const c of configs) {
  try {
    c.view = createScene({ host: $(c.host), sectors, transform: c.transform, frame: c.frame,
      onSelect: id => { state.selected = id; state.progress = 0; update(); } });
    $(c.fallback).hidden = true; $(c.status).hidden = true;
    document.documentElement.dataset[c.dataset] = 'webgl';
  } catch (error) {
    $(c.host).querySelectorAll('canvas').forEach(canvas => canvas.remove());
    $(c.status).textContent = `3D view unavailable. The interactive SVG and discussion remain available. ${error.message}`;
    document.documentElement.dataset[c.dataset] = 'svg';
  }
  new IntersectionObserver(entries => { c.visible = entries[0].isIntersecting; }).observe($(c.host));
}
update();
let previous = performance.now();
function frame(now) {
  const dt = Math.min((now - previous) / 1000, 0.05); previous = now;
  if (!document.hidden) {
    if (state.playing) {
      state.progress = Math.min(1, state.progress + dt / 4);
      if (state.progress === 1) setPlaying(false);
      updateProgress();
    }
    for (const c of configs) if (c.visible) c.view?.render();
  }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
// Keep the independent electron trial's data/load failure isolated from both frames.
import('./electron.js').then(module => module.mountElectronView()).catch(error => {
  document.documentElement.dataset.electronView = 'error';
  $('electron-status').textContent = `Electron source view unavailable: ${error.message}. The discussion and static diagram remain available.`;
});

// Read-only display observability; no scientific verdict.
globalThis.PacketView = { snapshot: () => ({ ...state, sectorCount: sectors.length,
  dimension: counts(Number($('dimension').value)), view: document.documentElement.dataset.view,
  tetraView: document.documentElement.dataset.tetraView,
  frames: Object.fromEntries(configs.map(c => [c.frame, c.view?.stats() || null])) }) };
