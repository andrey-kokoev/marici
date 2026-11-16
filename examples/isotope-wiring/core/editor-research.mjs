import { importLegacyAbsolute } from './legacy-adapter.mjs';
import { canonicalJSON } from './attributed-diagrams.mjs';
import { createModelChecker } from './model-evaluation.mjs';

// Live UI checks use the same predicate evaluator as Node, without archival hashes.
const { verifyModel } = createModelChecker();
const cache = new Map();
export function inspectDefinition(source) {
  const key = canonicalJSON(source);
  if (cache.has(key)) return cache.get(key);
  let result;
  try {
    const packet = importLegacyAbsolute(source), d = packet.object.diagram;
    const report = verifyModel(packet.object, packet.modelContext);
    const supportCells = new Map(), cellSupports = new Map(d.sets.cell.map(c => [c, new Set()]));
    const add = (cell, edge) => {
      const support = d.maps.edgeSupport[edge];
      if (!supportCells.has(support)) supportCells.set(support, new Set());
      supportCells.get(support).add(cell); cellSupports.get(cell).add(support);
    };
    for (const p of d.sets.pair) for (const color of ['red', 'blue']) add(d.maps.pairCell[p], d.maps[`${color}Edge`][p]);
    for (const w of d.sets.lineWitness) add(d.maps.lineCell[w], d.maps.lineEdge[w]);
    const affectedCells = issue => {
      if (issue.sort === 'cell') return [issue.id];
      if (issue.sort === 'pair') return [d.maps.pairCell[issue.id]];
      if (issue.sort === 'lineWitness') return [d.maps.lineCell[issue.id]];
      if (issue.sort === 'port') return [d.maps.portCell[issue.id]];
      if (issue.sort === 'support') return [...(supportCells.get(issue.id) || [])];
      const shell = issue.sort === 'shell' ? issue.id : issue.sort === 'boundaryWitness' ? d.maps.boundaryWitnessShell[issue.id] : null;
      return shell ? d.sets.cell.filter(c => d.maps.cellShell[c] === shell) : [];
    };
    result = {
      status: report.status, scope: report.scope,
      counts: { cells: d.sets.cell.length, vertices: d.sets.vertex.length, supports: d.sets.support.length },
      checks: report.checks.map(check => ({ ...check, issues: check.issues.map(issue => ({ ...issue, cells: affectedCells(issue).filter(Boolean) })) })),
      cells: Object.fromEntries(d.sets.cell.map(cell => {
        const supports = cellSupports.get(cell);
        const neighbors = new Set([...supports].flatMap(s => [...supportCells.get(s)]).filter(c => c !== cell));
        const ports = d.sets.port.filter(p => d.maps.portCell[p] === cell).map(p => ({
          role: packet.object.labels.port[p].role, lattice: packet.object.labels.vertex[d.maps.portVertex[p]].lattice,
        }));
        return [cell, { ports, supportCount: supports.size, neighbors: [...neighbors].sort() }];
      })),
    };
  } catch (error) {
    result = { status: 'invalid', error: error.message, checks: [], cells: {} };
  }
  // UI callers cannot mutate cached checks, and cache growth is bounded.
  if (cache.size >= 4) cache.delete(cache.keys().next().value);
  const freeze = value => { if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); } return value; };
  cache.set(key, freeze(result)); return result;
}

export function compareDefinitions(base, target) {
  const changes = [];
  for (const collection of ['shells', 'cells', 'pairs', 'witnesses']) {
    const a = new Map(base.graph[collection].map(r => [r.id, r])), b = new Map(target.graph[collection].map(r => [r.id, r]));
    for (const id of new Set([...a.keys(), ...b.keys()])) {
      const before = a.get(id), after = b.get(id);
      if (before && after && canonicalJSON(before) === canonicalJSON(after)) continue;
      const cells = new Set();
      for (const record of [before, after].filter(Boolean)) {
        if (collection === 'cells') cells.add(record.id);
        else if (record.cell) cells.add(record.cell);
        else if (collection === 'shells' || record.shell) {
          const shell = collection === 'shells' ? record.id : record.shell;
          for (const cell of [...base.graph.cells, ...target.graph.cells]) if (cell.shell === shell) cells.add(cell.id);
        }
      }
      changes.push({ collection, id, change: !before ? 'added' : !after ? 'removed' : 'changed', before, after, cells: [...cells] });
    }
  }
  const metadata = [];
  for (const key of new Set([...Object.keys(base), ...Object.keys(target)])) {
    if (key === 'graph' || canonicalJSON(base[key]) === canonicalJSON(target[key])) continue;
    metadata.push({ key, before: base[key], after: target[key] });
  }
  return { base: base.id, target: target.id, changes, metadata };
}

