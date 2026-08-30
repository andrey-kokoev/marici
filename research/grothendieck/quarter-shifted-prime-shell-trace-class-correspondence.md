# The gamma quarter shift uniquely selects a trace-class prime-shell correspondence

On the valuation-normalized prime-ray space, the critical quadratic mass of
one prime is `1/(p-1)`. Group primes into logarithmic shells

```
S_k(c)={p: exp(k+c)<=p<exp(k+1+c)}.                    (1)
```

Their masses are

```
m_k(c)=sum_(p in S_k(c))1/(p-1).                       (2)
```

The prime number theorem with its classical zero-free-region error gives

```
m_k(c)=log((k+1+c)/(k+c))+epsilon_k,                   (3)
```

where the shell errors decay fast enough that their suitably polynomially
weighted absolute sum converges. Replacing `1/p` by `1/(p-1)` changes only an
absolutely summable sequence because `1/(p-1)-1/p=O(p^-2)`.

## Quarter-shift selection theorem

For fixed `c`,

```
log((k+1+c)/(k+c))
 =1/k-(c+1/2)/k^2+O(k^-3).                            (4)
```

The inverse covariance of the canonical even gamma oscillator is

```
g_k=1/(k+1/4)=1/k-(1/4)/k^2+O(k^-3).                  (5)
```

Matching through second order uniquely requires

```
c+1/2=1/4,
c=-1/4.                                                (6)
```

Thus the shells are

```
exp(k-1/4)<=p<exp(k+3/4).                              (7)
```

The same quarter shift already forced by oscillator parity and the gamma
factor now fixes the origin of the prime logarithmic shells; it is not a
fitted cutoff constant.

## Trace-class relative covariance

With `c=-1/4`, equations (3)--(5) imply

```
m_k(-1/4)/g_k-1=O(k^-2)+weighted epsilon_k.            (8)
```

Therefore the diagonal relative covariance operator

```
R=diag_k(m_k(-1/4)/g_k)-I                              (9)
```

is trace class. An ordinary relative Fredholm determinant is available for
the shell-radial covariance comparison.

Without the shifted shell origin, `c=0` gives a `1/k` relative discrepancy:
the comparison is only Hilbert--Schmidt and requires `det_2`. Hence the
quarter shift upgrades the determinant class by one full Schatten order.

## Weighted many-to-one correspondence

Inside shell `k`, define the normalized radial vector

```
eta_k=m_k^(-1/2) sum_(p in S_k) (p-1)^(-1/2)e_p.       (10)
```

Distinct shells are orthogonal. The map sending oscillator basis vector
`e_k` to `eta_k` is an isometry onto the shell-radial prime subspace, despite
the large prime multiplicity. The orthogonal complement records within-shell
arithmetic fluctuations rather than being falsely identified with gamma
modes.

Compression of the prime covariance to the radial subspace gives `m_k`; its
comparison with `g_k` is exactly (9). This resolves the previous rank/trace
conflict at the price of a nonunitary many-to-one correspondence and an
explicit residual fluctuation sector.

## What remains

The trace-class theorem concerns only the quadratic shell covariance. The
linear Euler cross entry depends on individual phases `exp(-iT log p)` and
von Mangoldt coefficients. Shell compression must not replace them by one
average frequency. A completed block needs both:

1. the trace-class radial prime--gamma covariance comparison;
2. the orthogonal within-shell sector carrying exact prime fluctuations and
   the linear Euler functional.

The relative determinant of (9) alone is nonzero wherever its covariance
ratios are positive and cannot be Xi.

## Falsifiers and next target

A proposal fails if it uses unshifted shells while claiming ordinary
trace-class relative covariance, discards the within-shell complement, or
identifies the radial determinant with Xi. The next target is the block
decomposition of the exact Euler cross functional into radial and fluctuation
parts and a proof that the fluctuation coupling is Hilbert--Schmidt after the
quarter-shifted compression.

This is a source-derived many-to-one covariance theorem, not the completed
determinant or an RH proof.
