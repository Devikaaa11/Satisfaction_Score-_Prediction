import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score, precision_score, recall_score
import pickle

data= pd.read_csv(r'D:\Internship_ICT\Electronic - Electronic.csv.csv')
df= data[['Items Purchased','Warranty Extension','Loyalty Score','Satisfaction Score']]
df[['Satisfaction Score','Loyalty Score']]= df[['Satisfaction Score','Loyalty Score']].round().astype(int)

#splitting the dataset into training and test sets
X= df.drop('Satisfaction Score', axis=1)
y= df['Satisfaction Score']

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2, random_state=42,stratify=y)

model = SVC(kernel='linear', C=0.1, decision_function_shape='ovr', random_state=42) #tuned parameters
model.fit(X_train, y_train)
y_pred_svm = model.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svm))
print("\nClassification Report:\n", classification_report(y_test, y_pred_svm))
print("\nF1 Score:", f1_score(y_test, y_pred_svm,average = 'weighted'))
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print("Precision:", precision_score(y_test, y_pred_svm,average = 'weighted' ))
print("Recall:", recall_score(y_test, y_pred_svm,average = 'weighted'))

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
import sys
print(sys.version)