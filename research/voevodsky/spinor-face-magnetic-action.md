# Magnetic feedback on the source spinor loops

## Result

The existing cosine magnetic law now acts on the four source-derived triangular loops. The full weighted matter/electric/magnetic feedback preserves Gauss and total instantaneous Hamiltonian power balance.

A finite magnetic stiffness does NOT exactly preserve the native spinor flux. Every pure coherent spin has a nonzero circulating current with squared norm 1/9. At native flux the magnetic gradient is zero, so the current drives the field away from that flux for every finite stiffness.

An exact source-flux constraint does preserve the native kinetic doublet up to gauge. Its reaction force is constructed explicitly. Charged-density relaxation in that constrained sector is the next energy calculation.

## 1. Actual loop incidence

The four matter ports are the original tetrahedral faces. Their six shared-edge contacts form the dual tetrahedron. The four triangular loops surround the original tetrahedral vertices; they are the four faces of this geometric dual, not arbitrary triangles added to an abstract graph.

Orient them as the boundary of [0,1,2,3]:

    [1,2,3]-[0,2,3]+[0,1,3]-[0,1,2].

Let B be the vertex-edge incidence and C the resulting face-edge incidence. Exact checks give

    B C^T=0,
    sum_f C_f=0,
    C C^T=4I-ones,
    B^T B+C^T C=4I.

There are three independent face constraints. The source hopping Wilson phase is +i on every oriented dual face under this convention. Reversing orientation conjugates all phases without changing the energy law.

These loops can be embedded on the electron's six internal edges of the existing common exterior graph. They remain present in empty, electron, proton and belt configurations. The source connection is fixed data; the dynamical gauge field changes its relative flux.

## 2. Reuse the full magnetic action

Let Omega_source,f be the source Wilson phase and Omega_total,f its value after multiplying each source hopping by exp(i*q*A). Use

    H_mag = kappa sum_f[1-Re(conj(Omega_source,f)*Omega_total,f)]
          = kappa sum_f[1-cos((C A)_f)].

For q=+/-1, the cosine energy is the same. This anchors the DYNAMICAL flux to zero relative to the intrinsic spinor connection, not to a flat total spinor connection.

The complete link force is

    dot(E)=-q J_matter-kappa C^T sin(C A),
    dot(A)=beta E.

Because B C^T=0, the magnetic force does not change Gauss divergence. The exact weighted current calculation gives

    d/dt(B E-q rho)=0,
    dot(H_matter)+dot(H_electric)+dot(H_mag)=0.

The onsite coefficient 1-sqrt(3) from the source spinor adapter is retained. No contact diagonal or field energy is discarded.

## 3. Finite stiffness: an exact preservation falsifier

For a pure coherent spinor with unit Bloch vector s, the edge current is, up to the selected orientation,

    J_ij=-(n_i cross n_j) dot s /4.

The tetrahedral source normals obey

    sum_edges (n_i cross n_j)(n_i cross n_j)^T=(16/9)I.

Consequently ||J||^2=1/9 for EVERY pure logical spin. Also B J=0 and C^T C J=4J: this is a genuine circulation, not a density imbalance.

At A=0 the magnetic gradient vanishes. Hold the source state and its Gauss-compatible electric field fixed and vary

    delta A=-q J.

The complete energy derivative is -||J||^2=-1/9. It is strictly negative for every finite kappa. Magnetic energy starts only at quadratic order and cannot cancel this linear response. Thus exact native source flux is not even a local minimum of the unconstrained finite-stiffness model.

For large kappa with matter FROZEN, the leading response is

    A_cycle=-q J/(4 kappa),
    delta H=-1/(72 kappa)+O(kappa^-2).

This is not a full matter-relaxed ground-energy expansion. It shows why making the magnetic coefficient large gives approximate retention, not an exact spinor-sector law.

## 4. A coarse rival comparison is not a preservation proof

Complete cancellation of the source spinor holonomy costs 4 kappa, because each source face has relative phase +/-pi/2. Comparing the previous uniform flattened state with the coherent source state gives the crossing

    kappa_flat=(sqrt(3)-1+beta/120)/4.

At beta=3/5 this is approximately 0.184262701892. Above it that particular flattened rival is more expensive. The infinitesimal current-driven rival still lowers the source-state energy, so this threshold cannot be used to claim global source preservation.

## 5. Exact source-flux sector

Impose

    C A=0 modulo 2pi.

On the tetrahedral face-adjacency graph this makes the relative field connection pure gauge. The total hopping retains its sourced +i face phases, so its native kinetic spectrum and rank-two coherent return are retained up to gauge.

The constrained magnetic reaction has a concrete circulation multiplier. For a coherent source current choose

    lambda=-q C J/4.

Then C^T lambda=-q J, and in the force law -q J-C^T lambda the circulation cancels exactly. This is an exact constraint completion, not the claim that a finite cosine coefficient implements it. Its physical admission or limiting mechanism remains a constructor input.

Gauss requires a retained longitudinal electric field for charged density. Even with face flux constrained, that field can relax matter density outside the bare coherent sector. Therefore the next calculation must jointly minimize charged matter and electric energy under the exact face constraint, rather than announce that the full interacting spinor is unchanged.

## 6. Full feedback check

Reused the existing reversible splitting method with source hopping phases and the mandatory onsite term:

- electric half drift;
- magnetic half kick;
- forward/reversed matter-link half sweeps, updating signed electric flux;
- onsite phase;
- magnetic half kick;
- electric half drift.

At beta=3/5 and kappa=1, a 0.1-duration coherent-spinor test gives:

| Step | Maximum energy error | Gauss error | Reversal error |
|---|---:|---:|---:|
| 0.01 | 3.71e-8 | 1.06e-15 | 1.34e-15 |
| 0.005 | 9.27e-9 | 1.45e-15 | 1.00e-15 |

Both runs develop approximately 0.000998 relative face-flux deviation. This agrees with the exact finite-stiffness obstruction. The numerical control uses a closed four-vertex graph with fixed compensating background; it verifies local feedback, not the common exterior-vacuum mass comparison. The exterior model is not replaced by that test background.

## Verify

    python research/voevodsky/checkers/check_spinor_face_magnetic_action.py

Results: `results/spinor_face_magnetic_action.json`. Exact checks cover the actual incidence and source loop phases, signed nonlinear force, Gauss and power identities, coherent circulation norm and constraint multiplier. Numerical checks separately cover reversible complete feedback and second-order energy-error scaling. No measured mass chooses kappa or beta.
