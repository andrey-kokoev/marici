# Correction: faithful Pauli dilation cannot repair the raw diagonal mismatch

> **Scope refinement:** this proves a no-go for the faithful lift of the raw window Gram. The dossier later uses an undefined complete symbol `G_p^St` after mentioning positive resolved attachments. It does not prove a no-go for that completed form. See `correction-the-even-diagonal-falsifier-does-not-apply-to-the-undefined-complete-stieltjes-form.md`.

## Correction of the scope correction

The prior note claimed that the raw even-diagonal no-go does not test the Pauli-dilated comparison. That is true only for the **summed frame operator**

\[
XGX+YGY=2\operatorname{diag}(b,a),
\]

which is deliberately lossy. It is false for the full faithful Pauli linking Gram required by the constructor theorem.

## Faithful lift and retraction

Let

\[
R=[X\;Y],
\qquad
\Gamma_{\rm P}(G)=R^*GR.
\]

The `XX` block is \(XGX\), so

\[
G=X\,[\Gamma_{\rm P}(G)]_{XX}\,X.
\]

Hence \(\Gamma_{\rm P}\) is injective. Equality of full Pauli lifts implies equality of the underlying two-port Grams.

Equivalently, with Hadamard frame \(S=H[X\;Y]\),

\[
\Gamma_{\rm P}(G)=S^*(HGH)S,
\qquad
HGH=\frac14S\Gamma_{\rm P}(G)S^*.
\]

Thus the fixed Pauli/Hadamard converter also has an exact retraction.

## Propagation of the no-go

Suppose the theta output uses the required fixed faithful frame and the full linking-Gram identity holds:

\[
\Gamma_{\theta,p}=
\Gamma_{\rm P}(G_p^{\rm win}).
\]

If \(\Gamma_{\theta,p}\) is the faithful lift of the declared normalized theta two-port form \(H_p^\theta\), retraction forces

\[
H_p^\theta=G_p^{\rm win}.
\]

But the even diagonal theorem gives

\[
G_{p,11}^{\rm win}<1\le H_{p,11}^\theta.
\]

Contradiction. Therefore the full faithful Pauli comparison cannot repair the mismatch.

The apparently improved diagonal

\[
2\operatorname{diag}(b_p,a_p)
\]

belongs only to the summed frame shadow. Comparing that shadow alone discards the mixed \(X\)-\(Y\) blocks and fails the declared orientation/faithfulness requirement.

## Exact alternatives

A viable repair must do at least one of the following:

1. change the underlying theta two-port normalization by an independent source theorem;
2. compare a different theta object not equal to the faithful lift of the normalized direct-sum form;
3. weaken the theorem to the summed frame estimate, explicitly abandoning polarized constructor identity;
4. introduce a non-isometric source-derived embedding whose induced underlying Gram is the raw Stieltjes form.

Calling the same faithful Pauli lift a new target does not create a fifth option.

## Correct status

- raw direct metric equality: falsified;
- full faithful Pauli linking-Gram equality using the same normalized theta form: falsified by injectivity;
- summed Pauli frame bound: valid, but insufficient for orientation or constructor identity;
- genuinely different typed theta target: not yet constructed.

## Claim boundary

This no-go is local and normalization-specific. It does not reject Pauli dilation as an observability device, nor every possible non-isometric source-derived comparison.
