import pandas as pd
import os

os.getcwd()
os.chdir("z:\\workingpath") #set this to your current working path

df = pd.read_csv("R11709237_SL140.csv")

list(df)	# see all column names

df.head()       # first five rows
df.tail()       # last five rows
df.sample(5)    # random sample of rows
df.shape        # number of rows/columns in a tuple
df.describe()   # calculates measures of central tendency
df.info()       # memory footprint and datatypes


# See what each of these commands does to fetch df data

df[0:5]

df.iloc[0][0] # note: the i stands for index, we select a column by index

df.loc[0]["Geo_FIPS"] # note: without the i we locate a column by name

df.iat[0,0]

df.at[0,"Geo_FIPS"]

# note: iloc and iat work on positions
# note: loc and at work on labels
# note: loc commands separate rows and columns
# note: at commands combine rows and columns


# sets a column as the index
df.set_index("Geo_TAZ")

# drops a column
# note: axis = 1 means to operate vertically on a column
# note: axis = 0 would operate on a row
df.drop("Geo_PUMA5", axis=1)

# rename a column with a dictionary
df.rename(columns={"SE_T002_001":"totalpop"}, inplace=True)

# rename multiple columns with a dictionary
df.rename(columns={"SE_T037_001":"laborforce",
                   "SE_T037_002":"employed",
                   "SE_T037_003":"unemployed"}, inplace=True)

# create and calculate a new column
# calculate a new series named pcunemp
pcunemp  = (df.unemployed / df.laborforce)
# add series to the dataframe with column name of unemprate
df["unemprate"] = pcunemp

# filter for rows match condition
# str.match method matches the beginning of a strong
df2 = df[df['Geo_GEOID'].str.match('14000US13089')]

