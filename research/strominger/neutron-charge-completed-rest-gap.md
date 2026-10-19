# Neutron rest energy, iteration 3: conserved charge and a conditional rest gap

## Fresh result

The dynamical bank can consistently be an internal neutron channel, but it cannot be neutral under a conserved particle label that is nonzero on the prepared neutron. With this sector completion, the existing seam-register law has a rigorously calculated vacuum-subtracted gap:

    E_gap = (21/2) [sqrt((J+epsilon)^2+4g^2)
                   -sqrt((J-epsilon)^2+4g^2)].

At the prior supplied parameters epsilon=1/4, J=1/2, kappa=1, g=0, this is **21/4** in that model's energy unit. This iteration establishes a consistent conditional rest-gap model on the new binding; it does not derive these parameters from the canonical source pulses.

## Charge extension is forced by the generated dynamics

Freshly read the 24-dimensional seam-transport receipt and replay every basis-generation witness. Let x0 be the prepared coherent neutron. Its operator-word images span the full 24-dimensional neutron/bank closure.

Suppose a conserved linear label Q obeys

    Q x0=q x0,
    [Q,T]=0

for all bound pulses, native rotation and seam/native operators. Then every word image has eigenvalue q. Since those images form a basis, **Q=q I24**. This proof assumes no diagonal or native/bank block ansatz for Q.

Thus the supplied neutron labels electric charge 0 and baryon label 1 extend to every reached bank mode. The numerical physical labels are supplied, as in the prior `charge-compatible-internal-contact.md`; the operation algebra forces their extension, not their physical interpretation.

Append the prior model's empty vacuum with both labels zero. Pulses and rotation fix it, while carrier energies and seam projectors annihilate it. There is no vacuum-to-neutron transition in this sector completion.

## Apply the existing occupation law without identifying unlike registers

The carrier sector now includes all 24 neutron/bank modes. Write C=I24 in that sector and zero on the vacuum. Each transported seam projector P_e is zero on the bank and vacuum. The satisfied-interface control is

    S_e=C-P_e.

The prior model has **21 additional neutral two-state registers** n_e, not the six active bank directions or sixteen original bank coordinates. Reuse its explicit Hamiltonian:

    H_rest=H_native+kappa sum_e P_e
           +sum_e [epsilon n_e+J(n_e-S_e)^2-g X_e].

This rest Hamiltonian is a supplied occupation law. The bound canonical pulses are retained as charge-conserving driven interactions, not inserted as an invented autonomous sum.

## Ground-state proof on the actual transported operators

For an inactive register, its ground energy is

    e_v=(epsilon+J-sqrt((J+epsilon)^2+4g^2))/2.

For a matched occupied interface,

    e_b=(epsilon+J-sqrt((J-epsilon)^2+4g^2))/2.

Let delta=e_b-e_v. For J>epsilon>0, g>=0, one has 0<delta<=epsilon. With kappa>epsilon, the exact two-level spectral calculation gives

    H_rest >= 21 e_b I + H_native +(kappa-delta) sum_e P_e.

The actual transported native operator is positive semidefinite. Its common kernel with all 21 seams has dimension seven: the coherent neutron and the six bank directions. Any vector in this kernel, tensored with the matched register ground states, saturates the lower bound. The empty vacuum register ground is 21 e_v.

Therefore the occupied-minus-vacuum gap is exactly 21 delta, with occupied ground multiplicity seven. No exponentially large matrix was truncated to obtain this result; local spectral inequalities and a verified saturating carrier space prove it.

The original coherent neutron with the appropriate register ground state is among these conditional rest ground states. A driven source pulse may excite it out of that ground space, which is compatible with its role as an interaction.

## What the source still does not select

The same source binding and conserved-charge assignment admit, at g=0:

| epsilon | J | kappa | Gap |
|---:|---:|---:|---:|
| 1/4 | 1/2 | 1 | 21/4 |
| 1/2 | 1 | 2 | 21/2 |

Both satisfy the exact ground conditions. Hence charge completion alone does not choose the charging energy. The sevenfold ground degeneracy also prevents interpreting the ground sector as a uniquely selected bare neutron configuration.

This is the existing parameter-selection gap, now made explicit in the bound system—not a new proposed mass mechanism. Physical units and a bare particle baseline are not inferred from the pulse-angle convention.

## Verification

```sh
python research/strominger/checkers/check_neutron_charge_completed_rest_gap.py
```

Eight checks passed. The prior local spectral checker was freshly invoked for g=0, 1/8 and 3/8. Exact radical energies, conserved-sector certificate, positivity checks and parameter controls:

`research/strominger/results/neutron-charge-completed-rest-gap.json`.

## Next gate

Identify epsilon, J, g and the physical energy/time normalization from the source operations, rather than choosing another legal parameter set. The conditional rest-gap calculation is complete; a source-selected neutron rest energy is not.
