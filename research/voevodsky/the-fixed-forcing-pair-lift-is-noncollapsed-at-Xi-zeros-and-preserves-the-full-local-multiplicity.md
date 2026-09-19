# The fixed-forcing pair lift is noncollapsed at Xi zeros and preserves the full local multiplicity

The completion-injectivity question is already settled on the divisor-bearing
Evans lane, though not for the entire five-cell module.  Fix the theta forcing
`Phi` and define

\[
\Delta_\pm(z)=\Phi\otimes u_\pm(z).
\]

The exact history mismatch

\[
u_-(q;z)-u_+(q;z)=e^{zq}\tau(z)
\]

gives

\[
\Delta_-(z)-\Delta_+(z)
=\tau(z)\bigl(\Phi\otimes e^{zq}\bigr).
\]

Hence the two pair lifts agree modulo the Xi ideal.  If `tau` has order `m` at
`z_0`, their derivatives agree through order `m-1`; the order-`m` mismatch is
controlled by `tau^(m)(z_0)`.  The one-leg map therefore preserves the complete
local multiplicity rather than merely the zero set.

Noncollapse at the divisor follows from the actual correlation history, not
from a diagonal-ray argument.  For the glued state `u_z`, let

\[
\rho_z(t)=\int_{\mathbb R}\Phi(x)u_z(x+t)\,dx.
\]

Its Fourier transform is

\[
\widehat\rho_z(\xi)
=
\frac{\widehat\Phi(-\xi)\widehat\Phi(\xi)}{i\xi-z},
\]

with the removable interpretation at a common zero.  Since `Phi_hat` is a
nonzero entire function, the numerator is nonzero on an open dense subset of
the real axis.  Therefore `rho_z` is not identically zero.  The pair class
`[Phi tensor u_z]` survives the common-history interval-cycle quotient, and the
canonical codiagonal remains injective on this source-generated class.

Thus, for the Xi-relevant fixed-forcing lane:

- divisor-preserving pair lift: constructed;
- local multiplicity preservation: established;
- noncollapse after the cycle quotient: established;
- positive source-pulled energy on the lifted class: established.

What remains open is broader and genuinely quadratic: completion estimates for
the whole relative family and five-cell module, and identification of the
source-polarized four-entry coefficient Green form with the analytic Green
boundary form.  The missing correction is no longer a state-existence or
multiplicity problem on the Xi lane; it is the Green polarization/balance
comparison.
