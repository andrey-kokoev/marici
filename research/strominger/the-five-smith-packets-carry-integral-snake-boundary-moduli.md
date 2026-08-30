# The Five Smith Packets Carry Integral Snake-Boundary Moduli

For each exact Smith packet define

\[
\mu_X=
\frac{\prod_i s_i^{\mathrm{full}}(X)}
     {\prod_j s_j^{\mathrm{rel}}(X)}.
\]

All five quotients are integers. Their exact values are

\[
\begin{array}{c|r|c}
X&\mu_X&v_2(\mu_X)\\
\hline
A_+&505222245120&8\\
A_-&606017838336&8\\
B&79883493120&8\\
C_+&1204224&13\\
C_-&1990656&13.
\end{array}
\]

The \(C\) values obey one source-character law:

\[
\mu_C(\omega)=2^{13}\,3\,(8-\omega)^2.
\]

Hence

\[
\mu_C(+1)=2^{13}\cdot3\cdot7^2,
\qquad
\mu_C(-1)=2^{13}\cdot3\cdot9^2.
\]

The common 2-primary factor fixes depth thirteen. The relational orientation
bit is carried entirely by the odd square.

For \(A_\pm\), the modulus depth is eight in both cases; their orientation bit
also lies in the odd part, but unlike \(C\) it is supported only by the full
gauge extension. The unsplit \(B\) packet likewise has depth eight.

Thus the three 2-adic profile classes can be read as two extension-depth
strata:

- \(A_\pm\) and \(B\) have extension depth eight;
- \(C_\pm\) have extension depth thirteen.

Replay:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies seventy-seven exact gates.
