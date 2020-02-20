{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4075\n"
     ]
    }
   ],
   "source": [
    "# import factorial function as f\n",
    "from math import factorial as f\n",
    "\n",
    "# counter to count the number of instances\n",
    "counter = 0\n",
    "\n",
    "def combi(n, r):\n",
    "    #a function to find the combinatoric\n",
    "    return f(n)/(f(r)*f(n-r))\n",
    "\n",
    "# for loops\n",
    "for n in range(23, 101):\n",
    "    for r in range(4, n-3):\n",
    "        if combi(n, r) > 1000000:\n",
    "            counter += 1\n",
    "\n",
    "# printing the number of instances\n",
    "print (counter)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
