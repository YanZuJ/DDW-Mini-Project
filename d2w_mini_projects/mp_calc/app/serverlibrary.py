

#Each merge function has a byfunc parameter
def merge(array, p, q, r, byfunc=None):
    nleft = q - p + 1
    nright = r - q
    left_array = []
    right_array = []
    for idx in range(p,q+1):
        left_array.append(array[idx])
    for idx2 in range(q+1,r+1):
        right_array.append(array[idx2])
    left = 0
    right = 0
    dest = p
    while left < nleft and right < nright :
        # Implement byfunc function on elements in array if byfunc exists
        if (byfunc is None and left_array[left] <= right_array[right]) or (byfunc is not None and byfunc(left_array[left]) <= byfunc(right_array[right])):
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r, byfunc=None):
    if r - p > 0:
        q = int((p + r)/2)
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc=None):
    p = 0
    r = len(array)-1
    mergesort_recursive(array,p,r,byfunc)

class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





