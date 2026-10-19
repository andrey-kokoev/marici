# A full-five framed joint-field candidate

## Five coefficients retained through NE

The active N triple is coupled to the three existing sector-local modes. The
context patches are now selected by the reader's shared edge: the unique
centroid-edge patch incident to uv on each incoming/outgoing face. Their
orthogonal modes are replicated coherently across all three sectors, so the
outside coefficients remain invariant under the active C3 cycle. This gives
a norm-preserving 36-by-5 binding, exact C3 equivariance and a reducing subspace
for all three native N projectors. The face-to-context assignment and inherited
phase conventions remain explicit choices.

Apply the previously checked N/E contrast exchange on their 44-channel direct
sum. Two active contrast combinations move into E's native return doublet.
The common active combination and both contexts remain in the baryon field.
Thus the output has rank two in E and rank three in the retained N block, and
all five input coefficients remain recoverable with their exact norm.

The joint output binding includes the actual native NE permutation. Its E
block independently matches the earlier contrast/reflection construction;
it is not a new unrelated electron subspace. The three retained coefficients
are part of the joint reference, not falsely assigned to E's two-dimensional
return image.

## PN binding

Pulling the N binding back through the constructed global metric-unitary PN
map, with the native PN permutation, gives an isometric P binding satisfying

```
S_PN B_P = B_N Pi_PN.
```

This is an algebraic construction from the chosen PN map. It is not an
independent derivation of the P coupling from the tetrahedron alone. In
particular it does not silently reinstate the earlier fixed A4-equivariant
four-vertex/context hypothesis that encountered the holonomy obstruction.

## Checked native path comparison

Used the two contact-witnessed open native paths reaching the same P window
at origin 3 with an order-five relative coefficient permutation. The candidate
uses the constructed PN map/inverse, geometric P reader action, and the
ordered-corner co-moving N reader convention.

For each edge propagate the binding by

```
B_next = U_edge B_current Pi_edge^-1.
```

Every intermediate binding is isometric. Both paths produce the same physical
root-field map in this candidate, but their endpoint coefficient frames and
bindings differ. The equality `B_path F_path=U_path B_initial` holds exactly.
This retains the native coefficient comparison without creating a second
physical mode merely from a different frame.

The propagation equation is a stated construction rule, not an independent
source selection of every binding. Only this path pair is certified here;
simultaneous assemblies, NN orientation choices and E paths remain separate
tests. The subsequent `geometric-context-and-extended-coherence-v1.md` records
a bounded depth-28 native graph test of this candidate's field-frame parity.

## Explicit defect accounting

The raw source contrast has defect eigenvalue one; E's return has zero. The
native defect alone is therefore not conserved by the exchange. Adding the
explicit electron-return occupation term gives

```
Q = H_N direct-sum (H_E + N_E).
```

Q commutes exactly with the joint exchange. This is an algebraic, dimensionless
accounting rule; the additional term's physical meaning and energy units are
not supplied. It must not be presented as a derived conservation law for the
original defect operator or as measured particle energy.

## Disposition

There is now a consistent candidate connecting all five native coefficients
to a joint field, preserving their norm, accommodating PN/NE permutations,
and retaining the checked path-dependent frame. The model still contains
explicit choices: window-to-sector coupling, context modes, the global PN
completion, and the extra accounting term. Their physical/source selection
and global coherence have not been derived.

```sh
python research/strominger/checkers/check_full_five_channel_candidate.py
```

Evidence: `results/full-five-channel-candidate/verification.json`.
Production/viewer unchanged.
