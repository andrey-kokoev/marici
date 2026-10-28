# Opposite local orientation defeats selection from seam compatibility alone

Date: 2026-10-22. Owner: `marici.Strominger`. Result: exact counterprotocol, not rejection of the intended-source selection conjecture.

## Problem and frozen alternatives

Attack the [persistent-seam P/E conjecture](persistent-seam-pe-conjecture.md) without fitted corrections or new local operators. The conjecture selects identical local C or S on the two marked triangles. Its named serial rival breaks synchronization. A stronger rival would preserve gluing, both local circulations and transported reference exchange while violating the proposed opposite-triple law.

SCC obligation: route/coherence compatibility on the retained five-coordinate cochain, with fixed R1/R2 port labels. The local-operation menu is the powers of the documented short half-phase S, with C=S^2 and S^6=I. These are operator compositions, not a physical-time law or an assertion that retained execution records are identified.

## Counterprotocol

Let

\[
P(a,b,c)=(a,c,b),\qquad hP=h.
\]

Direct exact calculation gives

\[
PCP=C^{-1}=C^2,\qquad PSP=S^{-1}=S^5.
\]

The [source primitive](../nima/triangle-half-phase-primitive.md) explicitly notes that reversing cyclic orientation conjugates its short root to its transpose. No new correction matrix is introduced; the choice to give the two legs opposite local orientation is the rival protocol, not an asserted source selection.

Apply T to the first triangle and T inverse to the second, for T=C or S. Define

\[
K_-(a,b,c)=(a,b,c,-c,-b).
\]

Then

\[
R_1K_-=I,\qquad R_2K_-=-P,\qquad
T^{-n}R_2K_-=-PT^n.
\]

Because hP=h, both shared-edge proposals agree for every composition index. For C the first two seam equations are b+e=0 and c+d=0, proving maximality of this three-dimensional carrier. For S, its squared applications imply the same constraints; the displayed intertwining proves sufficiency.

This is different from the original K carrier, which requires d=-b and e=-c. Their intersection has dimension two (b=c).

## Same-input discrimination

The input x=(1,0,0,0,0) belongs to both carriers. One joint cyclic application gives

\[
F_+(x)=(0,0,1,0,-1),\qquad
F_-(x)=(0,0,1,-1,0).
\]

Both outputs are glued, with local circulations L=1 and R=-1. The second output violates the original K constraints: b+d=-1 and c+e=1.

The counterprotocol preserves the paired-occurrence metric as well: with M=diag(2,1,1,1,1), K_-^T M K_-=2I. Neither total balance nor that budget distinguishes it from the original synchronized protocol.

## Reference exchange and chart scope

For the already specified J,

\[
JK_-=K_-(-P),\qquad JF_TJ=F_{T^{-1}}\quad\text{on }K_-(\mathbb R^3).
\]

Thus reference exchange preserves the carrier and exchanges the two oriented schedules. On a marked pair (x,m), transport m along with J and use the exchanged schedule, just as for the serial rival. This is covariance, not commutation of J with one fixed forward operation. A source requirement of fixed-forward commutation would exclude this rival, but must be supplied rather than inferred from the existence of reference exchange.

Swapping the right coefficient slots transforms the carrier equations into the original form, but also changes the documented AD/DB port assignment and right operator. The comparison here holds R1/R2 and port labels fixed; no absolute inequivalence under every possible chart change is claimed.

## Bounded census and checks

For each of the 36 pairs (S^p,S^q), p,q in {0,...,5}, compute the global seam rows hS^(pn)R1+hS^(qn)R2 for n=0,...,5. Six rows exhaust all composition indices since both operators have period dividing six. The compatible dimensions, rows p and columns q, are

```text
5 3 3 4 3 3
3 3 1 2 1 3
3 1 3 2 3 1
4 2 2 4 2 2
3 1 3 2 3 1
3 3 1 2 1 3
```

Nondegenerate same-orientation and inverse-orientation pairs both retain dimension three. Unequal frequency example (S,S^2) leaves only the common fixed line. This census covers the declared six-phase power menu, not every possible source operation.

Run `python research/strominger/checkers/check_persistent_seam_pe_falsification.py`. All 32 exact checks passed. [Receipt](results/persistent-seam-pe-falsification.json) retains matrices, common-input outputs, the census and source hashes.

## Subsequent attack on this rival

The [native-source audit](counteroriented-rival-source-audit.md) rejects this rival as an unchanged elementary forward C/S process: the inverse half-phase squares to C inverse, not C, and forward native-clock compilation cannot preserve gluing at every prefix on its full carrier. The endpoint algebra above survives. Its realization requires an additional atomic-inverse, orientation or intermediate-state policy; existing positive-power identities alone do not supply that admission. Sixteen exact checks pass. Net revision 3 retains this obstruction separately from the mathematical rival.

## Disposition

- **Refuted:** persistent gluing, circulation balance, paired-occurrence budget and covariance under transported reference exchange select the same-orientation K protocol uniquely within the declared local-power menu.
- **Unchanged:** the observability theorem conditional on applying the same fixed local T to both triangles.
- **Open:** the conjecture that the intended P/E source specifically selects that same-orientation protocol. The audit has not independently established which relative leg orientation or schedule the intended source admits.

The missing selection is sharper: distinguish common local orientation from opposite local orientation, not merely simultaneous gluing from serial rewriting. No particle identity, isotope count or physical interpretation follows from either construction.
