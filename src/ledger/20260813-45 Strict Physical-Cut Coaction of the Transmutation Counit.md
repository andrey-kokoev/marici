# Strict Physical-Cut Coaction of the Transmutation Counit

## Record

Date: 2026-08-13

Status: all-arity tree-level field-theory theorem. For either of the two
gauge-equivalent scalar-scaffold gluing kernels, the pairwise transmutation
counit has an explicit physical-Cut coproduct. Its only correction to a tensor
product of lower counits factors through a separate lower Yang--Mills
annihilator. Consequently the counit is group-like in the ordinary tensor
product of lower amplitude quotients, not merely in the coarse Cut-evaluation
quotient of entry 44.

Reproducible certificate:

    research/nima/check_transmutation_cut_coaction.rs

The certificate expands every pair, both gluing gauges, and every inequivalent
planar split through seven points. It verifies the complete signed support
identity, including the annihilator correction, rather than only its final
amplitude.

## Setup

Let a physical channel have odd scaffold endpoints \(i,j\). Its two
factorization kernels may be written

\[
C^{(0)}_{km}
=
X_{k,m}-X_{k,j}-X_{m,i},
\]

and

\[
C^{(1)}_{km}
=
X_{k,m}-X_{k,i}-X_{m,j},
\]

where \(k\) lies in the open left interval and \(m\) lies in the open right
interval. Gauge invariance of the two lower amplitudes identifies the two
forms.

Let

\[
E_n=E_L\sqcup E_R
\]

be the corresponding partition of external even scaffold labels. The lower
amplitudes acquire internal even labels \(x_L,x_R\). There are four
distinguished external even labels:

\[
\ell_-=j-1,
\qquad
r_-=i-1,
\]

where the second expression is cyclic, and

\[
\ell_+=i+1,
\qquad
r_+=j+1.
\]

Thus \(\ell_-\) and \(r_-\) precede the two channel endpoints, while
\(\ell_+\) and \(r_+\) succeed them. For \(\sigma=0,1\), write

\[
(\ell_\sigma,r_\sigma)
=
\begin{cases}
(\ell_-,r_-),&\sigma=0,\\
(\ell_+,r_+),&\sigma=1.
\end{cases}
\]

On any local factor define

\[
B_g
=
\sum_{\substack{o\ {\rm odd}\\o\notin\{g-1,g+1\}}}
\partial_{X_{g,o}},
\]

and retain the notation

\[
U_{ab}
=
\partial_{X_{a,b}}
\prod_{g\notin\{a,b\}}B_g
\]

for the pairwise scalar counit.

## Two auxiliary sectors

The raw Cut formula naturally produces two additional operator types.

First, define the all-odd sector

\[
Z
=
\prod_{g\in E}B_g.
\]

Second, for four distinct even labels \(a,b,c,d\), define the two-pair sector

\[
P_{ab;cd}^{(2)}
=
\partial_{X_{a,b}}
\partial_{X_{c,d}}
\prod_{g\notin\{a,b,c,d\}}B_g.
\]

No physical interpretation of \(P^{(2)}\) is needed for the theorem. It is
merely the coefficient multiplying the null \(Z\) sector.

## Exact raw coaction formula

Apply \(U_{ef}\) to the scaffold factorization formula. Keep the one-bridge
terms of entry 43 and quotient only those terms that repeat a lower even label,
which annihilate the corresponding lower amplitude by polarization
multilinearity.

For either \(\sigma=0\) or \(1\), the result is as follows.

### Retained pair on the left

If \(e,f\in E_L\), then

\[
\boxed{
\Delta_D^{(\sigma)}U_{ef}
=
U_{ef}^{L}
\boxtimes
U_{x_R,r_\sigma}^{R}
+
\mathbf 1_{\ell_\sigma\notin\{e,f\}}\,
P_{ef;\ell_\sigma x_L}^{(2),L}
\boxtimes
Z_R.
}
\]

### Retained pair on the right

If \(e,f\in E_R\), then

\[
\boxed{
\Delta_D^{(\sigma)}U_{ef}
=
U_{\ell_\sigma,x_L}^{L}
\boxtimes
U_{ef}^{R}
+
\mathbf 1_{r_\sigma\notin\{e,f\}}\,
Z_L
\boxtimes
P_{ef;r_\sigma x_R}^{(2),R}.
}
\]

### Retained pair crosses the channel

If \(e\in E_L\) and \(f\in E_R\), then

\[
\boxed{
\Delta_D^{(\sigma)}U_{ef}
=
U_{e,x_L}^{L}
\boxtimes
U_{x_R,f}^{R}.
}
\]

