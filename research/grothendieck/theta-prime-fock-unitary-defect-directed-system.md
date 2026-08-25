# Prime Poisson kernels are unitary vacuum-defect determinants in a directed Fock system

## 1. One-prime Fock carrier

Fix \(0<r<1\) and let

\[
  \mathcal H_p=\ell^2(\mathbb Z_{\ge0})
\]

with occupation basis \(e_a\). Define the normalized geometric vacuum

\[
  \Omega_r
  =
  \sqrt{1-r}
  \sum_{a\ge0}r^{a/2}e_a.
\]

Indeed,

\[
  \|\Omega_r\|^2
  =
  (1-r)\sum_{a\ge0}r^a
  =1.
\]

Let occupation phase transport be

\[
  U_\theta e_a=e^{-ia\theta}e_a.
\]

This is unitary and has vacuum overlap

\[
  a_r(\theta)
  =
  \langle\Omega_r,U_\theta\Omega_r\rangle
  =
  \frac{1-r}{1-re^{-i\theta}}.
\]

Therefore

\[
  \boxed{
  |a_r(\theta)|^2
  =
  \frac{(1-r)^2}
       {1-2r\cos\theta+r^2}.}
\]

Up to the source-fixed positive normalization \((1-r)^2\), this is the local
Poisson kernel obtained from the full parity cone.

## 2. Excited compression

Let

\[
  P_r^\circ=I-|\Omega_r\rangle\langle\Omega_r|
\]

and compress phase transport to the excited sector:

\[
  D_r(\theta)
  =
  P_r^\circ U_\theta|_{\Omega_r^\perp}.
\]

The unitary vacuum-defect theorem gives

\[
  \boxed{
  \det(D_r(\theta)^*D_r(\theta))
  =
  |a_r(\theta)|^2.}
\]

Thus every local positive Poisson factor already has the exact coupled-sector
meaning required by the global programme.

For theta arithmetic,

\[
  r_p=p^{-1/2},
  \qquad
  \theta_p=x\log p.
\]

## 3. Finite-prime directed system

For a finite prime set \(S\), define

\[
  \mathcal H_S
  =
  \bigotimes_{p\in S}\mathcal H_p,
  \qquad
  \Omega_S
  =
  \bigotimes_{p\in S}\Omega_{r_p},
\]

and

\[
  U_S(x)
  =
  \bigotimes_{p\in S}U_{\theta_p}.
\]

Then

\[
  \langle\Omega_S,U_S(x)\Omega_S\rangle
  =
  \prod_{p\in S}
  \frac{1-p^{-1/2}}
       {1-p^{-1/2-ix}}.
\]

Compression to the global vacuum complement gives

\[
  \det(D_S(x)^*D_S(x))
  =
  \prod_{p\in S}
  \frac{(1-p^{-1/2})^2}
       {|1-p^{-1/2-ix}|^2}.
\]

Adding a new prime by tensoring with its reference vacuum gives canonical
isometric connecting maps. This is the requested finite-place directed
operator system.

## 4. Infinite tensor-product gate

The reference-vacuum infinite tensor product

\[
  \bigotimes_p(\mathcal H_p,\Omega_{r_p})
\]

exists. But the infinite product phase transport is implementable in that
representation only under the von Neumann convergence criterion

\[
  \sum_p
  \|(U_{\theta_p}-I)\Omega_{r_p}\|^2
  <\infty,
\]

equivalently,

\[
  \sum_p
  2\bigl(1-\operatorname{Re}a_{r_p}(\theta_p)\bigr)
  <\infty
\]

after the usual phase convention is fixed.

At critical half-density, the leading deviation is

\[
  1-\operatorname{Re}a_{r_p}(\theta_p)
  =
  p^{-1/2}\bigl(1-\cos(x\log p)\bigr)
  +O(p^{-1}).
\]

Thus ordinary global implementability is precisely exposed to the divergent
prime half-density. The archimedean completion must change or renormalize the
representation, not merely multiply the scalar overlap by a finite factor.

## 5. Orthogonality-catastrophe interpretation

Every finite subsystem has a nonzero vacuum overlap and an invertible excited
compression. In the infinite limit, failure of the implementability
criterion means that the transported and reference vacua enter inequivalent
infinite-product sectors; their finite overlaps can collapse to zero.

\[
\boxed{
\text{global zero formation is an arithmetic orthogonality catastrophe,
not a negative local factor}.}
\]

This gives a concrete operator mechanism for strict finite reserves tending
to zero.

## 6. What modular completion must do

Raw prime Fock transport is too singular to distinguish the known discrete
theta zeros from generic collapse. A viable completed construction must:

1. add the archimedean and endpoint sectors before the infinite tensor limit;
2. cancel or quotient the universal divergent degree direction;
3. retain relative prime phases and the parity cone;
4. produce an implementable or relatively implementable modular transport;
   and
5. allow loss of invertibility only on the unitary boundary.

This is more precise than asking for convergence of an Euler product.

## 7. Falsifiers

The programme fails if:

1. the all-place reference representation is not uniquely selected;
2. relative implementability depends on prime ordering;
3. completion removes the relative-phase labels together with the divergence;
4. every nonzero \(x\) produces the same catastrophe, leaving no discrete
   spectral events; or
5. the repaired overlap is identified with \(X\) only by analytic
   continuation.

## 8. Scope

The one-prime vacuum, overlap, defect determinant, finite tensor system, and
infinite-product implementability criterion are exact. The displayed
large-prime expansion is elementary. No all-place relative representation,
archimedean repair, discrete-zero theorem, or RH result is constructed.
