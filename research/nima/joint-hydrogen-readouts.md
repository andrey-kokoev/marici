# One retained composition packet, geometric and physical readouts

## Question

Unify the weighted barycenter and hydrogen mass calculations as readouts of one retained composition structure. Test regrouping and binding inside a larger composition without conflating them. Active obligation: common-source realization and readout compatibility under supplied composition and interaction witnesses.

## Common packet

Each leaf carries a name, retained parent references, a matter-provenance weight w, an additive moment m, and four-momentum P. Binary composition retains both children and adds (w,m,P). For nonzero w the geometric representative is m/w; invariant mass is obtained from P squared after composition.

The geometric coordinates here are formal provenance coordinates of marked inputs, not their physical positions or center of mass. This makes their meaning explicit instead of silently identifying an abstract barycenter with an energy-weighted physical center.

For hydrogen formation, proton and electron each contribute one original matter occurrence. The bound atom inherits weight two and both source links. The photon contributes zero to this particular matter-occurrence count, but retains both source links and has nonzero four-momentum. Its matter barycenter is undefined, not a spurious point at zero. Keeping (w,m) rather than only m/w allows it to participate in composition without division by zero.

The zero photon weight is a declared matter-provenance convention, not its physical energy or a count of all output records. Counting all records would be a different readout.

## Two different kinds of cell

1. Regrouping changes a binary tree while retaining the same leaves and summed data. Both readouts respect it by associativity of their additive inputs.
2. Binding replaces the active proton/electron pair by atom plus photon, retaining their sources. It requires its own certificate: total four-momentum, the atom and photon mass shells, and the supplied binding relation. It is not merely a reassociation witness.

The second cell uses the previously checked hydrogen recoil construction. Primitive masses, binding and the one-photon channel remain input; no amplitude or WG interaction-selection law is inferred.

## Context compatibility

Two independent spectator fixtures supply a four-input context for regrouping. The checker compares:

    bind the proton/electron subtree, then regroup;
    regroup, then bind that same subtree.

Both reach the same terminal tree ((hydrogen,photon),(X,Y)), with the same retained source links and both readouts. The two route records themselves remain distinct. All five bracketings of the initial leaves and all five of the final leaves give the same total payload. The spectator energies are fixtures, not particle predictions. These identities instantiate ordinary associative composition in this explicit packet model; no full native categorical realization is claimed.

## Discriminating controls

Deleting the photon leaves the geometric matter readout unchanged but violates four-momentum conservation. Thus the physical complement cannot be dropped merely because it is invisible to one geometric projection.

Two bound atoms with identical matter geometry and parent references but different supplied binding values have different invariant masses. Therefore the mass readout does not factor through this geometric representative alone. Their complete physical packets differ; no contradictory identity is asserted.

## Disposition and verification

The synthesis gives a common retained carrier for both readouts and a compatible binding-in-context diagram. It does not derive energy from barycenters. The physical quantities currently form an additional typed component, while the binding witness connects their input/output values. A mass prediction would require a source rule selecting that component, not another associativity calculation.

`python research/nima/checkers/check_joint_hydrogen_readouts.py` passed via `structured_command_execution:e_32876_1791228994344414700_54`; results: `results/joint-hydrogen-readouts.json`. The test uses exact rational arithmetic and the prior rounded physical inputs. No commit or publication is claimed.
