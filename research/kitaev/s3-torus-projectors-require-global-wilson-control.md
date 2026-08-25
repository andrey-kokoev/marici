# The two completing torus ports require coherent global Wilson control

Owner: `marici.Kitaev`

Ledger: Entry 2465

## Bounded question

Are the coherent sector projectors that complete protected \(D(S_3)\) torus
control native local Hamiltonian terms, or what source resource constructs
them?

## Native-source obstruction

Each frozen star or plaquette projector is the identity after compression to
the eight-dimensional frustration-free torus ground space. Thus the span of
the native commuting-projector generators compresses to rank one and cannot
distinguish topological sectors. None of

\[
 Q_A,Q_B,Q_C,Q_F
\]

is a native contractible Hamiltonian term.

This is distinct from the earlier endpoint flux ports. An endpoint projector
acts on a prepared excitation and may break gauge invariance. A torus sector
projector splits globally degenerate ground states and therefore carries
noncontractible support or an equivalent global protocol.

## Exact Wilson synthesis

For a Wilson loop of type \(x\) around one noncontractible cycle, the action on
the transverse character basis is diagonal:

\[
 W_x|a\rangle=\frac{S_{xa}}{S_{Aa}}|a\rangle.
\]

The resulting eight-by-eight Wilson character table has full rank. Hence every
sector projector has an exact expansion

\[
 Q_a=\sum_x c_x^{(a)}W_x.
\]

The checker exhausts all subsets of loop types and records the minimum support
family and one exact coefficient packet for each \(Q_a\). The individual costs
are

\[
 |Q_A|=|Q_B|=8,\qquad |Q_C|=|Q_F|=|Q_G|=|Q_H|=6,
 \qquad |Q_D|=|Q_E|=4.
\]

More importantly, it solves the two-target problem directly. Every completing
pair

\[
 (A,C),(A,F),(B,C),(B,F)
\]

requires all eight Wilson types; there is no cheaper shared family hidden by
the separate expansions. This identifies the exact global operator resource
without promoting its availability to a pulse source.

The same table exposes a strict readout/control gap. Four Wilson observables
are necessary and sufficient to give all eight sectors distinct joint spectral
signatures (there are eight minimum four-type families), whereas every
controllability-completing projector pair requires eight Wilson types. Jointly
faithful sector identification therefore does not furnish coherent projector
Hamiltonians.

## Instrument boundary

Full \(M_8\) controllability requires continuous coherent phases
\(e^{itQ_a}\) for one \(a\in\{A,B\}\) and one \(a\in\{C,F\}\). Three weaker
objects do not suffice:

1. a projective measurement of \(Q_a\), which destroys cross-sector coherence;
2. a classical sector label, which contains information but no data action;
3. an uncontrolled perturbative splitting, whose amplitude occurs only at
   system-size order and lacks an exact calibrated pulse.

A coherent Wilson ancilla can in principle compute the sector, kick back a
phase, and uncompute—the diagonal case that survived the label-copy no-go.
The remaining theorem is a microscopic, fault-tolerant construction of that
global phase protocol for a valid completing pair. In particular, character
completeness is an algebraic synthesis theorem, not an instrument-access
theorem.

## Falsifiers and typing boundary

This packet fails if a contractible native star/plaquette generator has a
non-scalar compression on the frozen torus ground space, or if a completing
pair lies in the span of fewer than eight rows of the exact Wilson character
table. The checker tests the latter exhaustively. It does not prove that the
abstract Wilson Hamiltonians can be pulsed by a geometrically local,
fault-tolerant device; that remains an explicitly unresolved instrument type.

## Artifacts

- Checker: `checkers/check_s3_torus_projector_wilson_synthesis.py`
- Result: `results/s3-torus-projector-wilson-synthesis.json`
