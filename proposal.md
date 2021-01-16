# Our role: Data scientist consultancy firm

# Target audience: Online streaming service company

## Section 1: Motivation and Purpose

More and more people are watching movies online instead of going to movie theaters. Online streaming services need to make sure that the movies they provide on their platforms and going to be popular among users of their services. If we could understand the factors that lead to higher vote values and higher profits, it may be possible to for the streaming service to increase thier revenue by purchasing only the more popular or profitable movies. To address this challenge, we propose building a data visualization app that allows decision makers in the streaming companies to explore a dataset of movies to determine the popular movies that they need to provide to their users. Our app will show the stakeholders which studios and genres are the most popular (or make the most money) and therefore would give them the best value when bidding for their rights.

## Section 2: Description of the data

We will be visualizing a dataset of approximately 1,008 movies. Each movie has 9 associated variable that describe the movies unique `id`, `title`, `runtime`, `budget`, `revenue`, `genres`, `studios`, `vote_average`, and `vote_count`. Our dashboad aims to use `budget`, `revenue` and a derived column `profit` to display the financial performance of a movie and/or a studio. We also aim to use the `vote_average`, `vote_count` to give the users a view on how well liked the movies are, if they feel the need to include that in their decision making process. Finally, our dashboard will allow filters on `genres` and `studios` to give the users the ability to drill down on specific movie performances.

## Section 3: Research questions and usage scenarios

Sara is a decision maker in a new online streaming service, Bestflix. Bestflix is looking to invest in making more horor movies available on their platform to increase their offering's varierty. She wants to know which studios make the most liked and/or the most profitable horror movies in order to make decisions on what movies the company should provide on their platform. She wants to be able to explore a dataset that has the past performance of various movies that she can filer by genre. When Sara logs on to the "Movies Selection App", she will see an overview of all the available movies in her dataset. She can then proceed to find out which studio consistently chooses to make the most profitable horror movies and use that as an indicator for how horror movies from that studio will do in the future. This insight would then help her convince her management to invest in the new, low-budget horror flick produced by the studio she found in her data analysis. If her management needs more convincing, she could go back to the app and find out how well horror movies from that studio are liked generally, using the vote average views. 
