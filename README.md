# Project 5
**Author:** Tommy Phung <br>
**Target:** Video Game Developers

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
Backloggd is a **community-based** listing website that takes lists of games and combined them with various features such as **ratings, played and wishlist**. The main feature we looked at is **genres** with some insight gained from the Ratings feature. <br>
The second dataset contians the **sales of games** from various regions. I looked at **Global Sales** which is just the sum of all the columns in the dataset. 

Since I am using both dataset, they **need to match** with one another to anaysis them fairly. This was the brekadown on the number of games and the final resulting dataframe. 
Majority of the games were not included due to different name changes or non english titles. Some were also to obsured to be included in the list entirely. 

|  | Backloggd | Ranked | **Final** |
|---|:---:|:---:|:---:|
| **# of Games** | 60,000 | 16,598 | **4,466** |
| **Desired Feature** | Genres | Global Sales | **N/A** |
| **# of Columns** | 12 | 10 | **6** |

## Data Preperations
To begin, multiple libraries were imported into the notebook for training, testing and visualization. I created some function to reduce the clutter made from all the visiualizations. <br>
Majority of the libraries came from Sklearn to complete most of the modeling and testing. 

The datasets didn't have missing values with the features I was concerned with. There were some data formatting that needed to be done before any anylsis was possible.<br>
A metric was also needed to determine a game success. Overall, a game was considered profitable if they sold over 1 million units or 100,000 if they were an indie or independant developer. When refering to the threshold of profit, I will use old or older for 1 million and 100,000 for newer indie developers. 
These were the step taken to obtain the final dataframe to begin modeling.
1. All of the dataset were imported 
2. The game titles that matched all the datasets were the only one used. 
3. The columns were Rating, Genres, Global_Sale and Title. 
4. The column, Genres, were changed to actual list of the game's genres. 
5. Any duplicate titles were combined if applicable. 
6. Based off the Global_Sales, two new columns were added to the dataframe to indicate profit. 

## Data Distribution
There are **24 genres** with the most common being **Adventure, Indie, RPG, Shooter, and Puzzle**. <br>
[Class Inbalance](http://localhost:8888/lab/tree/pictures/Class%20Distributions%20Both.JPG)
There are clear inbalance in games that perform well based of the threshold given. This could prove troublesome when modeling and would need to be rebalanced to get ideally better results. 

[Ratings](pictures/Rating Distribution.JPG)
When looking at the Ratings for the games, there is a **normal distribution** which indicates that there is an even number of bad and good games in the list. 

[Genre](pictures/Genres Distribution.JPG)
Unsurprisingly, **adventure** was the most common genre in the dataset having roughly **2,500** with this tag, followed by **RGP, Indie, Shooter, and Platform**. <br>
Due to the number of games with these genres, we can expect that most of the profitable games would have **similar genres**.

## Method
The first model will be based off the Decision Tree. Each model will have another similar model but with different target features to look at both the old and new company threshold determine earlier. 
The second model will be using the Random Forest, an ensemble algorithm based off the Decision Tree. Both of the models would be using the default parameters.
The third set of models would be using GridSearch in the attempt to find a better set of parameters. 
There will be a total of 6 models with the metric being the F1-Score. Since we know that there is a class inbalance, we want to make sure to score the model based off how many they predict correctly rather than just accuracy. 

The second set of modeling will be with a balanced training set when pfitiing the model. Using SMOTE, we oversampled the training set and resample the new data to get a more balance set. 
The same producre was performed and the scores were displayed and compared with one another. 

## Results 
When looking over video games that made over 1 million in sales, the best genres to have **adventure, rpg, simulartor and stratgery games**. Since there is a satruatration of Adventure and RPG, stratgety and simulator games would be best to make games that people would buy. This may be due to that most games pair these genres togther so it woud best to avoid these genres unless known for the genre themselves. Keep in mind that less games may also mean that most audience may not be looking for that specific genre at all which may limit others to play. The desireable result would being able to make game that encompass multiple genres like adding stragery in their adventure games or shooter platformer. 
When looking at the idea of indie developers in mind, there is a slight change in mindset. Indie games have two choice in making a game, make a unique game and define the genre they planned with their game, or go to a niche area that have little to no competition to the genre instead. There seems to be a great deal of interest in indie gmaes as a whole, being consistiently the most important genre in making over 100,000 in sales. If the goal is to start making games, it would be safe to stick with the games in the top feature importance to increase the chances of a good game. Once a genre of games proves to be the best, the best advice would be to conitune to make the games to define themsleves to that genre. Most opeople won't expect anything so stikcing with the common titles would be safest. 
When looking at feature importance when looking at the games labeled with Indie, there was a drascic shift in what the model determine as important. It appeared that RPG and Arcade performed the best for both the threshhols meaning that the most successful indie games were with these genres. Other good genres were variety with platformer, simulator, visual novel, adventure, and fighting. Given how Indie games usually varies, sticking the RPG's and Arcade style games would be best for new developers

| Rank | Over 1,000,000 | Over 100,000 |
|:---:|:---:|:---:|
| 1 | Adventure | RPG |
| 2 | RPG | Platform |
| 3 | **Simulator** | Adventure |
| 4 | **Puzzle** | **Strategy** |
| 5 | Platform | **Arcade** |

## Class Inbalance Results
Since the dataset has a major class inbalance, we need to model again with a more even dataset. The dataset is quite limited so I oversample by sythntically adding more data to the training set. 
SMOTE was used to oversample the dataset and pandas built in resampling method to resample 50% of the new balanced dataset. 

After balancing and resampling the training set to get a more even distribution, there was a slight change. Although majority of the gernes stayed the same, two genres stood out even though they were uncommon based off other metrics. Brawler and Fighting seemed to perfrom well depending on the model and should be explored. This may be too risky for indie developers due to the smaller pool of games and the lower accuracy of the model but could be benefitcal for old known developers in creating said type of games. 

| Rank | Over 1,000,000 | Over 100,000 |
|:---:|:---:|:---:|
| 1 | Adventure | RPG |
| 2 | RPG | Platform |
| 3 | **Simulator** | Adventure |
| 4 | **Puzzle** | **Strategy** |
| 5 | Platform | **Arcade** |

## Recommendations

**Triple-A Developer**: <br>
**Safe genres** to make are **Adventure and RPG** due to the reliablity in the gaming market. <br>
Add **puzzle and simulators** for added varity in games to increase performance.

**Indie Developers**: <br>
Avoid uncommon genres and stick to the common genres. **Adventure and RPG** are safe as well along with **platformer and shooters**. <br>
Adding **Strategy or Acade** in their game would increase the likelihood of performing well. 

Next Step
1. Add developer and publisher to the model. 
There is potential markers that may prove to be a igger factor in making a profitable game. 
2. More games
There was a lot of gmaes that weren't added to the final dataframe due to the title not matching perfectly and it would take too much time to individually look and see why that would be the case. More data would ideally lead to better modeling. 
3. Determine trends in genres
Throughout history, there have been trends that I have noticed from game developers make similar sytle of games. Some example on the top of my head was the MOBA, Open World and Battle Royal trend in most recent years where they were extremely popular and widely made even poorly. 