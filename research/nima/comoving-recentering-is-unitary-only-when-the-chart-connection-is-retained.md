# Comoving recentering is unitary only when the chart connection is retained

## Two translated fronts

Let
\[
g_0(q)=e^{-\pi q^2}
\]
and define unitary translations
\[
(\tau_a f)(q)=f(q-a).
\]

Then
\[
g_t^-(q)=e^{-\pi(q-t)^2}=\tau_tg_0,
\]
and
\[
g_t^+(q)=e^{-\pi(q+t)^2}=\tau_{-t}g_0.
\]

On the two-chart bundle
\[
\mathcal H_{\mathrm{chart}}
=
L^2(\mathbb R)\oplus L^2(\mathbb R),
\]
define the comoving recentering
\[
\mathcal C_t
=
\begin{pmatrix}
\tau_t&0\\
0&\tau_{-t}
\end{pmatrix}
\]
when the ordered chart vector is \((g_t^+,g_t^-)\).

Then
\[
\mathcal C_t(g_t^+,g_t^-)
=
(g_0,g_0).
\]

Since translations are unitary,
\[
\mathcal C_t
\]
is unitary for every \(t\). No superexponential scalar calibration is required.

## Why chart labels must survive

If the two recentered copies are immediately summed,
\[
(g_0,g_0)\longmapsto2g_0,
\]
the anti-diagonal chart coordinate is killed.

The faithful target is therefore not one centered Gaussian but
\[
g_0\otimes\mathbb C^2_{\mathrm{chart}}.
\]

The analytic profile is centered while reciprocal orientation remains in the chart coefficient line:

- diagonal coefficient \((1,1)\): even overlap;
- anti-diagonal coefficient \((1,-1)\): odd orientation.

Thus recentering and orientation preservation are compatible only before chart scalarization.

## Reflection covariance

Reflection satisfies
\[
R\tau_a=\tau_{-a}R.
\]
Since \(Rg_0=g_0\), reciprocal reflection swaps the two chart coordinates after recentering.

Hence the comoving frame preserves the same diagonal/anti-diagonal character splitting as the two-ray compiler.

## The connection term

Although the recentered state is constant in \(t\), the history has not disappeared. It moves into the comoving connection.

Let
\[
D_q=\partial_q.
\]
The translation derivatives are
\[
\partial_t\tau_t=-D_q\tau_t,
\qquad
\partial_t\tau_{-t}=D_q\tau_{-t}.
\]

Therefore the covariant history derivative in the recentered frame is
\[
\nabla_t
=
\partial_t
+
\begin{pmatrix}
-D_q&0\\
0&D_q
\end{pmatrix},
\]
up to the frozen convention for active versus passive translation.

The original translated path is equivalent to a constant centered profile equipped with this opposite-sign chart connection.

The orientation data now lives in the connection generator
\[
D_q\otimes
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix},
\]
not in a displaced scalar Gaussian.

## Theta transport

Apply the exponential half-density transport to the centered analytic profile:
\[
\mathcal M_n g_0(u)
=
\sqrt n\,e^{u/2}e^{-\pi n^2e^{2u}}.
\]

Keep the chart coefficient factor:
\[
\mathcal M_n g_0
\otimes
\mathbb C^2_{\mathrm{chart}}.
\]

The completion differential then produces the exact three-grade theta packet on the analytic factor, while the diagonal/anti-diagonal chart grading remains available for the ordered seam port.

This supplies the desired contraction
\[
e^{-\pi(ne^u\pm t)^2}
\longrightarrow
e^{-\pi n^2e^{2u}}
\]
without ill-conditioned scalar evaluation: translate to the comoving frame and retain the connection.

## Endpoint history

The interval \(t\in[L,2L]\) becomes parallel transport by the flat chart connection. Its holonomy is exactly
\[
\begin{pmatrix}
\tau_L&0\\
0&\tau_{-L}
\end{pmatrix}
\]
between the recentered endpoint frames, with sign adjusted by convention.

Because translation is unitary, this holonomy is uniformly norm-preserving. The earlier completion-stable coherence concern is automatically solved at this local step.

## Hostiles

1. Recenter and sum the chart copies: orientation is erased.
2. Retain the copies but discard the connection: the endpoint path becomes falsely constant.
3. Recover the centered scalar by pointwise division of the symmetric profile: this introduces the spurious factor \(e^{\pi t^2}\).
4. Apply separate positive-ray recenterings after restriction without accounting for crossing at the origin: chart sewing is mistyped.

## Remaining theorem

The comoving chart bundle must now be compared with the source arithmetic primitive/square coefficient bundle. Specifically, prove that the opposite translation generators push forward to the frozen Adams graph character and that theta label synthesis preserves the chart coefficient grading.

## Frontier

The translated-front obstruction is reduced to a connection-intertwining theorem:
\[
D_q\otimes\operatorname{diag}(-1,1)
\longrightarrow
\text{Adams/seam odd generator}
\]
through exponential half-density transport and theta completion.
