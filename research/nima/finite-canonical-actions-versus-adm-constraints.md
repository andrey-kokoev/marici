# Finite canonical actions versus the claimed ADM constraint algebra

## Frozen question and closure condition

Does the legacy S4 stabilizer check establish a constrained Hamiltonian or ADM
comparison, once the strongest completed rotor/phase realization is retained?

Active SCC obligation: forward realization and attachment comparison. The
source is the complete four-point permutation action, all its stabilizers and
composition, plus the separately typed completed Clifford rotor packet. They
are not identified by dimension. Keep the rotor's scalar/bivector coordinates,
phase fiber, positive kappa, defining-module lift and both HJ charts.

**Conjecture:** the old calculation establishes stabilizer covariance, not a
Poisson constraint algebra. Its claimed holonomy/flux and forced-SU2 checkers
report formulas without calculating them. The completed positive rotor
Hamiltonian cannot simply be renamed a zero constraint. Its existing HJ
structure should nevertheless admit a regular parametrized-constraint
comparison with an explicitly added angular parameter/momentum pair.

**Rivals:** stabilizer transport is a vanishing commutator; finite canonical
symmetry already supplies infinitesimal gauge constraints; Hamiltonian
conservation makes H=0 a nonempty constraint surface; the old evidence defects
invalidate the existing rotor; or supplying a parametrized mechanical
constraint derives ADM and its physical time interpretation.

**Risky consequences:** replay the entire old group calculation, inject a
failed stabilizer predicate, and test an actual noncommuting pair. Retain all
24 actions in their canonical cotangent lift. Reuse the completed rotor's
exported lift and generator, not its weaker historical zero-offset version.
The literal zero-level test and the extended constraint must have different
results; reduction must recover the original symplectic form and full phase
transport, without subtracting the module-selected constant.

**Closure:** distinguish the exact group theorem, canonical representation,
empty literal H=0 level and the conditional parametrized comparison. Repair or
quarantine the defective evidence and supersede its ADM/LQG promotion claims.
No new continuum construction, physical clock, selected gauge group or GR
field theory is requested. The existing continuum counterexample and
Hamiltonian/clock/scale-selection boundaries must remain closed.

## The group theorem and its actual canonical interpretation

The original checker does calculate

\[
g\,\operatorname{Stab}(p)\,g^{-1}=\operatorname{Stab}(g(p)).
\]

It defines no phase space, Poisson bracket or constraint functions. Injecting
one false stabilizer predicate changes `all_checks_pass` to false but execution
still returns normally and retains its ADM-closure classification. The repaired
entry point enforces the group equality and reports only that theorem.

Covariance is not commutation: take g=(01) and h=(12), with h fixing anchor 0.
Their group commutator is the nonidentity permutation (2,0,1,3). Conjugation
moves the stabilizer from anchor 0 to anchor 1 rather than fixing its fiber.
This is not a test of the different Poisson bracket printed in the old report.

There IS a canonical representation after the declared linearization. For the
actual permutation matrix P_g, the cotangent lift is

\[
(x,\pi)\longmapsto(P_gx,P_g^{-T}\pi).
\]

All 24 maps preserve the canonical form on T*R4, and all source compositions
are preserved. That eight-dimensional cotangent space is not identified with
the separately supplied four-dimensional Clifford phase space. A finite group
with its discrete topology has no nontrivial continuous one-parameter subgroup;
a continuous enlargement and its constraint functions are additional data.
Neither this fact nor the old check excludes such enlargements.

## Use the completed rotor, including its phase-selected constant

`check_retained_rotor_phase_transport.py` is run in full, with only its receipt
unlink/write suppressed. The comparison uses its computed lift, generator and
two checked HJ charts. In its conventions,

\[
\Omega=dq\wedge dp-ds\wedge dz,\qquad
\beta=p\,dq+s\,dz,\qquad
\alpha=d\varphi-\beta/\kappa,\qquad \kappa>0,
\]
\[
H^+=q^2+p^2+\kappa,\qquad
D=(0,2p,-2q,0),\qquad
\varphi'=(p^2-q^2-\kappa)/\kappa.
\]

The literal level H+=0 is empty: H+ is at least kappa. Conservation of H+ does
not change this. Subtracting kappa does not preserve the completed phase lift:
at angular parameter pi the retained phase is -1, whereas the zero-offset
replacement gives +1. A different energy level or compensating phase law is
new data, not a repair made silently inside this comparison.

There is also an exact convention residual in the old holonomy prose. These
specified forms give d(beta)=-Omega and therefore d(alpha)=+Omega/kappa, not
the printed negative sign. The residual is 2*Omega/kappa. No physical holonomy
orientation or field-theory bracket is inferred from that calculation.

