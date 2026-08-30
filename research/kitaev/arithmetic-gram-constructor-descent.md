# Arithmetic constructor descent through the non-diagonal Gram completion

## Adjacent-collapse theorem

Let \(K(n,m)=A(|\log(n/m)|)\), with \(A\) continuous at zero and
\(A(0)>0\). Suppose the diagonal operation

\[
T_fe_n=f(n)e_n
\]

extends boundedly to the Gram completion. For
\(v_n=e_{n+1}-e_n\),

\[
\|v_n\|_K^2=2\bigl(A(0)-A(\log(1+1/n))\bigr)\to0.
\]

For real-valued \(f\), the exact output identity is

\[
\|T_fv_n\|_K^2
=A(0)|f(n+1)-f(n)|^2
+2f(n+1)f(n)\bigl(A(0)-A(\log(1+1/n))\bigr).
\]

The complex formula replaces the last product by its real part. If \(f\) is
bounded, the second term tends to zero. Boundedness of \(T_f\) forces the
left side to zero, so

\[
\boxed{f(n+1)-f(n)\to0.}
\]

This is a necessary adjacent-continuity condition, not a sufficient descent
theorem.

## Exact non-descent witnesses

### Parity

For \(f(n)=(-1)^n\), every adjacent jump has magnitude two and

\[
\|T_fv_n\|_K^2
=2\bigl(A(0)+A(\log(1+1/n))\bigr)	o4A(0)>0.
\]

### Divisibility by a fixed prime

For the indicator of \(p\mid n\), the pairs \((pk-1,pk)\) give jumps from
zero to one for every \(k\). Their output norm is exactly \(A(0)\), because
one coefficient vanishes.

### Prime type

For every prime \(p>3\), the pair \((p-1,p)\) is composite/prime. Infinitely
many primes therefore supply persistent adjacent jumps. The checker records a
finite certified regression sample; infinitude, not the sample alone, proves
non-descent.

### Prime-power type

For every \(m\ge2\), the adjacent pair

\[
(2^{2m}-1,2^{2m})
\]

has a non-prime-power first member and a prime-power second member. Indeed,

\[
2^{2m}-1=(2^m-1)(2^m+1),
\]

and the two nontrivial odd factors are coprime. Hence the first number has at
least two distinct prime divisors. This gives an unconditional infinite jump
family.

## Mellin-character control

For \(f_t(n)=n^{it}\),

\[
|f_t(n+1)-f_t(n)|
=|e^{it\log(1+1/n)}-1|
\le |t|\log(1+1/n)
\le\frac{|t|}{n}.
\]

Thus every fixed Mellin character passes the adjacent necessary condition.
This does not prove boundedness on the full Gram completion.

## Exact full-kernel criterion

Let \(K_N=(K(n,m))_{1\le n,m\le N}\) and
\(D_{f,N}=\operatorname{diag}(f(1),\ldots,f(N))\). The diagonal constructor
descends boundedly with norm at most \(C\) exactly when

\[
D_{f,N}^*K_ND_{f,N}\le C^2K_N
\]

for every \(N\), with one cutoff-independent \(C\), after quotienting any
finite Gram nullspace. Adjacent continuity tests only one collapsing family;
the matrix inequality tests every finite linear combination.

## Minimal discrete-port compiler

Freeze the admitted non-descending constructor attributes
\(g_1,\ldots,g_r\). Define

\[
n\sim m
\iff
(g_1(n),\ldots,g_r(n))=(g_1(m),\ldots,g_r(m)).
\]

The minimal set-level port is the realized joint-pattern set. If arbitrary
binary coding is allowed, a finite pattern set of size \(M\) needs
\(\lceil\log_2M\rceil\) bits. Thus:

- parity alone needs one bit;
- divisibility by one fixed prime needs one bit;
- parity plus divisibility by an odd prime realizes four patterns and needs
  two bits;
- prime and prime-power predicates realize three patterns—neither, proper
  prime power, prime—and need two bits.

A Boolean prime-power port preserves only the predicate. An operation using
the prime base, exponent, or occurrence label requires that typed data, not
merely one bit. For infinite-valued admitted constructors the discrete port
may be countable rather than a fixed-width binary register.

## Authority trichotomy

For each proposed arithmetic operation:

\[
\begin{array}{ll}
T_f\text{ descends}:&\text{no new port is required for }f;\\
T_f\text{ fails}:&\text{retain a discrete port only if }f\text{ is admitted};\\
T_f\text{ is not operative}:&\text{there is no authority to preserve it.}
\end{array}
\]

The compiler theorem does not choose the constructor family. Grothendieck
must derive the operative theta/Tate/Fock operations first. The compiler then
tests the full kernel inequality and synthesizes the joint discrete code only
for those that fail.

## Falsifiers and boundary

- A persistent adjacent jump with a bounded Gram operator would contradict
  the norm inequality and falsify its claimed descent.
- Passing the adjacent test but failing a finite matrix inequality falsifies
  sufficiency of local continuity.
- A proposed discrete port that identifies two labels separated by an
  admitted constructor is not jointly faithful.
- Demanding a port for a predicate absent from the admitted source algebra is
  an authority error.

No conclusion here proves that Mellin characters satisfy the full kernel
inequality, nor that parity, primality, or prime-power tests are operative in
the RH source complex.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_arithmetic_gram_constructor_descent.py
```

The checker verifies the exact norm decomposition, infinite-family templates,
finite certified jump samples, Mellin bound statement, and finite joint-port
pattern counts.
