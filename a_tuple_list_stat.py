
def Average(lst): 
	return sum(lst) / len(lst)
def Minim(lst):
    return min(lst)
def Maxi(lst):
    return max(lst)
def Dupl(lst):
    dup = []
    for i in lst:
        if lst.count(i) > 1:
            dup.append(i)
    return dup 
def ascend(lst):
    return sorted(lst)
def descend(lst):
    return sorted(lst, reverse=True)


def main():
    lst = [1,1,2,3,3,4,5,5] 
    average = Average(lst)
    minim = Minim(lst)
    maxi = Maxi(lst)
    dupl = Dupl(lst)

    print("Average of the list =", round(average, 2)) 
    print("Maximum of the list =", round(maxi, 2))
    print("Minimum of the list =", round(minim, 2))
    print("Duplicants of the list =", (dupl))
    print("Here it is sorted ascendingly =", (ascend(lst)))
    print("Here it is sorted descendingly =", (descend(lst)))

if __name__== "__main__":
    main()