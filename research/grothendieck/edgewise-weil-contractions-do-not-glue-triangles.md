# Pairwise Weil contractions do not imply three-cell positivity

Normalize three locally positive short-support blocks so their diagonal Gram
entries are one. Suppose every normalized cross edge has magnitude at most
one, so each `2x2` principal block is positive. This does not imply positivity
of the global block matrix.

The exact hostile example is

```
G = [ 1   -3/4 -3/4 ]
    [ -3/4 1   -3/4 ]
    [ -3/4 -3/4 1   ].                                (1)
```

Every two-cell determinant is

```
1-(3/4)^2=7/16>0,                                    (2)
```

but the three eigenvalues are `7/4,7/4,-1/2`, and

```
det G=-49/32<0.                                       (3)
```

Thus even a proof of the prime-two contraction—and analogous contractions
for every individual prime-power separation—would not establish Weil
positivity.

## Arithmetic cycle gate

The first relevant cycles involve compatible logarithmic translations, for
example cells near `0`, `log p`, and `2log p`. Their edges see the first prime
shift twice and the `p^2` repetition once. Positivity requires a three-way
phase/coherence inequality, not merely bounds on the three edge norms.

This is where Adams and Mackey structure can add genuine information. The
`p^2` edge is not independent of two `p` steps: a source-derived composition
law or positive dilation must constrain their cycle holonomy. Without that
constraint, edgewise contraction data permits the hostile matrix (1).

## Revised attack sequence

1. Test the prime-two two-cell contraction as the first local falsifier.
2. If it passes, test the `0,log2,2log2` triangle including both the prime-two
   and prime-four explicit-formula contributions.
3. Seek a Mackey/Adams dilation theorem forcing every such repetition
   triangle to be positive.
4. Only then address mixed-prime cycles such as `log2,log3,log6`.

The triangle test remains source-only and finite. It prevents a collection of
successful pairwise numerics from being mistaken for an RH proof.

