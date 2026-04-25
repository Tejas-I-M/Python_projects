class Question:
    def __init__(self,text,options,correct_ans):
        self.text = text
        self.options = options
        self.correct_ans=correct_ans
class Quiz:
    def __init__(self):
        self.questions=[]
        self.score=0
    def add_question(self,question):
        self.questions.append(question)
    def start(self):
        if not self.questions:
            print("No questions!!")
            return
        for q in self.questions:
            print("\n", q.text)

            for i, option in enumerate(q.options,start=1):
                print(f'{i}. {option}')
            while True:
                try:
                    ans = int(input(f"Enter your option (1-4): "))
                    if 1 <= ans <= len(q.options):
                        break
                    else:
                        print(f"Enter a valid option between (1-4)!")
                except ValueError:
                    print("enter a valid option")
            if q.options[ans-1]==q.correct_ans:
                print("Correct!")
                self.score+=1
            else:
                print(f"Wrong! The correct answer is {q.correct_ans}")
        print(f"Score: {self.score}/{len(self.questions)}")
        print(f"Percentage: {(self.score/len(self.questions))*100:.2f}")
q1 = Question("1+1=?",["1","2","3","4"],"2")
q2 = Question("2*2=?",["1","2","3","4"],'4')

quiz = Quiz()

quiz.add_question(q1)
quiz.add_question(q2)
quiz.start()