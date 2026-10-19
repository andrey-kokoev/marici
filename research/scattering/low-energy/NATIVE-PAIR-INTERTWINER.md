# Native pair intertwiners: a construction and a multiplicity counterexample

[Contract](contracts/native-pair-intertwiner.v1.json) · [checker](check_native_pair_intertwiner.py) · [receipt](results/native-pair-intertwiner.v1.json)

## Result, precisely scoped

Two native spinor carriers admit explicit isometric, diagonal-binary-tetrahedral intertwiners into **both** two-output and three-output Bose-symmetric **scalar coefficient** spaces. The construction retains all four complex input amplitudes, not just a singlet probability. Therefore the finite symmetry, conservation, Bose coefficient symmetry and isometry conditions do not choose between these multiplicities.

This is not yet a physical photon intertwiner. The target action here is scalar pullback of direction/orientation coordinates; a measurable helicity frame carries additional rotation phases. No identification of that scalar action with physical photon rotations is made. Source electron/positron preparation, charge conjugation, total-momentum wavepackets, native joint-operation licensing and contact dynamics remain missing.

## 1. Fresh native source and the pair decomposition

Use the same current 24 quaternion actions and stored eight-dimensional raw spinor encoding as the [phase audit](HINGE-PHASE-CONTINUATION.md). If J=K/sqrt(2), then J†J=I2 and T(q)J=JU(q). Tensorization gives an isometric four-dimensional code in a 64-dimensional raw-pair space. The checker verifies these identities in factored form. The constructed output maps have that encoded four-dimensional domain, not the entire raw space: they do not license projecting away its 60-dimensional complement. A full raw implementation must preserve that complement in an explicit additional output/record; none is claimed here.

Both pairing conventions are tested, because physical charge/preparation binding has not selected one:

```
Vsame(q)=U(q) tensor U(q),
Vconjugate(q)=U(q) tensor conjugate(U(q)).
```

Let C have the row-major vectorizations of I, sigma_x, sigma_y, sigma_z, divided by sqrt(2), as columns. Then

```
C† Vconjugate(q) C = diag(1,R(q)).
```

For epsilon=[[0,1],[-1,0]], Csame=(I tensor epsilon) C similarly gives

```
Csame† Vsame(q) Csame = diag(1,R(q)).
```

All 24 identities and both raw-pair embeddings are checked exactly. The vector character has squared group norm one, so this is one singlet plus one irreducible triplet. Group averaging gives a rank-one invariant projector.

A target code consisting only of the preceding orientation-independent shape profiles is trivial under scalar pullback. Any equivariant map from the pair into that code therefore has rank at most one: it kills the triplet. It cannot be a four-dimensional input isometry.

For a lone source spinor the center acts as -I, whereas scalar orientation pullback has center +I. A strict linear intertwiner with no additional center-odd record must be zero. This is not a universal conversion no-go: a suitable transforming residual record changes the target representation. Tensoring two native carriers removes the center mismatch, as checked explicitly.

## 2. Two-output Bose coefficient code

For a unit ray n on S2, use normalized solid angle. Define

```
chi_s(n)=1,
(chi_x,chi_y,chi_z)=sqrt(15)*(n_y*n_z,n_z*n_x,n_x*n_y).
```

They are even under n -> -n, hence symmetric under exchange of the two equal-helicity photon labels in the assumed coefficient convention. Their Gram matrix is I4, using the exact normalized sphere monomial integrals.

For every native projected tetrahedral rotation, scalar pullback transforms the three quadrupoles by exactly R(q). Thus, after the above Clebsch–Gordan change of basis, mapping the four pair coefficients to chi_s,chi_x,chi_y,chi_z is an isometric native-group intertwiner. Complex superpositions remain coherent. For example the states (chi_s +/- chi_x)/sqrt(2) have expectations of the bounded observable chi_x differing by 2, not the zero difference of the corresponding incoherent mixtures.

**Important limitation:** these functions are quadrupoles, not a full SO(3) vector representation. A 45-degree z rotation takes chi_z to

```
sqrt(15)*(n_y^2-n_x^2)/2,
```

which is orthogonal to the entire four-function code and has squared norm one. This exact leakage witness excludes extending this particular native-group code to an SO(3) vector intertwiner. It is not a physical Landau–Yang proof. The finite tetrahedral group cannot distinguish all continuous angular-momentum representations: here its vector irrep also occurs inside the quadrupoles.

