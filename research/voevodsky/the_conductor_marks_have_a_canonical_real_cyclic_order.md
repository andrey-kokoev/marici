# The conductor marks have a canonical real cyclic order

The conductor conic

\[
-xa^2-yb^2+xy(x+y)h^2=0
\]

can be parametrized in the affine chart \(h=1\) by the slope

\[
m=\frac{b-x}{a-y}
\]

of a line through \(p_{++}=(y,x)\). Solving for the second intersection gives

\[
a(m)=-y\frac{-m^2y+2mx+x}{m^2y+x},
\]

\[
b(m)=x\frac{-m^2y-2my+x}{m^2y+x}.
\]

The four smoothing marks occur at

\[
\begin{array}{c|c}
\text{mark}&m\\ \hline
p_{++}&-1\\
p_{-+}&0\\
p_{--}&x/y\\
p_{+-}&\infty.
\end{array}
\]

For positive \(x,y\), their real cyclic order is therefore

\[
++\;\longrightarrow\;-+\;\longrightarrow\;--\;\longrightarrow\;+-\;\longrightarrow\;++.
\]

The corresponding cross-ratio is

\[
\frac{x+y}{x},
\]

so the marked configuration varies nontrivially with kinematics while its cyclic order remains fixed in the positive chamber.

The triality-fixed diagonal matching

\[
(++,--)\mid(-+,+-)
\]

pairs opposite points in this cyclic order. It is not the matching obtained by blindly pairing neighboring real marks.

This clarifies what the global based-path calculation must decide. One must lift the actual Bunch--Davies continuation to the marked \(m\)-sphere and determine its braid. Merely knowing the positive chamber or the unordered set of four points is insufficient: adjacent real arcs and the total-energy outer arm define different pairings.

Certificate:

- `research/voevodsky/checkers/parameterize_marked_conductor_conic.py`;
- `research/voevodsky/results/marked_conductor_parameterization.json`.
