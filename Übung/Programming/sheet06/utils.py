import numpy
import matplotlib.pyplot as plt

# the colors of the lecture: a model learned from data is blue, its
# uncertainty a light blue band, the test data gray
FIT = (.12, .32, .75)
BAND = (.82, .86, .95)
TEST = '0.6'

# the inputs of the cars are rescaled with these two numbers (see cars())
HP_CENTER, HP_SCALE = 138.0, 92.0
HP_GRID = numpy.linspace(40, 236, 197)


def gaussian_kernel(X1, X2, s):
    # kernel matrix of shape (N1, N2) with the entries
    # k(x, x') = exp(-||x - x'||^2 / (2 s^2))
    # for the rows x of X1 (shape (N1, d)) and the rows x' of X2 (shape (N2, d))
    sq = (X1 ** 2).sum(axis=1)[:, None] + (X2 ** 2).sum(axis=1)[None, :] - 2 * X1 @ X2.T
    return numpy.exp(-numpy.maximum(sq, 0) / (2 * s ** 2))


def polynomial_features(x, p):
    # the powers x, x^2, ..., x^p of the numbers x (shape (N,)) as the
    # columns of an array of shape (N, p)
    return numpy.stack([x ** j for j in range(1, p + 1)], axis=1)


def cars():
    """The cars of the lecture (Auto MPG data, UCI Machine Learning
    Repository): horsepower and miles per gallon of the 20 training cars and
    of the 372 test cars, as (hp_train, mpg_train, hp_test, mpg_test)."""
    hp, mpg = numpy.loadtxt('auto_mpg.csv', delimiter=',', skiprows=1).T
    train = numpy.random.default_rng(28885).choice(len(hp), 20, replace=False)
    test = numpy.setdiff1d(numpy.arange(len(hp)), train)
    return hp[train], mpg[train], hp[test], mpg[test]


def plot_cars(ax, hp_train, mpg_train, hp_test=None, mpg_test=None, title=None):
    """The training cars (black) and, if given, the test cars (gray)."""
    if hp_test is not None:
        ax.plot(hp_test, mpg_test, 'o', ms=2.5, color=TEST, zorder=1)
    ax.plot(hp_train, mpg_train, 'o', ms=5, color='k', mec='w', mew=.8, zorder=4)
    ax.set_xlim(40, 236)
    ax.set_ylim(0, 50)
    ax.set_xlabel('horsepower')
    ax.set_ylabel('miles per gallon')
    if title:
        ax.set_title(title, fontsize=10)


def plot_band(ax, mean, std):
    """A prediction over HP_GRID with the band mean +- 2 std."""
    ax.fill_between(HP_GRID, mean - 2 * std, mean + 2 * std, color=BAND, lw=0, zorder=0)
    ax.plot(HP_GRID, mean, color=FIT, lw=1.8, zorder=3)
