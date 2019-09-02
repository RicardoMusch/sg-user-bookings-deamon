"Script to check if users should be activated or disabled."
"Can be run on the renderfarm or as scheduled task (for example: every night at 00:01)"


from datetime import tzinfo, timedelta, datetime

fields = ["sg_status_list", "locked_until", "bookings", "name"]
filters = []
people = shotgun.find("HumanUser",filters,fields)


"Check the 'Locked until' Field"
for u in people:
    if u.get("locked_until") != None:
        start_date = u.get("locked_until")

        "Get Locked Until Timezone"
        tz_info = start_date.tzinfo

        "If It's time, Make Account Active"
        if datetime.now(tz_info) > start_date:
            data = {'sg_status_list': 'act'}
            result = shotgun.update('HumanUser', u.get("id"), data)


"Check for Bookings"
for u in people:
    if u.get("locked_until") != None:
        start_date = u.get("locked_until")

        "Get Locked Until Timezone"
        tz_info = start_date.tzinfo

        "If It's time, Make Account Active"
        if datetime.now(tz_info) > start_date:
            data = {'sg_status_list': 'act'}
            result = shotgun.update('HumanUser', u.get("id"), data)