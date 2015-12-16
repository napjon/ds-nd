
# Summary


```python

```


```python
import pandas as pd
```


```python
df = pd.read_csv('data/airline_delay_causes_2015.csv')
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>month</th>
      <th>carrier</th>
      <th>carrier_name</th>
      <th>airport</th>
      <th>airport_name</th>
      <th>arr_flights</th>
      <th>arr_del15</th>
      <th>carrier_ct</th>
      <th>weather_ct</th>
      <th>...</th>
      <th>late_aircraft_ct</th>
      <th>arr_cancelled</th>
      <th>arr_diverted</th>
      <th>arr_delay</th>
      <th>carrier_delay</th>
      <th>weather_delay</th>
      <th>nas_delay</th>
      <th>security_delay</th>
      <th>late_aircraft_delay</th>
      <th>Unnamed: 21</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>1</td>
      <td>AA</td>
      <td>American Airlines Inc.</td>
      <td>JFK</td>
      <td>New York, NY: John F. Kennedy International</td>
      <td>1369</td>
      <td>322</td>
      <td>73.31</td>
      <td>8.44</td>
      <td>...</td>
      <td>103.47</td>
      <td>86</td>
      <td>3</td>
      <td>20055</td>
      <td>5273</td>
      <td>999</td>
      <td>6358</td>
      <td>0</td>
      <td>7425</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>1</td>
      <td>AA</td>
      <td>American Airlines Inc.</td>
      <td>LAX</td>
      <td>Los Angeles, CA: Los Angeles International</td>
      <td>2633</td>
      <td>445</td>
      <td>157.17</td>
      <td>25.21</td>
      <td>...</td>
      <td>153.43</td>
      <td>41</td>
      <td>4</td>
      <td>25261</td>
      <td>10914</td>
      <td>1460</td>
      <td>3293</td>
      <td>42</td>
      <td>9552</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>1</td>
      <td>AA</td>
      <td>American Airlines Inc.</td>
      <td>DFW</td>
      <td>Dallas/Fort Worth, TX: Dallas/Fort Worth Inter...</td>
      <td>12466</td>
      <td>2463</td>
      <td>645.29</td>
      <td>64.66</td>
      <td>...</td>
      <td>982.99</td>
      <td>203</td>
      <td>6</td>
      <td>167313</td>
      <td>66714</td>
      <td>5055</td>
      <td>24137</td>
      <td>123</td>
      <td>71284</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>1</td>
      <td>AA</td>
      <td>American Airlines Inc.</td>
      <td>OGG</td>
      <td>Kahului, HI: Kahului Airport</td>
      <td>100</td>
      <td>22</td>
      <td>11.53</td>
      <td>0.00</td>
      <td>...</td>
      <td>4.00</td>
      <td>3</td>
      <td>0</td>
      <td>1776</td>
      <td>1207</td>
      <td>0</td>
      <td>188</td>
      <td>0</td>
      <td>381</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>1</td>
      <td>AA</td>
      <td>American Airlines Inc.</td>
      <td>HNL</td>
      <td>Honolulu, HI: Honolulu International</td>
      <td>169</td>
      <td>50</td>
      <td>28.69</td>
      <td>0.00</td>
      <td>...</td>
      <td>6.27</td>
      <td>0</td>
      <td>4</td>
      <td>4175</td>
      <td>2602</td>
      <td>0</td>
      <td>523</td>
      <td>0</td>
      <td>1050</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



Since month in dimple only except 2 digit format, change this


```python
df['month'] = df[' month'].map(lambda x: '0' +str(x)).tolist()
```

We want to have total number of operations and total minutes delay. So we're going to aggregate it per month.


```python
agg_month_sum = df.groupby('month',as_index=False).sum()
```


```python
agg_month_sum.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>year</th>
      <th>month</th>
      <th>arr_flights</th>
      <th>arr_del15</th>
      <th>carrier_ct</th>
      <th>weather_ct</th>
      <th>nas_ct</th>
      <th>security_ct</th>
      <th>late_aircraft_ct</th>
      <th>arr_cancelled</th>
      <th>arr_diverted</th>
      <th>arr_delay</th>
      <th>carrier_delay</th>
      <th>weather_delay</th>
      <th>nas_delay</th>
      <th>security_delay</th>
      <th>late_aircraft_delay</th>
      <th>Unnamed: 21</th>
      <th>on_time_flights</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01</td>
      <td>2367625</td>
      <td>1175</td>
      <td>469968</td>
      <td>95951</td>
      <td>28267.23</td>
      <td>3311.58</td>
      <td>29878.63</td>
      <td>148.22</td>
      <td>34345.34</td>
      <td>11982</td>
      <td>973</td>
      <td>5439862</td>
      <td>1708155</td>
      <td>263087</td>
      <td>1278055</td>
      <td>6700</td>
      <td>2183865</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02</td>
      <td>2335385</td>
      <td>2318</td>
      <td>429191</td>
      <td>95179</td>
      <td>27635.04</td>
      <td>4580.42</td>
      <td>29530.35</td>
      <td>111.35</td>
      <td>33322.07</td>
      <td>20517</td>
      <td>1011</td>
      <td>5635596</td>
      <td>1712660</td>
      <td>411265</td>
      <td>1349173</td>
      <td>4580</td>
      <td>2157918</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03</td>
      <td>2333370</td>
      <td>3474</td>
      <td>504312</td>
      <td>95452</td>
      <td>30094.13</td>
      <td>2348.12</td>
      <td>28283.47</td>
      <td>149.04</td>
      <td>34577.51</td>
      <td>11002</td>
      <td>1172</td>
      <td>5438910</td>
      <td>1818680</td>
      <td>228661</td>
      <td>1228893</td>
      <td>6586</td>
      <td>2156090</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04</td>
      <td>2325310</td>
      <td>4616</td>
      <td>485151</td>
      <td>82247</td>
      <td>24683.00</td>
      <td>2772.98</td>
      <td>26000.96</td>
      <td>96.66</td>
      <td>28693.24</td>
      <td>4520</td>
      <td>1380</td>
      <td>4619308</td>
      <td>1490594</td>
      <td>221590</td>
      <td>1118027</td>
      <td>3660</td>
      <td>1785437</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05</td>
      <td>2299115</td>
      <td>5705</td>
      <td>496993</td>
      <td>89645</td>
      <td>26388.30</td>
      <td>3639.07</td>
      <td>26555.12</td>
      <td>142.48</td>
      <td>32919.97</td>
      <td>5694</td>
      <td>1658</td>
      <td>5437359</td>
      <td>1667920</td>
      <td>336555</td>
      <td>1254652</td>
      <td>5711</td>
      <td>2172521</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
not_ontime_flights  = ['arr_cancelled','arr_diverted','arr_del15']
agg_month_sum['on_time_flights'] = agg_month_sum['arr_flights'] - agg_month_sum[not_ontime_flights].sum()
```


```python
agg_month_sum.to_csv('data/agg_month_sum_airlines_2015.csv')
```


```python
#Ignore this cell for now
# agg_month_sum.ix[5,'custom_month'] = 'Jun, (UA, "dispatching information")'
# agg_month_sum.ix[4,'custom_month'] = 'May, (UA, "automation issue")'
# agg_month_sum['custom_month'] = agg_month_sum['month'].map(lambda x: arrow.get('2015-'+x, "YYYY-MM").format('MMM'))
# agg_month_sum.ix[5,'custom_month'] = 'Jun, (UA, "dispatching information")'
# agg_month_sum.ix[4,'custom_month'] = 'May, (UA, "automation issue")'
```
