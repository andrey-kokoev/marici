# Mellin–Parseval Selects the Dual Strip and Exposes the Seam

## Canonical strip duality

The continuous duality missing from the six-channel lift is already present in the source Mellin transform. With

\[
\mathcal Mf(s)=\int_0^\infty y^{s-1}f(y)\,dy,
\]

Mellin–Parseval pairs complementary exponents:

\[
\int_0^\infty f(y)g(y)\,dy
=
\frac{1}{2\pi i}
\int_{\Re s=\sigma}
\mathcal Mf(s)\mathcal Mg(1-s)\,ds.
\]

In the programme's coordinate (q=s-1), the dual exponent is

\[
q^*=-q-1.
\]

The analytic base strip (-1<\Re q<0) is therefore paired with itself by reflection about (Re q=-1/2). This is source-derived; no weight is fitted to obtain an adjoint.

## The two source adjoints

Multiplication by the wall coordinate is self-adjoint:

\[
\int_0^\infty (yf)g\,dy
=
\int_0^\infty f(yg)\,dy.
\]

This is the source-side origin of the contragredient exponent shift. Differentiation carries the boundary concomitant:

\[
\int_0^\infty f'g\,dy
+
\int_0^\infty fg'\,dy
=
\left[fg\right]_0^\infty.
\]

For the decaying Pearson source, the infinite endpoint vanishes and the wall evaluation remains. Its Mellin presentation is exactly the first polar residue already identified in the Gamma-wall port.

The earlier obstacle must therefore be refined: the source does select a dual strip and a formal adjoint. What remains is the topology and domain on which the endpoint trace and all prime transports coexist continuously.

## Prime translation reveals the seam

Let right translation on the half-line be

\[
(T_Lf)(y)=f(y+L).
\]

Its (L^2(0,\infty)) adjoint is not inverse translation. It is truncated backward translation:

\[
(T_L^*g)(x)=\mathbf 1_{x\ge L}g(x-L).
\]

Indeed,

\[
\int_0^\infty f(y+L)g(y)\,dy
=
\int_L^\infty f(x)g(x-L)\,dx.
\]

The omitted interval ([0,L)) is precisely the finite moving seam. For (L=\log p), it is the same source interval that appeared earlier as the prime sewing current. The seam is therefore not an auxiliary correction: it is the cokernel of making a one-sided prime translation adjointable.

## Topological fork

The (L^2) translation family is uniformly bounded, repairing the failure of equicontinuity in the topology of all entire germs. But wall evaluation is not continuous on bare (L^2). Passing to a first-order Sobolev graph space makes the trace continuous, while truncated backward translation can create a jump at (L).

This forces a direct-sum architecture: the bulk graph space together with an
independent seam trace space.

The seam cannot be integrated out. It is exactly what permits both a continuous wall trace and a uniformly bounded prime-translation correspondence.

## New sharp theorem

Construct the Mellin–Parseval rigging with an explicit seam trace component and prove:

1. the Pearson derivative is a closed operator with its wall concomitant;
2. multiplication by (y) is self-adjoint on the paired domains;
3. each prime translation is a bounded correspondence whose adjoint defect is the interval ([0,\log p));
4. these interval defects resegment coherently over products of primes;
5. the restricted-product completion retains their trace norms.

The first failure among these is the genuine analytic obstruction. The dual-strip pairing itself is no longer missing.

## Verification

The dependency-free exact-rational checker `research/grothendieck/checkers/mellin_parseval_dual_strip_and_seam.py` verifies the Green endpoint identity, wall-coordinate self-adjointness, and truncated-translation adjoint identity on polynomial witnesses.
