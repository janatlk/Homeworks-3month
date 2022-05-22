def time(sec):
    if 0 > sec or sec > 359999:
        return "num is incorrect"
    hour=sec//60//60
    minute=sec//60-hour*60
    seconds=sec-minute*60-hour*60*60
    # return f"{hour}:{minute}:{seconds}" if hour > 9 or minute > 9 or seconds > 9 else f"0{hour}:0{minute}:0{seconds}"
    return f"{hour}:0{minute}:0{seconds}" if hour>9 and minute<10 and seconds<10 else f"0{hour}:{minute}:0{seconds}" if minute>9 and hour<10 and seconds<10 else f"0{hour}:0{minute}:{seconds}" if seconds>9 and minute<10 and hour<10 else f"{hour}:{minute}:{seconds}" if hour>10 and minute>10 and seconds>10 else f"{hour}:{minute}:0{seconds}" if hour>9 and minute>9 and seconds<10 else f"0{hour}:{minute}:{seconds}" if hour<10 and minute>9 and seconds>9 else f"{hour}:0{minute}:{seconds}" if hour>9 and minute<10 and seconds>9 else f"0{hour}:0{minute}:0{seconds}" if hour<10 and minute<10 and seconds<10 else f"{hour}:{minute}:{seconds}"

print(time())


print('hour-minute-sec')