# The P4 endpoint readout is one alternating prime cross-ratio

## Readout

Use the actual logarithmic shifts for the ordered frame

\[
(p_0,p_1,p_2,p_3)=(2,3,5,7)
\]

and the oriented operator-valued two-cochain

\[
\mathcal F_{ij}=K_{j,i}-K_{i,j}.
\]

For

\[
\mathcal Q_4
=
\{\mathcal F_{01},\mathcal F_{23}\}
-
\{\mathcal F_{02},\mathcal F_{13}\}
+
\{\mathcal F_{03},\mathcal F_{12}\},
\]

take the physical endpoint trace

\[
\rho_0(\mathcal Q_4)f=(\mathcal Q_4f)(0).
\]

Direct symbolic propagation through the half-line support conditions reduces all terms to one evaluation:

\[
\boxed{
(\mathcal Q_4f)(0)
=
f\!\left(-\log2+\log3-\log5+\log7\right).
}
\]

Equivalently,

\[
(\mathcal Q_4f)(0)
=
f\!\left(\log\frac{3\cdot7}{2\cdot5}\right)
=f\!\left(\log\frac{21}{10}\right).
\]

## Meaning

The fourth-rank readout does not return a sum of four independent prime observations. It returns their alternating multiplicative ratio:

\[
\frac{p_1p_3}{p_0p_2}.
\]

Its valuation vector is

\[
(-1,+1,-1,+1),
\]

which has signed word depth four. This is exactly why the coordinate appears in \(\Gamma_4^+\) but not in the positive subset-sum cube.

The result ties together the three structures under investigation:

1. the prime indices form valuation vectors;
2. half-line comparison introduces signed directions;
3. the four-dimensional cup closes to an alternating cross-ratio.

Thus a concrete candidate for fourth-rank observation is

\[
\boxed{
P^4(p_0,p_1,p_2,p_3)
=
\log\frac{p_1p_3}{p_0p_2},
}
\]

not as a universal definition, but as the endpoint shadow selected by this ordered half-line incidence system.

## Invariances

The alternating vector sums to zero:

\[
-1+1-1+1=0.
\]

Therefore common multiplicative rescaling of all four labels cancels. The readout measures relative configuration rather than absolute scale. Reversing the orientation exchanges numerator and denominator and negates the logarithmic coordinate.

These are cross-ratio-like properties arising from the source transport rather than being imposed afterward.

## Scope

The simplification uses the order and inequalities among \(2,3,5,7\). Other ordered quadruples can occupy different half-line support chambers and should be computed piecewise. The invariant object is the operator-valued four-cup; the single evaluation at \(\log(21/10)\) is its endpoint shadow in this chamber.

## Verification

Run:

```text
python research/coherence/check_log_prime_p4_endpoint_readout.py
```

Artifacts:

- `check_log_prime_p4_endpoint_readout.py`
- `log-prime-p4-endpoint-readout.v1.json`
