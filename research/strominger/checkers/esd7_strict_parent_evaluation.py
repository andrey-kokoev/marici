"""Typed conditional word evaluation of the source strict joint-graph diagram.
Programs are in execution order (left to right), not printed matrix-product order.
Never evaluate analytical functions or erase the retained occurrence history.
"""
from itertools import combinations

READOUTS=['ell_plus','ell_minus','retained_residual']


def require(value,message):
    if not value:raise ValueError(message)


def validate_profile(profile):
    require(profile['schema']=='marici.esd7-strict-parent-profile.v1','unknown profile')
    require(profile['carrierPolicy']=='correlated-essential-images','uncorrelated or unrestricted carrier')
    require(profile['chart4']=='full-response-BQAC','scalar fourth chart is not reversible')
    require(profile['inverseLawScope']=='on-images-of-the-same-D-only','inverse law outside declared images')
    require(profile['completionExtension'] is False,'unsupported completion extension')
    require(profile['retainedReadouts']==READOUTS,'endpoint or residual readout erased/relabelled')
    require(profile['assumedSourceIdentities']==['R_i S_i = I_D','S_i R_i = I_on_S_i(D)'],'unrecognized source identities')
    require(set(profile['charts'])=={'1','2','3','4'},'missing source chart')


def symbol_type(token):
    if len(token)==2 and token[0] in 'SR' and token[1] in '1234':
        chart='V'+token[1]
        return ('D',chart) if token[0]=='S' else (chart,'D')
    if token.startswith('F:') and token[2:] in READOUTS:
        return 'D','Y:'+token[2:]
    raise ValueError('unbound operator symbol '+token)


def normalize(program,start):
    current=start; stack=[]; cancellations=[]
    for index,token in enumerate(program):
        source,target=symbol_type(token)
        require(current==source,'operator domain mismatch at '+token)
        current=target
        if stack and token[0] in 'SR' and stack[-1][1][0] in 'SR' and token[1:]==stack[-1][1][1:] and token[0]!=stack[-1][1][0]:
            previous,other=stack.pop()
            cancellations.append({'positions':[previous,index],'executionPair':[other,token],
                                  'hypothesis':'R_i S_i=I_D' if other[0]=='S' else 'S_i R_i=I_on_S_i(D)'})
        else:stack.append((index,token))
    return {'start':start,'target':current,'normalForm':[token for _,token in stack], 'cancellations':cancellations}


def transition(i,j):
    require(i in range(1,5) and j in range(1,5),'parent chart outside1..4')
    return [] if i==j else ['R'+str(i),'S'+str(j)]


def equivalent(a,b,start):
    x,y=normalize(a,start),normalize(b,start)
    return x['target']==y['target'] and x['normalForm']==y['normalForm']


def path_program(word):
    return [token for i,j in zip(word,word[1:]) for token in transition(i,j)]


def evaluate(refinement,profile):
    validate_profile(profile)
    require(refinement['parentOrder']==[1,2,3,4],'unadmitted parent direction convention')
    require(refinement['orientationConvention']=='reverse cumulative-coordinate vertex order','unrecorded fine orientation')
    records=[]; restriction_count=0; triple_count=0; tetra_count=0
    by_id={row['cell']:row for row in refinement['cells']}
    for cell in refinement['cells']:
        word=cell['parentWord']; require(word and word==sorted(word),'nonmonotone parent nerve word')
        program=path_program(word); start='V'+str(word[0])
        reduction=normalize(program,start)
        require(equivalent(program,transition(word[0],word[-1]),start),'parent path does not reduce')
        for a,b,c in combinations(cell['parentSupport'],3):
            require(equivalent(transition(a,b)+transition(b,c),transition(a,c),'V'+str(a)),'parent triangular equation')
            triple_count+=1
        for a,b,c,d in combinations(cell['parentSupport'],4):
            full=transition(a,b)+transition(b,c)+transition(c,d)
            left=transition(a,c)+transition(c,d)
            right=transition(a,b)+transition(b,d)
            require(equivalent(full,left,'V'+str(a)) and equivalent(left,right,'V'+str(a)) and
                    equivalent(right,transition(a,d),'V'+str(a)),'parent tetrahedral reductions disagree')
            tetra_count+=1
        for face in cell['faceRestrictions']:
            deleted=face['deleteParentPositions']
            kept=[i for i in range(len(word)) if i not in deleted]
            target=by_id[face['face']]
            require([word[i] for i in kept]==target['parentWord'],'shared face occurrence mismatch')
            # Evaluate each new adjacency as its ORIGINAL subpath. Do not
            # merely compare the outermost endpoint of the entire face.
            for i,j in zip(kept,kept[1:]):
                require(equivalent(path_program(word[i:j+1]),transition(word[i],word[j]),'V'+str(word[i])),
                        'restriction shortcut does not match parent composition')
                restriction_count+=1
        readouts=[]
        for f in READOUTS:
            composite=program+['R'+str(word[-1]),'F:'+f]
            expected=['R'+str(word[0]),'F:'+f]
            require(equivalent(composite,expected,start),'retained observable square')
            readouts.append({'observable':f,'program':composite,'normalForm':normalize(composite,start)['normalForm'],
                             'zeroAssumed':False})
        records.append({'cell':cell['cell'],'parentOccurrences':[
            {'position':i,'chart':chart} for i,chart in enumerate(word)],
            'executionProgram':program,'reduction':reduction,
            'retainedReadoutSquares':readouts,'orientationRelativeToGeometry':cell['orientationRelativeToGeometry'],
            'identitiesSkippedInProgramOnly':sum(a==b for a,b in zip(word,word[1:])),
            'conditionalStrictChartEvaluation':True,'intendedAnalyticalWitnessBindingEstablished':False})
    return {'cells':records,'counts':{'cells':len(records),'restrictionAdjacencies':restriction_count,
            'parentTriangleInstances':triple_count,'parentTetrahedronInstances':tetra_count,'readoutSquares':3*len(records)},
            'sourceIdentitiesAssumed':True,'conditionalStrictDiagramEvaluationEstablished':True,
            'intendedAnalyticalWitnessBindingEstablished':False,'native44TransportBindingEstablished':False,
            'full114ChannelEstablished':False,'completionExtensionEstablished':False}
