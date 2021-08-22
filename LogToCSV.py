import pandas as pd
from datetime import datetime

def main():
    df = pd.read_csv("api.log", delimiter=r'\s+', names=["Date","Time", "LoggerType", "MessageType", "UID", "Message"])
    dictionary = {}

    for index, row in df.iterrows():
        timestamp = datetime.strptime(row["Date"]+" "+row["Time"], '%Y-%m-%d %H:%M:%S,%f')

        if row['UID'] not in dictionary:
            dictionary[row['UID']] = {"Start Time": timestamp, "Log Message": row["Message"]}
        else:
            if dictionary[row['UID']]["Start Time"] > timestamp:
                dictionary[row['UID']]["End Time"] = dictionary[row['UID']]["Start Time"]
                dictionary[row['UID']]["Start Time"] = dictionary[row['UID']]["End Time"]
                dictionary[row['UID']]["Log Message"] =  row["Message"] + " - " +dictionary[row['UID']]["Log Message"]
            else:
                dictionary[row['UID']]["End Time"] = timestamp
                dictionary[row['UID']]["Log Message"] += " - " + row["Message"]
            timeDiff = dictionary[row['UID']]["End Time"] - dictionary[row['UID']]["Start Time"]
            dictionary[row['UID']]["Time Diff"] = timeDiff.total_seconds()
    

    formatedDf = pd.DataFrame.from_dict(dictionary, orient="Index") 
    formatedDf.to_csv("api_log.csv", index=False, columns=["Log Message", "Start Time", "End Time", "Time Diff"])

if __name__ == "__main__":
    main()