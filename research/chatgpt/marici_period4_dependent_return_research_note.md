# A 4.5-tuple as a witnessed four-periodic orbit

**Research note · 2026-10-27**  
**Status:** General mathematical derivation; independently rerun finite/model checks. Cubical Agda candidate prepared but **not typechecked**.  
**Programme:** Marici — one-witness-at-a-time generation, return coherence, retained history.

## 1. Hypothesis and typing

Proposed primitive: `[a, b, c, d, a′]`, where the final component is not an independent fifth state but **a witness of return to the first state**.

There are two distinct interpretations of the expression `a * b * c * d ≈ a`:

- **Iterated successor (tested here):** for a given function `G : S → S`, take `b = G a`, `c = G b`, `d = G c` and `a′ : G d ≡ a`. The resulting dependent type is

  \[
  \operatorname{Per}_4(G) := \sum_{a:S}\bigl(G^4(a)\equiv a\bigr).
  \]

  The four intermediate positions are recoverable from `a` and `G`; the actual return proof is retained as data. This is the *homotopy equalizer* of `G⁴` and the identity.

- **Four independently supplied factors:** `a′ : a*b*c*d ≈ a`. The iterated-successor theorem below does **not** apply without a separately established relation between cyclic permutation and the `*` operation, and a transport/congruence action on `≈`. If `a′` merely names a proposition rather than a proof inhabiting it, no witnessed return has been supplied.

The equality-path interpretation is a **mathematical candidate**, not a claim that Marici's free directed occurrences are identity paths.

## 2. Canonical shift and four-shift return

Let `F := G⁴`. Define one shift on the dependent return record:

\[
\sigma(a,p) := \bigl(G(a),\operatorname{ap}_{G}(p)\bigr),
\qquad p:F(a)\equiv a.
\]

`G` and `F` commute definitionally as iterates of the same function, so this is well typed: `G(F(a)) = F(G(a))`.

Applying the same shift four times gives, up to the standard functoriality equalities,

\[
\sigma^4(a,p)=\bigl(F(a),\operatorname{ap}_{F}(p)\bigr).
\]

**Proposition (dependent four-shift return).** For every `G : S → S` in a type with identity paths, there is a specified homotopy

\[
\boxed{\quad\sigma^4\simeq\operatorname{id}_{\operatorname{Per}_4(G)}.\quad}
\]

**Proof argument.** The base component of the required dependent-pair path is `p : F(a) ≡ a`. The family over the base is `P(z) := (F(z) ≡ z)`. Transport of `ap_F(p)` along `p` evaluates to

\[
\operatorname{transport}^{P}(p,\operatorname{ap}_{F}(p))
=\operatorname{ap}_{F}(p)^{-1}\cdot\operatorname{ap}_{F}(p)\cdot p
=p.
\]

Thus the base path `p` and the equality of its dependent witnesses define a path in `Σ a, F(a) ≡ a`. No proof-irrelevance or set-truncation hypothesis is used. This proves return of the **complete dependent pair up to a path**, not literal fiberwise equality of `ap_F(p)` and `p`.

**Scope:** A homotopy `σ⁴ ~ id` does not by itself certify every higher compatibility law of a coherent `C₄`-action. The compatibility of that homotopy with additional shifts remains to be formalized.

## 3. Nontrivial checks of dependent transport

### Circle homotopy-groupoid control

Let `S = S¹` and let `G(z) = z²`; then `F = G⁴` has degree 16 and fixes basepoint `1`. A return path `p : F(1) ≡ 1` with winding number `k` transforms after four shifts to a raw path with winding number `16k`. For `k ≠ 0`, these are different loops at the same basepoint.

Nonetheless, the required dependent transport along the base loop of winding `k` sends `16k` back to `k`:

\[
16k-16k+k=k.
\]

The finite/model checker confirmed this for 19 tested winding numbers; 18 changed as raw loops. This demonstrates why **equality of dependent records** must not be replaced by equality of witnesses at a fixed basepoint.

### Noncommutative control

