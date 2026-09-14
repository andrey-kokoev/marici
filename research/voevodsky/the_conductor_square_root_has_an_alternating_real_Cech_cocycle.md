# The conductor square root has an alternating real Cech cocycle

For positive \(x,y\), the denominator of

\[
g(m)=\frac{m(m+1)(x-my)}{(m^2y+x)^2}
\]

is positive on the real conductor. In the cyclic intervals determined by

\[
-1<0<x/y<\infty,
\]

the signs are

\[
+,-,+,-.
\]

More explicitly,

\[
\begin{array}{c|c}
\text{interval}&\operatorname{sign}g\\ \hline
(p_{+-},p_{++})&+\\
(p_{++},p_{-+})&-\\
(p_{-+},p_{--})&+\\
(p_{--},p_{+-})&-.
\end{array}
\]

Thus the ordered normalized branches

\[
Q\pm\varepsilon\sqrt{-U}\,g(m)
\]

exchange their real ordering at every marked point. The mod-two Čech transition vector is

\[
(1,1,1,1),
\]

whose total monodromy is even, as required.

The positive and negative intervals define two checkerboard matchings:

\[
(p_{+-},p_{++})\mid(p_{-+},p_{--}),
\]

and

\[
(p_{++},p_{-+})\mid(p_{--},p_{+-}).
\]

A global interchange of the two normalization sheets exchanges these two matchings. Therefore the real sign pattern alone does not select the opposite-point matching previously associated with the fixed triality class.

This is another useful correction: the existence of a site-fixed outer arm did not by itself prove that the physical continuation lands on that arm. The actual answer depends on combining this checkerboard with the complex Bunch--Davies phase of \(\sqrt{-EU}\) and then applying the integral specialization map.

Certificate:

- `research/voevodsky/checkers/conductor_square_root_real_cech_signs.py`;
- `research/voevodsky/results/conductor_real_cech_signs.json`.
