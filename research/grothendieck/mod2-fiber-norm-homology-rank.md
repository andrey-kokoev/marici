# Multi-bit mod-two branch norms have residual square-zero homology

Epistemic-graph event: 1358.

## Fiber theorem

Let a finite-set quotient have `m` fibers, each of even size `d`, and use the
formal pushforward `S` and fiber trace `T` over `F_2`.  On each fiber the
source norm `N=TS` is the all-ones matrix `J_d`.  Hence

`N^2=d J_d=0`, `rank(N)=1`,

and

`dim ker(N)=d-1`.

The homology of the square-zero operator is therefore

`dim(ker N / im N)=d-2`

per fiber, and `m(d-2)` globally.

The one-bit case `d=2` is exceptional: image equals kernel and the norm
complex is acyclic.  Every larger even fiber has nonzero residual homology.

## Exact five-site census

For a `k`-bit branch collapse of `(C2)^5`,

`d=2^k`, `m=2^(5-k)`.

Thus the formal mod-two norm-homology dimensions are

| collapsed bits `k` | dimension |
| --- | ---: |
| 1 | 0 |
| 2 | 16 |
| 3 | 24 |
| 4 | 28 |
| 5 | 30 |

This refines the augmentation-filtration theorem: the norm monomial remains
nonzero and square-zero for every nonempty branch subset, but only a one-bit
collapse has no homology between its image and kernel.

## Stagewise interpretation

A simultaneous multi-bit norm contains a large residual quotient that is
invisible in the one-bit norm complexes.  It is not recovered by declaring
the terminal square-zero relation alone.  Conversely, the vanishing of
one-bit norm homology does not mean the geometric chain specialization
exists; it is a formal fiber-module calculation.

No physical relative-chain conclusion follows until the source-derived
five-site maps are available.
