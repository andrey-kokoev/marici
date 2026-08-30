# A Syndrome Fiber Is a Homology Torsor, Not a Decoder

Fix a coefficient ring \(\mathbf Z_n\) and a finite chain complex

\[
C_2\xrightarrow{\partial_2}C_1
\xrightarrow{\partial_1}C_0,
\qquad
\partial_1\partial_2=0.
\]

For an electric syndrome (s\in\operatorname{im}\partial_1\), define its error
fiber

\[
\mathcal F_s
=
\{z\in C_1:\partial_1z=s\}.
\]

Choose one solution (z_0\). Every other solution differs from it by a cycle:

\[
\mathcal F_s=z_0+\ker\partial_1.
\]

Thus the syndrome fiber is an affine torsor over the cycle group. Local
plaquette repairs translate it by \(\operatorname{im}\partial_2\). After
quotienting those repairs,

\[
\mathcal F_s/\operatorname{im}\partial_2
\]

is a torsor over

\[
H_1=\ker\partial_1/\operatorname{im}\partial_2.
\]

There is no preferred torsor origin in the syndrome data.

## Decoder as a section

A deterministic decoder is a section

\[
D:\operatorname{im}\partial_1\to C_1,
\qquad
\partial_1D(s)=s.
\]

If (D\) and (D'\) are two decoders, then

\[
D'(s)-D(s)\in\ker\partial_1.
\]

Modulo local repairs, their difference is an (H_1\)-valued function of the
syndrome. If both decoders are linear, their difference is a linear map

\[
\operatorname{im}\partial_1\to H_1.
\]

Consequently, syndrome specifies the decoder only when an additional rule
chooses a section. Minimum weight, locality, a boundary anchor, or a trusted
logical frame can supply such a rule, but each is extra structure.

If (H_1=0), all decoders agree modulo local repairs, although they can still
choose different chain representatives. If (H_1\ne0), different decoders can
apply logically inequivalent corrections while reproducing the same syndrome
exactly.

## Exact four-class fiber

Over \(\mathbf F_2\), take

\[
\partial_1=
\begin{pmatrix}1&0&0&0\end{pmatrix},
\qquad
\partial_2=
\begin{pmatrix}0\\1\\0\\0\end{pmatrix}.
\]

Then \(\partial_1\partial_2=0\),

\[
\ker\partial_1
=
\langle e_2,e_3,e_4\rangle,
\qquad
\operatorname{im}\partial_2=\langle e_2\rangle,
\]

and

\[
H_1\simeq\mathbf F_2^2.
\]

The nonzero syndrome (s=1) has eight chain solutions. Quotienting the
two-element local repair orbit leaves four logical classes, labelled by the
(e_3,e_4\) coordinates.

Two valid linear decoder values are

\[
D_0(1)=e_1,
\qquad
D_1(1)=e_1+e_3.
\]

They have identical syndrome and differ by a nontrivial logical class.

## Joint faithfulness with logical probes

Let (R:H_1\to Y\) be a logical readout. The augmented packet

\[
(\partial_1,R)
\]

is faithful modulo local repairs exactly when (R) is injective on (H_1).
For the smallest qubit torus, two independent loop bits identify the four
classes. They do not choose a decoder unless a preferred target logical class
is separately declared.

This is the kernel-reference theorem in affine form: the syndrome map loses
precisely the homology torsor, and the reference must separate that invisible
quotient.

## Magnetic dual

The same argument applies to (X)-error chains using the plaquette syndrome

\[
\partial_2^Tx
\]

and dual local repairs. Its quotient is the corresponding cohomology torsor.
Primal--dual intersection supplies a perfect comparison of the two logical
sectors only after the quantum coefficient bicharacter is added.

## Falsifiers

- Treating a syndrome fiber as a vector space with a canonical zero.
- Calling a minimum-weight section source-free or canonical.
- Concluding logical triviality from zero syndrome.
- Adding logical probes and claiming they automatically select a correction.
- Ignoring the difference between representative ambiguity and homology
  ambiguity when (H_1=0).
- Treating an abstract decoder section as a fault-tolerant physical procedure.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to state exactly why a correct local syndrome cannot be a
decoder.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The missing information is an affine (H_1)-origin; logical probes
separate the torsor, while a decoder additionally chooses a section.
