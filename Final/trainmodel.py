from sklearn import datasets, linear_model 
import numpy as np
import pandas as pd

    
def train(self):
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

    temp=df[7]
    train_y =temp.values
    
    self.mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
    self.mul_lr.fit(mainarray, train_y)
    
def test(self, test_data):
    try:
        test_predict=list()
        for i in test_data:
            test_predict.append(int(i))
        y_pred = self.mul_lr.predict([test_predict])
        return y_pred
    except:
        print("All Factors For Finding Personality Not Entered!")


def check_type(data):
if type(data)==str or type(data)==str:
    return str(data).title()
if type(data)==list or type(data)==tuple:
    str_list=""
    for i,item in enumerate(data):
        str_list+=item+", "
    return str_list
else:   return str(data)

def prediction_result(top, aplcnt_name, cv_path, personality_values):
"after applying a job"
top.withdraw()
applicant_data={"Candidate Name":aplcnt_name.get(),  "CV Location":cv_path}

age = personality_values[1]

print("\n############# Candidate Entered Data #############\n")
print(applicant_data, personality_values)

personality = model.test(personality_values)
print("\n############# Predicted Personality #############\n")
print(personality)
data = ResumeParser(cv_path).get_extracted_data()

try:
    del data['name']
    if len(data['mobile_number'])<10:
        del data['mobile_number']
except:
    pass

print("\n############# Resume Parsed Data #############\n")

for key in data.keys():
    if data[key] is not None:
        print('{} : {}'.format(key,data[key]))

if __name__ == "__main__":
model = train_model()
model.train()