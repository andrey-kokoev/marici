# Hadamard renormalization-section audit

## Question

Can Hadamard short-distance admissibility select a unique point in the full
finite-counterterm orbit of Ledger 3037?

## Typed object

Let \(\mathfrak P\) be the space of admitted renormalized field operators and
let \(\mathfrak H_P\) be the Hadamard states for \(P\). The natural object is a
family

\[
\mathfrak H\longrightarrow\mathfrak P,
\qquad
P\longmapsto\mathfrak H_P.
\]

Hadamard regularity is a membership condition inside \(\mathfrak H_P\). It is
not a canonical section of this family.

## External primary constraints

Fewster, *The art of the state*, arXiv:1803.06836, reviews two facts used here:

- any two Hadamard states for the fixed field problem differ by a smooth
  two-point function;
- there are infinitely many Hadamard states and no canonical choice among
  their smooth parts.

Hollands--Wald, *Local Wick Polynomials and Time Ordered Products of Quantum
Fields in Curved Spacetime*, arXiv:gr-qc/0103074, proves that locality,
covariance, scaling, commutation, and continuity determine the renormalized
objects only up to finitely many parameters, including curvature couplings.

Thus even strong short-distance and covariance requirements do not generally
remove finite renormalization freedom.

## Application to the finite-time toy cosmology

Ledger 3037 proves that the three admitted finite local counterterms span the
complete rank-three response space. A finite scheme change alters the chosen
renormalized operator and matching coordinates. The appropriate Hadamard
parametrix changes with that operator.

Comparing every scheme point against its own source-compatible parametrix can
test admissibility but does not select one point. Comparing every point against
one frozen parametrix may select a point, but the freezing is already an
independent normalization condition and cannot be attributed to Hadamard
regularity alone.

Even after freezing the operator, the smooth Hadamard freedom leaves many
states. Additional state data are still required.

## Result

Hadamard admissibility cannot by itself provide the missing finite readout
section. It can:

- reject a state with the wrong wavefront singularity;
- reject a counterterm that exits the admitted operator class;
- test a section chosen by independent physical normalization.

It cannot choose the renormalized operator or the smooth part of a state from
the source-independent class of possibilities.

The remaining selector must therefore be operational: declared renormalized
couplings or amplitudes, together with a state preparation/readout condition.

## Scope

This is a no-go result for Hadamard regularity alone. A stronger source packet
that fixes the renormalized operator and enough physical observables may still
select a unique state. That would be new normalization authority, not a
consequence of the bare Hadamard condition.

## Sources

- arXiv:1803.06836, especially the Hadamard-state discussion around Eq. (12)
- arXiv:gr-qc/0103074
- Collins--Holman--Vardanyan, arXiv:1408.4801
- Ledger 3037 and `research/benincasa/finite-counterterm-authority-audit.md`
