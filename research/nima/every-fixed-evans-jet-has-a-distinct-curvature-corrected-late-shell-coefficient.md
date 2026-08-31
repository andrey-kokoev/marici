# Every fixed Evans jet has a distinct curvature-corrected late-shell coefficient

## Question

What is the correct first relative correction for an arbitrary fixed Evans
parameter jet on a late prime shell?

## Claim boundary

The coefficient depends on both the jet order and the Evans parameter. It is
not the jet-independent \(-1/2\) previously stated. The formula below follows
from a two-variable endpoint expansion for the completed theta tail. It is
uniform only for bounded jet order and compact parameter sets.

## Tail scaling

Let

\[
 L=\Lambda(a)=-\frac{\Phi'(a)}{\Phi(a)}
\]

and

\[
 \varepsilon=\frac{\Lambda'(a)}{L^2}
 =\frac2L+O(L^{-2}).
\]

For local displacements of size \(L^{-1}\),

\[
 \frac{\Phi(a+y/L)}{\Phi(a)}
 =e^{-y}
 \left[1-\frac{\varepsilon}{2}y^2+O(L^{-2})\right].
\]

## Endpoint jet

The lower-end endpoint jet is

\[
 \partial_z^jI^{({\rm end})}(z)
 =(-1)^j\Phi(a)
 \int_0^\infty s^je^{-zs}\Phi(a+s)\,ds.
\]

The gamma moments give

\[
 \partial_z^jI^{({\rm end})}(z)
 =(-1)^j
 \frac{j!\Phi(a)^2}{L^{j+1}}
 \left[
 1-\dfrac{(j+1)(z+j+2)}{L}
 +O(L^{-2})
 \right].
\]

The curvature term uses

\[
 \frac{\int_0^\infty y^{j+2}e^{-y}\,dy}
 {\int_0^\infty y^je^{-y}\,dy}
 =(j+1)(j+2).
\]

## Ordinary jet

Write the two local variables as

\[
 x-a=\frac yL,
 \qquad
 r-x=\frac vL.
\]

The ordinary jet is a double endpoint integral with leading density

\[
 e^{-2y-v}v^j.
\]

Its first correction contains

\[
 -\frac{zv}{L}
 -\frac{\varepsilon}{2}
 \left[y^2+(y+v)^2\right].
\]

Under the normalized product moments,

\[
 \mathbb E\left[y^2+(y+v)^2\right]=(j+2)^2.
\]

Consequently

\[
 \partial_z^jI^{(0)}(z)
 =(-1)^{j+1}
 \frac{j!\Phi(a)^2}{2L^{j+2}}
 \left[
 1-\dfrac{(j+1)z+(j+2)^2}{L}
 +O(L^{-2})
 \right].
\]

## Combined jet

Through relative order \(L^{-1}\), only the leading ordinary term enters the
endpoint-scaled bracket. Therefore

\[
 \partial_z^j
 \left(I^{({\rm end})}+I^{(0)}\right)
 =(-1)^j
 \frac{j!\Phi(a)^2}{L^{j+1}}
 \left[
 1-\dfrac{(j+1)(z+j+2)+1/2}{L}
 +O(L^{-2})
 \right].
\]

For \(j=0\), this reduces to the corrected coefficient \(z+5/2\).

## Necessary reciprocal-linking law

Under unit ordinary and endpoint port coefficients, candidate one requires

\[
 \partial_z^j
 \left(I^{({\rm recip})}+I^{({\rm link})}\right)
 =(-1)^{j+1}
 \frac{j!\Phi(a)^2}{L^{j+1}}
 \left[
 1-\dfrac{(j+1)(z+j+2)+1/2}{L}
 +O(L^{-2})
 \right].
\]

Thus one entire response must generate a nonconstant hierarchy in \(j\); a
fixed subleading scalar multiplier cannot satisfy every multiplicity jet.

## Falsifier

For a proposed entire reciprocal/linking section:

1. extract its late-shell expansion at fixed \(j\);
2. compare the unit leading coefficient;
3. compare the relative coefficient
   \((j+1)(z+j+2)+1/2\);
4. repeat at \(j=0\) and \(j=1\).

Failure at either order rejects full multiplicity cancellation. Higher theta
labels cannot repair a late-shell mismatch because their pair densities are
superexponentially smaller.

## Disposition

The corrected two-term hostile now applies to every fixed Evans jet. Its
subleading coefficient is jet- and parameter-dependent. No current G4
reciprocal/linking formula is available for this test, and no RH conclusion is
authorized.
