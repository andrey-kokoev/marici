"""Equivalent experimental encodings of the archived native assembly queries."""
import z3

MODES=('baseline','pruned-int','scc-int','scc-bv','scc-cuts')

def adjacency(ids,operations):
    incoming={i:set() for i in ids};outgoing={i:set() for i in ids}
    for op in operations:
        a,b=op['source'],op['target']
        if a in outgoing and b in incoming:
            outgoing[a].add(b);incoming[b].add(a)
    return incoming,outgoing

def closure(starts,edges):
    reached=set(starts);queue=list(starts)
    for node in queue:
        for target in edges[node]:
            if target not in reached:reached.add(target);queue.append(target)
    return reached

def components(ids,outgoing,incoming):
    seen=set();order=[]
    for start in ids:
        if start in seen:continue
        stack=[(start,False)]
        while stack:
            node,finished=stack.pop()
            if finished:order.append(node);continue
            if node in seen:continue
            seen.add(node);stack.append((node,True))
            stack.extend((v,False) for v in sorted(outgoing[node],reverse=True) if v not in seen)
    owner={};groups=[]
    for start in reversed(order):
        if start in owner:continue
        index=len(groups);group=[];queue=[start];owner[start]=index
        for node in queue:
            group.append(node)
            for target in incoming[node]:
                if target not in owner:owner[target]=index;queue.append(target)
        groups.append(tuple(group))
    return owner,groups

def preprocess(p):
    root=p['root'];forbidden={b for a,b in p['conflicts'] if a==root}|{a for a,b in p['conflicts'] if b==root}
    ids=[i for i in p['packets'] if i not in forbidden]
    conflicts={frozenset((a,b)) for a,b in p['conflicts']}
    operations=[op for op in p['operations'] if frozenset((op['source'],op['target'])) not in conflicts]
    incoming,outgoing=adjacency(ids,operations)
    if root not in outgoing:return [],[]
    active=closure([root],outgoing)&closure([i for i in p['exits'] if i in incoming],incoming)
    return [i for i in ids if i in active],[op for op in operations if op['source'] in active and op['target'] in active]

def build(p,mode,timeout_ms,seed=0):
    if mode not in MODES:raise ValueError('Unknown encoding')
    if mode=='baseline':return baseline(p,timeout_ms,seed)
    ids=p['packets'];x={i:z3.Bool('packet_'+str(i)) for i in ids}
    active,operations=(ids,p['operations']) if mode=='baseline' else preprocess(p)
    incoming,outgoing=adjacency(active,operations);alive=set(active)
    s=z3.Solver();s.set(timeout=timeout_ms,random_seed=seed)
    s.add(x[p['root']])
    for i in ids:
        if i not in alive:s.add(z3.Not(x[i]))
    for a,b in p['conflicts']:s.add(z3.Or(z3.Not(x[a]),z3.Not(x[b])))
    local=mode.startswith('scc');owner,groups=components(active,outgoing,incoming) if local else ({i:0 for i in active},[tuple(active)])
    entry={};exit_rank={};bv=mode=='scc-bv';cuts=mode=='scc-cuts';cut_count=0
    if cuts:
        if any(len(group)>12 for group in groups):raise ValueError('SCC subset-cut budget exceeded')
        exits=set(p['exits'])
        for group in groups:
            group=sorted(group)
            for mask in range(1,1<<len(group)):
                subset={v for j,v in enumerate(group) if mask&(1<<j)}
                present=z3.Or(*[x[i] for i in sorted(subset)])
                if p['root'] not in subset:
                    edges=[z3.And(x[i],x[j]) for i in sorted(subset) for j in incoming[i] if j not in subset]
                    s.add(z3.Implies(present,z3.Or(*edges)));cut_count+=1
                if not subset.intersection(exits):
                    edges=[z3.And(x[i],x[j]) for i in sorted(subset) for j in outgoing[i] if j not in subset]
                    s.add(z3.Implies(present,z3.Or(*edges)));cut_count+=1
    for i in ([] if cuts else active):
        size=len(groups[owner[i]])
        if local and size==1:continue
        if bv:
            bits=max(1,(size-1).bit_length())
            entry[i]=z3.BitVec('entry_'+str(i),bits);exit_rank[i]=z3.BitVec('exit_'+str(i),bits)
            if size<(1<<bits):s.add(z3.Implies(x[i],z3.And(z3.ULT(entry[i],size),z3.ULT(exit_rank[i],size))))
        else:
            entry[i]=z3.Int('entry_'+str(i));exit_rank[i]=z3.Int('exit_'+str(i))
            # Preserve baseline formula and bounds; pruned mode uses its active size.
            s.add(z3.Implies(x[i],z3.And(entry[i]>=0,entry[i]<size,exit_rank[i]>=0,exit_rank[i]<size)))
    def lower(j,i,ranks):
        if local and owner[j]!=owner[i]:return z3.BoolVal(True)
        if local and j==i:return z3.BoolVal(False)
        return z3.ULT(ranks[j],ranks[i]) if bv else ranks[j]<ranks[i]
    if p['root'] in entry:s.add(entry[p['root']]==0)
    for i in ([] if cuts else active):
        if i!=p['root']:s.add(z3.Implies(x[i],z3.Or(*[z3.And(x[j],lower(j,i,entry)) for j in incoming[i]])))
        if i in p['exits']:
            if i in exit_rank:s.add(z3.Implies(x[i],exit_rank[i]==0))
        else:s.add(z3.Implies(x[i],z3.Or(*[z3.And(x[j],lower(j,i,exit_rank)) for j in outgoing[i]])))
    y=[z3.Or(*[x[i] for i in body['packets']]) for body in p['bodies']]
    for species,count in p['target'].items():
        terms=[(y[i],1) for i,body in enumerate(p['bodies']) if body['species']==species]
        s.add(z3.PbEq(terms,count) if terms else z3.BoolVal(count==0))
    for contact in p['contacts']:
        a,b=contact['bodies'];witness=z3.Or(*[z3.And(x[i],x[j]) for i,j in contact['links']])
        s.add(z3.Implies(z3.And(y[a],y[b]),witness))
    return s,x,{'inputPackets':len(ids),'activePackets':len(active),'inputOperations':len(p['operations']),'activeOperations':len(operations),
                'rankVariables':len(entry)+len(exit_rank),'components':len(groups) if local else None,
                'maxComponentSize':max(map(len,groups),default=0) if local else None,'subsetCuts':cut_count}