A `D₅` groupoid model transports loops by conjugation. The same dependent-return identity was checked for all 10 elements; five raw witnesses changed after four shifts. This guards against relying on commutativity of loop composition. These are mathematical groupoid calculations, not proof-assistant certificates.

## 4. Binding to Marici's six-arrow source

The actual source in [`ActualSeedEndpointTable.agda`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda) has vertices `A,B,C,D` and directed occurrences `AB, BC, CA, AD, DB, BA`.

Exact enumeration found **six rooted four-arrow closed histories**, organized into **two cyclic orbits** of sizes **two** and **four**. A selected four-cycle is

\[
A\xrightarrow{AD}D\xrightarrow{DB}B\xrightarrow{BC}C\xrightarrow{CA}A.
\]

The corresponding deterministic successor `A→D→B→C→A` uses actual primitive occurrences, but **its selection is additional data**: the original source also admits other outgoing arrows at some vertices.

The proposed Agda fixture `FourPeriodSeedWitness.agda` defines this selected `next`, its `next⁴` equality, the corresponding `Per4`, a shift, and an explicit nonempty free-path cycle. It has **not** been compiled. See [`SeedSeamPathComparisonBoundary.agda`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda) for the retained free-path datatype.

## 5. Essential obstruction: return is not history erasure

The actual Marici free-path record includes each primitive occurrence. If a full state is `(activeVertex, history)` and one execution appends one event, then four executions change history length from `n` to `n+4`. No finite history-bearing state is literally periodic under that update.

The correct history-preserving variant separates the **active reference being compared** from the **retained history witnessing return**:

\[
\sum_{a,t:S}\ \sum_{h:\operatorname{History}_4(a,t)}
\operatorname{ReturnCompare}\bigl(\pi(t),\pi(a);h\bigr).
\]

The reference map `π`, comparison relation, and any transport on its proofs must be source-defined. In particular, `π(t) ≈ π(a)` does not entitle us to erase `h` or identify distinct histories.

## 6. Negative control for independent products

In the commutative monoid `ℤ/5` under addition, take `(a,b,c,d)=(3,1,2,2)`.

\[
a+b+c+d=3=a\pmod5,
\]

but after cyclic permutation the same sum remains `3`, which is **not** the new first component `b=1`. Thus a single relation `a*b*c*d≈a` does not yield a shifted return relation by associativity or commutativity alone.

## 7. Evidence and proof status

- **Rerun in the current environment:** `python /mnt/data/marici_period4_witness_test.py` completed successfully and wrote `/mnt/data/marici_period4_witness_results.json`.
- **Verified by finite/model checks:** six rooted four-arrow histories, two cyclic orbits, history-length obstruction, additive-product counterexample, 19 circle winding tests and 10 `D₅` groupoid tests.
- **Mathematical argument provided, not newly typechecked:** the general dependent-pair homotopy `σ⁴ ~ id`.
- **Unverified Agda candidate:** `FourPeriodSeedWitness.agda` (source-selected finite case); no new safe Cubical Agda compilation has occurred.
- **Not established:** a unique source-selected `G`; a universal `≈`-based cyclic shift; a coherent `C₄`-action with all higher laws; a native proof-producing return operation on full histories; any emergent spatial dimension or physics interpretation.

## 8. Next minimal Agda obligations

1. In safe Cubical Agda, prove general `shift⁴ : (x : Per4 G) → shift (shift (shift (shift x))) ≡ x` using `ΣPathP`, with no `isSet` assumption.
2. State and check the next coherence law relating this four-shift homotopy to application of `shift` (the first higher equivariance square). Do not assume it from the previous proof.
3. Bind the theorem to the actual free-path source **without converting directed occurrences into equality paths**: keep the active return comparison and the entire four-occurrence history as separate typed fields.
4. Determine whether the source supplies a canonical successor selection and return comparison. If not, exhibit the missing input explicitly rather than importing an arbitrary map or filler as though generated.

**Research conclusion:** The 4.5-tuple can be represented as one selected four-step orbit plus one dependent return witness. In the equality-path model, a canonical shift exists and four shifts return to the same dependent orbit *up to higher equality*. Actual Marici retained histories do not become periodic merely because their visible endpoint returns.
