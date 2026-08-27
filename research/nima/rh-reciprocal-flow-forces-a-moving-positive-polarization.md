# RH reciprocal flow forces a moving positive polarization

## Result

The canonical reciprocal cross-form admits positive graph subspaces, but no nonzero positive graph is fixed by nontrivial reciprocal spectral dilation.

Write the doubled transport as

\[
E=
\begin{pmatrix}
R&0\\
0&R^{-1}
\end{pmatrix}
\]

and a graph subspace as

\[
L_H=\{(x,Hx)\}.
\]

For symmetric positive \(H\), the cross-form restricts to

\[
Q((x,Hx),(x,Hx))=2x^THx>0.
\]

Under reciprocal transport, the graph moves by

\[
H\longmapsto H'=R^{-1}HR^{-1}.
\]

If every dilation eigenvalue of \(R\) is greater than one, the fixed-graph equation

\[
R^{-1}HR^{-1}=H
\]

forces \(H=0\) entrywise. Therefore no static positive polarization is preserved.

The exact checker uses \(R=\operatorname{diag}(2,3,4)\). It transports \(H=I\) to

\[
H'=\operatorname{diag}\left(\frac14,\frac19,\frac1{16}\right),
\]

which remains positive but is not fixed.

## Meaning

Reciprocal doubling supplies the conserved split form. Orientation requires a positive graph inside it. Spectral flow necessarily transports that graph.

Thus the moving seam is not an optional coordinate trick. It is the evolution of the positive polarization under reciprocal dilation.

This yields a three-layer structure:

- split form: fixed and conserved;
- positive polarization: moving covariantly;
- scalar endpoint: a readout whose transversality to the moving polarization remains to be proved.

## Why this still does not prove RH

Any chosen positive initial graph can be transported. The source must select the initial graph and prove that the admissible theta state lies in its transported image.

Furthermore, finite positivity can collapse at completion if the smallest eigenvalue of \(H_X\) tends to zero. The exact fixture already displays the mechanism: repeated dilation drives the graph toward the null sector.

The required completion gate is therefore uniform graph transversality in the source topology, not merely positivity at each cutoff.

## DPC verdict

Candidate: a fixed positive polarization preserved by reciprocal spectral flow.

Verdict: impossible for nontrivial positive dilation.

Candidate: an arbitrarily chosen moving positive graph.

Verdict: algebraically available but source-unauthorized.

Surviving candidate: a source-derived initial polarization, covariantly transported by the doubled spectral and arithmetic system, with seam-jet compatibility and a completion-stable lower angle from the endpoint kernel.

## Finite falsifiers

At each cutoff:

1. test the graph transport law under one spectral step;
2. test the analogous law under one prime shift including all seam jets;
3. calculate the smallest eigenvalue of the transported graph metric;
4. calculate the principal angle between the admissible state image and the endpoint kernel.

Failure of covariance closes the proposed polarization. Collapse of either the eigenvalue or angle closes completion-stable orientation.
