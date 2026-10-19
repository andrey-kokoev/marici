# A three-helix candidate for the rung-12 field

## Outcome

We can construct three nonintersecting helices and encode the complete rung-12 field on labelled samples along them. The two complementary-sector strands have opposite handedness and opposite axial travel.

However, this explicit layout **does not realize the full tetrahedral symmetry as ambient rotations**, and the middle helix **does not form a separating barrier**. Those stronger interpretations fail even though the field encoding is exact.

This is a candidate layout for the field tower, not a new isotope construction or a claim about DNA or physical particle trajectories.

## Explicit geometry

Use real parameter t increasing along each directed strand:

```
h_Q1(t) = (cos(2*pi*t),   sin(2*pi*t),    t),
h_P(t)  = (2*cos(2*pi*t), 2*sin(2*pi*t), 2*t),
h_Q2(t) = (3*cos(2*pi*t), 3*sin(2*pi*t), -t).
```

The radii 1, 2 and 3 are disjoint, so no two strands intersect for any pair of real parameters. The middle helix is radially between the other two. The radii and pitches are declared drawing choices, not parameters derived from the field metric.

For Q1 and Q2, the signs of dz/dtheta are opposite, giving opposite handedness. With t increasing, their axial velocities are also opposite. Their angular velocities have the same sign.

This distinction is unavoidable: reversing both angular and axial velocity leaves the sign of dz/dtheta unchanged and therefore does not reverse handedness. Here “opposite travel” means opposite **axial** motion, as in the preceding proposed parametrization. Traversing a fixed helix backward also does not change the curve's handedness.

## Assigning the field without inventing a canonical strand basis

Rung 12 has twelve labelled directed edges, each carrying a corner vector c_e in C3. The source supplies a positive metric K3 and a rank-one K3-orthogonal projector P, with Q=I-P.

Choose a basis as follows:

1. one nonzero column of P;
2. one nonzero column of Q;
3. a second Q column, orthogonalized against the first Q vector.

This is a reproducible coordinate convention, not a physically selected basis of the two-dimensional complement. Write S for the matrix of these three basis vectors. Its Gram matrix D=S* K3 S is positive diagonal, without needing square-root normalization.

Encode

```
a_e = S^{-1} c_e.
```

Put the P coefficient a_e[0] on the radius-2 middle strand, and the two Q coefficients on the radius-1 and radius-3 strands. Directed edge e_k, in the declared lexicographic order, occupies phase t=k/12 on each strand. There are twelve labelled channels on each of three strands, hence 36 complex amplitudes.

All four endpoint labels and ordered-edge incidences remain explicit metadata. They are not inferred from which plotted points happen to be near each other. No extra field component is introduced by drawing the middle strand.

## What is preserved exactly

Recovery is c_e=S a_e. The coefficient norm is

```
sum_e c_e* K3 c_e = sum_e sum_j D[j,j] |a_e[j]|^2.
```

This is metric preservation for the complex field amplitudes with retained weights. It is not equality with Euclidean distances between plotted sample locations.

The named operations transport by change of basis:

- L becomes the P-component projector on every edge;
- G continues to average the same component across the twelve edge labels;
- the named corner cycle becomes S^{-1} C S and still has cube equal to identity.

The transported C is not a pure permutation of three strands. It mixes amplitudes and retains its source non-unitarity in the transported metric. Likewise, the projector-preserving U(2) action can mix the two complementary amplitudes without being a rigid motion swapping the two differently sized helices.

Thus this is a faithful **algebraic encoding carried by a chosen layout**, not evidence that all named operations are spatial motions of that layout.

## Tetrahedral symmetry test

Use the standard centered tetrahedron with vertices

```
(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1).
```

Its twelve proper rotations give the standard A4 action. This coordinate choice is a conventional tetrahedral realization; it is not a fitted isotope geometry.

For the complete three-curve union above, (1,0,0) is its unique point of Euclidean norm one. On Q1 the squared norm is 1+t^2, while the other two radii already exceed one. Any ambient rotation preserving the union must therefore fix (1,0,0).

Of the twelve tetrahedral rotations, exactly two do so:

- identity;
- the half-turn about the x axis.

The half-turn sends every h(t) to h(-t). It preserves the **unoriented complete curves**, but reverses their declared traversal. Consequently only identity preserves the directed layout. Only identity also preserves the actual finite set of 36 sample positions at t=k/12.

The full A4 action still acts on retained endpoint labels and field values; the checker verifies all twelve relabellings. But those relabellings are not realized by the corresponding ambient rotations of the helix drawing. Retaining a label action is not a spatial symmetry proof.

This rejects the full-A4 interpretation of this particular layout, not every possible construction involving helices. A tetrahedrally arranged family of axes or a different incidence realization would be a different candidate requiring its own tests.

## Why the middle helix does not separate the others

At z=0, the three helices meet that plane at (1,0,0), (2,0,0) and (3,0,0). The path

```
gamma(s) = (2-cos(pi*s), sin(pi*s), 0),    0<=s<=1,
```

joins the inner and outer points. Its distance from (2,0,0) is identically one, so it never touches the middle helix. At z=0 that point is the middle helix's only intersection.

Thus the middle strand is radially intermediate but is not a barrier preventing passage between the other two. The **whole radius-2 cylinder** would supply a separating surface between radii 1 and 3; a single helix lying on it does not. Introducing such a surface or a separating boundary condition would be additional structure, not something established by the rank-one P sector.

The algebraic P/Q orthogonality is a different meaning of separation: it splits coefficient sectors in a metric space, not regions of three-dimensional space.

## Verification and drawing

```
python research/strominger/checkers/check_rung12_helix_candidate.py
```

Outputs:

- `research/strominger/results/rung12-helix-candidate/verification.json`
- `research/strominger/results/rung12-helix-candidate/helix-layout.svg`

The field, metric, basis transformations, named operators, twelve exact sample phases and tetrahedral matrices use exact algebraic arithmetic. Nonintersection and the bypass path have all-parameter arguments above. The SVG is only a sampled illustration; no result relies on visual overlap or floating-point drawing accuracy.

No viewer, production model, isotope grammar or physical admission is changed.
