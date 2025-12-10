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
def _(mandelbrot_vectorized):
    # Параметры для более детального изображения
    width, height = 1000, 1000
    x_min, x_max = -2.0, 0.5
    y_min, y_max = -1.25, 1.25
    max_iter = 50
    mandelbrot_set = mandelbrot_vectorized(width, height, x_min, x_max, y_min, y_max, max_iter)
    return height, mandelbrot_set, max_iter, width, x_max, x_min, y_max, y_min


@app.cell
def _(mandelbrot_set, mo, plt, x_max, x_min, y_max, y_min):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.subplots()
    ax.imshow(mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap='hot')
    ax.set_title('Мандельброт. Цветовая схема: hot')
    #ax.colorbar()
    mo.as_html(ax)
    return (fig,)


@app.cell
def _(np):
    def mandelbrot(c, max_iter):
        """
        Вычисляет количество итераций для точки c до расхождения
        """
        z = 0
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return max_iter
    
    def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
        """
        Генерирует массив значений для множества Мандельброта
        """
        # Создаем сетку комплексных чисел
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        mandelbrot_set = np.zeros((height, width))
    
        # Вычисляем значение для каждой точки
        for i in range(height):
            for j in range(width):
                mandelbrot_set[i, j] = mandelbrot(x[j] + 1j*y[i], max_iter)
    
        return mandelbrot_set
    return (generate_mandelbrot,)


@app.cell
def _(
    generate_mandelbrot,
    height,
    max_iter,
    width,
    x_max,
    x_min,
    y_max,
    y_min,
):
    mandelbrot_set2 = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    return (mandelbrot_set2,)


@app.cell
def _(fig, mandelbrot_set2, mo, plt, x_max, x_min, y_max, y_min):
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig.subplots()
    ax2.imshow(mandelbrot_set2, extent=[x_min, x_max, y_min, y_max], cmap='hot')
    ax2.set_title('Мандельброт. Цветовая схема: hot')
    #ax.colorbar()
    mo.as_html(ax2)
    return


if __name__ == "__main__":
    app.run()
