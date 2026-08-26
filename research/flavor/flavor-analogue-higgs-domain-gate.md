# Analogue Higgs control domain gate (WP418)

## Executed analogue instrument

Phase-locked terahertz pulses have been used to excite and control hybrid Higgs
amplitude modes in an iron-based superconductor. The experiment reports a large,
reversible modulation of spectral weight while the mode frequency shifts by
less than ten percent. Two-pulse coherent spectroscopy supplies an executable
setting, a phase reference, and a calibrated amplitude-mode readout.

Primary source: [Light quantum control of persisting Higgs modes in iron-based
superconductors](https://doi.org/10.1038/s41467-020-20350-6).

This is the closest realized apparatus to WP412's relational architecture. It
demonstrates that a Higgs-type amplitude coordinate can be prepared, coherently
driven, and read relative to a pulse reference. It does not retain or measure
the displacement of the electroweak vacuum required by WP412.

## Domain and operator mismatch

The controlled object is the hybridization and spectral weight of collective
electron- and hole-band order-parameter modes. The paper does not report a
commanded change of a Standard Model Higgs quartic coefficient. Its material
order parameter, Hilbert space, source Hamiltonian, calibration, and symmetry
groupoid differ from those of the electroweak Higgs field.

Likewise, atomic lattice gauge–Higgs work supplies detailed proposals and
simulations, but the cited implementation is not an executed laboratory
experiment and concerns a $U(1)$ lattice model rather than the Standard Model
Higgs doublet.

Primary proposal: [Atomic quantum simulation of the lattice gauge–Higgs
model](https://doi.org/10.1103/PhysRevLett.111.115303).

Without an admitted source interface, the THz command $u_{\rm THz}$ and the
Standard Model coefficient $\kappa_4^{\rm SM}$ are independent coordinates:

$$
\frac{\partial\kappa_4^{\rm SM}}{\partial u_{\rm THz}}=0.
$$

Calling the material amplitude mode “Higgs” records a shared symmetry-breaking
mechanism; it does not identify the two physical state domains.

## Transferable constructor

The instrument architecture is valuable and source-authorized within its own
domain:

1. prepare a broken-symmetry state;
2. retain the phase-locked first pulse as a relational reference;
3. vary a second calibrated pulse;
4. read the coherent amplitude response;
5. test a withheld pulse setting without refitting.

Transport to WP416 requires a physical interface whose commanded setting
changes the electroweak quartic and whose response is read in detector units.
No algebraic analogy or shared word “Higgs” supplies that interface.

## Verdict

Analogue Higgs control closes an executable relational-instrument gate only for
the condensed-matter source domain. It cannot close the Standard Model quartic
actuation gate or the flavor-selector gate. The smallest transport falsifier is
the absence of a source-derived map from the THz command to
$\kappa_4^{\rm SM}$.

Run `uv run --with sympy python
research/flavor/checkers/wp418_analogue_higgs_domain_gate.py` to regenerate the
JSON result.
