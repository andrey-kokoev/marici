# Three coherence edges minimally certify the four-branch flux interferometer

Owner: `marici.Kitaev`

## Bounded question

Given the established rank-one environment-Gram criterion, what is the
smallest phase-sensitive experiment family that certifies clean closure of the
transposition-flux controlled-reflection interferometer?

## Verdict

Under a frozen branch-preserving and no-leakage model, exactly three pairwise
coherence tests are necessary and sufficient. Their tested branch pairs must
form a spanning tree on the four joint path-and-flag labels.

One convenient minimum family is:

```text
(path 0, A)  <->  (path 0, B)
(path 0, A)  <->  (path 1, A)
(path 1, A)  <->  (path 1, B)
```

Unit visibility on these three edges forces all four returned environment
states onto one ray. Their measured phases determine every branch phase up to
one global phase. Any family with fewer than three edges leaves a disconnected
hostile model that passes all selected tests while retaining which-branch
information.

## Four-branch dilation

Let the path label be `p` in `{0,1}` and the fusion flag be `q` in `{A,B}`.
Assume the complete physical process preserves these labels and returns the
visible probe configuration. Its dilation has the form

\[
|p,q\rangle|0\rangle_E
\longmapsto
d_{pq}|p,q\rangle|\eta_{pq}\rangle_E,
\]

where each environment vector is normalized. For the target controlled
reflection,

\[
d_{0A}=d_{0B}=d_{1A}=1,
\qquad
d_{1B}=-1.
\]

The environment includes probe centralizer state, path wave packet, motion
controller, annihilation channel, timing modes, local excitations, and every
unreturned record.

Tracing it out multiplies the coherence between two joint branches `i,j` by

\[
d_i\overline{d_j}
\langle\eta_j|\eta_i\rangle.
\]

Every computational-basis population is correct for every possible Gram
matrix. Basis-state success and clean classical annihilation therefore certify
none of the required coherences.

## Spanning-tree sufficiency

Associate a graph vertex to each branch `0A,0B,1A,1B`. Test an edge `i-j` by
preparing a coherent superposition of those two branches and measuring the
output visibility and phase in a complementary basis.

For normalized vectors,

\[
|\langle\eta_j|\eta_i\rangle|=1
\]

holds exactly when the two vectors lie on one ray. If every edge of a
connected test graph has unit visibility, ray equality propagates along paths.
All four environment vectors therefore lie on one common ray and the Gram
matrix has rank one.

A tree on four vertices has three edges. Hence three comparisons suffice.

The phase of each tested overlap fixes the relative environment-ray phase on
that edge. Tree propagation then fixes all four phases up to a common scalar.
Comparing them with the target coefficients `d_pq` decides whether the closed
unitary is the desired controlled reflection or a coherent but miscalibrated
diagonal gate.

## Necessity of three comparisons

Any graph with four vertices and fewer than three edges is disconnected. Put
all environment vectors in one tested connected component on a ray `e_0` and
all vectors in another component on an orthogonal ray `e_1`. Every selected
edge still has unit visibility because no selected edge crosses the
components.

The untested cross-component coherences vanish. The physical channel is not
unitary, yet all selected tests pass.

Thus three is a strict information lower bound for pairwise branch-coherence
tests in this model, not merely a convenient count.

## A source-aligned three-edge family

Choose the tree

\[
0A-0B,
\qquad
0A-1A,
\qquad
1A-1B.
\]

The edges diagnose different physical closures:

### Nonenclosing flag edge

The `0A-0B` comparison tests whether the nominal reference arm itself records
the middle-pair charge. It should not.

### A-channel path edge

The `0A-1A` comparison tests recombination of enclosing and nonenclosing arms
when the monodromy is trivial. Failure isolates arm-dependent motion,
dynamical phase noise, or probe return before the sign response is involved.

### Enclosing flag edge

The `1A-1B` comparison tests the nontrivial monodromy arm and must show the
target relative minus sign with unit visibility. Failure isolates
charge-dependent probe or environment return.

Together they imply the unmeasured `0B-1B` coherence and every diagonal
cross-comparison under the frozen model.

## What the three tests do not certify

The theorem assumes that branch labels are preserved and no amplitude leaks
outside the declared four-dimensional space. A general physical process can
mix `A` and `B`, switch paths, change probe species, or leak charge while still
matching selected interference fringes on a restricted preparation family.

The complete packet therefore has two layers:

1. leakage and branch-transition audit;
2. three-edge environment-ray audit conditional on layer one passing.

The spanning-tree theorem must not be promoted to unrestricted process
tomography.

## Quantitative hostile family

Let the first three branch environments equal `e_0` and let

\[
|\eta_{1B}\rangle
=
\gamma|e_0\rangle
+
\sqrt{1-|\gamma|^2}|e_1\rangle,
\]

with `e_1` orthogonal to `e_0`. All basis-state outputs are ideal. Any test
family omitting every edge incident across the partition containing `1B`
passes, while coherences involving `1B` are reduced by `gamma`.

At `gamma=0`, the environment has made a perfect record of the nontrivial
joint branch. At `|gamma|=1`, closure is coherent and only a calibratable phase
remains.

This is the smallest hostile witness for the controlled-reflection arm.

## First-failed convention

For this audit, `first` should be defined by causal constructor order rather
than by an arbitrary matrix-entry ordering:

1. branch preservation and leakage;
2. reference-arm flag coherence `0A-0B`;
3. trivial-monodromy arm closure `0A-1A`;
4. nontrivial-monodromy flag coherence `1A-1B`;
5. target phase calibration.

The first failed gate identifies the earliest physical distinction that
escaped uncomputation. A different spanning tree is mathematically valid but
changes diagnostic localization, so its ordering must be declared rather than
called canonical.

## Fault interpretation

- Failure of `0A-0B`: the reference arm already measures fusion charge.
- Failure of `0A-1A`: arm geometry or probe return is distinguishable even
  without a sign phase.
- Failure of `1A-1B`: the enclosing probe retains charge information rather
  than returning catalytically.
- Unit visibility with wrong phase: coherent calibration or winding error.
- Leakage before all three: the four-branch Gram model is inapplicable.

This classification has higher information value than repeating the same
fringe on several basis-state inputs.

## Falsifiers

- Four normalized branch environment vectors require more than three
  unit-modulus overlaps when the tested graph is connected.
- A graph with fewer than three pairwise tests is connected on four vertices.
- Unit overlap magnitude fails to imply equality of normalized vectors up to
  phase.
- A disconnected test graph excludes orthogonal environment rays on different
  components.
- Correct branch populations imply rank-one environment closure.
- The three-edge result is used despite untested channel mixing or leakage.
- The word `first` is used without a declared causal or algebraic ordering.

## Claim boundary

This packet specializes the existing environment-Gram theorem to the four
branches of the transposition-flux interferometer and proves the minimum
pairwise test count. It does not construct the interferometer or replace a
leakage and transition audit.

Its new result is exact: three connected coherence edges minimally certify
rank-one return, while their physical choice determines how failures are
localized to the source process.

No build, checker, or Git operation was used.
