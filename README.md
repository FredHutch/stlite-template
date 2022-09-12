# Python-Based Data Viz (No Installation Required)
## Write interactive apps in Python for non-computational users, without having to keep a server running

Hosted at [https://fredhutch.github.io/stlite-template/](https://fredhutch.github.io/stlite-template/)

No matter what type of organization you work in, people working in data science
exist on a spectrum of computational skills and background. 
One of the biggest challenges for computationally-savvy researchers is how to most
effectively deliver useful tools to their non-computational colleagues.
While Python is an extremely powerful tool for data analysis and visualization, it
is not trivial for non-computational researchers to install and run python-based
apps on their own computers.

However, recent innovations in [WebAssembly](https://webassembly.org/) have made
it possible to run Python code **directly inside the web browser**.
Instead of having to keep a Python server running, you can now just set up a
static webpage which performs all of the needed computation directly on the user's
machine.
In this tutorial I will walk you through a few simple steps for setting up a
Python-based web app (using [Streamlit](https://streamlit.io/)) to be launched
by users _without having to install absolutely anything_.
