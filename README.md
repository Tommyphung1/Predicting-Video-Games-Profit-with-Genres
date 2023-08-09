# Project 5
**Author:** Tommy Phung <br>
**Target:** Video Game Developers

## Overview 
With the increasing demand for video games, the market is primed and ready for investment and development. However, there isn't a hard and fast rule to make a great game much less a profitable one. There are many aspects to making video games and one of the most controllable features was the genre of the game. By narrowing down which genres are profitable, developers can focus on making the correct games when concerning profit. The best place to look is the community website, backloggd to get a better idea of what people actually like. 

It turns out that some of the most common genre happens to be profitable as well. This doesn't necessarily help since Adventure and RPG are common genres to have in games. Indie genres or Indie game shows are one of the best genres to have when making a game. Setting aside the Indie genre, I can isolate which genres are good when modeling. Indie developers can stick to popular features mentioned before but can also consider arcade and strategy in their games as well. Keeping Adventure and RPG will keep the games relatively safe to make while enhancing a mixture of the suggested genres. 

When moving the threshold of success for more developed companies was a bit more complicated. The first model shows similar results to the Indie Model with Simulator and Puzzle as important genres to focus on. However, when rebalancing the dataset, brawler came up as an important feature. If a company wants to explore brawlers, this could be a fruitful endeavor due to the low quality of brawler-based games. Rebalancing doesn't seem to change the results but other features should be looked at such as developer since the rebalanced model performed poorly. 

The produce models perform best when considering a lower threshold and should only be used for Indie Developers. More data is needed to help determine better genres for higher sales or more analysis is needed to help the model. 

## Business Understanding 
Video games have been a form of entertainment for all ages around the world. There has been **an increase in game production** with all the access to tools online as well as the demand for these games especially for the last couple of years of quarantine. <br>
Every year, **Steam**, one of the largest online video game platforms, has **300 games** on average published a day and this has only been increasing in the past decade.  
With so many games getting published, there is **a risk that the game won't be made profitable**. <br>

Depending on the **company size**, the number of sales changes can be a sign of a profitable game. <br>
For example, **Triple-A games** are expected to have a sale of **10 million units** whereas **Indie games**, which are smaller game companies, would expect **100,000 units** to be successful. 
There is also a bigger budget range when comparing Triple-A companies and Indie companies. 
To make a game that many would be interested in buying, **certain genres are more desirable than others** for the average player. <br>
By modeling the genres of the games, we can **isolate the genres to the best** to have when making a game that would **reach the benchmark** mentioned above. 

This information would be useful to have for **Indie developers** that would sell their games on Steam but can apply to other platforms. If a **new developer** is attempting to create a game, they should use the information to determine the best type of game that the audience would want to buy. **Triple-A** companies using the model should look at the worst genres and avoid those since they are already established and could improve their current library of games instead. 

