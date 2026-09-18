# Disposition: the prime-cell isometry is not the source-authorized quadratic construction

## Resolved ambiguity

The proposed independent datum

\[
G_S=T_p^*G_WT_p
\]

is not missing. It is the wrong quadratic requirement for the declared completion.

The source-authorized construction is a retained joint graph. For the independently constructed theta and Stieltjes/window forms and the source map \(K_p\), its form is

\[
G_{\Gamma,p}
=G_{\theta,p}+K_p^*G_{\mathrm{win},p}K_p.
\]

This is a positive graph extension, not an isometric identification of its two diagonal coordinates.

## Exact obstruction to isometry

On the odd source line, with

\[
K_pj_\theta=d_p,
\]

an isometric pullback would require

\[
G_{\mathrm{win},p}(d_p,d_p)
=G_{\theta,p}(j_\theta,j_\theta).
\]

But the raw Stieltjes/window energy tends to zero along the prime completion, whereas the retained theta endpoint metric gives a fixed positive energy. Therefore no uniformly completion-compatible isometry exists without inserting a forbidden inverse normalization.

On the even raw-window line there is also the local mismatch

\[
0<G_{p,11}^{St,even}<1
\]

against the normalized theta endpoint contribution one. This second observation is limited to the raw window component; the odd asymptotic obstruction already addresses the declared raw comparison topology.

## Role of the Pauli lift

The full Pauli linking lift is faithful and therefore cannot turn a false isometry into a true one:

\[
\Gamma_{\rm P}(G)=R^*GR,
\qquad
G=X[\Gamma_{\rm P}(G)]_{XX}X.
\]

Its summed diagonal frame remains useful for observability, but that lossy sum is not the polarized quadratic identity.

## Correct functoriality

The valid statement is covariance of the retained graph under the source constructor, together with radical compatibility:

\[
K_pN_{\theta,p}\subseteq N_{\mathrm{win},p}.
\]

After descent,

\[
G_{\Gamma,p}^{red}\ge G_{\theta,p}^{red}.
\]

The Stieltjes component is retained as a positive trace-class shadow and does not replace or normalize the theta coordinate.

## Consequences for alpha

There is no free \(\alpha_p\):

1. the actual linear theta columns are already fixed;
2. a fitted scalar cannot repair the completion-scale mismatch;
3. the source-authorized graph construction does not ask for diagonal isometry in the first place.

Thus searching for \(\alpha_p\) or a completed matrix equality is not a legitimate open gate.

## Contract disposition

The contract

`research/voevodsky/contracts/polarized-prime-cell-two-scalar-closure.v1.json`

is retained only as an audit of a rejected hypothetical isometry. It must not be used as an active theorem prerequisite.

The active quadratic obligations are instead:

1. define the full wall--jump--odd joint graph on one common domain;
2. prove radical compatibility for \(K_p\);
3. prove cutoff naturality and closed-range completion;
4. retain the signed mixed cross-leg pairing needed for arithmetic cycle closure.

None of these obligations is an equality of the two diagonal Green metrics.

## Claim boundary

This resolves the local isometry question negatively and identifies the canonical replacement. It does not prove the remaining mixed arithmetic balance, global Evans membership, or RH.
