# Half-line shifts transport jump triangles with an explicit boundary correction

## Right zero-extension

For a breakpoint \(c\), right extension by \(a\) transports its one-sided traces unchanged to \(a+c\). Therefore

\[
\boxed{
J_{a+c}S_a=J_c.
}
\]

Every refinement triangle commutes:

\[
\begin{array}{ccc}
\mathcal D_B&\longrightarrow&\mathcal D_{B\cup\{c\}}\\
\downarrow S_a&&\downarrow S_a\\
\mathcal D_{S_aB}&\longrightarrow&\mathcal D_{S_a(B\cup\{c\})}
\end{array}
\]

and the induced map on cofibers identifies

\[
\mathbb C_c\cong\mathbb C_{a+c}.
\]

Right extension also creates one new seam at \(a\), with

\[
J_a(S_af)=f(0+).
\]

Thus the original endpoint line becomes a jump line. This is the exact residual retyping already suggested by the boundary-charge picture.

## Left shift

If \(c>a\), the seam survives at \(c-a\), and

\[
\boxed{
J_{c-a}R_a=J_c.
}
\]

If \(c<a\), the seam crosses outside the half-line and is absent from the target graph. If \(c=a\), only the right trace becomes the new endpoint value; its jump cannot be reconstructed from the target alone.

These lost coordinates are exactly the relative Green defect of left compression. Hence left shift is not absolutely exact-triangle natural, but it is natural after adjoining its declared compression cofiber.

## Four-prime audit

For the fifteen positive subset-sum seams and four prime shifts, the checker records:

- 60 right-shift refinement squares;
- four new endpoint-to-jump cells;
- 49 surviving left-shift jump squares;
- seven seams crossing the boundary;
- four seams landing exactly at the new endpoint.

Every applicable jump identity is exact.

## Higher-categorical meaning

Shift transport acts on residuals by a recollement pattern:

\[
\text{discarded region}
\rightleftarrows
\text{full broken graph}
\rightleftarrows
\text{retained half-line}.
\]

Right extension embeds and retypes endpoint data as an interior seam defect. Left compression retains later seams and exports earlier seams to a relative cofiber.

Therefore the correct higher functor is not exact in an absolute target. It is an exact functor into a category of pairs or recollement diagrams, where the discarded boundary sector remains part of the morphism.

This completes the finite compatibility chain:

\[
\boxed{
\text{primitive transport}
\to
\text{jump cofiber}
\to
\text{typed residual transport}
\to
\text{new boundary primitive}.
}
\]

## Verification

Run:

```text
python research/coherence/check_shift_jump_triangle_naturality.py
```

Artifacts:

- `check_shift_jump_triangle_naturality.py`
- `shift-jump-triangle-naturality.v1.json`
