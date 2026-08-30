# Cauchy boundary vectors come from one-sided logarithmic exponentials

Epistemic-graph event: 1440.

## Source test vectors

Fix the Fourier convention

\`G(gamma)=integral_R g(u)exp(-i gamma u)du\`.

For \`z\` with \`Im(z)>1/2\`, define the one-sided logarithmic vector

\`g_z(u)=i exp(i z u)1_(u>=0)\`.

It decays exponentially and

\`G_z(gamma)=1/(gamma-z)\`.

Thus the formal Cauchy feature used in Ledger 1395 is not inserted from the
zero set. It is the transform of a canonical half-line Mellin boundary mode.

## Euler-domain convergence

Approximate \`g_z\` by smooth compactly supported half-line functions. For
\`Im(z)>1/2\`, the prime samples in the Weil pairing converge absolutely,
because their envelopes are powers \`n^(-1/2-Im(z))\`. The archimedean and
endpoint distributions extend by their standard continuity to these
exponentially decreasing vectors.

Hence the Weil form has a canonical sesquilinear extension on the span

\`E={finite sums of g_z: Im(z)>1/2}\`.

This is exactly the half-plane where the source Euler trace and the
theta-completed Weyl function can be compared without continuation of the
prime series.

## Kernel identity

For \`z,w\` in this domain, the extended explicit formula gives

\`<g_z,g_w>_W
=K_Xi(z,w)
=[M_Xi(z)-conj(M_Xi(w))]/[z-conj(w)]\`.

On the spectral side this is the Cauchy Gram sum. On the arithmetic side it is
the divided difference of the completed logarithmic derivative, with the
gamma, endpoint, and absolutely convergent prime-power terms all retained.

Therefore the assignment

\`g_z -> k_z\`

defines an exact isometry of Hermitian pre-spaces from the Euler-domain Weil
quotient into the Xi Pick preshape of Ledger 1391. It uses only the
Mellin half-line mode, theta completion, and intrinsic prime distribution.

## What remains beyond the Euler domain

The construction does not yet yield a positive Hilbert operator:

- the form can be indefinite;
- extension from \`Im(z)>1/2\` to all \`Im(z)>0\` uses analytic continuation;
- closability of multiplication by the spectral coordinate is conditional on
  the completed form; and
- compact resolvent follows only after positive Herglotz realization.

If RH holds, the Pick kernel is positive and its kernel vectors are total by
the reproducing-kernel construction. The isometry then extends from the span
of \`g_z\` to the completed Weil/Pick Hilbert space. Without RH, the same map
exists only between indefinite preshapes.

## Source-boundary interpretation

This supplies the previously missing comparison map at the analytic source
level:

\`one-sided Mellin boundary modes
 -> Weil prime--gamma quotient
 -> Xi Pick boundary vectors\`.

It is not a physical relative-chain pushforward, and it does not identify the
paired coefficient--Betti lattice with the analytic test space. But it proves
that the analytic boundary vectors themselves are derived from the
Mellin-dilation half-line rather than postulated from zeros.

## Scope

This is an exact Euler-domain comparison and an indefinite isometry on the
Cauchy span. Positivity, full upper-half-plane closure, and physical
coefficient--Betti realization remain open.
