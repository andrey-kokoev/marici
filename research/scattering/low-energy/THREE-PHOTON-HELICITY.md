# Three-photon helicity: the missing permutation phase and a rotation intertwiner

[Contract](contracts/three-photon-helicity.v1.json) · [checker](check_three_photon_helicity.py) · [receipt](results/three-photon-helicity.v1.json)

## Result

There is now an explicit **conditional isometric map from the encoded native pair into a relative three-photon helicity sector**, intertwining its diagonal native rotations. The target functions also have the documented continuous spatial rotation law. This narrows the previous scalar-coefficient construction: the polarization basis contributes a permutation sign, so the old scalar coefficients cannot simply be reused unchanged in a co-rotating helicity frame.

This imports the standard photon representation and relative massless phase space. It is not an emission interaction, an electron/positron preparation identification, a full Lorentz intertwiner or a normalizable total-momentum wavepacket. Nor does existence of this map select the actual outgoing amplitude.

## 1. One gauge for rotations and permutations

Work in the incoming CM frame with three positive-energy, noncollinear massless momenta summing to (M,0). Their spatial vectors lie in a plane. For the ordered tuple define

```
N=(p1_spatial cross p2_spatial)/|p1_spatial cross p2_spatial|,
n_i=p_i_spatial/E_i,
t_i=N cross n_i,
epsilon_h(p_i;N)=(t_i+i*h*N)/sqrt(2),  h=+1 or -1.
```

These are spatial Coulomb-gauge polarization vectors, with zero time component. The checker verifies exactly

```
n_i.epsilon_i=0,
epsilon_i.epsilon_i=0,
epsilon_i^*.epsilon_i=1,
n_i cross epsilon_i=-i*h*epsilon_i.
```

Define the unit-norm three-polarization section E_h(p)=epsilon_1 tensor epsilon_2 tensor epsilon_3, taking all three helicities equal. Proper spatial rotations send N to RN and each epsilon to R epsilon. Thus this **co-rotating** section has a simple rotation law, without deleting helicity phases by assumption.

### The exchange sign

Momentum conservation gives

```
p1 cross p2=p2 cross p3=p3 cross p1.
```

Consequently a permutation sigma changes the order-defined N by sign(sigma). Each t_i and epsilon_i changes by the same sign after relabelling. With three factors,

```
E_h(p_sigma)=sign(sigma)*P_sigma E_h(p).
```

Here P_sigma permutes polarization tensor slots. Therefore the scalar coefficient in **this gauge** must obey

```
phi(p_sigma)=sign(sigma)*phi(p)
```

to produce a Bose-symmetric full wavefunction phi(p) E_h(p). Constant coefficients or the previous even scalar code, interpreted unchanged in this frame, fail this requirement.

This does not refute the earlier Bose profiles in a fixed momentum-local laboratory helicity frame. Changing to this co-rotating section changes their coefficients too. The earlier scalar pullback representation was explicitly not identified with the physical photon action. This calculation supplies that missing distinction, not permission to discard previous records or reverse EF1-N.

## 2. A gauge-transition check

Under an arbitrary unit-modulus section change E'(p)=G(p)E(p), coefficients must change to phi'=phi/G. The permutation cocycle becomes

```
c_sigma'(p)=sign(sigma)*G(p_sigma)/G(p).
```

The checker uses the nonconstant ordered gauge

```
G(p)=(1+i*n_1x)/(1-i*n_1x),
```

verifies its unit modulus and the transformed cocycle, and checks that the complete singlet and triplet wavefunctions are unchanged. The coefficient alone is not a gauge-independent physical amplitude.

## 3. Corrected, normalized singlet and triplet

Use y_i=1-2E_i/M, the normalized relative measure dnu3=2 dy1 dy2 dR, and

```
A(y)=(y1-y2)*(y2-y3)*(y3-y1).
```

The following coefficient functions are odd under simultaneous photon relabelling:

```
phi_s=sqrt(840)*A(y),
phi_j=sqrt(3)*N_j,  j=x,y,z.
```

Multiplying each by E_h(p) gives Bose-symmetric helicity-sector wavefunctions Phi_s,Phi_x,Phi_y,Phi_z. Their Gram matrix is I4 because

```
integral A^2 dnu_shape=1/840,
<N_j>_Haar=0,
<N_i*N_j>_Haar=delta_ij/3,
||E_h(p)||=1.
```

