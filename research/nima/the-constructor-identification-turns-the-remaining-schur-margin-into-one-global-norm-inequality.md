# The constructor identification turns the remaining Schur margin into one global norm inequality

## Identifying the odd incidence family

Let

\[
J_{\mathrm{top}}e_p
=
d_p
=
W_{2\log p}-W_{\log p}
\]

be the established trace-class disagreement incidence, and let
\(J_{\mathrm{src}}\) be the completed ordered-history constructor.

The source-identification theorem

\[
J_{\mathrm{src}}=J_{\mathrm{top}}
\]

in the common relative Green quotient identifies the auxiliary odd incidence
vectors with the columns of one global operator. After the reciprocal
character reduction, write

\[
c_p=J_{\mathrm{src}}e_p=d_p.
\]

This equality is typed: it is not equality of raw carrier formulas.

## Resolvent loading operator

Let

\[
mathcal D_\pm
=
\bigoplus_p D_{p,\pm}
\]

on the prime-diagonal odd auxiliary carrier. Define

\[
K_\pm
=
\mathcal D_\pm^{\dagger/2}J_{\mathrm{top}}.
\]

Then the primewise Wronskian Schur scalar is

\[
q_{p,\pm}
=
\|K_\pm e_p\|^2.
\]

The exact local condition remains

\[
q_{p,\pm}<16a_p.
\]

A single global sufficient condition is

\[
\|K_\pm\|^2
<
16m_\nu^2
\]

for both reciprocal sheets, since \(a_p\ge m_\nu^2\).

Because both the theta coordinate and disagreement carrier are declared
prime-labelled orthogonal direct sums, \(K_\pm\) is block diagonal. Hence

\[
\|K_\pm\|^2
=
\sup_p q_{p,\pm}.
\]

There is no additional coherent-prime amplification at this stage. The global
norm is exactly the supremum of the primewise resolvent loadings.

The comparison with \(16m_\nu^2\) remains a sufficient uniform certificate,
because replacing \(a_p\) by its common lower bound may discard useful
primewise endpoint scale.

## Factorized bound

If

\[
M_D
=
\sup_{p,\pm}
\|D_{p,\pm}^{\dagger}\|
<\infty,
\]

then

\[
\|K_\pm\|^2
\le
M_D\|J_{\mathrm{top}}\|^2.
\]

Therefore the explicit sufficient margin is

\[
M_D\|J_{\mathrm{top}}\|^2
<
16m_\nu^2.
\]

Under the quarter-gap estimate

\[
D_{p,\pm}
\ge
\frac{\delta_{\mathrm{aux}}}{4}I,
\]

one may take

\[
M_D\le\frac4{\delta_{\mathrm{aux}}},
\]

and it is sufficient that

\[
\|J_{\mathrm{top}}\|^2
<
4\delta_{\mathrm{aux}}m_\nu^2.
\]

Every quantity in this inequality has an independent source meaning:

- \(\|J_{\mathrm{top}}\|\): disagreement incidence size;
- \(\delta_{\mathrm{aux}}\): reciprocal auxiliary gap;
- \(m_\nu\): primitive endpoint lower scale;
- the factor four: Wronskian quarter-column normalization.

## Exact versus sufficient tests

The global norm estimate discards two useful structures:

1. columns \(d_p\) become small with prime grade;
2. each \(d_p\) may avoid the soft spectral region of \(D_{p,\pm}\).

Hence failure of the factorized inequality does not imply failure of Schur
survival. The exact criterion is still

\[
\sup_{p,\pm}
\frac{
\langle d_p,D_{p,\pm}^{\dagger}d_p\rangle
}{
16a_p
}
<1.
\]

The factorized bound is the first cheap certificate.

## Trace-class consequence

Because \(J_{\mathrm{top}}\) is trace class and
\(\mathcal D_\pm^{\dagger/2}\) is bounded under the auxiliary gap,

\[
K_\pm
=
\mathcal D_\pm^{\dagger/2}J_{\mathrm{top}}
\]

is trace class. Consequently the odd Schur return

\[
J_{\mathrm{top}}^*
\mathcal D_\pm^{\dagger}
J_{\mathrm{top}}
=
K_\pm^*K_\pm
\]

is positive trace class.

This closes ideal-class availability once constructor identification and the
uniform reciprocal resolvent are proved. Trace class alone does not give the
strict loading margin.

## Logical order

The local programme now separates cleanly:

1. prove \(J_{\mathrm{src}}=J_{\mathrm{top}}\);
2. prove the reciprocal auxiliary gap;
3. evaluate the exact column ratios or the global norm certificate;
4. obtain the Wronskian Schur-survival margin;
5. retain mixed Pauli linking blocks for orientation;
6. proceed to global five-margin coercivity.

The norm inequality cannot authorize step one. Analytic smallness of
\(J_{\mathrm{top}}\) does not prove that it is the source Adams constructor.

## Minimal hostiles

1. The global norm certificate passes for \(J_{\mathrm{top}}\), but
   \(J_{\mathrm{src}}\ne J_{\mathrm{top}}\).
2. The common-lower-scale norm certificate fails although every sharper
   ratio \(q_{p,\pm}/(16a_p)\) remains uniformly below one.
3. The factorized quarter-gap bound fails although spectral alignment makes
   every exact resolvent loading small.
4. Trace-class return with largest diagonal loading reaching the endpoint
   budget.
5. One reciprocal sheet has a larger resolvent and violates the bound.

## Verdict

After reciprocal character selection, the first Adams constructor identity
does more than match two linear histories. It identifies the entire family of
odd Schur incidence vectors with the trace-class window disagreement operator.

The remaining local coercivity can then be certified by the single inequality

\[
\left\|
\mathcal D_\pm^{\dagger/2}J_{\mathrm{top}}
\right\|^2
<
16m_\nu^2,
\]

or by the sharper primewise spectral ratios. This is the shortest current
path from source identification to a completion-stable Adams edge.
