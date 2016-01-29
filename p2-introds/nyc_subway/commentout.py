
# From visualization section, I create new variable called 'Day', which will divide the day into business or weekend. To test whether this new categorical variable is really different, we also included significant test.

# sp.ttest_ind(df.ix[df.BusinessDay == 0,'ENTRIESn_hourly'],
#              df.ix[df.BusinessDay ==1,'ENTRIESn_hourly'])

# This is indeed very different, p-value in this case is practically zero. So we also use this categorical variables.

# Finally for our final model, we include EXITSn_hourly in numerical variables, include rainy,fog,business day as our categorical variables.

sp.ttest_ind(df.ix[df.fog==0,'ENTRIESn_hourly'],
             df.ix[df.fog==1,'ENTRIESn_hourly'])
#
#With such small p-value that we have. We're convinced that difference of subway whether fog or not is significant, hence we reject the null hypothesis,which stated that there's no different between fog or not. We're favor the alternative, and make this as one of our predictor.

plt.scatter(df['ENTRIESn_hourly'],result.predict(df[predictors]));

#It seems our predictions captured most of the data. Using R-squared

residuals = np.square(df.ENTRIESn_hourly - predictions).sum()
variance = np.square(df.ENTRIESn_hourly - df.ENTRIESn_hourly.mean()).sum()
r_squared = 1 - (residuals/variance)
r_squared


#Here we see most of the numerical variables doesn't have linearity relationship with the variable that we want to predict. With the exception is EXITSn_hourly, which somehow more intuitive. People that's entering subway should be more or less the same.. Other interesting thing to look is that there's a relationship between `meandewpti` and `meantempi`, but it's non-linear relationsip. And we only observe `ENTRIESn_hourly` as the predicted variable. 
#For linear regression, we have to diagnose each of numerical variables and see whether there is a linear relationship.If the variables are categorical, we want to test it using statistical test like rainy categorical in statistical test section. We're going to that with other categorical variables, plus one new variable that was created in Visualization section.
fig,axes = plt.subplots(nrows=4,ncols=4 ,squeeze=False)
rows = 0
cols = 0
for e in candidates:
     
    response = 'ENTRIESn_hourly'
    axes[rows][cols].scatter(df[e], df[response])
#     axes[rows][cols].figure(figsize=(3,3));
    axes[rows][cols].set_xlabel(e)
    axes[rows][cols].set_ylabel(response);
    if cols == 3:
        rows+=1
    cols = (cols + 1) % 4
fig.set_size_inches(15,13)

pd.scatter_matrix(df[['ENTRIESn_hourly']+rows],
                 figsize=(15,15));

def compute_adj_r_squared(data, predictions):
 
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-data)**2).sum()
    #adj_r_squared = 1 - (SSReg/SST * ((data.shape[1] - 1)/(data.shape[0]-data.shape[1] - 1)))
    r_squared = 1 - (SSReg/SST)
    return r_squared

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(df[['ENTRIESn_hourly']],df['EXITSn_hourly'])

compute_adj_r_squared(df[['ENTRIESn_hourly']]
                      ,reg.predict(df[['ENTRIESn_hourly']]))