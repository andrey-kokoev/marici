# Theta forcing is the exact parabolic-confinement residual

## Bounded question

What source-derived differential law would keep the theta transfer inside its
open incidence cell, and does the native tail system satisfy it?

## Invariant-hyperplane theorem

Let a transported state satisfy

\[
x'(\tau)=K(\tau)x(\tau)
\]

and let the scalar readout be

\[
y(\tau)=\ell x(\tau).
\]

Suppose the endpoint covector spans an invariant adjoint line:

\[
\ell K(\tau)=\alpha(\tau)\ell.
\]

Then

\[
y'(\tau)=\alpha(\tau)y(\tau),
\]

and hence

\[
y(\tau)
=
y(\tau_0)
\exp\left(\int_{\tau_0}^{\tau}\alpha(r)\,dr\right).
\]

If \(y(\tau_0)\ne0\), the readout cannot vanish anywhere along the admitted
flow.

Equivalently, the hyperplane \(\ker\ell\) is invariant. The transfer remains
inside one open incidence cell because its chosen pivot evolves
multiplicatively.

This is a noncircular chamber-confinement mechanism when \(K\), \(\ell\), and
their invariant relation are derived before inspecting \(y\).

## Native theta tail system

The one-sided source tail obeys

\[
G_q=-zG-f(q)c,
\qquad
c_q=0.
\]

With

\[
X=
\begin{pmatrix}
G\\
c
\end{pmatrix},
\qquad
K_z(q)=
\begin{pmatrix}
-z&-f(q)\\
0&0
\end{pmatrix},
\]

the theta endpoint readout uses

\[
\ell_G=\begin{pmatrix}1&0\end{pmatrix}.
\]

But

\[
\ell_GK_z(q)
=
\begin{pmatrix}
-z&-f(q)
\end{pmatrix},
\]

which is proportional to \(\ell_G\) only when \(f(q)=0\).

Thus the completed theta forcing is exactly the off-parabolic residual that
allows the transported state to cross the endpoint incidence divisor.

## The invariant but irrelevant channel

The constant-channel covector

\[
\ell_c=\begin{pmatrix}0&1\end{pmatrix}
\]

does satisfy

\[
\ell_cK_z=0.
\]

Its readout is conserved and nonzero, but it is not the theta scalar. Promoting
this invariant coordinate would change the observable rather than prove
nonvanishing of \(G(0,z)\).

## Required enlarged flag

A surviving source construction must enlarge the state and derive a covector
\(\widetilde\ell\) such that:

1. its boundary readout equals the completed theta scalar up to a proven unit;
2. it spans an invariant adjoint line in each open reciprocal sector;
3. primitive, square, seam, and archimedean channels cancel the forcing
   residual in the adjoint equation;
4. the invariant lines sew covariantly on the critical seam;
5. the construction precedes scalar zero inspection.

For a moving covector, the condition becomes

\[
\widetilde\ell'
+\widetilde\ell K
=
\alpha\widetilde\ell.
\]

This equation can always be solved backward from a chosen scalar solution, so
existence alone is tautological. The covector must be assembled locally from
the labelled source currents.

## Geometric meaning

The forcing \(f(q)c\) is not a nuisance term. It is the precise infinitesimal
motion transverse to the parabolic subgroup that preserves the endpoint
hyperplane. Removing it would prevent the theta source from entering the
readout at all.

Therefore the desired theorem cannot simply erase forcing. Reciprocal sewing
must convert transverse forcing from the two sectors into a larger invariant
flag or a controlled chamber current.

## Result

Invariant-hyperplane transport is the first exact symbolic mechanism that
would forbid incidence-divisor crossings. The native one-sided theta system
fails it, and the failure is exactly the nonzero source forcing. The RH-bearing
gate is now:

> Does the complete reciprocal theta/Tate enlargement turn the two forcing
> residuals into one source-derived invariant adjoint flag?

This is sharper than generic positivity and is directly falsifiable at finite
cutoff.

## Sharp falsifier

For any proposed enlarged finite system \(K_X\) and endpoint covector
\(\widetilde\ell_X\), compute

\[
R_X
=
\widetilde\ell_X'
+\widetilde\ell_XK_X
-\alpha_X\widetilde\ell_X.
\]

Any nonzero labelled primitive, square, seam, or archimedean component of
\(R_X\) disproves parabolic confinement. A covector obtained from the completed
theta solution itself fails source authority even if \(R_X=0\).
