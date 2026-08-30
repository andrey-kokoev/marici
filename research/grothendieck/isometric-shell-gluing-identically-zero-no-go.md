# Normalized shell gluing makes the resonance determinant identically zero

The paired gluing mechanism proposes

```
F(s)=det(I-C(1-s)C(s)),
```

which becomes `det(I-C(s)*C(s))` on the critical line. Zeros should occur
only when a prime--archimedean transfer singular value reaches one.

But the canonical weighted shell embedding `W:H_gamma->H_prime` is an
isometry by construction:

```
W*W=I.
```

If one takes `C=W`, then

```
det(I-W*W)=0
```

at every height. Dressing the map by unitary prime and gamma height flows
does not help. For

```
C(T)=U_prime(T) W U_gamma(T)*,
```

one still has `C(T)*C(T)=I`. Thus normalized covariance matching is too
perfect to be the zero-producing transfer: it puts the system permanently at
the resonance threshold.

Using the unnormalized shell map only replaces this by a height-independent
mass ratio such as `diag(m_k/g_k)`. That may define a relative covariance
determinant, but it cannot produce the oscillatory zero set.

## Required defect

The gluing operator must contain a genuinely nonunitary, height-dependent
comparison before normalization. Possible source-derived locations are:

1. the analytic-continuation defect of the first two prime channels;
2. a supported resolvent or boundary-value map rather than raw height
   evolution;
3. a coefficient--Betti mapping-cone differential whose norm is not fixed by
   the shell isometry;
4. a nontrivial Schur complement retaining the shell kernel.

The defect may not be inserted by scalar rescaling after observing Xi. It
must reduce in the Euler half-plane to the forced coefficients `1` and `1/2`
of `C_1,C_2` and satisfy the reflection-adjoint identity.

This no-go explains why covariance matching, even trace-class matching, does
not by itself approach the Riemann zeros. The spectral information lives in
the failure of prime and archimedean dynamics to intertwine, not in their
normalized static identification.

