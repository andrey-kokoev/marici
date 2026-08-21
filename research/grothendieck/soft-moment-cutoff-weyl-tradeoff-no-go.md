# A Weyl-sized soft moment boundary still has divergent operator leakage

Replace the hard moment projection by a diagonal taper `S_k` whose weights
fall from one to zero across `L_k` adjacent Jacobi modes. For the centered
multiplication Jacobi matrix `J`, the commutator has neighboring entries

```
[J,S_k]_(n,n+1)=a_(n+1)(w_(n+1)-w_n).
```

The Jacobi coefficients satisfy `a_n^2>=1/16`. Since the taper changes by a
total amount one, Cauchy--Schwarz gives

```
sum_transition (w_(n+1)-w_n)^2 >= 1/L_k.             (1)
```

Therefore the squared commutator leakage per shell obeys, up to the harmless
two-sided matrix convention,

```
||[J,S_k]||_2^2 >= 1/(16 L_k).                        (2)
```

After reciprocal-prime shell weighting, global Hilbert--Schmidt control
requires

```
sum_k 1/(k L_k) < infinity.                           (3)
```

But the Riemann--von Mangoldt law permits only `O(log k)` physical channels
per unit shell. If the taper width is Weyl-sized, `L_k=O(log k)`, (3)
dominates `sum 1/(k log k)` and diverges. A linear taper attains the bound in
(1), so no alternative taper profile improves the order.

## Forced null sector

A sufficient choice such as `L_k=(log k)^(1+epsilon)` uses more auxiliary
modes than the physical Weyl multiplicity and would overcount the spectrum if
they were ordinary positive states. Thus a soft-cutoff repair has only two
options:

1. abandon the Riemann zero density; or
2. place the superlogarithmic smoothing tail in a spectrally null paired
   sector whose coefficient--Betti/Krein cancellation removes it from the
   physical counting function while retaining its regularizing effect.

This makes the previously optional mapping-cone idea structurally necessary.
The physical Jacobi quotient may have logarithmic rank, but any operator-level
Hilbert--Schmidt smoothing tail must be homologically or indefinitely paired
so that it contributes zero net Weyl multiplicity.

The theorem is a lower bound for diagonal moment tapers. A non-diagonal soft
cutoff could evade it only by proving a genuinely different commutator bound;
unitary changes of moment basis alone cannot change the Hilbert--Schmidt norm.

