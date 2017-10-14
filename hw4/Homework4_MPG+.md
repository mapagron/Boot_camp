
Homework#4
Heroes of Pymoli
http://gw.bootcampcontent.com/GW-Coding-Boot-Camp/09-12-2017-GW-Arlington-Class-Repository-DATA/tree/master/Homework/Week04/Instructions



```python
#Import libraries 
import pandas as pd
import numpy as np 
import os
import json 
#os.getcwd()

```


```python
#Import data 
# json.load
# json.loads (it use of only strings)
#data = pd.read_json("http://localhost:8840/edit/Homework/Week04/Instructions/HeroesOfPymoli/purchase_data.json")
#ata = json.load(open('http://localhost:8840/edit/Homework/Week04/Instructions/HeroesOfPymoli/purchase_data.json', 'r'))

json_path = "purchase_data.json"
p_data_df = pd.read_json(json_path)

# to see the data 
p_data_df.head()
#p_data_df.columns
#p_data_df.dtypes
#p_data_df.describe()
#p_data_df.counts()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
    </tr>
  </tbody>
</table>
</div>



# Total number of players and purchasing analysis


```python
#total number of players
#TotalPlayers = p_data_df["SN"].count()
TotalPlayers = p_data_df["SN"].unique()
TotalUniquePlayers = len(TotalPlayers)
```


```python
#Purchasing Analysis (Total)
#Number of Unique Items
UniqueItems = p_data_df["Item ID"].unique()
NumberUniqueItems = len(UniqueItems)

#Average Purchase Price
averagePurchase = p_data_df["Price"].mean()

#Total Number of Purchases
TotalNumberPurchases = len(p_data_df["Price"])

#Total Revenue
TotalRevenue = sum(p_data_df["Price"])
```


```python
#Everything to a table 
PurchasingAnalysis = pd.DataFrame({"Total Players": [TotalUniquePlayers],
                                   "Number of Unique Items": [NumberUniqueItems],
                                   "Average Purchase Price": [averagePurchase],
                                   "Total Number of Purchases": [TotalNumberPurchases],
                                   "Total Revenue": [TotalRevenue]})
PurchasingAnalysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchases</th>
      <th>Total Players</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.924359</td>
      <td>64</td>
      <td>78</td>
      <td>74</td>
      <td>228.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender analysis
```


```python
#demographics = p_data_df["Gender"].value_counts()
#demographics

totalGender = p_data_df["Gender"].count()
male = p_data_df["Gender"].value_counts()['Male']
female = p_data_df["Gender"].value_counts()['Female']
nonGenderSpecific = totalGender - male - female
malePercent = (male/totalGender) * 100
femalePercent = (female/totalGender) * 100
nonGenderSpecificPercent = (nonGenderSpecific/totalGender) * 100
```


```python
#Everything to a table 

GenderDemographics = pd.DataFrame({"Total Gender": [totalGender],
                                   "Total Male": [male],
                                   "% attended Male": [malePercent],
                                   "Total Female": [female],
                                   "% attended Female": [femalePercent],
                                   "% Non Gender Specific":[nonGenderSpecific],
                                   "% Non Gender Specific Percent":[nonGenderSpecificPercent],
                                   
                                 })
GenderDemographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Non Gender Specific</th>
      <th>% Non Gender Specific Percent</th>
      <th>% attended Female</th>
      <th>% attended Male</th>
      <th>Total Female</th>
      <th>Total Gender</th>
      <th>Total Male</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1.282051</td>
      <td>16.666667</td>
      <td>82.051282</td>
      <td>13</td>
      <td>78</td>
      <td>64</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics


```python
#The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
#source: https://chrisalbon.com/python/pandas_binning_data.html

ageBinValue = [0, 9, 14, 19, 24, 29, 34, 39, 44, 100]
ageBinNames = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45<']
p_data_df["Age Demographics"]= pd.cut(p_data_df["Age"], ageBinValue, labels=ageBinNames)
demographic_group = p_data_df.groupby("Age Demographics")

print(demographic_group["Item Name"].count())
print((demographic_group["Price"].mean()))
print((demographic_group["Price"].sum()))
```

    Age Demographics
    10-14     3
    15-19    11
    20-24    36
    25-29     9
    30-34     7
    35-39     6
    40-44     1
    45<       0
    <10       5
    Name: Item Name, dtype: int64
    Age Demographics
    10-14    2.986667
    15-19    2.764545
    20-24    3.024722
    25-29    2.901111
    30-34    1.984286
    35-39    3.561667
    40-44    4.650000
    45<           NaN
    <10      2.764000
    Name: Price, dtype: float64
    Age Demographics
    10-14      8.96
    15-19     30.41
    20-24    108.89
    25-29     26.11
    30-34     13.89
    35-39     21.37
    40-44      4.65
    45<         NaN
    <10       13.82
    Name: Price, dtype: float64
    

