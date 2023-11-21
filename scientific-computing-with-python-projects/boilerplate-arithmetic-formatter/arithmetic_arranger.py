def parse_exmaple(example: str) -> str:
    operand1, operator, operand2 = example.split()
    len1, len2 = map(len, [operand1, operand2])

    

    if operator not in "+-":
        raise Exception("Error: Operator must be '+' or '-'.")
    if not (operand1.isnumeric() and operand2.isnumeric()):
        raise Exception("Error: Numbers must only contain digits.")
    if max(len(operand1), len(operand2)) > 4:
        raise Exception("Error: Numbers cannot be more than four digits.")
    
    
    result = str(eval(example))
    len3 = len(result)
    if result.startswith("-"):
        len3 -= 1

    max_len = max(len1, len2, len3)

    first_line = (max_len+2-len1)*" "+operand1
    second_line = operator+(max_len+1-len2)*" "+operand2
    third_line = (max_len+2)*"-"

    output = f"{first_line}\n{second_line}\n{third_line}"
    if result.startswith("-"):
        output += f"\n{(max_len+1-len3)*' '+result}"
    else:
        output += f"\n{(max_len+2-len3)*' '+result}"
        
    return output

def arithmetic_arranger(problems, compute_result=False):
    if len(problems) > 5:
        raise Exception("Error: Too many problems.")
    parsed = [parse_exmaple(problem) for problem in problems]

    first_lines = []
    second_lines = []
    third_lines = []
    results = []


    for example in parsed:
        part1, part2, part3, part4 = example.split("\n")
        first_lines.append(part1)
        second_lines.append(part2)
        third_lines.append(part3)
        results.append(part4)
    result = ""

    result += "    ".join(first_lines)+"\n"
    result += "    ".join(second_lines)+"\n"
    result += "    ".join(third_lines)

    if compute_result:
        result += "\n"+"    ".join(results)
    return result

if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print()
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
    print()
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))