# Shell ranks must be allocated cumulatively, not rounded locally

The Weyl density suggests

```
rho(t)=(1/(2 pi)) log(t/(2 pi)).                    (1)
```

But a shell dimension must be an integer. Defining
`m_k=floor(rho(k))` independently loses a fractional part of order one in
each shell. The accumulated error is generically `O(T)`, large enough to
corrupt the linear term `-T/(2 pi)` in the Riemann--von Mangoldt law.

The stable allocation is cumulative. Let

```
F(T)=T/(2 pi) log(T/(2 pi))-T/(2 pi)+C             (2)
```

on the range where it is increasing, and define

```
m_k = floor(F(k+1))-floor(F(k)).                    (3)
```

Then every `m_k` is a nonnegative integer and telescoping gives

```
sum_(k=K)^(N-1) m_k = floor(F(N))-floor(F(K)),       (4)
```

so the total discrepancy is uniformly bounded rather than linear. This is
a Beatty/Sturmian-style distribution of the fractional channel density among
neighboring shells. It preserves both leading smooth Weyl coefficients.

## The constant-term gate

Choosing `C=7/8` reproduces the smooth completed-zeta count, but doing so by
hand merely copies the answer. Phase-space area gives `C=1`; the missing
`-1/8` must arise from a source-derived boundary/Maslov correction. The
cumulative rule can transport that correction once derived, but cannot
explain it.

Thus the shell architecture has a precise integer form:

- phase-space geometry derives the continuous cumulative law;
- boundary/parity geometry must derive its constant;
- cumulative differencing turns it into finite shell ranks without changing
  the linear coefficient;
- local rounding is prohibited.

This also clarifies that shell rank is not a smooth dimension assigned one
shell at a time. It is an increment of a global spectral counting object,
already hinting that the required coefficient--Betti coupling is nonlocal.

