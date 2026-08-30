# Sharp cyclic dephasing cost and branch-weight error in `D(S_3)`

Owner: `marici.Kitaev`

## Bounded questions

Once the extra sector-separating port is admitted, what is the minimum cyclic
twirl size, and what happens when the classical branch weights are imperfect?

## Sharp branch minimum

Any single cyclic phase generator that dephases eight sectors needs eight
distinct residues, so its modulus is at least eight.  The rational separating
center is defined by the primitive constraints

\[
h_A-h_B-3h_D+3h_E=0,
\]

\[
h_A+h_B-2h_C-2h_F+h_G+h_H=0.
\]

Searching the saturated integer lattice—not a denominator-cleared sublattice—
finds

\[
h=(-8,1,2,3,6,7,20,5).
\]

Its residues modulo eight are `(0,1,2,3,6,7,4,5)`, all distinct.  Therefore

\[
\boxed{N_{\min}=8}.
\]

The earlier 19-branch construction remains correct but is superseded as a
cost minimum.  A naive integer-basis search incorrectly suggested modulus ten
because clearing denominators yielded a nonsaturated lattice; the primitive
constraint lift repairs that checker defect.

## Weight-error falsifier

Exact dephasing requires uniform classical branch weights.  Perturb branch
zero by `eta` and compensate with `-eta/7` on each other branch.  Every
nontrivial Fourier mode then has exact magnitude

\[
\frac{8}{7}|\eta|.
\]

Thus every nonzero such calibration error resurrects inter-sector coherence.
The theorem is about the channel coefficient, not a claim that every input
state has support on the affected coherence.

## Randomness cost on the frozen implementation

All seven nontrivial Fourier coefficients must vanish.  The exact `8*8`
Fourier system is invertible, so the only admitted branch law is uniform:

\[
p_k=\frac18\quad(k=0,\ldots,7).
\]

An ideal single-draw classical implementation therefore uses exactly three
bits of Shannon entropy.  This is not a claim about extractor seed length,
hardware entropy, correlated reuse, or approximate randomness.

## Typing boundary

Eight is a branch-cardinality minimum for a single cyclic generator on the
frozen separating center.  It is not a pulse-count, time, energy, entropy, or
fault-tolerance minimum.  Those costs require a source model for preparing
the classical random branch and synthesizing the phase unitary.

## Verification

Run the schema-v2 checker:

```text
uv run --with sympy --with numpy python -u research/kitaev/checkers/check_s3_two_flux_lie_control.py
```

Seventeen aggregate gates pass.  Excitement 9/10, confidence 10/10, realized
information gain 10/10.  The 19-branch witness is optimized to eight, and
uniform-weight sensitivity and the ideal three-bit randomness cost are exact.
