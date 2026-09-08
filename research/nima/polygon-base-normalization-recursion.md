# Polygon base-normalization recursion

## Question

How much independent normalization data remains once every polygon facet residue factorizes into its two regional forms?

## Claim boundary

The argument propagates a declared oriented point normalization. It does not select its value or establish physical normalization.

Let `c_n` denote the overall normalization of the `n`-point top form relative to a fixed combinatorial and volume convention, and let the triangle or zero-dimensional form have value

\[
c_3=s.
\]

A chord splitting an `n`-gon into a `p`-gon and a `q`-gon has `p+q=n+2`. Multiplicative residue factorization requires

\[
c_n=c_p c_q.
\]

Taking `p=3` gives `c_n=s c_{n-1}`, hence induction yields

\[
c_n=s^{n-2}.
\]

For every other split,

\[
(p-2)+(q-2)=n-2,
\]

so the same expression satisfies all factorization constraints. Thus the tower does not require an independent normalization at every polygon size: one oriented scalar `s` determines all of them.

Changing `s` to `-s` changes the `n`-point form by `(-1)^(n-2)`. This sign cannot be removed without simultaneously fixing the point orientation and the determinant-line comparison used for residues. A coefficient convention at one higher polygon size may constrain `s`, but interpreting that convention as source normalization requires the missing source-to-volume map.

## Disposition

The base-normalization residual has been reduced to one oriented scalar. Residue recursion propagates it uniquely but supplies no value for it; source provenance and orientation authority remain necessary.
