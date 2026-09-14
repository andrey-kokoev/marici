# The eight-leg relative Hardy feature admits a sign-preserving dyadic Halmos refinement

## One projection row relative to a base cutoff

Let `P,Q` be orthogonal projections and restrict first to

\[
x
\in
\operatorname{Ran}P.
\]

Set

\[
\boxed{
B
=PQP|_{\operatorname{Ran}P}.
}
\]

The projection feature is

\[
F_Qx
=(Qx,
(I-Q)x).
\]

Its norm identity is

\[
\boxed{
\|x\|^2
=
\|Qx\|^2
+
\|(I-Q)x\|^2.
}
\]

Moreover,

\[
\|Qx\|^2
=
\langle x,Bx\rangle,
\]

\[
\|(I-Q)x\|^2
=
\langle x,(I-B)x\rangle.
\]

Thus the two projection rows are positive realizations of `B` and `I-B` on the base-cutoff source.

## Polar identification

The operator

\[
QP:
\operatorname{Ran}P
\to
\operatorname{Ran}Q
\]

has polar decomposition

\[
\boxed{
QP
=V_QB^{1/2}.
}
\]

Likewise,

\[
(I-Q)P
=V_{I-Q}
(I-B)^{1/2}.
\]

The partial isometries preserve norms on the corresponding support spaces. Hence refining `Qx` is equivalent, up to canonical polar transport, to refining `B^(1/2)x`.

## Dyadic refinement of the positive `Q` row

Let

\[
E_1
=P_{\{1\}}(B).
\]

The exact infinite defect identity is

\[
\boxed{
B
=E_1
+
\sum_{j\ge0}
B^{2^j}
(I-B^{2^j}).
}
\]

Therefore the positive row `Qx` admits the norm-preserving feature refinement

\[
\boxed{
Qx
\rightsquigarrow
\left(
E_1x,
(d_j^B x)_{j\ge0}
\right),
}
\]

where

\[
d_j^B
=
[B^{2^j}
(I-B^{2^j})]^{1/2}.
\]

More precisely, polar transport by `V_Q` identifies the original observer-generated feature range with the abstract dyadic feature range. The refinement is canonical up to the irrelevant unitary freedom on null complements.

## Complementary row

Set

\[
C
=I-B.
\]

The `(I-Q)x` row has Gram `C`. It has its own exact tower

\[
\boxed{
C
=P_{\{1\}}(C)
+
\sum_{j\ge0}
C^{2^j}
(I-C^{2^j}).
}
\]

Here

\[
P_{\{1\}}(C)
=P_{\{0\}}(B),
\]

which is the exact `H_10` mismatch atom on `ran P`.

Thus

\[
\boxed{
(I-Q)x
\rightsquigarrow
\left(
P_{\{0\}}(B)x,
(d_j^{I-B}x)_{j\ge0}
\right).
}
\]

The `Q` and `I-Q` rows resolve opposite endpoints of the same angle contraction.

## Complete base-side refinement

Combining the two rows gives

\[
\boxed{
\begin{aligned}
\|x\|^2
&=
\|P_{\{1\}}(B)x\|^2
+
\|P_{\{0\}}(B)x\|^2\\
&\quad+
\sum_{j\ge0}
\|d_j^Bx\|^2
+
\sum_{j\ge0}
\|d_j^{I-B}x\|^2.
\end{aligned}
}
\]

Pointwise on `lambda in (0,1)`, this is

\[
\lambda
+(1-\lambda)
=1,
\]

with each summand expanded by its dyadic partition.

## Outside base-cutoff source

For general `x in H`, split first

\[
x
=Px+(I-P)x.
\]

On `ran(I-P)`, use the complementary compression

\[
B^{out}
=(I-P)(I-Q)(I-P).
\]

Halmos polar sewing identifies its generic angle contraction with `B`; its eigenvalue-one atom is `H_00`, the Sonin sector, while the inside eigenvalue-one atom is `H_11`.

Thus the full refinement contains:

- `H_11` and `H_10` on the inside source;
- one generic angle spine with its two endpoint-oriented towers;
- `H_01` and `H_00` on the outside source.

## Finite-depth transition maps

At every finite depth, refine the current bulk slot by

\[
W_Cz
=(Cz,
(I-C^2)^{1/2}z)
\]

for the appropriate positive contraction `C`. This is an exact isometry:

\[
W_C^*W_C=I.
\]

Existing atom and defect slots are carried identically. Therefore all depth refinements compose strictly.

## Sign-preserving refinement

Suppose a projection row occurs in a larger positive feature with signed-readout sign

