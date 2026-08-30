# Frozen derived-specialization network signature v7

## Status

Version 7 is a new frozen local candidate. Version 6 remains unchanged and falsified.

The repair replaces a bare specialization square with an equivariant specialization complex and retains its vanishing-cycle defect.

## Repair of the v6 hostile

The v6 hostile used

\[
H_{\mathrm{near}}=\operatorname{diag}(1,-1),
\qquad
H_{\mathrm{exc}}=(1),
\qquad
J=\begin{pmatrix}1&0\end{pmatrix}.
\]

Although (JH_{\mathrm{near}}=H_{\mathrm{exc}}J), the kernel of (J) is the half-turn line. v6 allowed that line and its boundary port to disappear.

v7 retains the full two-term equivariant complex

\[
R_{\mathrm{near}}\xrightarrow{J}R_{\mathrm{exc}}
\]

and its mapping cone. The kernel and cokernel inherit transport and remain visible as vanishing-cycle data. Nearby, exceptional, and defect objects form a distinguished triangle.

## Derived boundary port

Ordinary holonomy invariants are not generally exact. Therefore v7 does not define the global boundary calculation by taking fixed vector spaces term by term.

For a transport object (R), it retains the homotopy-fixed object and its cofiber in a triangle

\[
R^{h\Pi}\longrightarrow R\longrightarrow B_R.
\]

Applying this construction to the specialization triangle preserves the defect. Strict descent requires both the derived boundary object and the vanishing-cycle defect to vanish.

## First unused hostile

Let the loop group be the integers. Consider an exact sequence of representations

\[
0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow0
\]

where (A) and (C) are trivial one-dimensional representations and the generator acts on (B) by

\[
T_B=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

The invariant space of (B) is only the first coordinate line. Its projection to the invariant space of (C) is zero. Hence ordinary invariants do not preserve the surjection (B\to C).

The missing class is carried by the next derived fixed-point term. v7 explicitly requires the derived fixed-point triangle, so it does not mistake this packet for an exact sequence of ordinary invariant spaces.

## Frozen exclusions

v7 forbids:

- promoting a commuting specialization square to conservative transport;
- discarding a specialization kernel or cokernel;
- treating ordinary invariant spaces as an exact functor;
- discarding a nonzero vanishing-cycle boundary defect;
- performing finite projection before completed sewing;
- adding packet-specific derived cells during replay.

## Next falsifier

Attack completion. Use an infinite-dimensional transport complex where homotopy fixed points do not commute with the selected inverse limit, closure, or spectral completion. That is the first place a finite derived triangle may again lose a boundary channel.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v7.py
```
