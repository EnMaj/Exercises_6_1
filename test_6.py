for a1 in "123456789":
    for a2 in "0123456789":
        for a3 in "0123456789":
            number_set = {a1, a2, a3}
            number_int = int(a1) * 100 + int(a2) * 10 + int(a3)
            if len(number_set) == 3 and number_int * 3 < 1000:
                summ_set = set(str(number_int * 3))
                if len(summ_set)== 3 and len(summ_set&number_set)== 0:
                    print(number_int, " + ", number_int, " + ", number_int, " = ", number_int * 3)