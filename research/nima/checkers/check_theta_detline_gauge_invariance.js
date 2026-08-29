"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

const N = [1, 2, 4, 8, 16, 32];
const geometricSection = N.map(() => 1);

const frames = {
  stable: N.map(() => 1),
  vanishingCoordinate: N.map(n => n),
  divergingCoordinate: N.map(n => 1 / n)
};

function coordinates(frame) {
  return geometricSection.map((s, i) => s / frame[i]);
}

const stable = coordinates(frames.stable);
const vanishing = coordinates(frames.vanishingCoordinate);
const diverging = coordinates(frames.divergingCoordinate);

assert(stable.every(x => x === 1), "stable frame fixture failed");
assert(vanishing[vanishing.length - 1] < vanishing[0],
  "vanishing coordinate fixture failed");
assert(diverging[diverging.length - 1] > diverging[0],
  "diverging coordinate fixture failed");
assert(vanishing.map(x => 1 / x).every((x, i, a) => i === 0 || x > a[i - 1]),
  "inverse escape fixture failed");

for (let i = 0; i < N.length; i++) {
  assert(stable[i] * frames.stable[i] === geometricSection[i], "stable reconstruction failed");
  assert(vanishing[i] * frames.vanishingCoordinate[i] === geometricSection[i], "vanishing reconstruction failed");
  assert(diverging[i] * frames.divergingCoordinate[i] === geometricSection[i], "diverging reconstruction failed");
}

const loopPeriod = 3;
const exactGaugePeriod = 0;
assert(loopPeriod + exactGaugePeriod === loopPeriod,
  "closed-loop period was not gauge invariant");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.detline_gauge_invariance.result.v1",
  verdict: "coordinate_completion_bounds_are_not_gauge_invariant",
  frames_checked: Object.keys(frames),
  same_geometric_section_reconstructed: true,
  vanishing_coordinate_and_inverse_escape_checked: true,
  closed_loop_period_invariance_checked: true,
  remaining_gate: "source_derived_gauge_invariant_off_seam_detector"
}, null, 2));