## A regular parametrized comparison does exist

Add a cotangent pair (theta,Pi_theta) for the UNWRAPPED ANGULAR PARAMETER, not
physical time. On the extended six-dimensional base use

\[
\Omega_{\rm ext}=\Omega+d\theta\wedge d\Pi_\theta,\qquad
C=\Pi_\theta+H^+.
\]

C=0 is nonempty and regular because its derivative with respect to Pi_theta is
one. Its characteristic vector is (D,1,0); thus the old base generator is
recovered without changing H+. The section theta=theta0, Pi_theta=-H+ pulls
Omega_ext back to the ENTIRE original Omega, including the stationary s,z
pair. The constraint/section bracket is nondegenerate, and its Dirac bracket
on all four original coordinates is the original Poisson bracket.

The full phase comparison is equally explicit:

\[
\alpha_{\rm ext}=d\varphi-
\frac{\beta+\Pi_\theta\,d\theta}{\kappa},\qquad
\alpha_{\rm ext}(D,1,0,\varphi')=-C/\kappa.
\]

The supplied phase lift is therefore horizontal on C=0. Its section pulls
alpha_ext back to alpha. For the original Pin action with orientation sigma,
extend the source map by theta -> sigma*theta+eta and Pi_theta -> Pi_theta.
The full extended form and phase connection transform with that same sign,
and C is preserved. No reversal or phase coordinate was deleted.

Both previously checked HJ charts satisfy C=0 with p=partial_q A and
Pi_theta=partial_theta A. The spectator pair is retained by the identity
mixed generating term z*s_initial. The original chart boundary term and
module compatibility were rerun unchanged. Full source history records remain
separate retained data; neither a matrix endpoint nor this comparison
reconstructs or identifies them.

This discharges the finite Hamiltonian-to-parametrized-constraint comparison.
It does NOT derive an ADM field constraint from the discrete source. The
added cotangent pair is an explicit analytical extension, not a selected
physical clock. Requiring a field realization later cannot invalidate this
completed conditional comparison.

## Evidence correction and the first missing interface

The legacy holonomy/flux and SU2-promotion programs contain formula dictionaries,
not computed Poisson observables, brackets or group-selection tests. Both live
entry points now refuse verification with exit 2. Their historical receipts
were absent and remain absent. The existing abelian phase lift survives in
full; a Maurer-Cartan identity conditional on a chosen group does not select
SU2 from that successful U1 construction. The independent witness-gauge result
and its charge/kinetic underdetermination are not reopened.

The first missing ADM interface in these legacy arguments is a specified field phase space and a
Poisson/constraint map from the finite realization, with actual constraint
functions and smearing conventions. Its acceptance test must compare those
functions and their brackets, not just dimensions, group conjugation or
conservation of a scalar. An antisymmetric symplectic/curvature form also does
not certify a Lorentzian metric signature. No spacetime or time interpretation
is transported through that missing interface.

The earlier continuum counterexample remains closed. Neither another S4
identity nor another compatible parametrization supplies the missing field
map. This branch is deferred until new source material supplies it; there is
no waiting task or further finite-model search here.

## Disposition and verification

**Retained:** stabilizer covariance, canonical cotangent action and the
completed rotor phase/HJ model. **Constructed:** its regular parametrized
constraint and reduction. **Excluded:** literal H+=0 on the stated positive
kappa domain. **Withdrawn:** using the old finite reports as evidence of ADM
closure, a forced SU2 promotion or Planck-area calibration.

Nine original source files are preserved in
`quarantine/20261007-constraint-evidence/SHA256SUMS`. The repaired group checker
writes only `results/discrete-stabilizer-covariance-repaired.json`. The exact
comparison writes `results/finite-canonical-constraint-comparison.json` and
checks that old and predecessor receipts remain byte-unchanged.

Freeze: `scc-freezes/nima-finite-canonical-constraint-comparison.103d360ad31583da.json`.
Frozen challenge `e_38524_1791405554907021000_88` passes. Invocation:

```text
uv run --with sympy python research/aspect/scc/scc.py check nima-finite-canonical-constraint-comparison
```

Fresh owner-model check `e_38524_1791405926665530300_89` and the repaired live
stabilizer entry `e_38524_1791405926744866900_90` pass. Both quarantined entries
return the required nonzero status under the exact comparison. No physical GR
or fresh proof-assistant verification is claimed. Final source-integrity check
`e_38524_1791406210672400500_91` confirms twelve current inputs. Graph event
`ev-000000015826-fcdf6175-5470-46b9-a712-9ab27abc8a27` records the result without
certifying its truth. All artifacts remain uncommitted.
