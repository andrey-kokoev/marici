# Theta completion is a multiplier, not a discrete zero operator

Epistemic-graph event: 1409.

## The strongest direct completed source

Poisson summation for the Jacobi theta series gives the completed Riemann
function without using its zeros. After the logarithmic change of variable,
the standard integration-by-parts form is

\`Xi(t)=xi(1/2+i t)=integral_0^infinity Phi(u) cos(tu) du\`,

where

\`Phi(u)=sum_(n>=1) (4 pi^2 n^4 exp(9u/2)-6 pi n^2 exp(5u/2))
exp(-pi n^2 exp(2u))\`.

The kernel is real, smooth, even after reflection, and rapidly decreasing.
Let \`k\` be the even normalization whose Fourier transform is \`Xi\`, and
define logarithmic convolution on \`L^2(R)\` by

\`C_k f=k*f\`.

This is the direct theta/Poisson completion of the Mellin-dilation system: no
prime or zero has been fitted.

## Exact spectral representation

The unitary Fourier transform conjugates \`C_k\` to multiplication:

\`F C_k F^{-1}=M_Xi\`.

Because \`Xi(t)\` is real for real \`t\`, this is a bounded self-adjoint
operator. Its spectrum is the essential range of \`Xi\`, not the discrete set
of zeros of \`Xi\`.

More sharply,

\`ker(C_k) congruent L^2({t:Xi(t)=0})\`.

The entire function \`Xi\` is not identically zero, so its real zero set is
discrete and has Lebesgue measure zero. Therefore

\`ker(C_k)=0\`.

The Riemann zeros on the critical line label generalized plane waves
\`exp(i t y)\`; they are not \`L^2(R)\` eigenvectors. Since \`Xi(t)\` tends to
zero as \`|t|\` tends to infinity, zero belongs to the continuous spectrum,
but it is not an eigenvalue.

## Compactness and determinant obstruction

A nonzero multiplication operator on a nonatomic \`L^2\` space is not
compact. Indeed, on a positive-measure set where \`|Xi|>=epsilon\`, infinitely
many orthonormal functions have images separated by at least \`epsilon\`.
Thus \`C_k\` is neither compact nor trace class, despite its smooth rapidly
decreasing convolution kernel.

Consequently there is no Fredholm determinant \`det(I-z C_k)\` whose zero set
is the Riemann zero set. Applying the scalar function \`Xi\` to the
self-adjoint dilation generator merely restates the multiplier identity; it
does not produce an operator having those frequencies as discrete spectrum.

## Quotient obstruction

A reducing quotient or restriction compatible with logarithmic translations
is, in the Fourier representation, supported on a measurable spectral subset.
A discrete zero set has measure zero and hence selects the zero Hilbert space.
Any positive-measure selection retains multiplication spectrum rather than
turning the isolated zeros into normalizable eigenvectors.

Compactifying logarithmic position makes the dilation spectrum discrete, but
then the allowed frequencies form an arithmetic lattice fixed by the interval
and endpoint phase. Ledger 1375 proves that this has linear density and cannot
retain the exact theta multiplier or the \`T log T\` zero count.

## Consequence

Theta/Poisson completion solves analytic continuation noncircularly, while the
intrinsic-prime determinant solves the Euler trace noncircularly in
\`Re(s)>1\`. Their equality as scalar functions does not itself supply a
Hilbert--Polya operator. The missing structure is specifically a
source-derived non-translation-invariant boundary or quotient that makes
Mellin generalized eigenstates normalizable without imposing their
frequencies.

## Scope

This falsifies the direct translation-invariant theta convolution and all
translation-compatible spectral quotients. It does not exclude a
source-derived nonlocal, non-translation-invariant boundary, canonical system,
or relative scattering construction.
