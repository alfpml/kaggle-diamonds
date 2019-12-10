# kaggle-diamonds

### 1. Cleaning Techniques

**File: Diamonds_cleaning.ipynb**

1. Checking Data Types: Cut, clarity and color are categorical
2. Checking for nulls/NAs: NO nulls/NAs
3. Bining of carat: generate new column (carat_bin) to understand the price correlation of cut clarity and color keeping carat constant.
4. Correlation: 'x','y','z' are highly correlated with Carat so I dropped x,y,z
5. One Hot Encoding: I converted to numerical the categorical variables by ranking all the possible outcomes based on research on the influence of each. To do so I defined the functions in **File: functions.ipynb**
6. Normalization of 'carat','depth', 'table'

## 2. Parameters

I defined 4 parameters to play with for each model: 
    quant: number of quantiles on the bining of carat
    n1=multiplier for the cut variable
    n2=multiplier for the color variable
    n3=multiplier for thr clarity variable


### 3. Modelling 

**File: Diamonds_modelling.ipynb**

I tried the following models with RandomForestRegressor performing the best with 24quantiles and n1=3, n2=1 and n3=2 (oversizing cut variable).
1. LinearRegression: 
    *r2_score: 0.90*
    *rmse:1263*
2. RandomForestRegressor(n=200): 
    *r2_score: 0.98247*
    *rmse:522*
3. GradientBoostingRegressor: 
    *r2_score: 0.9756*
    *rmse:626*

### 4. Pipelines

**Diamonds_cleaning.ipynb** takes 'train.cdv' dataset from the input folder and publishes 'clean_diamonds.csv' after cleaning steps. It does the same with 'test.csv' dataset to produce 'clean_test.csv'. Functions for one hot encoding are stored in **functions.ipynb**

**Diamonds_modelling.ipynb** takes 'clean_diamonds.csv' and runs regression models on it to produce accuracy metrics (r2_score, rmse). After comparing results chose the best performer model. submission files in the output folder. Then it takes 'clean_test' runs the model on it and produces submisssion files in the ouput folder. 

