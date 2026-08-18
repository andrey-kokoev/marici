# 786 — The Cayley--Menger Boundary Does Not Select the Weighted Ratio at First Exceptional Order

## Question

Entry 783 identifies the source-normalized three-site Cayley--Menger contour
family as the remaining correctly typed candidate for physical weighted
specialization. Does its boundary geometry select the exceptional ratio

\[
t=\frac{X_2}{E_T^2}
\]

that Entries 749--780 left undetermined?

Entry 785 supplies a prior type gate: the real Cayley--Menger inequalities do
not define their own complex continuation along the Bunch--Davies weighted
approach. The calculation below is therefore an algebraic initial-form audit
of the boundary polynomial. It is not yet a strict transform of a transported
physical cycle.

## Frozen coordinate map

On the homogeneous physical locus and normalized chart used by the resolved
connection,

\[
P_1=X_1=1,\qquad
P_2=X_2=y,\qquad
P_3=X_3=u-1-y,\qquad
u=E_T.
\]

The weighted chart at the rational crossing is

\[
y=u^2t.
\]

Keep the loop-edge variables distinct from the external coordinate \(y\) and
write

\[
A=Y_{12}^2,\qquad B=Y_{23}^2,\qquad C=Y_{31}^2.
\]

Substitute these data into the source Cayley--Menger determinant (A.10) of
arXiv:2402.06558v3. The computation is exact over
\(\mathbf Q[u,t,A,B,C]\).

## Initial forms

Symbolic expansion gives

\[
\operatorname{CM}
=-2(A-B)^2
+4u(A-B)(A+1-C)
+u^2M_2+O(u^3),
\]

where the \(t\)-dependent part of the second coefficient is

\[
M_2|_{t\text{-dep}}
=-4t(A-B)(A+1-C).
\]

On the limiting contour boundary \(A=B\),

\[
M_2|_{A=B}=-8A.
\]

Therefore:

1. the special contour boundary is the doubled component
   \[
   A=B;
   \]
2. \(t\) is absent at ordinary normal orders zero and one;
3. its first coefficient is itself divisible by the limiting boundary normal
   \(A-B\).

Equivalently, after resolving the collision by

\[
A-B=u\xi,
\]

the first exceptional equation is independent of \(t\); the weighted ratio
enters one filtration step later.

## Narrow result

\[
\boxed{
\text{The source Cayley--Menger boundary does not select }t
\text{ at the first exceptional collision layer.}
}
\]

This explains why the Bunch--Davies ray in Entries 749 and 780 retains a
continuous normalization parameter even after the physical loop contour is
restored. The contour topology fixes the projective collision direction, but
its first exceptional normal geometry cannot distinguish the points
\(t=ic\).

This is not yet a theorem about the full physical current. The normalized
measure contains a power of the determinant and an external minor. A
distributional boundary or higher normal term could still carry \(t\)-data.
The coefficient comparison map also remains unconstructed.

More basically, by Entry 785 one must first choose admissible paths in the
discriminant complement and compare the Gauss--Manin transports of the real
source cycle. The polynomial calculation is path-independent, but the cycle
class need not be.

## Classification

| datum | status |
|---|---|
| Cayley--Menger carrier boundary | existing source carrier |
| doubled limit \(A=B\) | coefficient/fiber degeneration |
| first exceptional collision equation | \(t\)-independent |
| affine normalization of \(\ell_{\rm exc}\) | not selected |
| new carrier datum | none |

## Next finite falsifier

First implement Entry 785's transport gate: choose two independently
admissible paths from the positive Euclidean chamber to the punctured weighted
neighborhood and compare the transported relative-cycle classes. Only if they
agree, retain the source measure in equation (A.12), including its determinant
power, external \((2,2)\)-minor, orientation, and dimensional prefactor, and
resolve simultaneously

\[
u=0,\qquad A-B=0
\]

and compute the first nonzero exceptional distribution/current, not merely the
boundary polynomial. Test whether its normalized coefficient depends on \(t\).

- If it remains \(t\)-independent, the Cayley--Menger physical-contour route
  cannot normalize \(\ell_{\rm exc}\) at this degeneration.
- If a canonical \(t\)-dependent current appears, derive its map to the
  rank-four exceptional coefficient block before comparing with
  \(\ell_{\rm exc}\).

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/cayley_menger_weighted_physical_pullback.rs`
- `research/benincasa/cayley-menger-weighted-physical-pullback.json`
