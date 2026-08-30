# The Euler-to-theta incidence coefficient is an explicit superexponential prime-power sampling series

## Result

The source incidence between the local reciprocal Euler current and the completed-theta odd forcing can be computed without identifying their towers.

For each prime \(p\), the incidence scalar is

\[
c_p
=
2(\log p)
\sum_{k\ge1}
p^{-k/2}\Phi'(k\log p).
\]

The series converges superexponentially, splits exactly into primitive, square, and connected-tail channels, and has the correct reciprocal odd character.

Its proportionality coefficient relative to the local Euler derivative is explicit. Nonvanishing of that coefficient remains a separate monotonicity theorem.

## Source current

At grade \(k\), the Fock coefficient is

\[
a_{p,k}
=
\frac1k p^{-k/2}.
\]

The sheet-odd zero-section current paired with a signed position test \(f\) has response

\[
\nu_{p,k}^{\mathrm{odd}}(f)
=
2a_{p,k}k(\log p)f(k\log p)
=
2(\log p)p^{-k/2}f(k\log p).
\]

Take

\[
f=\Phi'.
\]

Then the full local source incidence is

\[
c_p
=
B_{\Phi'}^\times(\nu_p^{\mathrm{Euler}})
=
2(\log p)
\sum_{k\ge1}
p^{-k/2}\Phi'(k\log p).
\]

This is the authorized arithmetic-to-theta scalar. It is not the intrinsic Euler coefficient itself.

## Granularity split

The strict primitive and square contributions are

\[
c_p^{(1)}
=
2(\log p)p^{-1/2}\Phi'(\log p),
\]

\[
c_p^{(2)}
=
2(\log p)p^{-1}\Phi'(2\log p).
\]

The connected tail is

\[
c_p^{(\ge3)}
=
2(\log p)
\sum_{k\ge3}
p^{-k/2}\Phi'(k\log p).
\]

Thus

\[
c_p=c_p^{(1)}+c_p^{(2)}+c_p^{(\ge3)}.
\]

A strict two-endpoint Adams cell may use only the first two terms. The tail must remain a separate feature until a source-authorized Schur return or pushforward compresses it.

## Superexponential convergence

The completed-theta forcing and all its derivatives decay superexponentially as \(u\to+\infty\). In particular, there are constants \(A,B>0\) such that

\[
|\Phi'(u)|
\le
A\exp(-Be^{2u})
\]

for sufficiently large \(u\).

At the sampling points \(u=k\log p\),

\[
|\Phi'(k\log p)|
\le
A\exp(-Bp^{2k}).
\]

Therefore

\[
\sum_{k\ge1}
p^{-k/2}
|\Phi'(k\log p)|
\]

converges absolutely and superexponentially for every prime. The connected tail is much smaller than its bare Euler majorant.

The same estimate gives cutoff compatibility by ordinary dominated convergence on every finite-prime packet and in the previously declared projective exponential source topology.

## Reciprocal mate

Let the bilateral source current contain the two evaluations at \(\pm k\log p\) with opposite sheet signs. Since

\[
\Phi'(-u)=-\Phi'(u),
\]

the reciprocal mate pairing is invariant as a scalar contraction of two odd factors, while reversing either the current orientation or the theta normal orientation reverses the result.

Thus the mate square has the correct parity before analytic propagation:

\[
(\text{Euler odd})\otimes(\text{theta odd})
\longrightarrow
\text{scalar even}.
\]

The later Wronskian or seam-normal observer reattaches the analytic oriented line.

## Coefficient relative to the Euler normalization

The intrinsic local Euler odd coordinate is

\[
h_p^{\mathrm{Euler}}
=
\frac{(\log p)p^{-1/2}}{1-p^{-1/2}}.
\]

Hence

\[
c_p
=
\eta_p h_p^{\mathrm{Euler}},
\]

with the exact sampling coefficient

\[
\eta_p
=
2(1-p^{-1/2})
\sum_{k\ge1}
p^{-(k-1)/2}
\Phi'(k\log p).
\]

The strict two-grade coefficient is

\[
\eta_p^{(1,2)}
=
2(1-p^{-1/2})
\left[
\Phi'(\log p)
+
p^{-1/2}\Phi'(2\log p)
\right].
\]

The completed coefficient adds

\[
\eta_p^{(\ge3)}
=
2(1-p^{-1/2})
\sum_{k\ge3}
p^{-(k-1)/2}
\Phi'(k\log p).
\]

These coefficients are source-derived and cannot be replaced by one.

## Analytic outputs

After scalar incidence, the propagated vector is \(c_p\Phi'\). The two calibrated analytic ports give

\[
J_{\mathrm{Wr}}(c_p\Phi')
=
-\frac12c_p
=
-\frac{\eta_p}{2}h_p^{\mathrm{Euler}},
\]

and

\[
J_{\mathrm N}(c_p\Phi')
=
c_p\Phi''(0)
=
\eta_p\Phi''(0)h_p^{\mathrm{Euler}}.
\]

Their ratio remains the previously proved constant

\[
\frac{J_{\mathrm N}}{J_{\mathrm{Wr}}}
=
-2\Phi''(0).
\]

The prime-dependent arithmetic incidence coefficient cancels from the analytic cross-calibration.

## Nonvanishing qualification

Absolute convergence does not prove

\[
\eta_p\ne0.
\]

A cancellation among sampled grades is logically possible. Proving a uniform odd observer requires either:

- a sign theorem for \(\Phi'(u)\) on \(u>0\);
- a dominant-grade estimate at every prime;
- or a joint port that remains faithful when this scalar incidence vanishes.

The source symmetry gives \(\Phi'(0)=0\) and \(\Phi''(0)<0\), but local seam behavior alone does not prove global monotonicity.

## Next gate

The next calculation is now concrete:

> Prove that \(\Phi'(u)<0\) for \(u>0\), or directly prove that every \(\eta_p\) is nonzero with the correct cutoff-uniform normalization.

If the monotonicity theorem holds, every term in \(c_p\) has the same sign and the Euler-to-theta mate square is faithful prime by prime.
