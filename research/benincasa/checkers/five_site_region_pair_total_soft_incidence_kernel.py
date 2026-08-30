import json
from fractions import Fraction
from pathlib import Path

root=Path('research/benincasa/results')
data=json.loads((root/'five-site-region-pair-total-soft-occurrence-support.json').read_text())
labels=data['distinct_physical_labels']
occ=[x for rec in data['records'] for x in rec['surviving_labels']]
assert len(labels)==16 and len(occ)==50

# Columns are labelled pole occurrences; rows are surviving source labels.
matrix=[[Fraction(int(x==label)) for x in occ] for label in labels]

def rank(a):
    a=[row[:] for row in a]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; z=a[r][c]
        a[r]=[x/z for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

r=rank(matrix)
assert r==16
kernel=50-r; cokernel=16-r
assert kernel==34 and cokernel==0

# C5 characters: occurrence space is ten regular representations.  The label
# space is one fixed G line plus three regular five-element orbits.
chi_occ=[50,0,0,0,0]
chi_labels=[16,1,1,1,1]
chi_kernel=[a-b for a,b in zip(chi_occ,chi_labels)]
assert chi_kernel==[34,-1,-1,-1,-1]
assert (chi_kernel[0]+sum(chi_kernel[1:]))//5==6
assert (chi_kernel[0]-chi_kernel[1])//5==7

packet={
 'schema':'marici.five_site_region_pair_total_soft_incidence_kernel.v1',
 'map':'Q^{50}_pole_occurrences -> Q^{16}_surviving_source_labels',
 'rank':r,
 'kernel_rank':kernel,
 'cokernel_rank':cokernel,
 'occurrence_character':chi_occ,
 'label_character':chi_labels,
 'kernel_character':chi_kernel,
 'rational_kernel_decomposition':'6*Q_triv + 7*Q(zeta_5)',
 'chartwise_cancellation_relations':5,
 'removed_occurrences_in_cancellations':10,
 'classification':'pure occurrence redundancy before coefficient differential',
 'new_carrier_datum':False,
}
(root/'five-site-region-pair-total-soft-incidence-kernel.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
