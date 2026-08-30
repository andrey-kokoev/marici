# 1944 — The Physical Five-Site (D_4) Divisor Is Boundary-Separated on the Cyclic Slice

## Question

Does Entry 1941's physical logarithmic divisor meet total-energy, edge-soft,
or certified lower-wall support on the frozen cyclic five-site slice?

## Total energy

With (z=t^2),

\[
D_4(z)=1024z^4-16576z^3+95289z^2-231696z+202304.
\]

Total energy is (E_T=5t), hence (E_T=0) implies (z=0).  But

\[
\boxed{D_4(0)=202304\neq0.}
\]

Thus (D_4) does not meet total-energy support on this slice.

## Edge-soft support

For the active representative

\[
g_{12}\mid g_{34}\mid g_5,
\]

the wall equations fix

\[
y_2=-\frac32t,qquad
y_4=-\frac12t,qquad
y_5=-\frac12t.
\]

Any fixed-coordinate soft limit therefore requires (t=0), already excluded
by (D_4(0)\neq0).

The two free coordinates are (y_1,y_3).  The exact elimination packet proves
that (D_4) is coprime to both labelled equations obtained by imposing
(y_1=0) and (y_3=0).

Hence (D_4) meets no edge-soft support on the frozen slice.

## Lower-wall support

The same saturated packet proves that (D_4) is coprime to the complete
certified one-/two-wall discriminant union, including Entry 1870's earlier
triple-wall block used in that lower union.

Therefore

\[
\boxed{
D_4\cap
(E_T\cup\text{edge-soft}\cup\text{certified lower-wall support})
=\varnothing
}
\]

on the frozen cyclic slice.

## Interpretation

The physical logarithmic singularity is an open-stratum coefficient
phenomenon.  There is no supported nearby-cycle specialization of (D_4) to
compute at these boundaries within the current one-parameter family.

This does not exclude intersections in the fully dehomogeneous five-site
family.  Producing those intersections requires an independently frozen
dehomogeneous source and physical current; they must not be inferred from
the univariate polynomial.

## Next falsifier

Either:

1. freeze a dehomogeneous physical five-site family containing the (D_4)
   component and derive its boundary intersections; or
2. remain within the frozen cyclic source and construct the local logarithmic
   monodromy/connection at the open (D_4) root, including its cyclic
   five-occurrence assembly.

The second route is source-complete and therefore preferred.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_d4_boundary_separation.rs`
- `research/benincasa/results/five-site-d4-boundary-separation.json`
- `research/benincasa/results/five-site-cyclic-triple-region-census.json`
- Entries 1875 and 1941
- allocator claim: `seqclaim-dab8899abe43a357ff107f08`

