# Bilateral history reduces the auxiliary gate to distance from two points

## Normal convolution reduction

For the bilateral history operator

\[
(Hf)(t)=\int_0^\infty\Phi(r)f(t+r)\,dr,
\]

Fourier transform identifies \(H\) with multiplication by

\[
m(\xi)=\int_0^\infty\Phi(r)e^{i\xi r}\,dr.
\]

Hence \(H\) is normal, and the shifted-history factors satisfy

\[
I\pm iH
\longleftrightarrow
1\pm i m(\xi).
\]

Their exact lower singular values are

\[
c_\pm
=
\operatorname*{ess\,inf}_{\xi}
|1\pm i m(\xi)|.
\]

Equivalently,

\[
c_+
=
\operatorname{dist}(-i,\operatorname{essran}m),
\qquad
c_-
=
\operatorname{dist}(+i,\operatorname{essran}m).
\]

Thus

\[
D_\pm\ge\frac{c_\pm^2}{2}I.
\]

The entire auxiliary contraction problem has become a geometric exclusion theorem for the complex history transform.

## Cheap source-level sufficient bound

Young's inequality gives

\[
\|H\|
\le
\|\Phi\|_{L^1(0,\infty)}=:M_\Phi.
\]

If

\[
M_\Phi<1,
\]

then the essential range of \(m\) lies in the disk of radius \(M_\Phi\), and

\[
c_\pm\ge1-M_\Phi.
\]

Consequently,

\[
D_\pm
\ge
\frac{(1-M_\Phi)^2}{2}I.
\]

This route is robust but may be too strong. Failure of \(M_\Phi<1\) does not imply failure of the shifted-history gate, because the history symbol can have norm exceeding one while staying away from \(\pm i\).

## Exact geometric alternatives

Any one of the following proves the auxiliary margin:

1. disk exclusion:
   \[
   \operatorname{essran}m\subset\{z:|z|\le r<1\};
   \]
2. half-plane exclusion:
   \[
   |\operatorname{Re}m(\xi)|\ge a>0
   \]
   whenever \(\operatorname{Im}m\) is near \(\pm1\);
3. direct point-distance estimate:
   \[
   \inf_\xi\min\{|m(\xi)-i|,|m(\xi)+i|\}>0.
   \]

The third is exact and should be preferred if the theta transform is explicitly available.

## Compactness of the search

If \(\Phi\in L^1\), then \(m\) is continuous and

\[
m(\xi)\to0
\qquad
(|\xi|\to\infty)
\]

by the Riemann–Lebesgue lemma. Since \(0\) has unit distance from both forbidden points, any failure of a positive margin occurs in a bounded frequency interval.

Therefore an analytic or certified numerical proof may split the problem into:

- a compact interval containing all possible near-collisions;
- a high-frequency tail where \(|m(\xi)|\le r<1\).

This is a genuine finite attack path once the exact source formula for \(\Phi\) and certified tail bounds are frozen.

## Prime and cutoff typing

If the prime-labeled history is a translated or rescaled copy \(H_p\), its multiplier may be

\[
m_p(\xi)=\alpha_p m(\beta_p\xi)
\]

or a related source-fixed transform. Frequency rescaling alone does not change the range of \(m\), but amplitude scaling does. The prime-uniform margin must therefore track the exact coefficient \(\alpha_p\); it cannot be inferred from one unweighted master kernel.

Finite cutoff compressions need not preserve the normal multiplier representation. Their lower bounds require either:

- compression monotonicity inherited from the shifted Gram;
- or a separate finite-section stability theorem.

## Hostiles

1. \(M_\Phi>1\) while the symbol remains on the positive real axis. The cheap disk test fails although both shifted histories are uniformly invertible.
2. A symbol curve touches \(+i\) once. The auxiliary block has an exact radical despite excellent high-frequency decay.
3. Symbol curves avoid \(\pm i\) for every finite cutoff but approach one forbidden point as cutoff grows.
4. Prime amplitude factors \(\alpha_p\) move an otherwise safe master curve toward \(\pm i\).

## Next executable packet

Extract the exact completed theta history kernel \(\Phi\), its prime coefficient scaling, and its Fourier–Laplace transform \(m\). Then certify

\[
\inf_{p,\xi}
\min\{|m_p(\xi)-i|,|m_p(\xi)+i|\}>0
\]

on each compact off-seam parameter set. This is now the sharp auxiliary positivity calculation.
