"""Finite, one-shot proof/rejection planning with a coherent joint belief model.

No scientific outcomes are recorded. Failed attempts update hypothetical beliefs,
never facts. Proof prerequisites are certificates, not merely probability-one claims.
"""
from dataclasses import dataclass
from functools import lru_cache
from math import isclose, log2

OUTCOMES = ('++', '+-', '-+', '--')


def entropy(probabilities):
    return -sum(p * log2(p) for p in probabilities if p > 0)


def likelihood(action, truth, outcome):
    if action['intent'] == 'prove':
        success = action['sensitivity'] if truth else 0.0
        return {'++': success, '+-': 1 - success}.get(outcome, 0.0)
    success = action['sensitivity'] if not truth else 0.0
    return {'-+': success, '--': 1 - success}.get(outcome, 0.0)


def condition(worlds, predicates):
    kept = [w for w in worlds if all(w['truth'][claim] == value for claim, value in predicates.items())]
    total = sum(w['probability'] for w in kept)
    if total <= 0:
        raise ValueError('zero-probability readiness context')
    return [dict(w, probability=w['probability'] / total) for w in kept]


def marginal(worlds, claim):
    return sum(w['probability'] for w in worlds if w['truth'][claim])


def action_metrics(worlds, action, target):
    """Expected information, conditional on the supplied readiness context."""
    p = marginal(worlds, action['claim'])
    target_p = marginal(worlds, target)
    before_claim = entropy([p, 1-p])
    before_target = entropy([target_p, 1-target_p])
    after_claim = after_target = after_joint = 0.0
    probabilities = {}
    for outcome in OUTCOMES:
        weights = [w['probability'] * likelihood(action, w['truth'][action['claim']], outcome) for w in worlds]
        probability = sum(weights)
        probabilities[outcome] = probability
        if probability <= 0:
            continue
        posterior = [dict(w, probability=x / probability) for w, x in zip(worlds, weights) if x > 0]
        q = marginal(posterior, action['claim'])
        t = marginal(posterior, target)
        after_claim += probability * entropy([q, 1-q])
        after_target += probability * entropy([t, 1-t])
        after_joint += probability * entropy(w['probability'] for w in posterior)
    claim_ig = max(0., before_claim - after_claim)
    target_ig = max(0., before_target - after_target)
    return {
        'claim_probability_in_context': p,
        'outcome_probabilities': probabilities,
        'conclusive_probability': probabilities['++'] + probabilities['-+'],
        'claim_information_bits': claim_ig,
        'target_information_bits': target_ig,
        'joint_information_bits': max(0., entropy(w['probability'] for w in worlds) - after_joint),
        'claim_information_per_effort': claim_ig / action['cost'],
        'target_information_per_effort': target_ig / action['cost'],
    }


@dataclass(frozen=True)
class Value:
    success: float
    expected_cost: float
    action: str | None


