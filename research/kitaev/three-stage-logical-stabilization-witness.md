# Three-stage logical stabilization witness

## Question

What is the smallest finite directed system that separates immediate death, delayed death, later birth, surviving probe blindness, and a stagewise probe that does not descend?

Work over \(\mathbf F_2\). Let

\[
H_0=\langle a,b,c\rangle,\qquad
H_1=\langle u,v,w\rangle,\qquad
H_2=\langle r,s,t\rangle.
\]

Use transition matrices, in the displayed bases,

\[
F=
\begin{pmatrix}
1&0&0\\
0&0&1\\
0&0&0
\end{pmatrix},
\qquad
G=
\begin{pmatrix}
1&0&0\\
0&0&1\\
0&0&0
\end{pmatrix}.
\]

Thus \(a\mapsto u\), \(b\mapsto0\), \(c\mapsto v\), while \(u\mapsto r\), \(v\mapsto0\), and \(w\mapsto s\).

## Claim boundary

The first transition has

\[
\ker F=\langle b\rangle,
\qquad
\operatorname{coker}F=\langle w\rangle.
\]

The composite satisfies

\[
GF=
\begin{pmatrix}
1&0&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
\ker(GF)=\langle b,c\rangle.
\]

Therefore \(b\) dies immediately, \(c\) survives the first transition and dies at the second, and \(w\) is born at stage one and survives as \(s\). The class \(t\) is born at stage two.

A first compatible probe cocone is generated from

\[
p_2=(1,0,0),
\qquad
p_1=p_2G=(1,0,0),
\qquad
p_0=p_1F=(1,0,0).
\]

At stage zero,

\[
\ker p_0=\langle b,c\rangle=\ker(GF),
\]

so this one probe is faithful on the portion of \(H_0\) surviving through stage two.

At stage one,

\[
\ker p_1=\langle v,w\rangle,
\qquad
\ker G=\langle v\rangle.
\]

The surviving class \(w\) is blind. Add the compatible cocone

\[
q_2=(0,1,0),
\qquad
q_1=q_2G=(0,0,1),
\qquad
q_0=q_1F=0.
\]

Then

\[
\ker p_1\cap\ker q_1=\langle v\rangle=\ker G.
\]

The pair \((p,q)\) is jointly faithful on the stage-one sector surviving to stage two. It still misses the new terminal birth \(t\); a third terminal coordinate is required if \(H_2\) itself is the target sector.

The incompatible hostile is

\[
\widetilde p_0=(0,0,1),
\qquad
\widetilde p_1=0.
\]

It reads \(c\) at stage zero even though \(c\) later dies, and

\[
\widetilde p_1F-\widetilde p_0=\widetilde p_0\ne0.
\]

It is a valid stagewise readout but not a probe of the directed-system colimit.

The witness is finite and exact. It does not model Benincasa's actual transition matrices or prove that any reported birth survives another depth.

## Disposition

Three stages are minimal for delayed death: two stages show only the kernel of one map. The composite kernel detects the new death layer

\[
\ker(GF)/\ker F=\langle[c]\rangle.
\]

The audit table required at every triple \(H_n\to H_{n+1}\to H_{n+2}\) is:

| quantity | interpretation |
|---|---|
| \(\ker f_n\) | immediate deaths |
| \(\ker(f_{n+1}f_n)/\ker f_n\) | delayed deaths first exposed one stage later |
| \(\operatorname{coker}f_n\) | births at the next stage |
| image of each birth under \(f_{n+1}\) | survival or death of new classes |
| \(p_{n+1}f_n-p_n\) | probe-cocone residual |
| joint probe kernel modulo composite kernel | surviving blind sector |

This replaces inference from isolated ranks with transition-resolved persistence data.
