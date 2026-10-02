# Persistent backbone and unoriented exchange decomposition

## Organizing idea

The tetrahedral and octahedral compatibility fields can be organized as

\[
\boxed{M=P+2X,}
\]

where P counts a **formation-and-diagonal backbone** and X counts **unoriented
pairwise closure relations**. Orienting each exchange supplies its two matrix
entries.

The working interpretation calls the backbone persistent and the pairwise
closure layer exchange. This gives a more informative description than a single
undifferentiated arrow total: a cell combines formation structure with mutual
compatibility among its realized ports. The support decomposition is exact;
using its two parts as dynamical or energetic resources is the construction to
pursue next.

This note builds on the [monomial-projector support theorem](monomial-projector-support-theorem.md),
[octahedral realization](octahedral-monomial-projector-realization.md), and
[cube comparison](cube-octahedron-architecture-independent-energy-audit.md).

## Full-support decomposition

Let g be the number of group-indexed positions, m the monomial spatial-fiber
dimension, and Q the realized coordinate set, with d=|Q|=gm. Keep the three
operator stages separately typed:

    raw --L--> local selection --R--> alignment --N--> raw.

Their support counts are

\[
\ell=gm^2,\qquad r=g^2m,\qquad n=d^2.
\]

Here R is the alignment operator, called G in some earlier notes. Lowercase
ell, r and n denote counts, not operators. The collective projector is
N=u u^dagger/||u||^2, with u of full coordinate support.

Split its feedback support into diagonal closure and off-diagonal closure:

\[
d^2=d+d(d-1).
\]

The involution (q,q') -> (q',q) fixes the d diagonal entries and pairs all
remaining entries without fixed points. Thus

\[
P=\ell+r+d=gm(m+g+1),\qquad
X=\binom d2,
\]

and

\[
P+2X=gm^2+g^2m+(gm)^2=M.
\]

P is a scalar count here, not the local projector P_c. The partition places all
local-selection and alignment arrows in the backbone; it pairs only the
collective-feedback entries. That placement is the organizing convention of
this model.

## Three-dimensional packets

For m=3,

\[
d=3g,\qquad P=3g(g+4),\qquad X=\binom{3g}{2},
\]

\[
M(g)=P+2X=9g+12g^2.
\]

| Packet | Positions g | Coordinates d | Formation ell+r | Diagonal closure | Persistent backbone P | Unoriented exchanges X | Oriented total M |
|---|---:|---:|---:|---:|---:|---:|---:|
| Tetrahedron | 12 | 36 | 540 | 36 | **576** | **630** | **1836** |
| Octahedron | 24 | 72 | 1944 | 72 | **2016** | **2556** | **7128** |

Thus

\[
1836=576+2(630),\qquad 7128=2016+2(2556).
\]

Doubling the number of positions does not double the field. Local selection
scales linearly in g, while alignment and dense collective closure scale
quadratically. In particular, closure grows from 36^2 to 72^2. The model's large
component is therefore pairwise compatibility bookkeeping, rather than a sum
of independent local contributions.

## Retain weights when forgetting exchange orientation

The exchange layer can be constructed without throwing away complex phase.
Let s=||u||^2, and write

