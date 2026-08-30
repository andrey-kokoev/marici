# The earliest missing Adams constructor is now a two-lift Green identity

## Scope reset

The intensive-order audit removes a topology false positive for arbitrary
Adams iteration. It does not construct the first Adams edge. The earliest
missing arrow remains

\[
\text{global Laplace-rigged history}
\longrightarrow
\text{relative Green/Stokes mixed form}.
\]

All downstream determinant, holonomy, and order-semigroup calculations remain
conditional on this arrow.

## Solved input data

For each prime \(p\), with \(L=\log p\), the source supplies:

- primitive incidence at \(L\) with coefficient
  \(p^{-1/2-\sigma-it}\);
- square incidence at \(2L\) with coefficient
  \(\frac12p^{-1-2it}\);
- adjacent scale history on \([L,2L]\);
- raw boundary multiplier
  \[
  D_p=M_{W_{2L}-W_L},
  \qquad
  \|D_p\|\le1;
  \]
- finite valuation/Fock prime labels and grade change \(1\to2\);
- strong truncation convergence of the listed currents in suitable
  exponential dual rungs.

Thus neither local propagation nor diagonal prime summability is missing.

## Exact unknown

Construct independently typed endpoint lifts

\[
L_{P,p}:
\mathcal H_{\mathrm{hist},p}\to\mathcal P_{\sigma,p},
\qquad
L_{Q,p}:
\mathcal H_{\mathrm{hist},p}\to\mathcal Q_p
\]

from the primitive and square source channels, and prove the relative
Green/Stokes identity

\[
b_p(x,y)
=
\left\langle
L_{Q,p}^{*}y,\,
D_pL_{P,p}^{*}x
\right\rangle.
\]

The factorization must be derived from integration by parts on the comoving
history, not fitted from the already known rank-one boundary block.

## Minimal theorem

On a common source core, prove:

1. \(L_{P,p}\) and \(L_{Q,p}\) are defined by the source endpoint traces;
2. their ranges lie in the distinct exponential and tempered riggings;
3. the Green identity yields the oriented difference \(W_{2L}-W_L\);
4. both lifts annihilate the appropriate Green radicals;
5. the mixed form is closable;
6. endpoint reversal sends \(b_p\) to the reciprocal adjoint character;
7. the lifts preserve the finite prime idempotents;
8. for some \(\theta<1/2\) and fixed \(m\),
   \[
   \|L_{Q,p}\|,\|L_{P,p}\|
   \le Cp^\theta(\log p)^m.
   \]

The last bound is generous because \(\|D_p\|\le1\).

## Automatic global consequence

If the eight items hold and completion/sewing extends the prime idempotents,
then

\[
B_\sigma
=
\bigoplus_p
p^{-1/2-\sigma}
\left(\frac12p^{-1}\right)
L_{Q,p}D_pL_{P,p}^{*}
\]

converges absolutely through \(\sigma=0\). Indeed,

\[
\sum_p
p^{-3/2-\sigma+\theta}(\log p)^m
\]

converges uniformly for \(\sigma\ge0\) whenever \(\theta<1/2\).

Therefore no separate cross-prime estimate is needed once label-preserving
completion is proved.

## Earliest falsifiers

The irreducible hostiles are:

- correct endpoint traces but no Green identity;
- a fitted factorization disagreeing with the independent lifts;
- failure of radical annihilation;
- correct scalar Stokes value with wrong adjoint orientation;
- finite lift bounds with exponent \(\theta\ge1/2\);
- prime-labelled finite lifts whose closure smears labels;
- a closable local form whose global direct sum has no common dense adjoint
  domain.

## Research frontier

The first Adams edge has contracted to two source formulas and one identity:

\[
L_{P,p},
\qquad
L_{Q,p},
\qquad
b_p=L_{Q,p}D_pL_{P,p}^{*}.
\]

The next work must extract those endpoint trace maps from the source
Green/history construction. Further generic completion refinements should be
deferred until this factorization exists.
