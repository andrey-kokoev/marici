# Alexandrov domains and the Grothendieck overlay

## Question

What additional structure does the certificate-fibred computad acquire when its partial domains and certificate-strengthening maps are treated categorically?

## Claim boundary

This packet analyzes the finite certificate model. It does not assert that certificate strengthening creates scientific evidence or that local proposals glue without separately checked agreement cells.

## Alexandrov topology of realization domains

The certificate-state poset \(B_D\) carries its upper Alexandrov topology: an open set is upward closed under addition of certificates. Every partial generator \(f\) has an open realization domain

\[
U_f=\{b:R_f\subseteq b\}.
\]

Composition is defined on intersection:

\[
U_{g\circ f}=U_f\cap U_g\cap U_{\mathrm{interface}}.
\]

Products of composable partial representations therefore correspond to finite meets in the lattice of opens. Alternative constructors available on either domain correspond to unions, but union does not identify their values on overlap.

The complement of \(U_f\) is a downward-closed failure region. At a state \(b\), the minimal failed-prerequisite antichain is a local boundary presentation: it generates the upward closure of repairs needed to enter \(U_f\). Different antichains can describe different boundary components without selecting a first failure.

## Grothendieck construction

Let \(F:B_D\to\mathbf{Computad}\) send \(b\) to the computad \(\mathcal C_b\) and certificate strengthening \(b\le b'\) to inclusion. Its Grothendieck construction \(\int F\) has:

- objects \((b,x)\) with \(x\in\mathcal C_b\);
- vertical realization arrows induced by fiber generators at fixed \(b\);
- base-change arrows \((b,x)\to(b',x)\) for \(b\le b'\);
- mixed composites only when source, target, and interface types survive reindexing.

Base-change arrows record availability under stronger certificates. They are not transfer maps between scientific sectors and do not grant authority. There is generally no arrow from \(b'\) back to \(b\): forgetting a certificate can make a generator undefined.

## Local gluing obstruction

Suppose two proposed constructions define sections on opens \(U\) and \(V\). They glue over \(U\cup V\) only if their restrictions to \(U\cap V\) agree through a typed comparison cell satisfying its coherence laws. Equal source and target labels are insufficient.

This yields a new interpretation of the pyramid's comparison cells: they are descent data for gluing locally realized representations. The absence of a comparison cell is a genuine gluing obstruction, even when both local arrows exist.

Kitaev's independent descent and completion branches instantiate this exactly. The descent-only and completion-only opens overlap where both certificates hold, but no comparison between route composites follows from the overlap. Our metric-transition theorem supplies that comparison only in the Markov subcomputad.

## R-zeta stalks

For the current materialized certificate state, the stalk of the \(R_\zeta\) partial generator is empty because both primitive blockers remain false. Adding only source-typed \(U_{G4}\) or only a source-derived map reaches a boundary-adjacent state but not the realization open. Both are required before subsequent invariant and coherence predicates can even test gluing with adjacent pyramid faces.

## Consequences

1. A registry entry is an open-domain specification, not a global arrow.
2. Certificate strengthening is monotone availability, not evidential promotion.
3. Comparison cells are gluing data, not decorative commutativities.
4. Minimal failure antichains are boundary coordinates for repair.
5. A full equipment is a global section with all companion, conjoint, interchange, and Beck–Chevalley gluing conditions, not merely a nonempty terminal fiber.

## Disposition

The overlap forms a Grothendieck construction of computads over an Alexandrov certificate space. This refines the previous fibred model by separating base change, scientific transfer, and gluing cells. The next obstruction is no longer missing generators alone: it is whether locally realized sector representations admit coherent gluing on overlaps.

## Verification

- `research/voevodsky/checkers/check_alexandrov_grothendieck_overlay.py`
- `research/voevodsky/results/alexandrov_grothendieck_overlay.json`
