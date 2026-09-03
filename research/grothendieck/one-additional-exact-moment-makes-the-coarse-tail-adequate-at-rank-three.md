# One additional exact moment makes the coarse tail adequate at rank three

## Tail split comparison

Using the correct undilated variation `5184`, the coarse eighth-order tail widths are:

| split `N` | one-cell tail width | crude three-cell row sum |
|---:|---:|---:|
| 3 | 0.4774991580 | 1.432497474 |
| 4 | 0.06101536587 | 0.1830460976 |
| 5 | 0.01231260822 | 0.03693782465 |

The repaired rank-three scout has minimum eigenvalue approximately

`0.6204848787`.

At `N=4`, even the crude row-sum perturbation `0.18305` leaves an order `0.437` spectral reserve before finite-prefix interval widths.

## Consequence

Rank three does not require signed-atomic tail reconstruction. It requires only one additional exact undilated moment, at

`b=3+1/4=13/4`,

beyond the already checked `n=0,1,2` prefix. The finite-gamma formula handles this moment without a new analytic method.

At `N=5`, the coarse tail becomes small enough that finite-prefix widths should dominate, but `N=4` is the minimal efficient target indicated by the present margins.

## Acceptance test

1. Verify the closed `n=3` moment against direct quadrature for baseline, lag one, and lag two.
2. Assemble directed `N=4` intervals for all three Toeplitz cells.
3. Bound the symmetric matrix perturbation by its maximum interval row sum.
4. Certify the minimum eigenvalue remains positive.

## Disposition

The c=1 repaired programme has an executable rank-three interval target with no signed-atom dependency: exact prefix through `n=3` plus coarse variation tail.
