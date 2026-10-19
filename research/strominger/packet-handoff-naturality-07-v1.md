# Packet handoff ground naturality — iteration 7/10

Owner: `marici.Strominger`. **Iteration complete; objective in progress.**

[Live net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [original test](contracts/packet-handoff-naturality-07.v1.json) · [explicit revision](contracts/packet-handoff-naturality-07-revision.v1.json) · [checker](checkers/check_packet_handoff_naturality_07.py) · [receipt](results/packet-handoff-naturality-07-v1.json).

## Question, failed conjecture and disposition

Can the native proton local mode be identified with a Cartan square of an electron face spinor, and can that local relation sew into the actual native packet? Rivals are the opposite helicity, elliptical rather than circular triangle modes, and distinct supplied/block/projection transports.

**The pure-square conjecture is rejected at the first actual proton port.** All twelve local modes have circularity defect 16/25, not zero. The preserved [failed checker](checkers/check_packet_handoff_naturality_07_pure_square_hostile.py), SHA256 `d9d422336d755703a528ef3e929383d53e8a92a7cb8be0ed9137d9e3a0718713`, retains that assertion. Its scientific failure occurred at freeze `623129dcfd510b65`. Neither the metric nor the selected mode was changed to recover a circular line.

The replacement test explains the actual modes from **directed triangle geometry**, compares circular helicities only as controls, and retains failed global sewing. It is an explicit revision after counterevidence, not an unobserved prediction of the original conjecture.

## 1. Both baryon line families are actual geometric Fourier modes

For every native ordered triangle with vertices x0,x1,x2, set

    omega = (-1+i sqrt(3))/2,
    q = x0 + omega x1 + omega^2 x2.

All twelve proton and eighteen neutron selected geometric lines equal the line of this q. The exact complex amplitude/phase scale from q to the retained source encoder is recorded at every port; it is not erased or claimed to follow from an unmarked triangle alone.

Let A,B,C be its three **squared** Euclidean edge lengths. Expanding with `1+omega+omega^2=0` gives

    q* q = (A+B+C)/2,
    |q.q|^2 = A^2+B^2+C^2-AB-BC-CA,
    chi = |q.q|^2/(q* q)^2
        = 4(A^2+B^2+C^2-AB-BC-CA)/(A+B+C)^2.

The checker verifies the Fourier-line equality, tangency, norms and shape formula on all thirty actual source triangles.

| Native family | chi | Port count |
|---|---:|---:|
| Proton | 16/25 | 12 |
| Neutron, first shape | 823849/1423249 | 12 |
| Neutron, second shape | 3806401/4405801 | 6 |

For proton the squared edges are proportional to 1,3,1: they are the **subtriangles** of a regular tetrahedral face, not equilateral triangles themselves. This explains the failed circular-line identification without fitting another phase or changing geometry.

Cartan's q(z) satisfies `q(z).q(z)=0`. More generally, with the retained iteration4 Cartan matrix J, put `m=J^-1 q` and

    B(q) = [[m0,m1],[m1,m2]].

Then `det B(q)=-(q.q)/4`. Every native baryon mode here has rank-two B(q), whereas a pure spinor square has rank one. A general symmetric spinor quadratic is therefore a possible algebraic type; a **single decomposable spinor square is not**. No physical spin classification follows from that statement.

## 2. Proton has two circular components, not one helicity line

The actual proton and electron tetrahedral face normals coincide after the recorded face-label permutation. Apply the native Cartan bridge to both electron Pauli lines, P_f and I-P_f, obtaining two orthogonal circular vector-line projectors Q_minus and Q_plus in the tangent plane.

Neither equals any native proton local line. Instead every normalized proton mode has exact overlap weights

    tr(Q_native Q_minus) = 1/5,
    tr(Q_native Q_plus)  = 4/5.

The three source ports in a face have **three distinct ellipse projectors**, not one projector with three global phase choices. Their average is the rank-two mixed operator

    (1/3) sum_(ports in face) Q_native
        = (1/5) Q_minus + (4/5) Q_plus.

Replacing them by a circular helicity line or that average changes the native local preparation/readers. The shape defect and weights are compatible: `chi=4(1/5)(4/5)=16/25`.

## 3. Local circular controls fail the full native sewing square

For either circular helicity, duplicate the four face projectors into their three actual proton ports to obtain a linear adapter F from the three-dimensional symmetric-square spatial module into the twelve-port vector field. Both adapters are source-equivariant under all 24 electron operations projected to the actual proton A4 spatial group, and

    F* F = 4 I.

Actual proton L neither preserves nor annihilates these controls. Its retained norm fractions are respectively 1/5 and 4/5:

    F* L F = 4 w I.

But on the **entire** quadratic module,

    G F = N F = G L F = 0.

Thus even projecting the circular control into the actual elliptical local lines does not produce the native coherent return. Local normal matching, a symmetric-square representation or equal dimensions cannot replace the global packet sewing map. The symmetric-square spatial module is nontrivial under A4, while the native aligned body-coordinate module is trivial; the zero map is consistent with that representation obstruction.

## 4. Actual native transfer blocks and projection transport have different phases

### Electron: lossy face blocks retain curvature

For the actual native N=G, its face-to-face block is `P_j P_i/2`. The normalized line isometry is therefore

    U_(j,i) = sqrt(3) P_j P_i = 2 sqrt(3) N_(j,i).

With base points `r_f=-n_f` and the actual outward tetrahedral orientation, all four triangular loops have phase **-i**. These are exact phases of normalized **native coherence blocks**, not an assertion that the normalized move is an available native spin unitary. None of the twelve directed moves equals the restriction of any of the 24 native spin unitaries. At a fixed face, an actual order-six native spin lift instead has a sixth-root line character whose square is the spatial order-three character. Central spin sign is retained by that native operation and lost by the quadratic readout.

### Baryons: coherent rank-one blocks give flat code transport

Write v_i for the independently reconstructed selected vector at port i, s_i=v_i*v_i and rho for the total source norm. Native N blocks, using the exact source-plane embedding for neutron, give

    T_code_(j,i) = v_j v_i*/s_i = (rho/s_i) N_(j,i).

These preserve the retained scalar amplitude and compose exactly. All seven fundamental cycles of each actual dual graph return the original line state. For neutron the metric comparison uses the native intrinsic-plane embedding and its metric left inverse, not arbitrary free ambient preparations.

In contrast, geometric line projection uses `Q_j Q_i`. Its loop scalar lambda has modulus squared equal to the product of edge overlaps. The receipt retains lambda and its normalized phase squared without introducing unrecorded square roots. In the declared spanning-tree cycle bases, **7/7 proton and 6/7 neutron projection loops are nontrivial**, despite flat native code transport. Those counts describe these bases, not a topological charge.

### Circular controls are not native proton loops

The electron symmetric-square circular controls have projection-loop phase -1, while the supplied body-frame comparison around the same loop has phase +1. This is a valid control distinguishing connections, but the control line is **not** the native elliptical proton mode. The actual proton projection phases are recorded separately above. No scalar frame gauge can remove either witnessed loop mismatch.

The flat faithful two-face electron atlas from iteration6 remains valid: it retains the whole doublet. It does not flatten the lossy one-face blocks, identify them with native spin words, or turn a block normalization into a licensed primitive command.

## 5. Next executable frontier

`native-corner-cycle-metric-versus-Pauli-null-geometry`: reconstruct each real triangle-plane corner-cycle operator and average its actual metric over that cycle. Compare the resulting invariant complex structure with the retained Euclidean metric and the Pauli/Cartan null condition. Test whether circularizing a native baryon mode changes L/G/N preparation readers or requires additional metric/phase data. The actual triangles, modes, operations and readers exist; no missing-authority branch is being reopened by abstraction.

The source-selected indexed handoff and common physical M/C grading remain absent. The geometric Fourier constructor and transport distinctions are surviving source-level results, not assignments of proton/neutron/electron spin, charge, mass or physical time.

## Verification

The revised checker passes **31 exact groups** and a same-checker frozen challenge at `dc1da953bb6e5c8019d77d1e5654dbca5b5fcde4403eb8d686d74342bfe12f5c`. It pins both the failed source and the versioned revision. Early execution defects were a missing tuple parenthesis, an incorrectly transcribed Cartan matrix and an unhashable algebraic-value set; they were corrected and refrozen separately from the scientific nullity failure. The retained Cartan matrix is now checked directly against iteration4.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-07-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

These are bounded executable checks, not independent peer review or proof-assistant certification. No native producer, other-owner fixture edit, proof-assistant run, commit, push, publication or deployment is performed.
