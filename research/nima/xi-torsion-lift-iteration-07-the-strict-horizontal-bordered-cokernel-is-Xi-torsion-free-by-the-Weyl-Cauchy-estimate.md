# Xi-torsion lift iteration 7: the strict horizontal bordered cokernel is Xi-torsion-free by the Weyl--Cauchy estimate

## Analytic bordered graph category

Let `B` be the four-chart bordered Silva space of holomorphic germs with:

- the endpoint/Green graph seminorms;
- the opposite-chart Hadamard observer;
- the vertical-line Bohr seminorms of the recovered delta endpoint channel.

Iteration 6 gives a strict horizontal embedding

\[
J_B:K_B\hookrightarrow B.
\]

Its image is closed, so

\[
Q_B=B/J_B(K_B)
\]

is Hausdorff. Horizontality makes the image invariant under the spectral
connection, hence `Q_B` inherits a continuous connection.

## Local Weyl relation

At a Xi zero choose a local coordinate `u` such that

\[
\tau=u^m v,
\qquad v(0)\ne0.
\]

Let `U` be multiplication by `u` and let `D` be the induced covariant normal
derivative. Then

\[
[D,U]=1
\]

on `Q_B`.

If `Uq=0`, repeated commutation gives

\[
q=\frac{(-1)^n}{n!}U^nD^nq.
\]

## Quotient Cauchy estimate

Choose analytic disks `|u|<r<rho`. The quotient seminorm is the infimum of the
bordered graph seminorm over representatives. Cauchy's estimate therefore
passes to the quotient:

\[
\|D^nq\|_r
\le
\frac{n!}{(\rho-r)^n}\|q\|_\rho,
\]

with a finite Köthe-order shift absorbed by the projective family. Since
multiplication by `u^n` has norm at most `r^n`,

\[
\|q\|_r
\le
\left(\frac r{\rho-r}\right)^n\|q\|_\rho.
\]

Taking `r<rho/2` and `n -> infinity` gives `q=0` as a germ. Thus `Q_B` has no
`u`-torsion and consequently no `tau`-torsion, including at multiple Xi zeros.

## Apply to the bordered factor

The identity

\[
\Delta_{\rm border}=\tau H_{\rm border}
\]

and the source construction of `H_border` give a canonical coefficient packet
`s` with

\[
H_{\rm border}=J_B(s).
\]

Hence its cokernel class already vanishes. More generally, the torsion-free
theorem shows that any bordered class annihilated by `tau` must vanish; this is
not dependent on choosing the known lift.

Therefore objectives 1--3 are closed **inside the analytic four-chart bordered
category**:

1. `J_B` is strict and horizontal;
2. `H_border` lies in its recoverable source range;
3. `Q_B` has no Xi-divisor torsion.

## Logical boundary: this is not the Haar residual

The result concerns the complex-linear bordered Evans packet. Its source
coefficient `s` is the labelled Clark/endpoint packet. It is not the Hermitian
relative-Haar residual

\[
(1-p^{-2\operatorname{Re}z})E_p(b_z).
\]

The earlier topology discussion informally denoted a labelled residual by `R`
and risked identifying these two objects. The shellwise bordered divisibility
was already known; the present work strengthens it to strict recoverability
and torsion-freeness but does not construct the missing metric localization map
from the bordered packet to local Haar energy.

## Next audit

Before treating the three objectives as an RH advance, identify whether the
requested `H_border` range theorem was intended only for the Evans bordered
sector or was meant to transport the Haar cycle. In the latter case the next
necessary object remains a metric-compatible map from `Q_B` or `B` to the
primewise relative-Haar carrier; no topology can substitute for that map.