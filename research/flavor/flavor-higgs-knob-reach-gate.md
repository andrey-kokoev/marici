# Higgs context-knob reach gate (WP413)

## Candidate controls

WP412 needs one operation that varies the gauge-invariant Higgs quadratic term
while retaining the original broken vacuum as a reference. Four candidate
sources fail at different arrows.

1. The early-Universe thermal bath generates a source-derived Higgs thermal
   mass and supports condensate and screening calculations, but it is not an
   executable laboratory setting.
2. Heavy-ion collisions are executable and have calibrated electromagnetic and
   hadronic thermometers, but no common-frame Higgs curvature or retained-vacuum
   displacement instrument exists in the fireball.
3. A nonminimal curvature coupling can generate a Higgs mass deformation, but
   no laboratory curvature setting approaches a calibrated Higgs response.
4. A portal background could implement $c$, but introduces an unobserved source
   field and therefore returns to the missing-mediator problem.

The Standard Model electroweak crossover is measured nonperturbatively at
$159.5\pm1.5$ GeV. Recent ALICE direct-photon analyses quote effective slopes
around $0.3$--$0.46$ GeV, while warning that this slope is not a direct initial
temperature measurement. Using the largest quoted central slope, the scale
ratio is greater than 348; a radiation-density comparison exceeds
$1.4\times10^{10}$. This comparison is a reach diagnostic, not a claim that the
fireball has a single equilibrium temperature.

Primary sources are the [Standard Model crossover lattice calculation](https://doi.org/10.1103/PhysRevD.93.025003)
and the [ALICE direct-photon review](https://doi.org/10.1140/epjc/s10052-024-12935-y).

## Common-frame obstruction

The decisive failure is categorical. The early-Universe object has the source
and Higgs response but no executable control. The heavy-ion object has an
executable hot-medium preparation but no Higgs response instrument. Coordinate
compatibility between temperatures cannot compose these arrows.

Consequently no currently admitted Standard Model operation supplies all four
capabilities: source-derived deformation, executable control, Higgs curvature
readout, and retained-reference displacement readout. A new portal field would
be a new source constructor, not a repair by reinterpretation.

Run `uv run --with sympy python
research/flavor/checkers/wp413_higgs_knob_reach_gate.py` to regenerate the JSON
result.
