#coding=utf-8
"""
several common sorting algorithms

"""

def Bubble_sort(seq):
    '''
    时间复杂度 O(n**2),稳定排序
    :param seq:
    :return:
    '''
    L = len(seq)
    for i in range(L):
        for j in range(L-i-1):
            if seq[j] > seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
    return seq

def Selection_sort(seq):
    '''
    时间复杂度O(n**2),稳定排序
    :param seq:
    :return:
    '''
    L = len(seq)
    for i in range(L):
        for j in range(i+1,L):
            if seq[i] > seq[j]:
                seq[i],seq[j] = seq[j],seq[i]
    return seq

def Insert_sort(seq):
    '''
    0(n**2),稳定排序，有适应性:最坏O(n**2),最好O(n)
    :param seq:
    :return:
    '''
    L = len(seq)
    for i in range(1,L):
        key = seq[i]
        j = i-1
        while j >= 0 and key < seq[j]:
            seq[j+1] = seq[j]
            j = j-1
        seq[j] = key
    return seq

def Quick_sort(seq):
    '''
    O(nlogn),最坏情况O(n**2),不稳定排序
    :param seq:
    :return:
    '''
    L = len(seq)
    if L < 2:
        return seq
    else:
        pivot = seq[0]
        left,right = [],[]
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else :
                right.append(x)
        return Quick_sort(left) + [pivot] + Quick_sort(right)


def Merge_sort(seq):
    '''
    O(nlogn),稳定排序
    :param seq:
    :return:
    '''
    if len(seq) < 2:
        return seq
    result = []
    middle = int(len(seq)/2)
    left = Merge_sort(seq[:middle])
    right = Merge_sort(seq[middle:])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(Merge_sort(left))
    else:
        result.extend(Merge_sort(right))
    return result


if __name__ == "__main__":
    from time import clock
    import random
    seq = []
    for i in range(999): #python 有一个可用递归深度限制，我的电脑为1000次
        seq.append(random.randint(1,10000))
    #Bubble
    bubble_start = clock()
    Bubble_sort(seq)
    bubble_end = clock()
    print 'Bubble_sort cost time: %s' % (bubble_end - bubble_start)
    #Selection
    selection_start = clock()
    Selection_sort(seq)
    selection_end = clock()
    print 'Selection_sort cost time: %s' % (selection_end - selection_start)
    #Insert
    t3_start = clock()
    Insert_sort(seq)
    t3_end = clock()
    print 'Insert_sort cost time: %s' % (t3_end - t3_start)
    #Quick
    t4_start = clock()
    Quick_sort(seq)
    t4_end = clock()
    print 'Quick_sort cost time: %s' % (t4_end - t4_start)
    #Merge
    t5_start = clock()
    Merge_sort(seq)
    t5_end = clock()
    print 'Merge_sort cost time: %s' % (t5_end - t5_start)
    # merge_sorted = Merge_sort(seq)
    # print merge_sorted