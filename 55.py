import copy

def sol1(inlist, coms):
    _inlist = copy.deepcopy(inlist)
    outlist = []
    sumout = []

    for i in range(coms):
        outlist.append([])
        sumout.append(0)
    
    total_time = sum(_inlist)
    avg_time = total_time / coms
    
    for j in range(coms):
        if True in [k >= avg_time for k in _inlist]:
            for m in tuple(_inlist):
                if m >= avg_time:                    
                    outlist[j].append(m)
                    _inlist.remove(m)
                    sumout[j] += m
                    break
        else:
            for n in tuple(_inlist):
                outlist[j].append(n)
                _inlist.remove(n)
                sumout[j] += n
                if sumout[j] >= avg_time:
                    break
    
    return outlist

def sol2(inlist, coms):
    _inlist = copy.deepcopy(inlist)
    outlist = []
    sumout = []
    for x in range(coms):
        outlist.append([])
        sumout.append(0)
    
    _inlist.sort(reverse=True)
    
    for bread in _inlist:
        lowbasket = sumout.index(min(sumout))
        outlist[lowbasket].append(bread)
        sumout[lowbasket] += bread
    
    return outlist

if __name__ == '__main__':
    inlist = [3,5,2]
    coms = 2
    optimal = [[5], [3, 2]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('average:', sum(inlist) / coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))
    print('===========================')
    
    inlist = [3,15,6,22,13,2]
    coms = 3
    optimal = [[22], [15, 6], [13, 3, 2]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('average:', sum(inlist) / coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))
    print('===========================')

    inlist = [7,8,9,10,11]
    coms = 2
    optimal = [[11, 10], [9, 8, 7]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('average:', sum(inlist) / coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))
    print('===========================')
    
    inlist = [1, 1, 1, 2, 2, 2, 7, 8, 30, 40]
    coms = 3
    optimal = [[40], [30], [8, 7, 2, 2, 2, 1, 1, 1]]
    print('inlist:', inlist)
    print('coms:', coms)
    print('average:', sum(inlist) / coms)
    print('optimal:', optimal)
    print('sol1:', sol1(inlist, coms))
    print('sol2:', sol2(inlist, coms))
    print('===========================')
