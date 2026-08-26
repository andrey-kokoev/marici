# DPC multiplicity attack (WP392)

## Target

Attack the claim that a multiplicity-one, anomaly-free source line $L$ forces
one protected response direction and fixes the flavor coupling ratio.

## Exact countermodel

Use the CP group $Z_2$. Let the source contain one copy of the odd line,

\[
\rho_L=-1,
\]

while the two physical response coordinates form two copies of the same odd
representation,

\[
\rho_R=-I_2,
\qquad R=L\oplus L.
\]

A coupling vector $v:L\to R$ is equivariant when

\[
\rho_Rv=v\rho_L.
\]

This equation holds for every $v=(g_1,g_2)^T$. Therefore

\[
\dim\operatorname{Hom}_{Z_2}(L,R)=2,
\]

even though the source line itself is one-dimensional and present once. The
ratio $g_2/g_1$ is completely unrestricted.

This finite-dimensional CP representation is internally consistent and needs
no anomalous symmetry action. Adding anomaly freedom cannot reduce the
two-dimensional intertwiner multiplicity by itself.

## RG attack

Every real two-by-two mixing matrix commutes with $\rho_R=-I_2$. Hence CP
allows arbitrary RG rotation inside the multiplicity space. For

\[
A=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad v=(0,1)^T,
\]

one obtains $Av=(1,0)^T$, which is noncollinear with $v$. CP remains exact
while WP391 cross-scale coherence fails.

Likewise, the two allowed intertwiners $(1,1)^T$ and $(1,2)^T$ give a combined
Gram response of full rank. Per-context factorization through the same
abstract line does not force the same embedding of that line.

## Diagnosis

The DPC conflated three different multiplicities:

- multiplicity of $L$ in the source sector;
- dimension of the allowed intertwiner space from $L$ to the response;
- multiplicity of the protected line inside the response representation.

Only the second directly controls uniqueness of the coupling direction. Even
then, a physical normalization and source/readout parallelization are needed
to turn the unique abstract line into a calibrated numerical ratio.

## Required repair

A viable successor must require

\[
\dim\operatorname{Hom}_G(L,R)=1,
\]

and prove that the complete RG and threshold commutant preserves the image of
that unique intertwiner. It must also derive the embedding in physical16,
rather than choosing it after observing the flavor ratio.

The smallest exact falsifier is the present $Z_2$ model: one source line, two
response copies, arbitrary coupling ratio, and symmetry-allowed rotation.
The original DPC is therefore false as stated.

Run `uv run --with sympy python
research/flavor/checkers/wp392_dpc_multiplicity_attack.py` to regenerate the
result.
