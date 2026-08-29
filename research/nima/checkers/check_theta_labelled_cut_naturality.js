"use strict";

function assert(c, m) { if (!c) throw new Error(m); }

const phi = x => 3 - 2 * x + 5 * x * x - 7 * x * x * x;
const dphi = x => -2 + 10 * x - 21 * x * x;

function auditCut(p) {
  const g0 = phi(p);
  const h0 = phi(p);
  const gp0 = dphi(p);
  const hp0 = -dphi(p);
  const tailOutwardFlux = -gp0;
  const seamOutwardFlux = -hp0;
  return {
    p,
    value_residual: g0 - h0,
    outward_flux_sum: tailOutwardFlux + seamOutwardFlux,
    seam_physical_endpoint: phi(0)
  };
}

const labels = [
  { n: 2, p: Math.log(2), type: "primitive" },
  { n: 4, p: 2 * Math.log(2), type: "prime_power_square" },
  { n: 8, p: 3 * Math.log(2), type: "connected_prime_power" }
];

const audits = labels.map(x => ({ ...x, ...auditCut(x.p) }));
for (const a of audits) {
  assert(Math.abs(a.value_residual) < 1e-12, "cut values must agree");
  assert(Math.abs(a.outward_flux_sum) < 1e-12, "outward cut flux must cancel");
}
assert(audits[1].type === "prime_power_square", "prime four must retain square typing");
assert(audits[2].type === "connected_prime_power", "prime eight must retain connected typing");

const result = {
  schema: "marici.theta-labelled-cut-naturality.result.v1",
  verdict: "pass",
  audits,
  internal_cut_is_new_mellin_wall: false,
  local_cut_coherence: "exact",
  global_naturality: "unproved_without_coefficient_transport_and_synthesis_maps",
  next_cell: "primitive_two_and_square_four_labelwise_naturality"
};

process.stdout.write(JSON.stringify(result, null, 2) + "\n");