## Data Understanding 
The first dataset came from [Backloggd](https://www.backloggd.com/) and [Kaggle](https://www.kaggle.com/). <br>
Backloggd is a **community-based** listing website that takes lists of games and combined them with various features such as **ratings, played, and wishlist**. The main feature we looked at is **genres** with some insight gained from the rating feature. <br>
The second dataset contains the **sales of games** from various regions. I looked at **Global Sales** which is just the sum of all the columns in the dataset. 

Since I am using both datasets, they **need to match** with one another to analyze them fairly. This was the breakdown of the number of games and the final resulting dataframe. 
The majority of the games were not included due to different name changes or non-English titles. Some were also too obscured to be included in the list entirely. 

|  | Backloggd | Ranked | **Final** |
|---|:---:|:---:|:---:|
| **# of Games** | 60,000 | 16,598 | **4,466** |
| **Desired Feature** | Genres | Global Sales | **N/A** |
| **# of Columns** | 12 | 10 | **6** |

## Data Preparations
To begin, multiple libraries were imported into the notebook for training, testing, and visualization. I created some functions to reduce the clutter made from all the visualizations. <br>
The majority of the libraries came from Sklearn to complete most of the modeling and testing. 

The datasets didn't have missing values with the features I was concerned with. There was some data formatting that needed to be done before any analysis was possible.<br>
A metric was also needed to determine a game's success. Overall, a game was considered profitable if it sold over 1 million units or 100,000 if they were an indie or independent developer. When referring to the threshold of profit, I will use old or older for 1 million and 100,000 for newer indie developers. 
These were the step taken to obtain the final dataframe to begin modeling.
1. All of the datasets were imported 
2. The game titles that matched all the datasets were the only ones used. 
3. The columns were Rating, Genres, Global_Sale, and Title. 
4. The column, Genres, were changed to an actual list of the game's genres. 
5. Any duplicate titles were combined if applicable. 
6. Based on the Global_Sales, two new columns were added to the dataframe to indicate profit. 

## Data Distribution
There are **24 genres** with the most common being **Adventure, Indie, RPG, Shooter, and Puzzle**. <br>
[Class Inbalance](http://localhost:8888/lab/tree/pictures/Class%20Distributions%20Both.JPG)
There are clear imbalances in games that perform well based on the threshold given. This could prove troublesome when modeling and would need to be rebalanced to get ideally better results. 

[Ratings](pictures/Rating Distribution.JPG)
When looking at the Ratings for the games, there is a **normal distribution** which indicates that there is an even number of bad and good games in the list. 

[Genre](pictures/Genres Distribution.JPG)
Unsurprisingly, **adventure** was the most common genre in the dataset having roughly **2,500** with this tag, followed by **RGP, Indie, Shooter, and Platform**. <br>
Due to the number of games with these genres, we can expect that most of the profitable games would have **similar genres**.

## Method
The first model will be based on the Decision Tree. Each model will have another similar model but with different target features to look at both the old and new company threshold determine earlier. 
The second model will be using the Random Forest, an ensemble algorithm based on the Decision Tree. Both of the models would be using the default parameters.
The third set of models would be using GridSearch in an attempt to find a better set of parameters. 
There will be a total of 6 models with the metric being the F1-Score. Since we know that there is a class imbalance, we want to make sure to score the model based on how many they predict correctly rather than just accuracy. 

The second set of modeling will be with a balanced training set when fitting the model. Using SMOTE, we oversampled the training set and resample the new data to get a more balanced set. 
The same product was performed and the scores were displayed and compared with one another. 

## Results 
When looking over video games that made over 1 million in sales, the best genres to have **adventure, RPG, simulator, and strategy games**. Since there is a saturation of Adventure and RPG, strategy and simulator games would be best to make games that people would buy. This may be due to that most games pair these genres together so it would best to avoid these genres unless known for the genre themselves. Keep in mind that fewer games may also mean that most audiences may not be looking for that specific genre at all which may limit others to play. The desirable result would be able to make a game that encompasses multiple genres like adding strategy in their adventure games or shooter platformer. 
When looking at the idea of indie developers in mind, there is a slight change in mindset. Indie games have two choices in making a game, make a unique game and define the genre they planned with their game, or go to a niche area that has little to no competition to the genre instead. There seems to be a great deal of interest in indie games as a whole, being consistently the most important genre in making over 100,000 in sales. If the goal is to start making games, it would be safe to stick with the games in the top feature importance to increase the chances of a good game. Once a genre of games proves to be the best, the best advice would be to continue to make the games define themselves to that genre. Most people won't expect anything so sticking with the common titles would be safest. 
When looking at feature importance when looking at the games labeled with Indie, there was a drastic shift in what the model determined as important. It appeared that RPG and Arcade performed the best for both the thresholds meaning that the most successful indie games were with these genres. Other good genres were a variety of platformers, simulators, visual novels, adventure, and fighting. Given how Indie games usually vary, sticking the RPGs and Arcade style games would be best for new developers

| Rank | Over 1,000,000 | Over 100,000 |
|:---:|:---:|:---:|
| 1 | Adventure | RPG |
| 2 | RPG | Platform |
| 3 | **Simulator** | Adventure |
| 4 | **Puzzle** | **Strategy** |
| 5 | Platform | **Arcade** |

## Class Imbalance Results
Since the dataset has a major class imbalance, we need to model again with a more even dataset. The dataset is quite limited so I oversample by synthetically adding more data to the training set. 
SMOTE was used to oversample the dataset and the panda built-in resampling method was to resample 50% of the new balanced dataset. 

After balancing and resampling the training set to get a more even distribution, there was a slight change. Although the majority of the genres stayed the same, two genres stood out even though they were uncommon based on other metrics. Brawler and Fighting seemed to perform well depending on the model and should be explored. This may be too risky for indie developers due to the smaller pool of games and the lower accuracy of the model but could be beneficial for old-known developers in creating the said type of games. 

### Old Model Threshold
| Rank | Baseline | Random Forest |
|:---:|:---:|:---:|
| 1 | **RPG** | **Adventure** |
| 2 | Brawler | Indie |
| 3 | **Adventure** | Puzzle |
| 4 | Puzzle | **RPG** |
| 5 | Simulator | Shooter |

### New Model Threshold
| Rank | Baseline | Random Forest | Random Forest GS |
|:---:|:---:|:---:|:---:|
| 1 | Adventure | Indie | Brawler |
| 2 | Indie | **Stategy** | **Arcade** |
| 3 | **Strategy** | **Adcade** | Indie |
| 4 | **Arcade** | Adventure | **Strategy** |
| 5 | Simulator | RPG | Fighting |

## Recommendations

**Triple-A Developer**: <br>
**Safe genres** to make are **Adventure and RPG** due to their reliability in the gaming market. <br>
Add **puzzles and simulators** for added variety in games to increase performance.

**Indie Developers**: <br>
Avoid uncommon genres and stick to common genres. **Adventure and RPG** are safe as well along with **platformer and shooters**. <br>
Adding **Strategy or Acade** in their game would increase the likelihood of performing well. 

Next Step
1. Add developer and publisher to the model. 
There are potential markers that may prove to be a huge factor in making a profitable game. 
2. More games
There were a lot of games that weren't added to the final dataframe due to the title not matching perfectly and it would take too much time to individually look and see why that would be the case. More data would ideally lead to better modeling. 
3. Determine trends in genres
Throughout history, there have been trends that I have noticed from game developers making similar styles of games. Some example from the top of my head was the MOBA, Open World, and Battle Royal trend in most recent years where they were extremely popular and widely made even poorly. 