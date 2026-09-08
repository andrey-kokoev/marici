# 1634 — Virtual-Cut Balance Cancels the Production Moment-Filtration Shift

## Apparent mismatch

Entry 1632 shows that the positive production Cut alone acts with degree shift two:

\[
\mathbb M_{\le D+2}\to\mathbb M_{\le D}.
\]

Entry 1633 adds the source virtual/no-production cell.  Test whether their sum still requires a shifted tower or descends strictly at each moment degree.

## Trace-balanced generator

For an observed creation jump \(L=a^\dagger\), the adjoint generator is

\[
\mathcal L^\dagger(O)
=
a O a^\dagger
-\frac12\{aa^\dagger,O\}.
\]

The two displayed terms separately have principal degree \(D+2\) on a degree-\(D\) observable.  Their principal symbols agree and cancel.

For the number-moment subalgebra,

\[
\boxed{
\mathcal L^\dagger f(N)
=(N+1)\bigl[f(N+1)-f(N)\bigr].
}
\]

If \(\deg f=D\), then

\[
\deg\mathcal L^\dagger f\le D.
\]

For \(D>0\), the leading term is

\[
D N^D.
\]

The checker verifies every degree through \(32\).

## Narrow result

\[
\boxed{
\text{Production and virtual cells are individually shifted, but their source-balanced sum is a strict same-level moment map on number moments.}
}
\]

Consequently the restriction squares commute:

\[
\operatorname{res}_{\le D}
\circ\mathcal L_{D+2}
=
\mathcal L_D
\circ\operatorname{res}_{\le D}.
\]

No derived coherence cell is needed on this tested subalgebra.

## Qualifications

The principal-symbol cancellation holds generally for a linear Kraus operator, but the exact lower-degree ordering terms have only been audited here on the number-moment basis.  The full Weyl basis \(Q^mP^n\) remains the next finite test.

## Architectural consequence

This is a concrete example of why the complete comparison object matters:

\[
\text{positive Cut cell alone}
\neq
\text{normalized physical channel}.
\]

The full source pair restores both trace balance and strict filtration behavior.  The carrier already contains the two typed cells; the cancellation is coefficient-level coherence.

## Durable artifacts

- `research/benincasa/checkers/trace_balanced_moment_tower.rs`
- `research/benincasa/results/trace-balanced-moment-tower.json`
- `research/benincasa/trace-balanced-moment-tower.md`

## Next falsifier

Compute \(\mathcal L^\dagger\) on every Weyl monomial \(Q^mP^n\) through total degree eight.  Verify exact degree preservation and commutation with the CCR quotient.  Any surviving degree-raising term is the first obstruction to a strict full phase-space moment tower.