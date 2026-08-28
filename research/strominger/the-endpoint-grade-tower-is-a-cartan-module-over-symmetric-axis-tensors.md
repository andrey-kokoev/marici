# The Endpoint Grade Tower Is a Cartan Module over Symmetric Axis Tensors

## Coherence question

The axis-marked maps construct adjacent endpoint inclusions. A further question is whether repeated grade changes depend on their order or parenthesization when different axes are used.

They do not. The endpoint maps are the spin-weighted realization of the Cartan product: multiply an irreducible harmonic by a degree-one axis harmonic and retain the highest-degree irreducible component.

## Cartan product

Let (H_l) be the degree-(l) harmonic representation and let (a\in H_1) encode an axis vector. Define

\[
C_a(P)=\operatorname{Harm}_{l+1}((a\cdot x)P),
\qquad P\in H_l.
\]

The spin-weighted endpoint map (J_a) is this operator transferred through the extremal spin-raising identifications, multiplied by a nonzero scalar depending only on (l).

This transfer is exact. Define the normalized extremal spin identification

\[
R_l=\frac{\eth^l}{\sqrt{(2l)!}}:H_l^{(0)}\longrightarrow H_l^{(l)}.
\]

The scalar Cartan coefficient and the spin-weighted (J_l) coefficient have squared ratio

\[
\frac{\lvert J_l(l,m)\rvert^2}
{\lvert C_l(l,m)\rvert^2}
=\frac{2(2l+1)}{l+1},
\]

independent of (m). Therefore

\[
J_l=c_lR_{l+1}C_lR_l^{-1},
\qquad
c_l^2=\frac{2(2l+1)}{l+1}.
\]

All normalization factors depend only on the sequence of grades, never on the axes or weights. They cannot generate a swap or associator anomaly.

If (a,b\in H_1), then

\[
C_bC_a(P)
=\operatorname{Harm}_{l+2}((b\cdot x)(a\cdot x)P).
\]

Intermediate lower-degree and trace terms cannot contribute to the final highest-degree harmonic projection. Since scalar multiplication is commutative,

\[
C_bC_a=C_aC_b.
\]

For three or more axes, the same argument gives

\[
C_{a_k}\cdots C_{a_1}(P)
=\operatorname{Harm}_{l+k}
\left(\prod_{j=1}^k(a_j\cdot x)P\right).
\]

The result depends only on the symmetric tensor

\[
a_1\odot\cdots\odot a_k.
\]

Composition is therefore associative and permutation-invariant.

## Categorical structure

The endpoint tower is a graded module over the symmetric algebra of the vector representation:

\[
\operatorname{Sym}(H_1)\curvearrowright\bigoplus_{l\geq s}H_l,
\]

where multiplication means Cartan projection onto the highest representation.

This supplies the coherence cells constructively:

- every adjacent swap has identity residual;
- every braid has identity residual;
- every associator has identity residual;
- higher permutation coherence follows from ordinary commutative multiplication.

No additional anomaly tower is needed for this endpoint subsystem once the Cartan realization is retained. If only individual fixed-axis matrices were stored, these coherence laws would be invisible and would have to be reintroduced as external cells.

## Relation to the two-extremal filtration

Choosing one axis diagonalizes the Cartan action into axial weights. Each application enlarges the supported interval by the two new endpoints. Thus the two descriptions are equivalent:

- invariant description: Cartan multiplication by symmetric axis tensors;
- axis chart: retain all existing weights and add one extremal pair per grade.

The (5+2+2=9) spin-two grade-three chart is the axial-coordinate expression of the invariant Cartan module through two grade extensions.

## Scope

This coherence is mathematical and exact for the derived endpoint readout. It does not authorize physical higher-spin dynamics. It also does not identify affine torsion classes with harmonic vectors.

## Evidence replay

The dependency-free checker implements exact rational harmonic projection in three variables. It verifies commutation, association, and equality with direct highest-degree projection for degrees one through six, four independent rational axes, and two harmonic seeds per degree.

The companion checker `spin_weighted_cartan_transfer_normalization_checks.py` verifies the scalar-to-spin normalization and weight-independent transfer factor through degree fifty.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/cartan_endpoint_grade_change_coherence_checks.py
```

Machine-readable results are written to `research/strominger/results/cartan_endpoint_grade_change_coherence_checks.json`.
