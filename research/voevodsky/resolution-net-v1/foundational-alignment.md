# Computation and mathematical composition: the foundational test

This redirects attention from wire verification to the common mathematical structure. It does not replace or alter the legacy engines.

## A checked connection

Let P be a type of interfaces, U/V witness-bearing unary/binary rules, and Resolve S the finite derivations with open inputs in the family S. Supply an interpretation A with operations for U and V.

The new safe Cubical module `agda/ResolutionNetInterpretation.agda` proves:

1. `fold`: an assignment of inputs extends to an interpretation of complete derivations.
2. `unique`: every interpretation respecting the input assignment and rule operations agrees pointwise with that extension.
3. `fold-bind`: interpreting after substitution equals interpreting the substituted computations and then the surrounding derivation.

In notation, with k supplying computations for open inputs:

    eval_f(bind_k(d)) = eval_(s ↦ eval_f(k(s)))(d)

This is the precise alignment available here: composition of computations and substitution of mathematical derivations use the same structure. Wires are not needed to state it. A fresh `agda --ignore-interfaces --transliterate` check passed; log: `results/agda-interpretation.log`.

This is the algebraic content of free term substitution for the specified indexed signature. The uniqueness proof is pointwise for operation-preserving maps; it does not establish contractibility of arbitrary higher homomorphism/coherence records.

## Why that is not yet the sought foundation

These theorems hold for ANY supplied unary and binary operations. They hold whether a unary instruction means increment, identity, or an operation we invented yesterday. Thus the substitution laws organize a signature; they do not select meaningful mathematical rules or generate a theory of computation from nothing.

The distinction is essential:

* primitive rule witnesses specify what is allowed;
* substitution explains how allowed constructions compose;
* an interpretation says what the constructions mean;
* directed reduction specifies how a particular execution proceeds.

Mathematical equality alone does not select an evaluation direction, schedule, cost model or authority to consume an external resource. The earlier net normalization theorem concerns finite administrative substitution, not termination of all programs or an implementation of arbitrary mathematical functions.

## Stronger candidate: dependent substitution

For genuinely dependent mathematics, later inputs can depend on values supplied to earlier inputs. A context is not just an independent list of colored ports. Substituting an earlier input must simultaneously substitute into the types and witnesses of later inputs.

The corresponding computational operation is not merely plugging two fixed-typed trees together: it is executing a computation whose result determines the next interface. Proof composition and computation would then coincide at the level of dependent context substitution. Equality evidence also acts by transport, and different paths need not act identically.

The current fixed unary/binary indexed closure does not by itself supply binding, dependent context formation, their substitution laws, or nontrivial path transport. Encoding such things into giant package labels is not a derivation of them and can conceal the very machinery we want to explain.

## Decisive next experiment

Construct one dependent interaction: first supply x : X, then supply evidence y : Y(x). Compose it with a continuation whose interface depends on both. Establish that mathematical substitution and computational composition are literally the same defined operation and prove its unit/composition laws.

Then replace a trivial family by a family with nontrivial transport (the reported circle double cover is a candidate). If the representation treats all equal endpoint packages as interchangeable and loses the transport action, reject the representation rather than patching the observer.

Resource-sensitive substitution and effectful interaction remain further tests, not automatic consequences. The target is a common compositional foundation, not a claim that every mathematical object is executable or that one tiny calculus already explains all computation.
