# ApiLogToCSV
The github repo contains two python files. 

The ```LogToCsv.py``` file takes the ```api.log``` file as input and generates the ```api_log.csv``` file in the specified format. In order to run ```LogToCSV.py```, you need to have ```pandas``` installed. You can find installation instructions here [Installing pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).

The ```analysis.py``` file takes the ```api_log.csv``` file as input and generates the following plots: 
- ```frequencies```: A bar chart comparing the number of requests received for each request type.```imgs/freq_requests.png```
- ```boxplots```: boxplot comparisons for time taken to complete each request type.```imgs/boxplots_completion_time.png```
- ```request volume```: for each request type - the program plot the volume of requests received during different times the day. Images in ```imgs/tod```

To run the ```analysis.py```, you will have to have ```numpy``` and ```seaborn``` installed in addition to ```pandas```. [Installing seaborn](https://seaborn.pydata.org/installing.html), [Installing numpy](https://numpy.org/install/).


