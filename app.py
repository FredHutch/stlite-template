import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import plotly.express as px

st.title("Demo - Airway RNAseq Analysis")

@st.cache
def read_counts(nrows, url="https://github.com/BRITE-REU/programming-workshops/raw/master/source/workshops/02_R/files/airway_scaledcounts.csv"):

    df = pd.read_csv(
        url,
        nrows=nrows,
        index_col=0
    )

    return df

@st.cache
def read_metadata(url="https://github.com/BRITE-REU/programming-workshops/raw/master/source/workshops/02_R/files/airway_metadata.csv"):

    return pd.read_csv(
        url,
        index_col=0
    )

@st.cache
def run_ttest_genes(counts):
    """Compare the counts for treatments and controls."""

    return counts.apply(
        run_ttest_single,
        axis=1
    ).dropna(
    ).assign(
        neg_log_p=lambda d: -d["p"].apply(np.log10)
    ).reset_index(
    )

# Get the samples from the treatments and controls
@st.cache
def get_labels():

    metadata = read_metadata()

    return {
        label: m.index.values
        for label, m in metadata.groupby("dex")
    }

def run_ttest_single(r):

    labels = get_labels()
    
    return pd.Series(dict(
        zip(
            ["stat", "p"],
            stats.ttest_ind(
                r.loc[labels["treated"]],
                r.loc[labels["control"]]
            )
        )
    ))

def plot(stats_df):

    fig = px.scatter(
        stats_df,
        x="stat",
        y="neg_log_p",
        title="Comparison of genes in treated vs. control",
        labels=dict(
            stat="t-test statistic",
            neg_log_p="p-value (-log10)",
        ),
        hover_data=["ensgene"]
    )

    st.plotly_chart(fig)

if __name__ == "__main__":

    counts = read_counts(
        st.number_input(
            "Number of genes to test",
            min_value=100,
            max_value=38694,
            step=100,
            value=100,
            help="Number of genes to test"
        )
    )

    stats_df = run_ttest_genes(counts)

    plot(stats_df)