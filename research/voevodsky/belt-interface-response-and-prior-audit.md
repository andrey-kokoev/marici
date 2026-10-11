# Actual belt-interface response, after auditing prior mass mechanisms

## Prior research checked before construction

The following existing results determine what should be reused rather than rebuilt:

| Prior source in `research/nima/` | Existing result and consequence here |
|---|---|
| `mass-gauss-law-collective-excitation.md` | Compact rotor factors and an exact Gauss law already construct a collective integer excitation. Do not present a new rotor count as source-derived carrier energy. |
| `mass-rotor-action-and-external-charge.md` | Phase locking and charge locking give different inertias and external charges. An action, its charge normalization and its energy must be reduced together. |
| `mass-gap-symmetry-and-protected-kernel.md` | Internal symmetries permit sector-energy offsets; counting-charge positive squares do not by themselves protect the required kernel. Repeating this ambiguity is not a new mechanism. |
| `mass-local-sector-protection.md` | Exact constraints plus microscopic locality can protect transitions, but not the numerical energy gap. Do not confuse persistence with energy normalization. |
| `mass-history-retaining-locking-interaction.md` | Reversible preparation with retained difference records and explicit reservoirs already exists. Preparation work is not a new derivation of rest energy. |
| `interface-required-record.md` | A source response can determine the minimal additional observer record, while the rest of the state remains retained. Reuse its closure test rather than invent independent resource bits. |
| `collective-mechanics-prior-clues.md` | Kinetic/metric data and subsequent responses must descend together. A conserved norm or an excitation eigenvalue is not automatically mechanical mass. |
| `endpoint-loading-is-the-excess-over-the-harmonic-history-extension.md` | Harmonic extension and residual energy require the actual energy pairing and incidence. Its theta-specific conclusions cannot simply be transferred to the belt. |

The charged-core dressing model and our recent seam occupation, failed mass comparison, and collective spectrum are also retained dependencies. Their constructions and exclusions are not new claims in this note.

**New bounded task:** apply the existing response/closure method to the actual shared-edge bridge in the newly derived belt Hamiltonian. This computes source data a later vacuum/field coupling would need, without yet declaring that coupling or choosing its energy scale.

## 1. The physical-source address used

In one paired sector, the six triangle amplitudes have weights

    n=(2386,4198,2386,2386,4198,2386)/675.

The bridge joining the two faces is the actual seam between triangles 0 and 3. Its measured amplitude difference is a_0-a_3. The energy and response use the inherited metric diag(n), not an unweighted replacement.

The face-odd sector consists of states (x,-x). Its three-dimensional operator is

    K_odd = [[7037/3292, -2099/3292, -1/2],
             [-1193/3292, 1193/1646, -1193/3292],
             [-1/2, -2099/3292, 3745/3292]].

This is the exact invariant restriction previously obtained from the full carrier. No new degrees of freedom have been introduced. One may use the one-sector metric above, or the isometric globally aligned embedding with a factor 1/sqrt(3) across the three sectors.

## 2. The boundary scalar does not close its own dynamics

Two allowed odd-sector states,

    x=(0,0,0), y=(0,1,0),

have the same observed bridge coordinate x_0=y_0=0, but different next Hamiltonian responses:

    (K_odd y)_0-(K_odd x)_0 = -2099/3292.

The Schrödinger time derivative adds the common factor -i E*/hbar. Thus replacing the interface by one autonomous scalar loses an actual response distinction.

The exact controllability and observability matrices each have rank three. The minimal linear realization of this particular input/output response therefore needs three state coordinates: the boundary scalar and two additional retained collective coordinates. These are already present in the carrier. They are not three independent tensor factors, nor three newly created physical records.

This is the new source-specific result obtained by reusing Nima's interface-record method.

## 3. Exact frequency-dependent response

Let w be the unit mismatch vector for the normalized bridge projector. For spectral parameter z in the common energy units, define

    S(z)=<w,(K-zI)^(-1)w>.

Only the face-odd sector contributes. Equivalently,

    S(z)=[(K_odd-zI)^(-1)]_00.

The ground-state singularity of the full K is absent from this response because w is orthogonal to the coherent mode. At z=0 use the odd-sector inverse, or the regular continuation of this matrix element.

The exact rational function is

    S(z) = [-z^2 + (6131/3292)z - 6431463/10837264]
           /[z^3 - 4z^2 + (44361887/10837264)z
                     - 6431463/10837264].

All three face-odd modes are observable through this bridge. In particular,

    S(0)=1,
    S'(0)=4485/1193.

The poles are the three previously derived odd excitation energies. The derivative is a response coefficient in this first-order spectral problem, not a mechanical inertia or rest mass by definition.

## 4. Static boundary energy

For stiffness M K, M=diag(n), retain endpoints 0 and 3 and minimize over the other four amplitudes. The exact Schur complement is

    (1193/675) [[1,-1],[-1,1]].

Thus the minimum energy at prescribed endpoint amplitudes is

    (1193/675) |a_0-a_3|^2

in the declared amplitude and energy normalization. Each face's internal amplitudes relax to its boundary amplitude. Equal boundary values have zero minimum constraint energy.

This is a derived boundary stiffness, not an assumed capacitance. Turning it into a charging action or physical vacuum contribution still requires the kinetic, charge and coupling data identified in the prior rotor-action audit.

## 5. What this supplies to a vacuum/field construction

If a further model supplies a neutral reference level epsilon and coupling g to this normalized bridge mode, its exact scalar Schur denominator would be

    epsilon-z-g^2 S(z).

The source now fixes S(z), including its poles and response memory. It does not fix epsilon, g, the charge/type of the external field, or whether that level represents a vacuum excitation. An electron cannot be coupled into a neutral sector merely by renaming this probe.

There is also a precise restriction: the coherent belt state is dark to this mismatch port. Its overlap with w is zero, so a coupling solely through w leaves its eigenvalue unchanged. A proposed vacuum self-energy could still alter the relative reference energy, but that would require a separately specified common vacuum Hamiltonian and its ground-state calculation. Darkness alone is not a no-go theorem for relative energy shifts.

Accordingly, this response calculation does not generate a neutron rest mass. It replaces an unspecified interface with an explicit, source-derived three-mode response that any such calculation must retain. It also shows why merely charging each successful seam independently was not a consequence of the carrier dynamics.

## Next gate

Inspect source-supported couplings to the **coherent occupied mode**, or a common vacuum interaction whose ground-state change can be computed without adjustable sector offsets. The new response above is available for the mismatch channel; it must not be mistaken for such an occupation-sensitive coupling. Prior charged-core dressing supplies one conditional example, already tested, not a new derivation to repeat.

## Verification

    python research/voevodsky/checkers/check_belt_interface_response.py

Output: `research/voevodsky/results/belt_interface_response.json`.

Exact rational checks cover the resolvent, static Schur complement, both minimal-realization ranks, and the scalar-closure counterexample. No fitted mass, added independent register, new vacuum law or physical electron identification is used.
