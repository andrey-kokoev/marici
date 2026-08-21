# Prime phases and gamma resolvents meet as Fourier transforms of measures

For every `a>0`,

```
1/(a+iT/2)
 = 2 integral_0^infinity e^(-2au)e^(-iTu)du.          (1)
```

Thus a gamma/oscillator resolvent matrix element is a Fourier transform in
the same height variable `T` used by prime phases. The difference is the
underlying log-time measure:

```
prime:          atoms at u=log p (and log p^m),
archimedean:    continuous density 2e^(-2au)du.       (2)
```

Summing (1) over even oscillator levels `a=k+1/4` gives, before the standard
endpoint subtraction,

```
2 sum_(k>=0)e^(-2(k+1/4)u)
 = 2e^(-u/2)/(1-e^(-2u)).                            (3)
```

This is the continuous archimedean log-time density behind the digamma
resolvent. The prime logarithmic derivative is the Fourier transform of the
discrete von Mangoldt measure with critical weights. Endpoint/polar terms
provide the remaining distributions at `u=0` required by completion.

## Correct non-diagonal correspondence

The source comparison should therefore be a measure/current map

```
sum_n Lambda(n)n^(-1/2) delta_(log n)
   <-->  2e^(-u/2)/(1-e^(-2u))du + endpoint terms,    (4)
```

followed by Fourier transformation in `u`. Logarithmic shells and moment
fibers are quadrature/compression devices for this measure comparison; they
are not oscillator eigenmode identifications.

This bridge explains all prior typing facts:

- exact prime phases are retained because their atom positions remain
  `log n`;
- gamma enters through resolvents, not shell-center unitary phases;
- a nonzero commutator defect is expected because discrete atoms and a
  continuous density are not diagonally intertwined;
- the completed determinant problem becomes a relative determinant of two
  Fourier-transformed measures plus endpoint distributions.

## What remains

Both sides of (4) are singular near `u=0` or at infinite prime support. A
valid coefficient--Betti mapping cone must define their common test-function
space and relative finite part, prove the reflection/Hermitian boundary
condition, and show that the resulting Fourier transform is the logarithmic
derivative of one determinant rather than a fitted distribution.

This is a source-derived kernel identity, not a spectral identification or
RH proof. It supplies the correct arena for the next finite-cutoff block.