class Planner:
    """Maximize positive target closure within budget, then minimize expected cost.

    Each canonical action can run once. Conditional on a truth world, the declared
    bounded-attempt completion likelihoods are independent. Rejection may save work,
    but is not itself a positive certificate. Abandonment is always permitted.
    """
    def __init__(self, worlds, actions, target, known_proofs=(), budget=24):
        if not isinstance(budget, int) or budget < 0:
            raise ValueError('budget must be a nonnegative integer')
        if not worlds or abs(sum(w['probability'] for w in worlds)-1) > 1e-10:
            raise ValueError('world probabilities must sum to one')
        if any(w['probability'] <= 0 for w in worlds):
            raise ValueError('world probabilities must be positive')
        if len({a['id'] for a in actions}) != len(actions):
            raise ValueError('duplicate canonical actions')
        for a in actions:
            if a['intent'] not in ('prove', 'reject') or not 0 <= a['sensitivity'] <= 1:
                raise ValueError('invalid action likelihood')
            if not isinstance(a['cost'], int) or a['cost'] <= 0:
                raise ValueError('budgeted costs must be positive integers')
            if any(a['claim'] not in w['truth'] for w in worlds):
                raise ValueError('unknown action claim')
        self.worlds, self.actions, self.target = worlds, actions, target
        self.known = frozenset(known_proofs)
        self.budget = budget
        self._proof_index = {a['claim']: i for i, a in enumerate(actions) if a['intent'] == 'prove'}
        if len(self._proof_index) != sum(a['intent'] == 'prove' for a in actions):
            raise ValueError('one bounded prove action per claim required')
        if target not in self._proof_index:
            raise ValueError('missing target proof action')

    def solve(self):
        actions, worlds = self.actions, self.worlds
        start = (0,) * len(actions)

        @lru_cache(None)
        def beliefs(observations):
            weights = []
            for w in worlds:
                p = w['probability']
                for a, o in zip(actions, observations):
                    if o:
                        p *= likelihood(a, w['truth'][a['claim']], OUTCOMES[o-1])
                weights.append(p)
            total = sum(weights)
            return tuple(p / total for p in weights) if total else ()

        def certificates(observations):
            proved = set(self.known)
            refuted = set()
            for a, o in zip(actions, observations):
                if o == 1:
                    proved.add(a['claim'])
                elif o == 3:
                    refuted.add(a['claim'])
            return proved, refuted

        def reachable(claim, observations, proved, refuted, stack=frozenset()):
            if claim in proved:
                return True
            if claim in refuted or claim in stack or claim not in self._proof_index:
                return False
            i = self._proof_index[claim]
            return not observations[i] and all(reachable(d, observations, proved, refuted, stack | {claim})
                                               for d in actions[i]['requires'])

        @lru_cache(None)
        def go(observations, remaining):
            proved, refuted = certificates(observations)
            if self.target in proved:
                return Value(1., 0., None)
            if not reachable(self.target, observations, proved, refuted):
                return Value(0., 0., None)
            belief = beliefs(observations)
            if not belief:
                raise ValueError('unreachable zero-probability observation')
            best = Value(0., 0., None)
            for i, a in enumerate(actions):
                if observations[i] or a['cost'] > remaining or not set(a['requires']) <= proved:
                    continue
                if a['claim'] in proved or a['claim'] in refuted:
                    continue
                success, future_cost = 0., 0.
                for code, outcome in enumerate(OUTCOMES, 1):
                    p = sum(b * likelihood(a, w['truth'][a['claim']], outcome) for b, w in zip(belief, worlds))
                    if p <= 0:
                        continue
                    next_obs = list(observations)
                    next_obs[i] = code
                    child = go(tuple(next_obs), remaining-a['cost'])
                    success += p * child.success
                    future_cost += p * child.expected_cost
                candidate = Value(success, a['cost']+future_cost, a['id'])
                tied = isclose(candidate.success, best.success, rel_tol=1e-12, abs_tol=0.)
                if (candidate.success > best.success and not tied) or (tied and candidate.expected_cost < best.expected_cost):
                    best = candidate
            return best

        first = go(start, self.budget)
        # A compact policy trace along successful proof observations; actual
        # observations must trigger a new state/contract review, not auto-execution.
        trace, observations, remaining = [], start, self.budget
        while True:
            choice = go(observations, remaining)
            if choice.action is None:
                break
            trace.append(choice.action)
            i = next(i for i, a in enumerate(actions) if a['id'] == choice.action)
            a = actions[i]
            code = 1 if a['intent'] == 'prove' else 4
            observations = tuple(code if j == i else o for j, o in enumerate(observations))
            remaining -= a['cost']
            if not beliefs(observations):
                break
        return {
            'first_action': first.action, 'success_probability': first.success,
            'expected_total_effort': first.expected_cost, 'budget': self.budget,
            'success_branch_trace': trace, 'states_evaluated': go.cache_info().currsize,
        }
