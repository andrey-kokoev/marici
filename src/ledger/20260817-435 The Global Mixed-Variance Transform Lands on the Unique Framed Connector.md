---
id: 435
date: 2026-08-17
title: The Global Mixed-Variance Transform Lands on the Unique Framed Connector
---

# The Global Mixed-Variance Transform Lands on the Unique Framed Connector

Entries 430–434 provide all pieces of the correctly typed left leg. They now
assemble into a global mixed-variance integral transform in the fs/Kato sector.

An object on the normalization–conductor Milnor square is a diagram
\[
M_+\longrightarrow M_c\longleftarrow M_-.
\]
Pull it to the three-chart V/Čech correspondence and form the conductor
difference totalization
\[
\mathcal K(M)=
\left[p_+^*M_+\oplus p_-^*M_-
\xrightarrow{\epsilon_+-\epsilon_-}p_c^*M_c\right].
\]
Tensor with the exceptional logarithmic relative-dualizing packet and the
external Cartier packet, then apply normalized blowdown and Čech descent:
\[
\Phi(M)=
R q_!\left(
\mathcal K(M)\otimes^L\omega_q^{\log}
\otimes^L\mathcal C_{\rm Cartier}
\right).
\]
This formula is mixed-variance through the conductor restrictions; it does not
pretend that \(p\) is an ordinary ringed-space morphism.

For the distinguished normalization-sheet object
\((A_+\to C\leftarrow A_-)\), every component has already been independently
fixed. The integrated audit reruns the universal conductor kernel, all 215
multi-Rees stalks, 522 localization squares, 840 path comparisons, global
three-chart conductor descent, the generic logarithmic Thom comparison, and
both mandatory forgetting ablations.

The resulting image has frozen signature
\[
\begin{array}{c|c}
\text{datum}&\Phi(\mathcal S_{\rm sh})\\ \hline
\text{generic }Q\text{ roof}&+1\\
\text{generic Rees factor}&x_D\\
\text{closed Cartier residue}&+1\\
\text{endpoint matrix}&\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\\
\text{Tor}_1\text{ orientation}&+1\\
\text{Čech residual}&0\\
\text{Cartier commutator}&0\\
\text{reflection defect}&0\\
\text{Jordan associator}&0.
\end{array}
\]
Both ordinary-forgetting images are zero.

Entry 421 proves that the admissible connector with this complete signature is
unique: its local relative deformation group vanishes, and the global
order-three lift torsor and automorphism group both vanish. Since the transform
constructed above supplies an object with that signature,
\[
\boxed{\Phi(\mathcal S_{\rm sh})
=\text{the unique global framed filtered connector}}
\]
up to the unique admissible homotopy.

This closes the normalization-sheet kernel that Entries 144 and 146 left open,
within the fs/Kato logarithmic category precisely delimited by Entries
425–429. It does not resurrect the impossible ordinary span to separated
sheets, nor claim a global raw-scheme correspondence outside the Kato sector.

The next research fork is now genuinely downstream: form the physical derived
pullback/butterfly using the fixed road inclusion and evaluate its primitive
class, or test the constructed transform under the first eight-point Cut
naturality square.

The executable audit is
`research/voevodsky/check_global_mixed_variance_transform.py`.
