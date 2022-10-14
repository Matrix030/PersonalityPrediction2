from Question import Question
question_prompt = [
    "You find it difficult to introduce yourself to other people? \n a)DisAgree \n b)Agree \n",
    "Your mood can change very quickly? \n a)Disagree \n b)Agree \n",
    "You rarely worry about how your actions affect other people? \n a)Disagree \n b)Agree \n",
    "Logic is usually more important than heart when it comes to making important decisions? \n a)Disagree \n b)Agree \n"
]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"b"),
    Question(question_prompt[3],"a"),
]

def predict(questions):
    result = []
    
    personalities = [
                [['ISFJ'],['a','a','a','a'],['Very dedicated and warm protectors, always ready to defend their loved ones']],
                [['ISFP'],['a','a','a','b'],['Flexible and charming artists, always ready to explore and experience something new']],
                [['ISTJ'],['a','a','b','a'],['Practical and fact-minded individuals, whose reliability cannot be doubted']],
                [['ISTP'],['a','a','b','b'],['Practical and fact-minded individuals, whose reliability cannot be doubted']],
                [['INFJ'],['a','b','a','a'],['Bold and practical experimenters, masters of all kinds of tools']],
                [['INFP'],['a','b','a','b'],['Quiet and mystical, yet very inspiring and tireless idealists']],
                [['INTJ'],['a','b','b','a'],['Poetic, kind and altruistic people, always eager to help a good cause']],
                [['INTP'],['a','b','b','b'],['Innovative inventors with an unquenchable thirst for knowledge']],
                [['ESFJ'],['b','a','a','a'],['Very dedicated and warm protectors always ready to defend their loved ones']],
                [['ESFP'],['b','a','a','b'],['Spontaneous, energetic and enthusiastic people ñ life is never boring around them']],
                [['ESTJ'],['b','a','b','a'],['Excellent administrators, unsurpassed at managing things ñ or people']],
                [['ESTP'],['b','a','b','b'],['Smart, energetic and very perceptive people, who truly enjoy living on the edge']],
                [['ENFJ'],['b','b','a','a'],['Charismatic and inspiring leaders, able to mesmerize their listeners']],
                [['ENFP'],['b','b','a','b'],['Enthusiastic, creative and sociable free spirits, who can always find a reason to smile']],
                [['ENTJ'],['b','b','b','a'],['Bold,imaginative and strong-willed leaders,always finding a way -or making one']],
                [['ENTP'],['b','b','b','b'],['Smart and curious thinkers who cannot resist an intellectual challenge']]
]
    for question in questions:
        answer = input(question.prompt)
        result.append(answer)
    print(result)
    i = 0
    for i in range(len(personalities)):
        if result == personalities[i][1]:
            print("Personality Group: " + personalities[i][0][0] +"." + "\n" + " Description: " + personalities[i][2][0])
        i +=1

predict(questions)