These are normalizable **relative** states, conditional on a fixed total four-momentum. The fixed-M sharp total is still not a full Fock-space wavepacket.

Under the physical rotation action on polarization-valued wavefunctions,

```
(T_R Phi)(p)=R^(tensor 3) Phi(R^-1 p),
T_R Phi_s=Phi_s,
T_R Phi_j=sum_k R_kj Phi_k.
```

The polarization factors are essential to this statement. Thus the target representation is 1 direct-sum 3. Composing with the [exact source-pair Clebsch–Gordan matrices](NATIVE-PAIR-INTERTWINER.md) defines the map explicitly:

```
z in the four-dimensional encoded logical pair,
c=C† z  (or Csame† z for the same-spinor pairing),
W_h z=c_s*Phi_s+sum_j c_j*Phi_j.
```

It preserves every complex input amplitude and inner product and intertwines all 24 diagonal native source actions. A gauge-independent phase witness is explicit: the states (Phi_x +/- Phi_y)/sqrt(2) have expectations of the Bose-even observable N_x*N_y differing by 2/5, verified by the exact sphere fourth moment. An incoherent mixture would miss this difference. Both h choices give separate such maps; their physical relative amplitude is not selected. The continuous target rotation law does not license new continuous native operations. The encoded domain excludes the raw-pair orthogonal complement, which a full implementation must retain separately.

Unlike the earlier abstract scalar triplet, the corrected helicity triplet has no Vandermonde factor and need not vanish at equal energies. That change is demanded by the jointly specified polarization and permutation action, not fitted to a desired spectrum. These constructed profiles still do not predict the physical spectrum: rotationally invariant, Bose-compatible shape factors could change them while preserving the symmetry requirements.

## 4. Exact checks and limits

Two source-derived CM configurations are checked: equal-area three-output geometry and the preceding unequal-weight sensitivity case. For each helicity the checker verifies all six permutations, the gauge transition, all 24 native rotations and an additional nonnative 45-degree rotation. Counts are 24 permutation cases, 24 gauge-transition cases and 100 rotation cases. All arithmetic is exact in the existing radical field for these vector tests. General normalization uses the preceding exact simplex integral and the documented Haar moments; general covariance follows from the displayed vector identities. This is not a machine-formalized theorem.

The equal-area geometry itself supplies only a sharp energy shape, not these finite-width amplitude functions. Choosing W_h as a physical law remains an additional hypothesis. Standard imported kinematics, a mathematical embedding and symmetry are not a contact amplitude derivation.

## 5. Next gates

1. The [two-photon audit](TWO-PHOTON-HELICITY.md) now completes all four helicity pairs. It excludes a continuously identified total-J=1 input from exclusive two-real-photon outputs, but also completes the native finite-group quadrupole code to photon states. These are compatible: the native triplet has not been identified with physical total spin one. Continuous spin selection leaves singlet two-/three-sector weights unfixed.
2. The [native charge/preparation audit](NATIVE-CHARGE-PREPARATION.md) now confirms that the inspected sources select neither pair C sign nor singlet fraction. A raw opposite-Pauli-code flip exists but is excluded from the stored protocol. A typed statistics/charge extension is required before using a multiplicity selector; no electron/positron species or charge parity follows merely from U tensor conjugate(U).
3. The [graded contact vertex](GRADED-CONTACT-VERTEX.md) now constructs a conditional Hermitian operator with CAR, a vacuum-fixed species flip and retained spectators. It still recurs and leaves two coefficients free. The [Jacobi completion](CONTACT-ESCAPE-CONTINUUM.md) now tests local escape and bound clouds under additional lattice assumptions; the [total-momentum successor](TOTAL-MOMENTUM-PACKET.md) now supplies a full imported Fock packet and Lorentz coefficient carrier. The [covariant lift](COVARIANT-ESCAPE-LIFT.md) now supplies active lab translations under added velocity/mass postulates. Next audit local source/cluster assumptions and bind amplitudes, preparation and native licensing.

No branching ratio or source-selected energy distribution follows. C1–C12, exhausted C12 effort and paused high-energy execution are preserved. Owner files and historical source warnings are unchanged.

```sh
python -S research/scattering/low-energy/check_three_photon_helicity.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_three_photon_helicity.py
```
