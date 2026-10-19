# Packet handoff ground naturality — iteration 4/10

Owner: `marici.Strominger`. **Iteration complete; objective in progress.**

[Live conjecture net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [contract](contracts/packet-handoff-naturality-04.v1.json) · [exact checker](checkers/check_packet_handoff_naturality_04.py) · [receipt](results/packet-handoff-naturality-04-v1.json).

## 1. Dimensions do not identify geometric main spaces

Iteration2 selected M as the smaller full L/G image channel space. This iteration asks whether that M can literally be the unmarked geometric spatial vector representation V, **under the actual retained source actions**.

For each source I solved every coefficient of

    R_g X = X M_g

by exact RREF over the inherited number field. The domain is the **full M channel space**, not its active return alone; V is the complexification of the actual real spatial carrier. Baryon spatial rotations are freshly reconstructed from the supplied affine generators in the actual native frames. Electron uses all24 native spin operations and their Pauli spatial action. Source and target metrics are retained and transported in nonmonomial frame controls.

| Native source | dim M | dim V | dim Hom(M,V) | Result |
|---|---:|---:|---:|---|
| Proton | 3 | 3 | **0** | No nonzero unmarked linear geometric-vector map |
| Neutron | 3 | 3 | **3** | Invertible module maps exist, but are not uniquely selected |
| Electron | 2 | 3 | **0** | Central spin sign obstructs even a nonzero linear map |

This refutes the **tested capacity-M = common unmarked geometric-main-vector** interpretation. It does not refute all possible meanings of M, all source-native particle candidates or nonlinear/associated-bundle geometry.

## 2. Proton: M is a native transported body-frame fiber

Both actual proton generators act as **I_3 on M=Image(G)**. Their spatial A4 representation is nontrivial with no fixed vector. Three trivial channel copies therefore cannot be equivariantly identified with the spatial three-vector, despite equal dimensions. Replacing the native M action by the spatial rotation fails the actual source encoder square.

There is nevertheless a fully source-native geometric alternative. The actual twelve geometric transport frames R_t give invertible port evaluations

    F_t : M -> V,
    F_t = R_t B_body,
    F_(g.t) M_g = R_g F_t.

All twelve squares and inverse maps are checked. The entire **port-indexed field** is covariant without selecting a distinguished port. A single evaluation requires retaining its port mark.

The unmarked sum is exactly zero:

    sum_t F_t = 0.

Erasing the mark is not harmless: I constructed different full-M inputs at different ports with the same evaluated vector but different native encoded fields. This is a body-frame/associated-field interpretation, not a canonical unmarked ambient main-space identification. The collision is on the full alignment-image task; it is not asserted to lie entirely in the proton's rank-one active return.

## 3. Neutron: actual centroids miss the active scalar line

The source's local M representation is the three-sector cyclic permutation. Its native spatial rotation is the same three-cycle, so Hom has dimension3. This is **C3-module equivalence at the supplied source symmetry scope**, not a unique physical identification or a claim about every additional symmetry of the unmarked geometric belt.

Reconstruct the actual centroid of each six-triangle sector in the native Cartesian frame. The resulting geometric map is

          2/3 * [ 1 -1  0 ]
    C =         [ 0  1 -1 ].
                [-1  0  1 ]

It intertwines the native source actions but has rank **2**. Let

    P_axis = (I+S+S^2)/3 = Q_M,
    P_plane = I-P_axis.

Then

    C P_axis = 0,
    C* C = (4/3) P_plane.

The invariant axis is precisely the native active return line. Thus the obvious centroid bridge sends the coherent invariant mode to **zero**, not to a recovered geometric main vector.

Two complete maps are

    J_+ = C + (2/sqrt(3)) P_axis,
    J_- = C - (2/sqrt(3)) P_axis.

Both are invertible, equivariant and have the **same** target Gram `(4/3) I`. The native M Gram is another positive scalar times I, so both have the same metric calibration up to one common overall scale. Yet they have opposite signs on the active line. Symmetry, centroid geometry and this metric condition do not choose that sign.

The natural retained decomposition is therefore **an invariant scalar channel plus a moving geometric plane**, with an unselected axis completion—not an identification obtained from the number3 alone.

## 4. Electron: genuine quadratic geometry, not linear spinor/vector equivalence

The actual central native element acts as `-I_2` on M but `+I_3` on V. A linear equivariant map would require X=-X, hence X=0.

Two stronger, positive geometric bridges do exist:

### Density/Pauli bridge

For a logical spinor z, set rho=z z*. Then

    r_a = tr(sigma_a rho),
    rho = (tr(rho) I + sum_a r_a sigma_a)/2.

The linear map `End(M) -> V` intertwines all24 operations; its equivariant Hom space is one-dimensional, so this bridge is unique up to scale at the retained symmetry scope. Its kernel is the scalar identity line. Full density reconstruction is checked as a matrix identity, not merely sampled.

The actual four face effects satisfy

    E_f = P_f/2,
    probability_f = (tr(rho) - n_f dot r)/4.

Native face permutations and normal-vector transport commute with this bridge for all24 actions.

### Native Cartan/symmetric-square bridge

In the Pauli-compatible spatial convention, the existing native Cartan formula is

    q(z) = (z_0^2-z_1^2, i(z_0^2+z_1^2), -2 z_0 z_1).

The third-coordinate flip relative to the native `cartan` helper is explicit. It gives an invertible linear intertwiner

    Sym^2(M) -> V_complex,

again with a one-dimensional equivariant Hom space. This is an exact spinorial square-root relation to a complex spatial null vector, not an invented handoff tag.

Formal polynomial calculations in independent variables `a,b,conj(a),conj(b)` verify universally

    q dot q = 0,
    q* q = 2 (z* z)^2,
    r dot r = (z* z)^2.

Both quadratic bridges intertwine all24 native operations, and the declared Cartan convention is also compared with the actual helper on normalized native-field samples.

### Exact recovery boundary

Neither readout is an equivalence of the original coherent packet task:

* rho/r loses the whole U(1) spinor phase;
* q loses at least the central sign: q(z)=q(-z).

But z and -z have **opposite native encoded complex fields** and are distinguished by retained linear raw readers/history. The actual central native operation realizes this sign change. No physical claim about which coherent readers are experimentally observable is imported; the stated retained task includes them.

## 5. What this grounds—and what remains

The three smaller channel spaces have concrete, different source-natural meanings:

* proton: transported body-frame fiber over geometric ports;
* neutron: cyclic placement module with invariant scalar and moving plane;
* electron: spinor module with natural quadratic spatial observables.

These are not three copies of the same unmarked geometric main vector. The proposed indexed words remain conditional role windows; no source-selected physical M/C grading or indexed event-boundary law has yet been derived.

**Iteration5 executable frontier:** `source-native-boundary-module-and-role-grading`. Reconstruct the actual geometric boundary/incidence modules and transport native port groupings into them. Test carrier-relative M/C grading using proton boundary triangles, neutron sector patches and electron face-associated spinor lines. Keep geometric base dimension/codimension distinct from representation dimension and complex fiber rank. Any common grading must commute with the same native operations and preserve its declared reader task.

## Verification

**23 exact check groups pass.** A first baseline passed at `beb9b931e1d44fca`; the checker was then strengthened with full density splitting, all face-normal squares and formal polynomial norm/null identities. The strengthened baseline was refrozen before its successful check and passing same-checker challenge:

`research/strominger/scc-freezes/packet-handoff-naturality-04-v1.ef82d8effa47e90e.json`.

The challenge is not independent peer review. No mathematical acceptance was weakened.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-04-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

Native producers, other-owner/shared fixtures and proof-assistant sources were not modified or run. No physical particle/clock identification, commit, push or deployment is supplied.
