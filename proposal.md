# Our role: Data scientist consultancy firm

# Target audience: Online streaming service company

## Section 1: Motivation and Purpose

More and more people are watching movies online instead of going to movie theaters. Online streaming services need to make sure that the movies they provide on their platforms and going to be popular among users of their services. If we could understand the factors that lead to higher vote values, it may be possible to for the streaming service to increase thier revenue by purchasing only the more popular movies. To address this challenge, we propose building adata visualization app that allows decision makers in the streaming companies to explore a dataset of movies to determine the popular movies characteristics that they need to provide to their users. Our app will show the distribution of the factors contributing the vote score recieved by a particular movie and allow users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to a higher vote score.

## Section 2: Description of the data

We will be visualizing a dataset of approximately 1,008 movies. Each movie has 9 associated variable that describe the movies unique `id`, `title`, `runtime`, `budget`, `revenue`, `genres`, `studios`, `vote_average`, and `vote_count`. We could add a variable key_word extracted from the title.

## Section 3: Research questions and usage scenarios

Sara is a decision maker in a new online streaming service, Bestflix, and she wants to understand the factors that lead to higher movie rating score in order to make decisions on what movies the company should provide on their platform. She wants to be able to explore a dataset in order to compare the effect of the different variables on movie rating and identify the most relevant variables to use in selecting movies to be provided. When Sara logs on to the "Movies Rating App", she will see an overview of all the available variables in her dataset. She can filter our variables to compare specific factors, or rank movies according to thier vote_average score, and order movies based on vote_average. When she does so, Sara notices that higher runtime appears to be a strong predictor of a higher vote average and therefore decides to not spend resources on providing shorter content in the platform. 
