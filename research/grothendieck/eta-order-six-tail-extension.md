# The same finite eta architecture reaches the order-two corner

The next Hausdorff corner needs moments through `A_5`, hence the completed
source expansion through fifth order and eta derivatives through order six.
No larger prefix is required.

For `m=15,16`, exact rational evaluation gives

\[
 P_{m,j}(9)>0\qquad(0\le j\le6).
\]

Thus 15 Euler transforms at `N=10000` have rigorously decreasing positive
forward differences for every required derivative. The largest remainder
bound is

\[
 \frac{15!P_{15,6}(10)}{2^{15}10000^{16}}
 <1.15\,10^{-52}.
\]

This is a useful scaling result: reaching the next matrix order requires two
additional finite eta jets but neither a longer prefix nor a more elaborate
tail method. Fewer Euler transforms suffice because `10^-52` is already far
below the `10^-12` determinant-input target.

The next step is a generic truncated-series interval engine for the completed
logarithmic derivative. It should derive `A_4,A_5` mechanically rather than
introducing fragile hand-expanded formulas.

## Scope

This certifies the extended tail only. It does not yet evaluate the two new
eta derivatives or certify the order-two localizers.

## Durable verification

- Checker: `checkers/eta_order_six_euler_tail_bound.py`
- Result: `results/eta-order-six-euler-tail-bound.json`
