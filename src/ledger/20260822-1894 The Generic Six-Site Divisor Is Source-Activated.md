# Entry 1894 — The Generic Six-Site Divisor Is Source-Activated

## Physical gate

Entry 1893 leaves a generic nonsoft ordinary node on (D_6(k,z)=0).
Test the exact real point

\[
k=-\frac12,
\qquad
(z,x,v,w)=
\left(
\frac{2891}{842},
\frac{5899}{842},
\frac{1129}{421},
\frac{2207}{421}
\right).
\]

All four squared coordinates are positive.

## Source-ordered wall multipliers

Before identifying the three even edge squares, retain the six labelled
variables (s_i=y_i^2).  The conormal

\[
(\partial_{s_5}G)dF-(\partial_{s_5}F)dG
\]

vanishes in the free directions (s_1,s_3,s_5).  Its ordered components in
the active wall directions (s_2,s_4,s_6), evaluated on (D_6), are

\[
\left(
-\frac{17885}{107776},
-\frac{35}{6736},
-\frac{11025}{107776}
\right).
\]

Choose

\[
t=\sqrt{z}>0,
\qquad
y_2=y_4=y_6=-t.
\]

Passing from (ds_{2i}) to (dy_{2i}) multiplies every component by the
same negative factor (-2t).  Hence the three projective source-wall
multipliers have signs

\[
\boxed{(+,+,+)}.
\]

No multiplier vanishes.

## Frozen-source residue

On the homogeneous site-energy sheet (X_i=t), the nine source completions
from Entry 1884 evaluate without fitting:

- each (G-e_{23},G-e_{45},G-e_{61}) equals (4t);
- each (g_{1234},g_{1256},g_{3456}) equals (2t);
- the six singleton source factors reduce pairwise to the three positive odd
  loop energies.

The first six completion pairs contribute (1/(4t\,2t)), and the final
three contribute (1/(2t\,2t)).  Thus, in the common positive prefactor,

\[
\operatorname{Res}_{g_{12}=g_{34}=g_{56}=0}\Psi_6
=
6\frac1{8t^2}+3\frac1{4t^2}
=
\boxed{\frac{3}{2t^2}}.
\]

The nine terms reinforce rather than cancel.

## Bunch--Davies pairing

Under independent positive site regulators,

\[
X_i\longmapsto X_i-i\epsilon_i,
\qquad \epsilon_i>0,
\]

the three active walls acquire imaginary parts

\[
-(\epsilon_1+\epsilon_2),
\qquad
-(\epsilon_3+\epsilon_4),
\qquad
-(\epsilon_5+\epsilon_6).
\]

Their pairing with the positive multiplier normal is strictly negative on
the complete positive regulator cone.  No regulator hierarchy is needed.
Since the transverse singularity is an ordinary real node and the local
source residue is nonzero,

\[
\boxed{
|\langle\Gamma_{\rm BD},\delta_{D_6}\rangle|=1.
}
\]

## Narrow result

\[
\boxed{
D_6(k,z)=0
\text{ supports a source-normalized, Bunch--Davies-activated six-site
coefficient singularity.}
}
\]

This is coefficient support on the already frozen occurrence-labelled
triple incidence.  No new Carrier cell is required.

The remaining question is specialization: does this physical generic branch
produce Entry 1888's Cartier excess at (k=0), or merely meet that vertical
excess at an isolated point?

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_iepsilon_pairing.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-iepsilon-pairing.json`
- allocator claim: `seqclaim-542c74497be238249f28f72e`
- epistemic event: `ev-000000002259-8de614a9-81e1-49e4-9a04-d84fb7734c4e`
