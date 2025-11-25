import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Aнимация с помощью **slider**
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=-5, stop=5, step=0.2, value=1, full_width=True)
    return (slider,)


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(mo, slider):
    import matplotlib.pyplot as plt
    import numpy as np

    t = np.linspace(-10, 10, 100)
    sig = 1 / (1 + np.exp(-t*slider.value))

    fig, ax = plt.subplots()
    ax.axhline(y=0, color="black", linestyle="--")
    ax.axhline(y=0.5, color="black", linestyle=":")
    ax.axhline(y=1.0, color="black", linestyle="--")
    ax.axvline(color="grey")
    ax.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))
    ax.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
    ax.set(xlim=(-10, 10), xlabel="t")
    ax.legend(fontsize=14)
    mo.as_html(ax)
    #plt.show()
    return


if __name__ == "__main__":
    app.run()
