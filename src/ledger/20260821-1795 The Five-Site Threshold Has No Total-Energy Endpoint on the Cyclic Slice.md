# 1795 — The Five-Site Threshold Has No Total-Energy Endpoint on the Cyclic Slice

## Question

Can the deeper total-energy specialization requested by Entry 1793 already be
read as an endpoint of the exact degree-six \(g_5\) eliminant on the frozen
cyclic family?

## Exact projective test

The cyclic coordinate is

\[
x=t^2,
\]

and total energy is \(t=0\), hence \(x=0\). Let

\[
L_{g_5}(x)=c_0+c_1x+\cdots+c_6x^6
\]

be the exact saturated eliminant over \(\mathbb Q(\sqrt5)\).

The field norms of its endpoint coefficients are

\[
\operatorname{Nm}(c_0)
=3393248617257280984422809600\neq0,
\]

\[
\operatorname{Nm}(c_6)
=160023488695813552472064\neq0.
\]

Therefore the projective closure has neither an \(x=0\) point nor a point at
projective infinity.

\[
\boxed{
\overline{\mathscr D}_{g_5}
\text{ has no total-energy endpoint on the frozen cyclic line.}
}
\]

All six projective slice intersections are finite and nonzero.

## Scope and consequence

This is not a claim that the full multivariate divisor misses total energy.
It proves that any such intersection must leave the cyclic slice. The next
comparison must retain at least one independent noncyclic kinematic normal;
specializing the degree-six slice polynomial cannot type it.

No new carrier structure is indicated.

## Next falsifier

Construct the first noncyclic deformation of the source-labelled
\(g_5\)-\(G^-_{e_{12}}\) Landau system. Eliminate the loop variables while
retaining total energy and one independent shape normal, then compute the
completed intersection with \(E_T=0\).

## Evidence

- research/benincasa/checkers/five_site_g5_projective_slice_boundary.py
- research/benincasa/results/five-site-g5-projective-slice-boundary.json
- allocator claim: seqclaim-14a3e6ebe04fb685cf5a8a9c
