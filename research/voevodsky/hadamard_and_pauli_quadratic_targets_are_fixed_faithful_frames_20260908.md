# Hadamard and Pauli quadratic targets are fixed faithful frames

Date: 2026-09-08

## Converter

Let `G` be the resolved two-port polarized Gram, let

\[
L=HGH
\]

be its four Hadamard blocks, and let

\[
R=[X\;Y],\qquad \Gamma_{\rm P}(G)=R^*GR
\]

be the faithful Pauli lift.  Define the fixed frame

\[
S=HR.
\]

Then

\[
\Gamma_{\rm P}(G)=S^*LS.
\]

Moreover `SS*=2I`, so the converter has the explicit retraction

\[
L=\frac14S\Gamma_{\rm P}(G)S^*.
\]

Thus equality of all four Hadamard blocks is equivalent to equality of the
full Pauli quadratic lift.  The relative phase is fixed, not selected:

\[
Y=XU,\qquad U=XY=\operatorname{diag}(-i,i).
\]

## Consequence for the frontier

The proposed theta/Pauli theorem does not require sixteen independent matrix
identities.  It requires one equality of the resolved two-port Gram on the
common source core; either faithful frame then generates and reconstructs the
other.  Concretely, proving

\[
L_{\theta,p}=H G_p^{\rm St} H
\]

immediately gives

\[
\Gamma_{\theta,p}=\Gamma_{\rm P}(G_p^{\rm St}),
\]

provided the theta lift uses the fixed frame `S`.

The nonredundant remaining input is therefore not more finite matrix algebra.
It is source authority and analysis: construct the theta resolved Gram on the
common rapid wall-reduced core, prove it uses `S`, and establish closability,
radical descent, and cutoff naturality.

## Evidence

- `check_marici_rh_hadamard_to_pauli_frame_converter_20260908.py`
- `marici_rh_hadamard_to_pauli_frame_converter_certificate_20260908.json`
