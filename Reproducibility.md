Steps provided are to help recreate the project using Google Colab

1. Download Datasets from Kaggle.com 
[Top 50 Games](https://www.kaggle.com/datasets/devrimtuner/top-100-video-games) 
[Popular Video Game Title](https://www.kaggle.com/datasets/matheusfonsecachaves/popular-video-games)
Code assume that all the datasets are in a folder called 'datasets'. 
2. Upload Github File of notebook
[Original Notebook](https://github.com/Tommyphung1/Project_5/blob/master/Final_Notebook.ipynb)
3. Import Custom Functions
Instruction for importing functions to Google Colab are commented in the Notebook and can be uncommented to be run.
Functions were used mainly to visualize the data for results. Other functions ain't necessary to create the model and can be run without them. The models used have built in method to help obtain the feature importance that was presneted in the project. [Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) and [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier) mehtods can be found in there corresponding links. 

Note: Notebook was setup with dataset in the a seperate folder. Repath the import to the location. If using default directory, use 
df = pd.read_csv('/content/backloggd_games.csv')    ### Main dataset with the genres.
ranked_df = pd.read_csv('/content/vgsales.csv')     ### Dataset to grab global sales from. 