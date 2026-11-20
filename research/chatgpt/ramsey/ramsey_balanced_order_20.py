"""Fully refine by local balance; emit pivot, positive branch, negative branch."""
import csv
from pathlib import Path
from ramsey_min_diff_order import balanced_choices, build


def order(rows, group):
    if group.bit_count() <= 1:
        return [group.bit_length()-1] if group else []
    _, i, plus, minus = balanced_choices(rows, group)[0]  # first current index wins ties
    return [i] + order(rows, plus) + order(rows, minus)


def main():
    full = (1 << 20) - 1
    rows = [r & full for r in build()[:20]]
    p = order(rows, full)
    assert sorted(p) == list(range(20))
    result = [sum(((rows[i] >> j) & 1) << t for t,j in enumerate(p)) for i in p]
    assert order(result, full) == list(range(20)), 'second pass must preserve order'
    path = Path(__file__).with_name('ramsey_balanced_order_20.csv')
    with path.open('w',newline='') as f:
        w = csv.writer(f); w.writerow(['address', *p]);
        for i,r in zip(p,result): w.writerow([i,*[(r>>t)&1 for t in range(20)]])
    print('order:',p,'; unchanged on second pass')

if __name__=='__main__':main()
