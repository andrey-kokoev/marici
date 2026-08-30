# The first frontier is a prime-power-to-Mellin interface rewrite

## Frontier selection

The hierarchy is now stable enough to stop adding abstract margins. The next obligation is constructor-level:

> Build one source-authorized rewrite from a prime-power arithmetic generator to the complete Mellin/Green feature packet, preserving every external interface.

This is prior to coercivity and prior to spectral identification.

## Source and target constructors

For a prime power \(q=p^k\), let the arithmetic atom be
\[
\mathsf P(q;s)
\]
with typed ports for:

- prime label \(p\);
- grade \(k\);
- Mellin parameter \(s\);
- primitive, square, and connected incidence;
- cutoff inclusion;
- endpoint and archimedean boundary;
- Real and reciprocal-sheet action;
- source-energy version.

The analytic target is not a scalar Euler term. It is a feature packet
\[
\mathsf M(q;s)
=
\big(
\mathsf T,\mathsf S,\mathsf E,\mathsf A,
\mathsf R,\mathsf C,\mathsf X
\big)_{q,s},
\]
where the components carry tail, seam, endpoint, archimedean, reciprocal, connected, and mixed comparison data.

The proposed constructor is an oriented rule
\[
\rho_{q,s}:\mathsf P(q;s)\longrightarrow\mathsf M(q;s).
\]

## Required scalar shadow

Applying the terminal Mellin observer must recover the prime-power contribution
\[
\mathcal O_{\mathrm{Mellin}}\rho_{q,s}
=
w(q)\,q^{-s},
\]
with the exact source-derived coefficient \(w(q)\).

This scalar equality is only a necessary shadow. It does not define \(\rho_{q,s}\).

## Adams-weight transport law

If seam transport factors as
\[
\alpha:s\to t,\qquad \beta:t\to u,
\]
the positive coefficient must obey
\[
a(\beta\alpha)=a(\beta)a(\alpha),
\]
and the typed packet must satisfy the critical join
\[
\mathsf M(q;s)
\xrightarrow{\alpha}
\mathsf M(q;t)
\xrightarrow{\beta}
\mathsf M(q;u)
=
\mathsf M(q;s)
\xrightarrow{\beta\alpha}
\mathsf M(q;u).
\]

Equality here includes terminal port, orientation, phase/sign, endpoint labels, and reciprocal typing—not merely the numerical product.

## Cutoff naturality without an inferred retraction

For an authorized cutoff inclusion
\[
i_{X,X'}:\mathsf P_X(q;s)\to\mathsf P_{X'}(q;s),
\qquad X\le X',
\]
require
\[
\rho_{X',q,s}\,i_{X,X'}
=
I_{X,X'}\,\rho_{X,q,s}.
\]

No reverse arrow is available unless a cutoff retraction is separately constructed and admitted. Zero padding does not authorize one.

## Reciprocal and Real joins

Let \(\sigma:s\mapsto1-s\) be reciprocal-sheet transport and let \(\kappa\) denote the Real involution. The rewrite must furnish coherent joins
\[
\rho_{q,1-s}\,\sigma_P
\simeq
\sigma_M\,\rho_{q,s},
\]
and
\[
\rho_{q,\bar s}\,\kappa_P
\simeq
\kappa_M\,\rho_{q,s}.
\]

The two joins themselves must satisfy their mixed critical square. Otherwise reciprocal continuation and Real structure can agree separately but fail jointly.

## Boundary preservation

The external boundary of \(\rho_{q,s}\) must retain:

1. seam source and target fibers;
2. endpoint residue;
3. archimedean completion channel;
4. grade \(k\);
5. orientation and phase/sign;
6. observer-theory version;
7. source-energy version;
8. authorized gauge class.

The rule is inadmissible if any component is reconstructed only after applying a scalar observer.

## Termination orientation

Define a local measure
\[
\mu=
(n_{\mathrm{unresolved\ prime}},
 n_{\mathrm{untransported\ seam}},
 n_{\mathrm{unnormalized\ weight}},
 n_{\mathrm{unassembled\ boundary}}).
\]
The prime-to-feature rewrite must strictly reduce the first component and must not increase any earlier component through later normalization rules.

The global SCC measure must then be checked to refine this local measure. A local decrease is insufficient if an existing inverse rewrite recreates the prime atom.

## Prime-power overlap audit

The first finite certificate must resolve these overlaps:

- \(\rho_{q,s}\) with cutoff inclusion;
- \(\rho_{q,s}\) with moving-seam transport;
- \(\rho_{q,s}\) with Adams normalization;
- \(\rho_{q,s}\) with reciprocal transport;
- \(\rho_{q,s}\) with Real involution;
- \(\rho_{q,s}\) with endpoint extraction;
- \(\rho_{q,s}\) with archimedean attachment;
- \(\rho_{q,s}\) with primitive/square/connected splitting;
- \(\rho_{q,s}\) with Green packet assembly.

Every pair needs a common reduct or an authorized higher cell.

## Minimal finite theorem

For a finite cutoff \(X\), define the admitted prime set
\[
\mathcal Q_X=\{p^k\le X\}.
\]
The first theorem should prove:

> The family \(\{\rho_{q,s}:q\in\mathcal Q_X\}\) extends the closed SCC schema by a terminating, coherently confluent, interface-preserving rewrite system. Its Mellin observer has the prescribed Euler shadow, and its full normal forms retain all seam and completion channels.

This theorem says nothing yet about a uniform margin. It creates the one legitimate joint Green system on which margin estimates can subsequently be meaningful.

## Failure witnesses

The certificate should return the first typed failure:

- missing target feature;
- nondecreasing orientation;
- unjoined critical pair;
- cutoff drift;
- Adams semigroup failure;
- reciprocal/Real incompatibility;
- boundary-interface loss;
- scalar shadow mismatch.

Each witness identifies a constructor defect rather than an analytic estimate failure.

## Interface to the next two obligations

Once the finite rewrite theorem holds:

1. assemble the arithmetic and analytic restricted limits from the admitted normal forms;
2. compute the five margins without changing the constructor theory;
3. form the Green/Birman–Schwinger pencil;
4. prove an independent identification theorem relating eigenvalue \(1\) to the completed off-seam zero condition.

The identification theorem must cite the rewrite certificate and the five-margin certificate as hypotheses. It cannot manufacture either retrospectively.