\[
D_q=N_{qq}=\frac{|u_q|^2}{s},\qquad
w_{qq'}=N_{qq'}=\frac{u_q\overline{u_{q'}}}{s}.
\]

For each unordered pair {q,q'}, choose a display order q<q' and retain w_qq'.
Its opposite coefficient is determined by conjugation, not by assigning a
second independent weight:

\[
w_{q'q}=\overline{w_{qq'}}.
\]

The Hermitian exchange contribution is

\[
E_{\{q,q'\}}
=w_{qq'}|q\rangle\langle q'|
+\overline{w_{qq'}}|q'\rangle\langle q|.
\]

The full feedback reconstructs exactly as

\[
N=\sum_q D_q|q\rangle\langle q|
  +\sum_{q<q'}E_{\{q,q'\}}.
\]

Equivalently, its quadratic response on a field a separates into

\[
a^\dagger Na
=\sum_qD_q|a_q|^2
 +2\operatorname{Re}\sum_{q<q'}\overline{a_q}w_{qq'}a_{q'}.
\]

This is a concrete starting point for studying how the exchange layer couples
to the backbone. The phase-sensitive cross terms are retained explicitly.
For a rank-one collective field, the weights obey

\[
|w_{qq'}|^2=D_qD_{q'},\qquad
w_{qq'}w_{q'q''}=D_{q'}w_{qq''}.
\]

These identities give useful reconstruction and consistency checks: the many
exchange slots belong to one coherent collective field rather than carrying
unrelated free coefficients.

The pair involution exchanges coordinate labels within the feedback matrix.
When lifting the records back to the circuit, retain the aligned-to-raw stage
tags: both entries are feedback arrows, not opposite traversals of a single
stage-typed circuit edge.

## Backbone coefficients and identity feedback

The backbone contains the actual diagonal coefficients D_q, not unit weights.
Their sum is one. Its support count happens to equal the count of the earlier
identity-feedback implementation when u has full support, but the operators
are different:

    backbone feedback: diag(N);
    identity feedback: I.

The decomposition retains the exchange layer to reconstruct N. It does not
assert that the diagonal backbone alone gives the original collective return.
This distinction lets us use the 576 and 2016 backbones without conflating them
with a different feedback implementation of the same cardinality.

## The cube as a restricted-compatibility case

The [native cube eigenline](cube-octahedron-architecture-independent-energy-audit.md)
has two nonzero spatial coordinates per position, rather than three. The
ambient coordinate space still has dimension 72, but the collective vector has
only d_active=48 nonzero entries. Its collective feedback therefore has 48
nonzero diagonal entries and 48*47 off-diagonal entries.

Keeping the full alignment operator gives

\[
P_{\mathrm{cube}}=96+1728+48=1872,
\qquad X_{\mathrm{cube}}=\binom{48}{2}=1128,
\]

\[
4128=1872+2(1128).
\]

Of the full alignment operator's arrows, 576 transport unused normal
coordinates. Restricting to the arrows covered by selected closed traversals
instead gives

\[
P_{\mathrm{cube,closed}}=96+1152+48=1296,
\]

\[
3552=1296+2(1128).
\]

The exchange layer is the same in both cube conventions; the difference lies
in retaining or pruning unused alignment structure. This makes the cube a
useful third case: geometry can suppress exchange pairs by restricting the
selected mode's support.

More generally, if the reference vector has k nonzero coordinates in an
m-dimensional monomial fiber, its transported vectors each have k, and

\[
P=gk^2+g^2m+gk,\qquad X=\binom{gk}{2}.
\]

For the selected closed-traversal union, the alignment support becomes g^2*k,
so its backbone is gk^2+g^2*k+gk. The full-support formulas are recovered at k=m.

## Next executable object

Construct explicit records for:

1. the L and R formation arrows with their stage types and coefficients;
2. the nonzero diagonal feedback entries D_q;
3. each unordered active pair {q,q'} with one complex coefficient and its
   conjugation rule;
4. the lift back to all oriented feedback arrows.

Test reconstruction of N, the rank-one weight identities, and the resulting
collective return for tetrahedron, octahedron and cube. Then compare a proposed
exchange/backbone update law against the retained-source Hamiltonian in the
energy audit, rather than attaching an energy unit to each slot in advance.

No new executable pairing checker is introduced by this documentation note.
The tetrahedral, octahedral and cube source checkers establish the underlying
operator supports; the pairing formulas and weighted reconstruction above are
algebraic consequences of their rank-one Hermitian feedback. The decomposition
provides the working language for the next dynamics experiment, not yet its
energy normalization or particle identification.
