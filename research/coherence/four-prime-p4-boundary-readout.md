# Audit of the proposed P4 complementary-face readout

## Correction

A subsequent null-space test refutes the interpretation of this compression as a complete six-channel intersection pairing. The computed operator is nonzero, but its face operators have exterior degree zero rather than two. The rank-five result must therefore be retained only as a finite compression diagnostic, not as a source-authorized P4 readout.

## Candidate restriction

The four-cell pairing \(\mathcal P_4\) was nonzero but had zero ordinary and super trace. Its source support identifies a more faithful readout.

Each curvature \(F_{pq}\) occupies a two-prime face, so \(\mathcal P_4\) preserves the grade-two exterior sector

\[
\Lambda^2\langle e_0,e_1,e_2,e_3\rangle.
\]

The half-line defects are supported near the seam. In the discrete exact model, let

\[
L=\max_i a_i=4
\]

and retain the left boundary sector

\[
\mathcal B_4
=
\Lambda^2\langle e_0,e_1,e_2,e_3\rangle
\otimes
\operatorname{span}\{\delta_x:0\le x<L\}.
\]

Define

\[
\rho_L(\mathcal P_4)
=
\Pi_{\mathcal B_4}\mathcal P_4\Pi_{\mathcal B_4}.
\]

This removes the artificial right endpoint introduced by finite seam truncation while retaining the actual half-line windows.

## Exact result

The retained space has dimension

\[
\binom42\cdot4=24.
\]

The readout has five nonzero matrix transitions and exact rank five:

\[
\operatorname{rank}\rho_L(\mathcal P_4)=5.
\]

Every transition pairs complementary two-faces:

\[
\{i,j\}
\longleftrightarrow
\{0,1,2,3\}\setminus\{i,j\}.
\]

Equivalently, the only admitted face pairings are

\[
01\leftrightarrow23,
\qquad
02\leftrightarrow13,
\qquad
03\leftrightarrow12.
\]

The scalar trace remains zero because no complementary two-face is itself. The information is entirely relational and off-diagonal.

## Interpretation

This initially suggested a concrete fourth-rank interpretation, but the null audit below rejects that conclusion for the present operator.

Four dimensions are distinguished because two observer faces can be complementary only through

\[
2+2=4.
\]

The three Pfaffian channels are precisely the three ways to partition four primitive axes into two observer pairs. Orientation assigns their signs.

This also explains why scalar trace was the wrong readout. A trace asks each face to return to itself. The four-cell instead relates each observer face to its complementary observer. Its natural shadow is therefore a six-channel incidence matrix, not a scalar diagonal sum.

## Remaining asymmetry

The missing sector is not one linear combination. Both full seam sectors associated with masks `0011` and `1100` are annihilated. This is structural: each \(F_{pq}\) is built from \(c_i i_j\), preserves exterior degree, and swaps occupancy inside a selected pair. It is not a two-form-valued curvature. Consequently the Pfaffian notation did not authorize a Hodge-style pairing of all six two-faces.

A genuine P4 constructor now requires a source-derived antisymmetric two-cochain

\[
\mathcal F\in C^2_{\rm cube}(\mathcal B),
\]

its typed cup product \(\mathcal F\smile\mathcal F\), and a relative boundary readout. These cannot be inferred from the nonzero degree-zero anticommutator alone.

## Verification

Run:

```text
python research/coherence/check_four_prime_p4_boundary_readout.py
```

Artifacts:

- `check_four_prime_p4_boundary_readout.py`
- `four-prime-p4-boundary-readout.v1.json`
