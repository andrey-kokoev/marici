# 2276 — Generic Tensor Projection Is Forced to Lose Rank on the Existing Gram Wall

## Frozen generic orientation

Retain Entry 2272's spectral Gaussian source, but let the tensor momentum be

\[
q=(a,b,c)
\]

relative to the equilateral hard-momentum plane \(z=0\).  Use the transverse
frame

\[
u=(-b,a,0),
\qquad
v=(-ac,-bc,a^2+b^2).
\]

The three hard momenta are

\[
p_1=(2,0,0),
\quad
p_2=(-1,\sqrt3,0),
\quad
p_3=(-1,-\sqrt3,0).
\]

For each occurrence, form the two traceless tensor contractions in this frame
and retain an independent positive spectral weight \(w_i\).  No relation among
the weights is used in the symbolic determinant.

## Exact factorization

After removing common nonzero polarization-frame normalizations, the
determinant contains the factor

\[
\boxed{c=q\cdot\widehat n},
\]

where \(\widehat n\) is the hard-triangle normal.  In the current polynomial
chart the complete expression is

\[
-4\sqrt3\,c(a^2+b^2)^2(a^2+b^2+c^2)\,B,
\]

where \((a^2+b^2)^2(a^2+b^2+c^2)\) is polarization-frame scaling and

\[
\begin{aligned}
B={}&2\sqrt3ab\,w_1(w_2-w_3)
+3a^2w_2w_3\\
&+b^2(2w_1w_2+2w_1w_3-w_2w_3)\\
&+2c^2(w_1w_2+w_1w_3+w_2w_3).
\end{aligned}
\]

The chart factors must not be interpreted as physical support: in particular,
the normal slice \(a=b=0\) is faithful by Entry 2272 and merely requires the
other polarization chart.

## Geometric rank loss

On

\[
c=0,
\]

the tensor momentum lies in the hard-momentum plane.  Projecting all three
hard momenta onto \(q^\perp\) leaves only one direction inside that plane.
Consequently all traceless tensor evaluations are collinear and the
scalar-plus-two-polarization matrix has rank at most two.

This is exactly the Gram/projection wall

\[
\boxed{
q\cdot(p_1\times p_2)=0.
}
\]

It is an existing kinematic support condition, not a new Carrier incidence
generator.

## Residual falsifier

Away from the Gram wall, any additional rank loss must satisfy

\[
B=0
\]

after imposing the source weights

\[
w_i=\frac1{2+|p_i+q|}>0
\]

up to a common positive normalization.  A bounded physical grid found
\(B>0\), with minimum approximately \(1.49\times10^{-2}\), but this is only
discovery evidence.  The next theorem must prove positivity of \(B\) or
produce an exact positive-energy counterexample.

## Verification

`research/benincasa/marici-gm/src/bin/generic_tensor_projection_determinant.rs`
derives the symbolic factorization with Symbolica and performs the bounded
physical-weight scan.
