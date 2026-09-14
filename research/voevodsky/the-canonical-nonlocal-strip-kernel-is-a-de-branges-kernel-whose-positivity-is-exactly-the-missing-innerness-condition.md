# The canonical nonlocal strip kernel is a de Branges kernel whose positivity is exactly the missing innerness condition

## Reflected multiplier

Let `E_S(z)` denote a finite-stage completed multiplier containing the archimedean factor and the finite inverse Euler factors in one fixed convention. Define

\[
E_S^\#(z)=
\overline{E_S(\bar z)}
\]

and the reflected ratio

\[
\Theta_S(z)=
\frac{E_S^\#(z)}{E_S(z)}.
\]

On a real boundary line where `E_S` has no zero,

\[
|\Theta_S(t)|=1.
\]

The logarithmic derivative of this ratio gives the local contour current studied previously.

## Canonical two-variable kernel

On the upper half-plane normalization, define

\[
\boxed{
K_S(z,w)
=
\frac{
1-\Theta_S(z)
\overline{\Theta_S(w)}
}{2\pi i(\bar w-z)}.
}
\]

Equivalently, before dividing by the outer factors,

\[
\boxed{
K_{E_S}(z,w)
=
\frac{
E_S(z)\overline{E_S(w)}
-
E_S^\#(z)\overline{E_S^\#(w)}
}{2\pi i(\bar w-z)}.
}
\]

These kernels are related by

\[
K_{E_S}(z,w)
=
E_S(z)\overline{E_S(w)}
K_S(z,w).
\]

After conformally mapping the critical strip to a half-plane or disk, the same formula applies with the corresponding Cauchy denominator.

## Exact positivity criterion

The kernel `K_S` is positive semidefinite if and only if `Theta_S` is a Schur function:

\[
\boxed{
K_S\succeq0
\quad\Longleftrightarrow\quad
\Theta_S\text{ is analytic and }
|\Theta_S(z)|\le1
\text{ in the domain}.}
\]

Equivalently, `E_S` must satisfy the Hermite--Biehler inequality

\[
\boxed{
|E_S^\#(z)|

\le
|E_S(z)|
}
\]

in the selected half-domain, with strict inequality away from degenerate factors.

This is the unique natural scalar two-variable positive kernel attached to the reflected scattering ratio.

## Boundary derivative

On the diagonal boundary, the kernel density is controlled by the phase derivative. Formally, if

\[
\Theta_S(t)=e^{i\phi_S(t)},
\]

then

\[
K_S(t,t)
=
\frac{\phi_S'(t)}{2\pi}
\]

up to the sign determined by the half-plane convention. Thus the gamma--prime logarithmic current is the boundary diagonal of the nonlocal kernel.

This explains why diagonalizing first lost positivity: the full kernel may be positive even though an incompletely normalized scalar density changes sign, but only when `Theta_S` is genuinely Schur.

## One-prime local test

For one inverse Euler factor

\[
m_p(z)=1-p^{-1/2-iz},
\]

put `z=x+iy`, `0<y<1/2`. Then

\[
|m_p(z)|^2
=
1+p^{-1+2y}
-2p^{-1/2+y}\cos(x\log p),
\]

while

\[
|m_p^\#(z)|^2
=
1+p^{-1-2y}
-2p^{-1/2-y}\cos(x\log p).
\]

At resonance `x log p=0 mod 2pi`,

\[
|m_p(z)|
<
|m_p^\#(z)|
\]

for the displayed orientation, whereas at antiresonance `x log p=pi mod 2pi`,

\[
|m_p(z)|
>
|m_p^\#(z)|.
\]

Therefore neither `m_p#/m_p` nor its reciprocal is uniformly contractive throughout the strip by itself. A single finite prime does not define a scalar Schur factor in this normalization.

This is the nonlocal version of the sign-changing Poisson-density calculation.

## Need for common completion

The archimedean factor and all finite factors must consequently be combined before testing the Hermite--Biehler inequality:

\[
E_S=E_\infty
\prod_{p\in S}m_p.
\]

No factorwise positive-kernel proof is possible, because the individual prime kernels change orientation across the strip. Any valid positivity must arise from correlated multiplication in the complete `E_S`.

This preserves deterministic cross-prime polarization automatically: products are formed before the de Branges kernel is evaluated.

## Prime transition formula

Adjoining `q` changes

\[
E_{S\cup\{q\}}=E_Sm_q
\]

and

\[
\Theta_{S\cup\{q\}}
=
\Theta_S
\frac{m_q^\#}{m_q}.
\]

The kernel increment is

\[
K_{S\cup\{q\}}(z,w)-K_S(z,w)
=
\frac{
\Theta_S(z)\overline{\Theta_S(w)}
}{2\pi i(\bar w-z)}
\left[
1-
\frac{m_q^\#(z)}{m_q(z)}
\overline{
\frac{m_q^\#(w)}{m_q(w)}
}
\right].
\]

The bracket is not positive by itself because the local ratio is not Schur. Hence transition positivity cannot be obtained by adding a positive prime kernel at each stage.

The tower must permit a nontrivial renormalization or congruence of the entire old kernel when a prime is adjoined.

## Relation to Suzuki

Suzuki's leakage ratio has the same structural form

\[
\Theta=
\frac{E^\#}{E},
\]

and the associated Toeplitz/model-space kernel becomes positive precisely when the reflected ratio is inner or Schur in the required domain. Assuming this property globally would import the zero-location statement that the construction is intended to prove.

Thus replacing the signed contour differential by its canonical de Branges kernel does not automatically avoid circularity.

## Endpoint incorporation

The rational endpoint factor can be included in `E_S` through a canonical product or treated as a boundary Pontryagin block. If included multiplicatively, its zeros at `plus-or-minus i/2` lie on the strip boundary and determine the even/odd residue channels.

The full kernel then belongs initially to a generalized de Branges/Pontryagin setting. Positivity after physical compression asks whether its negative squares disappear on the convolution-square observation subspace.

## Rung-four equivalence warning

For the globally completed zeta multiplier, Hermite--Biehler or innerness of the reflected ratio is tightly linked to zero placement. Therefore proving

\[
K_E\succeq0
\]

on the unrestricted completed space is not an easier local estimate; it is essentially the missing global theorem.

A noncircular strategy must prove positivity only after a source-derived compression that is weaker than global Schur innerness, or construct a different larger positive bulk whose positivity is unconditional and whose exact Schur complement is the Weil form.

## Disposition

The correct canonical nonlocal scalar kernel is

\[
\boxed{
K_S(z,w)
=
\frac{1-\Theta_S(z)
\overline{\Theta_S(w)}}
{2\pi i(\bar w-z)}.
}
\]

It couples all primes before polarization and avoids the false pointwise-density reduction. But its positivity is equivalent to the Schur/Hermite--Biehler property of the completed reflected multiplier. Individual prime transitions are not positive.

The next viable route is therefore not to assert `K_S>=0`, but to seek an unconditional larger positive kernel `G_S` and a source-derived contraction `R_S` such that

\[
K_S
=
G_S-R_S^*R_S,
\]

with the negative part identified with the single physical endpoint/Suzuki cokernel rather than with independent prime channels.
