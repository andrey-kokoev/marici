# The shell-center unitary surrogate has a quadratic resonance lattice

> **Scope correction.** The “gamma comparator” below is the unitary
> shell-center phase, not the resolvent family defining
> `Gamma(1/4+iT/2)`. This is an aliasing theorem, not a gamma or Xi
> singularity.

The static quarter-shifted covariance comparison is trace class, but the
quadratic prime channel at height `T` carries phase `p^(-2iT)`. In shell
`[-1/4,3/4]`, its leading PNT average is

```
e^(-2iTk)/k integral_(-1/4)^(3/4) e^(-2iTr)dr
 = e^(-2iTk)e^(-iT/2) sinc(T)/k.                    (1)
```

The centered unitary shell surrogate has leading term

```
e^(-2iTk)e^(-iT/2)/k.                                (2)
```

Hence the leading relative discrepancy is

```
[sinc(T)-1] e^(-2iTk)e^(-iT/2)/k.                    (3)
```

At `T=0`, the coefficient vanishes and the earlier trace-class covariance
theorem is recovered. For generic real `T` not in `pi Z`, the shell series is
only conditionally convergent by oscillation, not absolutely trace class. At
every nonzero resonance height `T=n pi`, the outer shell phase is one while
`sinc(n pi)=0`, so (3) becomes a nonzero constant times `1/k` and diverges
harmonically.

Thus static covariance matching does not extend through this unitary
shell-center surrogate. Its logarithmic resonances diagnose aliasing;
completed Xi and the actual gamma resolvent do not inherit them.

## Coupled-anomaly consequence

The resonance lattice must be removed by retaining within-shell information
before comparison with the gamma resolvent. It need not be canceled by an
opposite physical singularity. A proposal fails if it promotes this surrogate
periodicity to the completed determinant.

The result also explains why the single-Schur-operator requirement is not
merely aesthetic. The two low-order channels must share one continuation
because neither has an admissible global scalar continuation on its own.
