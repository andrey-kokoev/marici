# Canonical source-to-physical16 portal (WP360)

## Bounded question

Can the canonically normalized WP359 source readout enter a flavor operation
that descends under the full weak-basis groupoid and selects a proper subset of
`physical16`?

Let \(Q>0\) be the invariant canonical source displacement from WP359, and let
\(J\) be the signed Jarlskog coordinate on a nondegenerate local `physical16`
chart. Test the minimal CP-even portal

\[
V_{\mathrm{int}}=\lambda(J^2-cQ)^2,
\qquad \lambda>0,\quad c>0.
\]

Both \(J^2\) and \(Q\) are invariant under their respective weak-basis and
effective-field reparameterization groupoids. The portal therefore descends
without choosing a texture chart or reference port.

## Image and rank

The zero-energy locus is

\[
J^2=cQ.
\]

Away from \(J=0\), this is one regular constraint on the sixteen-dimensional
physical quotient. It selects two CP-conjugate sheets, each with fifteen free
CP-even coordinates. A CP-odd source bias would be required to select one
orientation; the even portal does not do so.

This is a genuine conditional proper-subspace selector, but not a numerical
selector. The selected magnitude responds to both admitted source quantities:

\[
\frac{\partial |J|}{\partial Q}
=\frac{\sqrt c}{2\sqrt Q},
\qquad
\frac{\partial |J|}{\partial c}
=\frac{\sqrt Q}{2\sqrt c}.
\]

The matching coefficient \(c\) and the source vacuum \(Q\) therefore carry
the numerical value.

## Contextual partition and hostile pair

The portal probes only \(J^2-cQ\). Two `physical16` points that share \(J\)
but differ in any CP-even coordinate are physically inequivalent and remain
indistinguishable to this operation. Thus the first nonfaithful arrow is

`physical16 -> J^2 -> portal residual`.

The source-side pair \((Q,c)=(1,1)) and \((4,1/4)\) also selects the same
shell \(J^2=1\). Descent does not imply source identification or numerical
authority.

## Disposition

Conditional on the displayed portal being derived from a flavor action, the
operation descends under the full weak-basis groupoid and selects a proper
codimension-one family. It is a selector and shell rigidifier, but neither a
full `physical16` selector nor a source-derived numerical prediction.

The smallest exact authority falsifier is the nonzero response
\(\partial |J|/\partial c\). The remaining physical-instrument gate is an
independent derivation of the portal coefficient and a common-frame experiment
measuring both the canonical source response \(Q\) and the signed or unsigned
Jarlskog readout. No absolute CP orientation is supplied by the even portal.

Run `uv run --with sympy python
research/flavor/checkers/wp360_canonical_source_physical16_portal.py` to
regenerate the exact result.
