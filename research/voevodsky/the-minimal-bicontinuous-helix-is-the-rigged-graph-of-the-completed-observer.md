# The minimal bicontinuous helix is the rigged graph of the completed observer

## Question

After unweighted history topology fails to support continuous reconstruction,
what is the minimal topology in which the faithful completed observer becomes a
reversible presentation change?

## Graph presentation

Let

\[
E_k=\mathcal C_{k,\exp}
\]

be the projective source and let

\[
\mathcal O_k=(\widehat B_k,\widehat Z_k):E_k\to H_k\oplus Z_k
\]

be the continuous faithful completed observer. Define its graph

\[
\Gamma_k=
\{(c,\mathcal O_kc):c\in E_k\}
\subseteq E_k\oplus H_k\oplus Z_k.
\]

Equip \(\Gamma_k\) with the subspace topology. Since \(\mathcal O_k\) is
continuous, the graph map

\[
g_k:E_k\longrightarrow\Gamma_k,
\qquad c\longmapsto(c,\mathcal O_kc)
\]

is continuous. Its inverse is the restriction of the first projection, hence
is continuous. Therefore

\[
\boxed{g_k:E_k\xrightarrow{\cong}_{\rm top}\Gamma_k}
\]

is a bicontinuous linear equivalence.

No closed-range estimate in the unweighted history norm is required: the graph
retains the source projective coordinate that the smoothing observation cannot
uniformly reconstruct.

## Minimal rigging statement

Equivalently, place on the realized observer image

\[
I_k=\operatorname{im}\mathcal O_k
\]

the transported seminorms

\[
p_{k,\delta}(x)=q_{k,\delta}(\mathcal O_k^{-1}x).
\]

Then

\[
\mathcal O_k:E_k\to I_k^{\rm rig}
\]

is a topological isomorphism. This is the smallest presentation topology that
simultaneously:

1. preserves all source projective seminorms;
2. makes the complete observer coordinates available;
3. makes reconstruction continuous.

It is not the subspace topology inherited from \(H_k\oplus Z_k\). The escaping
forest-edge sequence proves that the transported topology is strictly stronger.

## Successor transport

Suppose the source stage map

\[
U_k:E_k\xrightarrow{\cong}E_{k+1}
\]

is bicontinuous. Its graph lift is forced:

\[
\widetilde U_k
=g_{k+1}U_kg_k^{-1}:
\Gamma_k\xrightarrow{\cong}\Gamma_{k+1}.
\]

Explicitly,

\[
\widetilde U_k(c,\mathcal O_kc)
=
(U_kc,\mathcal O_{k+1}U_kc).
\]

This map is automatically bicontinuous and satisfies the observation square

\[
\operatorname{obs}_{k+1}\widetilde U_k
=
\mathcal O_{k+1}U_k g_k^{-1}.
\]

If an independently defined target transport \(T_k:H_k\oplus Z_k\to
H_{k+1}\oplus Z_{k+1}\) exists, preservation of the realized observer image is
exactly the nontrivial equation

\[
T_k\mathcal O_k=\mathcal O_{k+1}U_k.
\]

Only under this equation does \(T_k|_{I_k}\) equal the conjugated successor.
Thus graph lifting constructs the canonical candidate but does not manufacture
the analytic seam-naturality theorem.

## Four-phase helix

Retype the fourth presentation as \(\Gamma_k\), or equivalently as the rigged
image \(I_k^{\rm rig}\). If the other three presentation changes are
bicontinuous equivalences on compatible rigged objects, define one-phase
transport \(\tau\) around the four presentations. The full turn then obeys

\[
\tau^4\simeq\widetilde U_k.
\]

Since \(\widetilde U_k\) is conjugate to \(U_k\), it is invertible precisely
when the source stage transport is invertible. Information loss from scalar or
unweighted trace observation no longer decides monodromy.

## Relation to prior repository results

- Completed history plus the cycle port gives algebraic faithfulness.
- Grade-refining greedy forests have bicontinuously equivalent projective cycle
  coordinates.
- Ratio-normalized blocks have strict labelwise comparisons and reciprocal
  forest-presentation transport.
- Unweighted history has approximate kernels, forcing the stronger rigging used
  here.

Together these results support a presentation **groupoid of rigged observer
graphs**, rather than one canonical Hilbert trace space.

## Remaining source theorem

The next nonformal gate is to identify the actual \(k\)-successor \(U_k\) and
prove:

1. \(U_k\) and its inverse preserve every projective source seminorm up to
   finite seminorm shift;
2. the completed history and invariant cycle ports obey the displayed
   naturality equation;
3. the four local presentation equivalences and tetrahedral fillers lift to the
   graph groupoid;
4. the resulting degreewise phase operator satisfies \(\tau^4=\widetilde U\).

## Verdict

A topologically reversible presentation already exists canonically as the
rigged graph of the faithful completed observer. What remains open is whether
the source-authorized stage/seam dynamics act bicontinuously and naturally on
that graph. The topology problem and the dynamics problem are therefore
separated cleanly.
