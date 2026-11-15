# Doing this in Excel would be easier for smaller types of data because youre able to see and edit everything directly. Python is better for automating repetitive tasks and working with larger amouunts of data without having to do everything.
# A Business could use an append-mode log to keep track of daily sales. Append mode is useful because it adds new information without deleting previous records, allowing the business to look back at past sales.



import csv

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"

# Exercise 2

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    for row in reader:
        print(row)

# Exercise 4

total_revenue = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

        total_revenue += total

print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)
   
print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

# Exercise 6

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

# Exercise 7
summary ={}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product, total in (summary.items()):
    print(f"{product}: ${total:.2f}")

# Exercise 8

from datetime import datetime
LOG_FILE = "data/run_log.txt"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp}: Processed {rows_read} rows, wrote {len(high_value)} high-value rows to {CLEANED_FILE}.\n")
            
entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())
        
print(f"Total log entries: {entries}")