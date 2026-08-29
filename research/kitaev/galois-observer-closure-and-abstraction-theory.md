# Galois observer closure and abstraction theory

## Question

What common closure structure relates admitted experiments to operational indistinguishability, when does that closure become a probe matroid, and how should the 405-cell SCC lattice be typed as an abstraction of concrete constructor–observer systems?

## Claim boundary

The experiment–indistinguishability Galois connection is general after a source set and admitted experiment family are frozen. Representable matroid structure requires a fixed finite linear candidate family; it does not extend automatically to variable carriers, fault balls, or ordered constructor words.

The SCC account is an abstraction-theory proposal. The 405 profiles record certified guarantees but are not complete invariants of concrete behavior. Soundness requires every abstract promotion to be backed by concrete witnesses in one source-authorized context. Completeness generally fails and must not be inferred from passing finite examples.

## Disposition

### Internal Galois connection

Let (X) be a source state set and (E) a frozen family of admitted experiments, including authorized constructor precomposition. For (S\subseteq E), define the indistinguishability relation

\[
x\sim_S y
\iff
e(x)=e(y)\text{ for every }e\in S.
\]

For a candidate equivalence relation (R) on (X), define

\[
F(R)=\{e\in E:e\text{ is constant on every }R\text{-class}\}.
\]

Writing (K(S)=\sim_S), the antitone correspondence satisfies

\[
S\subseteq F(R)
\iff
R\subseteq K(S).
\]

Hence

\[
\operatorname{cl}_E(S)=F(K(S))
\]

is the complete admitted experiment theory with the same operational distinctions as (S), while

\[
\operatorname{cl}_R(R)=K(F(R))
\]

is the coarsest operational equivalence invisible to every admitted experiment compatible with (R).

If (E) is closed under precomposition by a constructor monoid \(\mathcal A\), every closed indistinguishability relation is constructor-stable. The operational domain is therefore a closed pair

\[
(\operatorname{cl}_E(S),K(S)),
\]

not an arbitrary probe list or kernel in isolation.

### Linear specialization and probe matroids

For a fixed finite linear candidate family \(E=\{e_1,\ldots,e_m\}\) over a field, with frozen base observer (B_0), define

\[
r(S)=
\operatorname{rank}
\begin{pmatrix}B_0\\ e_i:i\in S\end{pmatrix}
-\operatorname{rank}B_0.
\]

Then (r) is the rank function of a representable matroid on (E). Its closure is

\[
\operatorname{cl}(S)
=
\{e:r(S\cup\{e\})=r(S)\}.
\]

Minimal faithful augmentations are bases of the required quotient row space. Circuits are minimally redundant probe families. This justifies greedy or exact basis synthesis only in the fixed linear regime.

### Five replay geometries

The finite blind replay now types its closure geometry explicitly.

1. Toric logical commutator probes form a rank-4 representable matroid. Normalization, cardinality bound, monotonicity, and submodularity all pass exactly.
2. (D(S_3)) flux ports form a rank-2 partition matroid on the transposition and three-cycle conjugacy types. Endpoint-algebra dimension is a weight on its flats, not itself a matroid rank.
3. The 32 Boolean zeta rows form a free representable matroid of rank 32.
4. Replica detection and correction live in Hamming-code geometry because changing replica count changes the carrier and its fault balls.
5. Polarizer insertions form an ordered constructor-word semigroup because order matters and generators may repeat.

Thus the Galois closure is common, while the finite optimization geometry is coefficient- and constructor-sensitive.

### SCC as an abstract domain

Let \(\mathcal C\) be the class of concrete typed realization packets. Let

\[
\mathcal A_{\mathrm{SCC}}
=
\{\text{five scales}\}\times\{0,1,2\}^4
\]

with the four coordinates carrier, action, observation, and estimate. The abstraction map

\[
\alpha:\mathcal C\to\mathcal A_{\mathrm{SCC}}
\]

assigns the strongest profile actually certified by witnesses in the packet's authority context.

For a profile (a), define its concretization

