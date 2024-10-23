# You work at a low latency trading firm and are asked to deliver the order book data provided in order_book_data.txt to a superior
# The problem is that the data isn't formatted correctly. Please complete the following steps to apropriately format the data
# Notice, the first column is a ticker, the second column is a date, the third column is a Bid, the fourth column is an Ask, and the fifth column is a currency type
# 1. Open order_book_data.txt
# 2. Remove the order book lines. i.e. ***** Order Book: ###### *****
# 3. Get rid empty lines
# 4. Get rid of spaces
# 5. Notice that there are two currencies in the order book; USD and YEN. Please convert both the Bid and Ask price to USD (if not already)
# The Bid and Ask are the 3rd and 4th column, respectively
# 6. Create a header line Ticker, Date, Bid, Ask
# 7. Save the header line and properly formatted lines to a comma seperated value file called mktDataFormat.csv
import csv

remove = '******************** Order Book: ###0010 ********************'
data = []
bid = 2
ask = 3
currency = 4
precision = 4
with open('order_book_data.txt', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    for line in reader:
        clean_row = [cell.strip() for cell in line]
        if not any(cell.strip() for cell in line):
            continue
        if "*" in ''.join(clean_row):
            continue
        if len(clean_row) > currency:
            # Check if the value in column 5 is 'YEN'
            if clean_row[currency] == 'YEN':
                try:
                    # Multiply columns 3 and 4 by 0.007
                    clean_row[bid] = str(round(float(clean_row[bid]) * 0.007, precision))
                    clean_row[ask] = str(round(float(clean_row[ask]) * 0.007, precision))
                except ValueError:
                    # Handle cases where the values in columns 3 and 4 are not numbers
                    print(f"Error converting values in row: {clean_row}")
                    continue
        data.append(clean_row[:currency])

with open('mktDataFormat.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    header = ['Ticker', 'Date', 'Bid', 'Ask']
    writer.writerow(header)
    writer.writerows(data)
