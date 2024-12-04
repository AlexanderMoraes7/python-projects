def sum_point(ops = []):
    x = 0
    letters = ''
    record = []
    for i in ops:
        if i == "+":
            record.append(record[-1] + record[-2])
        elif i == "D":
            record.append(2 * record[-1] )
        elif i == "C":
            del record[-1]
        else:
            record.append(int(i))

    for i in range(len(record)):
        if i == len(record) -1:
            letters += str(record[i]) + " = "
        else:
            letters += str(record[i]) + " + "
        x += record[i]

    return f"The total sum is {letters}{x}"

print(sum_point(["5","-2","4","C","D","9","+","+"]))

# Output is 27