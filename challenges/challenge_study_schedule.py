def study_schedule(permanence_period, target_time):
    try:
        sum = 0
        for checkin, checkout in permanence_period:
            if checkin <= target_time <= checkout:
                sum += 1
        return sum
    except TypeError:
        return None
