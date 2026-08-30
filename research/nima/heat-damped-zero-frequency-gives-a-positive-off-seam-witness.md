# Heat-damped zero frequency gives a positive off-seam witness

Event 10281 made first-jet faithfulness conditional on meromorphic
continuation. For zero exclusion, a weaker positive witness is available.

For an off-seam reciprocal pair \((d,\gamma)\), the normal-jet kernel has

\[
\widehat K_{d,\gamma}(\xi)
=
-2\pi|\xi|e^{-d|\xi|}e^{-i\gamma\xi}.
\]

For a finite off-seam divisor packet,

\[
\widehat D_\perp(\xi)
=
-2\pi|\xi|
\sum_j m_j e^{-d_j|\xi|}e^{-i\gamma_j\xi}.
\]

Dividing by \(-2\pi|\xi|\) and taking \(\xi\to0\) gives

\[
\lim_{\xi\to0}
\frac{\widehat D_\perp(\xi)}
{-2\pi|\xi|}
=
\sum_jm_j.
\]

Because \(m_j>0\), this limit vanishes if and only if the finite packet has no
off-seam reciprocal pairs. No meromorphic continuation is needed for this
finite theorem.

## Completion by height damping

The full divisor has infinite mass, so the zero-frequency limit must be
regularized before completion. Apply a source-authorized positive height
weight, for example

\[
w_\eta(\gamma)=e^{-\eta\gamma^2},
\qquad \eta>0,
\]

to each divisor atom before assembling the normal jet. Then

\[
\widehat D_{\perp,\eta}(\xi)
=
-2\pi|\xi|
\sum_j
m_j e^{-\eta\gamma_j^2}
e^{-d_j|\xi|}
e^{-i\gamma_j\xi}.
\]

The damped count is finite under the standard zero-counting growth, and

\[
M_\eta
=
\lim_{\xi\to0}
\frac{\widehat D_{\perp,\eta}(\xi)}
{-2\pi|\xi|}
=
\sum_jm_j e^{-\eta\gamma_j^2}.
\]

Therefore

\[
M_\eta\ge0,
\]

and for any \(\eta>0\),

\[
M_\eta=0
\]

if and only if there are no off-seam zeros.

This is an exact positive RH witness after divisor identification.

## Typing warning

The height weight must act on the divisor/spectral labels before the kernels
are summed. Multiplying the assembled \(t\)-distribution by a Gaussian is a
different operation and does not yield the displayed formula.

Thus source authority requires a functional-calculus square:

\[
\text{polarized divisor}
\to
\text{height heat weight}
\to
\text{normal jet}
\]

intertwining the corresponding arithmetic constructor. The existing
quarter-heat carrier is a natural candidate, but the intertwiner must be
proved rather than inferred from the appearance of a Gaussian.

## Relation to the Green programme

The witness \(M_\eta\) is not yet an RH proof because constructing it from
prime data still requires the polarized divisor-identification arrow.
However, once that arrow exists, the final zero-exclusion test is much
simpler than full divisor reconstruction:

\[
\text{RH}
\quad\Longleftrightarrow\quad
M_\eta=0.
\]

Equivalently, any off-seam reciprocal pair creates strictly positive
heat-damped Neumann mass.

This converts the sign-changing pointwise kernel \(K_d\) into a positive
global observable through the zero-frequency boundary-flux coefficient. It
is a concrete candidate for the completion-stable “no invisible states”
port.
