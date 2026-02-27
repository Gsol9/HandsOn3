{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27fed448-e09b-4966-a9c1-47c624b91ff4",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"Sales tax module for HandsOn 3 (4.3).\"\"\"\n",
    "\n",
    "SALES_TAX_RATE = 0.06\n",
    "\n",
    "def calculate_sales_tax(total: float) -> float:\n",
    "    return round(total * SALES_TAX_RATE, 2)\n",
    "\n",
    "def total_after_tax(total: float) -> float:\n",
    "    return round(total + calculate_sales_tax(total), 2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
