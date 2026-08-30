# Theta local trace restricted product exists but misses the primitive anomaly

## Finite-place trace space

For a finite prime `p`, let

\[
 J_p:\mathcal S(\mathbb Q_p)
 \longrightarrow \operatorname{Fun}(\mathbb Q_p^\times),
 \qquad J_p\phi=\phi|_{\mathbb Q_p^\times}.
\]

Its exact image `T_p` consists of locally constant functions `g` on
`Q_p^x` such that:

1. `g(p^n u)=0` for all sufficiently negative `n`;
2. there is a constant `g_0` such that `g(p^n u)=g_0` for all sufficiently
   positive `n`, uniformly in `u in Z_p^x`;
3. on every bounded valuation interval, the unit dependence factors through
   a finite quotient of `Z_p^x`.

The eventual constant is the missing boundary value `phi(0)`.  Conversely,
extending `g` by `phi(0)=g_0` gives a unique Schwartz--Bruhat function on
`Q_p`.  Thus

\[
 \boxed{J_p:\mathcal S(\mathbb Q_p)\simeq\mathcal T_p}
\]

as locally convex test spaces when `T_p` is given the transported LF topology.

The distinguished unramified vector is

\[
 \tau_p=J_p\mathbf1_{\mathbb Z_p}.
\]

In valuation coordinates it is the constant tail `1` for `n>=0` and `0` for
`n<0`; it is not compactly supported on `Q_p^x`.

## Archimedean trace space

Let `T_infinity` be the restrictions to `R^x` of Schwartz functions on `R`.
Equivalently, its elements are rapidly decreasing with all derivatives at
infinity and have matching full one-sided Taylor jets at zero.  The seminorms
are the ordinary Schwartz seminorms after the unique smooth extension across
zero.  Hence

\[
 J_\infty:\mathcal S(\mathbb R)\simeq\mathcal T_\infty.
\]

## Restricted tensor product

The algebraic restricted tensor product

\[
 \boxed{
 \mathcal T_0(\mathbb A^\times)
 =\mathcal T_\infty
 \otimes'_{p}(\mathcal T_p,\tau_p)}
\]

exists.  The local traces assemble to

\[
 J=\bigotimes_vJ_v:
 \mathcal S(\mathbb A)\longrightarrow\mathcal T_0(\mathbb A^\times).
\]

With self-dual Haar conventions, local Fourier transform preserves each
source Schwartz space and fixes `1_(Z_p)` at every unramified place.
Therefore it induces a well-defined Fourier--Tate correspondence on `T_0` at
the algebraic test-space level.

## Local boundary terms

The eventual constant coordinate `g_0=phi(0)` is exactly the local datum lost
if one replaces `T_p` by compactly supported functions on `Q_p^x`.  Under the
local Tate functional equation, this coordinate and the corresponding
Fourier value `hat(phi)(0)` supply the polar boundary terms.  Thus the local
trace already retains the correct endpoint capability.

## Primitive-current failure

The ordinary restricted-product topology stabilizes every unramified factor
at `tau_p` and controls only finitely many deviations at a time.  The
primitive anomaly, however, assigns to the unramified prime tail the cutoff
coordinate

\[
 C_{1,X}(t)=2i\sum_{p\le X}p^{-1/2}\sin(t\log p),
\]

which has an unbounded `sqrt(X)/log(X)` envelope for fixed nonzero `t`.

Consequently there is no cutoff-independent continuous scalar functional on
`T_0` whose finite restrictions are all the primitive coordinates.  The
unramified vector is exactly where continuity fails; changing finitely many
ramified factors cannot repair it.

Therefore

\[
 \boxed{
 \mathcal T_0\text{ is the correct source trace space but not the complete
 anomaly value type}.}
\]

## Smallest witness

Every single-place and every finite-prime trace is well-defined, Fourier
covariant, and closable.  No one-prime or two-prime witness can detect the
failure.  The obstruction is irreducibly global and is witnessed by the
canonical net of unramified cutoffs itself.

This answers the requested smallest-witness question negatively:

\[
 \boxed{
 \text{all finite subsystems pass; the first failure is the infinite
 unramified restricted-product limit}.}
\]

## Required enlargement

The primitive field cannot be inserted merely by strengthening a tempered
seminorm on `T_0`, because its cutoff values do not converge.  It must be
retained as a relative or affine boundary coordinate with transition law

\[
 C_{1,Y}=C_{1,X}+\Delta C_{1;X,Y}.
\]

The completed trace object is therefore a torsor or determinant-line chart
over `T_0`, carrying `C_1` as a nonconvergent transition cocycle, `C_2` as a
Hilbert anomaly coordinate, and `k>=3` as an ordinary convergent value.

Only this enlarged relative object is a candidate domain for a closable
operator correspondence `(B_s,C_s,J)`.  Asking for adjoint-domain density in
an ordinary Hilbert graph before constructing the anomaly torsor is not yet
typed.
