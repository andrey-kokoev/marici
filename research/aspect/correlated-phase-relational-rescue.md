# Correlated phase noise rescues relational coherence

## Question

Does failure of the local-product visibility law falsify the Deutschian
`2(3+2+1)+1` explanation?

## Exact correction

Let each wing acquire a random phase sign `X_A` or `X_B`. The separate
coherence calibrations measure their expectations, but the sewing analyzer
measures the expectation of their product. Therefore

\[
V_{\rm joint}=\gamma s\,E[X_A X_B],
\]

not generally

\[
\gamma s\,E[X_A]E[X_B].
\]

The product form follows only when the two phase channels are independent.

## Surprising case

For perfectly correlated unbiased flips, the two signs are jointly `++` or
`--` with equal probability. Then

\[
E[X_A]=E[X_B]=0,
\qquad
E[X_A X_B]=1.
\]

Every local coherence calibration is zero while the joint relational fringe
is fully preserved. Perfect anticorrelation also gives zero local coherence
but reverses the joint fringe.

This is not a loophole to be subtracted away. It is a direct example of the
new architecture: coherence can inhabit the relation while disappearing from
both component descriptions.

## Apparatus discriminator

Drive the two phase modulators from preregistered binary sequences in four
modes: independent unbiased, correlated unbiased, anticorrelated unbiased,
and independent biased. Record the complete phase-sign census in the same
epoch as the parity scan.

The predicted joint factors are respectively zero, one, minus one, and one
quarter. In the biased independent case each local factor is one half, so the
product law returns one quarter exactly.

An observed product-law violation counts against the constructor composition
law only after the joint sign census establishes zero covariance. Otherwise it
measures a relational environment channel.

## Disposition

The earlier falsifier is repaired: independence is now an explicit admission
gate. The correlated hostile becomes a positive relational-coherence probe.

## Verification

Run:

```text
python research/aspect/checkers/check_correlated_phase_relational_rescue.py
```
