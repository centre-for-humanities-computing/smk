import pandas as pd

features = pd.read_csv("../data/feature_mat.csv")
classes = pd.read_csv("../data/pix_class.csv")

# Off by one error...
merged_features = pd.merge(features, classes, left_on="Unnamed: 0", right_on="fname")

del merged_features["Unnamed: 0_x"]
del merged_features["Unnamed: 0_y"]

# Remove class tags
mat = merged_features.iloc[:,0:36]

# Create MinMaxScaler object to normalise matrix
scaler = MinMaxScaler(feature_range=(-1,1))
scaled = scaler.fit(mat)

# Train and test
X_train, X_test, y_train, y_test = train_test_split(scaled, merged_features['pix_class'], test_size=0.2, random_state=69)


# Multinomial NB
NBmodel = MultinomialNB().fit(X_train, y_train)
# Predict using Multinomial NB
NBy_predict = NBmodel.predict(X_test)
print(classification_report(y_test,NBy_predict))
print("Confusion matrix \n\n", confusion_matrix(y_test, NBy_predict))

# Gaussian NB
GNBmodel = GaussianNB().fit(X_train, y_train)
# Predict using Gaussian NB
GNBy_predict = GNBmodel.predict(X_test)
print(classification_report(y_test, GNBy_predict))
print("Confusion matrix \n\n", confusion_matrix(y_test, GNBy_predict))

# Logistic Regression model
LRmodel = LogisticRegression(verbose=True).fit(X_train, y_train)
# Predict using Logistic Regression model
LRy_predict = LRmodel.predict(X_test)
print(classification_report(y_test,LRy_predict))
print("Confusion matrix \n\n", confusion_matrix(y_test, LRy_predict))

# Linear SVm
svclassifier = LinearSVC(verbose=True).fit(X_train, y_train)
# Predict using SVM model
SVy_pred = svclassifier.predict(X_test)
print(classification_report(y_test,SVy_pred))
print("Confusion matrix \n\n", confusion_matrix(y_test,SVy_pred))
