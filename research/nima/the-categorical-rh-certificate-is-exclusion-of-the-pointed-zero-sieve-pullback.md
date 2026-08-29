# The categorical RH certificate is exclusion of the pointed zero-sieve pullback

## Certificate object

Let \(U=H_+\sqcup H_-\) be the disjoint union of the two open half-planes. Over
the poset of compact subsets of \(U\), let \(\mathcal E\) be the completed
theta/Tate state object, equipped with:

- a source-derived distinguished section \(\Omega:1_U\to\mathcal E\);
- a readout \(r:\mathcal E\to\mathcal L\) into the completed determinant line;
- a source action category \(\mathcal W\);
- action maps \(F(w):\mathcal E\to\mathcal E\) for \(w\in\mathcal W\).

The behavioral morphism is

\[
\mathcal O:\mathcal E\longrightarrow
\prod_{w\in\mathcal W}\mathcal L,
\qquad
x\longmapsto\bigl(rF(w)x\bigr)_w.
\]

This is a morphism of compact-indexed completed objects, not merely a family of
pointwise linear maps.

Define the behavioral zero object by the pullback

\[
\mathcal Z_{\mathrm{beh}}
=
\mathcal E\times_{\prod_w\mathcal L}0.
\]

Define the present zero object by

\[
\mathcal Z_0
=
\mathcal E\times_{\mathcal L}0.
\]

There is always an inclusion
\(\mathcal Z_{\mathrm{beh}}\to\mathcal Z_0\), since the identity word is among
the probes.

## Zero-sieve arrow

A zero-propagation law is precisely a factorization

\[
\mathcal Z_0\longrightarrow\mathcal Z_{\mathrm{beh}}
\longrightarrow\mathcal E
\]

whose composite is the defining inclusion of \(\mathcal Z_0\). Together with
the canonical inclusion in the opposite direction, this identifies

\[
\mathcal Z_0\cong\mathcal Z_{\mathrm{beh}}.
\]

Thus zero propagation is stronger than invariance of one kernel under one
operator. It says that the present kernel already is the full source-generated
zero sieve.

Joint observability is the statement that \(\mathcal O\) is monic. Equivalently,

\[
\mathcal Z_{\mathrm{beh}}\cong0.
\]

Consequently, zero propagation plus joint observability forces

\[
\mathcal Z_0\cong0.
\]

This is the categorical nonvanishing mechanism.

## Pointed pullback exclusion

Pull the present zero object back along the distinguished section:

\[
\mathcal V
=
1_U\times_{\mathcal E}\mathcal Z_0.
\]

The object \(\mathcal V\) is the categorical vanishing locus of the distinguished
readout. If \(\mathcal Z_0\cong0\) and \(\Omega\) is disjoint from the zero
section, then

\[
\mathcal V\cong0.
\]

Suppose additionally that a source-derived line isomorphism identifies

\[
r(\Omega)=u\,\Xi
\]

for an everywhere invertible source-fixed section \(u\). Then
\(\mathcal V\cong0\) says exactly that \(\Xi\) has no zeros on \(U\). Reciprocal
completion leaves the seam as the only possible locus for nontrivial zeros.

The RH-bearing statement is therefore not that a coherence diagram commutes.
It is that a specific pointed pullback is initial after behavioral completion
and determinant-line identification.

## Morita transfer of observability

Let the positive and negative sectors form a two-object linking category with
algebras \(A_+\), \(A_-\) and bimodules \(M\), \(N\). Assume the source pairings

\[
M\otimes_{A_-}N\longrightarrow A_+,
\qquad
N\otimes_{A_+}M\longrightarrow A_-
\]

are Morita-full and completion-stable. Then tensor transport by \(M\) and \(N\)
is conservative: it reflects zero objects and monomorphisms.

If the action and readout squares commute under this transport, monicity of the
behavioral morphism in one sector implies monicity in the other. Hence a
Morita-full action reduces two independent observability proofs to:

1. one sectorwise monicity proof;
2. conservative Morita transport;
3. compatibility of the behavioral readouts with that transport.

This is the categorical payoff of the action gate. Mere off-diagonality cannot
perform the transfer because a proper image ideal need not reflect a hidden
state.

## Completion gate

Finite-cutoff monicity does not imply monicity after completion. Let
\(\mathcal O_n\) be the behavioral maps on a cofinal cutoff system. The required
completion theorem is that the canonical comparison

\[
\ker\!\left(\varprojlim_n\mathcal O_n\right)
\longrightarrow
\varprojlim_n\ker(\mathcal O_n)
\]

is an isomorphism and that the right side vanishes.

A sufficient route is:

- cutoffwise monicity;
- Mittag--Leffler control of the observer images or another source-authorized
  exactness condition for the inverse limit;
- a cutoff-independent lower observability margin on every compact;
- compatibility of the distinguished section and determinant line with the
  same limit.

Without this gate, a nonzero state may appear only at completion and belong to
\(\mathcal Z_{\mathrm{beh}}\). This is the escape-at-infinity defect in
categorical form.

## Exact certificate stack

A categorical RH certificate now consists of five typed constructors:

1. **Pointing:** a nonzero completed section \(\Omega\), constructed without
   dividing by \(\Xi\).
2. **Zero sieve:** a source proof that
   \(\mathcal Z_0\to\mathcal Z_{\mathrm{beh}}\) exists.
3. **Observability:** monicity of \(\mathcal O\) in one open sector, stable under
   completion.
4. **Morita transfer:** completion-stable fullness carrying monicity to the
   reciprocal sector.
5. **Determinant bridge:** an invertible line comparison
   \(r(\Omega)=u\,\Xi\).

The 28-box fillers certify coherence of the constructors. The stable apex
section certifies their uniform capability over compacts. Neither substitutes
for any item in this stack.

## Smallest hostile models

1. A present zero followed by a nonzero future readout violates the zero-sieve
   factorization.
2. A nonzero state with zero behavioral record violates monicity.
3. A proper Morita image ideal permits one sector to hide a state invisible
   from the other.
4. Cutoffwise monic maps with collapsing lower margin permit a completion
   kernel.
5. A determinant comparison with a vanishing multiplier transfers a hostile
   zero into the scalar section.

Each failure attacks a different arrow; scalar agreement cannot merge them.

## Frontier

The categorical target is now rigid: construct the zero-sieve factorization
and one completion-stable behavioral monomorphism, then transport it through a
source-derived Morita equivalence and identify the pointed readout with
\(\Xi\).

The current Adams result supplies only the action-category composition law for
one grade-changing subcategory. It does not yet supply Morita fullness,
zero propagation, completion-stable monicity, or the determinant bridge.

## Verdict

Categorical resolution of RH is a pullback-exclusion theorem. Under the five
constructors above, the distinguished zero locus over both open half-planes is
initial, and the determinant bridge confines every nontrivial zero of \(\Xi\)
to the seam. The unresolved work is now localized to four source-bearing
arrows rather than an undifferentiated coherence claim.
