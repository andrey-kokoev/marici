import itertools
import json
from pathlib import Path


SIGNS = (-1, 1)


def observe(source_phase, nuisance_phase):
    return source_phase * nuisance_phase


# One target observation admits both source signs.
single_setting_models = {}
for observed in SIGNS:
    models = [
        (source, nuisance)
        for source, nuisance in itertools.product(SIGNS, repeat=2)
        if observe(source, nuisance) == observed
    ]
    assert {source for source, _ in models} == set(SIGNS)
    single_setting_models[str(observed)] = [list(model) for model in models]

# A control with source phase +1 and a shared nuisance recovers the target.
shared_recoveries = []
for target_source, nuisance in itertools.product(SIGNS, repeat=2):
    target_observed = observe(target_source, nuisance)
    control_observed = observe(1, nuisance)
    recovered = target_observed * control_observed
    assert recovered == target_source
    shared_recoveries.append(
        {
            "target_source": target_source,
            "nuisance": nuisance,
            "target_observed": target_observed,
            "control_observed": control_observed,
            "recovered": recovered,
        }
    )

# Independent nuisance factors recreate the ambiguity even with a control.
independent_hostiles = []
for target_observed, control_observed in itertools.product(SIGNS, repeat=2):
    models = [
        (target_source, target_nuisance, control_nuisance)
        for target_source, target_nuisance, control_nuisance
        in itertools.product(SIGNS, repeat=3)
        if observe(target_source, target_nuisance) == target_observed
        and observe(1, control_nuisance) == control_observed
    ]
    assert {source for source, _, _ in models} == set(SIGNS)
    independent_hostiles.append(
        {
            "observations": [target_observed, control_observed],
            "models": [list(model) for model in models],
        }
    )

result = {
    "schema": "marici.associator-common-mode-control.v1",
    "single_setting_nonidentifiable": True,
    "single_setting_models": single_setting_models,
    "shared_nuisance_recoveries": shared_recoveries,
    "independent_nuisance_remains_nonidentifiable": True,
    "independent_hostiles": independent_hostiles,
    "verdict": "associator phase is identifiable only through a source-derived common-mode control",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "associator-common-mode-control.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
