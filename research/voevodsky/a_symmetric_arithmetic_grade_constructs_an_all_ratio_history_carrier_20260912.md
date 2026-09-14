# A symmetric arithmetic grade constructs an all-ratio history carrier

## Question

Can the fixed-ratio completed histories be assembled into one continuous all-ratio map without choosing an asymmetric numerator or denominator weight?

## Claim boundary

Yes as a mathematical source construction. Index reduced positive ratios by coprime pairs \((a,b)\), consecutive-prime shells by \(j\), and theta multiplicity by \(k\). Define

\[
W_{\mathrm{all}}(a,b;j,k)
=
\log(abkp_jp_{j+1}).
\]

This is a proper, reciprocal-invariant grade. It constructs a projective source and a Hilbert direct-sum history target. It is not claimed to be a physical covariance, an observer probability, or the unique global completion.

## Properness and reciprocity

For any cutoff \(R\), the condition

\[
abkp_jp_{j+1}\leq e^R
\]

admits only finitely many positive integer tuples; imposing \(\gcd(a,b)=1\) and consecutive primality restricts that finite set. Exchanging \(a\) and \(b\) leaves the grade fixed.

Define

\[
\mathcal C_{\mathrm{all},\exp}
=
\bigcap_{\delta>0}
\ell^1\!\left(E_{\mathrm{all}},e^{\delta W_{\mathrm{all}}}\right).
\]

Restriction to one ratio block recovers the earlier normalized topology up to the additive constant \(\log(ab)\).

## Target and bound

Let

\[
\mathcal H_{\mathrm{all}}
=
\ell^2_{(a,b)=1}
\bigl(L^2(\mathbb R_+)\bigr).
\]

For a finite packet \(c=(c_{a,b})\), apply the completed history separately in each ratio block. The fixed-block column estimate gives

\[
\|B_{a,b}c_{a,b}\|_2
\leq
K_\delta q_\delta^{a,b}(c_{a,b}),
\qquad
K_\delta=
\frac{\|\Phi_1\|_\infty\|\Phi_1\|_2}{\delta}.
\]

Since the all-ratio weight dominates the normalized block weight,

\[
q_\delta^{a,b}(c_{a,b})
\leq q_\delta^{\mathrm{all}}(c_{a,b}).
\]

Using \(\|(x_r)\|_{\ell^2}\leq\|(x_r)\|_{\ell^1}\),

\[
\|B_{\mathrm{all}}c\|_{\mathcal H_{\mathrm{all}}}
\leq
K_\delta q_\delta^{\mathrm{all}}(c).
\]

Finite-support packets are dense by weighted-\(\ell^1\) tail truncation. Therefore the blockwise map extends uniquely to

\[
\widehat B_{\mathrm{all}}:
\mathcal C_{\mathrm{all},\exp}
\longrightarrow
\mathcal H_{\mathrm{all}}.
\]

## Reciprocal action

Reciprocity exchanges the \((a,b)\) and \((b,a)\) Hilbert summands and the corresponding source coefficients. It is an isometry for every source seminorm and for the target norm, and it intertwines \(\widehat B_{\mathrm{all}}\) with the block exchange.

## Metaphysical boundary

This construction shows that the ratio blocks can coexist in one coherent completed carrier without selecting one ratio as fundamental. The counting direct sum means only square summability across declared arithmetic sectors. It does not make the ratio index physical time, assign Born weights, or prove that nature uses this completion.

## Disposition

The previously open all-ratio topology now has an explicit symmetric candidate with a continuous history map. The remaining noncanonical choice is the cross-ratio grade itself: other reciprocal-invariant proper grades may define inequivalent global completions unless coarsely comparable to \(W_{\mathrm{all}}\). Cycle-port calibration remains independent.
