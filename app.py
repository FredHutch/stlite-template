import streamlit as st
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy
import plotly.express as px
from pyodide.http import open_url

st.title("Demo - Interactive Heatmap")

@st.cache(show_spinner=False, max_entries=1)
def read_url(url:str):
    """Read the CSV content from a URL"""

    return pd.read_csv(
        # Use the pyodide utility to read the URL, because
        # requests is currently broken
        open_url(url),
        index_col=0
    )

def plot(
    counts:pd.DataFrame,
    top_n=1000,
    norm="none",
    method="average",
    metric="euclidean"
):

    # Make a list of messages to display after the plot
    msgs = []

    # Normalize the raw input values
    if norm == "prop":
        msgs.append("Values normalized to the proportion of each column")
        counts = counts / counts.sum()
    elif norm == "CLR":
        msgs.append("Values transformed to the centered-log-transform of each column")
        counts = counts.applymap(np.log10)
        gmean = counts.apply(lambda c: c[c > -np.inf].mean())
        counts = counts / gmean
        counts = counts.clip(lower=counts.apply(lambda c: c[c > -np.inf].min()).min())

    # Filter by top_n
    counts = counts.reindex(
        index=counts.sum(
            axis=1
        ).sort_values(
            ascending=False
        ).head(
            int(top_n)
        ).index.values
    )

    # Order the rows and columns
    counts = counts.reindex(
        index=get_index_order(counts, method=method, metric=metric),
        columns=get_index_order(counts.T, method=method, metric=metric),
    )

    # Make the plot
    fig = px.imshow(
        counts,
        color_continuous_scale='RdBu_r',
        aspect="auto",
        labels=dict(
            color=dict(
                none="counts",
                prop="proportion"
            ).get(norm, norm),
            x="sample"
        )
    )

    # Display the plot
    st.plotly_chart(fig)

    # Print the messages below the plot
    for msg in msgs:
        st.text(msg)


def get_index_order(counts, method=None, metric=None):
    """Perform linkage clustering and return the ordered index."""
    return counts.index.values[
        hierarchy.leaves_list(
            hierarchy.linkage(
                counts.values,
                method=method,
                metric=metric
            )
        )
    ]

def run():
    """Primary entrypoint."""

    # Read the counts specified by the user
    counts = read_url(
        st.sidebar.text_input(
            "Counts Table",
            value="https://raw.githubusercontent.com/BRITE-REU/programming-workshops/master/source/workshops/02_R/files/airway_scaledcounts.csv",
            help="Read the abundance values from a CSV (URL) which contains a header row and index column"
        )
    )

    # Render the plot
    plot(
        counts,
        top_n=st.sidebar.number_input(
            "Show top N rows",
            help="Only the subset of rows will be shown which have the highest average values",
            min_value=1000,
            max_value=counts.shape[0]
        ),
        norm=st.sidebar.selectbox(
            "Normalize values by",
            help="The raw values in the table can be normalized by the proportion of each column, or by calculating the centered log transform",
            index=2,
            options=[
                "none",
                "prop",
                "CLR"
            ]
        ),
        method=st.sidebar.selectbox(
            "Ordering - method",
            help="The order of rows will be set by linkage clustering using this method",
            index=6,
            options=[
                "average",
                "complete",
                "single",
                "weighted",
                "centroid",
                "median",
                "ward"
            ]
        ),
        metric=st.sidebar.selectbox(
            "Ordering - metric",
            help="The order of rows will be set by linkage clustering using this distance metric",
            index=7,
            options=[
                "braycurtis",
                "canberra",
                "chebyshev",
                "cityblock",
                "correlation",
                "cosine",
                "dice",
                "euclidean",
                "hamming",
                "jaccard",
                "jensenshannon",
                "kulczynski1",
                "mahalanobis",
                "matching",
                "minkowski",
                "rogerstanimoto",
                "russellrao",
                "seuclidean",
                "sokalmichener",
                "sokalsneath",
                "sqeuclidean",
                "yule"

           ]
        ),
    )

if __name__ == "__main__":

    run()
