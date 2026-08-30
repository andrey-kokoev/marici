# A Krein graph completion unifies local signs, contractivity, and global zeros

Let `H_A` and `H_P` be Hilbert spaces representing positive archimedean and
negative prime bookkeeping sectors. Equip

```
K=H_A direct_sum H_P
```

with the Krein form

```
[(a,p),(b,q)]_K=<a,b>_A-<p,q>_P.                      (1)
```

For a coupling operator `C:H_A->H_P`, consider its graph

```
Gamma_C={(a,Ca):a in H_A}.                             (2)
```

The induced form on completed states is

```
[(a,Ca),(b,Cb)]_K
 =<a,(I-C*C)b>.                                        (3)
```

Therefore:

```
Gamma_C nonnegative  iff  ||C||<=1,
Gamma_C positive     iff  I-C*C>0,
Gamma_C has a null state iff 1 is a singular value of C.                (4)
```

In finite dimension, the Gram determinant of the graph is

```
det(I-C*C),                                            (5)
```

exactly the global gluing determinant on the critical line.

## Interpretation of the source sign obstruction

The negative diagonal of every raw prime Herglotz contribution is no longer
expected to be positive by itself. It belongs to the negative leg of (1).
Endpoint and gamma completion define the positive leg and the coupling
constraint. Positivity is a theorem about the completed graph, not about an
orthogonal sum of local positive sectors.

This supplies the minimal algebraic architecture consistent with all prior
sign audits:

```
indefinite local bookkeeping
       + global coupling graph
       = positive completed state space when C is contractive.           (6)
```

## Boundary zeros and quotient

At a unit singular value, the graph form acquires a null vector. Quotienting
by the null space yields a positive Hilbert space, while the lost direction
records the determinant zero and its multiplicity. This is analogous to
physical-state constructions from an indefinite auxiliary space, but no
physical interpretation is asserted here.

## Holomorphic extension

Away from the critical line, `C*C` is nonholomorphic. The global analytic
family must remain

```
I-C(1-s)C(s),                                          (7)
```

which becomes (3) only on `1-s=conj(s)`. The Krein graph theorem controls
the fixed-line metric; it does not by itself prove off-line contractivity or
construct the analytic determinant.

## Physical limitation and falsifier

This is an algebraic Hilbert/Krein theorem. The prime and gamma source
spaces, the coupling map, and the physical relative-chain pushforward remain
unconstructed. A proposed completion fails if its graph contains a vector
with `||Ca||>||a||`, because the induced norm is then negative.

