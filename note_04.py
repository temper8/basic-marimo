import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(np):
    def mandelbrot_vectorized(width, height, x_min, x_max, y_min, y_max, max_iter):
        """
        Векторизованная версия для более быстрого вычисления
        """
        # Создаем сетку комплексных чисел
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        c = x + 1j * y[:, None]

        # Инициализируем массив z
        z = np.zeros_like(c)
        mandelbrot_set = np.zeros(c.shape, dtype=int)

        # Векторизованное вычисление
        for i in range(max_iter):
            mask = np.abs(z) <= 2
            z[mask] = z[mask]**2 + c[mask]
            mandelbrot_set[mask] = i

        return mandelbrot_set
    return (mandelbrot_vectorized,)


@app.cell
def _(mo):
    x_slider = mo.ui.range_slider(
        start=-2.0, stop=0.5, step=0.05, 
        value=[-2.0, 0.5], full_width=True, label="x")

    y_slider = mo.ui.range_slider(
        start=-1.25, stop=1.25, step=0.05,
        value=[-1.25, 1.25], full_width=True,label="y")
    return x_slider, y_slider


@app.cell
def _(mo, x_slider, y_slider):
    mo.vstack([x_slider, y_slider])
    return


@app.cell
def _(mandelbrot_vectorized, x_slider, y_slider):
    # Параметры для более детального изображения
    width, height = 1000, 1000
    x_min, x_max = x_slider.value
    y_min, y_max = y_slider.value
    #x_min, x_max = -2.0, 0.5
    #y_min, y_max = -1.25, 1.25
    max_iter = 50
    mandelbrot_set = mandelbrot_vectorized(width, height, x_min, x_max, y_min, y_max, max_iter)
    return mandelbrot_set, x_max, x_min, y_max, y_min


@app.cell
def _(mandelbrot_set, mo, plt, x_max, x_min, y_max, y_min):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.subplots()
    ax.imshow(mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap='hot')
    ax.set_title('Манделььброт. Цветовая схема: hot')
    #ax.colorbar()
    mo.as_html(ax)
    return


if __name__ == "__main__":
    app.run()
