def solution(s):  # Definition of function solution accepting string s

    a = len(s)  # Finding length of the string

    f = 0  # Flag to find if any other transformation possible or not

    i = 0  # Index for the iteration throughout the string

    # Algorithm and main program starts from here

    while f == 0:
        while (i <= a - 2):
            if (s[i] == 'A' and s[i + 1] == 'B'):  # if AB found in the string remove AB from the string
                s = s.replace('AB', '')
                i = 0  # if transformation done we need to iterate from the beginning of the string so need to set i = 0
            else:
                if (s[i] == 'B' and s[i + 1] == 'A'):  # if BA found in the string remove BA from the string
                    s = s.replace('BA', '')
                    i = 0
                else:
                    if (s[i] == 'C' and s[i + 1] == 'D'):  # if CD found in the string remove CD from the string
                        s = s.replace('CD', '')
                        i = 0
                    else:
                        if (s[i] == 'D' and s[i + 1] == 'C'):  # if DC found in the string remove DC from the string
                            s = s.replace('DC', '')
                            i = 0
                        else:
                            f = 1
                            i = i + 1  # if none found increase index by one to check in the next pair of characters
                            a = len(s)  # Finding length of the transformed string


return (s)  # Returning transformed string
