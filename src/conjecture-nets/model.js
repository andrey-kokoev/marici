/* Shared browser/build validation. Source dispositions are never upgraded. */
export function normalizeNet(raw, source = '', title = '') {
  if (!raw || typeof raw !== 'object' || !Array.isArray(raw.conjectures)) throw Error('Expected an object with a conjectures array.');
  if (!raw.conjectures.length || raw.conjectures.length > 500) throw Error('Choose a net with 1–500 nodes.');
  const text = v => typeof v === 'string' ? v : '';
  const nodes = raw.conjectures.map(n => {
    if (!n || typeof n.id !== 'string' || !n.id || n.id.length > 300) throw Error('Every node needs a nonempty ID (up to 300 characters).');
    const dependencies = n.depends_on ?? [];
    if (!Array.isArray(dependencies) || dependencies.some(p => typeof p !== 'string')) throw Error(`Invalid dependencies: ${n.id}`);
    if (new Set(dependencies).size !== dependencies.length) throw Error(`Repeated prerequisite: ${n.id}`);
    return { id: n.id, title: text(n.title) || n.id.replaceAll('-', ' ').replaceAll('_', ' '), status: text(n.status) || 'unspecified', kind: text(n.kind) || 'conjecture', statement: text(n.statement), depends_on: [...dependencies], outcome: n.outcome ?? null, raw: n };
  });
  const by = new Map(nodes.map(n => [n.id, n]));
  if (by.size !== nodes.length) throw Error('Duplicate node IDs.');
  for (const n of nodes) for (const p of n.depends_on) if (!by.has(p)) throw Error(`Missing prerequisite ${p} in ${n.id}`);
  const active = new Set(), levels = new Map();
  function level(id) {
    if (active.has(id)) throw Error(`Dependency cycle at ${id}`);
    if (levels.has(id)) return levels.get(id);
    active.add(id);
    const value = Math.max(-1, ...by.get(id).depends_on.map(level)) + 1;
    active.delete(id); levels.set(id, value); return value;
  }
  for (const n of nodes) n.level = level(n.id);
  const frontier = Array.isArray(raw.frontier) ? raw.frontier : [];
  if (frontier.some(id => !by.has(id))) throw Error('Frontier references a missing node.');
  return { id: text(raw.id) || text(raw.schema) || 'local-net', title: title || text(raw.title) || text(raw.id) || 'Local net', source, nodes, frontier, raw };
}

export function repositoryPath(value) {
  return typeof value === 'string' && /^(research|docs|src)\/[A-Za-z0-9_./ ()+@-]+$/.test(value) && !value.split('/').some(s => s === '..' || s === '.') && !value.includes('//');
}

export function sourceURL(value, local = false) {
  if (!repositoryPath(value)) return null;
  const encoded = value.split('/').map(encodeURIComponent).join('/');
  return local ? '../../../' + encoded : 'https://github.com/andrey-kokoev/marici/blob/main/' + encoded;
}
