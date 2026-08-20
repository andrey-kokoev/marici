# 1088 — The Rank-Twelve Reducer Is Already a Radial Blowup Chart

## Record

The missing rank-twelve connection was previously described as a full
three-variable reconstruction over \((E,X_1,X_2)\).  The frozen source
reducer admits a smaller exact formulation: its variables \((u,v)\) are
already coordinates on the \(X_1\ne0\) chart of the radial blowup.
Homogeneity supplies the radial connection independently.

Sequence claim: `seqclaim-a8ec2f444aa0f587fa62127c`.

## Exact chart identification

The reducer freezes \(X_1=1\) and defines

\[
X_2=\frac{u+v}{2}-1,
\qquad
X_3=\frac{u-v}{2}.
\]

Restoring scale gives

\[
\boxed{
u=\frac{E}{X_1},
\qquad
v=\frac{X_1+X_2-X_3}{X_1}.
}
\]

Thus the existing two-variable source engine is the projective
\(X_1\)-chart of the exceptional plane from Entries 607 and 1087.  Cyclic
copies provide the other site charts.

## Euler weights

Under simultaneous radial scaling of energies and fiber variables,

\[
K_{\rm CM}\mapsto\rho^6K_{\rm CM},
\qquad
K_1\mapsto\rho^5K_1,
\qquad
da\wedge db\mapsto\rho^2 da\wedge db.
\]

For a source class

\[
\frac{N\,da\wedge db}{L_1^{a}L_2^{b}K^{h/2}},
\]

the radial weight is

\[
\deg N+2-a-b-3h.
\]

In the frozen basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9)
\]

the exact weights are

\[
(-3,-2,-2,1,0,-1,0,-1,-2,-1,1,1).
\]

Consequently the radial Euler connection is diagonal in the source frame;
there is no independent off-diagonal radial \(B\)-block to reconstruct.

## Deutsch--Popperian correction

The stronger requirement

\[
\boxed{
\text{first reconstruct a new three-variable }B_E,B_{X_1},B_{X_2}
}
\]

is unnecessary and would overstate the missing datum.  The correctly typed
frontier is

\[
\boxed{
\text{derive the source-normalized two-variable extension class }B_u,du+B_v,dv
\text{ on each projective chart, then add the diagonal Euler connection.}
}
\]

This does not authorize use of Nima's triangle-wall adapter as cosmology
data.  It only narrows the independent source derivation.

## Classification

- radial coordinate: existing flagged normal geometry;
- \((u,v)\): projective exceptional-plane coordinates;
- Euler weights: source coefficient grading;
- radial off-diagonal extension: zero in the homogeneous source frame;
- unresolved datum: exact two-variable marked extension class;
- new carrier datum: none.

## Evidence

- `research/benincasa/check_rank12_radial_chart.rs`;
- `research/benincasa/rank12-radial-chart.json`;
- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- Entries 607, 849--855, 1087, and Nima's event 776.

## Next falsifier

Derive the two-variable extension as a source solution torsor rather than a
chosen primitive witness.  Pull that torsor to each predeclared exceptional
center and test logarithmic normality modulo regular triangular gauge.  Only
after this quotient-level test should a representative connection matrix be
chosen.