def baseline(p,timeout_ms,seed):
    # Preserve the production encoder's names, assertion order, and set iteration.
    ids=p['packets'];x={i:z3.Bool('packet_'+str(i)) for i in ids}
    entry={i:z3.Int('entry_'+str(i)) for i in ids};exit_rank={i:z3.Int('exit_'+str(i)) for i in ids}
    s=z3.Solver();s.set(timeout=timeout_ms,random_seed=seed)
    s.add(x[p['root']],entry[p['root']]==0)
    incoming,outgoing=adjacency(ids,p['operations'])
    for a,b in p['conflicts']:s.add(z3.Or(z3.Not(x[a]),z3.Not(x[b])))
    for i in ids:
        s.add(z3.Implies(x[i],z3.And(entry[i]>=0,entry[i]<len(ids),exit_rank[i]>=0,exit_rank[i]<len(ids))))
        if i!=p['root']:s.add(z3.Implies(x[i],z3.Or(*[z3.And(x[j],entry[j]<entry[i]) for j in incoming[i]])))
        if i in p['exits']:s.add(z3.Implies(x[i],exit_rank[i]==0))
        else:s.add(z3.Implies(x[i],z3.Or(*[z3.And(x[j],exit_rank[j]<exit_rank[i]) for j in outgoing[i]])))
    y=[z3.Or(*[x[i] for i in body['packets']]) for body in p['bodies']]
    for species,count in p['target'].items():
        terms=[(y[i],1) for i,b in enumerate(p['bodies']) if b['species']==species]
        s.add(z3.PbEq(terms,count) if terms else z3.BoolVal(count==0))
    for contact in p['contacts']:
        a,b=contact['bodies'];witness=z3.Or(*[z3.And(x[i],x[j]) for i,j in contact['links']])
        s.add(z3.Implies(z3.And(y[a],y[b]),witness))
    return s,x,{'inputPackets':len(ids),'activePackets':len(ids),'inputOperations':len(p['operations']),'activeOperations':len(p['operations']),'rankVariables':2*len(ids),'components':None,'maxComponentSize':None}

def validate_selection(p,selection):
    """Direct Boolean/graph check, independent of rank constraints and Z3."""
    chosen=set(selection)
    if len(chosen)!=len(selection) or not chosen<=set(p['packets']) or p['root'] not in chosen:return False
    if any(a in chosen and b in chosen for a,b in p['conflicts']):return False
    occupied=[bool(chosen.intersection(body['packets'])) for body in p['bodies']]
    if any(sum(occupied[i] for i,b in enumerate(p['bodies']) if b['species']==species)!=count for species,count in p['target'].items()):return False
    for contact in p['contacts']:
        a,b=contact['bodies']
        if occupied[a] and occupied[b] and not any(i in chosen and j in chosen for i,j in contact['links']):return False
    incoming,outgoing=adjacency(chosen,p['operations'])
    return closure([p['root']],outgoing)==chosen and closure(chosen.intersection(p['exits']),incoming)==chosen
