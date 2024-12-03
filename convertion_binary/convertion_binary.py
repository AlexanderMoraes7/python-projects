def convertion_binary(binary, base = 2):
    """Binary is the binary digit,
        By default is base 2
        others examples:
            2, binary digit
            8, octal digit
            16, hexadecimal digit
    """
    binary = str(binary)
    length = len(binary)
    result = 0

    if base == 2:
        for i in range(length):
            if binary[i] != "1" and binary[i] != "0":
                return "you can enter only 1 or 0"
            length -= 1
            if binary[i] == "0":
                continue
            result += int(binary[i]) * (base ** length)
        return result

    if base == 8:
        allow_octal = "0123456789"
        for i in range(length):
            if binary[i] not in allow_octal:
                return "you can enter only octal digits"
            length -= 1
            result += int(binary[i]) * (base ** length)
        return result

    if base == 16:
        binary = binary.upper()
        allow_hexa = "0123456789ABCDEF"
        for i in range(length):            
            if binary[i] not in allow_hexa:
                return "you can enter only hexadecimal digits"
            length -= 1
            match binary[i]:
                case "A":
                    result += 10 * (base ** length)
                    continue
                case "B":
                    result += 11 * (base ** length)
                    continue
                case "C":
                    result += 12 * (base ** length)
                    continue
                case "D":
                    result += 13 * (base ** length)
                    continue
                case "E":
                    result += 14 * (base ** length)
                    continue
                case "F":
                    result += 15 * (base ** length)
                    continue
            result += int(binary[i]) * (16 ** length)
        return result

print(convertion_binary(100101)) # Output 37
print(convertion_binary(764,8)) # Output 500
print(convertion_binary("b3ad",16)) # Output 45997
