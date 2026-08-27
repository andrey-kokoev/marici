---
id: 20260827-3299
date: 2026-08-27
status: exact-supported-jet-theorem
---

# 3299 — The First Signed-Energy Normal Grade Completes the 3 plus 1 Observer Unimodularly

## Question

Entry 3295 proves generic faithfulness of the marked quotient

\[
Q=\langle q_{\rm top},q_{\rm wall1},q_{\rm wall2}\rangle
\]

after one connection step, but its cleared determinant vanishes at the
pre-existing signed-energy support \(v=0\). This entry determines whether
that zero is repaired by the finite \(A_2\) specialization, survives as a
supported class, or is detected by a higher normal grade.

## Ordinary supported observer

At \(v=0\), retain:

- the second-Rees row \(\mu=(1,0,0)\);
- the logarithmic residue
  \[
  \rho=\operatorname{Res}_{v=0}(v\lambda_E)=(1,-1,1);
  \]
- the regular value of the transported observer
  \[
  \tau_0=(\mu R_E^T)|_{v=0}
  =\left(-1,-\frac12,\frac12\right).
  \]

These rows have rank two. Their common primitive kernel is

\[
k=(0,1,1)^T=q_{\rm wall1}+q_{\rm wall2}.
\]

The primitive finite \(A_2\) specialization of Entry 285 is carried by the
top conductor class, hence contributes another copy of \(\mu\). It has
zero value on \(k\) and does not repair this kernel.

Thus the supported zero found in Entry 3295 is real at ordinary costalk
grade, but it is not the finite \(A_2\) top class.

## First normal derivative

Differentiate the transported observer before specializing:

\[
\tau_1
=
\left.\partial_v(\mu R_E^T)\right|_{v=0}
=
\left(0,-\frac14,0\right).
\]

It detects the missing line:

\[
\tau_1(k)=-\frac14.
\]

Consequently

\[
\det
\begin{pmatrix}
\mu\\
\rho\\
\tau_1
\end{pmatrix}
=\frac14.
\]

The supported kernel is therefore not persistent. It is a class in the
first signed-energy normal grade.

## Integral primitive completion

Use Entry 3295's cleared integral transport row

\[
\tau_{\mathbb Z}(v)=(-2(v-2),2,v-2).
\]

Its conormal derivative is

\[
\delta_{\mathbb Z}
=\left.\partial_v\tau_{\mathbb Z}\right|_{v=0}
=(-2,0,1),
\qquad
\delta_{\mathbb Z}(k)=1.
\]

The integral jet observer is unimodular:

\[
\det
\begin{pmatrix}
1&0&0\\
1&-1&1\\
-2&0&1
\end{pmatrix}
=-1.
\]

Hence no supported torsion remains after adjoining the first normal grade.
The mod-two defect of generic integral eigensplitting and the signed-energy
conormal completion are different layers:

- generic reconstruction retains the half-sum conductor index two;
- at \(v=0\), the first conormal derivative supplies a primitive integral
  detector of the formerly hidden wall sum.

## Exact-sequence interpretation

Let \(O_0\) be the ordinary supported observer. Then

\[
0\longrightarrow \mathbb Z k
\longrightarrow Q_{v=0}
\xrightarrow{O_0}\operatorname{im}O_0
\longrightarrow0.
\]

The source-normal conormal symbol

\[
\delta_{\mathbb Z}:\mathbb Z k\longrightarrow
I_v/I_v^2
\]

is an isomorphism on this kernel after choosing the source normal \(v\),
because
\(\delta_{\mathbb Z}(k)=1\). The two-stage filtered observer is therefore
faithful and saturated.

This pointwise symbol has not yet been identified with a derived Bockstein or
an order-independent nearby-cycle comparison.

This is a genuine 3+1 mechanism: three source classes are seen by two
ordinary supported channels plus one conormal fallback channel.

## Classification

| Datum | Classification |
|---|---|
| ordinary kernel \(q_{\rm wall1}+q_{\rm wall2}\) | supported delayed observation |
| finite \(A_2\) top map | existing coefficient incidence, unrelated to this kernel |
| first signed-energy derivative | existing Rees/conormal calculus |
| integral jet determinant | unimodular |
| new carrier datum | none |

No physical-period statement follows. The theorem concerns the coefficient
observer before pairing with a physical relative cycle.

## Next falsifier

Construct the two iterated specialization routes at the corner \(u=v=0\):

\[
\psi_v\operatorname{gr}^{2}_{u}
\qquad\text{and}\qquad
\operatorname{gr}^{2}_{u}\psi_v.
\]

Test whether the existing marked Gauss--Manin/Rees calculus supplies a
Beck--Chevalley map carrying the conormal symbol between them. Failure would
leave only a coordinate-level pointwise completion; success would promote it
to a canonical supported filtered subquotient.

## Durable artifacts

- checker: `research/benincasa/checkers/audit_signed_energy_supported_observability_jet.py`;
- packet: `research/benincasa/results/signed_energy_supported_observability_jet.json`;
- allocator claim: `seqclaim-ea1031d4cb42ecd96ce6567d`.
