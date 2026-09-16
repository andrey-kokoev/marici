# The scalar C14 evaluation makes the helical successor noninvertible before observer completion

## Question

For the four-phase helix with seam equivalence

\[
R_k:V_{4,k}\xrightarrow{\simeq}V_{1,k+1},
\]

is the induced stage successor

\[
S_k=R_k\circ C_{14,k}:V_{1,k}\longrightarrow V_{1,k+1}
\]

invertible?

## Type audit of C14

The original source-typed assignment defines

\[
V_1(S)=\mathcal A_S
\]

and

\[
C_{14}:h\longmapsto W_S(h)
=
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}(P_\Lambda\widehat P_\Lambda U_S(h)).
\]

At this typing, \(C_{14}\) is evaluation by one scalar linear functional. It is
not an equivalence between the test-function algebra and a presentation object.
There is also a nearby but different object-level datum: the entire functional
\(W_S(-)\). Mapping a presentation to that functional is not the same map as
evaluating it at one \(h\).

## Exact obstruction

Let \(K\) be the scalar field. If the admitted linear source space
\(\mathcal A_S\) has dimension at least two, then any linear map

\[
W_S:\mathcal A_S\to K
\]

has nontrivial kernel. Indeed, rank-nullity gives

\[
\dim\ker W_S
\geq
\dim\mathcal A_S-1.
\]

If \(W_S=0\), the kernel is all of \(\mathcal A_S\). If \(W_S\ne0\), choose
\(a\) with \(W_S(a)\ne0\). For any \(b\) independent of \(a\),

\[
h=W_S(a)b-W_S(b)a
\]

is nonzero and satisfies \(W_S(h)=0\).

The source algebra contains more than one independent test direction, so the
scalar C14 evaluation is not faithful. Since \(R_k\) is an equivalence,
composition with it neither removes nor creates the kernel:

\[
\ker S_k=\ker C_{14,k}.
\]

Therefore \(S_k\) is not invertible under the displayed scalar-evaluation
typing.

## Agreement with prior repository evidence

This obstruction is consistent with stronger existing audits.

- `all-translate-weil-kernel-faithfulness.md` distinguishes one scalar/zero
  slice from all-translate Gram data and from a dense faithful Weil family.
- `finite_sampled_traces_do_not_identify_all_jet_radial_response_20260911.md`
  gives an explicit nonzero polynomial invisible to twelve retained trace
  samples.
- `source_infinite_rank_forces_radial_trace_carrier_enlargement_20260911.md`
  uses a source-derived infinite-rank family to rule out faithful
  factorization through one fixed 26-coordinate trace carrier.

Thus the failure is not repaired merely by replacing one scalar with the
currently tested finite sampled packet.

## Maximal invertible quotient at one stage

The first isomorphism theorem gives the exact reversible shadow

\[
\overline C_{14,k}:
V_{1,k}/\ker C_{14,k}
\xrightarrow{\cong}
\operatorname{im}C_{14,k}.
\]

After the seam, this yields an invertible successor only on the observational
quotient/image:

\[
\overline S_k:
V_{1,k}/\ker C_{14,k}
\xrightarrow{\cong}
R_k(\operatorname{im}C_{14,k}).
\]

This quotient is generally too small to represent the source presentation: for
one nonzero scalar functional it is only one-dimensional.

## Candidate repair: complete observer-valued C14

Replace scalar evaluation by a source-authorized observer family
\(\{W_{k,\alpha}\}_{\alpha\in I_k}\):

\[
\mathcal C_{14,k}:V_{1,k}\longrightarrow K^{I_k},
\qquad
h\longmapsto (W_{k,\alpha}(h))_{\alpha\in I_k}.
\]

Its kernel is

\[
N_k=\bigcap_{\alpha\in I_k}\ker W_{k,\alpha}.
\]

It is faithful exactly when \(N_k=0\). The all-translate work identifies the
appropriate shape of this condition, while the infinite-rank audit shows that
a fixed finite observer packet cannot establish it on the recorded full source
family.

Even injectivity is not yet equivalence. An inverse requires a reconstruction
theorem identifying the image, a topology on the observer carrier, and
continuity of reconstruction. To make the helical successor invertible across
stages one additionally needs

\[
N_k=S_k^{-1}(N_{k+1})
\]

and compatible reconstruction maps. If the observer family grows with \(k\),
the natural object is more likely a pro/ind system or completed telescope than
a stagewise automorphism.

## Verdict

The seam \(R_k\) may be invertible, but the currently displayed stage
successor is not:

\[
\boxed{S_k=R_kC_{14,k}\text{ is noninvertible under scalar C14 typing}.}
\]

The helix is therefore directed. A reversible helix can exist only after
retyping C14 as a jointly faithful complete observer map and proving
reconstruction, or after explicitly passing to its observational quotient.
