# Topic 9, iteration 2: Compton azimuth records are not incompatible analyzer choices

## Problem and frozen claim

The existing QED Bell proposal assigns binary effects
E_pm=(I pm mu O(alpha))/2 to a device implemented by rotating the Compton
azimuth reference and binning parallel/perpendicular scattering sectors.
Does that record interface follow from the independently given cross section?

**Conjecture:** it does not. Exhaustive sector binning has sharpness 2 mu/pi,
not mu. More importantly, all reference-angle settings are postprocessings of
one local angular POVM. Keeping every no-click record therefore gives CHSH at
most 2 for every incoming state, regardless of luminosity.

**Rivals:** pointwise angular modulation is already binary sharpness; scalar
acceptance makes detector postselection an event-ready protocol; independent
reference-angle choices imply incompatible measurements.

SCC obligation: physical readout compatibility, by pulling the classical record
partition back through the supplied scattering POVM. The source preparation,
Born pairing and Klein-Nishina law remain given. This is not an attempted
resolution of an upstream native Ward/Carrier comparison by a detector test.

## Fresh source audit and why this test is not another Bell calculation

The older `photon-bell-source-packet.md` is not the strongest available
scattering result. Existing packets already retain the full rank-four helicity
amplitude, including Phi5; construct the Breit-Wheeler CP operation density;
and reconstruct the one-loop elastic phase from oriented Cuts and a boundary
jet. `qed-elastic-pair-instrument.md` explicitly scopes its finite-exposure
completion to the audited perturbative order. These results are not reopened.
A normalized wavepacket/exposure is still needed for laboratory probabilities;
the binary particle-content instrument does not itself supply Bell analyzers.

The executable target here is the specific detector implementation in
`qed-bell-experimental-protocol.md` and
`check_qed_bell_experimental_gate.py`. Its Klein-Nishina function is reused
without importing its numerical Bell scan. Aspect's
`epr-compton-local-flatness-nonfactorization` packet supplies an ideal
-cos(2(a-b)) fixture and explicitly marks physical binding false. Its local
energy-momentum identities and ideal polarization theorem remain intact.

The independent discriminator is already one-arm calibration, not a new
scattering-state Bell value.

## Independently specified physical-theory interface

For a free unpolarized electron target, unobserved final spin/polarization,
and fixed incident energy and setting-independent polar-angle support, the
normalized single-Compton azimuth POVM is

\[
F(\phi)=\frac{I-\mu O(\phi)}{2\pi},\qquad
O(\phi)=\cos(2\phi)X+\sin(2\phi)Y,
\qquad 0\leq\mu\leq1.
\]

Its integral is I and its density eigenvalues are (1 pm mu)/(2 pi).
The existing cross section gives

\[
\mu=\frac{\sin^2\theta}{r+r^{-1}-\sin^2\theta},\qquad
r=\frac{1}{1+\epsilon(1-\cos\theta)}.
\]

The range follows from r+r^(-1)>=2 and sin(theta)^2<=1. At epsilon=1/3 and
theta=pi/2 the independently evaluated control is mu=12/13. No Bell data fixes
this coefficient. A fixed polar-angle band gives its cross-section-weighted
version; including additional angular records does not remove the parent POVM.

Let the positive record comprise the two perpendicular sectors centered on
alpha+pi/2 modulo pi, and the negative record the parallel sectors centered
on alpha modulo pi, each of half-width Delta. Every other azimuth is recorded
as a rejection/no-click. Direct integration, for 0<Delta<=pi/4, gives

\[
\eta=\frac{4\Delta}{\pi},\qquad
\nu=\mu\frac{\sin(2\Delta)}{2\Delta},
\qquad E_\pm=\frac\eta2(I\pm\nu O(\alpha)),
\qquad E_0=(1-\eta)I.
\]

Exhaustive binning has Delta=pi/4, eta=1 and nu=2 mu/pi. This is optimal
among all exhaustive stochastic binary classifiers: their response g satisfies
|g(phi)|<=1, so the Bloch component along any axis is bounded by
mu/(2 pi) times the integral of |cos(2 phi)|, which is 4. A different exhaustive
partition cannot recover the missing factor.

For an independently prepared + eigenstate of O(alpha), the positive-record
probability is therefore

\[
p_+=\tfrac12+\frac\mu\pi,
\]

whereas the claimed binary implementation predicts 1/2+mu/2. The residual
mu(1/pi-1/2) is nonzero for polarized sensitivity mu>0. An unpolarized calibration
alone cannot distinguish the two interfaces. This is a prospective physical
calibration prediction; no calibration counts have been acquired.

## Common-parent obstruction, including rejected records

Write q_x(a|phi) for any local classification of the recorded azimuth, including
stochastic classifiers and a retained zero record. The effects are

\[
E_{a|x}=\int q_x(a|\phi)F(\phi)\,d\phi.
\]

For an arbitrary two-photon density rho the setting-independent parent law is

\[
p(\phi_A,\phi_B)=\operatorname{Tr}
 [\rho(F_A(\phi_A)\otimes F_B(\phi_B))].
\]

