# Objectwise bijection without naturality breaks probe rewrite

## Question

Is an objectwise bijection between finite constraint presheaves enough to preserve matching-map fibers under a local rewrite?

## Claim boundary

This packet gives a finite countermodel on the full two-probe face system. It proves necessity of restriction naturality for the stated fiber-preservation argument. It does not prove that naturality alone establishes global rewrite confluence or physical equivalence.

## Face system

Use the four faces

\[
\varnothing,\quad \{p\},\quad \{q\},\quad \{p,q\}.
\]

Both presheaves \(F\) and \(G\) have the same objectwise sets:

\[
F(\varnothing)=G(\varnothing)=\{*\},
\]

\[
F(p)=G(p)=F(q)=G(q)=\{0,1\},
\]

\[
F(pq)=G(pq)=\{a,b\}.
\]

All singleton-to-empty restrictions are constant. This makes every composite restriction to the empty face agree.

## Different joint restrictions

For \(F\), define

\[
a\mapsto(0,0),
\qquad
b\mapsto(1,1)
\]

under restriction from the joint face to the two singleton faces. For \(G\), define

\[
a\mapsto(0,0),
\qquad
b\mapsto(0,0).
\]

Both are lawful presheaves: identity maps are identities, and every two-step route from the joint face to the empty face is the unique constant map.

The identity bijection at every face is an objectwise equivalence of the underlying sets. It is not natural. At the inclusion \(p\subset pq\), the naturality square evaluated on \(b\) compares \(1\) with \(0\).

## Matching maps and fibers

Compatibility over the empty face is automatic, so the matching object is

\[
M=\{0,1\}\times\{0,1\}.
\]

The matching maps are

\[
\mu_F(a)=(0,0),\quad \mu_F(b)=(1,1),
\]

and

\[
\mu_G(a)=(0,0),\quad \mu_G(b)=(0,0).
\]

With identity objectwise bijections, conjugacy would require \(\mu_F=\mu_G\), which fails on \(b\). The fiber over \((1,1)\) has cardinality one for \(F\) and zero for \(G\). Therefore no fiber equivalence over that matching datum exists.

## Consequence

Equal object cardinalities, objectwise bijections, and separately lawful restriction functors do not construct a rewrite certificate. Naturality is the coherence datum that relates objectwise coordinates to restriction maps. Without it, local extension multiplicity can change.

## Disposition

The countermodel rejects the rival claim that objectwise equivalence suffices. The natural-isomorphism hypothesis in `ProbeRewrite` is necessary for matching-map conjugacy and the induced fiber-equivalence theorem. This necessity result remains local and finite.
