# Amplituhedron residue square and cross-family cube boundary

## Four explicit squares

At the shared positive facet control e=44/445, take each cell i in {zero2_EB,zero2_FB,zero3_EB,zero3_FB}. Its local inverse branch gives the following comparison:

source eight-form -- pushforward along Phi_i --> target eight-form
       |                                             |
 source residue                                 target residue
       |                                             |
       v                                             v
source face seven-form -- boundary pushforward --> target face seven-form

All vertices are form data in their declared charts, not points of the amplituhedron. The source cells and target geometry have dimension eight; the square is an indexing diagram of operations.

## Independent route calculation

Use actual target chart coordinates y=vec(B), B=(C Z_first2)^(-1) C Z_last4. The earlier raw derivatives C*z are converted using the common face frame H^(-1). Write J_i=[c_i | T], where c_i is the w2 derivative and T the common seven-dimensional face tangent.

Choose a coordinate m with nonzero conormal component and normalize n_m=1. Let z be the remaining seven coordinates. The boundary determinant D=det(T with row m omitted) is nonzero. Locally the face is y_m=f(z); set x=y_m-f(z). At the control dx=n and the normal derivative is a_i=n*c_i.

For source residue scalar rho_i, the two independently evaluated coefficients in the ordered dz chart are

push then residue: (-1)^m rho_i a_i / det(J_i),
residue then push: rho_i / D.

They agree because det(J_i)=(-1)^m a_i D. This is also the general local regular-chart identity; the checker independently computes the interior and face determinants for the four actual maps.

The face source matrix is symbolically identical for all four cells. Hence their complete fermionic numerator restricts to the same polynomial. Equality of the scalar residue factors therefore extends to every component; 36 physical-pair fourth-power minors per cell provide 144 explicit coefficient checks. The common source denominator is the product of w4,w5,w6,w7,w8,u,(t-u). EB and FB have opposite source orientations within each family.

## Cube boundary assembled so far

For either role EB or FB, stack the zero2 and zero3 squares. Their lower source-face vertices identify via the same restricted 2x9 matrix, and their lower target-face vertices identify via the same restricted target map. The boundary pushforwards agree. Thus the lower connecting face is realized, with the full intermediate route records retained.

The upper source forms and target forms remain different off the facet. To complete this into a homotopy-coherent cube, one must define the upper cross-family comparison maps and the side-face comparisons, then specify a bulk filler with those exact boundaries. Source-chart parameter equality alone does not supply equality of pushed forms; earlier component checks demonstrate different off-face contributions.

The useful next task is to define the comparison category: for example, germs modulo regular forms retain residues but forget off-face regular differences; a category retaining full forms must record those differences explicitly. The choice changes which observer is being constructed. Both retainable quantities should be explicit before assigning a cube filler.

## Evidence

Fresh exact checker: `research/nima/checkers/check_nine_point_residue_pushforward_coherence_square.py`.
Result: `research/nima/results/nine-point-residue-pushforward-coherence-square.json`.

Four regular local residue squares pass; the cross-family boundary identification passes. Full cube comparison and physical contour selection remain open. No generic target coverage claim is inferred from this control.
