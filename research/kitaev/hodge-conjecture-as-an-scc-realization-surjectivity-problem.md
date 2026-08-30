# The Hodge conjecture as an SCC realization-surjectivity problem

## Scope

Let \(X\) be a smooth projective complex variety and let \(p\ge 0\). Define

\[
\operatorname{cl}_{X,p}:CH^p(X)_{\mathbf Q}\longrightarrow
\operatorname{Hdg}^p(X):=
H^{2p}(X,\mathbf Q)\cap H^{p,p}(X).
\]

This packet formalizes the conjecture without treating Hodge type as authority for algebraic realization.

## SCC objects

| Role | Object |
|---|---|
| source constructors | codimension-\(p\) algebraic cycles modulo rational equivalence |
| constructor quotient | \(CH^p(X)_{\mathbf Q}\) |
| observation carrier | \(H^{2p}(X,\mathbf Q)\) |
| type observer | projection to \(H^{p,p}(X)\) |
| admissible observed sector | \(\operatorname{Hdg}^p(X)\) |
| realization arrow | \(\operatorname{cl}_{X,p}\) |
| realization fiber over \(h\) | \(\operatorname{cl}_{X,p}^{-1}(h)\) |

The cycle-class map is source-authorized. Membership in the rational \((p,p)\) sector is an observational necessary condition. It does not construct a preimage.

## Three independent coherence gates

1. Hodge-type coherence: \(h\in H^{p,p}(X)\).
2. Coefficient coherence: \(h\in H^{2p}(X,\mathbf Q)\).
3. Constructor realization:

   \[
   \exists Z\in CH^p(X)_{\mathbf Q},
   \qquad \operatorname{cl}_{X,p}(Z)=h.
   \]

The first two gates define the target sector. The third asks whether its realization fiber is inhabited.

## SCC statement

The rational Hodge conjecture is

\[
\operatorname{im}\operatorname{cl}_{X,p}=\operatorname{Hdg}^p(X)
\]

for every smooth projective complex \(X\) and every \(p\). Equivalently, every SCC realization fiber over an admissible rational Hodge observation is nonempty.

This is an open constructor cell. SCC may verify its typing, naturality, and known instances, but coherence alone does not authorize the missing inhabitants.

## Naturality cells

For every admitted morphism for which the operation is defined, require

\[
\operatorname{cl}(f^*Z)=f^*\operatorname{cl}(Z),
\qquad
\operatorname{cl}(f_*Z)=f_*\operatorname{cl}(Z),
\]

and

\[
\operatorname{cl}(Z\cdot W)=
\operatorname{cl}(Z)\smile\operatorname{cl}(W).
\]

These cells constrain a realization arrow. They do not prove its surjectivity.

## Closed fixture: the Lefschetz \((1,1)\) theorem

For \(p=1\), the exponential sequence supplies the comparison

\[
\operatorname{Div}(X)\longrightarrow
\operatorname{Pic}(X)\xrightarrow{c_1}
H^2(X,\mathbf Z)\cap H^{1,1}(X).
\]

The realization map is surjective onto integral \((1,1)\)-classes. In SCC terms, the codimension-one realization fiber is inhabited because line bundles provide a complete intermediate constructor.

This fixture must not be generalized merely by replacing line bundles with higher-rank bundles or sheaves. No corresponding higher-codimension surjectivity theorem is known.

## Hostile fixture: the integral Hodge statement

The map

\[
CH^p(X)\longrightarrow
H^{2p}(X,\mathbf Z)\cap H^{p,p}(X)
\]

need not be surjective. An integral class can therefore pass the type and coefficient observers while its algebraic-cycle realization fiber is empty.

This falsifies the rule “observer-compatible implies constructor-realizable” and demonstrates that coefficient lens is part of the constructor theory.

## Kernel discipline

The conjecture concerns the image of the cycle-class map, not its kernel. Distinct cycles can have the same cohomology class. Therefore:

- cohomological equality is not constructor equivalence;
- injectivity is neither claimed nor required;
- a realization witness is a preimage, not a canonical inverse;
- uniqueness requires a stronger equivalence theory and is outside the conjecture.

## SCC profile

| Axis | Current status |
|---|---|
| carrier | compatible |
| action | typed by pullback, pushforward, and product where admitted |
| observation | Hodge-type and rationality observers defined |
| realization | closed for \(p=1\), open in general over \(\mathbf Q\), false in general over \(\mathbf Z\) |
| completion/estimate | not the generic missing gate |

The profile records certification strength only. It does not promote an open realization fiber.

## First-failure order

For a proposed realization, SCC should test:

1. smooth projective source typing;
2. codimension and cohomological degree;
3. rational coefficient typing;
4. Hodge type \((p,p)\);
5. source authority of the proposed algebraic cycle;
6. equality of its cycle class with the target;
7. naturality under every declared comparison.

Failure before step 5 is an observation/type obstruction. Failure at steps 5–6 is the missing realization constructor. Failure at step 7 is a coherence defect in a proposed realization family.

The adjacent TOML contract records the rational open cell, the Lefschetz closed fixture, and the false integral hostile without asserting the Hodge conjecture.

