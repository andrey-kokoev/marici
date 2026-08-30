# Bordered prime shift derives the Euler factor before scalar aggregation

## Question

The universal rank-one determinant bridge is nonexplanatory because it begins
with the aggregated scalar.  Can any determinant block instead be derived
forward from the labelled theta arithmetic constructors?

## Prime multiplication and theta synthesis

Let \(\mathcal C_{\mathrm{fin}}\) have basis \(e_n\), and define prime
multiplication by

\[
V_pe_n=e_{pn}.
\]

Let theta synthesis be

\[
Te_n=\phi_n.
\]

The exact translate law

\[
\phi_{pn}(u)
=
p^{-1/2}\phi_n(u+\log p)
\]

gives the source intertwiner

\[
TV_p=p^{-1/2}\tau_pT,
\]

where \(\tau_p\) translates the archimedean coordinate by \(\log p\).
Thus \(V_p\) is not an invented spectral shift; it is the labelled operator
implementing the theta scale constructor.

## One valuation chain

Fix a primitive label not divisible by \(p\).  Its valuation chain has basis

\[
e_0,e_1,\ldots,e_N,
\]

where \(e_k\) represents multiplication by \(p^k\).  Let

\[
Se_k=e_{k+1}
\]

for \(k<N\), with \(Se_N=0\).  Define

\[
D_N(q)=I-qS.
\]

Because \(S\) is nilpotent,

\[
D_N(q)^{-1}
=
I+qS+\cdots+q^NS^N
\]

and

\[
\det D_N(q)=1.
\]

The bulk shift alone therefore has a trivial determinant.  It cannot produce
an Euler factor.

## Source boundary ports

Let \(e_0\) be the primitive vacuum port and let \(\ell_N\) be the valuation
augmentation

\[
\ell_N(e_k)=1.
\]

Form the bordered source matrix

\[
\mathcal M_N(q)
=
\begin{pmatrix}
D_N(q)&e_0\\
\ell_N&0
\end{pmatrix}.
\]

Its Schur complement is derived from the shift system:

\[
\det\mathcal M_N(q)
=
-\ell_ND_N(q)^{-1}e_0
=
-\sum_{k=0}^Nq^k.
\]

Hence

\[
\det\mathcal M_N(q)
=
-\frac{1-q^{N+1}}{1-q}.
\]

For \(q=p^{-s}\), the infinite-chain limit in \(\Re s>0\) is the negative
local Euler factor

\[
-\frac1{1-p^{-s}}.
\]

No scalar Euler entry was inserted.  It emerged by eliminating a
source-derived valuation chain with its primitive and augmentation boundary
ports retained.

## Why the boundary is essential

The infinite unilateral shift is an isometry, so \(qS\) is not trace class
and \(I-qS\) has no ordinary Fredholm determinant of the desired kind.  The
Euler factor is instead a boundary matrix coefficient

\[
\ell(I-qS)^{-1}e_0.
\]

Moreover, \(\ell\) is distributional relative to the ordinary unweighted
\(\ell^2\) chain.  This identifies the primitive current concretely: it is the
augmentation boundary needed to read the whole valuation orbit.

The bordered determinant packages that distributional readout without
pretending it belongs to the bulk Hilbert determinant.

## Why this is better than the universal rank-one bridge

Every entry of \(\mathcal M_N\) is fixed before the Euler scalar is computed:

- \(S\) comes from prime multiplication;
- \(q=p^{-s}\) comes from the Mellin character;
- \(e_0\) is the primitive valuation boundary;
- \(\ell_N\) is the source augmentation over allowed powers.

The determinant identity is a consequence of elimination.  A hostile scalar
factor cannot be inserted without adding or changing a labelled block or
boundary port.

This is the first determinant construction in the programme that passes the
derivational-direction test.

## Remaining obstructions

The local construction does not prove RH.

1. Finite chains have numerator zeros \(q^{N+1}=1\) that disappear in the
   convergent infinite-chain chamber.
2. The infinite augmentation port requires a rigged or relative determinant
   topology.
3. Products over primes diverge at the primitive and prime-square levels and
   require their typed currents.
4. The archimedean rank-two continuation boundary must be coupled before its
   compression to \(1/2\).
5. No global off-seam kernel exclusion has yet been derived.

Thus the next construction is the finite-Euler direct sum of the bordered
prime blocks together with the two archimedean boundary components.  Its
relative determinant should reproduce the completed finite Euler
approximant, and its reciprocal graph should then be audited for a
source-derived Green identity.

## Falsifier

The construction fails globally if the required primitive, square, or
archimedean ports cannot be assembled into a cutoff-compatible determinant
line.  A scalar regularization that discards those ports is not an acceptable
repair.

At finite cutoff, the sharp audit is exact: every determinant coefficient must
arise from the shift and declared boundary rows.  Any fitted entry containing
an Euler product or completed theta scalar closes the proposed derivation.

## Result

A bordered prime-valuation shift derives each finite Euler factor from
source-local labelled transport before scalar aggregation.  The arithmetic
determinant bridge is therefore plausible, but it is intrinsically a relative
boundary determinant rather than an ordinary bulk Fredholm determinant.
