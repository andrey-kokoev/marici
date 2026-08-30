# The theta source channel is the candidate lossless boundary port

Grothendieck's source-derived tail system supplies the missing structural candidate identified by the scattering audit.

The augmented state is
\[
\Psi_s(q)
=
\binom{G_s(q)}{1},
\qquad
\mathcal D_s
=
\begin{pmatrix}
\partial_q+s&f(q)\\
0&\partial_q
\end{pmatrix},
\]
with
\[
\mathcal D_s\Psi_s=0.
\]
The constant component is a homogeneous source channel. Unlike the half-density prime delays, it is not attenuated. It is therefore a natural candidate for the lossless boundary direction that can attain unit modulus on the seam.

This gives a source-derived division of labor:

- \(G_s\): dissipative or strictly passive theta-tail state;
- constant source component: lossless wall input;
- \(f(q)\): coupling between the wall and tail;
- endpoint traces: boundary output;
- bilateral modular sewing: reciprocal unitary feedback.

The one-sided Green identity is
\[
\partial_q|G_s|^2
=
-2\operatorname{Re}(s)|G_s|^2
-
2\operatorname{Re}(f\overline{G_s}).
\]
The forcing cross-term is exactly the missing colligation cross block. On one side it is indefinite; after reciprocal doubling, the desired theorem is that the two forcing terms combine with wall and archimedean boundary flux to give a conservative system-node identity.

This points to the full block relation
\[
2\operatorname{Re}\langle \mathcal A x,x\rangle
=
\|u\|_{\mathrm{in}}^2-\|y\|_{\mathrm{out}}^2
-
\mathcal D_{\mathrm{bulk}}(x),
\]
where \(\mathcal D_{\mathrm{bulk}}\ge0\) off seam and vanishes in the lossless limit. Such an identity produces a Schur transfer without using \(\xi\).

The second Grothendieck result adds an important typing decision. The seam graph
\[
\Gamma_0(Gc)=Hc
\]
is unbounded, and closability is equivalent to density of
\[
\{y:H^{*}y\in\operatorname{Ran}G\}.
\]
The programme does not yet know this density theorem.

The scattering construction should therefore not assume that the seam is a closed function of the tail. Retain tail and seam as independent state/boundary components and encode their source relation as a closed linear relation
\[
\mathfrak R
\subset
\mathcal H_{\mathrm{tail}}\oplus\mathcal H_{\mathrm{seam}}.
\]
If the graph later proves closable, \(\mathfrak R\) reduces to the graph of \(\overline{\Gamma}_0\). If not, the multivalued boundary relation remains legitimate and no seam information is discarded.

This avoids making the unresolved Hankel--Volterra range problem a prerequisite for defining the conservative boundary system. It does not eliminate the range problem; it moves it into the minimality audit:

- a multivalued part corresponds to seam freedom not controlled by the tail;
- a kernel corresponds to a tail state invisible at the seam;
- both must be observed by the enlarged colligation or retained as explicit ports.

The next source-native construction is therefore:

1. take the doubled theta-tail systems at \(s\) and \(1-s\);
2. retain both constant source channels;
3. retain seam variables independently of tail variables;
4. impose the Hankel--Volterra incidence as a linear relation;
5. add archimedean endpoint flux;
6. derive the exact doubled Green identity;
7. read off the system-node transfer;
8. test strict passivity off seam and losslessness on seam.

The expected cancellation target is
\[
\operatorname{Re}\int f\overline{G_{+}}
+
\operatorname{Re}\int f^{\vee}\overline{G_{-}}
=
\text{wall flux}
+
\text{archimedean flux},
\]
with no residual indefinite bulk channel.

If that identity holds, the constant source carrier supplies the direct lossless port while the theta and Euler tails supply the interior phase. The seam zeros can then be conservative feedback resonances rather than artifacts of scalar continuation.

The minimal hostile eliminates the constant channel after solving the inhomogeneous equation. The resulting tail transfer remains strictly dissipative and cannot resonate on seam.

A second hostile forces the seam to equal \(HG^{-1}\) before proving closability. It obtains a convenient operator transfer by silently quotienting away a genuine multivalued boundary component.

Thus the earliest concrete scattering constructor is already present in the source programme: the doubled homogeneous theta-tail system with its constant wall channels, treated as a system node or boundary relation rather than as a bounded tail operator.
