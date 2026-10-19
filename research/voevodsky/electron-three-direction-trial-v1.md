# Electron three-direction trial

## Result

For the full normalized spinor, a three-direction packet has a particularly natural presentation:

\[
[z;\,(E_1z,E_2z,E_3z)],\qquad z\in\mathbb C^2,\quad z^*z=1.
\]

The three matrices are actual quaternion-unit rotations in the retained electron source:

\[
E_1=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
E_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
E_3=\begin{pmatrix}0&i\\i&0\end{pmatrix}.
\]

They provide a global real tangent frame on the normalized spinor sphere S3. Phase is included in these directions, rather than omitted from the tuple and assigned entirely to the retained label complex.

This is a stronger concrete candidate than merely counting three local parameters. It does not yet identify a physical electron or prove that this is the correct packet-counting convention.

## All-input frame identities

The source matrices satisfy

\[
E_a^*=-E_a,\qquad
E_a^*E_b+E_b^*E_a=2\delta_{ab}I.
\]

Consequently, for every normalized z,

\[
\operatorname{Re}\langle z,E_a z\rangle=0,\qquad
\operatorname{Re}\langle E_a z,E_b z\rangle=\delta_{ab}.
\]

Thus these are three independent tangent directions at every marked state, not only at one chart center. All 24 retained binary tetrahedral rotations transport the frame by real orientation-preserving orthogonal matrices. No spatial axes are being assigned to a physical electron.

The phase direction iz is a state-dependent linear combination of this frame. At z=(1,0), it is E1z; elsewhere it need not coincide with any one frame member. The earlier two-ray-directions-plus-phase presentation and this three-frame presentation are different decompositions of the same normalized carrier.

A unitary change of spinor coordinates maps the construction compatibly. The tuple is a presentation with frame-change witnesses, not an extra immutable choice of physical axes.

## Three coordinates and recovery

For t=(t1,t2,t3), let s=t1²+t2²+t3² and define

\[
C(t)=\frac{(1-s)I+2(t_1E_1+t_2E_2+t_3E_3)}{1+s}.
\]

The quaternion identities imply C(t)*C(t)=I for all real t. The map t ↦ C(t)z is a chart covering S3 except -z, with three independent derivatives 2Eaz at the origin. A second chart -C(t)z covers that missing state. On their overlap the coordinate transition is t ↦ -t/|t|². A global frame therefore does not mean one global real coordinate chart.

The original face encoding retains every such spinor. The checker uses the existing exact-field scaling K=√2 J, with decoder K*/2. Its composition is identity on the logical carrier and N on the retained raw subspace. No native source artifact is rewritten.

## Twelve sectors: a useful split between two trials

The three-direction frame permits 3 × 2 × 2 signed codimension-one sectors. There are two distinct operational interpretations.

### Constant native generators

For any distinct axes a,b and signs ε,η, put A=εEa and B=ηEb. Then

\[
AB=-BA,\qquad (AB)^*(BA)=-I.
\]

All twelve signed direction pairs have this obstruction. Their two ordered operations end at the same ray but opposite full spinors. Each individual operation has exact inverse recovery, but the two paths cannot be silently identified as the same amplitude-preserving square.

A three-direction spinor packet therefore has richer coherence than a flat coordinate cube with identical generators on parallel edges.

### Supplied coordinate-dependent transports

A conditional coordinate construction does work. Supply

\[
T(v,u)=C(v)C(u)^*.
\]

Along the coordinate grid, these transports telescope. Both orders around each of the twelve central signed coordinate squares have identical full-spinor endpoints. At each of the eight three-coordinate corners, all six orders agree.

The corresponding logical/raw capability pair can be written in the native isometric normalization as

\[
i_C=JC,\qquad o_C=C^*J^*,\qquad
o_Ci_C=I,\quad i_Co_C=N,\quad(i_Co_C)^2=i_Co_C.
\]

The exact checker verifies the equivalent scaled-K formulas at all grid vertices. These are explicit recovery and fourfold identities for the supplied finite linear model.

**The extra transports are substantive.** Among the 27 chart matrices at coordinates {-1,0,1}³, fifteen belong to the retained binary tetrahedral action set and twelve do not. In particular, every central two-coordinate corner requires an additional matrix. The construction is not obtained by composing only the native finite generators, whose closure remains the same 24-element group.

This establishes a finite coordinate-sector realization if these additional SU(2) capabilities are admitted. It does not establish their primitive cost, their derivation from the native 144-transfer protocol, a full higher capability complex, or packet minimality. The continuum of normalized states and the operational availability of every interpolating unitary are separate assumptions.

## Consequence for electron, positron, proton and neutron

This trial makes n=3 natural for the **full normalized spinor interface**, with phase retained as a direction of variation. It does not make n=3 unique to baryons. The same spin-state construction can apply to other spin-1/2 carriers; charge, magnetic response, strong coupling and internal structure require additional operational distinctions in their retained complexes.

At n=3, the proposed common accounting gives

\[
108+432+1296=1836.
\]

It would give this sum for the electron candidate too. Thus n alone cannot distinguish electron and proton masses under this convention. Any physical accounting must specify additional capability/cost data rather than select different dimension conventions for different particles.

## Reproduction

```text
python research/voevodsky/checkers/check_electron_three_direction_trial.py
```

Receipt: `research/voevodsky/results/electron-three-direction-trial-v1.json`.

Seventeen checks pass: source freshness, global-frame matrix identities, rational charts, native encoder recovery, phase inclusion, finite frame transports, all twelve native order obstructions, supplied coordinate-sector agreement, supplied port recovery/fourfold identities, and the eight six-order comparisons. The prerequisite is the existing passing two-direction/phase trial and its isolated native-producer replay. All bound inputs remain unchanged.

Verification uses exact coefficient arithmetic, all-input matrix identities and declared finite chart samples. It is not proof-assistant certification. The existing Three.js page remains the two-direction-base-plus-retained-phase view; this new trial has not yet been added to that visualization.