# Top Spenders


```python
spenders = p_data_df.groupby("SN")

#spenders.head()
topSpenders = pd.DataFrame(spenders["Price"].value_counts())
topSpenders.sort_values("Price", ascending = False, inplace = True)
#opSpenders

topSpenders.rename(columns = {"Price": "Total Items"},  inplace =True)
#topSpenders    
```

# Most Popular Items


```python
by_itemid = p_data_df.groupby('Item ID')
#counts occurance of item ID by grouping by item ID
pur_by_item = pd.DataFrame(by_itemid['Item ID'].count()) 

pur_by_item.rename(columns = {"Item ID": "Number of Items Sold"}, inplace = True)
#pur_by_item

#sums Price grouped by item ID
TotalPvalue = pd.DataFrame(by_itemid['Price'].sum()) 

#Renaming the column
TotalPvalue.rename(columns = {"Price": "Revenue"}, inplace =True)
#Removing duplicates
no_dup_items = p_data_df.drop_duplicates('Item ID')
#TotalPvalue
```


```python
fivePopular = no_dup_items.merge(pur_by_item, left_on = "Item ID", right_index = True)
fivePopular = fivePopular.merge(TotalPvalue, left_on = "Item ID", right_index = True)
fivePopular = fivePopular[['Item ID', "Item Name", "Price", "Number of Items Sold", "Revenue"]]
fivePopular.sort_values("Number of Items Sold", ascending = False, inplace = True)
fivePopular = fivePopular.iloc[0:5][:] 
fivePopular
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Number of Items Sold</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>94</td>
      <td>Mourning Blade</td>
      <td>3.64</td>
      <td>3</td>
      <td>10.92</td>
    </tr>
    <tr>
      <th>0</th>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>2</td>
      <td>8.98</td>
    </tr>
    <tr>
      <th>10</th>
      <td>126</td>
      <td>Exiled Mithril Longsword</td>
      <td>1.08</td>
      <td>2</td>
      <td>2.16</td>
    </tr>
    <tr>
      <th>42</th>
      <td>64</td>
      <td>Fusion Pummel</td>
      <td>2.42</td>
      <td>2</td>
      <td>4.84</td>
    </tr>
    <tr>
      <th>36</th>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>2.26</td>
      <td>2</td>
      <td>4.52</td>
    </tr>
  </tbody>
</table>
</div>




```python
fiveProfitable = no_dup_items.merge(pur_by_item, left_on = "Item ID", right_index = True)

fiveProfitable = top5_prof.merge(fivePopular, left_on = "Item ID", right_index = True)
#fiveProfitable = top5_prof[['Item ID', "Item Name", "Number of Items Sold", "Price", "Revenue"]]
#fiveProfitable
fiveProfitable.sort_values("Price", ascending = False, inplace = True)
fiveProfitable

```

# Final Report


```python

print ("The total number of players for Pymoli game is " + str(TotalUniquePlayers))
print ("The total number of unique items for Pymoli game is " + str(NumberUniqueItems))
print ("The average Purchase price for Pymoli game is (US$ ) " + str(averagePurchase))
print ("The total revenue is (US$ ) " + str(TotalRevenue))
print ("The majority of the buyers for Pymoli game are in the ages of 20-24 and spend an average of US$ 3")
print ("")
print ("To consider: The spenders between 40 - 44 spend on average US$4, to increase the revenue it could be an option to target this audience")

```

    The total number of players for Pymoli game is 74
    The total number of unique items for Pymoli game is 64
    The average Purchase price for Pymoli game is (US$ ) 2.9243589743589733
    The total revenue is (US$ ) 228.1
    The majority of the buyers for Pymoli game are in the ages of 20-24 and spend an average of US$ 3
    
    To consider: The spenders between 40 - 44 spend on average US$4, to increase the revenue it could be an option to target this audience
    
