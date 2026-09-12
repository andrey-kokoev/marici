# Odd residual charges are alternating gap products

## Closed formula

Let an odd ordered block have \(2m+1\) points and gap weights

\[
x_0,x_1,\ldots,x_{2m-1}.
\]

After choosing the boundary normalization induced by the chain cross-block profiles, its residual charges are

\[
q_{\rm out}=x_0x_2\cdots x_{2m-2},
\]

\[
q_{\rm in}=x_1x_3\cdots x_{2m-1}.
\]

For a singleton, both are empty products and equal one.

## Sewing

If odd blocks \(X\) and \(Y\) are separated by gap weight \(g\), then

\[
Z(X\star_gY)
=q_{\rm out}(X)\,g\,q_{\rm in}(Y).
\]

This is the adjacent amplitude of the combined even configuration.

Thus the entire internal odd block reduces to two alternating products. No cofactor vector is needed once its boundary normalization is fixed.

## Reversal

An odd block has an even number of gaps. Reversing their order exchanges even and odd gap positions, hence

\[
q_{\rm out}(X^{\rm op})=q_{\rm in}(X),
\qquad
q_{\rm in}(X^{\rm op})=q_{\rm out}(X).
\]

The residual Clifford swap is therefore visible directly in the gap word.

## Internal metric record

The product of the two charges is

\[
q_{\rm out}q_{\rm in}
=\prod_{i=0}^{2m-1}x_i.
\]

So the two-way residual splits the total interval weight into its two parity polarizations. Retyping does not invent the incoming/outgoing double; it separates the original gap word into its alternating factors.

## Simplified recursive representation

For the ordered chain protocol, an odd block may be represented by

```text
Residual {
  out = product(even-indexed gaps),
  in  = product(odd-indexed gaps),
  parity = odd,
  orientation
}
```

Sewing inserts the separating gap between these two alternating products. This is the smallest explicit realization of the recursive typed tuple in the finite metric model.

## Verification

The exact-rational checker verifies the formulas for 100 blocks of odd sizes one through nine:

```text
python research/coherence/check_odd_block_alternating_charges.py
```

Artifacts:

- `check_odd_block_alternating_charges.py`
- `odd-block-alternating-charges.v1.json`
