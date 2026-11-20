"""Exhaust just the optional one-step translation branch of the blind anchor test."""
from collections import Counter

def main():
    counts=Counter()
    for mask in range(128):
        d={1,7}|{11+i for i in range(7) if mask>>i&1};s=d|{35-i for i in d}
        if any((x+y)%35 in s for x in s for y in s):continue
        counts['triangle-free']+=1;ind=[0]
        for j in range(35):
            row=sum(1<<i for i in range(j) if j-i in s)
            ind.extend([p|1<<j for p in ind if not p&row]);
            if any(p.bit_count()==9 for p in ind):break
        else:print('valid',sorted(d));counts['valid']+=1
    print(counts)
if __name__=='__main__':main()
