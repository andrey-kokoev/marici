# Conclusive two-count events identify codeword mixtures

## Question

Can measured records detect violation of the fixed-codeword assumption used by the 35-trial likelihood classifier?

## Claim boundary

This gives algebraic identifiability of arbitrary classical mixtures of the four codewords under the exact response model. It does not provide a finite-sample confidence region or detect coherent superpositions with the diagonal count POVM.

## Conclusive event

For one logical mode, the calibrated count laws satisfy

\[
p_0(2)=0,
\qquad
p_1(2)=c=\frac9{250}.
\]

Hence a measured count of two cannot arise from logical occupation zero within the model.

Let

\[
w_{ab}\ge0,
\qquad
\sum_{a,b}w_{ab}=1
\]

be an arbitrary classical mixture of the four encoded classes. Define measured event probabilities

\[
r_1=\Pr[M_1=2],
\qquad
r_2=\Pr[M_2=2],
\qquad
r_{12}=\Pr[M_1=2,M_2=2].
\]

Independence of the calibrated channel conditional on each codeword gives

\[
r_1=c(w_{10}+w_{11}),
\]

\[
r_2=c(w_{01}+w_{11}),
\]

\[
r_{12}=c^2w_{11}.
\]

Therefore all mixture weights are recovered by

\[
w_{11}=\frac{r_{12}}{c^2},
\]

\[
w_{10}=\frac{r_1}{c}-w_{11},
\qquad
w_{01}=\frac{r_2}{c}-w_{11},
\]

\[
w_{00}=1-w_{10}-w_{01}-w_{11}.
\]

## Fixed-codeword gate

The fixed-codeword hypothesis holds exactly only when the recovered weight vector is one of the four simplex vertices. Any interior or multi-support weight vector is a mixture and invalidates interpretation of repeated trials as one unknown parity class.

Because \(c^2=81/62500\), the joint conclusive event can be rare. Algebraic identifiability therefore does not imply a small finite-sample leakage test.

## Site exchange

Exchanging optical modes one and two sends

\[
r_1\leftrightarrow r_2,
\qquad
w_{10}\leftrightarrow w_{01},
\]

while fixing \(r_{12},w_{00},w_{11}\). Thus the mixture reconstruction respects site exchange.

## Coherence limitation

Photon counting is diagonal in the occupation basis. It identifies the diagonal weights \(w_{ab}\), but cannot distinguish a coherent superposition from the corresponding incoherent mixture when both have the same occupation probabilities. A phase-sensitive complementary measurement would be required for that question.

## Disposition

The fixed-codeword assumption has an exact model-internal falsifier: reconstruct the four mixture weights from single and joint two-count frequencies and reject unless one vertex survives within a preregistered uncertainty region. Finite-sample confidence design and physical data remain missing.
