{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOBlrcfyTXYmXQbzPwOr1xg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lukaszplust/Lovely_Python/blob/main/%C4%87wiczenia.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex 1"
      ],
      "metadata": {
        "id": "36Bzzx7xLZCZ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JwbRPHEKLYUd",
        "outputId": "5c6a66d4-55bb-49dc-b77d-0b43c626fac2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1580"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ],
      "source": [
        "def calculate():\n",
        "  suma = []\n",
        "  for x in range(100):\n",
        "    if x % 5 == 0 or x % 7 ==0:\n",
        "      suma.append(x)\n",
        "  wynik = sum(suma)\n",
        "  return wynik    \n",
        "calculate()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wfUb2yvUMjZd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}