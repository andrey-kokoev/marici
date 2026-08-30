# 1777 — Disjoint-Cut Five-Site Pairs Produce Six Degree-Six Landau Eliminants

## Frozen source class

Entry 1238 closes the eight shared-cut mixed pair orbits. The remaining mixed
pair class consists of six source-admitted free \(C_5\)-orbits:

\[
q_e=5t+2y_e,
\qquad
q_A=mt+y_i+y_j,
\qquad
e\notin\{i,j\}.
\]

The representatives are

\[
G\!\setminus e_{12}\mid g_3, g_4, g_5, g_{34}, g_{45}, g_{345}.
\]

They account for thirty labelled pairs. No pair was added outside the frozen
180-term OFPT packet.

## Three-focus elimination

Put

\[
x=t^2,qquad a=y_i,qquad b=y_j,qquad c=y_e=-\frac52t,
\qquad p=ab.
\]

For nonzero Landau multipliers, stationarity implies

\[
n_i+n_j=\lambda n_e.
\]

Writing \(q=c\lambda\), the three exact focus-distance equations reduce to
two cubic polynomials in \(p\). Their \(6\times6\) Sylvester resultant was
computed exactly over

\[
\mathbb Q(\sqrt5)[x]
\]

using the source routing norms from Entry 1234.

## Result

Every raw resultant contains the universal total-energy factor

\[
x=t^2.
\]

After removing that factor, all six source orbits retain a nonconstant
degree-six polynomial in \(x\). Exact factorization does not reduce these
polynomials to Entry 1235's one-wall threshold factors.

Thus

\[
\boxed{
6\text{ disjoint-cut orbits}
\longrightarrow
6\text{ degree-six anomalous-threshold candidates}.
}
\]

## Classification and remaining gate

These eliminants are generated from two already frozen marked denominators and
the frozen routing Gram data. If they survive saturation, they are new
coefficient/period singular support over the existing carrier—not new carrier
incidence generators.

This entry records exact elimination, not yet a Landau-support theorem. The
next finite falsifier must:

1. saturate by both Landau multipliers and all forbidden zero-distance
   branches;
2. reconstruct a nondegenerate critical point over the generic point of every
   surviving irreducible factor;
3. test whether cyclic conjugate representatives produce the same field-norm
   divisor.

Failure at the first two gates retracts the corresponding factor as an
elimination artifact.

## Durable evidence

- exact Symbolica eliminator:
  `research/benincasa/marici-gm/src/bin/five_site_disjoint_mixed_pair_landau.rs`;
- capture and structural checker:
  `research/benincasa/checkers/capture_five_site_disjoint_mixed_pair_landau.py`;
- exact packet:
  `research/benincasa/results/five-site-disjoint-mixed-pair-landau.json`;
- convention note:
  `research/benincasa/five-site-disjoint-mixed-pair-landau.md`;
- allocator claim: `seqclaim-5a33b07046c56aaaeb641874`.

