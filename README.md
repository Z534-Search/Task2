# Yelp-Dataset-Challenge
ILS - Z534 Search Project on Yelp Dataset Challenge

## Group 4 Team Members:
* [Dhvani Deven Kotak](https://github.com/dhvanikotak) (dkotak@indiana.edu)  
* [Manikandan Murugesan](https://github.com/manikandan5) (murugesm@indiana.edu)  
* [Rohit Dandona](https://github.com/rohitdandona) (rdandona@indiana.edu)  
* [Vikrant Kaushal](https://github.com/KaushalVikrant) (vkaushal@indiana.edu)  
* [Yash Sumant Ketkar](https://github.com/yashketkar) (yketkar@indiana.edu)

## Task 2

Question: To help the entrepreneurs find the best location to build a successful restaurant.

Requirements:
- Python Version - 2.7.12
- MongoDB Version - 3.4
- Run `pip install pymongo`
- Run `pip install gensim`
- Run `pip install nltk`
- Run `import nltk` and `nltk.download()` in a python shell
- Run `pip install -U jupyter`
- Run `jupyter nbextension enable --py --sys-prefix widgetsnbextension`
- Run `pip install gmaps`
- Run `jupyter nbextension enable --py gmaps`

- python CorpusLoader.py
 - Populates the reviews for Phoenix, Arizona from the dataset JSON files where type of business equals to the restaurant.
 - Makes reviews more simplified for analysis by using nltk.

- python TopicModelling.py
 - Gensim python library creates a LDA model for different reviews.

- python DisplayTopics.py
 - Displays the six major topics and the sub-topics with maximum weightages respectively.
 - All 60 topics were categorized so as to highlight the sub-topic they represent.
 - The 60 subtopics highlighted in topics.txt

- python GetBusinessRating.py
 - Create Ratings Collection in MongoDB.

- python SaveBusinessInfo.py
 - Create Business Info Collection in MongoDB.

- python GetTop10BusinessTopic.py
 - Business Frequency Topic is plotted by data generated.

- python DisplayTopicsForReview.py
 - Displays the topics for review.

- Open Google_Maps_Heat_Map.ipynb in Jupyter Notebook
 - Enter the topic and rating.
 - Displays a heatmap of restaurants based on topic
