{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNhkkSPgJQp2QCDA1O/gMrF",
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
        "<a href=\"https://colab.research.google.com/github/Whyoblomovisme/barname-nevisi/blob/main/Class%20circle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "OFQSfNtApWFd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import math\n",
        "class circle():\n",
        "    pi=math.pi\n",
        "    def __init__ (self, r=5):\n",
        "        self.rad = r\n",
        "        print(\"circle created\")\n",
        "    def perim(self):\n",
        "        return 2*pi*self.rad\n",
        "    def Area(self):\n",
        "        return p*r*r\n",
        "    def __del__ (self):\n",
        "        print(\"circle deleted\")\n",
        "        return -1\n",
        "K = circle(10) #یک آبجکت به اندازه 10 وارد کلاس دایره میکند\n",
        "print(K.Area)\n",
        "print(K.perim)\n",
        "print(K.pi)\n",
        "del K\n",
        "#circle created\n",
        "#314\n",
        "#62.8\n",
        "#3.14\n",
        "#circle deleted"
      ],
      "metadata": {
        "id": "KcFTLCmSD5ps",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b6070a8d-a53c-4938-bd67-6052b079c73c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "circle created\n",
            "<bound method circle.Area of <__main__.circle object at 0x7a4d027390f0>>\n",
            "<bound method circle.perim of <__main__.circle object at 0x7a4d027390f0>>\n",
            "3.141592653589793\n",
            "circle deleted\n"
          ]
        }
      ]
    }
  ]
}