\[
\epsilon
\in
\{+1,-1\}.
\]

Assign the same sign `epsilon` to every atom and dyadic slot replacing that row. If `J` is the original fundamental symmetry and `J_ref` the refined diagonal symmetry, the refinement isometry `R_n` satisfies

\[
\boxed{
R_n^*
J_{ref}
R_n
=J.
}
\]

It also satisfies

\[
\boxed{
R_n^*R_n=I.
}
\]

Thus refinement changes neither the ordinary positive Gram nor the signed readout.

## Application to the four-leg relative feature

The four rows are

\[
Q_L^T,

\qquad
I-Q_L^T,

\qquad
Q_L^0,

\qquad
I-Q_L^0
\]

with signs

\[
(+,-,-,+).
\]

Refine each row relative to the same base cutoff `P` and carry its sign to all descendants. Denote the finite-depth refinement by

\[
\Psi_{L,n}^{ref}.
\]

Then

\[
\boxed{
(\Psi_{L,n}^{ref})^*
\Psi_{L,n}^{ref}
=I,
}
\]

and

\[
\boxed{
(\Psi_{L,n}^{ref})^*
J_{4,n}^{ref}
\Psi_{L,n}^{ref}
=Q_L^T-Q_L^0.
}
\]

The identity is exact at every depth.

For the pure reference pair, nesting makes its generic tower vanish; only exact mismatch/intersection atoms remain. The formal refinement adds zero slots and is harmless.

## Application to the eight-leg ordered feature

The eight-leg feature duplicates the four-leg feature on source legs `PA_g` and `A_g`. Apply the same row refinement to both copies.

Let

\[
\Theta_{L,n}^{ref}
\]

be the resulting positive feature and let

\[
K_{8,n}^{ref}
\]

be the off-diagonal signed involution pairing corresponding refined rows slotwise.

Because the same isometry is applied to both cross-paired copies,

\[
\boxed{
(\Theta_{L,n}^{ref})^*
K_{8,n}^{ref}
\Theta_{L,n}^{ref}
=
\frac12
(P\Delta Q_L+
\Delta Q_LP).
}
\]

The skew companion similarly remains

\[
\boxed{
\frac1{2i}
[P,
\Delta Q_L].
}
\]

Hence the exact ordered-product placement is invariant under dyadic Halmos refinement.

## Filtered limit

Taking the inductive limit over depth produces a countable positive feature carrier. Since all transition maps are isometries preserving the signed involution, the limit has:

\[
\boxed{
\Theta_{L,\infty}^*
\Theta_{L,\infty}
=
\Theta_L^*
\Theta_L,
}
\]

\[
\boxed{
\Theta_{L,\infty}^*
K_{8,\infty}
\Theta_{L,\infty}
=
\Theta_L^*K_8\Theta_L.
}
\]

Thus the filtered/pro-simplicial microscopic expansion is exactly compatible with the finite eight-leg macro-feature.

## Observer and conductor restrictions

Every construction is performed characterwise and by functional calculus in the corresponding angle contraction. Angular conductor projections commute with the row decomposition and restrict all atom/defect slots.

Therefore conductor filtration and dyadic depth refinement commute exactly at fixed cutoff.

## What the refinement does not prove

The refinement provides:

1. exact positive mass bookkeeping;
2. exact atom typing;
3. strict depth coherence;
4. unchanged relative signed readout.

It does not provide:

1. convergence of individual physical defect legs as `L->infinity`;
2. a universal effective truncation depth;
3. positive minimalization to `|A_S|`;
4. simultaneous regulator bounds.

Those are analytic completion questions, not finite-cutoff typing problems.

## Revised positive cell shape

The positive `C_34` filler has a finite macro-shape with eight cross-polarized rows. Each projection/complement row expands into:

- an exact endpoint atom;
- a countable dyadic generic-angle tower.

Reference generic towers collapse in the pure nested model. Tate generic towers remain filtered.

Thus the complete object is finite in macro-width and countably infinite in microscopic depth.

## Disposition

The dyadic Halmos refinement is a sign-preserving isometric subdivision of the relative positive feature:

\[
\boxed{
\text{eight-leg positive dilation}
\longrightarrow
\text{atom-typed dyadic eight-row tower},
}
\]

with exact invariants

\[
\boxed{
R_n^*R_n=I,
\qquad
R_n^*J_{ref}R_n=J.
}
\]

Therefore positive projection-pair sewing and prolate spectral refinement are compatible on the nose. The remaining work concerns analytic cutoff limits, not construction of the filtered positive feature itself.