The crossing formula is independent of \(\sigma\). Reversing \(e,f\) changes
only notation because \(U_{ef}=U_{fe}\).

These are identities of signed derivative supports modulo the separate
repeated-label annihilators. They are stronger than equality after evaluating
the complete Cut.

## Proof: crossing edge

Suppose \(e\in E_L\) and \(f\in E_R\). The distinguished derivative

\[
\partial_{X_{e,f}}
\]

cannot act on either lower amplitude. It must hit the \(+X_{k,m}\) term in
the gluing kernel, forcing

\[
k=e,
\qquad
m=f.
\]

The two built-in gluing derivatives become

\[
\partial_{X_{e,x_L}},
\qquad
\partial_{X_{x_R,f}},
\]

which are precisely the retained pair derivatives of the two lower counits.
Every remaining \(B_g\) choice must stay on its own side. Restricting the
global allowed odd targets to that side gives exactly the corresponding local
\(B_g\) support. The bridge coefficient is \(+1\), proving the crossing
formula term by term.

## Proof: same-side pair and anchor cancellation

Take \(e,f\in E_L\). The retained derivative
\(\partial_{X_{e,f}}\) remains on the left. A bridge sourced by a right even
label \(m\) has two possible representatives:

1. choose the left odd label \(k\), hitting \(+X_{k,m}\);
2. choose the applicable channel-boundary odd label, hitting the negative
   boundary term in \(C^{(\sigma)}_{km}\).

For every non-anchor \(m\), both choices occur in \(B_m\). After the bridge is
removed they leave exactly the same lower tensor, with opposite signs, and
cancel.

At \(m=r_\sigma\), the boundary target is adjacent to \(m\) and is excluded
from \(B_m\). Only the positive cross target survives. The built-in right
derivative then makes the pair \((x_R,r_\sigma)\). Varying \(k\) over the
allowed left odd labels supplies exactly \(B_{x_L}\), while all other local
choices supply the remaining lower \(B\)'s. This is the main term

\[
U_{ef}^{L}\boxtimes U_{x_R,r_\sigma}^{R}.
\]

There is one second bridge orientation: a left even source may target a right
odd label. The same positive/negative cancellation removes every source except
\(\ell_\sigma\). If \(\ell_\sigma\) is already one of the retained labels,
that \(B\)-source is absent and nothing remains. Otherwise the built-in
derivative creates a second left pair
\((\ell_\sigma,x_L)\), while the right factor contains only odd-target
derivatives. Summing all choices gives exactly

\[
P_{ef;\ell_\sigma x_L}^{(2),L}\boxtimes Z_R.
\]

This proves the left formula. Reflection across the channel proves the right
formula.

## The all-odd sector is a separate annihilator

The correction terms are harmless for a stronger reason than cancellation
after gluing. On a lower \(q\)-gluon factor,

\[
\prod_{g\in E_q}\mathcal W_g A_q^{\rm YM}
=
\mathcal W_e
\left(
\prod_{g\ne e}\mathcal W_g A_q^{\rm YM}
\right)
=
\mathcal W_e A_q^{\operatorname{Tr}\phi^3}
=0.
\]

Expand the product of all \(\mathcal W_g\)'s. Every term that chooses an even
target repeats that target's even label, because the same label already
appears as the source of its own \(\mathcal W\)-factor. Lower polarization
multilinearity kills it. The complete surviving support is therefore exactly

\[
\prod_{g\in E_q}B_g=Z_q.
\]

Consequently

\[
\boxed{
Z_q\in\operatorname{Ann}(A_q^{\rm YM}).
}
\]

Each correction in the raw coaction belongs to the separable ideal

\[
\operatorname{Ann}(A_L)\boxtimes\operatorname{Diff}^{\rm pol}_R
+
\operatorname{Diff}^{\rm pol}_L\boxtimes\operatorname{Ann}(A_R).
\]

No entangled Cut-kernel relation is required.

## Strong group-like theorem

Let

\[
Q_L=
\operatorname{Diff}^{\rm pol}_L/\operatorname{Ann}(A_L^{\rm YM}),
\qquad
Q_R=
\operatorname{Diff}^{\rm pol}_R/\operatorname{Ann}(A_R^{\rm YM}).
\]

The three raw formulas immediately give

\[
\boxed{
\Delta_D u_n
=
u_L\boxtimes u_R
\quad\text{in}\quad
Q_L\boxtimes Q_R.
}
\]

