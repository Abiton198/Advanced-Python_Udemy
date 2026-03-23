import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from tkinter import *


# -----------------------------
# Read the CSV file
# -----------------------------
def readFile():
    """
    Reads the dataset from a CSV file.
    X = all columns except the last one
    y = the last column (target/output)
    """
    dataset = pd.read_csv("test.csv")   # make sure test.csv is in the same folder
    X = dataset.iloc[:, :-1].values     # input features
    y = dataset.iloc[:, -1].values      # target/output
    return X, y


# -----------------------------
# Split the data into training and testing sets
# -----------------------------
def split_data(X, y):
    """
    Splits data into:
    - training data (60%)
    - testing data (40%)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=0
    )
    return X_train, X_test, y_train, y_test


# -----------------------------
# Train the linear regression model
# -----------------------------
def model_train(X_train, y_train, X_test, y_test):
    """
    Trains the linear regression model,
    makes predictions,
    calculates R² score,
    and predicts the value for a new area.
    """

    # Create the model
    lin_regressor = LinearRegression()

    # Train the model using training data
    lin_regressor.fit(X_train, y_train)

    # Predict values for the test data
    y_pred = lin_regressor.predict(X_test)

    # R² score compares actual test values and predicted test values
    r_square = r2_score(y_test, y_pred)

    # Predict a new value for Area = 37
    # The model expects a 2D array, so we use [[37]]
    area = np.array([[37]])
    pred_price = lin_regressor.predict(area)

    return lin_regressor, y_pred, r_square, pred_price


# -----------------------------
# Visualize the results
# -----------------------------
def visualize(X_train, y_train, lin_regressor):
    """
    Shows a scatter plot of training data
    and the regression line.
    """

    plt.scatter(X_train, y_train)
    plt.plot(X_train, lin_regressor.predict(X_train))
    plt.title("Linear Regression")
    plt.xlabel("Input (X)")
    plt.ylabel("Output (y)")
    plt.show()

# -----------------------------
# Show results in a Tkinter window
# -----------------------------
def show_gui(r_square, pred_price, lin_regressor):
    """
    Creates a Tkinter window that:
    1. Shows model accuracy (R² score)
    2. Shows the default prediction for area 37
    3. Lets the user type a new area value
    4. Uses the trained model to predict a new price
    """

    # Function that runs when user clicks the Predict button
    def model_pred():
        """
        Gets the user's input from the entry box,
        converts it to a number,
        predicts using the trained model,
        and displays the result.
        """
        try:
            # Get typed value from entry widget
            area_value = entry.get()

            # Convert typed text into integer
            area_num = int(area_value)

            # Model expects a 2D array: [[value]]
            trans_area = np.array([[area_num]])

            # Make prediction
            new_pred_price = lin_regressor.predict(trans_area)

            # Update result label with new prediction
            result_label.config(
                text=f"Predicted value for area {area_num}: {new_pred_price[0]:.2f}"
            )

        except ValueError:
            # Show error if user enters non-number
            result_label.config(text="Please enter a valid number.")

    # Create the main window
    window = Tk()
    window.title("Linear Regression")
    window.geometry("600x400")

    # Heading
    heading = Label(window, text="Linear Regression Results", font=("Arial", 16, "bold"))
    heading.pack(pady=20)

    # Show model score
    r2_label = Label(window, text=f"R² Score: {r_square:.4f}", font=("Arial", 12))
    r2_label.pack(pady=10)

    # # Show default prediction from your earlier code
    # default_pred_label = Label(
    #     window,
    #     text=f"Predicted value for area 37: {pred_price[0]:.2f}",
    #     font=("Arial", 12)
    # )
    # default_pred_label.pack(pady=10)

    # Instruction label
    label = Label(
        window,
        text="Enter the area of the land in thousand sq foot:",
        fg="red",
        font=("Arial", 12)
    )
    label.pack(pady=10)

    # Input box for user
    entry = Entry(window, fg="black", bg="white", font=("Arial", 12))
    entry.pack(pady=10)
    entry.delete(0, END)


    # Predict button
    pre_button = Button(
        window,
        text="Predict",
        command=model_pred,
        fg="red",
        bg="white",
        font=("Arial", 12)
    )
    pre_button.pack(pady=10)

    # Label where new prediction result will appear
    result_label = Label(window, text="", font=("Arial", 12, "bold"))
    result_label.pack(pady=20)


    # Start GUI loop
    window.mainloop()

# -----------------------------
# Main function
# -----------------------------
def main():
    X, y = readFile()
    X_train, X_test, y_train, y_test = split_data(X, y)
    lin_regressor, y_pred, r_square, pred_price = model_train(X_train, y_train, X_test, y_test)
    visualize(X_train, y_train, lin_regressor)
    show_gui(r_square, pred_price, lin_regressor)


# Run the program
if __name__ == "__main__":
    main()