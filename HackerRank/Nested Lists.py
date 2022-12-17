if __name__ == '__main__':
    scores=[]
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        student.append([name,score])
        
    scoresset=list(set(scores))
    scoresset.sort()
    student.sort()
    
    for i in range(len(student)):
        if scoresset[1]==student[i][1]:
            print(student[i][0])       
