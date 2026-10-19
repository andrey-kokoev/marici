# VF1 cycle 3 — full linked binary native inertia

The checker resumes the durable 41-row inverse frontier using its outward cumulative squared-norm bounds as exact dyadics. It verifies the final eight rows with Arb rather than replaying the prefix. Complete coverage gives a certified inverse-factor bound for all 49 rows.

It then reconstructs the binary raw H reference, checks exact Hermiticity and block-tridiagonal structure, and independently encloses H-shift I-LDL* using the **saved** L/D bytes. Thus the D-block, inverse-factor and factor-residual certificates share one durable witness; regenerated numerical factors are not silently assumed equal.

If d is the verified D separation, ell bounds ||L^-1|| and r bounds the linked factor residual, r<d/ell² proves the binary shifted H has the same inertia as D by Sylvester's law and a nonsingular Hermitian homotopy. This is a verified full-matrix native inertia subgate, not merely numerical pivot counting. The shift is the exact stored binary value with total-threshold label 10, not an unproved enclosure of the exact radical pose reference.

## Scope and attempt closure

VF1 ends **inconclusively for full H7** after three execution cycles. The binary native inertia subgate is complete; original source assembly/energy-reference errors, retained spectral-frame transfer and full-band coupled matching inverse are not certified. A native count of 130 does not alone bound the outgoing matching inverse or make the stored frame invariant.

The latest VF1 forecast 0.01 accepted / 0.02 rejected / 0.97 inconclusive is historical; the observed full-H7 outcome is inconclusive. No budget renews automatically. H6 also remains open with an exhausted attempt and a separate unspecified successor. The next nonredundant continuation is to specify and cost a source/frame or coupled-inverse bridge protocol using this binary certificate, not to replay completed inertia work.

Replay in the pinned source environment:

    python research/scattering/high-energy/check_verified_binary_inertia.py --check
