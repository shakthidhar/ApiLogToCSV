from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def generate_plots(df):

    unique_requests = df["Log Message"].unique()

    for i in range(0, len(unique_requests)):
        df["Log Message"] = df["Log Message"].str.replace(unique_requests[i],unique_requests[i][:unique_requests[i].index("start")])

    # plot for frequencies of requests
    print("generating plot for frequencies of requests...", end=" ")
    sns.countplot(data=df, x="Log Message")
    plt.xlabel("Request Type")
    plt.savefig("imgs/freq_requests.png")
    plt.clf()
    print("complete!")

    # plot boxplots time taken to complete the request
    print("generating boxplots for time taken to complete the request...", end=" ")
    sns.boxenplot(data=df, y="Time Diff", x="Log Message")
    plt.xlabel("Request Type")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Distribution of request completion duration")
    plt.savefig("imgs/boxplots_completion_time.png")
    plt.clf()
    print("complete!")

    # for each request plot volume of requests across different periods during the day
    print("generating plots volume of requests across different periods during the day...", end=" ")
    request_groups = df.groupby(["Log Message"])
    
    for name, group in request_groups:
        time_of_day, freq_percentage = time_of_day_frequency(group)
        y_pos = np.arange(len(time_of_day))
        plt.bar(y_pos, freq_percentage)
        plt.xticks(y_pos,time_of_day)
        plt.ylabel("Percentage of Requests")
        plt.xlabel("Time of Day")
        plt.title( "Requests for "+ name)
        plt.savefig("imgs/tod/tod_freq_"+name+".png")
        plt.clf()
    print("complete!")

def time_of_day_frequency(df):
    # Computing volume of requests receveied during different times of the day
    time_of_day = ("Morning","Afternoon","Evening","Late Night","Early Morning")
    counts = [0,0,0,0,0]

    for i in range(len(df)):
        start_time = datetime.strptime(df.iloc[i]["Start Time"], '%Y-%m-%d %H:%M:%S.%f')
        morning = start_time.replace(hour=9, minute=0, second=0, microsecond=0)
        noon = start_time.replace(hour=12, minute=0, second=0, microsecond=0)
        evening = start_time.replace(hour=17, minute=0, second=0, microsecond=0)
        night = start_time.replace(hour=21, minute=0, second=0, microsecond=0)
        midnight = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

        if start_time >= morning and start_time < noon:
            counts[0]+=1
        if start_time >= noon and start_time < evening:
            counts[1]+=1
        if start_time >= evening and start_time < night:
            counts[2]+=1
        if start_time >= night and start_time < midnight:
            counts[3]+=1
        if start_time >= midnight and start_time < morning:
            counts[4]+=1
    
    counts = [(x/len(df))*100 for x in counts]
    return time_of_day, counts

def main():
    df = pd.read_csv("api_log.csv")

    generate_plots(df)

if __name__ == "__main__":
    main()