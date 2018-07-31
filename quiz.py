import csv, random
def take_quiz(questions, answer_booklet):
    points = 0
    quest = randomize(questions)
    print('Answer the following in "TRUE" or "FALSE"')
    for q in quest:
        ans = input(q+"\n")
        real_ans = answer_booklet[q]  
        
        if ans.title() == real_ans:
            print("Correct Answer")
            points += 1
        else:
            print("Incorrect Answer")
    print("your Score",points)
    
def randomize(questions):
    randoms, quests = [], []
    while not len(randoms) == 3:
        rand = random.randint(1,10)
        if rand not in randoms:
            randoms.append(rand)
    for var in randoms:
        quests.append(questions[var])
    return quests

def get_questions(filename):
    questions, answers = [],{}
    with open(filename,'r') as F:
        text = csv.reader(F)
        for row in text:
            questions.append(row[0])
            answers[row[0]] = row[1].title()
    return questions, answers

if __name__ == '__main__':
    q, a = get_questions('Q.csv')
    take_quiz(q, a)