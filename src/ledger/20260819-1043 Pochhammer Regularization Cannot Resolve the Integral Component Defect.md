# 1043 — Pochhammer Regularization Cannot Resolve the Integral Component Defect

## Primary-source formula

Section 4.1 of Mizera, *Combinatorics and Topology of
Kawai–Lewellen–Tye Relations* (arXiv:1706.08527), defines the regularization
of the interval by equation (mathrm{reg	ext{-}0	ext{-}1}):

[
operatorname{reg}overrightarrow{(0,1)}
=
rac{S(arepsilon,0)}{e^{2pi i s}-1}
+overrightarrow{(arepsilon,1-arepsilon)}
-rac{S(1-arepsilon,1)}{e^{2pi i t}-1}.
]

Writing the facet monodromies as (M_0=e^{2pi i s}) and
(M_1=e^{2pi i t}), the boundary-circle coefficients are

[
rac1{M_0-1},
qquad
-rac1{M_1-1}.
]

The paper states that the higher-dimensional generalized Pochhammer contour
is obtained locally by the same product regularization near normal-crossing
faces.

## Integral type gate

Let

[
R_{mathbb Z}=mathbb Z[M_F^{pm1}]
]

be the integral Laurent group ring for a facet occurrence. The element
(M_F-1) is not a unit in (R_{mathbb Z}). Indeed, if

[
(M_F-1)f(M_F)=1
]

held for a Laurent polynomial (f), evaluation at (M_F=1) would give
(0=1).

Therefore the source regularization is defined over

[
R_{mathbb Z}ig[(M_F-1)^{-1}ig],
]

not over the unlocalized integral group ring. In several dimensions every
incident facet contributes its own required inverse.

## Consequence for Entry 1041

Entry 1041's quotient

[
mathbb Zlangle h_L,h_Rangle/
operatorname{im}(A_{H_0})
congmathbb Z/4
]

is an unlocalized constant-lattice comparison. The generalized Pochhammer
map does not provide integral columns in that lattice: its new boundary
pieces carry nonunit denominators (1/(M_F-1)).

Hence

[
oxed{
	ext{source Pochhammer regularization cannot canonically saturate the
Entry 1041 index-four quotient.}
}
]

This does not prove that the (mathbb Z/4) is physical torsion. It proves
that the proposed Pochhammer repair is mistyped. After localization the
finite quotient disappears, so localized twisted homology cannot decide
whether an integral form existed before localization.

## Narrow status

The string-sector packet now separates three layers:

[
egin{array}{c|c}
	ext{layer}&	ext{result}\ hline
	ext{rational occurrence Cousin complex}&H_1=H_2=0\
	ext{weighted character family}&	ext{strictly horizontal}\
	ext{unlocalized source orbit augmentation}&operatorname{coker}=mathbb Z/4
end{array}
]

The primary regularization lives only in the localized layer and cannot
identify the last row with an integral Betti invariant.

## Next falsifier

An integral conclusion now requires an independently declared integral form:
for example a relative chain lattice before monodromy localization, together
with a comparison to the six-word de Rham lattice. Absent that datum, retain
(mathbb Z/4) as a presentation-level two-primary defect—not as a physical
string class.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_pochhammer_integral_type_gate.rs`
- `research/benincasa/string-six-point-pochhammer-integral-type-gate.json`

Epistemic event: `ev-000000000661-0cbaf05e-6141-46be-a717-360acaf3b9e2`.
