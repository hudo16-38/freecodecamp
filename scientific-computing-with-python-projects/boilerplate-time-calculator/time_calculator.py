def add_time(start: str, duration: str, date: str | None=None):
    days = "Monday-Tuesday-Wednesday-Thursday-Friday-Saturday-Sunday".split("-")
    
    day = date.lower().capitalize() if date is not None else "Monday"
    day_index = days.index(day)

    time, day_part = start.split()
    h, m = map(int, time.split(":"))
    if day_part == "PM":
        h += 12

    dh, dm = map(int, duration.split(":"))

    res_m = (m + dm)
    res_h = (h + dh + res_m//60)
    index = day_index + res_h//24
    res_d = days[index%7]
    res_part = "PM" if res_h%24 >= 12 else "AM"

    additional_data = None
    if res_h > 24:
        diff = res_h // 24
        if diff == 1:
            additional_data = "(next day)"
        else:
            additional_data = f"({diff} days later)"
    res_h %= 12
    if res_h == 0: res_h += 12
    res_m %= 60

    new_time = f"{res_h}:{(res_m):>02} {res_part}"
    if date is not None:
        new_time += f", {res_d}"

    if additional_data is not None:
        new_time += f" {additional_data}"

    return new_time

if __name__ == "__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))