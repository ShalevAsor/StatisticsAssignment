import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_estimator(p, n):
    """
    This method return the samples estimator
    :param p: probability of success
    :param n: number of samples
    :return: the mean a.k.a the estimator
    """
    # set X~bin(n,p) - n random variable X_i ~ Ber(p) equivalent to X
    X = np.random.binomial(1, p, n)
    # get the estimator
    Pn = np.sum(X) / n

    return Pn


def plot_simulation(p, samples):
    """
    This method simulate the learning process and plot the results graph
    :param p: probability of success
    :param samples: array of samples , for example 200,400,600,...,5000
    """
    errors = []
    for n in samples:
        estimator = get_estimator(p, n)
        error = np.mean(np.abs(estimator - p))
        errors.append(error)

    plt.plot(samples, errors)
    plt.ylabel("|Pn - p| - the error")
    plt.xlabel("n - number of samples")
    plt.title('error of estimation | Samples \n p={:.3f}'.format(pr))
    plt.show()


def plot_histogram(p, n):
    """
    This method plots a histogram of the errors in estimating of n samples repeating constants times
    :param p: probability of success
    :param n: amount of samples
    """
    # set all the Pn values (estimators) 1000 times
    Pn_array = [get_estimator(p, n) for i in range(1000)]
    # add all the errors to the array
    errors = np.array(Pn_array) - p
    # plot the results histogram
    plt.hist(errors, bins=20, density=True, alpha=0.5, color='green', edgecolor='black')
    # set and plot the Normal distribution
    mu, std = norm.fit(errors)
    x = np.linspace(errors.min(), errors.max(), 100)
    y = norm.pdf(x, loc=mu, scale=std)
    # plot the histogram
    plt.plot(x, y, color='blue', linestyle='--', linewidth=2)
    plt.ylabel("Density")
    plt.xlabel("Pn - p")
    plt.title(f'Histogram of Pn - p \n n = {n} | p={pr:.3f}')
    plt.show()


# choose random probability of success
pr = random.uniform(0, 1)
# set array of n values 200,400,...,5000
n_values = range(200, 5001, 200)
# plot the simulation graph
plot_simulation(pr, n_values)
# plot the histogram for n = 200
plot_histogram(pr, 200)
# plot the histogram for n = 500
plot_histogram(pr, 5000)
