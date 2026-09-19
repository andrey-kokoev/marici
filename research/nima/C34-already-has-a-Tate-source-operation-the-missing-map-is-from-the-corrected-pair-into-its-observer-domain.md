# C34 already has a Tate source operation; the missing map is from the corrected pair into its observer domain

## Question

Is the first missing map an arithmetic-packet loading into `C34`?

## Claim boundary

That formulation is too strong. The relative `C34` feature already has an
independent source operation. For Mellin observers `g,h` its boundary
observation is

\[
q_{\mathfrak F}(g,h)
=
\sum_\chi\frac1{2\pi i}
\int \overline{m_{h,\chi}}m_{g,\chi}
\,\partial_s\log\gamma_\chi\,ds
+E_{\rm end}(g,h),
\]

and the local Tate identity identifies this with the Weil distribution

\[
W_S(g*h^*).
\]

Thus the independent arithmetic current is source-derived on the declared
Mellin test space. It does not need to be reconstructed from the retained prime
packet.

## Correct typing obstruction

The corrected pair source does not yet land in that test space. Its diagonal
coefficient has the meromorphic shell response

\[
\frac{\tau(z)A_{[a,b]}(z)}{\zeta-z},
\]

whereas the `C34` trace-class theorem assumes two-sided Schwartz localization
of the Mellin multiplier. Direct insertion is therefore undefined.

The missing map has type

\[
\Lambda_{\rm pair}:P_{\rm pair}
\longrightarrow E_{C34}^{\rm rig},
\]

where `E_C34^rig` must extend the observer domain to the pole--residue graph
without destroying trace-class or relative-trace control. On the ordinary test
core it must restrict to the existing Mellin representation.

## Acceptance test

A candidate extension must prove:

1. the pole coefficient and residue are separate observer coordinates;
2. the cross operator has a declared trace-class or renormalized-relative
   meaning before Xi specialization;
3. reciprocal exchange preserves the extended domain;
4. the residue remains Xi-exact;
5. the retained pair/source coordinate is not collapsed with that residue;
6. boundary evaluation agrees with `W_S(g*h*)` on the original test core.

## Disposition

Withdraw `D_ret^ar -> E_C34` as the first required map. The arithmetic current
already has Tate provenance. The first missing interface is the rigged observer
extension and corrected-pair map `Lambda_pair`; the independent bulk equality
remains downstream.