This holds for every physical planar channel, every retained pair, and either
gauge form of the gluing kernel. Cyclic rotation reduces a general odd--odd
channel to the representative used in the proof, so no channel is omitted.

Thus the stronger alternative left open in entry 44 is realized on the
counit submodule: its Cut-kernel discrepancy is generated by a separate lower
annihilator.

The theorem does not assert that the entire Cut-evaluation kernel for arbitrary
differential operators is separable. It proves precisely the separability
needed by the transmutation counit.

## Gauge change as deletion-simplex homotopy

The two gluing kernels select opposite boundary anchors:

\[
C^{(0)}
\longleftrightarrow
(\ell_-,r_-),
\qquad
C^{(1)}
\longleftrightarrow
(\ell_+,r_+).
\]

For a same-left pair, the two main representatives differ by

\[
U_{x_R,r_-}^{R}-U_{x_R,r_+}^{R};
\]

for a same-right pair they differ by

\[
U_{\ell_-,x_L}^{L}-U_{\ell_+,x_L}^{L}.
\]

All four operators represent the same lower scalar counit. More strongly, the
three retained labels in each comparison form a triangular face of the lower
deletion simplex. That triangle is the canonical higher reference-change
filler between the two edge contractions.

Hence the gauge equivalence of the two polarization sums is mirrored
combinatorially by a deletion-simplex homotopy. The choice of gluing kernel
does not disappear mysteriously; it moves the anchor from one boundary end to
the other along an already existing coherent face.

## What the certificate checks

Normalize the channel to

\[
D=X_{1,2\ell+1}.
\]

For every \(4\leq n\leq7\), every
\(2\leq\ell\leq n-2\), every one of the
\(\binom n2\) retained pairs, and both \(C^{(0)}\) and \(C^{(1)}\), the Rust
program:

1. expands all \((n-2)^{n-2}\) monomials of \(U_{ef}\);
2. lets each possible derivative hit each of the three terms of \(C_{km}\);
3. distributes the remainder to the lower cycles;
4. removes only repeated-even-label terms;
5. combines exact integer signs;
6. constructs the predicted \(U\boxtimes U\) and \(P^{(2)}\boxtimes Z\)
   supports independently;
7. compares the two complete integer coefficient maps.

All comparisons pass. At seven points this includes all four inequivalent
splits, 21 pairs, and both gauges; the largest surviving raw tensor support has
351 monomials.

The bounded computation audits the indexing and signs. The anchor-cancellation
and \(Z\)-annihilator arguments above are the all-arity proof.

## Consequence for the emerging operation algebra

The lowering operation now satisfies the first genuine compatibility relation
in the scalar-derived operator algebra:

\[
\boxed{
\operatorname{Cut}_D\circ u
=
(u\boxtimes u)\circ\operatorname{Cut}_D.
}
\]

The qualifications are explicit:

- \(u\) is the amplitude-quotient counit represented by the deletion simplex;
- the equality lives in the tensor product of the two lower physical
  amplitude quotients;
- the raw representative includes the displayed two-pair/all-odd null term;
- changing the gluing gauge changes the representative by a canonical
  deletion-simplex homotopy.

This is stronger than merely obtaining the scalar answer after
transmutation. The lowering map now respects physical composition.

Together with entries 42--44, the structure is

\[
\text{deletion simplex}
\longrightarrow
\text{pairwise trace counit}
\xrightarrow{\ \Delta u=u\boxtimes u\ }
\text{factorization-compatible scalar lowering}.
\]

The next frontier is no longer the tree Cut law. It is whether this resolved
counit admits:

1. a finite-\(\alpha'\) deformation compatible with the shifted string
   integrals;
2. a surface/loop lift compatible with closed-curve state sums;
3. a normal-line-corrected Verdier/Gysin comparison with the adjoint of the
   scalar fusion jet.

## Scope

The theorem uses:

1. the tree scaffold gluing formula;
2. the all-arity low-energy pair transmutation theorem;
3. even-label polarization multilinearity;
4. constant-coefficient differentiation in polarization-type scaffold
   variables.

It is not a finite-string, loop-integrand, or off-shell statement.

## Primary sources

- Backus and Figueiredo, *Surface Gauge Invariance, Soft Limits and the
  Transmutation of Gluons into Scalars*, especially equations (4)--(6) and
  the tree low-energy transmutation theorem:
  <https://arxiv.org/html/2505.17179>.
- Dong, Su, and Yang, *On differential operators for scalar-scaffolded
  gluons*, for the explicit even-label multilinearity and graph-extraction
  support:
  <https://arxiv.org/html/2512.15882v2>.

