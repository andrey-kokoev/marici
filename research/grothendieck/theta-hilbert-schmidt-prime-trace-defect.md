# Hilbert--Schmidt prime trace defect at the critical seam

Author: `marici.Grothendieck`

## 0. Operator stimulus and correction of emphasis

The operator proposed that the scalar meaning becomes undefined through a
loss of integrality after the two half-planes acquire their distinction. A
previous Fredholm audit emphasized that the prime operator is not
Hilbert--Schmidt *on* the critical line. The present observation changes the
emphasis: RH requires control of the open chamber, and the prime operator is
Hilbert--Schmidt at every point of that chamber.

This supplies a literal analytic threshold at `Re(s)=1/2` and isolates the
only prime channel not controlled by it.

## 1. Prime operator in the distinguished chamber

On `ell^2(primes)`, define

\[
P_s e_p=p^{-s}e_p.
\]

If `sigma=Re(s)`, then

\[
\|P_s\|_{\rm HS}^2=\sum_p p^{-2\sigma}.
\]

Therefore

\[
\boxed{
P_s\in\mathcal S_2
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac12.
}
\]

On the boundary, the norm diverges as `sum_p 1/p`. Thus the critical line is
exactly the loss-of-square-integrability seam for the prime character state.
This is not a plotted-coordinate artifact.

## 2. The nonvanishing regularized Euler determinant

For `Re(s)>1/2`, the Hilbert--Schmidt determinant

\[
D_2(s)=\det{}_2(I-P_s)
\]

is well-defined and holomorphic. Since `|p^(-s)|<1` for every prime,

\[
D_2(s)\ne0.
\]

Its convergent product and logarithm are

\[
\boxed{
D_2(s)
=\prod_p(1-p^{-s})e^{p^{-s}},
}
\]

\[
\log D_2(s)
=-\sum_p\sum_{k\ge2}\frac{p^{-ks}}k.
\]

Hence every nonlinear prime-power channel `k>=2` already forms a canonical
nonvanishing analytic object throughout the open RH chamber. No analytic
continuation of that double tail is required.

## 3. Exact isolation of the linear prime channel

In the honest Euler region, put

\[
\mathcal P_1(s)=\sum_p p^{-s}.
\]

Then

\[
\zeta(s)=e^{\mathcal P_1(s)}D_2(s)^{-1}
\qquad(\operatorname{Re}s>1).
\]

Consequently

\[
\xi(s)
=\frac12s\pi^{-s/2}\Gamma(s/2)
\left[(s-1)e^{\mathcal P_1(s)}\right]D_2(s)^{-1}.
\]

Define on the whole open chamber

\[
\boxed{
\mathcal T(s)
=\frac{2\pi^{s/2}\xi(s)}{s\Gamma(s/2)}D_2(s).
}
\]

All displayed factors are holomorphic there, with the apparent endpoint at
`s=1` already removed by completion. In `Re(s)>1`, this factor agrees with

\[
\mathcal T(s)=(s-1)e^{\mathcal P_1(s)}.
\]

Thus completion canonically continues the *exponentiated renormalized linear
prime trace* into `Re(s)>1/2` without choosing a logarithmic branch.

## 4. Exact reduced RH statement

The gamma factor, `s`, and `D_2` are nonzero in the open right chamber.
Therefore

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\mathcal T(s)\ne0
\quad\text{for }\operatorname{Re}s>\frac12.
}
\]

Equivalently, every possible chamber-interior divisor of `xi` is carried by
one scalar factor: the completed continuation of
`(s-1) exp(sum_p p^(-s))`.

This does not mean that higher prime powers are arithmetically irrelevant.
They determine the nonzero determinant used to extract `T`. It means they
cannot themselves carry divisor charge inside the Hilbert--Schmidt chamber.
All such charge is concentrated in the renormalized trace channel.

## 5. Integrality interpretation

Before regularization, the Euler determinant fails because `P_s` is not
trace class for `1/2<Re(s)<=1`. The `det_2` operation removes exactly the
linear trace and retains all cyclic words of length at least two. Therefore
the completed chamber splits canonically into

\[
\boxed{
\text{square-integrable nonlinear prime geometry}
+
\text{one renormalized linear trace channel}.
}
\]

At the seam, even the square-integrable geometry ceases to exist in this
Hilbert model. The operator's proposed ordering is consequently realized as

\[
\text{chamber distinction at }\operatorname{Re}s=\frac12
\longrightarrow
\text{Hilbert--Schmidt prime geometry inside the chamber}
\longrightarrow
\text{possible scalar trace-phase defect}.
\]

