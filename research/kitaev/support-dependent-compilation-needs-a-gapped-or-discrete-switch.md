# Support-Dependent Compilation Needs a Gapped or Discrete Switch

Suppose a compiler chooses different observation rows on different support
strata. Even if every stratumwise choice is exact, the compiler must first
determine which couplings are zero. For one complex coupling, this requires
the support indicator

\[
\sigma(z)=
\begin{cases}
0,&z=0,\\
1,&z\ne0.
\end{cases}
\]

The map \(\sigma:\mathbf C\to\{0,1\}\) is discontinuous at zero. The sequence

\[
z_N=1/N
\]

converges to zero while \(\sigma(z_N)=1\) for every finite (N) and
\(\sigma(0)=0\). Therefore exact finite support typing does not descend to an
analytic completion that permits nonzero couplings to approach zero.

## Gap theorem

Let the admitted coupling family satisfy the alternative

\[
z=0
\quad\text{or}\quad
|z|\ge\delta
\]

for some fixed \(\delta>0\). On this restricted family, the support indicator
is continuous and, with the ordinary metric on \(\{0,1\}\), satisfies

\[
|\sigma(z)-\sigma(w)|
\le
\frac{1}{\delta}|z-w|.
\]

Indeed, the only nontrivial case has one point zero and the other of magnitude
at least \(\delta\). Thus a support-switching compiler is completion-stable if
every switched edge has a uniform zero/nonzero gap and the stratumwise
decoders are uniformly bounded.

For a finite graph, a support vector

\[
\sigma_E(z)=(\sigma(z_e))_{e\in E}
\]

requires one such gap for every edge whose status changes the selected port
family. Edges irrelevant to the switching decision need not be typed.

## Hybrid discrete repair

If no analytic gap exists, one may retain an independently typed source label

\[
b_e\in\{0,1\}
\]

with the law

\[
b_e=0\Rightarrow z_e=0,
\qquad
b_e=1\Rightarrow z_e\ne0.
\]

This produces a hybrid source space

\[
\mathcal H_{\mathrm{analytic}}\times\{0,1\}^{E_{\mathrm{switch}}}.
\]

The bit is continuous in the product topology because it is retained as a
separate discrete coordinate. It is not reconstructed continuously from the
analytic coupling. Its compatibility law can also fail at completion if the
analytic component tends to zero while the bit remains one; the completed
target must then either admit a labelled zero or exclude that sequence.

## Relation to the port ceiling

Grothendieck's Packet 249 independently establishes that the scalar
compressed-shift model has only one incoming and one outgoing defect port,
regardless of hidden zero count. This constrains executable port vocabulary:
multiple support or current bits cannot be projected onto that scalar model
without a source-derived matrix lift or internal-state typing.

The abstract switching theorem does not enlarge that port count. It says only
what additional information a support-adaptive compiler would require.

## Compiler verdict

A support-dependent compiler must return one of:

- static compiler: one fixed robust row family works on every admitted
  support;
- gapped switch: support is analytically observable with uniform separation;
- discrete switch: a source-authorized label is retained outside the analytic
  completion;
- obstruction: stratumwise exact compilers exist, but their switch is not
  continuously observable.

## Falsifiers

- Treating exact zero testing as continuous in an ordinary analytic norm.
- Selecting cutoff-dependent port families without recording the switch.
- Inferring a discrete support bit from finite nonvanishing alone.
- Adding one bit per edge when only a smaller set affects the consumer.
- Mapping multiple discrete labels into a scalar defect model without a
  matrix lift.
- Allowing the discrete bit and analytic zero to disagree without typing the
  completed labelled-zero state.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to price the hidden switch behind stratumwise port
optimization.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. A switching compiler is continuous only with a uniform support gap or
an explicit discrete source port; finite zero testing supplies neither.
