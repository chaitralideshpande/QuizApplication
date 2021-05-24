
from q_mod import question
class quiz:

    def __init__(self):         #quiz has an empty dict of questions at the time of obj creation.
        self.q_list={}   #this dict will be used to store reference to all the question objects belonging to a particular quiz


    def createquestions(self,j):
        print('type question')
        qs=input()
        print('give 4 options')
        opl=[]
        for i in range(4):        #taking 4 options
            print(i+1,end=' ')
            opl.append(input())
        print('enter correct option')
        a=int(input())
        self.q_list[j]=question(qs,opl,a)  #reference of question stored in dict
    
    def solve(self):                       #quiz would be solveed using 2 methods...display first and then select_option
        for i in range(len(self.q_list)):
            self.q_list[i+1].displayquestion()
            self.q_list[i+1].select_option()


    def score(self):
        marks=0
        length=len(self.q_list)
        total=2*length
        for i in range(len(self.q_list)):
            if self.q_list[i+1].test():     #marks will be increases whenever test function of question obj returns true
                marks+=2
        return str(marks)+' scored out of '+str(total)
    
    def show_answers(self):
        for i in range(len(self.q_list)):
            print('answer to question',i+1,end=' ')
            x=self.q_list[i+1].correct
            print(x,self.q_list[i+1].options[x-1])