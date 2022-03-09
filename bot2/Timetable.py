def AM_TIME():
    return "08:20:00"  # 조례 시간


# 해당 교시 1~6교시 까지
def All_TIME(i):
    period = ["08:40:00", "09:40:00", "10:40:00", "11:40:00", "13:20:00", "14:20:00", "15:25:00"]  # 1교시부터 7교시까지
    return period[i]


# 시간표 끝 (종례)
def PM_TIME(state):  # 종례 시간
    if state == "default":
        return "14:15:00"
    elif state == "friday":
        return "15:05:00"


# 공휴일, 재량휴업일
def PUBLIC_HOLIDAY(i):
    holiday = []
    return holiday[i]