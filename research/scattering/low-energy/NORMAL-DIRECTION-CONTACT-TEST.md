# EF1-N: a concrete contact-support proposal fails its generic two-output test

[EF1](EDGE-FACE-ANNIHILATION-CONJECTURE.md) · [phase continuation](HINGE-PHASE-CONTINUATION.md) · [frozen candidate](contracts/normal-direction-contact.v1.json) · [checker](check_normal_direction_contact.py) · [receipt](results/normal-direction-contact.v1.json)

## Result: reject the literal normal-direction implementation, not every geometric explanation

We tested a concrete additional readout/selection hypothesis instead of leaving the contact law wholly unspecified:

> In the isolated incoming pair's centre-of-momentum frame, each extracted output triangle emits a positive-energy massless ray along its normal (either sign is allowed). A contact conversion operator may connect only records satisfying total four-momentum conservation. For generic edge release, first test all ways of partitioning the six vertices into two triangles without changing their geometry.

These are **new hypotheses**, not consequences of the native source. They give a necessary support condition, not a fully specified self-adjoint contact Hamiltonian or a photon dictionary.

**This implementation fails:** the old ACE/BDF two-output template never permits two such momenta at any non-superposed hinge angle. Moreover, all ten complementary two-triangle partitions fail on an explicit open interval of admissible edge placements. Changing phases, coupling strengths or normal signs cannot repair that support failure.

The face-sharing three-triangle construction does admit balanced massless momenta, but only in its rigid equal-energy, 120-degree configuration. That is kinematic permission, not a production mechanism or a rate.

## 1. Independent conservation constraint

Set c=1. For an exclusive isolated two-ray final state in the incoming CM frame,

```
E1*n1 + E2*n2=0,   E1+E2=M>0,   |n1|=|n2|=1, E1,E2>0.
```

Necessarily n2=-n1 and E1=E2=M/2. Allowing either sign of each triangle normal still requires their unoriented normal lines to be parallel. A nonzero cross product therefore rules out the conversion for every choice of positive energies.

This uses ordinary massless energy–momentum conservation as an independently stated physical input. It does not derive relativity, the direction map or massless photons from the seed. If an apparatus or residual object carries recoil, this is no longer the exclusive isolated two-photon claim being tested.

## 2. The existing two-triangle template fails at every angle

Keep the native tetrahedron ABCD and its AB hinge. Let M be the edge midpoint, c=C-M and d=D-M. For a congruent second tetrahedron ABEF write

```
E=M+(a-b)c+3b*d,
F=M-3b*c+(a+b)d,
a=cos(phi),  b=sin(phi)/(2sqrt(2)),  a^2+8b^2=1.
```

For the earlier proposed outputs ACE and BDF, take the unnormalized normals

```
N1=(C-A) cross (E-A),
N2=(D-B) cross (F-B).
```

Putting u=a-1 gives

```
N1=2(u-4b, u+8b, -u+4b),
N2=2(u+4b, -u+8b, u+4b),
(N1 cross N2)_z=-8*u^2-256*b^2.
```

This is strictly negative except at a=1,b=0, where the bodies superpose and the output triangles degenerate. Thus the original two-triangle construction cannot realize the proposed exclusive two-ray readout at any distinct hinge placement.

The checker also verifies the polynomial identity in the rational hinge chart

```
a=(1-2r^2)/(1+2r^2), b=r/(1+2r^2),
(N1 cross N2)_z=-128*r^2*(r^2+2)/(1+2r^2)^2.
```

The missing chart point phi=pi is checked separately and gives cross-product z component -32. Admissible non-overlapping finite-chart placements have |r|>=1/2, with equality the face-contact endpoints.

## 3. Exhausting the ten vertex-disjoint alternatives

There are exactly ten unordered complementary partitions of ABCDEF into two triples. We allow all of them, not only ACE/BDF, and allow both normal orientations.

At r=2, so a=-7/9,b=2/9, **none has parallel normals**. This is phi=2*alpha, where cos(alpha)=1/3: a source-geometric witness, not an observationally fitted angle.

For every partition the checker constructs the cleared polynomial cross product and encloses a nonzero component throughout

```
r in [1999/1000,2001/1000].
```

All interval enclosures exclude zero. This gives a whole open family of edge encounters with no permitted two-ray conversion in the declared extraction class.

