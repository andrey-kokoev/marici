"""Export one actual balanced source case into a kernel-checkable native WG.

Re-run the exact source checks, use their live objects (not a hand-copied JSON
fixture), and serialize every retained field. --check verifies existing bytes.
"""
import contextlib
import io
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    data = runpy.run_path(str(ROOT/'research/strominger/checkers/check_relation_wg_packets.py'))
# Nonzero singly-retained/forgotten witness, with forgotten middle event.
case = data['answers'][4]
assert len(case.left_cut.product.terms) == 8
data['verify'](case)


def alist(items):
    return '(' + ' ∷ '.join([*items, '[]']) + ')'


def datum(x):
    if isinstance(x, (bool, int)):
        return f'({"neg" if x < 0 else "nat"} {abs(int(x))})'
    if isinstance(x, str):
        assert x in ('e','v')
        return 'edge-tag' if x == 'e' else 'vertex-tag'
    assert isinstance(x, tuple), type(x)
    return '(tuple ' + alist([datum(v) for v in x]) + ')'


def term(item):
    (word, marks), coefficient = item
    return '(term ' + alist(map(str,word)) + ' ' + alist(map(str,marks)) + \
        f' {"true" if coefficient < 0 else "false"} {abs(coefficient)})'


def arrow(a):
    return f'(arrow {a.start} {a.end} ' + alist([term(t) for t in a.terms]) + ')'


# Source values are exported independently for each cut. The equalities below
# are checked on those literal values by Agda, not assumed via postulates.
lines = ['{-# OPTIONS --safe --cubical --guardedness #-}',
         'module ActualRelationPacketCase where',
         'open import Cubical.Foundations.Prelude',
         'open import Cubical.Data.Bool.Base using (true; false)',
         'open import Cubical.Data.List.Base using ([]; _∷_)',
         'open import Cubical.Data.Sum.Base using (inl; inr)',
         'open import Cubical.Data.Empty.Base using (⊥)',
         'open import Cubical.Data.Bool.Properties using (false≢true)',
         'open import RelationPacketEncoding', '']
for name, fp in [('leftCut', case.left_cut), ('rightCut', case.right_cut)]:
    lines += [name + ' : Factors', name + ' = factors',
              '  ' + arrow(fp.left), '  ' + arrow(fp.right),
              '  ' + arrow(fp.product), '  ' + datum(fp.raw),
              '  ' + datum(fp.balanced), '  refl refl refl', '']
# Include actual four-event factors/product AND computed attachment matrices.
a4, b4, p4 = (data[k] for k in ('a4','b4','p4'))
attachment = ((a4.start,a4.end,a4.terms),(b4.start,b4.end,b4.terms),
              (p4.product.start,p4.product.end,p4.product.terms),
              data['actual_action'],data['graded_action'])
q = case.request
lines += ['actual : Case', 'actual = record',
          '  { original = request ' + arrow(q.a) + ' ' + arrow(q.middle) + ' ' + arrow(q.b),
          '  ; cut-left = leftCut', '  ; cut-right = rightCut',
          '  ; attachment = ' + datum(attachment),
          '  ; same-product = refl', '  ; same-balanced = refl',
          '  ; nonzero-detector = refl }', '',
          '-- Execution uses the actual existing Layer1 signature.',
          'actual-generated : generate (inl actual) ≡ (inr (actual , solve actual) , reconciled actual)',
          'actual-generated = refl', '',
          '-- A cut-address detector rejects erasure of the distinct raw cuts.',
          'cut-is-left : Datum → Bool',
          'cut-is-left (tuple ((tuple ((tuple ((nat 7) ∷ rest)) ∷ tail)) ∷ rows)) = true',
          'cut-is-left _ = false', '',
          'different-raw-cuts : Factors.raw leftCut ≡ Factors.raw rightCut → ⊥',
          'different-raw-cuts p = false≢true (sym (cong cut-is-left p))', '']
# Need Bool type itself for the detector.
lines[3] = 'open import Cubical.Data.Bool.Base using (Bool; true; false)'
content = '\n'.join(lines)
path = ROOT/'research/strominger/agda/ActualRelationPacketCase.agda'
if '--check' in sys.argv:
    assert path.read_text(encoding='utf-8') == content, 'exported source drift'
    print('Actual relation export matches live checked source objects.')
else:
    path.write_text(content,encoding='utf-8')
    print('Exported actual eight-term relation case, both seam cuts and attachment evidence.')
