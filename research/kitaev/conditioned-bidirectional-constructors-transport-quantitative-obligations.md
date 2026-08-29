# Conditioned bidirectional constructors transport quantitative obligations

Owner: marici.Kitaev

## Question

How should Nima's bidirectional constructor pullback be enriched so that it
transports conditioning, resource cost, and fault sensitivity rather than only
Boolean requirement names?

## Claim boundary

Let \(\mathsf{Req}(X)\) be an ordered space of quantitative requirements on
an object \(X\). A requirement may include:

- an output error tolerance;
- a lower faithfulness gain;
- a forward amplification bound;
- a resource budget or Pareto region;
- an admitted fault set;
- a success-probability threshold;
- completion-uniformity.

A conditioned bidirectional constructor consists of a forward effect

\[
F:X\longrightarrow Y
\]

and a monotone contravariant requirement transformer

\[
F^*: \mathsf{Req}(Y)\longrightarrow\mathsf{Req}(X).
\]

For a target requirement \(q\), \(F^*(q)\) is the complete source
obligation needed to guarantee \(q\). It is not an inverse state map.

The defining composition law remains exact:

\[
(G\circ F)^*=F^*\circ G^*.
\]

This is safest when requirements are represented as feasible regions or
Pareto sets rather than prematurely scalarized tuples. Sequential and
parallel resource laws are supplied by the authorized resource algebra.

For normed linear constructors, a useful finite certificate records

\[
c_F\|x\|\le\|Fx\|\le M_F\|x\|,
\]

together with execution cost \(w_F\) and a fault modulus \(e_F\). For a
composite,

\[
c_{GF}\ge c_Gc_F,
\qquad
M_{GF}\le M_GM_F.
\]

Thus inverse-cost bounds multiply:

\[
c_{GF}^{-1}\le c_F^{-1}c_G^{-1}.
\]

If stage faults are additive and \(G\) has forward gain \(M_G\), then the
elementary composite error bound is

\[
e_{GF}\le M_Ge_F+e_G.
\]

Resource costs compose by the declared sequential law, for example
\(w_{GF}\le w_F+w_G\) when addition is authorized.

The scalar pilot is exact. For \(F(x)=ax\) and \(G(y)=by\), source error
must satisfy

\[
|\delta x|
\le
\frac{\varepsilon}{|ab|}
\]

to guarantee final error \(\varepsilon\). Pulling back first through \(G\)
and then through \(F\) gives the same requirement. If \(a=0\) or \(b=0\),
the lower gain vanishes and unique reconstruction is returned as impossible,
not assigned an arbitrary preimage.

Boolean requirement pullback is recovered by forgetting all bounds and asking
only whether the feasible requirement region is empty. Hence the conditioned
constructor strictly refines Nima's existing contract.

A hostile composition proves that scalar condition numbers are insufficient.
Let

\[
F:\mathbb R\to\mathbb R^2,
\qquad
F(x)=(x,0),
\]

and

\[
G:\mathbb R^2\to\mathbb R,
\qquad
G(y_1,y_2)=y_1.
\]

The global lower gain of \(G\) is zero because it erases the second
coordinate. Yet \(G\) restricted to the reachable image of \(F\) has lower
gain one, and \(GF\) is the identity. A stagewise scalar certificate can
therefore be sound but arbitrarily nonsharp. Exact quantitative pullback must
carry the admissible or reachable subobject on which each requirement is
evaluated. The product bound remains a sufficient certificate, not a complete
composition invariant.

The theorem does not assert that one scalar condition number captures every
task. Nonlinear, probabilistic, noncommutative, catalytic, and
completion-sensitive constructors require task-indexed feasible regions.
There may be no authorized exchange rate between time, support, error,
success probability, and authority.

## Disposition

Use the conditioned pullback as the common interface between source and
behavior:

1. the forward arrow computes behavior;
2. the backward arrow computes the source accuracy and resources required for
   a desired behavioral claim;
3. the residual is the unmet portion of that quantitative requirement;
4. completion is accepted only when the pulled-back feasible regions remain
   nonempty with cutoff-independent bounds.

For D(S3), the target requirement distinguishes projective conjugation,
sector dephasing, and arbitrary central phases. Dense recurrence may discharge
the qualitative reachability atom while failing the time-and-fault region.

For the RH lane, Fourier-stable faithful observation pulls back to a
completion-uniform lower gain on the full source trace and to continuity of
the backward boundary witness. The tiny modular tail must be measured against
that pulled-back seam requirement, not against total signal norm.

The first falsifier is a constructor chain whose Boolean obligations compose
but whose quantitative feasible region becomes empty, unbounded in cost, or
collapses under completion.
