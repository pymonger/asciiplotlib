# -*- coding: utf-8 -*-
#
import numpy

import asciiplotlib as apl


def test_plot():
    x = numpy.linspace(0, 2 * numpy.pi, 10)
    y = numpy.sin(x)

    fig = apl.figure()
    fig.plot(x, y, label="data", width=50, height=15)
    string = fig.get_string()

    ref = """    1 +---------------------------------------+
  0.8 |    **     **                          |
  0.6 |   *         **           data ******* |
  0.4 | **                                    |
  0.2 |*              **                      |
    0 |                 **                    |
      |                                   *   |
 -0.2 |                   **            **    |
 -0.4 |                     **         *      |
 -0.6 |                              **       |
 -0.8 |                       **** **         |
   -1 +---------------------------------------+
      0     1    2     3     4     5    6     7"""

    assert string == ref
    return


def test_nolabel():
    x = numpy.linspace(0, 2 * numpy.pi, 10)
    y = numpy.sin(x)

    fig = apl.figure()
    fig.plot(x, y, width=50, height=15)
    string = fig.get_string()

    ref = """    1 +---------------------------------------+
  0.8 |    **     **                          |
  0.6 |   *         **                        |
  0.4 | **                                    |
  0.2 |*              **                      |
    0 |                 **                    |
      |                                   *   |
 -0.2 |                   **            **    |
 -0.4 |                     **         *      |
 -0.6 |                              **       |
 -0.8 |                       **** **         |
   -1 +---------------------------------------+
      0     1    2     3     4     5    6     7"""

    assert string == ref
    return


def test_plot_lim():
    x = numpy.linspace(0, 2 * numpy.pi, 10)
    y = numpy.sin(x)

    fig = apl.figure()
    fig.plot(
        x,
        y,
        label="data",
        width=50,
        height=15,
        xlim=[-1, 1],
        ylim=[-1, 1],
        xlabel="x vals",
        title="header",
    )
    string = fig.get_string()

    ref = """                       header

    1 +---------------------------------------+
      |                               ********|
  0.5 |                          ************ |
      |                      ****             |
    0 |                   ***                 |
      |                                       |
 -0.5 |                                       |
      |                                       |
   -1 +---------------------------------------+
     -1       -0.5        0        0.5        1
                       x vals"""

    assert string == ref
    return
