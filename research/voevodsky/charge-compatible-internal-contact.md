# Charge-compatible internal-channel dressing: the common offset cancels

## Result

We completed the preceding common-contact model so that its exchange does not turn a neutral reference excitation into a charged proton. Each reference channel is now an **internal excited channel of the same particle**, carrying the same declared charge and baryon label.

With one shared internal gap and coupling, the source-derived response ordering still places the belt above the proton. Moreover, the splitting is independent of the common bare particle energy. This separates the relative-energy question from one previously unresolved absolute offset.

This is a consistent candidate Hamiltonian, not a derivation of the physical internal channel or its parameters.

## 1. Prior work and what is new

Nima's `mass-primitive-quotient-charge.md` already constructs a conditional common charge assignment and explains why charge conservation alone does not protect particle identity. `mass-local-sector-protection.md` supplies a separate conditional locality mechanism, while `mass-gap-symmetry-and-protected-kernel.md` establishes that internal symmetries do not fix energy offsets. Those results are not reconstructed here.

The previous source-emission and common-contact analyses distinguish empty vacuum from excitation exchange. We now change the **type of the auxiliary channel**: it is an internal channel with the same particle labels, rather than a shared free neutral excitation. This gives an explicit charge-compatible completion of the existing response comparison.

## 2. Hilbert space and declared labels

Use the direct sum of an empty vacuum and two particle sectors. Each sector contains its retained 36-dimensional carrier and one auxiliary internal state. The full finite space has dimension 75.

Assign

| Sector | Q | B |
|---|---:|---:|
| Empty vacuum | 0 | 0 |
| Proton carrier and its internal auxiliary | 1 | 1 |
| Belt carrier and its internal auxiliary | 0 | 1 |

These are supplied physical labels, not extracted from the triangle geometry. No cross-species or vacuum-to-particle transition is included. The internal exchange preserves both Q and B. A neutral interaction can connect states with these identical labels without requiring a charge-changing reservoir.

This does not construct a microscopic mediator, derive baryon conservation, or establish the proposed particle identifications. It removes the charge mismatch of the trial interaction itself.

## 3. Shared internal-channel Hamiltonian

For each species s use its actual carrier operator K_s and normalized local contact w_s from the preceding comparison:

    H_s = mu I + [[Delta, g<w_s|],
                  [g|w_s>, K_s]].

The bare offset mu, internal gap Delta>0 and exchange strength g are shared. The auxiliary energy is mu+Delta: changing the common particle baseline moves its internal auxiliary with it.

The source fixes each contact response

    R_s(x)=<w_s,(K_s+xI)^(-1)w_s>, x>0.

The carrier-connected lowest energy has the form

    E_s=mu-x_s,
    Delta+x_s=g^2 R_s(x_s).

For nonzero g this equation has exactly one positive solution: its left side increases while its right side decreases from infinity to zero.

The already certified source inequality R_proton(x)>R_belt(x) implies

    x_proton>x_belt,
    E_belt-E_proton=x_proton-x_belt>0.

The common offset mu cancels exactly. Choosing mu>x_proton keeps both particle sectors above the empty vacuum. This is stability of the declared finite model, not a relativistic mass-shell calculation.

## 4. An exact shared-offset control

For the illustrative shared values Delta=g=1/2, the shifts are approximately

    x_proton=0.096763542666,
    x_belt=0.054249113064.

The checker varies only the common baseline:

| mu | Proton energy | Belt energy | Difference |
|---|---:|---:|---:|
| 1/4 | 0.153236457334 | 0.195750886936 | 0.042514429602 |
| 1/2 | 0.403236457334 | 0.445750886936 | 0.042514429602 |
| 1 | 0.903236457334 | 0.945750886936 | 0.042514429602 |

All three have a stable empty reference. Weighted Hermiticity and commutation with Q and B are checked exactly in the response-accessible subspaces. The omitted carrier modes are uncoupled nonnegative-energy spectators; their original carriers are retained.

The values are not mass fits. At finite coupling the states remain dressed rather than equal to their bare coherent returns.

## 5. Source-controlled dependence, not just a sign

At weak coupling, with Delta fixed,

    E_belt-E_proton
      = (2099/26910) g^2/Delta + O(g^4).

The coefficient is the difference of the actual coherent-contact weights, not a seam count.

At large |g| with Delta fixed, the splitting tends to

    2099/6584

in the common energy unit. This follows from the difference of the contacts' first energy moments. Maintaining the empty vacuum in that limit requires increasing the common mu. This limiting value is not asserted to be a bound at all couplings or a physical mass.

## 6. What remains to identify

The relative splitting no longer needs a separately selected proton and belt bare offset within this shared-law model. What remains is the physical origin of the **common internal channel, Delta, g and energy unit**, together with their electron/reference relation.

Equal bare offsets and shared internal parameters are declared construction rules; charge conservation does not force them. Additional charge-dependent interactions could change the comparison and must be derived rather than fitted away.

We therefore have a charge-compatible mechanism for a positive relative energy under common inputs, but not yet the observed neutron–proton mass difference or the neutron's relative atomic mass.

## Verification

    python research/voevodsky/checkers/check_charge_compatible_contact.py

Results: `research/voevodsky/results/charge_compatible_contact.json`.

Exact checks cover weighted Hermiticity, charge and baryon commutators, rational shift brackets, vacuum stability and cancellation of the common offset. The general ordering reuses the exact response certificate from `common_contact_dressing.json`. No measured mass is used.
