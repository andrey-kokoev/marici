# 1866 — The Cyclic Five-Site Landau Eliminants Give a Degree-Eighty-Three Candidate Bound

## Frozen object

Use the source-defined cyclic physical period of Entry 1234,

\[
\Pi_{C_5}^{\rm cyc}(t),
\qquad z=t^2.
\]

No differential operator or master basis is fitted. The calculation compiles
only Landau eliminants already derived from the frozen OFPT integrand and
physical routing geometry.

## Exact factor inventory

The rational one-wall factor has degree seven in \(z\):

\[
z(z-2)(16z-17)(16z^2-44z+29)(81z^2-189z+109).
\]

The physical region-pair norm of Entry 1831 has degree four:

\[
1121-18540z+94932z^2-174960z^3+104976z^4.
\]

For each of the six disjoint mixed-pair orbits, the saturated eliminant is a
degree-six polynomial over \(\mathbb Q(\sqrt5)\). Exact conjugate
multiplication in Symbolica produces six rational degree-twelve field norms.
Their total degree is seventy-two.

At the good prime

\[
p=2147483647,
\]

the eight factor blocks pass eight square-freeness gcd tests and all
twenty-eight pairwise coprimality tests. A nonconstant rational gcd would
remain nonconstant at every good reduction, so this proves that the displayed
blocks are square-free and pairwise coprime over \(\mathbb Q\).

Therefore the raw product has degree

\[
\boxed{7+4+6\cdot12=83}
\]

in \(z=t^2\).

## Interpretation

This is the first finite, source-derived candidate denominator bound for a
scalar Picard--Fuchs search on the frozen five-site slice. It is substantially
more restrictive than allowing an arbitrary rational denominator.

It is not yet the exact singular polynomial. In particular, the calculation
does not prove:

- absence of factors from higher compatible Landau subsets;
- that every resultant factor survives saturation by all boundary and
  nonstationary components;
- that every surviving Landau factor acts nontrivially on the selected period;
- any bound on the differential-operator order.

## Narrow result

\[
\boxed{
\deg_z D_{\rm cand}=83
}
\]

for the presently certified one- and two-wall eliminant inventory. This is a
coefficient-singularity candidate over the existing carrier, not a new
carrier divisor theorem.

## Next falsifier

Process the compatible three-wall orbit representatives and saturate their
source ideals against boundary and nonstationary components. Only the
resulting square-free union may be used as the denominator ansatz for exact
creative telescoping.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_landau_candidate_bound.rs`
- `research/benincasa/results/five-site-cyclic-landau-candidate-bound.json`
- `research/benincasa/results/five-site-cyclic-one-wall-landau.json`
- `research/benincasa/results/five-site-disjoint-mixed-pair-landau.json`
- `research/benincasa/results/five-site-region-pair-threshold-polynomial.json`
- allocator claim: `seqclaim-0239dab89b2e128530af727f`
