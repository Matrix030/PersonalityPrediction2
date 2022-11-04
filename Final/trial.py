

from sklearn import datasets, linear_model 
import numpy as np
import pandas as pd

data =pd.read_csv('training_dataset.csv')
array = data.values
for i in range(len(array)):
        if array[i][0]=="Male":
            array[i][0]=1
        else:
            array[i][0]=0

df=pd.DataFrame(array)

maindf =df[[0,1,2,3,4,5,6]]
mainarray=maindf.values
X = mainarray

temp=df[7]
Y =temp.values

from sklearn.linear_model import LogisticRegression
classifier = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
classifier.fit(X, Y)



openness = 0
neuroticism = 0
conscientiousness = 0
agreeableness = 0
extraversion = 0

brief = input("Below is a Personlaity Test you have two choices. Press a to Agree and b to Disagree. If you wish to  take the test please press y to start: ")

while brief == "y":
    open_array = []
    neuro_array = []
    couns_array = []
    agree_array = []
    extr_array = []

    q1 = input("1) I do not have a good imagination: ")
    open_array.append(q1)
    q2 = input("2) I am quick to understand things: ")
    open_array.append(q2)
    q3 = input("3) I have difficulty understanding abstract ideas: ")
    open_array.append(q3)
    q4 = input("4) I spend time reflecting on things: ")
    open_array.append(q4)
    q5 = input("5) I am full of ideas.: ")
    open_array.append(q5)
    # print(open_array)
    for i in range(len(open_array)):
        if open_array[i] == "a":
            openness += 1
    


    q6 = input("6) I worry about things: ")
    neuro_array.append(q6)
    q7 = input("7) I am easily disturbed: ")
    neuro_array.append(q7)
    q8 = input("8) I am relaxed most of the time: ")
    neuro_array.append(q8)
    q9 = input("9) I get stressed out easily: ")
    neuro_array.append(q9)
    q10 = input("10) I get upset easily: ")
    neuro_array.append(q10)
    # print(neuro_array)
    for i in range(len(neuro_array)):
        if neuro_array[i] == "a":
            neuroticism += 1
    
    


    q11 = input("11) I follow a schedule: ")
    couns_array.append(q11)
    q12 = input("13) I pay attention to details: ")
    couns_array.append(q12)
    q13 = input("13) I leave my belongings around: ")
    couns_array.append(q13)
    q14 = input("14) I make a mess of things: ")
    couns_array.append(q14)
    q15 = input("15) I am exacting in my work: ")
    couns_array.append(q15)
    # print(couns_array)
    for i in range(len(couns_array)):
        if couns_array[i] == "a":
            conscientiousness += 1
    


    q16 = input("16) I have a soft heart: ")
    agree_array.append(q16)
    q17 = input("17) I feel little concern for others: ")
    agree_array.append(q17)
    q18 = input("18) I am not interested in other people's problems: ")
    agree_array.append(q18)
    q19 = input("19) I sympathize with others' feelings: ")
    agree_array.append(q19)
    q20 = input("20)cI make people feel at ease: ")
    agree_array.append(q20)
    # print(agree_array)
    for i in range(len(agree_array)):
        if agree_array[i] == "a":
            agreeableness += 1
    



    q21 = input("21) I don't talk a lot : ")
    extr_array.append(q21)
    q22 = input("22) I feel comfortable around people: ")
    extr_array.append(q22)
    q23 = input("23) I don't like to draw attention to myself : ")
    extr_array.append(q23)
    q24 = input("24) I start conversations : ")
    extr_array.append(q24)
    q25 = input("25) I talk to a lot of different people at parties : ")
    extr_array.append(q25)
    # print(extr_array)
    for i in range(len(extr_array)):
        if extr_array[i] == "a":
            extraversion += 1
    

    
    new_openness =  (openness*10)/5
    new_neuroticism = (neuroticism*10)/5
    new_conscientiousness = (conscientiousness*10)/5
    new_agreeableness = (agreeableness*10)/5
    new_extraversion = (extraversion*10)/5


    print("openness score:",int((openness*10)/5))
    print("neuerotism score:",int((neuroticism*10)/5))
    print("conscientiousness score:",int((conscientiousness*10)/5))
    print("agreeableness score:",int((agreeableness*10)/5))
    print("extraversion score:",int((extraversion*10)/5))
    

    break;

array = np.array([1,21,new_openness,new_neuroticism,new_conscientiousness,new_agreeableness,new_extraversion])
predict_this = array.reshape(-1, 7)
print('this is the prediction',classifier.predict(predict_this))