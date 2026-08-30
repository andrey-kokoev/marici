# 1872 — The First Region-Only Triple Produces a Second Quartic Candidate

## Representative

Entry 1871 isolates four generically nonsoft (g+g+g) representatives that
admit pure-(t) wall elimination. Take

\[
g_{1234}\mid g_{234}\mid g_{2345}.
\]

Its walls fix

\[
y_1=y_4=-\frac32t,
\qquad
y_5=-\frac52t,
\]

leaving

\[
x=y_2^2,
\qquad
v=y_3^2.
\]

## Exact elimination

The Kummer differences solve the three routing coordinates over
\(\mathbb Q(\sqrt5)[x,v,z]\), where (z=t^2). The first and fifth cover
equations then give two source-derived equations

\[
F(x,v,z)=0,
\qquad
G(x,v,z)=0.
\]

The checker computes

\[
R(v,z)=\operatorname{Res}_x(F,G)
\]

and the critical-value discriminant

\[
\operatorname{Res}_v(R,\partial_vR).
\]

After taking the quadratic-field norm and removing its rational unit, the
result is

\[
\boxed{
D_{3,\mathrm{reg}}(z)
=2016064-5586608z+5762041z^2-2628992z^3+446464z^4.
}
\]

## Finite hostile checks

At the good prime (2147483647), the quartic is:

- squarefree;
- coprime to the (y_2=0) elimination;
- coprime to the (y_3=0) elimination;
- coprime to all eight Entry 1866 blocks;
- coprime to Entry 1870's certified triple-wall quartic.

Thus the region-only triple supplies a second new nonsoft quartic candidate,
not a re-expression of the current degree-87 union.

## Scope

This is an exact iterated-resultant candidate, not yet a saturated Landau
divisor. The three source wall multipliers have not been proved nonzero on
the generic quartic. The selected physical period may also cancel a
geometrically admissible factor.

Accordingly, the candidate denominator degree is not yet promoted from 87 to
91.

## Next falsifier

Compute the source-ordered wall multipliers on the repeated-root scheme and
test whether each multiplier-zero elimination is coprime to
(D_{3,\mathrm{reg}}). A vanishing multiplier rejects the quartic as a
genuine three-wall component; three nonvanishing multipliers certify it.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_pilot.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-pilot.json`
- allocator claim: `seqclaim-b07ac7c882e871d62119cab2`
- epistemic event: `ev-000000002226-2e5ad25d-4f1b-4ccc-b3c7-01f08017eea6`
