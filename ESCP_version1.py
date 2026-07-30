from statistics import mean,median,variance,stdev,correlation,linear_regression

#THE FIRST LIST
#Set up the list in size.
print("------------------Easy Statistical Calculation-------------------")
print("-----------------------------------------------------------------")

first_list = list()
first_list_len = len(first_list)
selected_firstlist_len = int(input("Enter the size of the first list: "))
first_list_len = selected_firstlist_len 

#Enter data into the list.
data_first_list = int(input("Enter the number of the fist list: "))
while len(first_list) != first_list_len:
    first_list.append(data_first_list)
    if len(first_list) == first_list_len:
        break
    data_first_list = int(input("Enter the number of the fist list: "))
print("-----------------------------------------------------------------")

#THE SECOND LIST
#Set up the list in size.
second_list = list()
second_list_len = len(second_list)
selected_secondlist_len = int(input("Enter the size of the second list: "))
second_list_len = selected_secondlist_len 

#Enter data into the list.
data_second_list = int(input("Enter the number of the second list: "))
while len(second_list) != second_list_len:
    second_list.append(data_second_list)
    if len(second_list) == second_list_len:
        break
    data_second_list = int(input("Enter the number of the second list: "))
print("-----------------------------------------------------------------")

x_data_number_list = first_list
y_data_number_list = second_list

#Statistical Calculation of X List
print("X List")
print("The data of X are",x_data_number_list)
#MEAN
print("Mean of X is",round(mean(x_data_number_list),4))
#MEDIAN
print("Median of X is",round(median(x_data_number_list),4))
#VARIANCE
print("Variance of X is",round(variance(x_data_number_list),4))
#STD
print("Standard Deviation of X is",round(stdev(x_data_number_list),4))
print("-----------------------------------------------------------------")

#Statistical Calculation of Y List
print("Y List")
print("The data of Y are",y_data_number_list)
#MEAN
print("Mean of Y is",round(mean(y_data_number_list),4))
#MEDIAN
print("Median of Y is",round(median(y_data_number_list),4))
#VARIANCE
print("Variance of Y is",round(variance(y_data_number_list),4))
#STD
print("Standard Deviation of Y is",round(stdev(y_data_number_list),4))
print("-----------------------------------------------------------------")

#Correlation Equation and Prediction
correlation_data = correlation(x_data_number_list,y_data_number_list)
slope_data,intercept_data = linear_regression(x_data_number_list,y_data_number_list)

#Correlation and Equation
print("Correlation and Equation")
print("Correlation of X and Y is",round(correlation_data,4))
print("Slope of X and Y is",round(slope_data,4))
print("Intercept of X and Y is",round(intercept_data,4))
print("-----------------------------------------------------------------")

#Prediction
print("Prediction of X and Y")
x_value = float(input("Enter the X value : "))
y_value = (slope_data*x_value)+intercept_data
print(f"y = ({slope_data:.4f}x{x_value:.4f})+{intercept_data:.4f} = {y_value:.4f}")
print("-----------------------------------------------------------------")
