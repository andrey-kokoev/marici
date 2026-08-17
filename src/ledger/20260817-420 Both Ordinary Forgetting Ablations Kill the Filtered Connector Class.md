---
id: 420
date: 2026-08-17
title: Both Ordinary Forgetting Ablations Kill the Filtered Connector Class
---

# Both Ordinary Forgetting Ablations Kill the Filtered Connector Class

Entry 419 constructed the assembled connector in the finite filtered PC/Čech
model. Its ordinary shadow must now satisfy Entry 133's mandatory negative
controls. The correct requirement is not recovery of a nonzero ordinary
carrier class. The class must become nullhomotopic when either its
support/\(Q\) framing or its Tate--Cartier filtration is forgotten.

Both ablations pass.

## Forgetting support and the based \(Q\)-leg

The carrier factor of the Gysin-collapsed source is the exact Tate window.
Entry 417 gives the integral contraction
\[
h_{\rm Tate}(z)=r_0,\quad
h_{\rm Tate}(r_1)=-t_0,\quad
h_{\rm Tate}(r_2)=-t_0-t_1,\quad
h_{\rm Tate}(t_2)=o,
\]
with all other values zero, and
\[
d h_{\rm Tate}+h_{\rm Tate}d=\operatorname{id}.
\]
For any ordinary chain map \(f\) obtained by forgetting the support and
based-\(Q\) restrictions,
\[
f=d(fh_{\rm Tate})+(fh_{\rm Tate})d.
\]
Thus its ordinary chain-homotopy class is zero. The homotopy is inadmissible
before forgetting because it moves the generic \(Q\)-roof backward through
the support filtration.

## Forgetting the Tate/Cartier window

On the external Cartier packet, exterior multiplication by the first
positive normal gives
\[
B h_{\rm Cart}+h_{\rm Cart}B=\operatorname{id}.
\]
Consequently the operator-valued class also becomes nullhomotopic when the
Tate--Cartier framing is discarded. This homotopy is inadmissible in the
filtered category because it changes Cartier level and erases the fixed
closed residue.

The checker verifies both identities on all 64 filtered generators.

## Interpretation

Before forgetting, the independently fixed boundary values remain
\[
\operatorname{gr}_Q=+1,\qquad
\operatorname{Res}_{x_D}=+1,\qquad
\det(M_{\rm endpoint})=-1.
\]
After either ablation, the class is zero. Hence the connector has exactly
the behavior demanded by Entry 133:
\[
\boxed{\text{nonzero as a framed secondary class, zero in the ordinary
derived category}.}
\]

This corrects the provisional next-test wording in Entry 419: the
ordinary-forgetting cone should contract, not reproduce a nonzero ordinary
connector.

The remaining question is now categorical rather than coefficientwise.
The finite filtered PC/Čech construction supplies an explicit admissible
model, but it must still be compared with the raw normalization-sheet
six-functor geometry. The decisive test is whether the geometric
realization functor sends its marked log-blowup kernel to this framed class
without admitting either forbidden contraction.

The executable audit is
\`research/voevodsky/check_filtered_connector_forgetting_ablations.py\`.
