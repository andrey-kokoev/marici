# Correction: the `2L` pure Hardy strip is an exact mismatch sector, not the first prolate defect

## Claim being corrected

The localized Hardy identity

\[
\|(I-\Pi)
M_{e^{2iLs}}
\Pi M_m\|_{HS}^2
=2L\|g\|_{Pl}^2
\]

was identified with the first dyadic prolate defect

\[
\|[B(I-B)]^{1/2}A_g\|_{HS}^2.
\]

That identification is false for the pure exponential reference pair.

## Nested Hardy projections

Let

\[
Q_L
=M_{e^{2iLs}}
P
M_{e^{2iLs}}^*.
\]

In the Fourier-dual variable, multiplication by `e^(2iLs)` translates the Hardy half-line. Hence either

\[
Q_L\le P
\]

or

\[
P\le Q_L,
\]

depending on orientation.

Thus the pure pair is nested.

## Compression of a nested pair

If

\[
Q_L\le P,
\]

then

\[
B_L
=P Q_L P
=Q_L
\]

on `ran P`. Therefore

\[
\boxed{
B_L^2=B_L
}
\]

and

\[
\boxed{
B_L(I-B_L)=0.
}
\]

If `P<=Q_L`, then `P Q_L P=P`, and the same conclusion holds.

Consequently every generic dyadic defect vanishes for the pure translated Hardy projection pair:

\[
\boxed{
B_L^{2^j}
(I-B_L^{2^j})
=0.
}
\]

## Where the strip lives

For nested projections, the finite interval between the two Hardy boundaries is an exact Halmos mismatch sector:

- `H_10=ran P intersect ker Q` in one orientation;
- `H_01=ker P intersect ran Q` in the other.

It is not part of the generic angle block.

The projection difference is exactly

\[
P-Q_L
=P_{H_{10}}
\]

when `Q_L<=P`, or the negative of `P_(H_01)` in the opposite orientation.

Its observer-localized trace is

\[
\boxed{
2LG_{Pl}.
}
\]

Thus the `2L` coefficient measures exact mismatch-strip mass.

## Unitary commutator versus projection-pair sewing

The operator

\[
H_L
=(I-P)
M_{e^{2iLs}}
P
\]

measures how the translating unitary crosses the fixed Hardy boundary.

The projection-pair off-diagonal block is instead

\[
S_L
=(I-P)
Q_LP.
\]

For nested projections,

\[
\boxed{
S_L=0.
}
\]

These operators are not interchangeable:

\[
\boxed{
(I-P)UP
\ne
(I-P)(UPU^*)P.
}
\]

The former can have `2L` Hilbert--Schmidt mass after observer localization while the latter vanishes identically.

## Halmos decomposition of the pure pair

The generic Halmos carrier `K \oplus K` is absent for a strictly nested pair. The full pair consists only of exact intersections:

\[
H
=
H_{11}
\oplus
H_{10}
\oplus
H_{01}
\oplus
H_{00}.
\]

In the orientation `Q_L<=P`:

- `H_11=ran Q_L`;
- `H_10=ran P minus ran Q_L`, the finite-width Hardy strip;
- `H_01=0`;
- `H_00=ker P`.

All eigenvalues of `P Q_L P` are exactly zero or one.

## Role of Tate scattering

For

\[
\sigma_{L,\chi}
=e^{2iLs}
\gamma_\chi(s),
\]

the nontrivial Tate phase generally destroys exact nesting. Then a generic angle block can appear, with nonzero

\[
B_{L,\chi}(I-B_{L,\chi}).
\]

Accordingly:

- pure translation supplies exact spectral-flow mismatch mass;
- Tate scattering converts part of the boundary geometry into generic angle/prolate defects;
- the finite arithmetic term is relative to the exact pure mismatch reference.

This is the correct positive sewing picture.

## Consequence for the reference Widom proposal

A pure translated Hardy pair does not have the ordinary smooth prolate plunge spectrum. Its compression is a projection, so applying a defect test function `f` with

\[
f(0)=f(1)=0
\]

gives

\[
\boxed{
f(B_L^0)=0.
}
\]

Therefore the classical Widom coefficient for compact time--band concentration cannot be assigned directly to this nested one-sided reference pair.

The `2L` mismatch strip and the compact-prolate `log c` plunge are different mechanisms.

## Revised positive reference feature

The reference positive feature must include exact Halmos mismatch slots

\[
\boxed{
P_{H_{10,L}^0}A_g,

\qquad
P_{H_{01,L}^0}A_g
}
\]

rather than a nonexistent generic defect slot.

The Tate pair contains:

1. exact intersections/mismatches;
2. a generic angle tower produced by the gamma perturbation.

Positive relative sewing must compare the full Tate Halmos feature against the full pure-reference exact-intersection feature.

## Revised common-edge removal

The common leading `2L` Gram, when present, belongs to the mismatch reference sector. A positive decomposition of Tate and reference Grams can still use

\[
D_L
=G_L^T-G_L^0
\]

and the common-Gram Jordan construction. But `G_L^0` must be the mismatch-strip Gram, not the first dyadic defect Gram.

Therefore the algebraic common-edge theorem survives, while its physical slot assignment changes.

## Revised analytic target

The exact finite-cutoff alignment must prove that

\[
\boxed{
\begin{aligned}
&	ext{Tate exact-intersection slots}
+
	ext{Tate generic defect tower}\\
&
-
	ext{pure-reference mismatch strip}
\end{aligned}
}
\]

has centered signed Gram converging to the Tate logarithmic-derivative form.

At the positive level, one must identify a common subfeature between the extensive Tate boundary mass and the pure exact mismatch strip.

## Effect on extremal/plunge analysis

The ordinary Landau--Widom asymptotic remains relevant for compact auxiliary prolate regulators and potentially for the nonnested Tate generic block. It is not the spectral law of the pure one-sided exponential reference pair.

Thus one must distinguish:

- compact-window prolate plunge;
- one-sided pure Hardy mismatch strip;
- gamma-induced generic-angle spectrum.

No single `c` or `L` scaling law should be transferred among them without an explicit regulator comparison.

## Status table

| Statement | Status |
|---|---|
| localized unitary Hardy transition has Gram `2L G_Pl` | correct |
| pure projection pair is nested | correct |
| pure `PQP` has only eigenvalues zero and one | correct |
| pure first dyadic defect equals the unitary transition | false |
| pure dyadic defect has Gram `2L G_Pl` | false |
| `2L` mass lies in `H_10/H_01` mismatch strip | correct |
| gamma-scattered pair may have generic defects | open/expected |

## Corrections to prior workload

The leading reference calculation is already exact, but it concerns the mismatch projection. Higher pure-reference dyadic power asymptotics are unnecessary because all such defects vanish.

The remaining work is instead:

1. materialize the full Tate Halmos decomposition relative to the pure nested pair;
2. compare its exact mismatch and generic-angle masses with the pure strip;
3. prove the relative signed difference equals the localized Hardy/Tate trace;
4. construct positive common-strip removal.

## Disposition

The exact identity is

\[
\boxed{
\|(I-P)
M_{e^{2iLs}}P M_m\|_{HS}^2
=2L\|g\|_{Pl}^2,
}
\]

but its geometric meaning is

\[
\boxed{
\text{unitary boundary crossing}
=
\text{exact Hardy mismatch strip},
}
\]

not

\[
\text{first generic prolate defect}.
\]

The `2L` reference feature belongs to `H_10` or `H_01`; the dyadic generic tower begins only after nontrivial Tate scattering destroys nesting.
