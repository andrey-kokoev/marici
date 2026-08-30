# 3861 — Source Normalization Converts the Conductor Pole into the Physical Residue Grade

## Correction to the unnormalized Laurent analysis

Entries 3852 and 3855 retained the source analytic exponent but had not yet applied the complete dimension-dependent normalization (c_{d,n_e^{(L)},L}).

For the one-loop three-site family,

\[
n_s=3,
\qquad L=1,
\qquad n_e=3,
\qquad d=3+2\epsilon.
\]

After removing the (epsilon)-independent factor

\[
\frac{16}{9}\operatorname{Vol}\Sigma_2(P^2),
\]

the source normalization is

\[
c_{\rm red}(\epsilon)
=
\frac{\pi^\epsilon 3^{2\epsilon}}{\Gamma(\epsilon)}.
\]

Its expansion is

\[
c_{\rm red}(\epsilon)
=
\epsilon
+
\epsilon^2
\left(
\gamma_E+\log\pi+2\log3
\right)
+O(\epsilon^3).
\]

## Action on a conductor jet

Let the unnormalized conductor contribution be

\[
J(\epsilon)
=
\frac{A}{\epsilon}+B+O(\epsilon),
\]

where (A) is the conductor residue and (B) contains the endpoint logarithm and regular remainder.

Then

\[
c_{\rm red}(\epsilon)J(\epsilon)
=
A
+
\epsilon
\left[
B+A(\gamma_E+\log\pi+2\log3)
\right]
+O(\epsilon^2).
\]

Therefore

\[
\left.c_{\rm red}J\right|_{\epsilon=0}=A.
\]

## Result

The source measure has a simple zero that cancels the conductor Laurent pole. The normalized (d=3) contribution is finite and equals the intrinsic conductor residue grade.

Consequently:

- no finite counterterm is required to remove the conductor (1/\epsilon) pole at grade zero;
- the principal endpoint logarithm from Entry 3855 contributes only to the first (epsilon)-grade;
- the complicated finite remainder need not be computed to determine the normalized grade-zero conductor readout;
- the two independent residue directions of Entry 3848 are the actual grade-zero coefficient data.

The common (g_1\cap g_2) marked-wall endpoint remains separately typed. Since (K\ne0) there, it must first be removed by the source sewing of Entry 3857.

## Updated architecture

\[
\text{source Čech sewing at marked corners}
+
\text{analytic normalization at conductor costalks}
\longrightarrow
\text{finite rank-two grade-zero readout}.
\]

This is not a new Carrier stratum and not a renormalization-section ambiguity.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_source_normalization_cancels_conductor_pole.py`
- `research/benincasa/results/rank26-source-normalization-cancels-conductor-pole.json`

The checker passes four exact expansion gates.

## Next falsifier

Apply the common source factor

\[
\frac{16}{9}\operatorname{Vol}\Sigma_2(P^2)
\]

and the physical wall orientations to both conductor residues. Test whether the resulting rank-two grade-zero vector is horizontal under the fixed rank-26 Gauss–Manin connection and compatible with cyclic occurrence transport. Failure of either test rejects it as a physical coefficient readout despite its local finiteness.
