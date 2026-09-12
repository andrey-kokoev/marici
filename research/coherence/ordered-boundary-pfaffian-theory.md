# Ordered boundary–Pfaffian theory: synthesis and claim ledger

## Kind

The constructed finite object is a parity-polarized, metric, fermionic factorization algebra on ordered half-line configurations. Equivalently, it is a based skew self-dual complex whose even sectors carry Pfaffian torsion and whose odd sectors carry a canonical residual line.

It is presently a mathematical theory. Its operator vocabulary has familiar physical semantics, but no physical realization or empirical interpretation is asserted here.

## Primitive data

For positive lengths \(a_i\), let \(R_i\) be half-line left translation and \(S_i=R_i^*\) right zero-extension. Their boundary noncommutativity is

\[
K_{j,i}=R_jS_i-S_iR_j.
\]

Cubical alternation gives the operator-valued two-cochain

\[
\mathcal F_{ij}=K_{j,i}-K_{i,j}.
\]

It is antisymmetric and satisfies the covariant Bianchi identity

\[
[R_i,\mathcal F_{jk}]+[R_j,\mathcal F_{ki}]+[R_k,\mathcal F_{ij}]=0.
\]

## Finite chain theorem

On exponentials \(f_t(x)=e^{-tx}\), endpoint evaluation gives the skew chain kernel

\[
M_{ij}(t)=\operatorname{sgn}(a_j-a_i)e^{-t|a_j-a_i|}.
\]

For \(2m\) distinct positions,

\[
\operatorname{Pf}M
=
\operatorname{or}(a_0,\ldots,a_{2m-1})
\exp(-tL_{2m}),
\]

where

\[
L_{2m}=\sum_{r=0}^{m-1}(a_{(2r+1)}-a_{(2r)}).
\]

This is the minimum perfect-matching cost on the line. The identity is exact, not asymptotic.

For \(2m+1\) positions, the Pfaffian cofactor vector

\[
v_i=(-1)^i\operatorname{Pf}(M_{\widehat i})
\]

spans the canonical null line.

## Minimal model

A determinant-one triangular congruence reduces the chain form to

\[
M\cong
H(x_0)\oplus H(x_2)\oplus\cdots\oplus\mathbb K^{n\bmod2},
\qquad
H(x)=\begin{pmatrix}0&x\\-x&0\end{pmatrix}.
\]

The hyperbolic pairs are contractible after passage to the associated skew complex. Their weights survive in the Pfaffian determinant line. The odd line survives in homology.

Thus the two outputs are

\[
\boxed{
\text{persistent state} = \text{odd homology},
\qquad
\text{pairing record} = \text{even Pfaffian torsion}.
}
\]

## Sewing laws

For contiguous ordered blocks:

1. even–even factorization is strict;
2. even amplitudes act on odd cofactor lines;
3. odd–odd contraction through the rank-one cross kernel reconstructs the even Pfaffian;
4. the empty configuration is the unit.

These operations give the finite \(\mathbb Z_2\)-graded sewing algebra.

Refinement is metric and polarized, not topologically invisible. Inserting a pair contributes its amplitude between existing pairs and its inverse inside an existing pair.

## Arithmetic realization

Prime labels provide lengths

\[
a_p=\log p.
\]

Valuations supply lattice position, signed prime words supply trace depth, and independent prime axes supply cubical coherence dimension. These are compatible gradings but must not be identified.

At rank four, the ordered prime frame \((2,3,5,7)\) yields

\[
L_4=\log\frac{3\cdot7}{2\cdot5}=\log\frac{21}{10}.
\]

All 24 frame permutations preserve this coordinate and multiply the oriented readout by their permutation sign.

## Analytic carrier

No fixed locally finite broken-Sobolev line is invariant under all signed log-prime translations: the generated breakpoint group is dense. The correct carrier is a varying finite-depth graph bundle

\[
B\longmapsto(\mathcal D_B,\mathcal T_B,J_B).
\]

Right zero-extension is a Green isometry between fibers. Left shift is a bordered compression with an explicit relative Green defect. A word of depth \(k\) lands in the signed-log trace fiber \(\Gamma_k^+\).

## Corrections retained

The first degree-zero candidate \(F_{pq}=\{d_p,h_q\}+\{d_q,h_p\}\) is a genuine boundary anticommutator but not a two-form-valued curvature. Its proposed six-face P4 interpretation was rejected by an exact null audit. The later cochain \(\mathcal F_{ij}=K_{j,i}-K_{i,j}\) repairs that typing error.

The theory should therefore be cited through the antisymmetric window cochain and chain-kernel theorem, not through the earlier degree-zero Pfaffian analogy.

## Open boundary

The finite algebraic core is coherent. Still open are:

- completion over unbounded prime sets and word depth;
- determinant/Pfaffian-line continuity on the projective source rigging;
- compatibility of sewing with the full varying Green graph;
- coincident-length degenerations;
- a universal categorical presentation covering noncontiguous sewing;
- any separately proposed physical realization.

## Verification map

The principal executable certificates are:

- `check_four_prime_hypercube.py`;
- `check_four_prime_halfline_windows.py`;
- `check_four_prime_antisymmetric_two_cochain.py`;
- `check_p4_permutation_covariance.py`;
- `check_p4_arbitrary_length_chambers.py`;
- `check_p6_pfaffian_matching.py`;
- `check_odd_chain_pfaffian_kernel.py`;
- `check_odd_odd_pfaffian_gluing.py`;
- `check_pfaffian_even_cut_sewing.py`;
- `check_even_odd_pfaffian_module.py`;
- `check_pair_insertion_refinement_law.py`;
- `check_chain_skew_minimal_model.py`.
