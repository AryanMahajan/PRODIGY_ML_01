import pandas as pd

unwanted_columns = ["Id","MSSubClass","MSZoning","LotFrontage","Street","Alley","LotShape","LandContour","Utilities","LotConfig","LandSlope","Neighborhood","Condition1","Condition2","BldgType","HouseStyle","OverallQual","OverallCond","YearBuilt","YearRemodAdd","RoofStyle","RoofMatl","Exterior1st","Exterior2nd","MasVnrType","MasVnrArea","ExterQual","ExterCond","Foundation","BsmtQual","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinSF1","BsmtFinType2","BsmtFinSF2","BsmtUnfSF","TotalBsmtSF","Heating","HeatingQC","CentralAir","Electrical","1stFlrSF","2ndFlrSF","LowQualFinSF","GrLivArea","KitchenAbvGr","KitchenQual","TotRmsAbvGrd","Functional","Fireplaces","FireplaceQu","GarageType","GarageYrBlt","GarageFinish","GarageCars","GarageArea","GarageQual","GarageCond","PavedDrive","WoodDeckSF","OpenPorchSF","EnclosedPorch","3SsnPorch","ScreenPorch","PoolArea","PoolQC","Fence","MiscFeature","MiscVal","MoSold","YrSold","SaleType","SaleCondition"]

df_uncleaned_train = pd.read_csv(r"house-prices-advanced-regression-techniques\train.csv")

df_uncleaned_train = df_uncleaned_train.drop(unwanted_columns, axis = 1)

df_uncleaned_train["BsmtFullBath"] = df_uncleaned_train["BsmtFullBath"] + df_uncleaned_train["BsmtHalfBath"] + df_uncleaned_train["FullBath"] + df_uncleaned_train["HalfBath"]

df_uncleaned_train = df_uncleaned_train.drop(["BsmtHalfBath","FullBath","HalfBath"], axis = 1)

df_uncleaned_train = df_uncleaned_train.rename(columns={"LotArea":"Area", "BsmtFullBath":"Bathrooms","BedroomAbvGr":"Bedrooms","SalePrice":"Sales Price"})

df_uncleaned_train.to_csv(r"Data\train.csv")

df_uncleaned_test = pd.read_csv(r"house-prices-advanced-regression-techniques\test.csv")

df_uncleaned_test = df_uncleaned_test.drop(unwanted_columns, axis = 1)

df_uncleaned_test["BsmtFullBath"] = df_uncleaned_test["BsmtFullBath"] + df_uncleaned_test["BsmtHalfBath"] + df_uncleaned_test["FullBath"] + df_uncleaned_test["HalfBath"]

df_uncleaned_test = df_uncleaned_test.drop(["BsmtHalfBath","FullBath","HalfBath"], axis = 1)

df_uncleaned_test = df_uncleaned_test.rename(columns={"LotArea":"Area", "BsmtFullBath":"Bathrooms","BedroomAbvGr":"Bedrooms","SalePrice":"Sales Price"})

df_uncleaned_test.to_csv(r"Data\test.csv")