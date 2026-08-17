# Entry-143 Ringed Incidence Enhancement

## Result

The cellular cosheaf of entry 349 has a canonical enhancement to a module
on a ringed finite space. This supplies an honest target derived category in
which an extraordinary inverse image can be typed. It does not construct
the central-flip span or compute that extraordinary inverse image.

Let (P=P_{K_6}^{m or}), and use the opposite Alexandrov space
(X=P^{m op}). For (x=(S,H)), set

[
A_x=R[X]igl[u_a^{-1}:ain Ssetminus Higr].
]

For every entry-143 boundary relation (xprec y), the set of inverted
normal parameters only grows. Hence the canonical localization
(ho_{xy}:A_x	o A_y) is a ring map. Iterated localizations commute, so
the (A_x) and (ho_{xy}) define a sheaf of rings (mathcal O_X) on
the opposite Alexandrov space.

Define a rank-one diagram of (mathcal O_X)-modules
(mathcal L^{check C}) by (mathcal L_x=A_x e_x). Its transition on a
normal deletion is

[
e_xlongmapsto e_y,
]

and its transition on radial addition by (a) is

[
e_xlongmapsto (X_a/u_a)e_y.
]

These maps are semilinear over (ho_{xy}). Every two-step square
commutes: localization commutes with localization, the radial factors
commute with each other, and localization commutes with multiplication by a
radial factor. Thus (mathcal L^{check C}) is a well-defined module on
the ringed incidence space, not merely a list of coefficient groups.

After the standard cellular incidence signs and the degree
(deg(S,H)=3-|S|+|H|) are inserted, the compact cellular chains of
(mathcal L^{check C}) are exactly
(mathcal E_{partial,Q}^{m BM,check C}). The support diagrams
(F_Vsubset F_Bsubset F_K) are submodules, so the filtered quotients and
their ranks are unchanged.

## What this types

For a morphism (q:Z	o X) of finite ringed spaces, the derived
direct-image functor on the bounded constructible/perfect subcategory is a
functor between small derived module categories. Whenever the chosen
subcategory is preserved and the right adjoint exists, denote that right
adjoint by

[
q^!:D(X,mathcal O_X)longrightarrow D(Z,mathcal O_Z).
]

The target of (q^!) is now defined and the expression (q^!mathcal
L^{check C}) is type-correct once (q) is supplied. This is a typing
theorem, not an existence theorem for a particular central-flip (q), and
not a purity or trace calculation.

## Exact remaining boundary

The enhancement is a ringed finite incidence space. It is not claimed to be
the exit-path diagram of an algebraic or fs-log scheme, and no comparison
with étale, analytic, or Kato--Nakayama six operations is asserted.
In particular:

1. no normalization-provenanced correspondence space (Z) has been
   constructed;
2. no projections (p) and (q) from such a (Z) have been defined;
3. preservation of the required perfect/constructible subcategory for
   those projections is unproved;
4. no relative dualizing object, orientation, proper trace, or PC-purity
   comparison has been computed.

Consequently the first remaining central-flip obligation is now
`d_central_flip_projections`, followed by the dualizing trace and PC
purity. The product-branch Rees blowup of entry 216 remains useful input,
but entry 348's warning still applies: it is not itself the required span.

Delegation evidence: run-62988bfa58c046d19b3ec80df2416628. The two
parallel constructive audits, run-2f4fe14ee2364adea9055de7be8cbb6d and
run-786a0fc498bd41bb8fd49af8eb1ebf1e, exited without results and are not
used as evidence.
