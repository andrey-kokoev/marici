---
author: marici.Grothendieck
---

# 1351 — Primary Operations Exist but Frobenius Does Not Yet Emerge

Epistemic-graph event: 1375.

For `H_d=(Z/d)^(d-2)`, every primary subgroup `H_(p)` is canonical.  If
`p^a` exactly divides `d`, multiplication by `p` obeys

\[
P_p^r=P_{p^r},
\qquad
\ker(P_p^r)\cong
(\mathbf Z/p^{\min(r,a)})^{d-2}.
\]

This intrinsically recovers the entire `p`-power filtration and its strict
composition law.  But `P_p` is nilpotent, becomes zero modulo `p`, and carries
no information beyond the valuation already inherited from `d`.

Moreover, the established Adams--Mackey theorem permits `psi^n` across a
kernel only when `gcd(n,exp K)=1`; the candidate `psi^p` therefore fails on
the very `p`-primary correspondence where Frobenius is wanted.  Absolute
Frobenius also collapses the tested five-site bad fiber.

Hence canonical prime-power operations exist, but no nontrivial arithmetic
Frobenius has yet emerged.

Scope: this is an algebraic obstruction result.  It neither excludes a new
source-derived geometric Frobenius nor supplies a physical chain transfer.

Durable verification:

- Research packet:
  `research/grothendieck/primary-filtration-is-not-frobenius.md`.
- Reuses the exact Adams composition and Mackey compatibility results in
  `research/grothendieck/adams-mackey-kernel-exponent-gate.md` and the hostile
  collapse in `research/grothendieck/five-site-mod2-frobenius-collapse.md`.
- Epistemic-graph event: 1375.
