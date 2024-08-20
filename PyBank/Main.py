{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b5dc42de-c343-433a-83e5-00bb3c030a77",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import the necessary libraries\n",
    "import os\n",
    "import csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ed1ebb32-ca4e-4a0f-af67-2ec5781356aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create an object out of the CSV file\n",
    "csvfile = os.path.join(\"Resources\",\"budget_data.csv\")\n",
    "\n",
    "csvreader = csv.reader(csvfile)\n",
    "header = next(csvreader)\n",
    "\n",
    "total_months = 0\n",
    "total_profit = 0\n",
    "prev_profit = 0\n",
    "max_profit_month = \"\"\n",
    "min_profit_month = \"\"\n",
    "max_profit = float('-inf')\n",
    "min_profit = float('inf')\n",
    "total_profit_change = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "22863bba-844b-4dce-a15c-97c6ceeced6f",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (3340819902.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[12], line 2\u001b[1;36m\u001b[0m\n\u001b[1;33m    for row in csvreader:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# Read through each row in the CSV file\n",
    "    for row in csvreader:\n",
    "        total_months += 1\n",
    "        total_profit += int(row[1])\n",
    "\n",
    "        # Calculate the change in profit from the previous month\n",
    "        profit_change = int(row[1]) - prev_profit\n",
    "        prev_profit = int(row[1])\n",
    "\n",
    "        # Update max and min profit and corresponding month\n",
    "        if profit_change > max_profit:\n",
    "            max_profit = profit_change\n",
    "            max_profit_month = row[0]\n",
    "\n",
    "        elif profit_change < min_profit:\n",
    "            min_profit = profit_change\n",
    "            min_profit_month = row[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "899a4d4b-fdde-4fba-a34d-2fe91c53a780",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (4277322238.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[13], line 2\u001b[1;36m\u001b[0m\n\u001b[1;33m    total_profit_change += profit_change\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# Calculating the total profit change\n",
    "        total_profit_change += profit_change\n",
    "            \n",
    "        # Calculating the average profit change\n",
    "        if total_months > 1:\n",
    "            avg_profit_change = total_profit_change / (total_months -1)\n",
    "            avg_profit_change = round(avg_profit_change, 2)\n",
    "        else:\n",
    "            avg_profit_change = 0\n",
    "\n",
    "        # Calculating the total net profit\n",
    "        net_profit = total_profit\n",
    "        net_profit = round(net_profit, 2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2120810e-9469-4bfc-bdc4-7f1ff0839bf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Total number of months\n",
    "        total_months += 1\n",
    "\n",
    "        #Total net amount of \"Profit/Losses over entire period\"\n",
    "        total_pl = total_pl + int(row[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "50e9ecf0-82b3-42b3-8ba6-b82963220318",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (2287950826.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[14], line 2\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(f\"Financial Analysis\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# Print results\n",
    "    print(f\"Financial Analysis\")\n",
    "    print(\"----------------------------\")\n",
    "    print(f\"Total Months: {total_months}\")\n",
    "    print(f\"Total: ${total_profit}\")\n",
    "    print(f\"Average Change: ${avg_profit_change}\")\n",
    "    print(f\"Greatest Increase in Profits: {max_profit_month} (${max_profit})\")\n",
    "    print(f\"Greatest Decrease in Profits: {min_profit_month} (${min_profit})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "820f0e7a-a066-4e74-8581-4eb83ef1db2e",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'Analysis/financial_analysis.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[15], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mAnalysis/financial_analysis.txt\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mw\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m output_file:\n\u001b[0;32m      2\u001b[0m     output_file\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFinancial Analysis\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m     output_file\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m----------------------------\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda\\anaconda3\\envs\\dev\\lib\\site-packages\\IPython\\core\\interactiveshell.py:310\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    303\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    304\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    305\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    306\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    307\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    308\u001b[0m     )\n\u001b[1;32m--> 310\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Analysis/financial_analysis.txt'"
     ]
    }
   ],
   "source": [
    "with open('Analysis/financial_analysis.txt', 'w') as output_file:\n",
    "    output_file.write(\"Financial Analysis\\n\")\n",
    "    output_file.write(\"----------------------------\\n\")\n",
    "    output_file.write(f\"Total Months: {total_months}\\n\")\n",
    "    output_file.write(f\"Total: ${total_profit}\\n\")\n",
    "    output_file.write(f\"Average Change: ${avg_profit_change:.2f}\\n\")\n",
    "    output_file.write(f\"Greatest Increase in Profits: {max_profit_month} ${max_profit}\\n\")\n",
    "    output_file.write(f\"Greatest Decrease in Profits: {min_profit_month} ${min_profit}\\n\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00d3c37f-0a87-45a5-b9e2-0be6c092c077",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
