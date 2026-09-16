# The sewn and defect subspaces form a hyperbolic pair, and Green flux does not control defect energy

## Question

How does the positive sewing-defect energy relate to the indefinite Green boundary form? Can vanishing Green flux force the defect to vanish?

## Claim boundary

The Hilbert-orthogonal decomposition into sewn and defect components is a pair of complementary maximal-isotropic subspaces for the Green form. Green flux is their mixed pairing, while defect energy is the positive norm of the transverse component. Consequently zero flux does not imply zero sewing defect.

## Two complementary graphs

Let

$$
\Lambda_+=\operatorname{Graph}(T)
=
\{(h,Th):h\in H\},
$$

and define the Hilbert-orthogonal transverse graph

$$
\Lambda_-
=
\{(-T^*k,k):k\in H\}.
$$

Every \((x,y)\in H\oplus H\) decomposes uniquely as

$$
(x,y)
=(h,Th)+(-T^*k,k),
$$

where

$$
h=\frac12(x+T^*y),
$$

$$
k=\frac12(y-Tx).
$$

The first term is the closest sewn pair; the second is the minimal defect representative.

## Both subspaces are Green-isotropic

For the boundary form

$$
[(x,y),(x',y')]_\partial
=
\langle x,x'\rangle-
\langle y,y'\rangle,
$$

unitarity gives

$$
[(h,Th),(h',Th')]_\partial=0.
$$

Likewise,

$$
[(-T^*k,k),(-T^*k',k')]_\partial
=
\langle T^*k,T^*k'\rangle-
\langle k,k'\rangle
=0.
$$

Thus \(\Lambda_+\) and \(\Lambda_-\) are complementary maximal-isotropic subspaces: a hyperbolic polarization of boundary phase space.

## Mixed Green pairing

Their cross pairing is

$$
[(h,Th),(-T^*k,k)]_\partial
=-2\langle Th,k\rangle
$$

up to the declared convention for which slot is linear. It is nondegenerate: if this vanishes for all \(h\), then \(k=0\), and conversely.

Hence the Green form pairs the sewn coordinate with the defect coordinate; it does not provide a positive norm on either one separately.

## Flux formula

For \(d=y-Tx=2k\), the boundary flux of an arbitrary pair is

$$
\boxed{
[(x,y),(x,y)]_\partial
=-2\operatorname{Re}\langle Th,d\rangle.
}
$$

By contrast, its positive distance from sewing is

$$
\boxed{
\operatorname{dist}((x,y),\Lambda_+)^2
=\frac12\|d\|^2.
}
$$

## Zero-flux counterexample

Choose nonzero \(h,d\) with

$$
\operatorname{Re}\langle Th,d\rangle=0.
$$

Then

$$
[(x,y),(x,y)]_\partial=0,
$$

but

$$
\operatorname{dist}((x,y),\Lambda_+)^2
=\frac12\|d\|^2>0.
$$

Even more simply, every nonzero pure transverse vector in \(\Lambda_-\) has zero Green flux while carrying positive defect energy.

Therefore scalar isotropy is strictly weaker than membership in the sewing graph.

## Evans consequence

A Green identity proving only

$$
[e,e]_\partial=0
$$

cannot establish

$$
e_+=Te_-.
$$

It tests one real mixed matrix coefficient, whereas sewing requires the full vector defect \(d_Te\) to vanish or be Xi-divisible. The arithmetic return must control the transverse defect coordinate itself.

## Character sectors

The hyperbolic splitting is compatible with the four Fourier projectors. In each character sector, Green flux pairs the sewn and defect coordinates, while

$$
\frac12\|D_\lambda\|^2
$$

is the independent positive defect energy. Summed scalar flux can vanish both within and across sectors without forcing any \(D_\lambda\) to vanish.

## Disposition

Boundary phase space has a canonical hyperbolic polarization into the sewing graph and its Hilbert-orthogonal defect graph. Green flux is only their mixed pairing. This gives an exact geometric reason maximal isotropy or scalar Green cancellation cannot replace the vector-valued Evans sewing condition.