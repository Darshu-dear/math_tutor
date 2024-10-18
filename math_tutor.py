import random 
import time
def math_tutor():
    no_of_q=int(input("How many questions do you want: "))
    high_val=int(input("How high should be the numbers? "))
    questions=[]
    operators=["+", "-", "*", "/"]
    answers=[]
    wrong_answers_index=[]
    wrong_answers=[]
    correct_answers=[]
    qs=[]
    percentage=0
    times=[]
    total_time=0
    for i in range(no_of_q*2):
        questions.append(random.randint(1, high_val))
    questions=list(questions[i: i+2] for i in range(0, len(questions), 2))
    for question in questions:
        question.insert(1, random.choice(operators))
        x=""
        for q in question:
           x=x+str(q)
        qs.append(x)  
    for q in qs:
        start=time.time()
        answer_input=float(input(f"Enter your answers: {q}")) 
        end=time.time()
        time_taken=end-start
        times.append(round(time_taken, 2))
        answers.append(answer_input)
    for ans in questions:
        if ans[1]=="+":
            correct_answers.append(ans[0]+ans[2])
        elif ans[1]=="-":
            correct_answers.append(ans[0]-ans[2])
        elif ans[1]=="*":
            correct_answers.append(ans[0]*ans[2])
        elif ans[1]=="/":
            correct_answers.append(round(ans[0]/ans[2], 2))
    for j in answers:
        if j not in correct_answers:
            wrong_answers_index.append(answers.index(j))
            wrong_answers.append(j)
    percentage=100-((len(wrong_answers_index)/len(correct_answers))*100)
    for k in times:
        total_time+=k
    total_time=round(total_time, 2)
    print("Congrats, you finished, thanks for playing")
    print(f"You got {wrong_answers_index} questions wrong")
    print(f"Your percentage of correct answers is {percentage}%")
    print(f"All questions: {qs}")
    print(f"All correct answers: {correct_answers}")
    print(f"You took {times} seconds per question and you took {total_time} seconds in total.")
math_tutor()