# Neutrino continuation: actual rim attachment and a spin-compatible contact

Owner: `marici.Strominger`. Operator: “let's do it.”

**Result:** a geometric boundary attachment is constructed, and the existing conditional coherent doublet is attached to actual rim edges. A nonzero normalized scalar contact with the retained electron spinor is constructed. **No physical neutrino identification or weak-decay vertex is established.**

## 1. The geometric attachment is now an explicit operator

The actual neutron source's six selected side triangles form an annulus. Their chain boundary has six edges in two triangular components, exactly matching the reserved caps. These components are computed from the boundary matrix, not injected as target ports.

A new, explicitly declared **isometric source-equivariant boundary-cycle attachment** identifies a filled candidate disk's three boundary vertices with one exposed rim, retains its cap-induced metric, maps its three center-cone cells into that cap, and chooses the outward chain orientation so the rim boundary cancels.

| Retained surface | Exact Betti numbers `(b0,b1,b2)` | Boundary |
|---|---|---|
| Original neutron side belt | `(1,1,0)` | two triangular rims |
| One disk attached | `(1,0,0)` | other triangular rim |
| Both disks attached | `(1,0,1)` | none |

Each cap has three forward cycle-equivariant identifications: **six maps total**. Reversed maps require the inverse source-cycle word and fail the unchanged forward-word contract. The original metric-eight disk still fails fixed-scale matching; the separately declared metric-three variant passes.

The three forward preparations at a cap yield the same unmarked fundamental chain but different labelled-corner/word histories. Recovery therefore retains the host/disk archives and correspondence; it is not a faithful inverse from the unmarked glued surface alone.

**Global context discriminant:** the unchanged proton surface is closed and supplies no exposed boundary component for this operator. But explicit face excision and a declared uniform3/8 metric rescaling produce a proton-derived countermodel with the same local attachment. This is a changed-source control, not an operation silently admitted on the original proton. The rule recognizes a boundary-filling situation, not a unique particle species. Closing a surface is not a neutron-to-proton reaction.

This capability is new at this contract's geometric scope; it is **not** the inherited single-pole rule and not automatically a native physical coupling.

[Contract](contracts/neutrino-rim-attachment.v1.json) · [checker](checkers/check_neutrino_rim_attachment.py) · [receipt](results/neutrino-rim-attachment-v1.json): **15 exact check groups pass**.

## 2. Why the bare disk cannot be the electron's spin partner

Ordinary geometric chain legs have central full-rotation action `+1`; the actual retained electron doublet has `-1`, checked through both its logical and raw encoders. A transition using neutron/proton geometric chain lines and an undecorated disk line therefore requires

    (-I2) T = T,

hence `T=0`. More generally, matched baryon central parities and an odd electron require an odd partner. This is a **restricted representation obstruction**, not a claim that every possible weak vertex vanishes or that physical baryons are scalar.

A spinor fiber is thus substantive missing capability, not a label inferred from three arrows.

## 3. The existing coherent fiber can be attached to actual edges

We do not manufacture a spinor from the bare disk. Instead, explicitly borrow the already constructed electron-derived coherent doublet and its retained omission mark.

For tetrahedral source normals `n_f`, omit `o` and construct

    t_f = n_f+n_o/3,
    r_f = 3 t_f/(2 sqrt(2)),  f != o.

The three `r_f` lie in the plane perpendicular to `n_o`, sum to zero, have unit radius and squared pair distances **3**. They therefore match the actual neutron cap rims. This unit normalization is a declared source construction, not physical scale calibration.

There are **24 proper metric frame charts**: four omissions, two caps, three cyclic placements. In each, projector `f` is indexed by the **actual rim edge opposite `r_f`**. The negative Pauli line's tangential polarization points along that edge's outward normal; no momentum or physical helicity is assigned.

Retain the previous coherent encoder

    V_o = stack(P_f R_o),
    R_o = P_o+(I-P_o)/sqrt(2),
    V_o^dagger V_o = I2.

These are now geometrically attached three-edge spinor-line ports, with full two-component recovery. For every chart, all six native stabilizer spin operations jointly intertwine the proper metric frame, actual neutron cycle, edge permutation and spinor encoder: **144 joint transport squares pass**.

Both lifts are retained. The central operation fixes base points/edges but negates the doublet. The spinor interface does not descend to the bare geometric C3 action by forgetting that sign.

## 4. A nonzero source-bound scalar contact

Let `K4` be the retained raw electron encoder and `E=K4/sqrt(2)` its normalized version. Construct

    Psi_o = (E tensor V_o)(|01>-|10>)/sqrt(2).

This **48-coordinate raw pair vector** has norm one, exactly recovers the logical singlet and is fixed by common native electron/edge-spinor stabilizer transport, including the central operation. It supplies a spin-compatible scalar preparation/contact map. It is **not a complete n→p+e+nu reaction**, nor a declaration of which partner is neutrino versus antineutrino.

Two controls prevent promotion:

* Dephasing the three edge flags reduces overlap with the coherent contact projector to **1/3**, not1. Classical edge records do not retain the constructed pair.
* Zero and nonzero contact strengths satisfy the same covariance. Symmetry permits this coupling but does not establish physical production or determine its rate.

[Contract](contracts/neutrino-spinor-rim-contact.v1.json) · [checker](checkers/check_neutrino_spinor_rim_contact.py) · [receipt](results/neutrino-spinor-rim-contact-v1.json): **12 exact check groups pass**.

## Remaining physical gate

The construction now supplies an actual geometric attachment, a source-bound spinor/edge identification and an allowed scalar contact. Still missing is an **independently grounded particle-selection and weak-production law**, including its baryon legs and physical charge, momentum/energy, chirality and flavor readers. Neither cap, omission nor contact strength is selected. The borrowed spinor is not derived from the arrow-first candidate. No mass, rate or neutrino identity follows.

## Verification and provenance

Both contracts/checkers were frozen before scientific execution. Passing freezes:

* `scc-freezes/neutrino-rim-attachment-v1.7bb266067a915c5a.json`
* `scc-freezes/neutrino-spinor-rim-contact-v1.08a7780e1adc7ad1.json`

The first rim challenge invocation mistakenly supplied a registered check ID where SCC expected a file path; Python failed before launching the checker. Reusing the identical freeze with the correct path passed. No mathematical acceptance or checker code changed in response. The spinor-contact challenge passed on its first invocation.

Fresh replay:

```text
python research/aspect/scc/scc.py check neutrino-rim-attachment-v1
python research/aspect/scc/scc.py check neutrino-spinor-rim-contact-v1
```

These **27 new check groups** are separate from the preceding33 follow-up groups and22 original table groups. Pure inherited constructors and stored coefficients were reused; native producer CLIs, proof-assistant sources and gallery were not run or modified. No other-owner source/shared fixture was edited, and no commit, push or deployment was performed.
