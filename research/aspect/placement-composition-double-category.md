# Placement and composition as two categorical directions

## Question

How should joint instrument placement be separated from ordered transformer composition, and when does their interchange require extra interaction data?

## Claim boundary

This packet gives a double-categorical typing discipline. Horizontal and vertical directions denote placement and composition order, respectively. Neither direction has physical-time meaning without a source-derived map to a physical-time object.

## Two directions

Use a double category or suitable pseudo-double category \(\mathbb I\):

- objects are typed boundary or continuation-state interfaces;
- horizontal arrows are occurrence-preserving placements or juxtaposition interfaces;
- vertical arrows are instrument transformers with declared input and output interfaces;
- squares are compatibility cells between placement and transformer composition.

Horizontal composition

\[
p\odot q
\]

forms a joint placement. It retains the two occurrence identities and all incidence needed to tell them apart. It need not be symmetric: a symmetry cell is admitted only when supplied by source geometry.

Vertical composition

\[
g\circ f
\]

connects the output continuation interface of \(f\) to the input continuation interface of \(g\). It is defined only when those interfaces agree or are connected by a declared transport map.

## Interchange

Given four compatible squares, strict interchange has the form

\[
(g_1\odot g_2)\circ(f_1\odot f_2)
=
(g_1\circ f_1)\odot(g_2\circ f_2).
\]

In a pseudo-double category, replace equality by a specified invertible interchange cell satisfying coherence. The formula is justified only for componentwise independent transformers whose horizontal product exists.

## Joint interactions

A transformer

\[
J:X_1\odot X_2\to Y_1\odot Y_2
\]

is separable when it factors as

\[
J=J_1\odot J_2.
\]

If no such factorization exists, interchange cannot reduce \(J\) to independent vertical arrows. The attachment must contain a genuine joint interaction cell with its own source, target, incidence, and coherence equations.

Thus a common target type or matching dimensions do not establish separability. Factorization is a testable property of the typed transformer.

## Continuation and placement coherence

For a placement square, each horizontal boundary map must commute with the vertical continuation maps. This square condition ensures that transporting a placed state and then applying instruments agrees with applying the component maps and then placing the results, up to the admitted coherence cell.

Failure has three distinct forms:

1. boundary mismatch, so vertical composition is undefined;
2. missing interchange cell, so both composites exist but are not identified;
3. nonseparable interaction, so no componentwise decomposition exists.

These failures must not be repaired by treating an ordering index as physical time.

## Finite diagnostic

On bit states, horizontal product is Cartesian pairing and vertical arrows are unary bit functions. Exhaustive evaluation verifies strict interchange for every pair of componentwise unary transformers.

The joint map

\[
J(a,b)=(a,a\mathbin{\mathrm{xor}}b)
\]

cannot factor as \((u(a),v(b))\): its second output depends on both inputs. Exhaustive search over all unary bit functions rejects every proposed factorization. The map is valid only as a joint interaction cell, not as horizontal composition of independent instruments.

## Disposition

Joint placement and transformer composition are independent categorical directions. Interchange holds for typed componentwise products, strictly or through declared coherence. Nonseparable transformers require explicit joint interaction cells. No direction acquires physical-time semantics from this construction.
