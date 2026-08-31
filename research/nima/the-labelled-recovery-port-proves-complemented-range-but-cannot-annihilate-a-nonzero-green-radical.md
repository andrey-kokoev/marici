# The labelled recovery port proves complemented range but cannot annihilate a nonzero Green radical

## Question

What do the retained-label recovery identities actually prove about closed range and G4 quotient descent?

## Claim boundary

A continuous left inverse proves that the labelled source range is complemented and therefore closed in the declared projective target. It does not prove radical annihilation. In fact, the recovery map itself cannot annihilate any nonzero source radical because it is the identity on recovered source coefficients. Recovery and physical quotient return must be distinct arrows whenever the Green radical is nontrivial.

## Complemented labelled range

Let

\[
\mathcal I:\mathcal A_{\exp}\to\mathfrak H_{\exp}^{\rm lab}
\]

be the labelled theta-history synthesis and let

\[
\mathcal R:\mathfrak H_{\exp}^{\rm lab}\to\mathcal A_{\exp}
\]

be the continuous fibrewise recovery map, with

\[
\mathcal R\mathcal I=I.
\]

Then

\[
\mathcal P_{\rm src}=\mathcal I\mathcal R
\]

is a continuous idempotent:

\[
\mathcal P_{\rm src}^2
=\mathcal I\mathcal R\mathcal I\mathcal R
=\mathcal I\mathcal R
=\mathcal P_{\rm src}.
\]

Its range equals \(\operatorname{ran}\mathcal I\). Hence

\[
\operatorname{ran}\mathcal I
=\ker(I-\mathcal P_{\rm src})
\]

is closed and complemented in the labelled projective history carrier.

This is a projective closed-range theorem. It is not an unweighted Hilbert closed-range theorem and does not survive a codiagonal unless the recovery map factors through that codiagonal continuously.

## Radical incompatibility

Let \(G\) be the source Green form and

\[
N=\operatorname{rad}G
\subset\mathcal A_{\exp}.
\]

If \(n\in N\), then recovery gives

\[
\mathcal R\mathcal I n=n.
\]

Therefore

\[
\mathcal R\mathcal I n=0
\quad\Longleftrightarrow\quad
n=0.
\]

If \(N\ne0\), the recovery port does not annihilate \(N\). It faithfully reports radical directions rather than quotienting them.

Thus a claim that the same arrow is both a left inverse and a radical-annihilating physical return forces

\[
N=0.
\]

That conclusion requires an independent proof of nondegeneracy and cannot be inferred from recovery.

## Required quotient diagram

For a nontrivial radical, G4 needs two separate maps:

\[
\mathfrak H_{\exp}^{\rm lab}
\overset{\mathcal R}{\longrightarrow}
\mathcal A_{\exp}
\overset{q}{\longrightarrow}
\mathcal A_{\exp}/N.
\]

The physical reduced return is

\[
q\mathcal R,
\]

and satisfies

\[
q\mathcal R\mathcal I n=q(n)=0
\]

for \(n\in N\). The quotient map \(q\), its topology, and the proof that every G4 mixed or return form factors through it are additional interface data.

Alternatively, a Green feature map \(J\) may realize

\[
\ker J=N.
\]

Then descent is through \(J\), not through the faithful coefficient recovery map.

## G4 conformance consequence

A valid retained-label G4 interface must expose distinct fields for:

- `source_recovery`, satisfying \(\mathcal R\mathcal I=I\);
- `green_radical`;
- `quotient_map` or a feature map with exactly that kernel;
- `physical_return`, factoring through the quotient;
- a witness that all mixed forms annihilate the radical in each required variable.

One generic `return` field cannot certify both faithful recovery and nontrivial quotient descent.

## Direction rescore

- Labelled projective closed range: completed.
- Unweighted Hilbert closed range: disproved previously.
- Radical annihilation from recovery: disproved unless the radical is zero.
- Separate quotient-return diagram: exact criterion completed; G4 data absent.
- G4 nondegeneracy proof or radical witness: interface-blocked.

## Disposition

Architecture A now has a precise strength boundary: it supplies complemented projective source range and faithful coefficient recovery. Radical descent requires a separate quotient or Green feature map. G4 must not identify recovery with physical reduced return unless it first proves the source Green radical is zero. No RH conclusion is authorized.
