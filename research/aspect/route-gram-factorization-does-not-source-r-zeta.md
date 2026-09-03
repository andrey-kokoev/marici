# Route-Gram factorization does not source the radial intertwiner

## Question

Can a complete-route factorization \(Q=B^*B\) produce the independently derived common core and radial intertwiner required by the unbounded mixed-bridge theorem?

## Claim boundary

No. The factorization starts from a closed or closable route map \(B\) with a declared domain. It can recover the positive form \(Q\), but it cannot construct a different map \(R_\zeta\), a second route map \(C\), or a common invariant core on which \(CR_\zeta=B\).

Defining

\[
R_\zeta=C^{-1}B
\]

would require an independently established inverse with the correct domain and range. Without those data it merely inserts the desired identity.

## Discriminating obstruction

If independently sourced candidates \(B,C,R_\zeta\) and a common core \(\mathcal D\) become available, define the route-Gram residual

\[
\Delta(v,w)=
\langle Bv,Bw\rangle-
\langle CR_\zeta v,CR_\zeta w\rangle,
\qquad v,w\in\mathcal D.
\]

Any nonzero value disproves \(CR_\zeta=B\), and even disproves equality up to a target isometry. The kernel implication

\[
\ker(R_\zeta|_{\mathcal D})\subseteq\ker(B|_{\mathcal D})
\]

is another necessary test.

Vanishing of \(\Delta\) is not sufficient for the desired identity. Equal Gram forms imply at most a partial isometry between the closures of the two route ranges. For example, \(B=I\) and \(CR_\zeta=-I\) have identical Gram forms but are unequal. One still needs a source-derived target-frame identification, domain equality, closure compatibility, and the literal intertwining law.

## Domain obstruction

The formal intersection

\[
\mathcal D(B)\cap R_\zeta^{-1}\mathcal D(C)
\]

is not an independently derived common invariant core. It may be nondense, fail to be a form core, or fail invariance. Naming this intersection does not discharge the radial source gate.

## Disposition

The Aspect route factorization cannot fill the first missing radial object identified in `research/voevodsky/r-zeta-source-adequacy-audit.md`. It does provide a bounded falsifier once independent candidates exist: a nonzero route-Gram residual or failed kernel inclusion rejects the proposed bridge before closure and coercivity analysis. Zero residual only advances the candidate to the separate partial-isometry and domain tests; it does not verify \(CR_\zeta=B\).
