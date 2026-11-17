import assert from 'node:assert/strict';

// Reviewed authored H–Na recipe checkpoint, not geometry inferred from inventory.
// The preceding contour sketches are superseded; higher isotope contours retain
// their separate tests. Full edge/arrow/transform assertions also live in
// isotope-wiring-li6-line-colors.test.mjs.
const drawings = {
  Li6: [null, '-86 14 172 200', 8, 0],
  Li7: ['Li6', '-86 14 172 200', 8, 2],
  Be9: ['Li7', '-86 14 172 250', 10, 2],
  B10: ['Li6', '-86 -86 172 300', 13, 0],
  B11: ['B10', '-86 -86 172 300', 13, 2],
  C12: ['B10', '-86 -86 172 350', 15, 0],
  C13: ['C12', '-86 -86 172 350', 15, 2],
  N14: ['C12', '-86 -86 172 400', 18, 0],
  N15: ['N14', '-86 -86 172 400', 18, 2],
  O16: ['N14', '-86 -86 172 450', 20, 0],
  O17: ['O16', '-86 -86 172 450', 20, 2],
  O18: ['O16', '-86 -86 172 450', 20, 4],
  F19: ['O18', '-86 -86 172 500', 23, 4],
  Ne20: ['F19', '-136 -86 272 350', 25, 0],
  Na23: ['Ne20', '-86 -86 172 600', 28, 4],
};

export function assertCurrentDrawing(core, source) {
  const expected = drawings[source.id];
  assert(expected, 'No reviewed current drawing expectation: ' + source.id);
  const before = JSON.stringify(source);
  assert.equal(source.graph.pairs.length, source.Z);
  assert.equal(source.graph.witnesses.length, source.N);
  assert.equal(core.validate(source).valid, true);
  for (const standalone of [false, true]) {
    const svg = core.renderSVG(source, { standalone });
    const [base, view, arrows, braces] = expected;
    assert.equal(svg.match(/data-definition="([^"]+)"/)?.[1], source.id);
    assert.equal(svg.match(/data-drawing-base="([^"]+)"/)?.[1] ?? null, base);
    assert.equal(svg.match(/viewBox="([^"]+)"/)?.[1], view);
    assert.equal((svg.match(/class="mid-arrow"/g) || []).length, arrows);
    assert.equal((svg.match(/class="neutron lithium-side-bar"/g) || []).length, braces);
    assert.equal((svg.match(/class="neutron sketch-cross"/g) || []).length, 1);
    assert.match(svg, /class="neutron lithium-base" data-cell="s2-01" d="M-50 184 L50 184"/);
    assert.doesNotMatch(svg, /drawing-unavailable|<path class="ep |data-question-cell=|class="difference-mark/);
    assert.equal(JSON.stringify(source), before);
  }
}
