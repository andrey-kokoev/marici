# Boolean readout of a specified tetrahedral face

Actor: marici.Voevodsky. Date: 2026-10-06. Textual derivation from existing theorem signatures; no new Agda check claimed.

## Use the existing compatibility question

Fix the actual six-edge package e and three face witnesses alpha:Face012, beta:Face123 and gamma:Face013. Let h denote this horn. The existing `unique023` constructs a pair (delta_h,t_h): a fourth face and an interior witness. Given a separately specified fourth face d:Face023, define

\[
F(h,d)=\operatorname{Tetrahedron}(\alpha,\beta,\gamma,d).
\]

The existing `solve023` gives

\[
F(h,d)\simeq(d=\delta_h),
\]

where delta_h is the inverse image of the right pasted route under `route023 alpha`. Thus the compatibility question is native to the retained boundary; no NAND labels or new geometric vertices are chosen.

There are two distinct requests. Constructing some compatible face and filler is solved by `unique023`. Filling the specified d additionally requires its agreement with delta_h; `incompatible-face` expresses the obstruction. One must not replace the latter request with the former.

## Apply the existing Boolean reflection

Define the stable truth

\[
C_{h,d}=\neg\neg F(h,d).
\]

It is propositional and double-negation stable, because it is a negation. The face-compatibility equivalence induces

\[
C_{h,d}\simeq\neg\neg(d=\delta_h).
\]

This readout retains (h,d) as external indices. It does not assert that the Boolean value encodes or reconstructs the full boundary, face or interior witness.

For any two further questions P and Q, the existing constructive theorem gives

\[
W(P,Q,C_{h,d})\simeq\neg\neg C_{h,d}\simeq C_{h,d}.
\]

Therefore the Wolfram expression is a Boolean presentation of the double-negated compatibility question of this specified tetrahedral face. P and Q remain arbitrary: the result does not select them from the tetrahedral boundary, and therefore does not complete the proposed three-question identification.

For d=delta_h, the constructed t_h gives a witness of C by n mapping to n(t_h). If a refutation of F(h,d) is supplied, it refutes C by evaluation. No general decidability of compatibility is assumed.

## Does it construct the filler?

A filler gives its double-negation image:

\[
F(h,d)\longrightarrow C_{h,d}.
\]

The reverse is not supplied by Boolean reflection. Even a term of W(P,Q,C) returns only double-negated compatibility through this route, not a term of F. Recovering a filler requires a separate double-negation eliminator for F. An equivalence with F also requires propositionality of F. In higher retained types, neither condition follows merely from horn completion; contractibility of the total missing-face-and-filler space does not make every prescribed-face fiber inhabited or stable.

Thus it is accurate to say that Wolfram's expression presents the stable truth of this filling question. It is not yet accurate to say that the formula is the tetrahedral filler or generates that filler.

## The discriminating observation

The proof above works for any type T in place of F(h,d): W(P,Q,not-not T) is equivalent to not-not T. It does not use the six-edge incidence or four-face pasting beyond selecting T.

Consequently this supplies a genuine predicate-level bridge, but not an explanation of why tetrahedral incidence would select Wolfram's particular nesting. Such an explanation needs a constructor-respecting assignment of P,Q,C whose actual boundary operations elaborate to that nesting, plus an argument that the connection is not generic substitution of an arbitrary proposition into an already proved identity.

This is stronger than identifying vertices with Boolean atoms: the predicate concerns the actual full marked boundary. It remains weaker than the proposed formula-as-filler identification. The next missing datum is the assignment of operations and the other two questions, not another generic proof of Booleanity.

## Source evidence

- `research/nima/agda/MarkedTetrahedronCoherence.agda`: `route023`, `unique023`, `solve023`, `incompatible-face`.
- `research/nima/agda/RetainedTetrahedralPackage.agda`: `Over.Horn`, `complete`, boundary preservation and horn/package isomorphism.
- `research/nima/agda/QBooleanity.agda`: `wolfram-double`, `stable-equivalence`, `idempotent` and `reflection`.
- `research/nima/agda/RetainedNandPhases.agda`: retained-question counterpart and information-loss boundary.

The statements here are a mathematical composition of these interfaces, not a new compiled bridge module, a discovered single axiom, or a proof of universal constructor capability.
