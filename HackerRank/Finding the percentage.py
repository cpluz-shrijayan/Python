if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    liist=[]
    liist = student_marks[query_name]
    j=0
    for i in liist:
        j=j+i
    print(format(j/len(liist), '.2f'))
