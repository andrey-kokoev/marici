// Geometry/counting model only; no scientific recovery or filler is asserted.
export const names = ['a', 'b', 'c'];
export const origin = [0, 0, 0];
// Three unit vertex rays of a regular tetrahedron; the fourth is minus their sum.
export const tetrahedralBasis = [[1, 1, 1], [1, -1, -1], [-1, 1, -1]].map(v => v.map(x => x / Math.sqrt(3)));
export function tetrahedralPoint(point) {
  return [0, 1, 2].map(j => point.reduce((sum, x, i) => sum + x * tetrahedralBasis[i][j], 0));
}
export function counts(n) {
  if (!Number.isInteger(n) || n < 1 || n > 12) throw new RangeError('Choose an integer dimension from 1 to 12.');
  const sectors = n * 2 ** (n - 1);
  const encounters = n * sectors;
  const terms = [encounters * n, encounters * sectors, encounters * encounters];
  return { n, cellDimension: n - 1, sectors, encounters, terms, total: terms.reduce((a, b) => a + b, 0) };
}
function axisPoint(axis, sign) {
  const p = [...origin]; p[axis] = sign; return p;
}
export function sectors3() {
  const result = [];
  for (let omitted = 0; omitted < 3; omitted++) {
    const axes = [0, 1, 2].filter(i => i !== omitted);
    for (const u of [-1, 1]) for (const v of [-1, 1]) {
      const first = axisPoint(axes[0], u), second = axisPoint(axes[1], v);
      const corner = first.map((x, i) => x + second[i]);
      const signed = (axis, sign) => `${sign > 0 ? '+' : '−'}${names[axis]}`;
      const labels = [signed(axes[0], u), signed(axes[1], v)];
      result.push({ id: `${omitted}:${u}:${v}`, omitted, axes, signs: [u, v], labels,
        title: `${labels.join(' / ')} · omit ${names[omitted]}`,
        boundary: [[...origin], first, corner, second, [...origin]],
        routes: [[[...origin], first, corner], [[...origin], second, corner]],
        corner,
      });
    }
  }
  return result;
}
export function pointOnPath(points, progress) {
  const t = Math.max(0, Math.min(1, progress)) * (points.length - 1);
  const index = Math.min(points.length - 2, Math.floor(t));
  const f = t - index;
  return points[index].map((x, i) => x + (points[index + 1][i] - x) * f);
}
export function project([x, y, z]) {
  return [330 + 115 * (x - z), 220 + 62 * (x + z) - 125 * y];
}
export function previewSvg(selectedId = null, onlySelected = false, fills = true, frame = 'lattice', showGuide = true) {
  const transform = frame === 'tetrahedral' ? tetrahedralPoint : p => p;
  const draw = p => project(transform(p));
  const colors = ['#c59bff', '#ffc179', '#78d6e8'];
  const faces = sectors3().filter(s => !onlySelected || s.id === selectedId).map(s => `<polygon data-sector="${s.id}" points="${s.boundary.slice(0, 4).map(p => draw(p).join(',')).join(' ')}" fill="${s.id === selectedId ? '#ffe4a0' : colors[s.omitted]}" fill-opacity="${fills ? '.18' : '0'}" stroke="${s.id === selectedId ? '#ffe4a0' : colors[s.omitted]}" stroke-width="2"/>`).join('');
  const axes = names.map((name, i) => { const p = [0, 0, 0]; p[i] = 1; const [x, y] = draw(p); p[i] = 1.24; const [tx, ty] = draw(p); return `<path d="M330 220L${x} ${y}" stroke="#eff5ff" stroke-width="3"/><circle cx="${x}" cy="${y}" r="4" fill="#eff5ff"/><text x="${tx + 8}" y="${ty - 5}">${name}</text>`; }).join('');
  let guide = '';
  if (frame === 'tetrahedral' && showGuide) {
    const vertices = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]];
    for (let i = 0; i < 4; i++) for (let j = i + 1; j < 4; j++) {
      const a = draw(vertices[i]), b = draw(vertices[j]);
      guide += `<path d="M${a.join(' ')}L${b.join(' ')}" stroke="#8d9fb9" stroke-dasharray="5 5" fill="none"/>`;
    }
    const d = draw(vertices[3]); guide += `<text x="${d[0] + 8}" y="${d[1] + 8}" fill="#b8cada">d</text>`;
  }
  const description = frame === 'tetrahedral' ? 'Twelve rhombi in a tetrahedral frame; the fourth vertex ray is derived.' : 'Three coordinate sheets with four signed sectors each meet at the label l.';
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 460" role="img" aria-labelledby="title desc"><title id="title">A marked packet and twelve coherence sectors</title><desc id="desc">${description} These are configuration directions, not physical spatial axes.</desc><rect width="660" height="460" rx="16" fill="#101827"/><g font-family="system-ui,sans-serif" fill="#edf3fa" font-size="20">${guide}${faces}${axes}<circle cx="330" cy="220" r="8" fill="#ffe4a0"/><text x="340" y="245">l</text><text x="24" y="35" font-size="16">one mark · three directions · twelve signed sectors</text><text x="24" y="435" font-size="14" fill="#b8cada">Proposed configuration-space primitive · n = 3</text></g></svg>\n`;
}
