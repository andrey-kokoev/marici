# Four-stage paw closure: geometric algebra versus packet execution

## Supplied geometric realization

Begin with a flat paw with triangle ABC and leg AD:

    A=(0,0,0), B=(1,0,0), C=(0,1,0), D=(-1,0,0).

The initial graph has AB,AC,BC,AD and eight directed packets. Three-dimensional
Euclidean Cl(3,0), the embedding, the rotation axes and the completion rule are
inputs. This experiment does not derive three-dimensional space from the paw.

The proposed stages are realized as follows:

| Stage | Operation | Packet incidence |
|---|---|---|
|1: identity|Retain the flat paw and its labels|8 directed packets|
|2:1:many|Rotate the triangle about the fixed AD axis by phi|8 packets; triangle-orientation family|
|3:many:1 candidate|Rotate the leg about the transported AC axis by theta; compare the two operation orders|8 packets; congruent body-frame presentations at fixed theta|
|4:closed identity candidate|Add BD and CD from retained BA+AD and CA+AD paths|12 packets; complete tetrahedral graph|

Rotation generates the family. The many-to-one operation would collect congruent
presentations at fixed theta into a common record while retaining frame and path
witnesses. The experiment verifies congruence; it does not implement a quotient
of the continuous family or identify differing theta values.

## Commuting rotation square

Let H(phi) rotate about the initial leg axis and L(theta) rotate about AC.
After rotating the body, the leg's triangle-attached rotor is

    L_transported = H L H^-1.

Consequently

    L_transported H = H L.

One route rotates the body, then the leg about the transported axis. The other
rotates the leg first, then rotates the whole configuration by H. Both retain
the original labels and agree at their final coordinates.

An explicit continuous square is:

    A(s,t)=A,
    B(s,t)=H(s*phi)B,
    C(s,t)=H(s*phi)C,
    D(s,t)=H(s*phi)L(t*theta)D.

Its boundary supplies the two routes and a homotopy between them in the ambient
configuration space. This is a mathematical construction with numerical boundary
checks, not an Agda proof identifying its homotopy with the existing tower maps.

## Independent mechanical check

One implementation uses explicit Clifford blade products and rotor sandwiches.
The other uses Rodrigues rotation matrices. Packet completion separately searches
the initial incidence graph for two-step paths. The only missing pairs are:

- BD with retained BA,AD;
- CD with retained CA,AD.

Their composed packet displacements agree with the geometric-algebra edge
vectors. Both orientations of each connection are retained. Rotations alone
leave the packet incidence unchanged; the explicit completion operation adds
four directed packets.

The geometric-algebra trivector volume matches the independent scalar triple
product. Oriented triangular-face area bivectors sum to zero, checking boundary
closure. Including a filled tetrahedral cell amounts to taking the nondegenerate
convex hull; graph completion by itself does not produce a simplicial filler.

## What is produced

For the supplied unit right-triangle seed, signed volume is sin(theta)/6,
independent of the body angle phi.

| Leg angle theta | Volume | Nondegenerate tetrahedral realization |
|---:|---:|---|
|0 degrees|0|no: planar|
|30 degrees|1/12|yes|
|45 degrees|sqrt(2)/12|yes|
|60 degrees|sqrt(3)/12|yes|
|90 degrees|1/6|yes|
|135 degrees|sqrt(2)/12|yes|
|180 degrees|0|no: D coincides with B|

The missing-edge squared lengths are BD^2=2+2cos(theta) and CD^2=2. Thus different
theta values generally give distinct geometries. The closure rule selects no
preferred angle. The90-degree case is a right tetrahedron, not a regular one;
the initial right triangle already fixes unequal base edge lengths.

Five body angles and seven leg angles give35 independent comparisons. Body
orientation changes preserve all edge lengths and volumes at fixed theta.
A full body turn preserves vector positions but ends at rotor-1 rather than+1;
that retained rotor distinction is checked without assigning a particle spin.

## Outcome

The proposed four-stage picture admits a concrete, internally consistent
realization: a flat paw can be moved into a noncoplanar configuration, and its
witnessed missing connections close the tetrahedral graph. The conditional
predictions are explicit and agree between two implementations. The selected
axes, completion constructor and continuous-family identification still need
connection to the fiber tower; none is implied merely by the rung labels.

## Verification

```
python research/nima/checkers/check_paw_rotor_tetrahedron.py
```

All35 cases and controls passed with tolerance1e-10. No external numerical
libraries are required. Results: `results/paw-rotor-tetrahedron.json`.
