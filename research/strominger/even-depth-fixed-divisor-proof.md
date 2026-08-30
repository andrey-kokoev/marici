# Prime-by-prime proof of the even-depth fixed divisor

For `n>=1`, define

\[
P_n(a)=a^{\overline n}=a(a+1)\cdots(a+n-1)
\]

and the fixed divisor on the positive even constructor

\[
\delta_n=\gcd_{a\in2\mathbb Z_{>0}}P_n(a).
\]

We prove

\[
\boxed{
\delta_n=
\begin{cases}
n!,&n\text{ even},\\
n!\,2^{\nu_2(n+1)},&n\text{ odd}.
\end{cases}}
\]

## Ordinary consecutive-product lemma

For unrestricted integer starts,

\[
\gcd_{a\ge1}P_n(a)=n!.
\]

Indeed

\[
P_n(a)=n!\binom{a+n-1}{n},
\]

so every value is divisible by `n!`, while `P_n(1)=n!`.

## Odd primes

Fix an odd prime `p`.  The even starts are not a restriction modulo any power
of `p`, because multiplication by two is invertible modulo `p^N`.  More
explicitly, choose `N>nu_p(n!)`.  There is a positive even `a` with

\[
a\equiv1\pmod{p^N}.
\]

For `j=0,...,n-1`, the `p`-valuation of `a+j` then equals that of `1+j`:
each nonzero valuation is below `N`, and congruence modulo `p^N` preserves it.
Hence

\[
\min_{a\in2\mathbb Z_{>0}}\nu_p(P_n(a))=\nu_p(n!).
\]

Thus every odd-primary part of `delta_n` is exactly the corresponding part of
`n!`.

## The prime two

Write an even start as `a=2x`.

If `n=2h`, exactly `h` factors are even, and

\[
\nu_2(P_{2h}(2x))
=h+\nu_2(P_h(x)).
\]

Minimizing over `x` and using the ordinary lemma gives

\[
\min_x\nu_2(P_{2h}(2x))
=h+\nu_2(h!)
=\nu_2((2h)!).
\]

If `n=2h+1`, exactly `h+1` factors are even, and

\[
\nu_2(P_{2h+1}(2x))
=h+1+\nu_2(P_{h+1}(x)).
\]

Therefore

\[
\min_x\nu_2(P_{2h+1}(2x))
=h+1+\nu_2((h+1)!)
=\nu_2((2h+2)!).
\]

Since

\[
\nu_2((2h+2)!)
=\nu_2((2h+1)!)+\nu_2(2h+2),
\]

the odd-length fixed divisor has the extra factor
`2^(nu_2(n+1))`.  Combining this with the odd-prime result proves the boxed
formula.

## Magnetic residue index

At grade `g`, put `n=g-1`.  The common transport factor is

\[
G_g=g(g+1)C_{g+1}.
\]

Hence the infinite even-depth residue index is

\[
d_g^{stable}=G_g\delta_{g-1}
=g(g+1)C_{g+1}(g-1)!
\begin{cases}
1,&g\text{ odd},\\
2^{\nu_2(g)},&g\text{ even}.
\end{cases}
\]

The extra factor is entirely constructor-derived: it records the restriction
to even starts.  It is not another rational cohomology direction.
