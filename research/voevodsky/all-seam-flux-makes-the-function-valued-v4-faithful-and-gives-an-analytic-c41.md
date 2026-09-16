# All-seam flux makes the function-valued V4 faithful and gives an analytic C41

## Question

Does the Fourier-saturated four-function response presentation admit a genuine analytic inverse to the source presentation?

## Claim boundary

Yes on the Schwartz test core and its transported response image. The all-seam flux component is exactly the source density as a function, so recovery is continuous coordinate projection. This does not repair bounded inversion of the old scalar four-port Hilbert record.

## Forward response map

Define

$$
C_{14}^{\rm resp}g
=
\mathscr R(g)
=(B_g,Q_g,A_g,C_g),
$$

where

$$
B_g(a)=g(a),
\qquad
Q_g(a)=\widehat g(a),
$$

$$
A_g(a)=\int_{-\infty}^ag(x)\,dx,
\qquad
C_g(a)=\operatorname{pv}\int
\frac{e^{-2\pi iax}g(x)}x\,dx.
$$

Give the response target the product test/response topology in which the first component carries the Schwartz topology and the remaining components carry their declared Schwartz, history, and strong-dual response topologies.

## Recovery

Define

$$
C_{41}^{\rm resp}(B,Q,A,C)=B.
$$

On the response image,

$$
C_{41}^{\rm resp}C_{14}^{\rm resp}g
=B_g
=g.
$$

Conversely, if \((B,Q,A,C)=\mathscr R(g)\), then

$$
C_{14}^{\rm resp}C_{41}^{\rm resp}(B,Q,A,C)
=\mathscr R(B)
=(B,Q,A,C).
$$

Thus the two maps are inverse analytic chart transitions on the essential image.

## Why this is not an inserted identity channel

For Volterra history,

$$
J_a(Hg)=g(a).
$$

The function \(B_g:a\mapsto g(a)\) is therefore the seam-flux trace retained simultaneously at every moving seam. It is not an independently appended source copy. Passing from one seam scalar to the complete moving-seam response turns the family of flux evaluations into the original function by point separation.

## Fourier compatibility

The response action \(\mathbb T\) satisfies

$$
C_{14}^{\rm resp}\mathcal F
=\mathbb T C_{14}^{\rm resp}.
$$

Applying the inverse gives

$$
\mathcal F C_{41}^{\rm resp}
=C_{41}^{\rm resp}\mathbb T
$$

on the response image. Hence both forward and reverse fourth-chart edges are quarter-turn equivariant.

## Pyramid consequence

Let the other complete source charts be \(S_2=C_{12}\) and \(S_3=C_{13}\). On their essential images, define

$$
C_{i4}^{\rm resp}=C_{14}^{\rm resp}C_{1i},
\qquad
C_{4i}^{\rm resp}=C_{1i}C_{41}^{\rm resp}.
$$

All triangular and tetrahedral composites reduce strictly through the source chart. Thus the function-valued fourth presentation admits the analytic fillers that failed for the scalar Hilbert record.

## Scope boundary

This theorem uses the topology of complete moving-seam response functions. It does not imply a bounded inverse from:

- one fixed-seam scalar packet;
- the old four-scalar history target;
- the source-forgetting Euler-weighted four-port Hilbert synthesis.

## Disposition

The seam-uniform four-function \(V_4^{\rm resp}\) is a faithful analytic presentation of the source on its essential image, with explicit inverse \(C_{41}^{\rm resp}(B,Q,A,C)=B\). Its presentation pyramid closes strictly and remains compatible with the actual Fourier quarter turn.