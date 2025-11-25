import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import math as math
    return (math,)


@app.cell
def _(math):
    math.sin(math.pi/2)
    return


if __name__ == "__main__":
    app.run()
