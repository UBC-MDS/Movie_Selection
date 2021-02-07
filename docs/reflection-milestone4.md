# Reflection

_Milestone 4_

_**Group 7**_

## Choice of programming language and plotting library
For this milestone, we chose to use Python over R for the easiness of deployment on heroku. We noted on the enhanced interactivity of Plotly when develop our app in R. Therefore, we chose to use Python & Plotly to deliver our dashboard for the benefit of flexibility in implementation and fluency in layout designing. 

## What we have implemented
We implemented additional features per TA and peer feedback for our app in this milestone. We migrated our plotting library from Altair to Plotly. By incorporating the Plotly plots, we improved the aesthetics of the app. Moreover, we enabled the click interaction on the studio boxplots to filter the following scatter plot/table by selected studio. This helps complete the story flow and adds complexity to our app. We noted that Dash does not seem to have an elegant way to track the individual callback trigger, so the way to reset our plot remains manual. However, we counter this by provide guiding text for users to guide their usage of the lower charts.

We also tried to improve the app in other ways. We added the mean revenue and mean vote average vertical lines in the studio boxplots so that user could compare which studio is doing better or worse than average. We stacked the voting scatter plot and the table horizontally so that the app visualizes nicely in one full page. We added 2 more summary cards `average profit` and `vote count` so that more numeric summaries are displayed. We introduced the native sorting feature for the table of top movies. Finally, other edits are also made to improve the general aesthetics. 

## What can be improved
We could add more controls on the left sidebar to further increase the complexity of our app. However, our data do not provide extra dimensionality for us to do this. To complete this, we need to collect more data and incorporate them into our original dataset. With our time and resource constraints, we decided not to pursue this task. 

## Thoughts on the feedback
We received valuable feedbacks from our TA and peer. Per our TA's and peer's feedback, our app is clean and has good design/flow. It is easy to use and effective in fulfilling its purpose. Improvement feedback that we got both from our TA and peer is that we could add more complexity/functionality to our app from (i) adding a median/mean vertical line to the boxplots to (ii) horizontally stacking the scatter plot, which we find very helpful in making our app better. Therefore, we kept most of the app design and focus on improving interactivity and introducing new features swiftly. We are very happy with our results after this milestone.

