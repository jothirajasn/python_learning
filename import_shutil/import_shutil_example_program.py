import shutil

try:
    print ("Processing file...")

    shutil.move("incoming/customer.csv", "processed/customer.csv")

    print("File processed successfully")

except Exception:

    shutil.move("incoming/customer.csv", "failed/customer.csv")

    print("File processing failed")