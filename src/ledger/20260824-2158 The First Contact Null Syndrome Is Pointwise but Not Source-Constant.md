---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2158 — The First Contact Null Syndrome Is Pointwise but Not Source-Constant

## Candidate parity-check matrix

At the isolated-contact normals \(\nu_i=0\), retain the three grade-two
sectors \(S_i\) isolating vertex \(i\), together with the fully deleted
sector \(S_{123}\). The labelled normal readout matrix is

\[
M=
\begin{pmatrix}
4P_{23}&0&0&-8C_2C_3\\
0&4P_{31}&0&-8C_1C_3\\
0&0&4P_{12}&-8C_1C_2
\end{pmatrix}.
\]

The \(P_{jk}\) are connected two-site spectator periods and the \(C_i\) are
isolated-contact coefficients. Their retention is forced by the component
product.

## Pointwise kernel

Over the generic function field, \(M\) has rank three and kernel generator

\[
v_{\rm pt}
=
\left(
\frac{2C_2C_3}{P_{23}},
\frac{2C_1C_3}{P_{31}},
\frac{2C_1C_2}{P_{12}},
1
\right).
\]

Thus each generic fiber has an invisible combination, but its line varies
with kinematics and with the source-normalized spectator periods.

## Hostile constant-circuit test

Forgetting the spectator factors suggests the constant circuit
\((2,2,2,1)\). Exact evaluation at two independent generic packets gives
nonproportional pointwise kernel generators, and the constant vector lies in
neither kernel. Hence

\[
\boxed{
\text{the apparent constant contact circuit is a spectator-forgetting
artifact.}
}
\]

Strominger's exceptional vector is a primitive source-constant kernel of a
fixed finite readout matrix. The cosmological packet currently supplies only
a moving function-field kernel. It becomes analogous only if the line is
horizontal and source-normalized.

The next test is

\[
\nabla v_{\rm pt}\stackrel?{\in}\langle v_{\rm pt}\rangle,
\]

using the actual Gauss--Manin connections of \(P_{jk}\) and \(C_i\). Ratios
must not be treated as horizontal merely because they exist.

## Classification

- existing Carrier support: labelled contact normals;
- generic pointwise kernel: rank one;
- source-constant circuit: absent;
- horizontal kernel line: untested;
- new Carrier datum: none.

## Evidence

- research/benincasa/isolated-contact-null-syndrome-audit.md
- research/benincasa/checkers/isolated_contact_null_syndrome.rs
- allocator claim seqclaim-915254f11223328681d06616
