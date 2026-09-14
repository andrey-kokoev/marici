# Tate jet / primitive connection audit for the scalar-to-line lift

Date: 2026-09-08

## Question

Can the existing primitive-current connection or full Tate jet tower construct the completion-level scalar-to-boundary-line lift needed by the relative-null/multiobserver Beck–Chevalley cell?

## Findings

Prior research contains three distinct connection structures.

### 1. Determinant-line logarithmic connection

The primitive, square, connected-tail and archimedean currents assemble the logarithmic connection of the completed determinant section. This fixes the section, its divisor and multiplicities up to one source normalization. It does not lift the scalar determinant line to the full state/observer transport. The determinant functor forgets traceless shear, squeeze and rotation channels.

Source: `research/nima/a-source-logarithmic-connection-fixes-the-determinant-section.md` and `research/nima/rh-relative-connection-must-be-operator-valued-not-only-tate-scalar.md`.

### 2. Flat spectral jet connection

The source-derived connection

\[
\nabla_q=\partial_q+z,
\qquad
\nabla_z=\partial_z+q
\]

is flat and generates the complete triangular Tate jet ladder. It detects every zero and its multiplicity. It does not constrain the zero location. The same connection exists for hostile transforms with off-seam zeros.

Source: `research/grothendieck/theta-flat-spectral-jet-connection-detects-but-does-not-confine-the-divisor.md`.

### 3. Parallel endpoint-line connection

A regular connection making the distinguished endpoint section parallel would exclude off-seam zeros. But for a scalar section `F`, parallelization forces the coefficient `F'/F`, which has poles at its zeros. Constructing this coefficient from the scalar section is circular. A regular connection on the full state is also insufficient unless the endpoint covector spans an invariant dual line.

Sources: `research/nima/rh-off-seam-zero-is-forbidden-by-a-source-derived-regular-parallelism.md` and `research/nima/rh-regular-state-transport-needs-an-invariant-endpoint-line.md`.

## Verdict

Neither the primitive logarithmic connection nor the Tate jet tower supplies the missing lift. They determine and detect the Xi divisor but do not provide a regular operator-valued transport whose endpoint covector is invariant.

The exact missing datum is an operator-valued connection

\[
A(z):\mathcal V_z\to\mathcal V_z
\]

on the completed labelled source/observer state and a distinguished endpoint covector `ell(z)` satisfying

\[
\ell'(z)+\ell(z)A(z)=a(z)\ell(z)
\]

with `A` and `a` regular before scalar projection. It must also preserve the completed source domain, six-normal incidence, reflection, and positive observer margin.

## Finite falsifier

At each cutoff, compute the component of

\[
R_X(z)=\ell_X'(z)+\ell_X(z)A_X(z)
\]

transverse to `ell_X`. A nonzero component proves that the endpoint dual Krylov module has rank greater than one and rejects rank-one parallelism. Determinant or jet agreement cannot remove this residual.

## Consequence

The completion-level Beck–Chevalley construction cannot be completed from the existing scalar/jet connection data. The next evidence-bearing calculation is the endpoint dual-Krylov rank of the first source-authorized finite operator colligation—not another scalar connection or fitted `Xi'/Xi` form.
