from flask import Flask, render_template, request
import json
from parser import * 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():

    skills = ["Python", "C++", "Java", "Javascript", "Typescript", "MATLAB", "Scala", "Shell Script", "Keras", "Pytorch", "OpenMP", "MPI", "Hadoop", "Kafka", "Spark", "Elasticsearch", "Kibana", "Docker", "Kubernetes", "ROS", "Android Studio", "MySQL", "Postgresql", "MongoDB", "Data Intensive Computing", "Machine Learning", "Deep Learning", "Reinforcement Learning"]
    names = ["Stock Investment Agent with A2C", "Rumour Detection with BERT and GCN", "Music Sample Detection"]
    explains = [
                [ 
                    "- Trained an investment agent less losing money in a bear market with the stock data of Samsung Electronics and Hyundai Motors from 1980 to 2010 with A2C Model", 
                    "- Implemented an auto trading program using Volatility Breakout Strategy and 14-days Moving Average, made a 3% return on Bitcoin."
                ], 
                [
                    "- Trained BERT and 3-layered GCN model classifying the stances of the text and comments of rumoureval 2019's Twitter and Reddit data and returning the probability of whether it is a rumor or not. Stance classification recorded an accuracy of 67%, and rumor detection recorded an accuracy of 70%. This study was selected as the best study in the Advanced Natural Language Processing class."
                ], 
                [
                    "- Trained various the number of CNN layers and BiRNN layers to detect two samples in Prime Loops Dubhop Beats in 100 soundtracks made by Logic Pro, and to return the probability of real time sample, and recorded up to 63%"
                ]]

    # skills = ["Python", "C++", "Java", "Javascript", "MATLAB", "Scala", "Shell Script", "Hadoop", "Kafka", "Spark", "Airflow", "Docker", "Kubernetes", "Jenkins", "MySQL", "Postgresql", "MongoDB", "Data Intensive Computing", "Machine Learning", "Deep Learning", "Reinforcement Learning"]


    length_items = len(names)
    # file = request.args['jobid']+'.json'
    # print(keyword_extract(file))

    return render_template('test3.html', skills = skills, names=names, explains=explains, length=length_items)

if __name__ == '__main__':
    app.run(debug=True)

