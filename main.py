
from mcqmod import quiz

class platform:      


    def __init__(self):
        self.easy_quiz = {}    #list of quiz objects(quizes) for easy level
        self.med_quiz= {}    #list of quiz objects(quizes) for medium level
        self.hard_quiz= {}    #list of quiz objects(quizes) for hard level
        while True:
            print('Are you \n1)superuser\n2)student\n3)exit')
            usr=int(input())
            if usr==1:
                self.superuser()    #if u r superuser superuser function of interface will be called
            elif usr==2:
                self.student()
            else:
                break


    def superuser(self):
        print('1)create quiz\n2)modify a quiz')
        c=int(input())
        print('enter name of quiz')
        qname = input()
        print('select level\n1)easy\n2)medium\n3)hard')
        k = int(input())

        if c==2:    #if superuser wants to modify an existing quiz
            if k==1:
                if qname in self.easy_quiz:
                    print('quiz found ')
                    print('1)add question\n2)modify existing question')
                    s=int(input())
                    if s==2:
                        print('enter question number you want to modify')
                        qno=int(input())
                        self.easy_quiz[qname].createquestions(qno)
                    elif s==1:
                        l=len(self.easy_quiz[qname].q_list)
                        self.easy_quiz[qname].createquestions(l+1)
                else:
                    print('no such quiz exists')

            elif k==2:
                if qname in self.med_quiz:
                    print('quiz found ')
                    print('1)add question\n2)modify existing question')
                    s=int(input())
                    if s==2:
                        print('enter question number you want to modify')
                        qno=int(input())
                        self.med_quiz[qname].createquestions(qno)
                    elif s==1:
                        l=len(self.med_quiz[qname].q_list)
                        self.med_quiz[qname].createquestions(l+1)
                else:
                    print('no such quiz exists')

            elif k==3:
                if qname in self.hard_quiz:
                    print('quiz found ')
                    print('1)add question\n2)modify existing question')
                    s=int(input())
                    if s==2:
                        print('enter question number you want to modify')
                        qno=int(input())
                        self.hard_quiz[qname].createquestions(qno)
                    elif s==1:
                        l=len(self.hard_quiz[qname].q_list)
                        self.hard_quiz[qname].createquestions(l+1)
                else:
                    print('no such quiz exists')
            else:
                print('invalid choice of level')


        elif c==1:    # if superuser wants to create a new quiz
            print('how many questions you want to add into the quiz')
            n = int(input())
            if k==1:
                self.easy_quiz[qname]=quiz()
                for i in range(n):
                    self.easy_quiz[qname].createquestions(i+1)
            elif k==2:
                self.med_quiz[qname]=quiz()
                for i in range(n):
                    self.med_quiz[qname].createquestions(i+1)
            elif k==3:
                self.hard_quiz[qname]=quiz()
                for i in range(n):
                    self.hard_quiz[qname].createquestions(i+1)
            else:
                print('invalid choice')
        else:
            print('invalid choice')



    def student(self):
        print('enter your name')
        n=input()
        print('enter your email id')
        e=input()
    
        while True:
            print('select level\n1)easy\n2)medium\n3)hard')
            k = int(input())
            if k==1:
                if len(self.easy_quiz)==0:
                    print('no quiz available please try again later')
                else:
                    print('list of quizs available')
                    for val in self.easy_quiz:
                        print(val)
                    print('name the quiz you want to solve')
                    choice=input()
                    self.easy_quiz[choice].solve()
                    m=self.easy_quiz[choice].score()
                    print('Name:',n)
                    print('Email ID:',e )
                    print(m)
                    self.easy_quiz[choice].show_answers()

            elif k==2:
                if len(self.med_quiz)==0:
                    print('no quiz available please try again later')
                else:
                    print('list of quizs available')
                    for val in self.med_quiz:
                        print(val)
                    print('name the quiz you want to solve')
                    choice=input()
                    self.med_quiz[choice].solve()
                    m=self.med_quiz[choice].score()
                    print('Name:',n)
                    print('Email ID:',e )
                    print(m)
                    self.med_quiz[choice].show_answers()

            elif k==3:
                if len(self.hard_quiz)==0:
                    print('no quiz available please try again later')
                else:
                    print('list of quizs available')
                    for val in self.hard_quiz:
                        print(val)
                    print('name the quiz you want to solve')
                    choice=input()
                    self.hard_quiz[choice].solve()
                    m=self.hard_quiz[choice].score()
                    print('Name:',n)
                    print('Email ID:',e )
                    print(m)
                    self.hard_quiz[choice].show_answers()
            else:
                print('invalid choice of level')

            print('Want to solve another quiz\n1)yes\n2)no')
            sel = int(input())
            if sel == 2:
                break
            elif sel==1:
                continue
            else:
                print('invalid choice')


P= platform()