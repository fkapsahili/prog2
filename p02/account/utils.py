from datetime import datetime

# calculate the current age based on the birthday
# => return the age as an integer
def calculate_age(birth_date):
    return int((datetime.now() - birth_date).total_seconds() // 31536000)
