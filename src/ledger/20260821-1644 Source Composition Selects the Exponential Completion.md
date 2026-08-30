# 1644 — Source Composition Selects the Exponential Completion

## Frontier

Entry 1643 proves that the second-order Cut jet alone has inequivalent exact CP completions.  Add one predeclared source datum: continuous one-parameter composition with fixed infinitesimal generator.

## Composition theorem

Let

\[
U(0)=I,
\qquad
U(g+h)=U(g)U(h),
\qquad
U'(0)=-iH.
\]

Differentiating in (h) at zero gives

\[
U'(g)=-iU(g)H.
\]

The initial-value problem has the unique solution

\[
\boxed{U(g)=e^{-igH}.}
\]

Thus the exact Hamiltonian completion is selected by

\[
\text{first tangent}+\text{one-parameter composition},
\]

not by the finite Cut jet alone.

## Hostile comparison

For (H^2=I), Entry 1643's polar completion has slope

\[
r_{\rm pol}(g)=\frac{2g}{2-g^2}
\]

in the basis (I,-iH).  Matrix composition combines slopes by

\[
r\star s=\frac{r+s}{1-rs}.
\]

The exact checker finds

\[
r_{\rm pol}(g+h)\ne
r_{\rm pol}(g)\star r_{\rm pol}(h)
\]

at every tested generic rational pair.  Hence the competing CP completion is rejected by source composition.

## Narrow result

\[
\boxed{
\text{The source composition law removes the global CP-completion ambiguity and selects the exponential.}
}
\]

This identifies a second native ingredient alongside the carrier and sector coefficient object: a composition/evolution law.  It should not be folded into the carrier, because the same carrier supports distinct coefficient dynamics.  Nor is it arbitrary repair; it is the primary Hamiltonian time-composition law.

This result does not yet prove compatibility between time composition and Cut sewing on general labelled graphs.

## Durable artifacts

- `research/benincasa/checkers/composition_selects_exponential.rs`
- `research/benincasa/results/composition-selects-exponential.json`
- `research/benincasa/composition-selects-exponential.md`

## Next falsifier

Test the interchange law between temporal composition and labelled Cut sewing on two adjacent cubic steps.  The two routes

\[
\text{compose globally then Cut},
\qquad
\text{Cut each step then sew occurrences}
\]

must agree after retaining the virtual terms and internal-state pushforward.  A nonzero commutator would require a coherence cell in the shared calculus.