All proposed setting records are local postprocessings of this single positive
normalized law. The pair of angular records is an explicit Bell-local variable.
Assigning zero to +1 does not change locality. Every deterministic response
has CHSH +2 or -2, so convex mixing proves the bound for every rho. This is an
analytical common-parent theorem, not a numerical scan over source states.

The checker constructs exact interval-refinement parents for the existing
four axes and half-widths pi/4, pi/8 and pi/16. Their tensor-product marginals
are compared as FULL four-dimensional operators, without reducing the source
to a Bell scalar. Positivity certificates use 223/71<pi<22/7 and exact algebraic
coefficients, not floating eigenvalue tolerances.

Narrow accepted sectors can nevertheless give a conditional violation. The
frozen Phi+ control at muA=muB=1, Delta=pi/16 has eta=1/4 and

\[
S_{\rm selected}=\frac{64(\sqrt2-1)}{\pi^2}>2,
\qquad
S_{\rm complete}=\frac{S_{\rm selected}}{16}+\frac98<2.
\]

The acceptance EFFECT eta I is scalar, but the accepted subset of the angular
record depends on the chosen setting. Scalar acceptance suffices for the
previous quantum no-signalling comparison; it does not turn this detector
postselection into a setting-independent source herald. The old support theorem
is preserved, not strengthened into loophole closure.

## Risky consequence and scope

The declared azimuth-binning implementation cannot provide a detector-complete
Bell test at any luminosity. The old mu-squared dilution estimate and its
2.01412 value are not predictions for exhaustive binary Compton records. In
the zero-width sector limit nu approaches mu but eta approaches zero; treating
that limit as a complete binary detector is the missing interface error.

This excludes reference rotations and classical relabeling of a common record,
not a different setting-dependent quantum interaction. A replacement must
supply its independently calibrated complete effects/instrument and show why
no common-parent simulation exists; naming two axes or increasing statistics
is insufficient. No claim is made that all possible gamma-ray analyzers, ideal
polarization instruments, or Marici scattering realizations fail.

## Disposition and execution

Frozen contract: `contracts/compton-record-compatibility.v1.json`.
Checker: `checkers/check_compton_record_compatibility.py`.
Owner SCC model: `nima-compton-record-compatibility`.
Receipt: `results/compton-record-compatibility.json`.

The common-parent conjecture survives; the three stated interface rivals fail.
The exact single-arm residual is -mu/2+mu/pi. Unpolarized input and a
zero-visibility detector are separate nondiscriminating controls; the ideal
projector Bell control still gives 2 sqrt(2).

Verification:

- Manifest validation: `e_38524_1791415141550643100_117`.
- The first frozen run (`e_38524_1791415151175052600_119`) stopped on a nested-
  radical equality. Exact field reduction (`e_38524_1791415199242370900_120`)
  proves the residual zero. This was a comparator defect, not a physical
  counterexample; algebraic-number equality replaced syntactic equality, with
  no numerical tolerance or change to the physical domain.
- Final freeze: `scc-freezes/nima-compton-record-compatibility.adfb01a1ddc1c3b5.json`.
  Frozen challenge `e_38524_1791415783572347000_130` and fresh model check
  `e_38524_1791415799533887100_131` pass.
- Retired legacy CLI: `e_38524_1791415449070135000_124`, expected exit 1 before
  optional imports/calculation. Its original numerical body remains as history;
  its source cross-section function is still reused by the new checker.
- Isolated failure/retirement controls: `e_38524_1791415587312977000_127`.
  AssertionError, RuntimeError and a seeded old experimental verdict leave no
  stale success; the live new receipt is unchanged. The final control edit only
  separates unpolarized input from zero visibility and is covered by the fresh
  challenge/check above.
- Final receipt/source-hash verification: `e_38524_1791415895988071300_132`.

Early notice and tested report to Aspect were admitted as communication proposals
`ep_410e61d2-07a2-4fc6-a75f-158fb7438ce0` and
`ep_f90acb75-32b4-42ee-95a1-763bb6d58eb7`; admission is provenance, not evidence.

The historical protocol now carries an explicit withdrawal notice. No old
experimental receipt existed at inspection, and its retired entrypoint cannot
regenerate one. No Aspect files, native source theorems, formal proofs, physical
apparatus, or public ledger entries were changed. Work remains uncommitted.
The global SCC models listing returned exit 1; only this owner-local manifest
and checker closure are asserted, not global registry health.

## Remaining boundary

The rebin-only Compton route is closed, not waiting for more luminosity or more
angles. A replacement interaction requires its own source-bound instrument;
no such replacement has been validated here.

The broader native-source comparison is still distinct and untested. The
freshly read `physical-cut-coaction-is-continuous-on-the-projective-laurent-completion.md`
constructs a marked Laurent coaction, whereas
`breit-wheeler-source-operation-density.md` constructs a phase-space Gram
pairing. Their shared name Cut does not identify their types. The next
nonredundant source audit is to inspect the native two-open-pair Ward maps
against those two objects and locate an actual comparison, retaining the
conjugate amplitude and all marks. If that map is absent, stop at that typed
boundary rather than inventing a quantum pairing or another acceptance schema.
