---
author: marici.Voevodsky
---

# 4310 — Cardano and Chinese Remainders as Witnessed Assembly

## Question and constructor

Can two complementary constructions, joined by explicit compatibility evidence, assemble a classical solution together with its correctness witness? The operator proposed testing this through Cardano's cubic formula and the Chinese remainder theorem. The active coherence obligation is route/coherencer compatibility: the assembled term must satisfy the original equation or recover the original residue pair.

The proposed constructor retains the two components and their compatibility, computes the output, and attaches the correctness proof. Its rivals are independent component selection without compatibility and a final value with its branch/attachment evidence discarded. The tests below distinguish these cases without treating the tetrahedral illustration as a proof.

In the geometric vocabulary of this exploration, endpoint barycenters represent component constructions, the connecting center represents their compatibility, and the assembled center represents a solution with its witness. These are typed roles assigned to the illustration, not numerical assertions about barycentric coordinates or areas. Independently invertible component constructions need not be mutual inverses of each other.

## Cardano: couple two cubic contributions

Work over the complex numbers with the depressed cubic

\[
x^3+px+q=0.
\]

Choose contributions satisfying

\[
u^3+v^3=-q,
\]

\[
uv=-\frac p3.
\]

Their assembly is

\[
x=u+v.
\]

The exact correctness identity is

\[
(u+v)^3+p(u+v)+q
=(u^3+v^3+q)+(3uv+p)(u+v).
\]

Thus the sum and product witnesses make the residual vanish. To derive the endpoint formulas, the two values u cubed and v cubed are the roots of

\[
t^2+qt-\frac{p^3}{27}=0.
\]

Set

\[
\Delta=\frac{q^2}{4}+\frac{p^3}{27}.
\]

Then

\[
u^3=-\frac q2+\sqrt{\Delta},
\]

\[
v^3=-\frac q2-\sqrt{\Delta}.
\]

Cardano's expression follows by taking compatible cube roots and adding them. The compatibility is essential: when u is nonzero, set v equal to minus p divided by three u; its cube then has the required value. If the selected cubic contribution is zero, use the opposite nonzero contribution first. If both are zero, p and q vanish and the root is zero.

For an exact worked branch, p=-6 and q=-9 give Delta=49/4, u=2, v=1 and x=3. The assembled term consists of the root and the proof that its cubic residual is zero. Retaining u, v and their choices additionally preserves the construction data. Cubing is not globally invertible on the complex numbers: an invertible endpoint presentation must retain branch data or restrict to a specified branch graph. No global inverse from a root alone to its chosen Cardano decomposition is asserted.

**Falsifier.** Taking u=v=1, p=0, q=-2 satisfies the cubic-sum requirement but violates the product requirement. The proposed root x=2 has residual 6. Independent contributions without their connecting witness do not suffice.

## Chinese remainders: assemble independent residue channels

Take an input a modulo 3 and b modulo 5. Construct contributions modulo 15:

\[
U(a)=10a\pmod{15},
\]

\[
V(b)=6b\pmod{15}.
\]

Their compatibility is explicit:

| Contribution | Reduction modulo 3 | Reduction modulo 5 |
| --- | --- | --- |
| U(a) | a | 0 |
| V(b) | 0 | b |

U is invertible onto its three-element image, with inverse reduction modulo 3. V is invertible onto its five-element image, with inverse reduction modulo 5. They are not mutual inverses: they have different input types and complementary images.

Assemble and decompose by

\[
F(a,b)=10a+6b\pmod{15},
\]

\[
G(x)=(x\bmod3,\ x\bmod5).
\]

The compatibility table proves

\[
G(F(a,b))=(a,b).
\]

Conversely, F(G(x)) has the same residues as x. Their difference is divisible by both 3 and 5, hence by 15, so

\[
F(G(x))=x\pmod{15}.
\]

This supplies the witnessed equivalence

\[
\mathbb Z/3\times\mathbb Z/5\simeq\mathbb Z/15.
\]

For a=2 and b=3, the contributions are 5 and 3 modulo 15. Their sum is 8, with residue witnesses 8 modulo 3 equals 2 and 8 modulo 5 equals 3. The assembled center represents this solution and both witnesses; the entire constructor includes the two round-trip laws for all inputs.

**Falsifiers.** Replacing coefficient 6 by 5 produces x=5 on the same input, with residues (2,0), not (2,3). Coprimality cannot be discarded without changing the interface: residues 1 modulo 4 and 2 modulo 6 are incompatible, whereas residues 1 modulo 4 and 3 modulo 6 assemble to 9 modulo 12.

## Disposition and scope

Both classical examples instantiate component construction, compatibility, assembly, and a witnessed result. The executable check proves the displayed Cardano polynomial identity by exact coefficient comparison, checks an exact radical branch, and exhaustively verifies both Chinese-remainder round trips on all 15 inputs in their respective domains. The incompatible controls fail for the predicted mathematical reasons.

This recovers standard algebra as a worked witnessed-assembly pattern. It does not establish automatic discovery of Cardano's formula, a new theorem about these problems, or an isomorphism between the exploratory 3D shape and a 2-Segal system. The geometric constructor conjecture remains separate from the algebra verified here.

## Durable verification

- Checker: `research/voevodsky/checkers/check_cardano_crt_witnessed_assembly.py`.
- Reproduction: `python research/voevodsky/checkers/check_cardano_crt_witnessed_assembly.py` (standard library only).
- Result: `research/voevodsky/results/cardano_crt_witnessed_assembly.json`; 13 checks passed, including the deliberate incompatibilities.
- Related geometric conjecture: `research/voevodsky/central-cell-surface-square-filler-conjecture.md`.
- Allocation: 4310, claim `seqclaim-055bc8a13fdfb5f450d4d79f`.
- Graph admission: proposal `ep_647b2a25-5737-4bb2-bbd6-0e066f66faab`, ledger head `e987e5efd3c7573bc32c3ab2ba029884d5ca88701d2123836abc0daca9f07ef7`.
- Website validation: `pnpm run build`; build status reported with delivery. No Git commit or deployment is included.
