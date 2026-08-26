# Constructive upgrades require trace observability and Blackwell dominance

## Problem

An intervention can make a system easier to operate by destroying distinctions in its prior state. Such an intervention may be useful control, but it is not an observation or explanation of the predecessor.

A genuine constructive upgrade must pass two independent gates:

1. the enlarged experiment distinguishes the declared predecessor states from admissible traces;
2. the enlarged experiment preserves the decision capabilities of the old experiment.

The first gate is controlled observability. The second is Blackwell dominance.

## Static experiment kernel

For a state object \(X\) and admitted experiment family \(E\), let \(H_e\) be the readout of experiment \(e\). Define

\[
x\sim_E x'
\quad\Longleftrightarrow\quad
H_e(x)=H_e(x'),
\qquad e\in E.
\]

Equivalently, the kernel pair of the family is

\[
K_E=\bigcap_{e\in E}\operatorname{Eq}(H_e).
\]

For a declared quotient \(q:X\to Q\), an admitted input extension \(U\) is separating exactly when

\[
K_{E\cup U}=\operatorname{Eq}(q).
\]

It is fully observable exactly when this kernel pair is the diagonal.

Minimality is evaluated only among independently source-admitted experiments. An arbitrary function engineered to kill the kernel is not an authorized calibration.

## Group-action specialization

Suppose the passive ambiguity is an action of a group \(G\) on \(X\). Prepared references \(u_i\) leave the residual ambiguity

\[
G_U=\bigcap_i\operatorname{Stab}_G(u_i).
\]

Full controlled observability requires \(G_U\) to be trivial. Thus a minimal calibration family is a base for the action, minimized within the source-admitted preparation family.

For the free \(\mathbb Z_5\) clock action, one exactly known reference is a base. An orbit-uncertain reference has stabilizer \(\mathbb Z_5\) and contributes no distinguishing power.

## Dynamic trace equivalence

Static kernel intersections are insufficient for interventions that change state. Let

\[
x_{t+1}=F_{u_t}(x_t),
\qquad
y_t=H_{u_t}(x_t),
\]

where each \(u_t\) is chosen by one admitted nonanticipating policy \(\pi\) from prior observed history. Let \(\operatorname{Tr}_\pi(x_0)\) denote the complete input-output trace.

Define

\[
x\sim_{\mathrm{tr}}x'
\quad\Longleftrightarrow\quad
\operatorname{Tr}_\pi(x)=\operatorname{Tr}_\pi(x'),
\qquad \pi\in\Pi_{\mathrm{adm}}.
\]

This excludes oracle policies that select inputs using the hidden state rather than the observed history.

## Reset hostile

Consider an intervention that forces the hidden frame coordinate to zero before the next readout. Every run then ends in a known terminal frame.

A terminal-state audit declares success because the final state is unambiguous. The trace audit does not: distinct predecessor states can produce the same pre-reset observations and the reset maps them to one successor.

Therefore:

- the reset is a corrective control;
- it constructs a new calibrated successor;
- it does not observe or explain the predecessor;
- predecessor authority survives only if the transition and erased information are independently retained.

Controllability is not observability.

## Probabilistic trace version

For controlled stochastic kernels, each admitted policy produces a trace law \(P_x^\pi\). Probabilistic trace equivalence is

\[
x\sim_{\mathrm{prob}}x'
\quad\Longleftrightarrow\quad
P_x^\pi=P_{x'}^\pi,
\qquad \pi\in\Pi_{\mathrm{adm}}.
\]

Unequal laws establish asymptotic identifiability only. A bounded physical distinction additionally requires a declared risk, horizon, repetition budget, resource law, and nuisance class. Under equal priors, the best binary error for one policy is

\[
R_\pi^*=\frac{1-\operatorname{TV}(P_x^\pi,P_{x'}^\pi)}{2}.
\]

A valid comparison uses one prospective policy and one common nuisance model. Hypothesis-dependent policies, postselected rare branches, and separately fitted calibrations are invalid hostiles.

## Preservation by Blackwell dominance

Let \(E\) be the old stochastic experiment and \(E'\) the proposed upgrade. The upgrade preserves every decision capability of \(E\) exactly when a state-independent garbling kernel \(K\) exists such that

\[
E=K\circ E'.
\]

Then \(E'\) Blackwell-dominates \(E\). Extra records that are Blackwell-equivalent to \(E\) add no decision capability. A replacement may separate a new target while failing constructive preservation if no such \(K\) reconstructs the old experiment law.

## Upgrade criterion

A source-admitted experiment extension is a constructive observational upgrade only if:

1. its policy-indexed trace kernel equals the declared quotient kernel;
2. its policies are nonanticipating and common across hypotheses;
3. its separation is robust over the admitted nuisance class;
4. it Blackwell-dominates the prior experiment;
5. its transport and policy composition remain defined for future admitted extensions.

This criterion distinguishes three operations that endpoint inspection conflates:

- observing a predecessor distinction;
- controlling the system into a known successor;
- replacing the experiment with a different decision interface.

Only the first, together with preservation of the old interface, is a constructive observational upgrade.
