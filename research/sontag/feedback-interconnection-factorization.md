# Feedback interconnection factorization

Owner: `marici.Sontag`

## Bounded question

When does a plant/controller pair descend to a single well-defined closed-loop
transition?

## Typed constructor

Use plant equations `x+=Ax+Bu`, `y=Cx` and controller equations
`z+=Fz+Gy`, `u=Hz+Ky`. With the stated update order and no plant direct
feedthrough, substitution yields the exact block transition
`[[A+BKC,BH],[GC,F]]` on `X x Z`.

For the scalar-port witness `A=F=K=0` and `B=C=G=H=1`, the block transition is
`[[0,1],[1,0]]`. Every internal signal is typed and uniquely determined.

## Hostile falsifier

If the plant instead has direct feedthrough `y=Cx+Du`, the controller equation
requires `(I-KD)u=Hz+KCx`. At scalar values `D=K=1`, the solve operator is zero.
For `x=1,z=0,C=1,H=0`, the right side is one, so no internal signal exists.
For zero right side it is nonunique. An unordered diagram cannot repair this.

## Completion gate and verdict

The descent gate is invertibility of `I-KD`, plus a declared causal order.
Verdict: exact factorization for the no-feedthrough witness; obstruction for
the singular algebraic loop. Stability is deliberately not inferred from
well-posed interconnection.
