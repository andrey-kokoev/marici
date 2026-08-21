# Mixed-prime rectangle positivity splits into two parity contractions

For the real normalized rectangle with vertices
`0,log p,log q,log(pq)`, write horizontal and vertical correlations as
`r,s` and the two diagonal correlations as `c,d`:

```
G = [ 1  r  s  c ]
    [ r  1  d  s ]
    [ s  d  1  r ]
    [ c  s  r  1 ].                                  (1)
```

Reorder the vertices into opposite pairs and take even/odd combinations.
The matrix becomes the direct sum

```
G_+ = [1+c  r+s],       G_- = [1-c  r-s].            (2)
      [r+s  1+d]              [r-s  1-d]
```

Consequently, rectangle positivity is equivalent to the two parity
conditions

```
(1+c)(1+d) >= (r+s)^2,
(1-c)(1-d) >= (r-s)^2,                               (3)
```

together with the nonnegative diagonal conditions for the two blocks.

## Exact Mackey tensor case

If coprime interchange is exact, `c=d=rs`. Both parity determinants reduce
to

```
(1-r^2)(1-s^2),                                      (4)
```

and the full determinant is its square. Thus the tensor theorem is recovered.

## Holonomy interpretation

The average `(c+d)/2` measures the direct composite edge; the difference
`(c-d)/2` measures route/orientation holonomy between the two diagonals. The
two inequalities in (3) separately constrain its even and odd parity
channels. Bounds `|r|,|s|,|c|,|d|<=1` on individual edges are insufficient.

This gives the exact first mixed-prime source test. Compute the four
normalized cross forms from the completed Weil distribution on a common
short-support basis and test both parity blocks. Failure of either one
produces a finite negative Weil square. Success supplies the first
coprime-Mackey rectangle but still does not control larger nonchordal cycles.

For complex/operator-valued correlations the parity decomposition requires
the appropriate adjoints and may leave noncommuting block entries. The real
formula is the finite scalar falsifier that any such extension must recover.

