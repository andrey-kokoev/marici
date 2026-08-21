# The vector-valued crossed cut reconstructs \(g_2\) and \(g_3\)

The source paper uses

\[
t_{\rm src}=(p_2+p_3)^2,\qquad u_{\rm src}=(p_1+p_3)^2.
\]

Our physical momentum transfer is \(u_{\rm src}\). Therefore the left cut at
fixed transfer exchanges \(s\) with \(t_{\rm src}\), taking

\[
M_{--++}\longrightarrow M_{+--+}.
\]

In the physical Cutkosky matrix these are the two diagonal channels
\(C_{++,++}\) and \(C_{+-,+-}\). Their inverse moments assemble with opposite
crossing characters at consecutive grades:

\[
\boxed{
g_2=J_2^{++}+J_2^{+-},\qquad
g_3=J_3^{++}-J_3^{+-},
}
\qquad
J_n^h=\frac1\pi\int_4^\infty\frac{C_{h,h}(s,0)}{s^{n+1}}\,ds.
\]

This is the missing dispersive completion of the \(\Phi_1\) sector. It is a
map on the helicity vector, not a scalar even/odd assignment.

Away from the forward point, with \(\nu=s+T/2\), a naive D10 truncation would
predict

\[
[\nu^2]\Phi_1=g_2-\frac32Tg_3,\qquad
[\nu^3]\Phi_1=g_3.
\]

The exact cut moments do **not** obey this truncated identification: at
\(T=-1/4\), the inverse-fourth moment differs from \(g_3\) by about 14.6%.
This is expected because D12 and higher terms such as \(s^4\) acquire a
\(\nu^3\) component after shifting \(s=\nu-T/2\). Thus forward moments isolate
the EFT grade, while nonzero-transfer moments require a triangular
higher-grade subtraction. The failure is retained as a deliberate gate.

For the source-typed D12 basis

\[
\Phi_1^{(12)}=g_{4,1}s^4+g_{4,2}s^2(s^2+t^2+u^2),
\]

the first triangular law is

\[
[\nu^3]\Phi_1
=g_3-2T(g_{4,1}+g_{4,2})+O(T^2).
\]

Consequently, two nonzero-transfer moments and a first Richardson step give a
discovery estimate of the independent combination \(g_{4,1}+g_{4,2}\). This
is different from the transverse Bell combination
\(g_{4,1}+\tfrac32g_{4,2}\).

Reproduce with `research/nima/check_qed_phi1_crossed_cut.py`.
