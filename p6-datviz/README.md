This is the visualization:
http://bl.ocks.org/napjon/raw/3a36381045a0b872e312/


# Summary

The visualization measures the performance of 2015 US
Flight.
Performance based on how much on time number of flights, and how it
decrease vary based on number of flights delay,cancelled,diverted.
Second plot measures delay across months based on carrier.

# Design

When I visited
[RITA](http://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp) to get
the data, I notice that they use pie chart for visualization. This is
harder to measure based on the angle, and it doesn't span very well
across month. So I want to build visualization like theirs but clearer
and additional time series.I found one of Udacity material (link in References
section) about time-series part-to-whole relationship is
best explained with line plot, and each part can be compared across
time. It's better than stacked bar chart since stacked bar harder to measure for each part.

The visualization use line+scatter for the plot. The reason behind came
from Jonathan lecture's at Dimple Chapter of Udacity. Scatter plot is
used when we have two numerical variables, and variables in x-axis is
independent of one another. Since it's time series, the measurement
depend on the earlier month. Line plot is great when we want to see up
and down of something that we want to measure for time series. But line
plot also has its downside. We don't know how many number of data
points, and whether the data has missing values. This will obscure the
data. We don't do any interpolation since this month is categorical
variable. So no hovering between month. Because of these reasons, I
choose line+scatter plot. Readers would know when something missing in
the data, and they can see the points so they can hover over it to get
the tooltip.

After collecting the feedback, in the first plot  I notice that number of flights delay
doesn't really cared that much, and they just prefer to have total delay
altogether. So based on this, I will just use total number of flights
delay. However on-time flights doesn't just decrease because of the
delay, it's also caused by number of flights cancelled and diverted.

The original second visualization is how delay varied. One of Udacity
reviewers gave me feedback that the visualization will still be
exploratory, and better to show which airlines affect highest delay.

I also use preattentive attribute, correlates with Gestalt's Principles. With data, Southwest Airlines stands-out from the rest (Proximity). I also add red-color and leave the rest with gray line (Similarity). I still use different color for the dots since It will easier for readers to differentiate the
line, which represent airline.


# Feedback

## Person 1

* *What do you notice in the visualization?*
I notice, there is no significant turn on both graph. Consistency on both fligh operation & delayed flight are steady.
* *What questions do you have about the data?*
No question
* *What relationships do you notice?*
The more flight operation, should be, the more chance delayed flight
* *What do you think is the main takeaway from this visualization?*
US flight operation runs steady
* *Is there something you don’t understand in the graphic?*
I think graphic quite clear. I understand.

## Person 2

* *What do you notice in the visualization?*
I notice that the number of on-time flight is way more compare to the
delay flight
* *What questions do you have about the data?*
With Such a high number of delayed flighht, how come the total Minutes
is very small?
* *What relationships do you notice?*
The Relation between carrier Delay and Late Arrival is highly correlated
base on totalhe second graph
* *What do you think is the main takeaway from this visualization?*
The Graph is pretty straight forward and easy to digest
* *Is there something you don’t understand in the graphic?*
I can’t really understand is there a relationship between number of
flight with the amount of delays.

## Person 3

* y-axis is misleading, is it in minutes? Why so small?
* Better to use bar chart type
* We can just see delay line plot in detail at the plot below. No need
  in the first plot. 

# Resources

* http://www.perceptualedge.com/articles/visual_business_intelligence/displays_for_combining_time-series_and_part-to-whole.pdf

