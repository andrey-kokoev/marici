# The translation/reversal context Hankel rank stabilizes at two

## Frozen constructor alphabet

At the residual level, admit exactly

```text
T_z  reciprocal-weight translation
R    orientation reversal
```

with

\[
R^2=I,
\qquad RT_zR=T_z^{-1}.
\]

This freezes the protocol before asking for a complete contextual type.

## Context process

Let words in \(\{T_z,R\}^*\) act on the stationary carrier

\[
L_{\rm in}\oplus L_{\rm out}.
\]

For a generic initial state \(\beta\) and readout \(\alpha\), define

\[
f(w)=\alpha\rho(w)\beta
\]

and finite-depth Hankel matrices

\[
H_h(u,v)=f(uv),
\qquad |u|,|v|\le h.
\]

## Result

Every \(H_h\) factors through the two-dimensional carrier, so

\[
\operatorname{rank}H_h\le2.
\]

For generic probes, the rank reaches two and remains there. The checker evaluates depths zero through four in 35 exact-rational systems; every rank sequence is nondecreasing, bounded by two, and stabilized at two.

Thus the hyperbolic double is not merely sufficient. Relative to the frozen \(T_z/R\) protocol, it is generically minimal and context-closed.

## Rank audit

For this protocol:

```text
constructor alphabet size = 2
continuous orbit rank     = 1
minimal realization rank  = 2
```

The discrete reversal does not add a continuous orbit direction, but it doubles the stationary realization by exposing the dual weight.

## Scope

Adding seam refinement, jump creation, or independent prime-labelled controls changes the context alphabet and requires a new stabilization calculation. This result authorizes stationarity only for translation and reversal.

## Verification

```text
python research/coherence/check_dihedral_context_hankel_stabilization.py
```

Artifacts:

- `check_dihedral_context_hankel_stabilization.py`
- `dihedral-context-hankel-stabilization.v1.json`