\[
\gamma(a)=\{c\in\mathcal C:a\le\alpha(c)\}.
\]

For a set of packets (C\subseteq\mathcal C), the strongest common guarantee is

\[
\alpha_\cap(C)=\bigwedge_{c\in C}\alpha(c).
\]

Then

\[
a\le\alpha_\cap(C)
\iff
C\subseteq\gamma(a).
\]

This is the abstraction-level Galois correspondence: profiles describe common certified lower bounds, not complete realizations.

### Abstract transformers

For a concrete constructor or reconciliation operation (T), a sound abstract transformer (T^\sharp) must satisfy

\[
T(\gamma(a))\subseteq\gamma(T^\sharp(a)).
\]

The strongest universally sound profile is the meet

\[
T^\sharp(a)
=
\bigwedge_{c\in\gamma(a)}\alpha(Tc),
\]

restricted to packets for which (T) is source-authorized and typed. An undefined concrete operation remains undefined abstractly; it is not replaced by a low-confidence arrow.

Completeness at (c) would require

\[
\alpha(Tc)=T^\sharp(\alpha(c)).
\]

This generally fails. Toric loop probes, (D(S_3)) flux ports, Boolean scores, and reflection responses can occupy the same SCC profile while their constructor closures and future transformations differ. Therefore no transformer depending only on the 405 position can predict every concrete promotion exactly.

### Reduced-product abstraction

The next useful abstract state is not a larger ordinal lattice. It is a reduced product

\[
\mathcal A_{\mathrm{refined}}
=
\mathcal A_{\mathrm{SCC}}
\times
\mathcal A_{\mathrm{kernel}}
\times
\mathcal A_{\mathrm{strength}}
\times
\mathcal A_{\mathrm{closure}}
\times
\mathcal A_{\mathrm{authority}}.
\]

Its coordinates retain:

- SCC certification strength;
- kernel or partition type;
- Gramian spectrum, Smith profile, or typed replacement;
- matroid, Hamming, partition, or word-semigroup closure geometry;
- the source context in which joins and transports are authorized.

Consistency reduction removes impossible combinations. For example, observation grade `faithful` is inconsistent with a nonlegal behavioral kernel, and a parallel Gramian join is inconsistent with an ordered-word instrument lacking a common nondisturbing frame.

### Counterexample-guided refinement

An automatic resolver can now use a disciplined loop:

1. classify a packet in the coarse SCC domain;
2. apply only sound abstract gates;
3. concretely replay a proposed witness;
4. if the abstract verdict is spurious or incomplete, add the kernel, strength, closure, or authority coordinate exposed by the witness;
5. repeat until a concrete certificate or typed obstruction is obtained.

This is counterexample-guided abstraction refinement. It prevents two opposite errors: pretending that one SCC profile fixes a unique operational domain, and abandoning reusable abstraction merely because the first profile is incomplete.

### Falsifiers

1. A purported linear probe rank violates a matroid axiom.
2. A variable-carrier or ordered-word problem is solved by subset rank without an equivalence proof.
3. Two experiment families have the same kernel but different claimed Galois closures inside one frozen admitted (E).
4. An SCC promotion lacks a concrete witness in its source-authorized context.
5. An abstract transformer claims completeness for two same-profile packets with different concrete images.
6. A partial authority-sensitive join is replaced by an unconditional lattice join.
7. Refinement adds a solution-specific label rather than a reusable discriminating coordinate.
8. A concrete counterexample is discarded because the coarse abstract profile passed.

### Programme consequence

There are now two nested abstraction mechanisms:

\[
\text{experiments}
\rightleftarrows
\text{indistinguishability congruences}
\]

inside each realization, and

\[
\text{concrete realizations}
\rightleftarrows
\text{SCC guarantee profiles}
\]

across the programme. The first can be exact after the admitted experiment universe is frozen. The second is intentionally lossy. Automatic resolution is trustworthy when the target property is complete for the chosen refined abstraction; otherwise the compiler must return a witness-driven refinement request rather than a fabricated verdict.

Machine evidence: `research/kitaev/results/finite-observer-blind-replay.json`.
