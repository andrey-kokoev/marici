# The Gauge Fitting Conic Has Simple Transverse Multiplicity in the Tested Presentation

**Date:** 2026-08-17  
**Status:** finite-field exact-lift result; generic symbolic statement still open  
**Depends on:** Entries 388--389

## Hard-to-vary claim

For a generic point of
\[
C_{\rm fit}: X_1X_2-E_T^2=0,
\]
the frozen exact-lift presentation has a maximal-rank minor whose first normal
jet is nonzero. Thus the rank-one special-fiber enhancement has Fitting
multiplicity one in the tested presentation.

## Frozen test

On the affine patch
\[
v=2u^2-u+2,
\]
freeze the exact-form degrees 8 and 10 and the source-defined presentation.
At the neighboring fiber \(v+1\), row reduction selects a square maximal-rank
minor. The same rows, monomials, and columns are then specialized to the conic.

If \(r\) and \(\ell\) span the right and left null lines of the specialized
minor \(M_0\), test
\[
\ell^T(\partial_v M)_0r.
\]
No rows, columns, support factors, or carrier cells are fitted after seeing the
answer.

## Result

At
\[
u=3,5,7,11,19,37
\]
and at both exact-form degrees, the selected minor loses exactly one rank on
the conic. All twelve transverse pairings are nonzero in
\(\mathbb F_{2305843009213693951}\).

The derivative was reconstructed independently at interpolation orders 12 and
16. The two values agree in all twelve cases. The previous 196-fiber conic
sweep and 392 neighboring-fiber controls remain unchanged after refactoring.

Hence
\[
\boxed{C_{\rm fit}\text{ has simple transverse Fitting multiplicity in every tested fiber}.}
\]

Equivalently, for each tested local minor,
\[
\det M=(X_1X_2-E_T^2)U
\]
with \(U\) nonzero at the sampled conic point.

## Interpretation

This rules out the immediate higher-normal-order alternative for the conic.
The extra class is a first-order special-fiber class of the relative
coefficient presentation, unlike the algebraic quartic \(\mathcal Q\), whose
ordinary total-energy deformation begins at second order.

This strengthens H2 without adding a carrier stratum:
\[
\text{shared carrier and calculus}
+
\text{sector-specific relative coefficient presentation}
+
\text{simple internal Fitting divisor}.
\]

## Epistemic boundary

The result is exact over one large finite field and stable across two exact-form
degrees, but it is not a symbolic proof of the global Fitting ideal. It does not
show that the conic is the only residual component, identify the induced
rank-one flat subquotient, or determine whether \(\mathcal Q\) belongs to its
connection or to the extension class.

## Next falsifier

Compute the connection induced on the conic-only kernel class. Test whether its
flat saturation is rank one and whether its nonintegral singular support
contains \(\mathcal Q\). If not, compute the extension class between this
algebraic direction and the elliptic quotient. No new carrier datum is
admissible unless both coefficient mechanisms fail.

## Evidence

- `research/benincasa/gauge-fitting-conic-transverse-jet.json`
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`
