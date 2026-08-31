# The two-sided theta-history mismatch is an exact Evans lift of the Xi section

## Theta forcing transform

Let \(\Phi(q)\) be the completed theta forcing on the additive half-density
coordinate.  Freeze the transform convention

\[
\tau(z)
=
\int_{\mathbb R}e^{-zq}\Phi(q)\,dq.
\]

After the declared centered-coordinate and archimedean normalization,
\(\tau(z)\) is the Xi section.

The rapid theta decay makes the integral entire in \(z\).

## Two stable histories

Define the left-stable history

\[
u_-(q;z)
=
\int_{-\infty}^{q}
 e^{z(q-r)}\Phi(r)\,dr
\]

and the right-stable history

\[
u_+(q;z)
=
-
\int_q^{+\infty}
 e^{z(q-r)}\Phi(r)\,dr.
\]

Both satisfy the same forced first-order equation

\[
(\partial_q-z)u_\pm(q;z)=\Phi(q).
\]

Their respective integration limits select the two endpoint-decaying
solutions.  Superexponential theta decay makes these histories well-defined
and holomorphic in \(z\) on compact parameter sets.

## Exact seam mismatch

At the common seam \(q=0\),

\[
u_-(0;z)-u_+(0;z)
=
\int_{-\infty}^{+\infty}
 e^{-zr}\Phi(r)\,dr.
\]

Therefore

\[
u_-(0;z)-u_+(0;z)=\tau(z).
\]

This is a source Evans identity: the Xi section is the mismatch of two
independently constructed stable histories.

## Zero-to-state gluing

If \(\tau(z_0)=0\), then

\[
u_-(0;z_0)=u_+(0;z_0).
\]

Define

\[
u(q;z_0)
=
\begin{cases}
u_-(q;z_0),&q\le0,\\
u_+(q;z_0),&q\ge0.
\end{cases}
\]

The value match removes the seam delta in the distributional derivative.
Hence \(u(\cdot;z_0)\) is a global two-ended solution of

\[
(\partial_q-z_0)u=
\Phi
\]

with both endpoint conditions.

After adjoining the constant source coordinate, the vector

\[
\binom{u(\cdot;z_0)}{1}
\]

is a nonzero kernel state of the triangular augmented history operator with
the two-ended seam domain.

This constructs the Xi-zero-to-history-state arrow without dividing by Xi.

## Chain square

Let \(i(z)\) send the theta carrier generator to the pair
\((u_-(z),u_+(z),1)\), and let \(w\) insert a scalar seam mismatch.  The
history matching operator \(C_{\rm match}(z)\) satisfies

\[
C_{\rm match}(z)i(z)=w\tau(z).
\]

This is the previously requested divisibility square on the analytic history
carrier.

## Multiplicity

The Evans mismatch is exactly \(\tau(z)\), not merely a function with the same
zero set.  Therefore its local vanishing order equals the Xi multiplicity.
Differentiating the history family with respect to \(z\) gives the associated
parameter-root chain for the matching complex.

This preserves multiplicity for the triangular history matching problem.

## What remains unresolved

The glued state solves the forced triangular equation.  It does not
necessarily satisfy the lower adjoint source equation of the paired Green
pencil.  Its Green identity retains

\[
2\operatorname{Re}z\,\|u\|^2
=
-2\operatorname{Re}\langle u,\Phi\rangle
\]

under vanishing endpoint flux.

Thus the Evans lift closes the divisor-to-state arrow for the triangular
history complex, but not the promotion from that state to the adjoint-complete
positive Green pencil.

## G4 consequence

One of the two corrected G4 residuals is now closed on the analytic history
carrier:

\[
\tau(z)=0
\Longrightarrow
\text{nonzero two-ended augmented history state}.
\]

The sole RH-bearing promotion is now the source map from this triangular
Evans state to the paired arithmetic--analytic Green kernel, including
cancellation of the forcing pairing and preservation of multiplicity.  No RH
conclusion is authorized.
