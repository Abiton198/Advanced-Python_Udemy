import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


# -----------------------------
# Read the dataset from CSV
# -----------------------------
def readFile():
    """
    Reads the dataset from the CSV file.

    X = all input columns except the last one
    Y = the last column (target/output)
    """
    dataset = pd.read_csv("house_prices_practice.csv")
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, -1].values
    dataset.head()
    return X, Y


# -----------------------------
# Split dataset into train/test sets
# -----------------------------
def splitData(X, Y):
    """
    Splits the data into:
    - X_train, Y_train for training
    - X_test, Y_test for testing
    """
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.4, random_state=0
    )
    return X_train, X_test, Y_train, Y_test


# -----------------------------
# Train the model and predict
# -----------------------------
def modelTraining(X_train, Y_train, X_test, Y_test):
    """
    Trains a multiple linear regression model,
    predicts on the test set,
    and returns evaluation results.
    """

    # Create the regression model
    model = LinearRegression()

    # Train the model using only training data
    # fit() needs:
    #   X_train = input features
    #   Y_train = target values
    model.fit(X_train, Y_train)

    # Predict the target values for the test set
    y_pred = model.predict(X_test)

    # Calculate model performance
    mse = mean_squared_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)

    # Return everything needed later
    return model, y_pred, mse, r2

# -----------------------------
# Show results
# -----------------------------
def showResults(Y_test, y_pred, mse, r2):
    """
    Prints real values, predicted values,
    and model evaluation scores.
    """
    print("Actual values:", Y_test)
    print("Predicted values:", y_pred)
    print("Mean Squared Error:", mse)
    print("R² Score:", r2)


# -----------------------------
# Visualize results
# -----------------------------
def visualize(Y_test, y_pred):
    """
    For multiple regression, a normal regression line plot
    is not suitable because there are multiple features.

    Instead, we compare:
    - Actual values
    - Predicted values
    """
    plt.scatter(Y_test, y_pred)
    plt.title("Actual vs Predicted Values")
    plt.xlabel("Actual House Prices")
    plt.ylabel("Predicted House Prices")
    plt.show()


# -----------------------------
# Main function
# -----------------------------
def main():
    X, Y = readFile()
    X_train, X_test, Y_train, Y_test = splitData(X, Y)
    model, y_pred, mse, r2 = modelTraining(X_train, Y_train, X_test, Y_test)
    showResults(Y_test, y_pred, mse, r2)
    visualize(Y_test, y_pred)


# Run program
if __name__ == "__main__":
    main()