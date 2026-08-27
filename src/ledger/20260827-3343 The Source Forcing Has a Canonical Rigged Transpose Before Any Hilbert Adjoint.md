# The Source Forcing Has a Canonical Rigged Transpose Before Any Hilbert Adjoint

For the fixed theta source `f` in a test space `E`, the forward incidence is

\[
B_f:\mathbb C\to E,
\qquad B_f(c)=cf.
\]

Its topological transpose is canonical and metric-free:

\[
B_f^\times:E'\to\mathbb C,
\qquad B_f^\times(\lambda)=\lambda(f).
\]

This is the missing reversal of variance. Hilbert adjoints arise only after a
chosen Riesz embedding `H -> E'` and change when the Hilbert metric changes.
For a Fourier-fixed source, the rigged transpose is Fourier-covariant under the
dual action.

The appropriate completed block is therefore initially a rigged
correspondence from `E direct-sum C` to `E' direct-sum C`, not a bounded
selfadjoint operator on one prematurely selected Hilbert space. Primitive,
square, and connected-tail grades need continuous embeddings into `E'`; they
need not share one Hilbert adjoint.

The next gate is to test each boundary grade against evaluation on `f` and
compare that canonical transpose with the independently derived reciprocal
incidence.

Research packet:
`research/grothendieck/the-source-forcing-has-a-canonical-rigged-transpose-before-any-hilbert-adjoint.md`

Exact checker:
`research/grothendieck/checkers/check_rigged_transpose_precedes_hilbert_adjoint.py`

The checker passes 6/6 exact tests.