## 3. Three-output Bose coefficient code

Use the preceding [relative phase-space measure](RELATIVE-PHOTON-MEASURE.md), dnu3=2 dy1 dy2 dR. Let the reference triangle lie in the xy plane, and define

```
A(y)=(y1-y2)*(y2-y3)*(y3-y1),
eta_s=1,
eta_j(y,R)=sqrt(2520)*A(y)*(R e_z)_j,  j=x,y,z.
```

The exact simplex integral is

```
integral A(y)^2 dnu_shape = 1/840.
```

Normalized Haar moments give <(R e_z)_i>=0 and <(R e_z)_i*(R e_z)_j>=delta_ij/3. Therefore the four eta functions have Gram matrix I4. The checker evaluates the simplex polynomial exactly and checks an exact degree-two sphere cubature witness for the stated Haar moment inputs; it does not equate that finite cubature with Haar measure at higher degrees.

A photon permutation changes A by its sign. The corresponding proper reference-triangle permutation changes the plane normal by the same sign. Their product is invariant: eta_j is Bose-symmetric, unlike the uncorrected orientation vector alone. Both polynomial permutation signs and all six proper reference-triangle rotations are checked.

Scalar left rotation acts on eta_j as a vector for all SO(3), hence for the native group. This supplies another isometric pair-coefficient intertwiner. It still does not include physical photon-helicity phases. No source spin-to-photon angular-momentum dictionary is inferred.

The triplet profile vanishes at equal y_i. This is not a prediction that a physical triplet annihilation spectrum vanishes there; it is a property of this constructed scalar code. In particular importing it as a photon amplitude requires the missing helicity and preparation checks.

## 4. Explicit remaining multiplicity freedom

Call the two isometries W2 and W3. Their target sectors are orthogonal. For any complex a,b satisfying |a|^2+|b|^2=1,

```
W(a,b)=a*W2 direct-sum b*W3
```

is another diagonal-native-group intertwining isometry. Its conditional sector weights are |a|^2 and |b|^2 for every normalized input. The checker verifies examples

```
(1,0), (9/25,16/25), (16/25,9/25), (0,1).
```

These are counterexamples to selection by the stated conditions, not proposed fitted physical branching laws. No free choice in this family is promoted to a prediction. A contact generator, extra physical symmetry, or independently bound preparation/helicity rule must do additional work.

## 5. Three-photon helicity continuation and next gate

The [three-photon helicity audit](THREE-PHOTON-HELICITY.md) now supplies an explicit co-rotating polarization section and its odd-permutation cocycle. In that gauge, unchanged even scalar coefficients fail full Bose symmetry. Corrected odd coefficients sqrt(840)*A and sqrt(3)*N_j yield a conditional relative three-photon rotation intertwiner for the encoded native pair. This is not a physical preparation binding or emission operation; the original scalar results above remain scoped to their declared action.

The [two-photon continuation](TWO-PHOTON-HELICITY.md) now completes all helicity pairs and the finite quadrupole code's photon interpretation. Its continuous total-J=1 exclusion must not be applied without binding the native source's total spin and orbital content. The [native charge/preparation audit](NATIVE-CHARGE-PREPARATION.md) now inspects those actual source operators: it constructs a raw Pauli-code flip but excludes it from the fixed protocol, and leaves both pair C sign and singlet fraction unselected. The [graded contact extension](GRADED-CONTACT-VERTEX.md) now postulates CAR and a species flip and constructs a retained self-adjoint vertex; this is not a promotion of the source antiunitary to charge conjugation. Its finite code recurs; the [Jacobi completion](CONTACT-ESCAPE-CONTINUUM.md) now supplies conditional escape and retained-cloud tests, with physical continuum/source binding still open. Compute both actions in one specified polarization gauge: a co-rotating frame may simplify rotation phases while introducing permutation phases, which must not be silently deleted. Keep the diagonal native-group result separate from a continuous spin claim. Independently identify any charge-conjugation/inversion operation from the native source before using it as a multiplicity selector; it must not be imported from the desired annihilation outcome.

C1–C12 are unchanged, C12 has no renewed effort, and high-energy execution stays paused. Owner files are read-only; the historical producer-hash mismatch remains reported rather than repaired. No physical output or branching outcome is admitted.

```sh
python -S research/scattering/low-energy/check_native_pair_intertwiner.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_native_pair_intertwiner.py
```
