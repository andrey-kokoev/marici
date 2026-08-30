# The Additive and Multiplicative Vacua Are Disjoint Half-Density Sectors

## Canonical finite half-density

Under additive Haar measure \(\mu_+\) on
\(\widehat{\mathbb Z}\), the finite multiplicative density is

\[
W_Q
=
\frac{Q}{\varphi(Q)}
\mathbf 1_{(x,Q)=1}.
\]

Its canonical half-density vector is

\[
h_Q=\sqrt{W_Q}
=
\sqrt{\frac{Q}{\varphi(Q)}}
\mathbf 1_{(x,Q)=1}.
\]

Since \(\int W_Qd\mu_+=1\),

\[
\|h_Q\|_{L^2(\mu_+)}=1.
\]

Thus every finite additive--multiplicative comparison has a normalized
half-density representative.

## Vacuum overlap

The additive vacuum is the constant function one. Its overlap with the
multiplicative half-density is

\[
\langle1,h_Q\rangle
=
\sqrt{\frac{\varphi(Q)}{Q}}.
\]

For primorial cutoffs,

\[
\langle1,h_{Q_y}\rangle
\sim
\frac{e^{-\gamma/2}}{\sqrt{\log y}}
\longrightarrow0.
\]

The two normalized vacua become orthogonal at infinite conductor.

## Weak escape against every finite observer

Let \(g\) be a cylinder function factoring through a fixed modulus \(M\).
For every squarefree \(Q\) divisible by \(M\), Chinese remainder
factorization gives

\[
\langle g,h_Q\rangle
=
\sqrt{\frac{\varphi(Q)}{Q}}
\frac1{\varphi(M)}
\sum_{\substack{a\bmod M\\(a,M)=1}}\overline{g(a)}.
\]

The finite unit-residue average is fixed, while the prefactor tends to zero.
Hence

\[
h_Q\rightharpoonup0
\]

against the dense family of finite-conductor cylinder observables. Since
\(\|h_Q\|_2=1\), no strong additive-Hilbert limit exists.

## Infinite-product interpretation

Locally,

\[
h_p
=
\frac{\mathbf 1_{\mathbb Z_p^\times}}{\sqrt{1-p^{-1}}},
\qquad
\langle1,h_p\rangle=\sqrt{1-p^{-1}}.
\]

The global vacuum overlap is the product of the local overlaps:

\[
\prod_p\sqrt{1-p^{-1}}=0.
\]

Therefore the additive reference vacuum and the multiplicative unit vacuum
belong to disjoint infinite-product sectors. Finite tensor comparisons exist,
but their vacuum overlap vanishes in the restricted-product limit.

## Consequence for the carrier

The half-density is not a vector that was accidentally omitted from additive
\(L^2\). The global multiplicative vacuum lives in a different
representation. The correct bridge is a correspondence or bimodule carrying:

1. the additive Haar representation;
2. the multiplicative Haar representation;
3. the finite half-density intertwiners;
4. the relative determinant line recording their vanishing overlap.

One archimedean factor cannot turn the zero infinite product into an ordinary
nonzero overlap. The archimedean half-density must participate in a
renormalized relative construction with the prime-square boundary line.

## Meaning for the two-sector picture

The programme's two sectors are now mechanically distinct:

- the additive sector supports theta summation and Poisson transport;
- the multiplicative sector supports Euler connectedization and idelic Haar.

The critical seam is the unitary normalization of the correspondence between
them. It is not an internal axis of one common raw Hilbert representation.

This explains why repeated attempts to add a comparison vector produced weak
escape: the desired object is an arrow between sectors, not a state inside
either sector.

## Remaining RH theorem

The measure-class and half-density architecture is source-derived, but it
still does not prove zero confinement. The remaining theorem is:

> The renormalized additive--multiplicative correspondence sends the formal
> connected prime current to a tempered relative boundary state in each open
> spectral sector.

That theorem must be stated in the correspondence topology. A norm estimate
inside additive \(L^2\) is now known to be ill-typed.

## Falsifier

A proposed construction fails if it:

- asserts a nonzero global product of the local vacuum overlaps;
- places both vacua in the same incomplete infinite tensor product;
- treats weak convergence of \(h_Q\) to zero as norm convergence;
- or represents the global half-density by a bounded additive-Hilbert vector.

