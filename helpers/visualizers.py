import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm

def get_normal_distribution(data):
    # fit normal distribution to the data
    mean = np.mean(data)
    std_dev = np.std(data)
    normal_dist = np.random.normal(mean, std_dev, 1000)
    
    return mean, std_dev.round(2), normal_dist

def get_histogram(data, mean, std_dev):
    # determine the number of bins needed for the histogram
    num_bins = int(np.sqrt(len(data)))

    # create a histogram
    histogram = go.Histogram(x=data, nbinsx=num_bins, histnorm='probability', name='Histogram')

    # create a normal distribution curve
    x = np.linspace(min(data), max(data), 1000)
    y = norm.pdf(x, mean, std_dev)
    histogram_normal = go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution', line=dict(color='red', width=3))

    # create standard deviation lines
    std_dev_lines = []
    for i in range(-3, 4):
        line = go.Scatter(x=[mean + i * std_dev, mean + i * std_dev],
                        y=[0, norm.pdf(mean + i * std_dev, mean, std_dev)],
                        mode='lines',
                        line=dict(color='blue', dash='dash'),
                        showlegend=False)
        std_dev_lines.append(line)

    # generate a histogram figure
    figure = go.Figure(data=[histogram, histogram_normal] + std_dev_lines)

    figure.update_layout(
        title='Fit Sentiment Results: Mean={:.2f}, Standard Deviation={:.2f}'.format(mean, std_dev),
        xaxis_title='Sentiment Score Value',
        yaxis_title='Probability Density'
    )

    figure.write_html(r'..\sentiment-analysis\outputs\sentiment_histogram.html')

def get_stacked_barchart(dataframe, groupby_field, values_field):

    # make dataframe where each row corresponds to a group, and the columns contain counts of value for that group.
    chart_data = dataframe.groupby(groupby_field)[values_field].value_counts().unstack(fill_value=0)
    chart_data = chart_data.rename_axis(columns=None).reset_index()
    chart_data.columns = [groupby_field, 'NEGATIVE', 'NEUTRAL', 'POSITIVE'] 

    # reshape the dataframe so it works with plotting
    melted = chart_data.melt(id_vars=groupby_field, var_name=values_field, value_name='Count')

    # generate a chart figure
    figure = px.histogram(melted, x=groupby_field, y='Count', color=values_field, pattern_shape=values_field)

    figure.write_html(r'..\sentiment-analysis\outputs\sentiment_chart.html')