// Bounded, deterministic survey of one record's same-shell destinations. No ranking
// or physical inference: each row is exactly the corresponding single-trial check.
export function surveyPlacements(source, kind, recordId, { offset = 0, limit = 8 } = {}) {
  if (!['pairs', 'witnesses'].includes(kind)) throw Error('Choose pairs or witnesses.');
  if (!Number.isSafeInteger(offset) || offset < 0 || !Number.isSafeInteger(limit) || limit < 1 || limit > 8) throw Error('Survey pages require a nonnegative offset and a limit from 1 to 8.');
  const packet = importLegacyAbsolute(source), doc = packet.retainedSource;
  const record = doc.graph[kind].find(r => r.id === recordId);
  if (!record || (kind === 'witnesses' && record.kind !== 'line')) throw Error('Choose an existing cell-owned record.');
  const destinations = doc.graph.cells.filter(c => c.shell === record.shell && c.id !== record.cell).map(c => c.id).sort();
  if (offset > destinations.length) throw Error('Survey offset exceeds the destination count.');
  const action = kind === 'pairs' ? trialPairPlacement : trialWitnessPlacement;
  const rows = destinations.slice(offset, offset + limit).map(cell => {
    const { report } = action(doc, recordId, cell);
    return { cell, status: report.status, inventoryStatus: report.checks.find(c => c.predicate === 'inventory-targets')?.status ?? 'notApplicable', error: report.error ?? null,
      findings: report.checks.filter(c => c.status !== 'verified').map(c => ({ predicate: c.predicate, status: c.status,
        codes: [...new Set(c.issues.map(i => i.code))] })) };
  });
  const nextOffset = offset + rows.length;
  return { kind, recordId, sourceCell: record.cell, shell: record.shell, sourceStatus: inspectDefinition(doc).status,
    total: destinations.length, offset, nextOffset, complete: nextOffset === destinations.length, rows,
    scope: 'Only single-record, same-shell relocations with fixed routes/axis and supplied targets; not a physical uniqueness test.' };
}

// A line witness has cell ownership; a boundary witness does not and is not relocated.
export function trialWitnessPlacement(source, witnessId, destinationId) {
  const packet = importLegacyAbsolute(source), candidate = JSON.parse(JSON.stringify(packet.retainedSource));
  const witness = candidate.graph.witnesses.find(w => w.id === witnessId);
  const destination = candidate.graph.cells.find(c => c.id === destinationId);
  if (!witness || witness.kind !== 'line') throw Error('Choose an existing neutron line witness; boundary witnesses are shell-owned.');
  if (!destination) throw Error('Choose an existing destination cell.');
  if (destination.shell !== witness.shell) throw Error('Placement trials stay within the same shell.');
  if (destination.id === witness.cell) throw Error('Choose a different cell.');
  if (!Array.isArray(witness.history)) throw Error('The witness history must be an array.');
  if (candidate.placementQuestions !== undefined && !Array.isArray(candidate.placementQuestions)) throw Error('Placement questions must be an array.');
  if (candidate.editHistory !== undefined && !Array.isArray(candidate.editHistory)) throw Error('Edit history must be an array.');
  const from = witness.cell;
  witness.cell = destination.id;
  witness.history.push(`placement trial: ${from} -> ${destination.id}`);
  candidate.status = 'unresolved';
  candidate.name = `${source.name} — witness placement trial`;
  candidate.notes = `Trial placement of ${witness.id} (${witness.axis} neutron witness): ${from} → ${destination.id}. Supplied counts are unchanged; placement remains unresolved.`;
  candidate.placementAlternative = { sourceDefinitionId: source.id, witnessId, fromCell: from, toCell: destination.id, sourceNote: source.notes ?? null };
  const questionId = 'trial-witness-placement:' + witnessId;
  candidate.placementQuestions = [...(candidate.placementQuestions || []).filter(q => q?.id !== questionId),
    { id: questionId, witnessIds: [witnessId], reason: 'This trial neutron-witness location has not been established; equal inventories do not select a placement.' }];
  candidate.editHistory = [...(candidate.editHistory || []), { action: `Trial relocation of neutron witness ${witnessId} from ${from} to ${destination.id}` }];
  return { definition: candidate, report: inspectDefinition(candidate), difference: compareDefinitions(source, candidate) };
}

// A bounded placement experiment: one owned EP moves inside its existing shell.
// This conserves supplied targets and inventory; passing predicates does not choose a placement.
export function trialPairPlacement(source, pairId, destinationId) {
  const packet = importLegacyAbsolute(source), candidate = JSON.parse(JSON.stringify(packet.retainedSource));
  const pair = candidate.graph.pairs.find(p => p.id === pairId);
  const destination = candidate.graph.cells.find(c => c.id === destinationId);
  if (!pair) throw Error('Choose an existing EP record.');
  if (!destination) throw Error('Choose an existing destination cell.');
  if (destination.shell !== pair.shell) throw Error('Placement trials stay within the same shell.');
  if (destination.id === pair.cell) throw Error('Choose a different cell.');
  if (!Array.isArray(pair.history)) throw Error('The EP history must be an array.');
  if (candidate.placementQuestions !== undefined && !Array.isArray(candidate.placementQuestions)) throw Error('Placement questions must be an array.');
  if (candidate.editHistory !== undefined && !Array.isArray(candidate.editHistory)) throw Error('Edit history must be an array.');
  const from = pair.cell;
  pair.cell = destination.id;
  pair.history.push(`placement trial: ${from} -> ${destination.id}`);
  candidate.status = 'unresolved';
  candidate.name = `${source.name} — placement trial`;
  candidate.notes = `Trial placement of ${pair.id}: ${from} → ${destination.id}. Supplied counts are unchanged; placement remains unresolved.`;
  candidate.placementAlternative = { sourceDefinitionId: source.id, pairId, fromCell: from, toCell: destination.id, sourceNote: source.notes ?? null };
  const questionId = 'trial-placement:' + pairId;
  candidate.placementQuestions = [...(candidate.placementQuestions || []).filter(q => q?.id !== questionId),
    { id: questionId, pairIds: [pairId], reason: 'This trial location has not been established; equal inventories do not select a placement.' }];
  candidate.editHistory = [...(candidate.editHistory || []), { action: `Trial relocation of ${pairId} from ${from} to ${destination.id}` }];
  return { definition: candidate, report: inspectDefinition(candidate), difference: compareDefinitions(source, candidate) };
}
