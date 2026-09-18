# Many-many relative realization triangle

## Finite-family object

For a finite labelled family

$$
\mathcal F=\{(n_i,m_i,a_i,b_i)\}_{i=1}^r,
$$
retain one source-labelled carrier

$$
\mathcal G_{\mathcal F}
=\bigoplus_{i=1}^r\mathcal G_{n_i m_i}^{[a_i,b_i]}.
$$

Each summand retains its pair operator, forcing coefficient, endpoint value, and shell coordinate.

## Three vertices

The forming triangle has vertices:

1. `P_F`: prime-labelled family observer;
2. `R_F`: pair-response graph observer;
3. `B_F`: boundary/spectral readout observer.

The edges are:

$$
P_{\mathcal F}\to R_{\mathcal F},
\qquad
R_{\mathcal F}\to B_{\mathcal F},
\qquad
P_{\mathcal F}\to B_{\mathcal F}.
$$

## First triangle law

The required law is equality of the two composite readouts on the common source core:

$$
(B_{\mathcal F}\leftarrow R_{\mathcal F})
\circ
(R_{\mathcal F}\leftarrow P_{\mathcal F})
=
(B_{\mathcal F}\leftarrow P_{\mathcal F}).
$$

Equality is required as a typed relative observation. Ordinary carrier positivity is handled separately.

## Scope

This construction operates above the RH gate. It establishes many-many source-labelled coherence, with scalar spectral-kernel positivity treated as a later property.

Status: finite-family triangle defined; the first triangle identity and its higher associativity remain to be checked.
