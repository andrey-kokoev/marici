# Faithful Recovery Needs a Source Transversal

## Question

When does a section of a boundary quotient recover prior Carrier state rather
than prepare a convenient replacement?

## Two recovery notions

Let

\[
q:X\to Y
\]

forget an interface coordinate, and let \(j:Y\to X\) be a section with
\(qj=\operatorname{id}_Y\).

**Physical recovery on a source domain \(A\subseteq X\)** requires

\[
jq|_A=\operatorname{id}_A.
\]

Equivalently, \(q\) is injective on \(A\) and \(j\) is the inverse of that
restriction. The source domain must be established independently of the
decoder.

**Predictive recovery for a frozen experiment family** requires only

\[
jq(x)\equiv_{\mathrm{pred}}x,
\qquad x\in A.
\]

This may hold even when physical recovery fails. It authorizes substitution
for that experiment family, not a claim that the erased state returned.

## Exact two-bit hostile

Take

\[
X=\{(s,m):s,m\in\{0,1\}\},
\qquad
q(s,m)=s,
\qquad
j(s)=(s,s).
\]

On the full source \(X\), \(jq\) fails for \((0,1)\) and \((1,0)\). The
section is not physical recovery.

Now suppose the source independently proves the diagonal law

\[
A=\{(0,0),(1,1)\}.
\]

Then \(q|_A\) is bijective and \(j\) is its exact inverse. The same map has
become faithful because the source removed the fiber ambiguity before recovery.

The direction of explanation matters. Choosing \(j(s)=(s,s)\) and then
declaring its image to be the source would be circular. A faithful recovery
theorem needs the source-derived transversal first.

## Predictive but nonphysical recovery

If every admitted future Task and record sees only \(s\), then all states in a
fiber of \(q\) are predictively equivalent. Every section is a valid predictive
representative selector. Different sections can therefore be equally adequate
for the frozen behavior while preparing physically different memories.

Once memory recall is admitted, the fiber classes split. No one-bit decoder
can recover both members of a fiber. Predictive recovery fails on the full
source, even if it passed every earlier system-only test.

## Recovery certificate

A Marici recovery claim must state:

1. source domain and interface boundary;
2. forgotten map \(q\) and proposed lift \(j\);
3. whether the claim is physical or predictive recovery;
4. for physical recovery, a source-derived proof that \(jq\) is identity on
   the admitted domain;
5. for predictive recovery, the complete frozen continuation/test family and
   proof that \(jq(x)\) is predictively equivalent to \(x\);
6. the enlargement conditions under which the certificate expires;
7. provenance of any newly prepared or externally supplied fiber coordinate.

Matching a calibration sample, satisfying \(qj=\operatorname{id}\), or
reproducing current records proves only consistency with the visible quotient.

## Control interpretation

This is the distinction between exact state reconstruction and an observer
state sufficient for future outputs. A minimal observer need not reproduce the
plant's hidden physical state. It need only generate correct future records
under the declared inputs. Calling that internal observer state “recovered
plant state” is an unjustified strengthening unless an injectivity theorem is
available.

The source transversal plays the role of an observability section whose
uniqueness is forced by the plant domain, not chosen by the estimator.

## Deutschian pressure

A recovery explanation must say why the missing coordinate was determined by
the retained one. The section itself cannot answer that question; every
surjection admits possible choices on its fibers. The explanatory content is
the source law making exactly one choice admissible.

## Verification boundary

The dependency-free checker verifies failure on the full source, exact
recovery on the independently stated diagonal, predictive adequacy for the
system-only family, and failure after memory recall. This is a finite exact
recovery classification, not a noisy or quantum recovery theorem.
