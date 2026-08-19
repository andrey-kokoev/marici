# 1047 — The Chart Phase Enters the Invariant Ring Only Through \(\sin\phi\) at Leading Order

## Question

Entry 1042 showed the loop phase \(\phi\) is a chart invariant, not a
physical one.  The refined next test (registered from marici.Benincasa):
the surviving route to physical meaning is that the chart pushes a
*function* of \(\phi\) forward into a genuine weak-basis invariant.
Derive that pushforward exactly, compute its fibers, and ask whether the
physical invariant ring can prefer discrete values such as
\(\pi/8,\pi/4,3\pi/8\).

One correction to the refinement is needed first.  The worry that "the
same ten observables" might not be "the same physical point" is settled
by a dimension count: \((Y_u,Y_d)\) carry \(36\) real parameters, the
effectively acting flavor group \(U(3)^3\) has \(26\) generators (one
diagonal phase acts trivially), so
\(\dim \mathfrak F_{\mathrm{phys}} = 10 = 6 + 3 + 1\).
The paper's ten fit observables are generically a *complete* coordinate
set on the physical quotient.  What survives of the caveat is finite
numerical tolerance and discrete fibers — which the orbit criterion of
Entry 1042 already addresses more strongly than any scan comparison.

## What the exact computation establishes

For the two shortest-loop worked examples of the source, with the placed
phase generalized to \(e^{i\phi}\):

- Example I (S38, phase on \(Y^u_{12}\)):
  \[
  \det[Y_uY_u^\dagger,Y_dY_d^\dagger]_{\mathrm{lead}}
  =
  d_{12}d_{22}d_{23}^2d_{33}^2\,u_{12}u_{22}u_{33}^4\,\epsilon^{26}\,
  \bigl(e^{i\phi}-e^{-i\phi}\bigr);
  \]
- Example II (S43, phase on \(Y^d_{33}\)):
  \[
  \det[Y_uY_u^\dagger,Y_dY_d^\dagger]_{\mathrm{lead}}
  =
  d_{13}d_{23}^2d_{32}^2d_{33}\,u_{13}u_{22}^2u_{33}^3\,\epsilon^{22}\,
  \bigl(e^{i\phi}-e^{-i\phi}\bigr).
  \]

In both cases the coefficient \(K\) is verified exactly to be a
positive-real monomial in the edge magnitudes, free of \(\phi\), so

\[
\det[H_u,H_d]_{\mathrm{lead}} = 2iK\sin\phi .
\]

Since \(\det[H_u,H_d] = \pm 2i\,J\,\Delta_u\Delta_d\) (Vandermonde
products of the squared-mass spectra), this is the leading pushforward of
the chart phase into the physical invariant ring:
\(\phi \mapsto J_{\mathrm{lead}} \propto K\sin\phi\).
At the paper's placements the formula reduces correctly
(\(\phi=\pi/2\): \(2iK\), purely imaginary, checked exactly;
\(\phi=-\pi/8\): \(-2iK\sin(\pi/8)\), likewise).

## Result

\[
\boxed{
\text{LO pushforward: }\phi_{\rm chart}\mapsto \sin\phi\ \text{into }
J;\quad
\text{fibers }\{\phi,\pi-\phi\};\quad
\text{no algebraic mechanism prefers any value of }\sin\phi .
}
\]

Consequences, stated no more strongly than the evidence:

- within these charts the physical invariant data fix only \(\sin\phi\)
  at leading order; \(\phi\) and \(\pi-\phi\) are indistinguishable, and
  the invariant ring is a smooth function of the phase — it cannot
  quantize it;
- therefore the almost-\(\pi/8\) clustering cannot originate on the
  physical-invariant side.  It must enter through the viability/fit
  conditions — the leading-order identifications
  \(\phi\simeq\alpha,\beta,\gamma\) push the *observed* CKM angles (which
  sit near multiples of \(\pi/8\)) back onto the chart phase.  The
  "sparse-presentation selection effect" reading is no longer only a
  prior; for these two charts it is the derived leading-order structure;
- the invariant ring does see the phase: CP is carried physically
  (\(J\neq0\) unless \(\sin\phi=0\)), consistently with the paper's
  strong-CP-relevant determinant structure remaining chart-level.

Caveats: leading order in \(\epsilon\), two charts.  Higher orders add
the calculable corrections that separate the Yukawa triangle from the
CKM triangle; the no-quantization statement is structural (traces and
determinants are entire functions of \(e^{i\phi}\)) and does not depend
on the truncation.

## Next finite test

Extend the same exact computation to the six-link loop (Example III,
S48, \(\gamma\simeq\pi-\phi\)) and to the \(\pi/4\) texture (S53), and
check whether the \(\sin\phi\) form persists with a chart-computable
\(K\).  In parallel, WP4's symbolic audit of App. II should isolate
*which* fit-viability condition forces \(\phi\) onto the CKM angles —
that condition, not the invariant ring, is where any \(\pi/8\) structure
must live.

## Verification artifacts

- `research/flavor/checkers/phi_pushforward.py`
- `research/flavor/results/phi_pushforward.json`

Epistemic graph event: `ev-000000000668-103f62df-d90b-4452-b8dc-d869d4636226`.

## Sequence
- allocator claim: `seqclaim-ddd40e145204d186b25c8ccf`.
