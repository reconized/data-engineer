<p style="text-align:center">
    <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork899-2023-01-01">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>


# Peer Review Assignment - Data Engineer - Extract API Data


Estimated time needed: **20** minutes


## Objectives

In this part you will:

-   Collect exchange rate data using an API
-   Store the data as a CSV


For this lab, we are going to be using Python and several Python libraries. Some of these libraries might be installed in your lab environment or in SN Labs. Others may need to be installed by you. The cells below will install these libraries when executed.



```python
!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y
```

    
                      __    __    __    __
                     /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                  /  / \   / \   / \   / \  \____
                 /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝
    
            mamba (1.4.2) supported by @QuantStack
    
            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack
    
    █████████████████████████████████████████████████████████████
    
    
    Looking for: ['pandas==1.3.3']
    
    [?25l[2K[0G[+] 0.0s
    pkgs/main/linux-64 [90m━━━╸[0m[33m━━━━━━━━━━━━━━━╸[0m[90m━━━━━[0m   0.0 B /  ??.?MB @  ??.?MB/s  0.0s[2K[1A[2K[0G[+] 0.1s
    pkgs/main/linux-64 [90m━━━╸[0m[33m━━━━━━━━━━━━━━━╸[0m[90m━━━━━[0m   0.0 B /  ??.?MB @  ??.?MB/s  0.1s
    pkgs/main/noarch   [90m━━━╸[0m[33m━━━━━━━━━━━━━━━╸[0m[90m━━━━━[0m   0.0 B /  ??.?MB @  ??.?MB/s  0.1s
    pkgs/r/linux-64    [33m━━━━━━━━━━━╸[0m[90m━━━━━━━━━━━━━[0m   0.0 B /  ??.?MB @  ??.?MB/s  0.1s
    pkgs/r/noarch      [33m━━━━━━━━━━━━━╸[0m[90m━━━━━━━━━━━[0m   0.0 B /  ??.?MB @  ??.?MB/s  0.1s[2K[1A[2K[1A[2K[1A[2K[1A[2K[0Gpkgs/main/noarch                                              No change
    pkgs/main/linux-64                                            No change
    pkgs/r/linux-64                                               No change
    pkgs/r/noarch                                                 No change
    [?25h
    Pinned packages:
      - python 3.7.*
    
    
    Transaction
    
      Prefix: /home/jupyterlab/conda/envs/python
    
      Updating specs:
    
       - pandas==1.3.3
       - ca-certificates
       - certifi
       - openssl
    
    
      Package   Version  Build           Channel                Size
    ──────────────────────────────────────────────────────────────────
      Downgrade:
    ──────────────────────────────────────────────────────────────────
    
      [31m- pandas[0m    1.3.5  py37h8c16a72_0  pkgs/main                  
      [32m+ pandas[0m    1.3.3  py37h8c16a72_0  pkgs/main/linux-64     10MB
    
      Summary:
    
      Downgrade: 1 packages
    
      Total download: 10MB
    
    ──────────────────────────────────────────────────────────────────
    
    
    [?25l[2K[0G[+] 0.0s
    Downloading      [90m━━━━━━━━━━━━━━━━━━━━━━━[0m   0.0 B                            0.0s
    Extracting       [90m━━━━━━━━━━━━━━━━━━━━━━━[0m       0                            0.0s[2K[1A[2K[1A[2K[0G[+] 0.1s
    Downloading  (1) [33m━━━━━━━━━━━━━━━━━━━━━━━[0m   0.0 B pandas                     0.0s
    Extracting       [90m━━━━━━━━━━━━━━━━━━━━━━━[0m       0                            0.0s[2K[1A[2K[1A[2K[0Gpandas                                               9.7MB @  56.8MB/s  0.2s
    [+] 0.2s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [90m━━━━━━━━━━━━╸[0m[33m━━━━━━━━━━[0m       0 pandas                     0.0s[2K[1A[2K[1A[2K[0G[+] 0.3s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━╸[0m[90m━━━━━━━━━━━━━━━[0m       0 pandas                     0.1s[2K[1A[2K[1A[2K[0G[+] 0.4s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━╸[0m[90m━━━━━━━━━━━━━━[0m       0 pandas                     0.2s[2K[1A[2K[1A[2K[0G[+] 0.5s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━━╸[0m[90m━━━━━━━━━━━━━[0m       0 pandas                     0.3s[2K[1A[2K[1A[2K[0G[+] 0.6s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━━━━╸[0m[90m━━━━━━━━━━━[0m       0 pandas                     0.4s[2K[1A[2K[1A[2K[0G[+] 0.7s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━━━━━╸[0m[90m━━━━━━━━━━[0m       0 pandas                     0.5s[2K[1A[2K[1A[2K[0G[+] 0.8s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━━━━━━╸[0m[90m━━━━━━━━━[0m       0 pandas                     0.6s[2K[1A[2K[1A[2K[0G[+] 0.9s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━━━━━━━╸[0m[90m━━━━━━━━[0m       0 pandas                     0.7s[2K[1A[2K[1A[2K[0G[+] 1.0s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [33m━━━━━━━━━━━━━━━╸[0m[90m━━━━━━━[0m       0 pandas                     0.8s[2K[1A[2K[1A[2K[0G[+] 1.1s
    Downloading      ━━━━━━━━━━━━━━━━━━━━━━━   9.7MB                            0.1s
    Extracting   (1) [90m╸[0m[33m━━━━━━━━━━━━━━━╸[0m[90m━━━━━━[0m       0 pandas                     0.9s[2K[1A[2K[1A[2K[0G[?25h
    Downloading and Extracting Packages
    
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done


## Imports

Import any additional libraries you may need here.



```python
import requests
import pandas as pd
from datetime import datetime
```

## Extract Data Using an API


Using ExchangeRate-API we will extract currency exchange rate data. Use the below steps to get the access key and to get the data. 
1. Open the url : https://exchangeratesapi.io/ and click on **Get Free API Key**. 
2. Subscribe for Free plan and Sign-in with the Google Account. 
3. Once the account is created you will be redirected to https://apilayer.com website.
2. Now, click on the **user icon** and click **Account** as shown below:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/Images/account.png">

3. Scroll down and you will get the API Key section. Copy the API key and use in the url in Question 1.


### Call the API

 <b> Question 1</b> Using the `requests` library call the endpoint given above and save the text, remember the first few characters of the output: 



```python
# Write your code here
url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=3f819bafa0fda540aa1899311192b5af"  #Make sure to change ******* to your API key.
data = requests.get(url)
data
#  print(data)
```




    <Response [200]>



### Save as DataFrame

 <b> Question 2</b>  Using the data gathered turn it into a `pandas` dataframe. The dataframe should have the Currency as the index and `Rate` as their columns. Make sure to drop unnecessary columns.



```python
# Turn the data into a dataframe
data1 = data.json()
df = pd.DataFrame(data1)
df[["rates"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AED</th>
      <td>3.888871</td>
    </tr>
    <tr>
      <th>AFN</th>
      <td>83.642242</td>
    </tr>
    <tr>
      <th>ALL</th>
      <td>105.288214</td>
    </tr>
    <tr>
      <th>AMD</th>
      <td>410.265969</td>
    </tr>
    <tr>
      <th>ANG</th>
      <td>1.907286</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>YER</th>
      <td>265.035808</td>
    </tr>
    <tr>
      <th>ZAR</th>
      <td>19.900635</td>
    </tr>
    <tr>
      <th>ZMK</th>
      <td>9530.169734</td>
    </tr>
    <tr>
      <th>ZMW</th>
      <td>22.276371</td>
    </tr>
    <tr>
      <th>ZWL</th>
      <td>340.922495</td>
    </tr>
  </tbody>
</table>
<p>170 rows × 1 columns</p>
</div>




```python
# Drop unnescessary columns
df[["rates"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AED</th>
      <td>3.888871</td>
    </tr>
    <tr>
      <th>AFN</th>
      <td>83.642242</td>
    </tr>
    <tr>
      <th>ALL</th>
      <td>105.288214</td>
    </tr>
    <tr>
      <th>AMD</th>
      <td>410.265969</td>
    </tr>
    <tr>
      <th>ANG</th>
      <td>1.907286</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>YER</th>
      <td>265.035808</td>
    </tr>
    <tr>
      <th>ZAR</th>
      <td>19.900635</td>
    </tr>
    <tr>
      <th>ZMK</th>
      <td>9530.169734</td>
    </tr>
    <tr>
      <th>ZMW</th>
      <td>22.276371</td>
    </tr>
    <tr>
      <th>ZWL</th>
      <td>340.922495</td>
    </tr>
  </tbody>
</table>
<p>170 rows × 1 columns</p>
</div>



### Load the Data

Using the dataframe save it as a CSV names `exchange_rates_1.csv`.



```python
# Save the Dataframe
csv_out = df[["rates"]]
csv_out.to_csv('exchange_rates_1.csv')
```

Your CSV should be in this format with more currencies

| | Rates |
| ------- | ------- |
|  AED| 4.398618    |
|  AFN| 92.917693   |  
|  ALL| 123.099093  |
|  AMD| 621.935674  |
|  ANG| 2.149648    | 



```python
logfile    = "logfile.txt"     
targetfile = "transformed_data.csv"
```


```python
def extract():
    df = pd.read_csv('exchange_rates.csv')
    df = df.drop(columns={"Unnamed: 0"})
    return df.head()

# data = extract()
# data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Market Cap (US$ Billion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JPMorgan Chase</td>
      <td>432.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bank of America</td>
      <td>231.52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Industrial and Commercial Bank of China</td>
      <td>194.56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Agricultural Bank of China</td>
      <td>160.68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HDFC Bank</td>
      <td>157.91</td>
    </tr>
  </tbody>
</table>
</div>




```python
def transform(data):
    # data['rates'] = round(data.rates, 2)
    return data


# transformed_data = transform(data)
# transformed_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Market Cap (US$ Billion)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JPMorgan Chase</td>
      <td>432.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bank of America</td>
      <td>231.52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Industrial and Commercial Bank of China</td>
      <td>194.56</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Agricultural Bank of China</td>
      <td>160.68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HDFC Bank</td>
      <td>157.91</td>
    </tr>
  </tbody>
</table>
</div>




```python
def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile) 
```


```python
def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + '\n')
```


```python
log("ETL job started...")

log("Extraction has started")

#  Call extract function
data = extract()

log("Extract step has completed")

log("Transform step has started")

#  Call transform function
transformed_data = transform(data)

log("Transform step has completed")


log("Load step has started")

#  Call load function
load(targetfile, transformed_data)


log("Load step has completed")

log("ETL process has completed")

```

## Authors


Ramesh Sannareddy, Joseph Santarcangelo and Azim Hirjani


### Other Contributors


Rav Ahuja


## Change Log


| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2022-05-06        | 0.3     | Malika            | Updated instructions to get the API and the url|
| 2021-04-15        | 0.2     | Malika            | Updated the lab from USD to EUR    |
| 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |


 Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork899-2023-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).

