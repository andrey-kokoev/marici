# All two-photon helicities: continuous spin selection versus native finite symmetry

[Contract](contracts/two-photon-helicity.v1.json) · [checker](check_two_photon_helicity.py) · [receipt](results/two-photon-helicity.v1.json)

## Result and boundary

The two-photon rotation/exchange audit now covers **all four helicity pairs**. It constructs a global equal-helicity polarization product and completes the earlier native finite-group code to actual relative photon wavefunctions. It also gives an exact reference-direction constraint proof of the familiar conditional **total J=1 exclusion** for isolated two-real-photon outputs.

These results are compatible: a tetrahedral triplet is not automatically continuous physical total spin one. The stored finite-group representation also occurs inside a quadrupole, and no source binding has selected its continuous interpretation. The native source triplet is therefore **not** declared forbidden from producing two photons. Physical incoming species, orbital/preparation content, continuous rotation licensing and charge conjugation remain open.

## 1. A matched pair of helicity frames

In the CM frame the momenta are (M/2)*(1,n) and (M/2)*(1,-n). Choose any real unit t perpendicular to n and s=n cross t. For h1,h2 in {+1,-1}, define

```
e1=(t+i*h1*s)/sqrt(2),
e2=(t-i*h2*s)/sqrt(2),
B_h1h2(n,t)=e1 tensor e2.
```

Each factor is normalized, transverse and has its stated helicity relative to its own momentum. Every B has unit tensor norm. A transverse-frame rotation by alpha changes the product by

```
B -> exp[-i*(h1-h2)*alpha] B.
```

This is also its physical stabilizer character under a rotation about n, which leaves both momenta fixed. The checker verifies the character at 45 and 90 degrees for every helicity pair, rather than deleting it as a phase convention.

Exchange acts as

```
B_h2h1(-n,t)=transpose(B_h1h2(n,t)).
```

For equal helicities the product is independent of t and has the global expression

```
B_h(n)=[I-n*n^T+i*h*[n]_cross]/2,
[n]_cross v=n cross v.
```

It obeys

```
B_h(-n)=B_h(n)^T,
B_h(Rn)=R B_h(n) R^T,
||B_h(n)||^2=1.
```

Thus a Bose-symmetric equal-helicity full wavefunction is simply an **even** scalar coefficient f(n) times B_h(n), with physical rotations acting by scalar pullback on f. This completes the two-photon frame issue left open by the earlier scalar audit. Opposite helicities retain their nontrivial frame character; they are not assigned this scalar formula.

## 2. Conditional continuous total-J=1 exclusion

Suppose the incoming representation really is total J=1 under continuous SO(3), and the only outputs are two real photons with no additional angular-momentum-carrying system. At reference n=e_z, let L be the row functional giving a particular helicity-channel coefficient from the three input amplitudes.

This is a finite-spin induced-representation argument: a bounded equivariant map from a finite-dimensional SO(3) irrep has smooth finite-spin representatives. Equivalently use Frobenius reciprocity. No point evaluation of an arbitrary L2 equivalence class is assumed.

Let

```
R90=rotation about z by pi/2,
Y=rotation about y by pi.
```

### Opposite helicities (+,-) and (-,+)

Their stabilizer character at R90 is -1. Equivariance requires

```
L*(R90+I)=0.
```

The matrix is invertible: its constraint Gram determinant is 16. Therefore L=0 in each opposite-helicity channel. Rotation transitivity makes the entire intertwiner zero.

### Equal helicities (+,+) and (-,-)

Their stabilizer character is +1. The first constraint is

```
L*(R90-I)=0,
```

which leaves only the z component. Bose exchange and the frame-independent tensor imply additionally

```
L*(Y-I)=0.
```

Since Y reverses z, this kills the remaining component. The combined constraint Gram is

```
(R90-I)*(R90-I)^T+(Y-I)*(Y-I)^T=diag(6,2,4),
determinant=48.
```

Hence the continuous total-J=1 to exclusive two-photon intertwiner has rank zero for **all helicities**, including arbitrary superpositions. This is a conditional Landau–Yang-type selection result in the imported photon framework, not a derivation of the native source's physical total angular momentum. It does not apply to off-shell photons, recoil/residual systems or an input with additional orbital content changing total J.

