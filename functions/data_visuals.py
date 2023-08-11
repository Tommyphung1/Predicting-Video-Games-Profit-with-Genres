import matplotlib.pyplot as plt
import numpy as np

def visual_baseline(list_1, list_2):
    '''
    Input: List_1, list_2 - lists
    Output: BarH graphs
    Take two lists and visualize as bar graphs.
    Both lists have names and values and needs to be seperated from each other. 
    '''
    
    x = [x[0] for x in list_1]
    y = [x[1] for x in list_1]

    x_2 = [x[0] for x in list_2]
    y_2 = [x[1] for x in list_2]
    
    fig, ax = plt.subplots(ncols= 2,figsize = (25,8))
    ax[0].barh(x, y)
    ax[0].set_title('Feature Importance - Over 1')
    xlabel = ['{}%'.format(x) for x in np.arange(0,20,2)]
    ax[0].set_xticks(np.arange(0,20,2));
    ax[0].set_xticklabels(xlabel);
    ax[0].set_ylabel('Genres');
    ax[0].set_xlabel('Percentage');

    ax[1].barh(x_2, y_2)
    ax[1].set_title('Feature Importance - Indie')
    xlabel = ['{}%'.format(x) for x in np.arange(0,20,2)]
    ax[1].set_xticks(np.arange(0,20,2));
    ax[1].set_xticklabels(xlabel);
    ax[1].set_ylabel('Genres');
    ax[1].set_xlabel('Percentage');
    
def visual_top_5(list_1, list_2):
    '''
    Input: List_1, list_2 - lists
    Output: BarH graphs
    Take two lists and visualize as bar graphs.
    Both lists have names and values and needs to be seperated from each other. 
    Only display the top 6 genres 
    '''
    x = [x[0] for x in list_1]
    y = [x[1] for x in list_1]

    x_2 = [x[0] for x in list_2]
    y_2 = [x[1] for x in list_2] 


    fig,ax = plt.subplots(ncols= 2, figsize = (25, 5))

    xlabel = ['{}%'.format(x) for x in np.arange(0,14,2)]
    ax[0].barh(x[17:24], y[17:24])
    ax[0].set_title('Feature Importance - Over 1')

    ax[0].set_xticks(np.arange(0,14,2));
    ax[0].set_xticklabels(xlabel);
    ax[0].set_ylabel('Genres');
    ax[0].set_xlabel('Percentage');

    for i, v in enumerate(y[17:24]):
        ax[0].text(v + .2, i, str(v) + '%', color='blue', fontweight='bold')
        
    ax[1].barh(x_2[17:24], y_2[17:24])
    ax[1].set_title('Feature Importance - Indie')
    ax[1].set_xticks(np.arange(0,14,2));
    ax[1].set_xticklabels(xlabel);
    ax[1].set_ylabel('Genres');
    ax[1].set_xlabel('Percentage');

    for i, v in enumerate(y_2[17:24]):
        ax[1].text(v + .2, i, str(v) + '%', color='blue', fontweight='bold')