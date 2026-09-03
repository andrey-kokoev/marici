# Certificate-fibred coherence computad

## Question

What categorical object results when verified analytic fragments and certificate-indexed partial pyramid representations are overlaid without promoting proposals into theorems?

## Claim boundary

This packet constructs a finite logical model of the overlay. It organizes generators and their domains of definition; it does not source the missing cross-sector maps or prove that every future certificate predicate is already known.

## Certificate base

Let \(D\) be the dependency DAG of certificate predicates. A certificate state is a downward-closed truth assignment: a predicate may hold only when every predecessor required by \(D\) holds. Ordered by adding true predicates, these states form a finite poset \(B_D\).

For a proposed generator \(f\), let \(R_f\) be its required predicates. Its domain of definition is the upward-closed subset

\[
U_f=\{b\in B_D:R_f\subseteq b\}.
\]

A blocked record at state \(b\) carries the minimal elements of \(R_f\setminus b\) under dependency reachability. They form an antichain. This is the intrinsic obstruction boundary of \(f\), not a linear first failure.

## Fibred computad

For every \(b\in B_D\), define a computad \(\mathcal C_b\):

- all source-typed objects certified at \(b\);
- every generator \(f\) with \(b\in U_f\);
- only those relations and coherence cells whose own certificates hold at \(b\).

If \(b\le b'\), inclusion of admitted generators defines a structure-preserving map

\[
\mathcal C_b\longrightarrow\mathcal C_{b'}.
\]

Thus the overlay is a covariant diagram of computads over \(B_D\), equivalently a certificate-indexed family with monotone realization. A proposed transfer is a partial section defined on \(U_f\). The verified Markov equipment occupies a realized subcomputad in every state containing its analytic certificates.

## Composition

For composable proposed generators \(f,g\), the composite exists over

\[
U_{g\circ f}=U_f\cap U_g\cap U_{\mathrm{interface}},
\]

where \(U_{\mathrm{interface}}\) certifies target/source compatibility. Required predicates are unioned, then minimized only for reporting current failures. Dependency edges are never invented by composition.

At a blocked state, the composite obstruction is the antichain of minimal false prerequisites of that union. This operation is associative because set union and reachability minimization are associative at the represented upward-closed domain level.

## Independent descent and completion axes

Kitaev's counterexamples exhibit four possible local states: neither certificate, descent only, completion only, and both. Therefore the base contains a square rather than a chain. A comparison cell between the two routes exists only when a typed theorem supplies it. In the metric-transition Markov fiber, our completion-descent theorem supplies an invertible identity comparison. Outside that fiber, the square remains without a cell.

This distinguishes:

- logical coexistence of two certificates;
- existence of both route composites;
- a Beck–Chevalley comparison between them;
- invertibility of that comparison.

None implies the next without a theorem.

## The R-zeta corner

The current \(R_\zeta:S_\zeta^{labels}\to U_{G4}\) proposal has two incomparable minimal blockers: source-typed target \(U_{G4}\) and source-derived map \(R_\zeta\). It therefore lies outside every fiber missing either primitive. It is not a malformed analytic arrow; it is a partial generator whose domain currently has no materially realized state.

Even after both primitives appear, preserved invariants, descent, coherence, completion, and demonstrated strength remain independent predicates unless typed results add dependency edges. No direct promotion to a physical/readout arrow follows.

## New falsifiers

The model rejects:

- replacing the base DAG by a total order;
- treating a passed checker as admission of an unrelated predicate;
- composing records by choosing one first failure;
- adding a comparison cell merely because both route objects exist;
- treating transport into the registry as realization in a fiber.

## Disposition

The overlay is best represented as a computad-valued diagram over a certificate-state poset. Verified analytic equipment is a realized subcomputad; partial pyramid representations are partial sections; minimal failure antichains are boundaries of their domains. A full cross-sector equipment would require a realized terminal certificate state plus sourced coherence cells, not merely a complete list of proposed generators.

## Verification

- `research/voevodsky/checkers/check_certificate_fibred_coherence_computad.py`
- `research/voevodsky/results/certificate_fibred_coherence_computad.json`
