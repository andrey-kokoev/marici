# First rung4 output of the existing fiber kernel

This test uses the retained-total schedule documented in
`label-from-to-fibration-tower.md`: eight selectors label,from,to,label,from,to,
label,from. It imports `TableFibrationCycle` directly and iterates its proven
`fibrate-table` / `restore-table` operations. No line-graph promotion, ancestry
metric, clock convention or particle identification is added.

Two input schemas are supplied:

- One row with unit label, source and target.
- Four rows X=Bool x Bool, with label(x)=x, from(a,b)=a, to(a,b)=b.

The latter is a binary source/target table of four record vectors. It does not
automatically equip four records with the tetrahedron's twelve arrows.

## Observed first floor

For the four-row seed, the outermost selector at rung4 is from:

| Outer fiber | Original records retained inside |
|---|---|
|0|(0,0),(0,1)|
|1|(1,0),(1,1)|

Each member retains its complete eight-level grouping history. The record for
(0,1), shown outside-in, has inherited keys:

    from=0
      label=(0,1)
        to=1
          from=0
            label=(0,1)
              to=1
                from=0
                  label=(0,1)
                    original=(0,1)

Every layer also carries the corresponding fiber membership equality witness.
The one-row seed produces one similarly nested floor value.

## Formal result

`FirstRungFourRecordRegression.agda` proves for an arbitrary table that the
floor's row type is isomorphic to its original row type, preserving labels and
both endpoint fields. It proves both inverse laws: every original is recovered,
and every floor value is the lift of a recovered original. The concrete
four-record example also proves the outer key is the first Boolean coordinate.
Thus there is no additional floor state hidden by a one-way reconstruction test.

This is an inspected retained fiber record, not a particle identification. The
kernel has no supplied charge readout, spin action, mass/energy operator or
propagation law from which to determine a particle species. The stage name
rung4 alone supplies none of those readouts.

## Verification

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module FirstRungFourRecordRegression -Fresh
```

Fresh safe Cubical Agda verification passed, including all dependencies with
`--ignore-interfaces`. A separate finite expansion checked all four explicit
rows and recovered each after all eight nested keys.

- Source: `agda/FirstRungFourRecordRegression.agda`
- Receipt: `results/agda-FirstRungFourRecordRegression.json`
- Log: `results/agda-FirstRungFourRecordRegression.log`
