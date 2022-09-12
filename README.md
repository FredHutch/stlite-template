# Python-Based Data Viz (With No Installation Required)

## Write interactive apps in Python for non-computational users, without ever having to run a server

No matter what type of organization you work in, people working in data science
exist on a spectrum of computational skills and background. 
One of the biggest challenges for computationally-savvy researchers is how to most
effectively deliver useful tools to their less-computational colleagues.
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

## Weighing benefit and cost in data science

Working as a bioinformatician, I'm always on the lookout for new tools which can help
me perform really useful analyses for my collaborators.
But the decision to adopt a new tool is not purely based on what it can deliver -- 
I also have to weigh the difficulty of learning to use that new tool.
For a long time the world of web development felt like it was out of my reach purely
based on the apparent difficulty of learning JavaScript alongside HTML/CSS.

While it is true that Python (and R) can both be used to set up interactive
web apps, those libraries (Flask, Dash, Streamlit, and Shiny) are intended to
be run on active servers which perform all of the computation and then send the
results to the user's browser.
It is inherently much more difficult to run web apps in this way, both because
of the expense of keeping a machine constantly running as well as the complexity
of providing a protected network connection.
There are some wonderful hosted solutions for sharing R and Python based apps,
but it's complex enough that I'm not going to set up my own version.

## How it became possible

The transformational tool which profoundly changed the landscape of software
development has been [WebAssembly](https://webassembly.org/), which makes it
possible to compile Python code so that it can be run directly in a web browser.
Making code which runs in the web browser is fantastic because you no longer have
to ask a user to install any dependencies -- they almost certainly already have
a web browser.

The project which has implemented Python in JS is called [Pyodide](https://pyodide.org/en/stable/).
Using this framework, [Yuichiro Tachibana](https://github.com/whitphx) has
made a port of the Python GUI library [Streamlit](https://streamlit.io/)
called [stlite](https://github.com/whitphx/stlite).
Using stlite it is possible to write Python code which is run entirely in the
web browser, meaning that the user doesn't need to install anything for it to
run.

I may not have been as excited by this if I were not already a huge fan
of [Streamlit](https://streamlit.io/).
This Python library makes it extremely easy to build a simple GUI which
drives any sort of data visualization you like.
There is native integration with multiple powerful plotting libraries
(PyPlot, Altair, Vega Lite, Plotly, Bokeh, pydeck, and graphviz), as
well as flexible controls for user input, page layout, and media
display.
Most importantly the brainspace-overhead is low -- you don't have to learn
much to get started.
If you are already working in Python and want to quickly prototype and deploy
an interactive web app, it is definitely worth your time to explore
Streamlit.

And now, those Streamlit apps can be served to users and run directly in
the browser.

## Intended use and limitations

You can make an effective GUI using Python and stlite as long as you remember
that it is being run directly in the user's browser.

- Operations which require a large amount of memory, CPU, or I/O will likely cause problems --
try to keep the computation as lightweight as possible;
- Any files which you need to read in must also be available to the user's browser,
either by (1) hosting them yourself, (2) accessing them at a public URL, or (3)
when the user 'uploads' them into the browser;
- Access control matters -- anyone with access to the webpage will be able to run the app _and_ read its source.

## Getting started

This guide will walk you through:

1. Copying a template repository on GitHub
2. Adding your Streamlit app
3. Testing locally
4. Deploying publicly to the web with GitHub Pages

To use this guide you should have familiarity with (1) manipulating
software repositories on GitHub and (2) running Streamlit locally.

### 1. Fork the template repository

Navigate to the [FredHutch/stlite-template](https://github.com/FredHutch/stlite-template)
repository and [fork it](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
into your own account or organization.
Make sure to change the name and description, since you will be making
something entirely new.

![fork-repo](./img/fork-repo-screenshot.png)


Hosted at [https://fredhutch.github.io/stlite-template/](https://fredhutch.github.io/stlite-template/)

