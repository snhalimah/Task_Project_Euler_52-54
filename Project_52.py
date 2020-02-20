{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "142857\n"
     ]
    }
   ],
   "source": [
    "# while loop iterator\n",
    "i = 1\n",
    "\n",
    "# while loop\n",
    "while True:\n",
    "    if set(str(i)) == set(str(6*i)):\n",
    "        if set(str(i)) == set(str(5*i)):\n",
    "            if set(str(i)) == set(str(4*i)):\n",
    "                if set(str(i)) == set(str(3*i)):\n",
    "                    if set(str(i)) == set(str(2*i)):\n",
    "                        print (i)\n",
    "                        break\n",
    "    i += 1"
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