More generally each chosen component is a nonzero polynomial divided by a positive power of 1+2r^2. It has finitely many roots, so almost every hinge angle fails for every one of the ten partitions. This analytic conclusion does not require a numerical scan or a fitted angular acceptance.

At the witness the smallest squared sine between unoriented normal lines is exactly

```
104/729,   hence |cos(angle)|<=25/27.
```

Even replacing rays by wavepackets strictly supported in narrow cones does not remove this witness obstruction: if each cone half-angle epsilon satisfies

```
sin(epsilon)^2 < 1/27,
```

no choice of two directions in the cones can be back-to-back. The threshold is about 11.1 degrees. This is a support statement, not a bound for arbitrary broad wavepackets or distributions with nonzero tails everywhere.

**Important exception:** at phi=pi four different partitions do have nondegenerate parallel normals:

```
ACD / BEF, ACF / BDE, ADE / BCF, AEF / BCD.
```

At this placement the six points are centrally symmetric about M, with antipodal pairs A/B, C/E, D/F. The four allowed partitions are antipodal face pairs of their octahedral convex hull. This does not assert that the two input tetrahedra fill that hull: completing the body would be another operation. Two of these pairs, **ACD/BEF and AEF/BCD**, already consist of faces present in the input tetrahedra and do not need new cross-body edges. They are concrete alternative two-output geometries to investigate, with balanced energies M/2—not implementations of separation or photon identity.

Therefore this is not a no-go for every edge-mediated two-output construction. A dynamically selected special release angle, reorientation during separation, a different extraction rule or a different independently justified momentum map could change the conclusion. Those are new constructions to derive and test, not permissions to retain the failed generic claim unchanged. Static zero measure does not forbid dynamical hitting of such a special angle.

Vertex-disjointness is the deliberately restricted search class here, not a theorem that independent quantum factors require disjoint geometric support. Overlapping supports with explicit factor operations and retained residuals remain outside this classification.

## 4. The three-face channel: allowed, but very rigid

For the existing ABC face-sharing pair, let e be the reflected apex. The extracted triangles ADe,BDe,CDe have oriented normals

```
N_A=(16/3,-16/3,0),
N_B=(-16/3,0,-16/3),
N_C=(0,16/3,16/3).
```

Their sum is zero, all squared lengths are 512/9 and each pair has dot product -256/9. Thus their normalized directions are 120 degrees apart. With all three signs consistently chosen, positive energies M/3 give three null four-momenta adding to (M,0,0,0).

The normal matrix has rank two and kernel spanned by (1,1,1). Under this fixed normal readout, CM momentum conservation therefore forces equal energies; it does not supply the general unequal-energy three-body spectrum. Claiming that this rigid picture explains all three-photon events would require an additional independently derived shape, recoil or momentum-profile mechanism. We have not imported a dataset or performed an empirical spectrum comparison here.

The three faces still share De. Their independence, separation, photon identity and production amplitude remain unproved. Passing the conservation test is necessary, not sufficient.

## 5. Consequence for the contact operator and EF1

Any isolated conversion operator supported on these unmodified normal-direction output records must have zero two-output matrix elements throughout the certified open interval, irrespective of a proposed scalar coupling. Coherent sums of forbidden total-momentum records do not restore support in the conserved momentum sector; zero mean momentum is not exact momentum conservation. A unitary completion or phase controller cannot turn a momentum-forbidden record into an allowed exclusive final state.

We therefore reject **EF1-N's generic edge-release realization**. This is a criticism of a specific, frozen realization—not a refutation of all EF1 constructions. It is progress beyond fitting another capture mixer: one natural proposed physical readout is now constrained and partially eliminated.

A concrete next candidate must supply a **momentum-conserving separation map** or independently selected special-angle release, together with its native operation/phase witness. It must explain the allowed output directions and energy sharing before a branching amplitude is inferred. Simply identifying the extracted triangles with already separated photons no longer suffices.

## Verification boundary

Exact rational algebra verifies the source hinge parameterization, all ten partitions, the original template's polynomial obstruction, interval separation, the angular witness bound, exceptional pi placements and the three-face Gram identities. The conservation argument, finite-root reasoning and cone interpretation are documented mathematics, not machine-formalized proofs. No finite check licenses the new physical readout.

The source owner receipts, C1–C12 dispositions, exhausted C12 budget and high-energy pause are preserved. No physical outcome or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_normal_direction_contact.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_normal_direction_contact.py
```
