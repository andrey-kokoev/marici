# The quarter shift derives the seven-eighths Weyl constant

The smooth zero count is governed by the Riemann--Siegel phase

```
theta(T)=Im log Gamma(1/4+iT/2) - (T/2)log pi.
```

For `z=a+it`, Stirling's formula gives

```
Im log Gamma(a+it)
 = t(log t-1) + (a-1/2)pi/2 + O(1/t).
```

Putting `a=1/4` and `t=T/2` yields

```
theta(T)/pi
 = T/(2pi) log(T/(2pi)) - T/(2pi) - 1/8 + O(1/T).
```

The argument-principle count has the separate topological base term `+1`:

```
N(T)=theta(T)/pi + 1 + S(T).
```

Hence the smooth constant is `1-1/8=7/8`.

The boundary correction is therefore not fitted. The same archimedean datum
`a=1/4` centers the even-parity shell Jacobi blocks and, through the gamma
phase, supplies the `-1/8` term. The `+1` is logically distinct: it comes from
the argument-principle base count, not gamma asymptotics.

The cumulative rank allocation may now use

```
F(T)=T/(2pi)log(T/(2pi))-T/(2pi)+7/8
```

without learning its constant from observed zeros. What remains unexplained
is precisely `S(T)`, the fluctuating zeta-argument term that the nonlocal
prime coupling must generate.

