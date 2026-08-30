# The Krein reserve must vanish at high spectral frequency

## Bounded question

Can the parity-cone conjecture possess a uniform positive coercivity reserve,
or must every finite-order theta orbit approach its light cone?

## Order-dependent probability measure

For fixed `n`, define

\[
 N_n=\iint_{mathbb R^2}
 (u-v)^{2n}\Phi(u)\Phi(v)\,du\,dv>0
\]

and push the normalized positive density

\[
 \frac{(u-v)^{2n}\Phi(u)\Phi(v)}{N_n}\,du\,dv
\]

forward along `sigma=u+v`.  Call the resulting probability measure `mu_n`.
Then packet 124 gives

\[
 r_n(x)
 :=\frac{(2n)!\mathcal L_n[X](x)}{N_n}
 =\int_{\mathbb R}\cos(x\sigma)\,d\mu_n(\sigma).
\]

## Absolute continuity and decay

The theta source `Phi` is smooth and rapidly decreasing.  Integrating along
the affine fibers `u+v=sigma` gives `mu_n` an integrable density.  Therefore
the Riemann--Lebesgue lemma applies:

\[
 \boxed{r_n(x)\longrightarrow0\quad\text{as }|x|\to\infty.}
\]

Using `r_n=1-2p_n^-`, one obtains

\[
 \boxed{
 p_n^-(x)\longrightarrow\frac12,
 \qquad
 p_n^+(x)\longrightarrow\frac12.}
\]

Every fixed-order orbit asymptotically balances its reciprocal parities.

## No uniform coercivity

Even if the Deutsch--Popperian parity-cone conjecture is true and
`r_n(x)>=0` for every finite `x`, it necessarily satisfies

\[
 \inf_{x\in\mathbb R}r_n(x)=0.
\]

Hence no theorem of the form

\[
 \mathcal L_n[X](x)\ge c_nN_n,
 \qquad c_n>0,
\]

can hold globally on the real spectral axis.

The orbit may remain inside the causal cone at every finite position while
approaching its light cone arbitrarily closely at high frequency.  Strict
finite positivity and zero global reserve are therefore compatible and, for
the theta source, unavoidable.

## Operational meaning

This gives literal content to the earlier intuition about arbitrarily precise
probes:

\[
 \boxed{
 \text{every finite probe may show positive parity reserve, while no uniform
 finite-resolution margin exists}.}
\]

The limiting half--half balance is not a Riemann zero and does not occur at a
finite spectral point. It is an asymptotic loss of coercivity caused by phase
mixing in an absolutely continuous sum-coordinate distribution.

## Consequence for proof strategy

Norm estimates with a fixed positive gap cannot prove the hierarchy.  Any
successful argument must preserve **orientation without coercivity**—for
example by a variation-diminishing, positive-definite, or no-crossing theorem.

This also calibrates numerical evidence: small positive values at large `x`
are structurally expected and cannot by themselves indicate a nearby failure.
The exact falsifier remains a finite `x` at which `r_n(x)<0`, not decay toward
zero.
