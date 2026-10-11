# Iteration 2: the local mixer needs relative orientation, which an edge can supply

## Fresh source boundary

Iteration 1 selected R(X)=tr(X)I-X^T among common-frame-natural algebra automorphisms with the hidden-port property. This iteration freshly read that result and tested the actual two-edge port, whose factors have different endpoint roles.

Write the bank as V tensor U, with U:0->1 and V:1->2. An independent orthogonal middle-frame change acts by

    Gamma_Q(V tensor U)=(V Q^T) tensor (Q U).

Sewing is invariant: C Gamma_Q=C. The question is whether any invertible bank mixer can both be natural under these changes and expose the requested hidden port.

## General obstruction, beyond one-factor mixers

For the four exact frame changes Q=I,e1,e2,J, the checker establishes

    average(Gamma_Q)=P=C^T C.

P is the rank-four readable projector. If a linear bank map K commutes with those frame changes, it commutes with P. Then

    K C^T = P K C^T = C^T (C K C^T).

Consequently C K C^T=0 would imply K C^T=0, contradicting invertibility. This excludes ALL invertible sixteen-dimensional linear mixers under that unframed local policy, not just the one-factor class tested previously. The finite averaging identity plus this written algebraic argument establishes the general claim; it is not inferred from trying a few candidate mixers.

The policy is explicit. Independent local O(2) changes are not already a theorem about every physical interpretation of the Boolean seed.

## Identify the missing reference rather than guess it

The determinant-weighted average gives another rank-four projector:

    P_det = average(det(Q) Gamma_Q) = L P L^T.

The remaining projector has rank eight. Thus the selected hidden port is specifically the determinant-character sector, rather than an unnamed memory channel.

The selected L transforms by a sign:

    Gamma_Q L Gamma_Q^-1=det(Q) L.

With all three endpoint frames independent, the sign becomes det(Q2)det(Q1). Therefore the required reference is a RELATIVE orientation between endpoints 1 and 2. A retained sign o12 transforming by this character makes L_o=o12 L a covariant family. An unpointed metric alone cannot supply that sign, because a reflection fixes the metric but reverses the sign.

Exact checks cover all 64 combinations of the four endpoint-frame transformations. They are consistent with the general two-dimensional identity Q J Q^T=det(Q)J.

## A source edge supplies relative orientation, with a decisive consequence

For the existing invertible orthogonal edge action V, take

    o12=det(V).

This is calculated from a retained edge, not selected by adding a desired response sign. It has precisely the required frame transformation law. No absolute physical orientation has been chosen.

However, in two dimensions an orthogonal V satisfies

    Ad_J(V)=det(V) V.

Hence the self-attached mixer obeys

    o12 Ad_J(V)=V,
    L_o(V tensor U)=V tensor U.

On this source class the hidden readout equals the ordinary readout. In particular the prior ordinary/twisted sign distinction disappears under this covariant self-attachment. The paths, references and higher witnesses need not be erased; they are simply not distinguished by this particular observed port.

This is the general orthogonal-edge version of the preceding flat-reference controls, with the required reference type now derived from the bank representation. It does not show that every richer state or independent reference is trivial.

## Selection status

- **Common-frame mixer:** conditionally selected by iteration 1's explicit policy.
- **Independent endpoint frames:** a fixed unframed hidden mixer is impossible under the tested covariance requirement. A retained edge supplies the needed relative orientation and makes the family covariant.
- **Signal:** that self-attached readout carries no extra information on the orthogonal two-edge source used so far.
- **Evolution:** after exchange the general bank need not factor as V tensor U; its source attachment must remain retained rather than reconstructing an arbitrary V from the bank.
- **Physical frame and gravity:** no absolute frame, metric origin, matter coupling or gravitational normalization is selected here.

The zero-discrepancy outcome must not be repaired by silently freezing the orientation while declaring local frame covariance. An independent physical reference or a richer source interpretation would need its own preparation/admission evidence.

## Next executable continuation

Audit gravitational normalization directly against the current selected algebraic structure. Check whether its admissible changes of amplitude, budget/action calibration and clock leave the witnessed dynamics unchanged, and inspect any prior source law alleged to remove that freedom. This is still a nonredundant executable test; the present result is not a reason to stop before checking the normalization claim.

## Verification

`python research/nima/checkers/check_local_frame_mixer_obstruction.py` passed with exact rational frame actions, projectors, rank certificates, covariance and self-orientation controls. Results: `results/local-frame-mixer-obstruction.json` with source digests.

No prior dynamics implementation was modified. No new Agda theorem, physical gauge admission, ledger entry, commit or publication is claimed.