The underlying integer prime labels remain intact. What can fail is the
integrable scalar trivialization of their linear trace.

## 6. Relation to the oval/circle observation

If `T` has a zero `rho`, then locally

\[
\mathcal T(s)=(s-\rho)^mU(s),
\qquad U(\rho)\ne0.
\]

Its constant-amplitude ovals become circles in the conformal coordinate
`w=(s-rho)U(s)^(1/m)`, and their phase winding is the integral defect `m`.
Because `D_2` is nonzero, this winding belongs entirely to the trace factor,
not to the regularized nonlinear determinant.

## 7. New minimal theorem

The missing statement is no longer an unspecified continuation of the full
Euler product. It is

\[
\boxed{
\text{the completed exponentiated linear-prime trace }\mathcal T
\text{ has a holomorphic logarithm in }\operatorname{Re}s>\frac12.
}
\]

The theta source must explain this single channel. A promising construction
would express `T` as the exponential of a completed prime-seam current whose
apparent singularity at `s=1` cancels before integration. Defining that
current as `T'/T` is circular unless its regularity is obtained independently
from the source.

## 8. Falsifier and scope

Any claimed reduction fails if its regularized determinant retains the
linear prime trace, uses `det(I-P_s)` where `P_s` is not trace class, or
asserts `det_2` exists on the critical line itself. It exists precisely in
the open chamber.

The Hilbert--Schmidt threshold, nonvanishing of `D_2`, and factorization in
the Euler region are exact. The chamber definition of `T` is an exact
analytic continuation obtained from `xi`; proving it nonzero is equivalent
to RH. The reduction isolates the missing channel but does not prove its
phase triviality. RH is not proved.

## 9. The surviving current is prime discrepancy

In the Euler chamber, logarithmic differentiation of the isolated factor
gives

\[
\boxed{
\frac{\mathcal T'(s)}{\mathcal T(s)}
=\frac1{s-1}-\sum_p(\log p)p^{-s}.
}
\]

All repeated prime powers have disappeared into the holomorphic nonvanishing
factor `D_2`.  The remaining current compares the primitive-prime measure

\[
d\vartheta(x)=\sum_p(\log p)\delta_p
\]

with its continuous main density.  Stieltjes summation gives

\[
\sum_p(\log p)p^{-s}
=s\int_1^\infty\vartheta(x)x^{-s-1}\,dx
\qquad(\operatorname{Re}s>1).
\]

Since

\[
s\int_1^\infty x\,x^{-s-1}\,dx=\frac{s}{s-1},
\]

the completed trace current is exactly

\[
\boxed{
\frac{\mathcal T'}{\mathcal T}(s)
=-1+s\int_1^\infty
\bigl(x-\vartheta(x)\bigr)x^{-s-1}\,dx.
}
\]

Thus the scalar phase defect is the Mellin transform of one arithmetic
discrepancy: continuum scale minus accumulated primitive-prime weight.

## 10. Why the exponent one half appears twice

If

\[
\vartheta(x)-x=O_\epsilon(x^{1/2+\epsilon}),
\]

then the discrepancy integral converges in every half-plane
`Re(s)>1/2+epsilon` and supplies the desired chamber logarithmic current.
Conversely, sufficiently controlled continuation and growth of this Mellin
transform yields the corresponding prime-number error estimate.  This is
the classical square-root frontier in a form typed to the isolated trace
channel.

The critical exponent therefore has two compatible meanings:

\[
\boxed{
\begin{aligned}
\operatorname{Re}s>\frac12
&\Longleftrightarrow
\{p^{-s}\}_p\in\ell^2,\\
\operatorname{Re}s=\frac12
&\Longleftrightarrow
\text{square-root scale of the primitive-prime discrepancy.}
\end{aligned}
}
\]

This coincidence is structural.  The first line says nonlinear prime
geometry is integrable inside the chamber.  The second says the only
remaining linear statistic fluctuates at precisely the boundary scale.

In the operator's language, the half-planes acquire distinction at the
square-integrability threshold, and scalar meaning can fail only through the
unrenormalized discrepancy between the integer prime lattice and its
continuous carrier density.

## 11. Revised theorem target

The theta side need not reconstruct every Euler factor.  It must produce a
branch-independent completion of

\[
-1+s\int_1^\infty(x-\vartheta(x))x^{-s-1}\,dx
\]

whose primitive has no integral monodromy in `Re(s)>1/2`.  Any proof that
assumes square-root cancellation for `vartheta(x)-x` has merely inserted an
RH-equivalent estimate.  The opportunity is to derive the cancellation from
reciprocal theta sewing or from a source-defined orthogonality of the prime
discrepancy current.
