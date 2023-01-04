from flask import Flask, render_template, request
import json
# from parser import * 
app = Flask(__name__)
import json
import os

@app.route('/', methods=['GET'])
def hello_world():

    skills = ["C++", "Python",  "Java", "Javascript", "Typescript", "MATLAB", "Scala", "Shell Script", "Keras", "Pytorch", "OpenMP", "MPI", "Hadoop", "Kafka", "Spark", "Elasticsearch", "Kibana", "Docker", "Kubernetes", "ROS", "Android Studio", "MySQL", "Postgresql", "MongoDB", "Data Intensive Computing", "Machine Learning", "Deep Learning", "Reinforcement Learning"]
    project_names = ["Stock Investment Agent with A2C", "Rumour Detection with BERT and GCN", "Music Sample Detection"]
    project_explains = [
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

    length_items = len(project_names)

    return render_template('test.html', skills = skills, names=project_names, explains=project_explains, length=length_items)

@app.route('/template3', methods=['GET'])
def tempelate3():

    # files = os.listdir('jobs')
    # file = files[0]
    # print(file)
    # f = open("jobs/"+file, "r+")
    # data = json.load(f)
    # data['title'] = file.split('.')[0]
    # return render_template('test3.html', 
    #     data = data
    # )

    key = request.args.get('f')
    files = list( filter ( lambda x : key in x, os.listdir('jobs/json/')))
    file = files[0]
    f = open("jobs/json/"+file, "r+")
    data = json.load(f)
    data['title'] = file.split('.')[0]

    res = render_template('test3.html', data = data)
    res = res.replace("&lt;strong&gt;", "<strong>")
    res = res.replace("&lt;/strong&gt;", "</strong>")
    return res


@app.route('/template4', methods=['GET'])
def tempelate1():

    key = request.args.get('f')
    files = list( filter ( lambda x : key in x, os.listdir('jobs/json/')))
    file = files[0]
    f = open("jobs/json/"+file, "r+")
    data = json.load(f)
    data['title'] = file.split('.')[0]

    res = render_template('template4.html', data = data)
    res = res.replace("&lt;strong&gt;", "<strong>")
    res = res.replace("&lt;/strong&gt;", "</strong>")

    return res


if __name__ == '__main__':
    app.run(debug=True)
