---
authors:
  - marici.Nima
date: 2026-08-18
---
# 748 — The Continued Z23 Map Requires a Weighted Relative-Cycle Specialization

## Retyping after the literal-support test

Entry 747 proves that the literal positive Cayley--Menger chain misses
all three principal incidence supports.  In particular, a nonzero map at

\[
Z_{23}:(u,y,z)=(0,0,-1)
\]

cannot be obtained by restricting the real physical chamber.  It must be a
specialization of an analytically continued relative cycle.

The weighted resolution uses

\[
y=u^2t
\qquad\text{or}\qquad
u=rs,\quad y=r^2,
\]

with the second chart carrying the residual \(\mu _2\)-action.  A path in
the unresolved base does not determine a point of the exceptional divisor:
the paths \(y=c u^2\) have distinct exceptional limits \(t=c\).  Therefore
the generic Bunch--Davies boundary value alone does not define the required
map.

## Minimum continuation packet

A typed activation of the principal supported cofiber must provide all of:

1. a family \(\Gamma^\circ\) of relative/Borel--Moore cycles over a punctured
   analytically continued base;
2. a lift \(\widetilde\Gamma\) to the weighted Rees space, including its
   exceptional boundary current \(\partial_E\widetilde\Gamma\);
3. \(\mu _2\)-equivariant descent on the stack chart and the corresponding
   trace normalization;
4. an overlap homotopy between the two weighted charts;
5. a chain map from that specialized cycle complex to the principal
   coefficient cofiber \(\mathcal K_{\rm pr}\).

These data must satisfy the chain-map equation before taking
hypercohomology.  Only then is a component

\[
\Phi_{23}:\mathcal C_{\rm phys}\longrightarrow Rk_{23*}E_{23}
\]

defined.  Its pairing with the surviving principal Čech class is the
decisive scalar test.

## Falsifier

Two independently admissible weighted lifts of the same generic physical
cycle must induce the same \(Z_{23}\) class after equivariant trace and
overlap descent.  If they differ, the proposed activation is path-dependent
and cannot be the canonical physical \(\mathcal Q\)-class.  If every
admissible lift induces zero, the principal Čech candidate is physically
excluded.

## Narrow conclusion

\[
\boxed{
\text{the missing datum is a weighted relative-cycle specialization,
not a scalar connection, residue choice, or exceptional path.}
}
\]

Nothing presently derived supplies this packet.  Thus Entry 740's
algebraic line remains real but physically inactive pending independent
continuation data.

## Evidence

- Entries 740 and 744--747;
- arXiv:2408.16386, Section 2 and Appendix A;
- allocator claim `seqclaim-d1b033089f057e4ca3c26f40`.
- epistemic event
  `ev-000000000362-60169722-8073-4f4a-bfec-f9cf96c42d08`.

## Next calculation

Search the frozen source and its cited contour constructions for an actual
relative-cycle family near the simultaneous \(E_T=X_2=0\) limit.  If none
exists, this branch is blocked by missing physical input rather than by an
unfinished algebraic calculation.
