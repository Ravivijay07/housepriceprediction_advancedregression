{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5d760482",
   "metadata": {},
   "source": [
    "# Lending Club Case Study"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52459f0e",
   "metadata": {},
   "source": [
    "Lending Club is a finance company which specialises in lending various types of loans to urban customers. When the company receives a loan application, the company has to make a decision for loan approval based on the applicant’s profile. Two types of risks are associated with the bank’s decision:\n",
    "\n",
    "1.If the applicant is likely to repay the loan, then not approving the loan results in a loss of business to the company\n",
    "\n",
    "2.If the applicant is not likely to repay the loan, i.e. he/she is likely to default, then approving the loan may lead to a financial loss for the company"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81c34742",
   "metadata": {},
   "source": [
    "# Table of Contents"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b56ea04b",
   "metadata": {},
   "source": [
    "\n",
    "* [General Info](#general-information)\n",
    "* [Conclusions](#conclusions)\n",
    "* [Technologies Used](#technologies-used)\n",
    "* [Acknowledgements](#acknowledgements)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9c153bb",
   "metadata": {},
   "source": [
    "## General Information"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de51090f",
   "metadata": {},
   "outputs": [],
   "source": [
    "Provide general information about your project here.\n",
    "- What is the background of your project?\n",
    "- What is the business probem that your project is trying to solve?\n",
    "- What is the dataset that is being used?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6110be8",
   "metadata": {},
   "source": [
    "**Project Background**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24cbf52e",
   "metadata": {},
   "source": [
    "This company is the largest online loan marketplace, facilitating personal loans, business loans, and financing of medical procedures. Borrowers can easily access lower interest rate loans through a fast online interface. \n",
    "\n",
    " \n",
    "\n",
    "Like most other lending companies, lending loans to ‘risky’ applicants is the largest source of financial loss (called credit loss). Credit loss is the amount of money lost by the lender when the borrower refuses to pay or runs away with the money owed. In other words, borrowers who default cause the largest amount of loss to the lenders. In this case, the customers labelled as 'charged-off' are the 'defaulters'. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "93ffd2ca",
   "metadata": {},
   "source": [
    "**Business problem**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ca49931",
   "metadata": {},
   "source": [
    "If one is able to identify these risky loan applicants, then such loans can be reduced thereby cutting down the amount of credit loss. Identification of such applicants using EDA is the aim of this case study.\n",
    "\n",
    " \n",
    "\n",
    "In other words, the company wants to understand the driving factors (or driver variables) behind loan default, i.e. the variables which are strong indicators of default.  The company can utilise this knowledge for its portfolio and risk assessment. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab8c2427",
   "metadata": {},
   "source": [
    "**Dataset**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b8b5d03",
   "metadata": {},
   "source": [
    "Loan Data Set: It contains the complete loan data for all loans issued through the time period 2007 to 2011."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42971625",
   "metadata": {},
   "source": [
    "# Conclusions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "caab418f",
   "metadata": {},
   "source": [
    "Factor whether an applicant will be Defaulter:\n",
    "\n",
    "Continuous Variable:\n",
    "1. LOAN_AMOUNT : Loan amount greater than 15000 dollors have higher default rate\n",
    "2. FUNDED_AMOUNT : Funded amount greater than 15000 dollors have higher default rate\n",
    "3. FUNDED_AMOUNT_INVESTED : Funded amount invested greater than 15000 dollors have higher default rate\n",
    "4. INTEREST_RATE : As Interest rate increases the default rate increases steeply\n",
    "5. ANNUAL_INCOME : As the annual income increase the default rate decreases\n",
    "6. DTI : As dti increase the default rate increases\n",
    "\n",
    "Categorical Variable:\n",
    "1. TERM : 60 months term have a higher default rate than 36 months term\n",
    "2. GRADE : As the Grade decreases (A B C D E F G) default rate increases\n",
    "3. SUB_GRADE : As the Sub Grade decreases (A1 A2 B1 B2.....) default rate increases\n",
    "4. VERIFICATION STATUS : Percent of loan defaulted is higher for verifed borrowers\n",
    "5. PURPOSE : Small business borrowers have high default rate\n",
    "\n",
    "Decisive Factor whether an applicant will be Defaulter:\n",
    "    \n",
    "- FUNDED_AMOUNT_INVESTED\n",
    "- INTEREST_RATE\n",
    "- ANNUAL_INCOME\n",
    "- DTI\n",
    "- TERM\n",
    "- GRADE\n",
    "- SUB_GRADE\n",
    "- PURPOSE"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a4b234c",
   "metadata": {},
   "source": [
    "# Technologies Used"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41463a10",
   "metadata": {},
   "source": [
    "- pandas - 1.3.4\n",
    "- numpy - 1.20.3\n",
    "- matplotlib - 3.4.3\n",
    "- seaborn - 0.11.2\n",
    "- plotly - 5.8.0"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6c9a123",
   "metadata": {},
   "source": [
    "# Acknowledgements"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac7c4f33",
   "metadata": {},
   "source": [
    "Give credit here.\n",
    "\n",
    "This project was group case study for an online advance course.\n",
    "- https://www.geeksforgeeks.org/\n",
    "- https://seaborn.pydata.org/\n",
    "- https://plotly.com/\n",
    "- https://pandas.pydata.org/\n",
    "- https://learn.upgrad.com/"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1d0652b",
   "metadata": {},
   "source": [
    "# Contact"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62f73b7d",
   "metadata": {},
   "source": [
    "Created by [@ravivijay07] - feel free to contact me!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
