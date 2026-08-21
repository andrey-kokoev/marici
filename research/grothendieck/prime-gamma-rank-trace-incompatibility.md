# The simple gamma oscillator cannot match prime rank and covariance simultaneously

At cutoff `P`, the colored source has at least `pi(P)~P/log P` independent
prime-ray directions. Matching its covariance divergence with the
quarter-shift oscillator requires only

```
K_trace(P)~log P,                                      (1)
```

since `sum_(k<K)1/(k+1/4)~log K~log log P`.

A finite-cutoff unitary or Bogoliubov comparison instead requires

```
K_rank(P)>=pi(P).                                      (2)
```

These conditions are incompatible. Conversely, using `K=pi(P)` makes the
oscillator covariance grow as

```
log pi(P)=log P-log log P+o(1),                        (3)
```

which is much larger than the prime `log log P` divergence.

## Projection/Schatten obstruction

For finite-rank support projections `E_P,F_P`,

```
||E_P-F_P||_2^2 >= |rank(E_P)-rank(F_P)|.              (4)
```

With ranks `pi(P)` and `floor(log P)`, the lower bound diverges. Therefore
matching scalar covariance traces cannot establish Shale--Stinespring
implementability or quasi-free equivalence; it has forgotten multiplicity.

The earlier scalar prime--oscillator subtraction remains valid, but it is not
an equivalence of one-particle representations.

## Surviving repairs

The archimedean reference must gain at least one of:

1. source-derived multiplicities comparable to prime counts in logarithmic
   shells;
2. a weighted many-to-one Hilbert correspondence instead of a unitary;
3. a Krein space with a large null sector removed after pairing;
4. a relative determinant that compares forms without identifying support
   projections.

Arbitrary oscillator multiplicities would change its spectral zeta function
and destroy the gamma determinant. A many-to-one map must expose its fiber
norm and weighted Mackey degree.

## Falsifiers and next target

A proposal fails if it infers Bogoliubov implementability from matching trace
asymptotics while ignoring ranks, or raises the oscillator cutoff to `pi(P)`
without recomputing covariance and the gamma determinant.

The next target is a weighted correspondence from prime rays to logarithmic
oscillator shells. Its fiber norm must reproduce the prime covariance while
its induced archimedean determinant remains the quarter-shift gamma factor.

This theorem falsifies only the simple gamma quasi-free comparison, not every
relative determinant or RH.
