# Cross-lead selection is gauge-compatible but not the existing endpoint dynamics

**Third batch, iteration 10 of 10.**

**Strength:** exact operator-class obstruction, retained integer-basis tests, and a conditional symmetry selector. Not a physical control implementation.

[Previous ground doublets](FLUX-GROUND-DOUBLETS.md) · [Checker](check_cross_lead_selection.py) · [Receipt](results/cross-lead-selection.v1.json)

## 1. Fresh owner comparison

The owning [endpoint constructor](../../voevodsky/spinor-endpoint-constructor.md) and its checker specify

    G_i=n_i+ell_i+N_i,
    T_ji=|j><i| R_i R_j*,
    H=sum K_ji T_ji+(beta/8)||n||²+(beta/2)||ell||²+eta/2.

R acts on endpoint momentum, not lead momentum. Every assisted matter hop and every charging term leaves each ell_i unchanged. Finite sums, products and adjoints of these generators do so too; functions of the resulting block-diagonal Hamiltonian retain that property.

The dressed-ground projector P_plus has nonzero entries between different lead labels. It therefore lies outside this existing operator class. Unitary time evolution under the specified Hamiltonian cannot supply it by waiting. This is a scoped obstruction for the declared dynamics, not for every gauge-compatible device or control.

## 2. Gauss permits flux transfer, but a simple shift leaks

Introduce a separate bilateral shift with

    Delta ell=e_a-e_b,
    Delta n=-Delta ell,
    matter unchanged.

This preserves every G_i and both total momenta. It is an allowed kinematic operator on the rotor lattice, but absent from the owning Hamiltonian.

For the ground lead i to lead j transfer, matter remains g_i rather than becoming g_j. Its squared overlap with the destination ground is

    |<g_j,g_i>|²/(r²+1)²=4/[3(v²+4)].

At v=3/20 the retained ground weight is 1600/4827 and the excited weight is 3227/4827. Neutrality alone does not protect the dressed ground. The checker tests neutral shifts and parent hops on all eighty sum-minus-one fluxes in [-2,2]^4; shifted outputs need not remain inside that fixture window. This is not a truncated rotor implementation.

## 3. Joint native symmetry does preserve the ground

The already checked monomial native T with permutation pi extends to

    |k;n;ell> -> t_k |pi(k);pi(n);pi(ell)>.

Endpoint and lead momentum norms are unchanged, and source K covariance preserves the assisted hopping term. The map permutes Gauss generators, hence preserves their common zero kernel. It need not commute individually with every G_i away from that physical kernel.

All 576 group compositions remain exact. The full rotor-lattice extension is unitary and its ground restriction is the previously computed T. This is a real symmetry construction, not an existing flux-changing Hamiltonian term or an implementation protocol.

## 4. Conditional coherent selector, with the added input explicit

Finite-group character theory supplies the bounded central projector

    P_full=(2/24) sum_g conjugate(chi_plus(g)) U_joint(g).

The checker verifies its restriction to the dressed ground equals P_plus. The extension to the full rotor representation is a projector by the finite-group central-idempotent theorem. It preserves the physical Gauss kernel and commutes with the original Hamiltonian.

An explicitly **new** bounded positive interaction

    H_new=H+delta*(I-P_full), delta>0

would leave the plus ground doublet at its original energy and raise the minus doublet by delta. A delta=1/7 exact ground witness is included. The nonselected sector still exists; it is not erased. This addition makes no claim of preparing a state or dissipatively relaxing it.

Unlike the original dynamics, this interaction does not conserve every fixed lead momentum. It retains total charge but requires joint matter/field controls. The group sum is an existence formula, not a circuit, microscopic local coupling or physical apparatus. Its coefficients are not controller probabilities.

## 5. Continuation remains executable

The next nonredundant test is to factor these joint symmetry maps into retained matter/endpoint/lead controls, or compare them with an existing source control library. That should specify the flux-changing work/control assumptions, field-history records and nonselected output. Mathematical group covariance must not become an implicit physical selector.

This completes the third ten-turn batch, not the scientific root. Root outcome remains null. Shared sources, receipts, atlas and formal contracts are unchanged; no physical spin selection, charge conjugation, annihilation or photon output is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_cross_lead_selection.py
python research/scattering/seed-composition/check_cross_lead_selection.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The local checker recomputes the preceding exact algebra and native adapter/actions. It does not run the receipt-writing owner checker or repair historical receipts. The finite-group extension and operator-class closure are stated mathematical arguments, not new formal proof-assistant admissions.
