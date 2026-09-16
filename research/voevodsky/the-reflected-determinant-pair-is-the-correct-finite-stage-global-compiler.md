# The reflected determinant pair is the correct finite-stage global compiler

## Question

What determinant-line object simultaneously respects the direct Sonin Euler orientation, reciprocal reflection, and the Weil logarithmic current?

## Claim boundary

At every finite stage the compiler is a reflected pair of holomorphic determinant sections. Their ratio is meromorphic, unitary on the real axis, and its logarithmic connection is exactly the local Weil current. A subsequent completion audit shows that the raw positive and negative sections cannot converge as finite-valued holomorphic frames on a domain crossing the completed-zeta divisor; only meromorphic sections or local numerator/denominator frames are admissible there.

## Positive section

For a finite prime-and-grade stage define the source-oriented section

$$
D_{+,N}(z)
=
A_{\infty,N}(z)
\exp\left(
\operatorname{Tr}K_N(z)
-
\frac12\operatorname{Tr}K_N(z)^2
\right)
\det_3(I+K_N(z)),
$$

with local return orientation

$$
K_p(z)=-p^{-1/2-iz}.
$$

The regularized determinant identity gives

$$
D_{+,N}(z)
=A_{\infty,N}(z)
\prod_{p\in S_N}(1-p^{-1/2-iz}).
$$

## Reflected section

For a holomorphic section \(H\), write

$$
H^\#(z)=\overline{H(\bar z)}.
$$

Define

$$
D_{-,N}=D_{+,N}^\#.
$$

Both sections are holomorphic on their common finite-stage domain. The determinant-line scattering section is

$$
\mathcal S_N(z)
=
\frac{D_{+,N}(z)}{D_{-,N}(z)}.
$$

It is meromorphic, and on the real axis away from zeros,

$$
|\mathcal S_N(t)|=1.
$$

Reflection gives

$$
\mathcal S_N^\#=\mathcal S_N^{-1}.
$$

## Weil connection

On the real axis,

$$
\frac1{2i}\partial_t\log\mathcal S_N(t)
=
\operatorname{Im}
\frac{D_{+,N}'(t)}{D_{+,N}(t)}.
$$

This is precisely the gamma-plus-finite-prime Weil current in the retained normalization. Adding

$$
\varepsilon_{\rm end}\frac{2z}{z^2+1/4}\,dz
$$

incorporates the two endpoint residues into the same meromorphic connection.

Thus the completed finite-stage object is naturally a line with two reflected holomorphic frames and a meromorphic unitary transition function. The poles of the transition are zeros of the reflected frame, not failures of holomorphy of either frame.

## Multiplicity and Fourier reciprocity

A zero of order \(m\) in \(D_{+,N}\) contributes divisor multiplicity \(+m\); a zero of order \(m\) in \(D_{-,N}\) contributes \(-m\) to the ratio. Reciprocal reflection exchanges these two divisor components. This is the determinant-line analogue of the previously proved canonical-dual branch swap.

## Infinite-stage criterion — corrected

Raw compact-local convergence to globally holomorphic finite-valued frames is too strong and generally impossible across the completed divisor. The admissible completion data are instead local holomorphic numerator/denominator frames for meromorphic sections, with transition compatibility on overlaps. Normal convergence is required only after the declared local renormalizations and away from denominator zeros. No globally bounded logarithm or inverse-gap estimate is required to define the resulting meromorphic transition.

## Disposition

The finite-stage determinant compiler is the reflected pair \((D_{+,N},D_{-,N})\) with transition \(D_{+,N}/D_{-,N}\). It exactly reproduces reciprocal symmetry and the Weil logarithmic current. Global completion must occur in a meromorphic determinant line using compatible local holomorphic numerator/denominator frames; completion as two global holomorphic direct-product limits is rejected.