A spin-zero source, by contrast, has normalized equal-helicity states B_+(n) and B_-(n). Opposite helicities have a nontrivial stabilizer character and do not support spin zero. No relative amplitude of the two allowed helicity sectors is selected here.

## 3. Why the native finite triplet still has a two-photon map

For either equal helicity, multiply B_h(n) by the earlier even coefficients

```
chi_s=1,
(chi_x,chi_y,chi_z)=sqrt(15)*(n_y*n_z,n_z*n_x,n_x*n_y).
```

The complete photon wavefunctions are normalized and Bose-symmetric. Since B_h has unit pointwise norm and the correct rotation tensor law, their Gram and native-group transformation matrices are exactly the previously verified scalar ones. Composing with the source-pair Clebsch–Gordan matrix gives a **conditional relative two-photon isometry for all 24 native actions**, retaining all four input amplitudes.

The nonconstant functions belong to continuous angular momentum two, although their restriction to the native tetrahedral group is its vector irrep. A 45-degree rotation takes chi_z completely out of this code with squared leakage norm one. This is now also a physical photon-wavefunction leakage statement, not just a scalar-coordinate test.

Crucially R90 and the 45-degree rotation are **not in the native finite rotation set**. The continuous exclusion uses information not supplied merely by those native actions. Source identification with a physical total-J=1 input, including orbital and record content, must be justified independently before applying it.

## 4. What continuous selection still does not fix

Even if one independently supplied a continuous spin0-plus-spin1 source and allowed only the two-/three-photon sectors, a unique branching law would not follow. Let Ps and Pt be its singlet/triplet projectors. The preceding [three-photon helicity construction](THREE-PHOTON-HELICITY.md) supplies a normalized scalar and vector output code; the two-photon sector supports the singlet. For |a|^2+|b|^2=1,

```
W2=a*W2_s*Ps,
W3=b*W3_s*Ps+W3_t*Pt
```

is a continuous-rotation intertwining isometry in this conditional model. Its sector weights are

```
P2=|a|^2*||Ps z||^2,
P3=|b|^2*||Ps z||^2+||Pt z||^2.
```

The checker verifies exact isometry Grams for singlet weights (1,0), (9/25,16/25) and (0,1). This demonstrates remaining singlet freedom; it is **not** a fitted mechanism or a physical prediction that every native triplet produces three photons. That statement would additionally require the absent total-spin binding, exclusive-output assumption and interaction/preparation law. With only the finite native symmetry, even the triplet's multiplicity remains unfixed.

## 5. Exact verification and next gate

The checker verifies four exchange identities, 104 explicit frame rotation cases, and 364 frame-independent tensor rotation identities, using exact radical-field arithmetic. It checks all four reference constraint ranks via nonzero exact Gram determinants, the photon-completed native quadrupole code, its continuous leakage, and the remaining conditional singlet-weight family. General representation arguments and phase-space measures remain documented analytic inputs, not machine-formalized proofs.

The [native charge/preparation audit](NATIVE-CHARGE-PREPARATION.md) now inspects the actual spinor, flux, pairing and geometric-reversal sources. It constructs a full raw linear opposite-Pauli-code flip, excludes it from the fixed stored word class, and verifies that neither the pair swap sign nor the singlet preparation fraction is selected. The source's existing antiunitary/negative-Choi result is replayed without rerunning owner entrypoints. The [graded contact extension](GRADED-CONTACT-VERTEX.md) now constructs those resources under explicit CAR/charge postulates, preserving spectators and exposing finite-code recurrence. The [Jacobi completion](CONTACT-ESCAPE-CONTINUUM.md) now gives conditional local escape and retained bound clouds; its band and energy-uncertain preparation still need physical/source binding, not relabelling as annihilation. Do not import a positronium charge rule or a desired two-/three-output selector without a native operator and state binding. The [total-momentum successor](TOTAL-MOMENTUM-PACKET.md) now supplies a full imported Fock packet with helicity transport. The [covariant lift](COVARIANT-ESCAPE-LIFT.md) now supplies active lab dynamics under explicit velocity/mass postulates. Retain local source/cluster support, actual amplitudes, incident preparation and operation licensing as open gates.

C1–C12, exhausted C12 effort, paused high-energy execution and owner files are unchanged. Historical source warnings remain reported. No physical outcome, unique spectrum or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_two_photon_helicity.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_two_photon_helicity.py
```
