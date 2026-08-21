# Three-cell positivity is exactly contractivity of the Adams composition defect

For three normalized local Weil blocks, write the Hermitian Gram matrix as

```
G = [ 1   a   c  ]
    [ a*  1   b  ]
    [ c*  b*  1  ].                                   (1)
```

Here `a` and `b` are consecutive cross-block correlations and `c` is the
direct two-step correlation. Its determinant is

```
det G
 =1-|a|^2-|b|^2-|c|^2+2 Re(a b c*).                 (2)
```

Completing the square gives the exact identity

```
det G
 =(1-|a|^2)(1-|b|^2)-|c-a b|^2.                    (3)
```

Assuming the two edge contractions `|a|,|b|<=1`, the triangle is positive if
and only if

```
|c-a b|^2 <= (1-|a|^2)(1-|b|^2).                    (4)
```

Thus the direct edge need not equal the composite edge. Its defect must fit
inside the product of the two local contraction deficiencies.

## Adams/Mackey interpretation

For cells at `0,log p,2log p`, the consecutive edges are the first prime
translation and the direct edge includes the `p^2` repetition. Define the
normalized cycle defect

```
kappa_p=(c_p2-a_p^2)/(1-|a_p|^2)                    (5)
```

in the translation-invariant scalar case. Triangle positivity is precisely
`|kappa_p|<=1`. Exact Adams composition `c_p2=a_p^2` gives `kappa_p=0` and
makes positivity automatic, but the more general contraction bound permits a
controlled source anomaly.

This is the first universal coupled positivity theorem at cycle level. It is
not termwise positivity: a possibly signed prime-power edge is allowed, but
its failure to equal the Mackey composite is quantitatively bounded by the
unused positivity of the adjacent blocks.

## Operator target

For operator-valued blocks, (3) becomes the Schur/Parrott completion problem.
After defect-space normalization, the direct edge must have the form

```
C=A B + D_(A*) K D_B,          ||K||<=1,              (6)
```

with the appropriate left/right defect operators. The scalar identity fixes
the exact finite falsifier; an operator theorem must specify domains and
ordering rather than commute the blocks silently.

The next computation is now sharply defined: evaluate `a_2` and `c_4` from
the prime--gamma Weil form on a common short-support basis and test (5), not
merely the separate edge norms.

