# Classification of the twelve pole-filtered classes

## Result

The twelve classes have the following structure:

- all belong to q-family index 2;
- four occur at each pole grade six, seven, and eight;
- they form twelve distinct exponent-parity orbit seeds;
- the set is closed under exchanging the two exponent axes.

Canonical exact row-echelon residual coordinates are recorded for every A12 class. Residual support ranges from one to 36.

Both squared-axis transports of every class remain nonzero at A14. The filtered-image ranks grow from `(640,2148,4423)` at A12 to `(843,2823,5823)` at A14 for grades six through eight, but none of the 24 transported targets enters the enlarged image.

## Claim boundary

A14 persistence does not prove persistence at every later degree because new same-grade source rows may eventually kill a class. The residual coordinates depend on the declared ordered exact row-echelon convention. The filtration remains algebraic pole order, not DNC or I-adic.

## Disposition

Test all four A16 paths and formulate an induction criterion excluding later-degree killers before claiming all-even filtered classes.

## Verification

- `research/voevodsky/check_cosmology_filtered_classification_transport.py` — exit 0
- `research/voevodsky/results/cosmology_filtered_classification_transport.json`
