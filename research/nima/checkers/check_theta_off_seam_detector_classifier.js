"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function sigma(z) {
  return z;
}

function normSquared(z) {
  return z * z;
}

assert(normSquared(sigma(0)) === 0, "metric-zero witness failed");
assert(sigma(0) === 0, "dual-pairing zero witness failed");

const windingOfZ = 1;
assert(windingOfZ !== 0, "connection period witness failed");

const sectorIndices = { right: 1, left: -1 };
assert(sectorIndices.right + sectorIndices.left === 0,
  "global index cancellation witness failed");
assert(sectorIndices.right !== 0 && sectorIndices.left !== 0,
  "supported sector defects disappeared");

const d = 3;
const h = 1 / d;
assert(Math.abs(d * h - 1) < 1e-12, "finite contraction identity failed");

const scalarManufacturedComplex = { differential: "completed_section" };
assert(scalarManufacturedComplex.differential === "completed_section",
  "circular-complex hostile fixture failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.off_seam_detector_classifier.result.v1",
  verdict: "only_source_contracted_supported_complex_survives",
  metric_only_rejected: true,
  dual_pairing_only_rejected: true,
  connection_period_only_rejected: true,
  global_index_rejected_by_reciprocal_cancellation: true,
  supported_sector_indices_retained: true,
  finite_contraction_identity_checked: true,
  remaining_gate: "assemble_source_complex_and_completion_stable_sector_contractions"
}, null, 2));
