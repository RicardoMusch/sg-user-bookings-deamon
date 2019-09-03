"Script to check if users should be activated or disabled."
"Can be run on the renderfarm or as scheduled task (for example: every night at 00:01)"


from datetime import tzinfo, timedelta, datetime
current_date = datetime.today().strftime('%Y-%m-%d')
#print "Current Date:", current_date

"Find all Users"
fields = ["sg_status_list", "locked_until", "bookings", "name"]
filters = [ ["locked_until", "is_not", None] ]
people = shotgun.find("HumanUser",filters,fields)


"Check the 'Locked until' Field"
for u in people:
    start_date = u.get("locked_until")

    "Get Locked Until Timezone"
    tz_info = start_date.tzinfo

    "If It's time, Make Account Active"
    if datetime.now(tz_info) > start_date:
        data = {'sg_status_list': 'act'}
        result = shotgun.update('HumanUser', u.get("id"), data)
        print "Setting", str(u.get("name")), "to Active because of the 'locked_until' date" 


"Check for Bookings"
fields = ["user", "start_date", "end_date"]
filters = []
bookings = shotgun.find("Booking",filters,fields)

for b in bookings:
#    print b.get("user")

    "If start date is in the future or end date has passed"
    if b.get("start_date") > current_date or b.get("end_date") < current_date:
#        print b
        data = {'sg_status_list': 'dis'}
#        result = shotgun.update('HumanUser', b.get("user").get("id"), data)
        try:
            print "Deactivating", str(b.get("user").get("name")), "because a booking has expired:", str(b.get("start_date")), "-", str(b.get("end_date"))
        except:
            pass



    if b.get("start_date") < current_date and b.get("end_date") > current_date:
        data = {'sg_status_list': 'act'}
#        result = shotgun.update('HumanUser', b.get("user").get("id"), data)
        print "Setting", str(b.get("user").get("name")), "to Active because an active booking has been found with a start date of:", str(b.get("start_date")), "and a end date of:", str(b.get("end_date")) 